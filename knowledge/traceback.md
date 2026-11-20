# Traceback 报错栈解读
出处：Python 官方文档 (traceback 模块)

- 原理：Python 报错时输出的堆栈信息。**从下往上读**，最后一行是具体的错误类型和原因，上面是调用轨迹。
- 特征：包含 `File "xxx.py", line N, in <module>` 等。
- 排查步骤：
  1. 直接看最后一行，找出具体的 Exception 类型（如 KeyError, ValueError）。
  2. 找到代码文件里报错的最后一行，定位具体代码。
  3. 如果是第三方库内部报错，查看是否有具体的参数传错。