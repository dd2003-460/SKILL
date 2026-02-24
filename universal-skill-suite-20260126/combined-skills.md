--- directive-compliance-skill ---
---
name: directive-compliance-skill
description: 强化指令跟随与拒绝策略，确保输入契约满足后再执行。
---

# 指令跟随技能

## 角色与目标
严格按照输入契约执行；信息不足时拒绝并说明最小需求。

## 工作流
1. 解析输入契约（目标、范围、必填字段、单位/时区、阈值）。
2. 校验完整性与冲突；不满足则拒绝并列出缺失。
3. 按步骤执行并在每步结束前做自检；失败则回滚或请求补充。
4. 生成符合输出契约的结果，并附上执行摘要。

## 输出契约
- 明确列出满足的输入项与未满足项（若有）。
- 主体内容按步骤产出；拒绝时给替代路径。
- 用现代简体中文；不含尖括号；结构为分级小节与要点。

## 自检清单
- 必填字段是否齐全；冲突是否已解决。
- 每步执行是否可验证；摘要是否对应事实。
- 是否满足禁用项与长度限制。

## 拒绝策略
- 不满足契约/约束时拒绝并给最小补充清单与替代方案。


--- engineering-principles-skill ---
---
name: engineering-principles-skill
description: 输出遵循工程原则（模块化、解耦、迭代、契约），含自检与拒绝策略。
---

# 工程原则技能

## 角色与目标
指导与生成遵循工程化原则的方案或代码片段（不绑定特定语言）。

## 工作流
1. 捕获需求与约束（性能、安全、可测试、演进）。
2. 产出模块划分、接口契约、依赖关系与演进路径。
3. 给出迭代计划与风险控制；附最小可验证策略。
4. 自检与纠偏：一致性、边界条件、耦合度与复杂度。

## 输出契约
- 提供模块清单、接口说明（输入/输出、异常）、依赖关系图示（文字）。
- 给出迭代计划（里程碑、验证点）与测试策略（单元/集成）。
- 结构为 Markdown 分级；不含尖括号；中文。

## 自检清单
- 模块边界是否明确；接口是否可测试。
- 依赖是否最小化；是否满足非功能需求。
- 迭代计划是否可执行；验证是否可度量。

## 拒绝策略
- 需求不完整或矛盾时拒绝并给补充清单与折中方案。


--- iterative-optimizer-skill ---
---
name: iterative-optimizer-skill
description: 以迭代方式优化既有输出，提供改进理由与变更摘要，自检与拒绝策略。
---

# 迭代优化技能

## 角色与目标
读取既有输出，提出改进（结构/内容/格式）并给出变更摘要与理由。

## 工作流
1. 解析现有输出与目标；校验约束是否明确。
2. 提出优化建议（分级列出）与风险点。
3. 生成新版本输出；提供变更摘要（diff 风格文字）。
4. 自检：契约一致性、长度、禁用项；失败则回滚或请求补充。

## 输出契约
- 分别提供：问题列表、优化建议、更新后的输出、变更摘要。
- 用中文；结构为 Markdown 分级与要点；不含尖括号。

## 自检清单
- 优化建议是否针对问题；变更摘要是否覆盖所有改动。
- 新输出是否满足原契约；是否控制长度与禁用项。

## 拒绝策略
- 输入缺失或目标不明时拒绝并给最小需求清单。


--- Khazix-Skills-main-circle-circle-skill ---
---
name: ralph-wiggum-skill
description: 自主迭代技能，让Claude自己改自己的代码。
---

# Ralph Wiggum 技能

## 角色与目标
反复向Agent输入提示语直到生成可用代码，支持设置循环次数限制，自动化迭代优化流程。

## 工作流
1. 接收初始代码生成请求和约束。
2. 向AI输入提示语，生成代码。
3. 检查代码可用性；如果失败，生成改进提示并重复。
4. 限制循环次数（建议5-10次），达到上限时停止并报告。
5. 输出最终可用代码和迭代摘要。

## 输出契约
- 列出每次迭代的代码版本和改进理由。
- 最终输出可用代码、总迭代次数和成功状态。
- 用中文；结构为分级小节；不含尖括号。

## 自检清单
- 代码是否可运行；迭代是否在限制内。
- 每次改进是否有效；最终代码是否满足需求。

## 拒绝策略
- 如果初始请求不明确，拒绝并要求补充约束。

