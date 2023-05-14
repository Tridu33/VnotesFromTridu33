

LLVM项目是模块化和可重用的编译器和工具链技术的集合。LLVM主要的子项目有一下几个：

1.LLVM核心库:

LLVM提供一个独立的链接代码优化器为许多流行CPU（以及一些不太常见的CPU）的代码生成支持。这些库是围绕一个指定良好的代码表示构建的，称为LLVM中间表示（“LLVM IR”）。LLVM还可以充当JIT编译器 - 它支持x86 / x86_64和PPC / PPC64程序集生成，并具有针对编译速度的快速代码优化。。

2.LLVM IR 生成器Clang:

Clang是一个“LLVM原生”C / C ++ / Objective-C编译器，旨在提供惊人的快速编译（例如，在调试配置中编译Objective-C代码时比GCC快3倍），非常有用的错误和警告消息以及提供构建优秀源代码工具的平台。

3.LLDB项目:

LLDB项目以LLVM和Clang提供的库为基础，提供了一个出色的本机调试器。它使用Clang AST和表达式解析器，LLVM JIT，LLVM反汇编程序等，以便提供“正常工作”的体验。在加载符号时，它也比GDB快速且内存效率更高。

4.libc ++和libc++:

libc ++和libc++ ABI项目提供了C ++标准库的标准符合性和高性能实现，包括对C ++ 11的完全支持。

5.lld项目:

lld项目旨在成为clang / llvm的内置链接器。目前，clang必须调用系统链接器来生成可执行文件。
其他的就不再详细介绍了,详情可以参考(LLVM和Clang)
总之，LLVM是Apple主导的开源框架，并提供一套使用于Apple平台的LLVM编译器，同时提供优秀的性能，所以Apple采用LLVM的方式进行编译






# 1. AST-LLVMIR

前端负责解析，验证和诊断输入代码中的错误，然后将解析的代码转换为LLVM IR（通常情况。但是也有例外，通过构建AST然后将AST转换为LLVM IR）。





前端 --AST标准格式--> LLVM优化器 ---标准LLVM-IR数据结构-->  后端pass-->底层目标代码。

了解 Clang AST
https://jonasdevlieghere.com/understanding-the-clang-ast/

doc https://clang.llvm.org/docs/IntroductionToTheClangAST.html



如何查看 Clang AST？ https://stackoverflow.com/questions/18560019/how-to-view-clang-ast













## 1.1. AST标准格式














## 1.2. 标准LLVM-IR数据结构


































































