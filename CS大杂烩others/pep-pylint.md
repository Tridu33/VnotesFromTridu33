# 1. pep-pylint









pylint filename.py






pylint --help-msg=<msg-id> 指令可以查看这个问题的的详细信息 。

主要类型有

C——违反代码风格标准;

R——代码结构较差;

W——关于细节的警告;

E——代码中存在错误;

F——导致Pylint无法继续运行的错误。

知道了自 己的代码哪里不规范，就去针对性地改正吧，**PEP8并不是要百分百遵守的，当遵循PEP 8规范会使代码可读性变差、会跟周围代码风格不一致的时候，还是要遵循自己的判断。**


pylint --disable=invalid-name 模块名称 命令对相关规范进行屏蔽重新检测，发现问题提示会减少，评分也提升了一些

















pip install black即可完成该模块的安装，不过black依赖于Python 3.6+，但它仍然可以格式化Python2的代码。

black filename.py即可完成对filename.py的修正