--- Khazix-Skills-main-circle-preparation ---
---
name: loop-preparation-skill
description: 循环前准备技能，确保安全迭代。
---

# 循环前准备技能

## 角色与目标
在开始循环前，复制整个项目为副本，只操作副本，如果出错则回退到上一个正确版本。

## 工作流
1. 接收循环任务描述。
2. 复制整个项目到副本目录。
3. 验证副本完整性。
4. 准备循环参数。
5. 如果后续出错，回退到正确版本。

## 输出契约
- 副本路径和验证报告。
- 回退选项。
- 用中文；不含尖括号。

## 自检清单
- 副本是否完整；操作是否在副本上。
- 回退是否可用。

## 拒绝策略
- 如果无法复制，拒绝并要求检查权限。

--- Khazix-Skills-main-evolution-skill-evolution-manager ---
---
name: Skill Evolution Manager
description: 专门用于在对话结束时，根据用户反馈和对话内容总结优化并迭代现有 Skills 的核心工具。它通过吸取对话中的“精华”（如成功的解决方案、失败的教训、特定的代码规范）来持续演进 Skills 库。
license: MIT
---

# Skill Evolution Manager

这是整个 AI 技能系统的“进化中枢”。它不仅负责优化单个 Skill，还负责跨 Skill 的经验复盘和沉淀。

## 核心职责

1.  **复盘诊断 (Session Review)**：在对话结束时，分析所有被调用的 Skill 的表现。
2.  **经验提取 (Experience Extraction)**：将非结构化的用户反馈转化为结构化的 JSON 数据（`evolution.json`）。
3.  **智能缝合 (Smart Stitching)**：将沉淀的经验自动写入 `SKILL.md`，确保持久化且不被版本更新覆盖。

## 使用场景

**Trigger**: 
- `/evolve`
- "复盘一下刚才的对话"
- "我觉得刚才那个工具不太好用，记录一下"
- "把这个经验保存到 Skill 里"

## 工作流 (The Evolution Workflow)

### 1. 经验复盘 (Review & Extract)
当用户触发复盘时，Agent 必须执行：
1.  **扫描上下文**：找出用户不满意的点（报错、风格不对、参数错误）或满意的点（特定 Prompt 效果好）。
2.  **定位 Skill**：确定是哪个 Skill 需要进化（例如 `yt-dlp` 或 `baoyu-comic`）。
3.  **生成 JSON**：在内存中构建如下 JSON 结构：
    ```json
    {
      "preferences": ["用户希望下载默认静音"],
      "fixes": ["Windows 下 ffmpeg 路径需转义"],
      "custom_prompts": "在执行前总是先打印预估耗时"
    }
    ```

### 2. 经验持久化 (Persist)
Agent 调用 `scripts/merge_evolution.py`，将上述 JSON 增量写入目标 Skill 的 `evolution.json` 文件中。
- **命令**: `python scripts/merge_evolution.py <skill_path> <json_string>`

### 3. 文档缝合 (Stitch)
Agent 调用 `scripts/smart_stitch.py`，将 `evolution.json` 的内容转化为 Markdown 并追加到 `SKILL.md` 末尾。
- **命令**: `python scripts/smart_stitch.py <skill_path>`

### 4. 跨版本对齐 (Align)
当 `skill-manager` 更新了某个 Skill 后，Agent 应主动运行 `smart_stitch.py`，将之前保存的经验“重新缝合”到新版文档中。

## 核心脚本

- `scripts/merge_evolution.py`: **增量合并工具**。负责读取旧 JSON，去重合并新 List，保存。
- `scripts/smart_stitch.py`: **文档生成工具**。负责读取 JSON，在 `SKILL.md` 末尾生成或更新 `## User-Learned Best Practices & Constraints` 章节。
- `scripts/align_all.py`: **全量对齐工具**。一键遍历所有 Skill 文件夹，将存在的 `evolution.json` 经验重新缝合回对应的 `SKILL.md`。常用于 `skill-manager` 批量更新后的经验还原。

## 最佳实践

- **不要直接修改 SKILL.md 的正文**：除非是明显的拼写错误。所有的经验修正应通过 `evolution.json` 通道进行，这样可以保证在 Skill 升级时经验不丢失。
- **多 Skill 协同**：如果一次对话涉及多个 Skill，请依次为每个 Skill 执行上述流程。


