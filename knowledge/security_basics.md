# 代码安全与防护基础
出处：OWASP Top 10 安全指南

## 敏感信息泄露
- 症状：代码中硬编码了数据库密码、API Key。
- 解决：一律使用环境变量读取，将配置放入 `.env` 文件中，并加入 `.gitignore` 防止提交。

## SQL 注入
- 症状：拼接 SQL 字符串导致 `' OR '1'='1` 绕过验证。
- 解决：使用参数化查询（如 `cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))`）。