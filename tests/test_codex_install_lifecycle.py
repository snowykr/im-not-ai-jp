from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
INSTALL_FIXTURE_PATHS = (
    ".agents/plugins/marketplace.json",
    ".claude/skills/humanize-japanese",
    "legacy/upstream-korean/agents",
    "plugins/im-not-ai-codex",
    "install.sh",
    "uninstall.sh",
)


def _copy_install_fixture(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    for relative in INSTALL_FIXTURE_PATHS:
        source = ROOT / relative
        target = repo / relative
        if source.is_dir():
            shutil.copytree(source, target)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return repo


def _env_without_codex(codex_home: Path) -> dict[str, str]:
    return os.environ | {
        "CODEX_HOME": str(codex_home),
        "PATH": "/usr/bin:/bin",
    }


def test_codex_only_installs_without_codex_binary(tmp_path: Path) -> None:
    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    installed = codex_home / "skills" / "humanize-japanese"

    subprocess.run(
        ["bash", "install.sh", "--codex-only"],
        cwd=repo,
        env=_env_without_codex(codex_home),
        check=True,
    )

    assert installed.is_symlink()
    assert (
        installed.readlink()
        == repo / "plugins" / "im-not-ai-codex" / "skills" / "humanize-japanese"
    )


def test_codex_auto_detects_existing_home_without_codex_binary(
    tmp_path: Path,
) -> None:
    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    codex_home.mkdir()
    installed = codex_home / "skills" / "humanize-japanese"

    subprocess.run(
        ["bash", "install.sh"],
        cwd=repo,
        env=_env_without_codex(codex_home),
        check=True,
    )

    assert installed.is_symlink()
    assert (
        installed.readlink()
        == repo / "plugins" / "im-not-ai-codex" / "skills" / "humanize-japanese"
    )


def test_codex_uninstall_removes_packaged_plugin_symlink(tmp_path: Path) -> None:
    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    installed = codex_home / "skills" / "humanize-japanese"
    env = _env_without_codex(codex_home)

    subprocess.run(["bash", "install.sh", "--codex-only"], cwd=repo, env=env, check=True)
    subprocess.run(["bash", "uninstall.sh"], cwd=repo, env=env, check=True)

    assert not installed.exists()


def test_uninstall_removes_legacy_claude_agent_symlinks(tmp_path: Path) -> None:
    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    claude_home = tmp_path / "claude-home"
    agents_home = claude_home / "agents"
    agents_home.mkdir(parents=True)
    env = _env_without_codex(codex_home) | {"CLAUDE_HOME": str(claude_home)}
    old_agent = agents_home / "ai-tell-detector.md"
    moved_agent = agents_home / "naturalness-reviewer.md"

    old_agent.symlink_to(repo / "agents" / "ai-tell-detector.md")
    moved_agent.symlink_to(
        repo / "legacy" / "upstream-korean" / "agents" / "naturalness-reviewer.md"
    )

    subprocess.run(["bash", "uninstall.sh"], cwd=repo, env=env, check=True)

    assert not old_agent.exists()
    assert not old_agent.is_symlink()
    assert not moved_agent.exists()
    assert not moved_agent.is_symlink()


def test_uninstall_preserves_unmanaged_claude_agent_entries(tmp_path: Path) -> None:
    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    claude_home = tmp_path / "claude-home"
    agents_home = claude_home / "agents"
    unmanaged_target = tmp_path / "user-agents" / "naturalness-reviewer.md"
    agents_home.mkdir(parents=True)
    unmanaged_target.parent.mkdir()
    unmanaged_target.write_text("user-managed agent\n", encoding="utf-8")
    env = _env_without_codex(codex_home) | {"CLAUDE_HOME": str(claude_home)}
    unmanaged_file = agents_home / "ai-tell-detector.md"
    unmanaged_symlink = agents_home / "naturalness-reviewer.md"

    unmanaged_file.write_text("do not remove\n", encoding="utf-8")
    unmanaged_symlink.symlink_to(unmanaged_target)

    subprocess.run(["bash", "uninstall.sh"], cwd=repo, env=env, check=True)

    assert unmanaged_file.read_text(encoding="utf-8") == "do not remove\n"
    assert unmanaged_symlink.is_symlink()
    assert unmanaged_symlink.readlink() == unmanaged_target


def test_codex_uninstall_removes_native_plugin_install(tmp_path: Path) -> None:
    codex = shutil.which("codex")
    if codex is None:
        pytest.skip("codex CLI is required for native plugin lifecycle coverage")

    repo = _copy_install_fixture(tmp_path)
    codex_home = tmp_path / "codex-home"
    codex_home.mkdir()
    env = os.environ | {"CODEX_HOME": str(codex_home)}

    subprocess.run(
        [codex, "plugin", "marketplace", "add", ".", "--json"],
        cwd=repo,
        env=env,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    subprocess.run(
        [codex, "plugin", "add", "im-not-ai-codex@im-not-ai-jp", "--json"],
        cwd=repo,
        env=env,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )

    subprocess.run(["bash", "uninstall.sh"], cwd=repo, env=env, check=True)

    listed = subprocess.run(
        [codex, "plugin", "list", "--available", "--json"],
        cwd=repo,
        env=env,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    installed = json.loads(listed.stdout)["installed"]

    assert all(
        plugin["pluginId"] != "im-not-ai-codex@im-not-ai-jp" for plugin in installed
    )


def test_lifecycle_scripts_do_not_expose_korean_user_text() -> None:
    korean_text = re.compile(r"[\uac00-\ud7a3]")

    for relative in ("install.sh", "uninstall.sh"):
        script = (ROOT / relative).read_text(encoding="utf-8")
        assert korean_text.search(script) is None