--- Khazix-Skills-main-github-to-skills ---
---
name: github-to-skills
description: Automated factory for converting GitHub repositories into specialized AI skills. Use this skill when the user provides a GitHub URL and wants to "package", "wrap", or "create a skill" from it. It automatically fetches repository details, latest commit hashes, and generates a standardized skill structure with enhanced metadata suitable for lifecycle management.
license: MIT
---

# GitHub to Skills Factory

This skill automates the conversion of GitHub repositories into fully functional AI skills.

## Core Functionality

1. **Analysis**: Fetches repository metadata (Description, README, Latest Commit Hash).
2. **Scaffolding**: Creates a standardized skill directory structure.
3. **Metadata Injection**: Generates `SKILL.md` with extended frontmatter (tracking source, version, hash) for future automated management.
4. **Wrapper Generation**: Creates a `scripts/wrapper.py` (or similar) to interface with the tool.

## Usage

**Trigger**: `/GitHub-to-skills <github_url>` or "Package this repo into a skill: <url>"

### Required Metadata Schema

Every skill created by this factory MUST include the following extended YAML frontmatter in its `SKILL.md`. This is critical for the `skill-manager` to function later.

```yaml
---
name: <kebab-case-repo-name>
description: <concise-description-for-agent-triggering>
# EXTENDED METADATA (MANDATORY)
github_url: <original-repo-url>
github_hash: <latest-commit-hash-at-time-of-creation>
version: <tag-or-0.1.0>
created_at: <ISO-8601-date>
entry_point: scripts/wrapper.py # or main script
dependencies: # List main dependencies if known, e.g., ["yt-dlp", "ffmpeg"]
---
```

## Workflow

1. **Fetch Info**: The agent first runs `scripts/fetch_github_info.py` to get the raw data from the repo.
2. **Plan**: The agent analyzes the README to understand how to invoke the tool (CLI args, Python API, etc.).
3. **Generate**: The agent uses the `skill-creator` patterns to write the `SKILL.md` and wrapper scripts, ensuring the **extended metadata** is present.
4. **Verify**: Checks if the commit hash was correctly captured.

## Resources

- `scripts/fetch_github_info.py`: Utility to scrape/API fetch repo details (README, Hash, Tags).
- `scripts/create_github_skill.py`: Orchestrator to scaffold the folder and write the initial files.

## Best Practices for Generated Skills

- **Isolation**: The generated skill should install its own dependencies (e.g., in a venv or via `uv`/`pip`) if possible, or clearly state them.
- **Progressive Disclosure**: Do not dump the entire repo into the skill. Only include the necessary wrapper code and reference the original repo for deep dives.
- **Idempotency**: The `github_hash` field allows the future `skill-manager` to check `if remote_hash != local_hash` to trigger updates.


--- Khazix-Skills-main-plan-pan1skill ---
---
name: ai-planning-skill
description: 综合AI规划技能，结合持久化规划和头脑风暴升级。
---

# AI规划技能

## 角色与目标
用Markdown文件做持久化任务规划，头脑风暴时连续追问，帮助理清需求思路，自动生成需求文档、开发计划、测试用例，支持与其他Skills组合。

## 工作流
1. 接收任务描述和约束。
2. 创建或更新Markdown文件（如todo.md、plan.md）。
3. 跟踪任务状态，更新进度。
4. 进行多轮头脑风暴，确认需求、梳理边界、讨论风险。
5. 生成需求文档、开发计划、测试用例。
6. 指导其他Skills执行子任务，形成协作链。
7. 输出完整规划、文档和执行摘要。

## 输出契约
- 提供文件列表、内容更新、需求文档、计划、测试用例。
- 任务状态跟踪报告和头脑风暴记录。
- 用中文；Markdown格式和分级结构；不含尖括号。

## 自检清单
- 文件是否正确创建；需求是否全面。
- 进度是否可跟踪；计划是否可执行。
- 风险是否评估；协作是否有效。

## 拒绝策略
- 如果任务描述不完整或需求模糊，拒绝并要求补充。

--- Khazix-Skills-main-skill-management-skill-manager ---
---
name: skill-manager
description: Lifecycle manager for GitHub-based skills. Use this to batch scan your skills directory, check for updates on GitHub, and perform guided upgrades of your skill wrappers.
license: MIT
---

# Skill Lifecycle Manager

This skill helps you maintain your library of GitHub-wrapped skills by automating the detection of updates and assisting in the refactoring process.

## Core Capabilities

