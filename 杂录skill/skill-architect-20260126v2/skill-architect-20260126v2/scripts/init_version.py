#!/usr/bin/env python3
"""
Skill Version Initializer (v2.2)
Creates new versioned skill directories, optionally inheriting from previous versions or upstream.
"""

import sys
import os
import shutil
import argparse
import datetime
import re
import hashlib
import yaml
from pathlib import Path

# --- Environment Auto-Correction ---
# Ensure we are running inside the project's .venv
SCRIPT_DIR = Path(__file__).resolve().parent
# Path chain: scripts/ -> skill-ver/ -> my_skills/ -> ROOT
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent
VENV_PYTHON = PROJECT_ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists():
    # Resolve symlinks to compare absolute paths
    current_exe = Path(sys.executable).resolve()
    target_exe = VENV_PYTHON.resolve()

    if current_exe != target_exe:
        # Re-execute with venv python
        try:
            os.execv(str(VENV_PYTHON), [str(VENV_PYTHON)] + sys.argv)
        except OSError as e:
            print(f"⚠️  Warning: Failed to auto-switch to venv: {e}")
# -----------------------------------

# Configuration
MY_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

SKILL_TEMPLATE = """
---
name: {skill_name}
description: [TODO: Brief description in English for the model]
---

# {skill_title}

## Role & Objective
[TODO: English System Prompt. Define who the agent is and what they do.]

## Workflow
[TODO: English System Prompt. Define the steps.]

"""

CUSTOMIZATION_TEMPLATE = """
# Customization Log
Base: {base_source}
Fork Date: {date}

## Changes ({date})
- **Initialized**: {action_description}
"""


def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def find_latest_version(skill_name):
    """Find the latest version directory for a skill."""
    pattern = re.compile(rf"^{re.escape(skill_name)}-(\\d{{8}})$")
    versions = []
    if MY_SKILLS_ROOT.exists():
        for item in MY_SKILLS_ROOT.iterdir():
            if item.is_dir():
                match = pattern.match(item.name)
                if match:
                    versions.append((match.group(1), item))

    versions.sort(key=lambda x: x[0], reverse=True)
    return versions[0][1] if versions else None


def init_skill_version(skill_name, base_on=None, force=False):
    today = datetime.datetime.now().strftime("%Y%m%d")
    new_dir_name = f"{skill_name}-{today}"
    new_dir_path = MY_SKILLS_ROOT / new_dir_name

    print(f"🚀 Initializing {skill_name}...")
    print(f"   Target: {new_dir_path}")

    if new_dir_path.exists() and not force:
        print(f"❌ Error: Directory already exists: {new_dir_path}")
        print("   Use --force to overwrite.")
        return False

    # Scenario 1: Fork from External Base
    if base_on:
        base_path = Path(base_on).resolve()
        if not base_path.exists():
            print(f"❌ Error: Base path not found: {base_path}")
            return False

        print(f"   Forking from: {base_path}")
        if new_dir_path.exists():
            shutil.rmtree(new_dir_path)
        shutil.copytree(base_path, new_dir_path)

        # Generate UPSTREAM.yaml
        upstream_data = {"source_path": str(base_path), "files": {}}
        for root, _, files in os.walk(base_path):
            for file in files:
                full_path = Path(root) / file
                rel_path = full_path.relative_to(base_path)
                # Skip .git or hidden files
                if not str(rel_path).startswith("."):
                    upstream_data["files"][str(rel_path)] = calculate_sha256(full_path)

        with open(new_dir_path / "UPSTREAM.yaml", "w") as f:
            yaml.dump(upstream_data, f)

        # Create Customization Log
        with open(new_dir_path / "CUSTOMIZATION.md", "w") as f:
            f.write(
                CUSTOMIZATION_TEMPLATE.format(
                    base_source=str(base_path),
                    date=today,
                    action_description=f"Forked from {base_path}",
                )
            )

    # Scenario 2: Inherit from Previous Version
    elif latest := find_latest_version(skill_name):
        print(f"   Inheriting from latest: {latest.name}")
        if new_dir_path.exists():
            shutil.rmtree(new_dir_path)
        shutil.copytree(latest, new_dir_path)

        # Update Customization Log with inheritance info
        cust_log = new_dir_path / "CUSTOMIZATION.md"
        if cust_log.exists():
            # Read previous version's changes
            prev_cust_log = latest / "CUSTOMIZATION.md"
            inherited_features = []
            if prev_cust_log.exists():
                with open(prev_cust_log, "r") as f:
                    content = f.read()
                    # Extract the last "## Changes" section
                    import re

                    matches = re.findall(
                        r"## Changes \((\d{8})\)\n(.*?)(?=\n##|\Z)", content, re.DOTALL
                    )
                    if matches:
                        last_date, last_changes = matches[-1]
                        inherited_features.append(f"## Inherited from v{latest.name}")
                        inherited_features.append(
                            f"Previous version ({last_date}) introduced:"
                        )
                        for line in last_changes.strip().split("\n"):
                            if line.strip().startswith("-"):
                                inherited_features.append(line)

            # Append to new version's CUSTOMIZATION.md
            with open(cust_log, "a") as f:
                if inherited_features:
                    f.write("\n" + "\n".join(inherited_features) + "\n")
                f.write(
                    f"\n## Changes ({today})\n- **Upgraded**: Created new version based on {latest.name}.\n"
                )

    # Scenario 3: Fresh Start
    else:
        print("   Creating fresh skill.")
        new_dir_path.mkdir(parents=True, exist_ok=True)
        (new_dir_path / "scripts").mkdir(exist_ok=True)
        (new_dir_path / "references").mkdir(exist_ok=True)

        # Write Template SKILL.md
        with open(new_dir_path / "SKILL.md", "w") as f:
            f.write(
                SKILL_TEMPLATE.format(
                    skill_name=skill_name,
                    skill_title=skill_name.replace("-", " ").title(),
                )
            )

    print(f"✅ Successfully initialized {new_dir_name}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Initialize a Gemini Skill version.")
    parser.add_argument("skill_name", help="Name of the skill")
    parser.add_argument("--base-on", help="Path to external skill to fork from")
    parser.add_argument(
        "--force", action="store_true", help="Overwrite existing directory"
    )

    args = parser.parse_args()
    init_skill_version(args.skill_name, args.base_on, args.force)


if __name__ == "__main__":
    main()
