# Clang中文手册













clang.llvm.org/docs/ 卡死人




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




#### [术语](http://clang.llvm.org/docs/UsersManual.html#id10)[](http://clang.llvm.org/docs/UsersManual.html#terminology)

前端，解析器，后端，预处理器，未定义行为，诊断，优化器

#### [基本用途](http://clang.llvm.org/docs/UsersManual.html#id11)

介绍新手如何使用C编译器。

































