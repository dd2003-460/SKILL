# Test Template - Filling Guide

## Summary
- Briefly describe the nature and scope of the change (1-2 sentences)
- Example: "新增 RePPIT 工作流集成，修改了 SKILL.md 和 references/ 目录"
- Write in Chinese

## Action Item Priorities
- **🔴 Must-fix**: Security vulnerabilities, breaking functional errors, data loss risks
- **🟡 Recommended**: Performance issues, code style inconsistencies, missing edge case handling
- **🟢 Consider**: Long-term improvements, refactoring opportunities, documentation enhancements
- Write descriptions in Chinese, keep file paths in English

## Code References
- Be precise with file paths and line numbers for quick navigation
- Format: `path/to/file.py:123` or `path/to/file.py:45-67`

## Review Dimensions
- **Security**: Input validation, sensitive data handling, permission checks
- **Performance**: Unnecessary loops, redundant computations, large object copies
- **Style**: Consistency with existing code, naming conventions
- **Edge Cases**: Null checks, exception handling, boundary conditions
- **Dependencies**: New external dependencies introduced, version compatibility
- **Integration**: Compatibility with other modules, API contract adherence
- Write all descriptions in Chinese
