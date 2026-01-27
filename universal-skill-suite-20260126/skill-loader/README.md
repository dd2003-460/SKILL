# Skill 合并工具说明书

## 概述
这是一个用于批量加载和合并 Skill 文件夹中 `SKILL.md` 文件的工具。支持命令行和可视化界面两种模式，帮助用户将多个 Skill 合并为一个系统提示文件，用于 AI 导入。

## 文件结构
- `batch_skill_loader.py`：主脚本文件。

## 功能
- **遍历文件夹**：自动扫描指定目录下的子文件夹，查找 `SKILL.md` 文件。
- **选择性加载**：支持命令行指定文件夹，或通过 GUI 多选。
- **合并输出**：将选中的 Skill 合并为 `combined-skills.md` 文件。
- **跳过无效**：如果文件夹无 `SKILL.md`，自动跳过并提示。

## 使用方法

### 1. 准备
- 确保 Python 已安装（推荐 3.6+）。
- 将 Skill 文件夹放在同一目录下（或用 `--dir` 指定路径）。

### 2. 运行脚本
- **可视化模式（推荐）**：
  - 运行 `python batch_skill_loader.py`（无参数）。
  - 弹出窗口：选择要合并的文件夹（复选框多选）。
  - 点击“执行合并”：生成 `combined-skills.md`。
  - 点击“退出”：关闭窗口。

- **命令行模式**：
  - 指定文件夹：`python batch_skill_loader.py --folders folder1 folder2`
  - 指定目录：`python batch_skill_loader.py --dir /path/to/skills --folders folder1`
  - 指定输出：`python batch_skill_loader.py --output my-skills.md --folders folder1`

### 3. 参数说明
- `--dir`：Skill 根目录（默认当前目录）。
- `--output`：输出文件名（默认 `combined-skills.md`）。
- `--folders`：指定文件夹名（空格分隔，使用命令行模式）。

### 4. AI 导入
- 生成的 `combined-skills.md` 包含合并的系统提示。
- 复制内容到 AI 平台（如 ChatGPT、Claude）的系统提示字段。
- 示例：加载到自定义 GPT 的 Instructions 中。

## 示例
- 合并所有 Skill：`python batch_skill_loader.py`
- 合并特定 Skill：`python batch_skill_loader.py --folders directive-compliance-skill iterative-optimizer-skill`

## 注意事项
- 确保文件夹中有 `SKILL.md` 文件，否则跳过。
- 输出文件覆盖同名文件。
- GUI 需要 Tkinter 支持（Python 标准库）。
- 如果有错误，检查终端输出。

## 更新日志
- v1.0：初始版本，支持 GUI 和命令行。