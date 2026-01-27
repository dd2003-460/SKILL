#!/usr/bin/env python3
"""
Skill Publisher (v2.2)
Handles version rotation and symlink deployment for Gemini Skills.
"""

import os
import sys
import re
import shutil
import argparse
import datetime
from pathlib import Path

# --- Environment Auto-Correction ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent
VENV_PYTHON = PROJECT_ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists():
    current_exe = Path(sys.executable).resolve()
    target_exe = VENV_PYTHON.resolve()
    if current_exe != target_exe:
        try:
            os.execv(str(VENV_PYTHON), [str(VENV_PYTHON)] + sys.argv)
        except OSError:
            pass
# -----------------------------------

# Configuration
MAX_VERSIONS_TO_KEEP = 3
GEMINI_SKILLS_DIR = Path.home() / ".gemini" / "skills"
OPENCODE_SKILLS_DIR = Path.home() / ".config" / "opencode" / "skills"
MY_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent


def get_skill_versions(skill_name):
    """Find all versioned directories for a skill."""
    versions = []
    pattern = re.compile(rf"^{re.escape(skill_name)}-(\d{{8}})$")

    if not MY_SKILLS_ROOT.exists():
        return []

    for item in MY_SKILLS_ROOT.iterdir():
        if item.is_dir():
            match = pattern.match(item.name)
            if match:
                date_str = match.group(1)
                versions.append({"path": item, "date": date_str, "name": item.name})

    # Sort by date descending (newest first)
    versions.sort(key=lambda x: x["date"], reverse=True)
    return versions


def deploy_symlink(source_path, target_base_dir, link_name):
    """Create or update a symlink pointing to the source."""
    target_base = Path(target_base_dir)
    target_link = target_base / link_name

    # Ensure target directory exists
    target_base.mkdir(parents=True, exist_ok=True)

    # Check if target exists
    if target_link.exists() or target_link.is_symlink():
        if target_link.is_symlink():
            # It's a symlink, safe to remove
            target_link.unlink()
        elif target_link.is_dir():
            print(
                f"⚠️  Warning: Target '{target_link}' is a real directory, not a symlink."
            )
            print("   Please manually remove or rename it to allow symlinking.")
            return False
        else:
            # File or other
            target_link.unlink()

    # Create new symlink
    # Use relative path if possible for portability, or absolute?
    # Absolute is safer for global links.
    try:
        os.symlink(source_path, target_link)
        print(f"✅ Linked: {target_link} -> {source_path}")
        return True
    except OSError as e:
        print(f"❌ Error creating symlink: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Publish and rotate Gemini Skills.")
    parser.add_argument(
        "skill_name", help="Base name of the skill (e.g., 'doc2x-pdf-parser')"
    )
    parser.add_argument(
        "--target",
        choices=["global", "local"],
        default="global",
        help="Deployment target (default: global)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without changes"
    )

    args = parser.parse_args()

    skill_name = args.skill_name
    print(f"🚀 Publishing skill: {skill_name}")

    # 1. Find versions
    versions = get_skill_versions(skill_name)
    if not versions:
        print(
            f"❌ No versioned directories found for '{skill_name}' in {MY_SKILLS_ROOT}"
        )
        sys.exit(1)

    latest_version = versions[0]
    print(f"📍 Latest version: {latest_version['name']}")

    # 2. Rotation (Cleanup old versions)
    if len(versions) > MAX_VERSIONS_TO_KEEP:
        to_remove = versions[MAX_VERSIONS_TO_KEEP:]
        print(f"\n🧹 Rotating versions (Retention: {MAX_VERSIONS_TO_KEEP})")
        for v in to_remove:
            print(f"   Candidate for deletion: {v['name']}")
            if not args.dry_run:
                # In a real tool, we might ask for confirmation or move to trash
                # For now, we'll just log advice to delete manually to be safe
                print(f"   [Action Required] Please manually delete: {v['path']}")

    # 3. Deploy (Symlink)
    if args.dry_run:
        print("\n[Dry Run] Would create symlink pointing to latest version.")
        sys.exit(0)

    source_path = latest_version["path"]

    if args.target == "global":
        # Deploy to both Gemini and OpenCode
        print(f"\n🌍 Deploying to Global (Dual CLI):")

        print(f"   📦 Gemini CLI: {GEMINI_SKILLS_DIR}")
        gemini_success = deploy_symlink(source_path, GEMINI_SKILLS_DIR, skill_name)

        print(f"   📦 OpenCode: {OPENCODE_SKILLS_DIR}")
        opencode_success = deploy_symlink(source_path, OPENCODE_SKILLS_DIR, skill_name)

        if not (gemini_success and opencode_success):
            print("\n⚠️  Warning: Some symlinks failed to create. Check errors above.")

    elif args.target == "local":
        # Current working directory - Dual CLI support
        cwd = Path.cwd()
        print(f"\n🏠 Deploying to Local Project (Dual CLI):")

        # Gemini CLI
        gemini_target = cwd / ".gemini" / "skills"
        print(f"   📦 Gemini CLI: {gemini_target}")
        gemini_success = deploy_symlink(source_path, gemini_target, skill_name)

        # OpenCode
        opencode_target = cwd / ".opencode" / "skills"
        print(f"   📦 OpenCode: {opencode_target}")
        opencode_success = deploy_symlink(source_path, opencode_target, skill_name)

        if not (gemini_success and opencode_success):
            print(
                "\n⚠️  Warning: Some local symlinks failed to create. Check errors above."
            )

    # --- Post-Deployment Checklist ---
    obsidian_vault = Path.home() / "Documents/Knowledge_Cloud/Computer"
    print("\n📝 Post-Deployment Checklist (Obsidian):")
    print(
        f"1. [User Guide] Update or Create: {obsidian_vault}/{title_case(skill_name)}_Skill_User_Guide.md"
    )
    print(f"   (Remember to bold new features like 'v{latest_version['date']}')")
    print(f"2. [MOC] Register in: {obsidian_vault}/Skills_MOC.md")
    print("\n✅ Deployment Complete.")


def title_case(s):
    return s.replace("-", " ").title().replace(" ", "_")


if __name__ == "__main__":
    main()
