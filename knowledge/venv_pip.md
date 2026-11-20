# 虚拟环境与 Pip 包管理
出处：Python 官方文档 (venv) 与 pip 官方文档

## 虚拟环境
- 症状：明明装了包，运行却提示 ModuleNotFoundError。
- 原因：终端未激活虚拟环境，或者 IDE 解释器选错。
- 解决：Windows 执行 `.\venv\Scripts\activate`，Mac/Linux 执行 `source venv/bin/activate`。

## Pip 安装失败
- 症状：Timeout 超时、ConnectionError 网络错误。
- 解决：换国内源。例如 `pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple`