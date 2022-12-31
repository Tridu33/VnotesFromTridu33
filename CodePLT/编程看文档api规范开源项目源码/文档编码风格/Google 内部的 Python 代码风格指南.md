



尽管Python支持通过双下划线__(即"dunder")来私有化.不鼓励这样做.优先使用单下划线.单下划线更易于打出来、易读、易于小的单元测试调用.



# 1. Google 内部的 Python 代码风格指南
https://github.com/shendeguize/GooglePythonStyleGuideCN

谷歌Python代码风格指南 中文翻译


https://jishuin.proginn.com/p/763bfbd561a9
Google 内部的 Python 代码风格指南




pylint是一个用于在Python代码中发现bug和代码风格问题的工具,，pylint查找那些常在非动态语言(例如C或C++)编译器中捕获的问题.由于Python是动态语言,一些警告可能不正确,不过应该非常少有错误警告.


 Imports
只在import包和模块的时候使用import,而不要应用在单独的类或函数.(这一条对于typing_module有特别的意外)

Cons
pylint并不完美,为了更好的利用工具,我们有时候需要

a. Write around it(适配上下文风格)

b. 压制一些警告

c. 优化工具



 Pros
能够发现一些易被遗漏的错误,类似拼写错误,调用早于声明等等.


Decision(以下都译为建议)
确保对代码应用pylint

如果一些警告是不合适的,就抑制这些警告,这是为了让其他警告不会被隐藏.为了压制警告,可以设置行级别的注释:




```python
import x（当x是包或模块）
from x import y （当x是包前缀，y是不带前缀的模块名）
from x import  y as z （当有重复模块名y或y过长不利于引用的时候）
import y as z （仅在非常通用的简写的时候使用例如import numpy as np）
```



















































