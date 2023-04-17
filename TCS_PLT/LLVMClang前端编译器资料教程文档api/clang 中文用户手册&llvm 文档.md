https://clang.llvm.org/docs/index.html


# 1. Clang中文手册





[clang 中文用户手册&llvm 文档下载](https://www.bookstack.cn/books/clang-llvm "clang 中文用户手册&llvm 文档")


[在线阅读clang-llvm/README.md](https://www.bookstack.cn/read/clang-llvm/README.md)







github翻译项目
github.com/oxnz/clang-user-manual








Clang编译器是C系列编程语言的开源编译器，它的目标是成为它们的最好类实现。LLVM优化器和代码生成器允许构建之上的Clang为许多目标提供高质量的优化和代码生成支持。 更多信息可以参阅[Clang网站](http://clang.llvm.org/)或[LLVM网站](http://llvm.org/)。

本文介绍了使用Clang作为终端用户的编译器，记录支持的特征，命令行选项等重要注意事项。如果您有兴趣使用Clang构建成处理代码的工具，请参阅[“Clang” CFE Internals Manual](http://clang.llvm.org/docs/InternalsManual.html)。 如果您对[Clang Static Analyzer](http://clang-analyzer.llvm.org/)感兴趣，请参阅它的网页。

Clang是C系列编程语言的完整工具链中一个组成部分。 单独的文档描述了[assemble a complete toolchain](http://clang.llvm.org/docs/Toolchain.html)所需的其他部分。

Clang旨在支持包括C，Objective-C，C ++和Objective-C ++以及其他许多方言在内的C系列编程语言。 有关特定于语言的信息，请参阅相应的语言特定部分：

[C Language](http://clang.llvm.org/docs/UsersManual.html#c): K&R C, ANSI C89, ISO C90, ISO C94 (C89+AMD1), ISO C99 (+TC1, TC2, TC3).  
[Objective-C Language](http://clang.llvm.org/docs/UsersManual.html#objc): ObjC 1, ObjC 2, ObjC 2.1, plus variants depending on base language.  
[C++ Language](http://clang.llvm.org/docs/UsersManual.html#cxx)  
[Objective C++ Language](http://clang.llvm.org/docs/UsersManual.html#objcxx)  
[OpenCL C Language](http://clang.llvm.org/docs/UsersManual.html#opencl): v1.0, v1.1, v1.2, v2.0.

除了这些基础语言和方言外，Clang还支持被记录在相应语言中的各种各样语言扩展。 GCC，Microsoft，以及其他主流编译器能兼容这些扩展。同样的，Clang特定功能可以改进这些语言扩展的功能。 Clang驱动和语言功能有意与GNU GCC编译器兼容，这样就可以直接从GCC迁移到Clang中。 在大多数情况下，代码“只是工作”。 Clang还提供了一个替代驱动程序，[clang-cl](http://clang.llvm.org/docs/UsersManual.html#clang-cl)，旨在与Visual C ++的cl.exe编译器兼容。

除了语言特定功能之外，Clang还具有多种取决于正在编译的CPU架构或操作系统的功能。 有关详细信息，请参阅[Target-Specific Features and Limitations](http://clang.llvm.org/docs/UsersManual.html#target-features) 部分。

最后介绍了这个手册中使用的一些基本的[compiler terminology](http://clang.llvm.org/docs/UsersManual.html#terminology)，其中包含作为命令行编译器的[introduction to using Clang](http://clang.llvm.org/docs/UsersManual.html#basicusage) 。


 [术语](http://clang.llvm.org/docs/UsersManual.html#id10)[](http://clang.llvm.org/docs/UsersManual.html#terminology)

前端，解析器，后端，预处理器，未定义行为，诊断，优化器

[基本用途](http://clang.llvm.org/docs/UsersManual.html#id11)

介绍新手如何使用C编译器。


# 2. clang 中文用户手册&llvm 文档

有关LLVM（https://github.com/yejinlei/about-compiler） - 叶金雷的文章 - 知乎
https://zhuanlan.zhihu.com/p/22740225

https://github.com/oxnz/clang-user-manual




## 2.1. 基本命令

-   llvm-as - LLVM assembler 汇编器
-   llvm-dis - LLVM disassembler 反汇编器
-   opt - LLVM optimizer 优化器
-   llc - LLVM static compiler 静态编译器
-   lli - directly execute programs from LLVM bitcode 直接执行LLVM 字节码
-   llvm-link - LLVM bitcode linker 字节码连接器
-   llvm-ar - LLVM archiver 归档器
-   llvm-nm -list LLVM bitcode and object file’s symbol table 列出LLVM字节码和目标文件中的符号表
-   llvm-config - Print LLVM compilation options 打印LLVM编译选项
-   llvm-diff - LLVM structual ‘diff’ LLVM结构上的diff
-   llvm-cov - emit coverage information 省略覆盖信息
-   llvm-stress - generate random .ll files 生成随机的.ll文件
-   llvm-symbolizer - convert addresses into source code locations 把地址值转换成源代码位置
    
    ## 调试工具
    
-   bugpoint - automatic test case reduction tool 自动测试用例下降工具
-   llvm-extract - extract a function from an LLVM module 从LLVM模块中抽取一个函数
-   llvm-bcanalyzer - LLVM bitcode analyzer LLVM字节码分析器
    
    ## 开发者工具
    
-   FileCheck - Flexible pattern matching file verifier 弹性模式匹配的文件验证器
-   tblgen - Target Description To C++ Code Generator 目标描述到C++代码生成器
-   lit - LLVM Integrated Tester LLVM集成的测试器
-   llvm-build - LLVM Project Build Utility LLVM项目生成工具
-   llvm-readobj - LLVM Object Reader LLVM目标文件阅读器




https://www.bookstack.cn/read/clang-llvm/llvm-command-guide.md




















