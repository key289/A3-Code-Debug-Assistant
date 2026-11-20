# Git 合并冲突处理
出处：Git 官方文档 (Basic Merge Conflicts)

- 症状：执行 `git merge` 或 `git pull` 时提示 CONFLICT (content)。
- 原因：两个分支修改了同一个文件的同一行代码。
- 解决步骤：
  1. 打开冲突文件，找到 `<<<<<<< HEAD`、`=======`、`>>>>>>> branch_name` 标记。
  2. 手动保留需要的代码，删除这些标记符号。
  3. 执行 `git add 文件名`。
  4. 执行 `git commit -m "解决冲突"`。