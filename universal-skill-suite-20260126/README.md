# Universal Skill Suite

## 版权声明

## 项目来源
本仓库（universal-skill-suite）基于以下开源项目和贡献：

- **Khazix Skills**：来源于GitHub上的Khazix相关技能库，感谢原作者的开源贡献。
- **Claude相关**：部分灵感来源于Claude AI的技能和提示系统。
- **研究生师兄的仓库**：借鉴了我研究生师兄的仓库设计和代码结构。

## 版权尊重
- 本项目尊重所有原作者的版权，所有代码、文档和技能定义的版权归原作者所有。
- 本项目仅用于学习、研究和个人非商业用途。
- 任何商业使用、复制、分发或修改必须获得原作者的明确许可。

## 使用限制
- **禁止商业化**：不得将本项目用于任何商业目的，包括但不限于销售、广告或盈利服务。
- **开源共享**：鼓励在遵守版权的前提下进行学习和改进，但请注明来源。
- **免责声明**：本项目不承担任何使用后果的责任，使用者需自行评估风险。

## 联系方式
如有版权问题，请联系项目维护者。

## Skill介绍

本仓库包含多种AI技能（Skills），分为主要技能和次级技能，用于增强AI模型的行为和功能。

### 主要技能
- **directive-compliance-skill**：强化指令跟随与拒绝策略，确保输入契约满足后再执行。
- **engineering-principles-skill**：输出遵循工程原则（模块化、解耦、迭代、契约），含自检与拒绝策略。
- **iterative-optimizer-skill**：以迭代方式优化既有输出，提供改进理由与变更摘要，自检与拒绝策略。
- **latex-output-skill**：统一LaTeX输出格式与可编译性（最小模板），包含自检与拒绝策略。
- **md-output-skill**：统一Markdown输出格式、结构与规整性，包含自检与拒绝策略。

### 次级技能（Khazix-Skills-main下）
- **ralph-wiggum-skill**：自主迭代技能，让Claude自己改自己的代码。支持循环次数限制，自动化迭代优化。
- **planning-with-files-skill**：用Markdown文件做持久化的任务规划技能。任务状态跟踪和进度管理，可以指导其他Skills工作。
- **Superpowers-skill**：一个"技能库的技能库"，把Claude Code的Plan模式升级了十几倍。头脑风暴时连续追问，帮助理清需求思路。
- **circle-skill**：循环技能，结合循环前准备，确保安全迭代。
  - **loop-preparation-skill**（次级）：循环前准备，要求全部复制项目为副本，只操作副本，如果出错就回退到上一个正确版本。
- **ai-planning-skill**：综合AI规划技能，结合持久化规划和头脑风暴升级。

### 使用方法
1. 使用`skill-loader/batch_skill_loader.py`合并技能到`combined-skills.md`。
2. 复制内容到AI工具的系统提示中。
3. 参考各技能文件夹下的`README.md`获取详细使用建议。