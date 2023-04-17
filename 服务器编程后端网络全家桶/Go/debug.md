
Go 语言基础：包括语言基础、变量、数据类型、控制语句、函数、指针、数组、切片、映射、结构体等等。

Go 语言并发：Go 语言天生支持并发，学习并发编程需要掌握 goroutine 和 channel 的使用，以及常用的并发模型和并发编程的技巧。

Go 语言标准库：Go 语言的标准库非常丰富，学习如何使用标准库可以让你更快速地编写高效的程序。

Go 语言开发工具和环境：学习如何安装和配置 Go 语言的开发环境，以及如何使用 Go 的命令行工具进行编译、运行和调试程序。

Go 语言网络编程：Go 语言天生支持网络编程，学习如何使用 Go 编写网络程序，包括 HTTP、TCP、UDP 等协议的编程。

Go 语言测试和调试：Go 语言内置了测试框架，学习如何编写测试用例以及如何使用调试工具进行调试，可以帮助你更好地开发和维护 Go 语言程序。
# debug



go语言有哪些好的debug方法？ - quinn的回答 - 知乎
https://www.zhihu.com/question/40980436/answer/2913150382
- dlv就是go的gdb

使用：
1、dlv debug xxx.go 指定需要debug的文件
2、进入dlv交互式窗口后，b <filename>:<line> 指定断点
3、r arg 指定运行参数
4、n 执行一行
5、c 运行至断点或程序结束





 https://github.com/go-delve/delve/blob/master/Documentation/cli/README.md

- godebug
- 
```
go get github.com/mailgun/godebug
```
使用不同的方法，直接把源码作为目标程序，在每一行插入调试代码，然后编译并运行。结果就是一个全功能的调试器，完全可以移植到不同平台。事实上，由于有了gopherjs ，你也可以在浏览器上进行调试：

