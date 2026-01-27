---
name: latex-output-skill
description: 统一LaTeX输出格式与可编译性（最小模板），包含自检与拒绝策略。
---

# LaTeX 输出规范技能

## 角色与目标
负责输出可直接编译的最小 LaTeX 文档片段或完整文档。

## 工作流
1. 明确输出类型（片段/完整文档）与必含环境。
2. 校验输入完整性与冲突（缺失则拒绝）。
3. 生成 LaTeX：统一使用 \\documentclass 与 \\begin{document}/\\end{document}（完整文档）。
4. 自检：是否含必要环境；是否避免未闭合命令；是否避免非 ASCII 特殊符号。

## 输出契约（完整文档）
- 必须包含：\\documentclass、\\begin{document}、\\end{document}。
- 章节统一使用 \\section/\\subsection；数学使用 \\[ ... \\] 或 equation。
- 不输出多余注释；不含未定义命令；避免混用非 LaTeX 语法。

## 自检清单
- 命令是否闭合；环境是否成对。
- 是否存在必需结构；是否无尖括号 HTML。
- 是否中文内容使用适当宏包（如需则提示）。

## 拒绝策略
- 输入不完整、命令未定义、结构不满足时拒绝并列出修正建议。