1.  **Audit**: Scans your local skills folder for skills with `github_url` metadata.
2.  **Check**: Queries GitHub (via `git ls-remote`) to compare local commit hashes against the latest remote HEAD.
3.  **Report**: Generates a status report identifying which skills are "Stale" or "Current".
4.  **Update Workflow**: Provides a structured process for the Agent to upgrade a skill.
5.  **Inventory Management**: Lists all local skills and provides deletion capabilities.

## Usage

**Trigger**: `/skill-manager check` or "Scan my skills for updates"
**Trigger**: `/skill-manager list` or "List my skills"
**Trigger**: `/skill-manager delete <skill_name>` or "Delete skill <skill_name>"

### Workflow 1: Check for Updates

1.  **Run Scanner**: The agent runs `scripts/scan_and_check.py` to analyze all skills.
2.  **Review Report**: The script outputs a JSON summary. The Agent presents this to the user.
    *   Example: "Found 3 outdated skills: `yt-dlp` (behind 50 commits), `ffmpeg-tool` (behind 2 commits)..."

### Workflow 2: Update a Skill

**Trigger**: "Update [Skill Name]" (after a check)

1.  **Fetch New Context**: The agent fetches the *new* README from the remote repo.
2.  **Diff Analysis**:
    *   The agent compares the new README with the old `SKILL.md`.
    *   Identifies new features, deprecated flags, or usage changes.
3.  **Refactor**:
    *   The agent rewrites `SKILL.md` to reflect the new capabilities.
    *   The agent updates the `github_hash` in the frontmatter.
    *   The agent (optionally) attempts to update the `wrapper.py` if CLI args have changed.
4.  **Verify**: Runs a quick validation (if available).

## Scripts

- `scripts/scan_and_check.py`: The workhorse. Scans directories, parses Frontmatter, fetches remote tags, returns status.
- `scripts/update_helper.py`: (Optional) Helper to backup files before update.
- `scripts/list_skills.py`: Lists all installed skills with type and version.
- `scripts/delete_skill.py`: Permanently removes a skill folder.

## Metadata Requirements

This manager relies on the `github-to-skills` metadata standard:
- `github_url`: Source of truth.
- `github_hash`: State of truth.


--- Khazix-Skills-main-circle-circle-skill ---
---
name: ralph-wiggum-skill
description: 自主迭代技能，让Claude自己改自己的代码。
---

# Ralph Wiggum 技能

## 角色与目标
反复向Agent输入提示语直到生成可用代码，支持设置循环次数限制，自动化迭代优化流程。

## 工作流
1. 接收初始代码生成请求和约束。
2. 向AI输入提示语，生成代码。
3. 检查代码可用性；如果失败，生成改进提示并重复。
4. 限制循环次数（建议5-10次），达到上限时停止并报告。
5. 输出最终可用代码和迭代摘要。

## 输出契约
- 列出每次迭代的代码版本和改进理由。
- 最终输出可用代码、总迭代次数和成功状态。
- 用中文；结构为分级小节；不含尖括号。

## 自检清单
- 代码是否可运行；迭代是否在限制内。
- 每次改进是否有效；最终代码是否满足需求。

## 拒绝策略
- 如果初始请求不明确，拒绝并要求补充约束。

--- Khazix-Skills-main-circle-preparation ---
---
name: loop-preparation-skill
description: 循环前准备技能，确保安全迭代。
---

# 循环前准备技能

## 角色与目标
在开始循环前，复制整个项目为副本，只操作副本，如果出错则回退到上一个正确版本。

## 工作流
1. 接收循环任务描述。
2. 复制整个项目到副本目录。
3. 验证副本完整性。
4. 准备循环参数。
5. 如果后续出错，回退到正确版本。

## 输出契约
- 副本路径和验证报告。
- 回退选项。
- 用中文；不含尖括号。

## 自检清单
- 副本是否完整；操作是否在副本上。
- 回退是否可用。

## 拒绝策略
- 如果无法复制，拒绝并要求检查权限。

--- Khazix-Skills-main-evolution-skill-evolution-manager ---
---
name: Skill Evolution Manager
description: 专门用于在对话结束时，根据用户反馈和对话内容总结优化并迭代现有 Skills 的核心工具。它通过吸取对话中的“精华”（如成功的解决方案、失败的教训、特定的代码规范）来持续演进 Skills 库。
license: MIT
---

# Skill Evolution Manager

