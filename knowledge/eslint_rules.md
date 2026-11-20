# ESLint 前端代码规范
出处：ESLint 官方文档

- 症状：终端或编辑器报出大量红色波浪线或 Warning。
- 常见报错：
  - `no-unused-vars`：声明了变量但未使用。解决：删除该变量。
  - `semi`：缺少分号。解决：在语句末尾加上 `;`。
  - `no-console`：禁止使用 console.log。解决：上线前注释掉。
- 自动修复：在终端执行 `npx eslint --fix 文件名` 可自动修复 80% 的格式问题。