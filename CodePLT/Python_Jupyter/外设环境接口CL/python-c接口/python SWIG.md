# 1. python SWIG


https://www.cnblogs.com/dda9/p/8612068.html

[http://www.swig.org/download.html](http://www.swig.org/download.html)





[https://wiki.jikexueyuan.com/project/interpy-zh/c_extensions/swig.html](https://wiki.jikexueyuan.com/project/interpy-zh/c_extensions/swig.html)













https://www.cnblogs.com/kaituorensheng/p/4464117.html

C 和 C++ 被公认为（理当如此）创建高性能代码的首选平台。对开发人员的一个常见要求是向脚本语言接口公开 C/C++ 代码，这正是 Simplified Wrapper and Interface Generator (SWIG) 的用武之地。SWIG 允许您向广泛的脚本语言公开 C/C++ 代码，包括 Ruby、Perl、Tcl 和 Python等。

为了建立python的扩展模块，SWIG采用分层的策略：用c写扩充模块，其余部分用python写。c包含低层次的封装，而python包含高层次的封装。分层策略是扩展模块的特定部分用特定的语言完成（而不全部用c/c++完成），另外通过利用2种语言，可以发挥各自语言的特性，增加灵活性。






