这是整个 AI 技能系统的“进化中枢”。它不仅负责优化单个 Skill，还负责跨 Skill 的经验复盘和沉淀。

## 核心职责

1.  **复盘诊断 (Session Review)**：在对话结束时，分析所有被调用的 Skill 的表现。
2.  **经验提取 (Experience Extraction)**：将非结构化的用户反馈转化为结构化的 JSON 数据（`evolution.json`）。
3.  **智能缝合 (Smart Stitching)**：将沉淀的经验自动写入 `SKILL.md`，确保持久化且不被版本更新覆盖。

## 使用场景

**Trigger**: 
- `/evolve`
- "复盘一下刚才的对话"
- "我觉得刚才那个工具不太好用，记录一下"
- "把这个经验保存到 Skill 里"

## 工作流 (The Evolution Workflow)

### 1. 经验复盘 (Review & Extract)
当用户触发复盘时，Agent 必须执行：
1.  **扫描上下文**：找出用户不满意的点（报错、风格不对、参数错误）或满意的点（特定 Prompt 效果好）。
2.  **定位 Skill**：确定是哪个 Skill 需要进化（例如 `yt-dlp` 或 `baoyu-comic`）。
3.  **生成 JSON**：在内存中构建如下 JSON 结构：
    ```json
    {
      "preferences": ["用户希望下载默认静音"],
      "fixes": ["Windows 下 ffmpeg 路径需转义"],
      "custom_prompts": "在执行前总是先打印预估耗时"
    }
    ```

### 2. 经验持久化 (Persist)
Agent 调用 `scripts/merge_evolution.py`，将上述 JSON 增量写入目标 Skill 的 `evolution.json` 文件中。
- **命令**: `python scripts/merge_evolution.py <skill_path> <json_string>`

### 3. 文档缝合 (Stitch)
Agent 调用 `scripts/smart_stitch.py`，将 `evolution.json` 的内容转化为 Markdown 并追加到 `SKILL.md` 末尾。
- **命令**: `python scripts/smart_stitch.py <skill_path>`

### 4. 跨版本对齐 (Align)
当 `skill-manager` 更新了某个 Skill 后，Agent 应主动运行 `smart_stitch.py`，将之前保存的经验“重新缝合”到新版文档中。

## 核心脚本

- `scripts/merge_evolution.py`: **增量合并工具**。负责读取旧 JSON，去重合并新 List，保存。
- `scripts/smart_stitch.py`: **文档生成工具**。负责读取 JSON，在 `SKILL.md` 末尾生成或更新 `## User-Learned Best Practices & Constraints` 章节。
- `scripts/align_all.py`: **全量对齐工具**。一键遍历所有 Skill 文件夹，将存在的 `evolution.json` 经验重新缝合回对应的 `SKILL.md`。常用于 `skill-manager` 批量更新后的经验还原。

## 最佳实践

- **不要直接修改 SKILL.md 的正文**：除非是明显的拼写错误。所有的经验修正应通过 `evolution.json` 通道进行，这样可以保证在 Skill 升级时经验不丢失。
- **多 Skill 协同**：如果一次对话涉及多个 Skill，请依次为每个 Skill 执行上述流程。


--- Khazix-Skills-main-plan-pan1skill ---
---
name: ai-planning-skill
description: 综合AI规划技能，结合持久化规划和头脑风暴升级。
---

# AI规划技能

## 角色与目标
用Markdown文件做持久化任务规划，头脑风暴时连续追问，帮助理清需求思路，自动生成需求文档、开发计划、测试用例，支持与其他Skills组合。

## 工作流
1. 接收任务描述和约束。
2. 创建或更新Markdown文件（如todo.md、plan.md）。
3. 跟踪任务状态，更新进度。
4. 进行多轮头脑风暴，确认需求、梳理边界、讨论风险。
5. 生成需求文档、开发计划、测试用例。
6. 指导其他Skills执行子任务，形成协作链。
7. 输出完整规划、文档和执行摘要。

## 输出契约
- 提供文件列表、内容更新、需求文档、计划、测试用例。
- 任务状态跟踪报告和头脑风暴记录。
- 用中文；Markdown格式和分级结构；不含尖括号。

## 自检清单
- 文件是否正确创建；需求是否全面。
- 进度是否可跟踪；计划是否可执行。
- 风险是否评估；协作是否有效。

## 拒绝策略
- 如果任务描述不完整或需求模糊，拒绝并要求补充。

