#!/usr/bin/env python3
"""
Upstream Checker (Git-Aware)
Verifies if the upstream source files have changed, checking both Git status and file hashes.
"""

import sys
import os
import hashlib
import yaml
import subprocess
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

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b''):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def check_git_status(source_dir):
    """
    Check if the source directory is a git repo and if it's behind remote.
    Returns: (is_git_repo, message)
    """
    try:
        # Check if it's a git repo
        subprocess.check_call(
            ["git", "rev-parse", "--is-inside-work-tree"], 
            cwd=source_dir, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, "Not a git repository"

    print(f"📡 Checking Git remote status for {source_dir}...")
    try:
        # Fetch latest info from remote (safely)
        subprocess.check_call(
            ["git", "fetch", "--dry-run"], 
            cwd=source_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Check local vs remote
        # We assume main branch usually, but let's check current branch status
        status = subprocess.check_output(
            ["git", "status", "-uno"], 
            cwd=source_dir, 
            text=True
        )
        
        if "Your branch is behind" in status:
            return True, "⚠️  BEHIND REMOTE: Your local upstream repo is outdated. Please run 'git pull' in it first."
        elif "Your branch is up to date" in status:
            return True, "✅ Git repo is up to date with remote."
        else:
            return True, f"ℹ️  Git status: {status.splitlines()[1] if len(status.splitlines()) > 1 else 'Unknown'}"
            
    except subprocess.CalledProcessError as e:
        return True, f"⚠️  Git check failed: {e}"

def check_upstream(skill_path):
    skill_path = Path(skill_path).resolve()
    upstream_file = skill_path / 'UPSTREAM.yaml'

    if not upstream_file.exists():
        print("ℹ️  No UPSTREAM.yaml found. This is likely an original skill.")
        return

    print(f"🔍 Checking upstream for: {skill_path.name}")
    
    with open(upstream_file, 'r') as f:
        upstream_data = yaml.safe_load(f)

    source_path = Path(upstream_data.get('source_path'))
    recorded_files = upstream_data.get('files', {})

    if not source_path.exists():
        print(f"⚠️  Warning: Upstream source path not found locally: {source_path}")
        return

    # Phase 1: Git Status Check
    is_git, git_msg = check_git_status(source_path)
    print(f"   Git Status: {git_msg}")
    print("-" * 60)

    # Phase 2: File Hash Check
    changes_detected = False
    
    print(f"   Upstream Source: {source_path}")
    print(f"{'File':<40} | {'Status':<15}")
    print("-" * 60)

    for rel_path, recorded_hash in recorded_files.items():
        src_file_path = source_path / rel_path
        current_hash = calculate_sha256(src_file_path)

        if current_hash is None:
            status = "MISSING"
            changes_detected = True
        elif current_hash != recorded_hash:
            status = "CHANGED"
            changes_detected = True
        else:
            status = "OK"

        print(f"{rel_path:<40} | {status:<15}")

    print("-" * 60)
    
    if "BEHIND REMOTE" in git_msg:
        print("🚨 CRITICAL: Your local upstream repo is outdated!")
        print(f"   Action: Go to {source_path} and run 'git pull', then run this check again.")
    elif changes_detected:
        print("⚠️  Upstream changes detected in local files! You may want to review and merge manually.")
    else:
        print("✅ Upstream is clean. No changes detected.")

def main():
    if len(sys.argv) < 2:
        # Default to checking current directory if valid skill
        cwd = Path.cwd()
        if (cwd / 'SKILL.md').exists():
            check_upstream(cwd)
        else:
            print("Usage: python check_upstream.py <skill_directory>")
            sys.exit(1)
    else:
        check_upstream(sys.argv[1])

if __name__ == "__main__":
    main()