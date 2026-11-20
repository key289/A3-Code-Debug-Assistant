# Python 常见异常与错误
出处：Python 官方文档 (https://docs.python.org/3/tutorial/errors.html)

## ModuleNotFoundError / ImportError
- 症状：No module named 'xxx'
- 原因：包未安装、虚拟环境选错、Python解释器路径不对。
- 排查：确认当前终端是否激活虚拟环境；执行 `pip show 包名`；检查 VS Code 右下角 Python 解释器。

## NameError
- 症状：name 'xxx' is not defined
- 原因：变量未定义、拼写错误、作用域问题。
- 排查：检查变量名拼写；确认变量在使用前已赋值。

## TypeError
- 症状：unsupported operand type(s) for +: 'int' and 'str'
- 原因：数据类型不匹配。
- 排查：打印变量 `type()` 进行核对；使用 `int()` 或 `str()` 进行类型转换。