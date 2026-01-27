# Customization Log
Base: Anthropic skill-creator
Fork Date: 2026-01-24

## Changes (2026-01-24)
- **Initialized Fork**: Created version 20260124 based on the official `skill-creator`.
- **Architecture**:
    - Adopted Symlink-based deployment (Source remains in `my_skills/`, deployed via link).
    - Adopted Immutable Versioning (`<skill>-<date>` folders).
- **Tooling**: 
    - Renamed `scripts/init_skill.py` -> `scripts/init_version.py` to support versioning logic.
    - Renamed `scripts/quick_validate.py` -> `scripts/validate_skill.py`.
    - Added `scripts/publish.py` for symlink management and version rotation.
    - Added `scripts/check_upstream.py` for tracking upstream changes.
    - Added **Environment Auto-Correction** to all scripts to force usage of project-local `.venv`.
    - Updated `publish.py` to print a "Post-Deployment Checklist" with specific Obsidian paths.
- **Documentation**:
    - Updated `SKILL.md` to define the V2.2 Bilingual Workflow.
    - Explicitly mandated Phase 5 (Obsidian Integration & MOC Registration) as the final requirement for any skill lifecycle.
    - Added requirements for `UPSTREAM.yaml` tracking.

## Changes (20260126)
- **Architecture Shift**: Replaced the 5-phase linear workflow with the RePPIT 6-phase cycle (Research -> Propose -> Plan -> Implement -> Test -> Publish).
- **Rationale**: 
  - Prevents "hallucinated modifications" by enforcing pre-coding rigor (Research, Proposal, Planning phases).
  - Transforms the agent from a "code writer" into a "software engineer" with structured decision-making.
  - Token optimization: LLM writes directly in Chinese, no translation step, saves ~50% token.
- **Key Additions**:
  - `references/template-*.md`: Added 12 template files (4 phases × 3 files/phase):
    - Template files (Chinese): For LLM to fill directly
    - User guide files (Chinese): For user understanding
    - Filling guide files (English): For LLM precise guidance
  - `SKILL.md` Workflow section (lines 22-77 in v2.2): Completely rewritten to define Phase 0-6 with explicit behavior contracts, deliverables, and user checkpoints.
  - Formalized `my_skills/Draft/` as the directory for intermediate artifacts.
    - Naming (v1): `<skill>-<YYYYMMDD>_<Stage>.md`
    - Naming (v2+): `<skill>-<YYYYMMDD>-v<N>_<Stage>.md`
  - **Dual CLI Support**: `publish.py` now creates symlinks for both:
    - Gemini CLI: `~/.gemini/skills/<name>`
    - OpenCode: `~/.config/opencode/skills/<name>`
- **Trade-offs**:
  - **Pro**: Maximizes safety, code quality, token efficiency, and adherence to user intent.
  - **Con**: Slower interaction loop (requires user approval at each phase).
- **Deferred**:
  - Modification of `init_version.py` to auto-generate blank `DESIGN.md` (postponed to v2.4+).
  - Integration of automated code review into `validate_skill.py` (postponed to future iteration).
  - Project-level dual symlinks (`<Project>/.gemini/skills` and `<Project>/.opencode/skills`) (postponed to v2.4+).

## Changes (20260126v2)
- **Draft Structure**: Changed Draft path from `~/Documents/skill_management/Draft/<file>.md` to `my_skills/Draft/<skill>-<YYYYMMDD>/` folder structure. Each project now has a dedicated folder for all phase documents.
- **Safe Modification Protocol**: Added mandatory "Backup-Modify-Cleanup" workflow in Phase 4 to prevent hallucinated file regeneration.
- **Inheritance Enhancement**: `init_version.py` now automatically extracts and records previous version's changes in "Inherited from" section.
- **Obsidian Permission Workaround**: Standardized temporary directory workflow for Obsidian vault updates to avoid permission errors.
- **Validation Clarity**: Clarified that `validate_skill.py` is only for format checking; Agent performs code validation directly in Phase 5.
- **Venv Transparency**: Added explicit documentation that users don't need to manually activate virtual environment.
- **New Directory Enforcement**: Phase 4 now requires verification that implementation happens in newly created version directory.
- **Project-Level Dual CLI**: `publish.py` now supports both `.gemini/skills/` and `.opencode/skills/` for local deployment, completing dual CLI support.