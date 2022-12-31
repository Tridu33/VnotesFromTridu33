# 1. clang

[在VS Code中使用Clang作为你的C++编译器https://www.jianshu.com/p/afe0ffa7839d](https://www.jianshu.com/p/afe0ffa7839d)

 [Clang编译器的使用](https://www.cnblogs.com/ykmzy/articles/6095251.html)


 clang 编译多个文件生成.ll 的Makefile

https://blog.csdn.net/liubaosen/article/details/104551747




## 1.1. 实验


zybuluo.com/sangyy/note/166600






# 2. clang 和 llvm 编译命令




https://feng-qi.github.io/2017/06/14/clang-llvm-compile-command/
LLVM(low level virtual machine)顾名思义它是一种虚拟机，它在对代码进行处理的时候都需要使用IR中间文件，所以源代码要被先转换为LLVM IR中间文件（LLVM Intermediate Representation）。

LLVM在对程序进行优化的时候全部都是以IR的形式来进行优化的，它类似于是一种被LLVM所使用的一种语言，可以跨平台使用，因此所有平台上的LLVM都可以解释同一份IR，然后LLVM后端再利用IR生成不同平台上的机器码，此种类型的程序才可以正常运行。

LLVM IR文件(文本形式)

生成文本格式的IR文件：

clang -O3 -emit-llvm helloworld.c -S -o helloworld.ll
1
LLVM IR文件(二进制形式)

直接编译生成二进制格式IR文件：

clang -O3 -emit-llvm helloworld.c -c -o helloworld.bc
1
LLVM IR文件格式转换

.bc和.ll文件的转换：

llvm-as helloworld.ll     //llvm .ll -> .bc assembler
llvm-dis helloworld.bc  //llvm .bc -> .ll disassembler
1
2
LLVM IR生成平台对应的汇编文件
通过IR文件生成符合目标平台上的汇编文件，LLVM后端做的事情，通过llc进行操作：

llc helloworld.ll -o helloworld.S
1
LLVM IR生成平台对应的可执行文件

通过IR文件生成符合目标平台上的可执行文件，LLVM后端做的事情，通过llc进行操作：


llc -filetype=obj helloworld.ll -o helloworld.o
gcc helloworld.o
1
2
3
或者

llc -filetype=obj helloworld.bc -o helloworld.o
gcc helloworld.o
1
2
llvm只能保证生成obj文件，最后都需要使用gcc进行一次链接才能生成可执行文件。
LLVM IR文件link操作

llvm-link func1.bc func2.bc -o linked.bc





















