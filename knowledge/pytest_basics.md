# Pytest 单元测试基础
出处：pytest 官方文档

- 命名规范：测试文件必须以 `test_` 开头（如 test_demo.py），测试函数必须以 `test_` 开头。
- 断言：直接使用 Python 自带的 `assert` 语句。
- 运行方式：在终端输入 `pytest` 即可自动发现并运行所有测试。
- 预期结果：如果代码正确，显示 `1 passed`；如果代码错误，显示 `AssertionError` 和具体不符的值。