
z3官网 http://rise4fun.com/z3/tutorial 


交互方式

```cmd
z3 -in
```

编写一个x.smt然后输入
```
z3 -smt2 x.smt
```

libz3.dll和* .pyc / py所在的目录添加到PYTHONPATH

```
java -jar ./com.microsoft.z3.jar -q x.smt2
```


下载Z3对应的可执行文件到某个目录，然后使用编辑器编写一个SMT-LIB格式，后缀为.smt2的纯文本文件。 

接着调用`./z3 smt-lib-file.smt2`，即可对对应的SMT-LIB文件进行求解。 

现在流行的编辑器vscode有smt-lib-syntax插件，可以对SMT-LIB格式的文件进行语法高亮，便于编辑。  


Z3的输入形式有多种，包括文本，API以及交互式输入。 我们选择使用的在线版Z3，在编辑器中输入SMT-LIB格式的SMT公式即可。



# 1. SMTlib cpp版本输入标准smt-lib2格式



pp + smt-lib2.0的输入 https://rise4fun.com/Z3/tutorial/guide smt2在线运行官方教程简短教程，其中介绍了Z3的基础功能和简单的SMT-LIB语法。https://rise4fun.com/z3/tutorialcontent/guide 中文翻译 https://blog.csdn.net/alu_xd/article/details/52169885 1 https://blog.csdn.net/alu_xd/article/details/52174022 2

这是博主翻译的官网上的z3手册，但是不全面，想看全面的手册见官网手册。Z3的输入格式是SMT-LIB2.0标准（想进一步了解smt-lib标准，可以参考[这个](http://smtlib.cs.uiowa.edu/)网站）的一个拓展，一个Z3脚本就是一个命令序列。

可以使用**help**命令去查看一系列可用的命令。

**echo**命令用于显示一个信息。

Z3的内部维持着一个栈，这个栈里面保存着用户输入的公式和申明（常量的和函数的）。

**declare-const**命令用于申明一个给定类型的常量，

**declare-fun**命令则用于申明一个函数。


























































































































