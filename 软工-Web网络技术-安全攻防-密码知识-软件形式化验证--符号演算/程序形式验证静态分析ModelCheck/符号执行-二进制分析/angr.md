符号执行-Angr-CTF-教学-ais3_crackme





angr 符号执行爆破 CTF-RE 入门
https://www.cnblogs.com/Node-Sans-Blog/p/14403013.html









https://www.bilibili.com/video/av46689373/

https://www.bilibili.com/video/av96737211/
一般还是s2e好一些，triton angr这些需要自己写大量的函数摘要
# 1. angr


符号执行-Angr实践
https://blog.csdn.net/yalecaltech/article/details/88753923、












https://bbs.pediy.com/thread-261885.htm



[angr的官方文档](https://docs.angr.io/)对于angr的定义如下：

angr是一个多体系结构的二进制分析工具包，能够执行动态符号执行（如Mayhem、kle等）和二进制文件的各种静态分析。


	
我个人对angr的理解是angr使用符号执行的技术，可以静态的遍历程序的每一个分支，模拟运行这个分支的时候的内存、寄存器实时的变化，**并且能够找到触发该分支的输入内容**。虽然angr理论上应该对恶意程序的分析是可行的，但是作为刚接触符号执行这个概念的新手，还是决定先试试使用angr获取简单的crack程序的flag。


