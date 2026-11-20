# SQL 语法错误与保留字
出处：MySQL 8.0 官方参考手册

## 保留字冲突
- 症状：You have an error in your SQL syntax near 'order'
- 原因：表名或字段名使用了数据库保留字（如 order, user, group, desc）。
- 解决：使用反引号包裹表名或字段名，例如 `select * from \`order\``。

## 常见语法错误
- 症状：check the manual that corresponds to your MySQL server version。
- 原因：缺少逗号、单引号未闭合、括号不匹配。
- 排查：将 SQL 复制到 Navicat 或 DataGrip 中，一般会高亮提示语法错误位置。