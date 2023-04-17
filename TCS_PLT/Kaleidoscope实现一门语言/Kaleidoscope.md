










# 1. Kaleidoscope
http://llvm.org/docs/tutorial/index.html

# 2. LLVM Tutorial: Table of Contents


要求：本教程假定您了解C ++，但是没有以前的编译器经验是必需的。  
欢迎使用“使用LLVM的我的第一语言前端”教程。  
在这里，我们介绍了一种简单语言的实现，展示了它多么有趣和轻松。

本教程将帮助您快速入门和运行，并显示使用LLVM生成代码的具体示例。  
本教程介绍了简单的“万花筒”语言，并在数章的过程中对其进行了迭代构建，并展示了如何逐步构建。  
这样一来，我们就可以涵盖一系列语言设计和LLVM特定思想，一路展示和解释其代码，并减少大量的细节。  

我们强烈建议您使用此代码-进行复制并修改并进行实验。  

警告：为了专注于教授编译器技术和LLVM，本教程未展示软件工程原理的最佳实践。  

例如，代码普遍使用全局变量，不使用访问者，等等。。。而是保持简单，着重于手头的主题。  

本教程分为几章，涵盖各个主题，使您可以随意跳过：

    第1章：万花筒语言和Lexer-显示了我们要去的地方和要构建的基本功能。  
    词法分析器也是构建语言解析器的第一部分，并且我们使用了易于理解的简单C ++词法分析器。  
    第2章：实现解析器和AST-有了词法分析器，我们可以讨论解析技术和基本AST构造。  
    本教程描述了递归下降解析和运算符优先级解析。  
    第3章：向LLVM IR生成代码-准备好AST之后，我们将展示生成LLVM IR的简便性，并展示了一种将LLVM集成到项目中的简单方法。  
    第4章：添加JIT和Optimizer支持-LLVM的一大优点是它对JIT编译的支持，因此我们将深入探讨它，并向您展示添加JIT支持所需的3条线。  
    后面的章节介绍了如何生成.o文件。  
    第5章：扩展语言：控制流-随着基本语言的启动和运行，我们展示了如何通过控制流操作（“ if”语句和“ for”循环）进行扩展。  
    这使我们有机会谈论SSA的构建和控制流程。  
    第6章：扩展语言：用户定义的运算符-本章扩展了语言，使用户可以定义任意一元和二进制运算符-具有可分配的优先级！  
    这使我们可以将大量的“语言”构建为库例程。  
    第7章：扩展语言：可变变量-本章讨论将用户定义的局部变量与赋值运算符一起添加。  
    这表明在LLVM中构造SSA表单是多么容易：LLVM不需要您的前端就可以构造SSA表单！  
    第8章：编译为目标文件-本章说明如何获取LLVM IR并将其编译为目标文件，就像静态编译器一样。  
    第9章：调试信息-一种真正的语言需要支持调试器，因此我们添加了调试信息，该信息允许在万花筒函数中设置断点，打印出参数变量和调用函数！  
    第10章：结论和其他花絮-本章通过讨论扩展语言的方式来总结本系列，并包括指向“特殊主题”的信息的指针，例如添加垃圾收集支持，异常，调试，对“意大利面条堆栈”的支持等  
    
在本教程结束时，我们将编写少于1000行（非注释，非空白）的代码行。  

借助少量的代码，我们将为非平凡的语言构建一个不错的小型编译器，其中包括手写词法分析器，解析器，AST，以及代码生成支持（静态和JIT）！  

其广度充分证明了LLVM的优势，并说明了为什么它对于语言设计人员和其他需要高性能代码生成的人如此受欢迎。


-   [Chapter #1: Kaleidoscope language and Lexer](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html) \- This shows where we are going and the basic functionality that we want to build. A lexer is also the first part of building a parser for a language, and we use a simple C++ lexer which is easy to understand.
-   [Chapter #2: Implementing a Parser and AST](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl02.html) \- With the lexer in place, we can talk about parsing techniques and basic AST construction. This tutorial describes recursive descent parsing and operator precedence parsing.
-   [Chapter #3: Code generation to LLVM IR](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl03.html) \- with the AST ready, we show how easy it is to generate LLVM IR, and show a simple way to incorporate LLVM into your project.
-   [Chapter #4: Adding JIT and Optimizer Support](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl04.html) \- One great thing about LLVM is its support for JIT compilation, so we’ll dive right into it and show you the 3 lines it takes to add JIT support. Later chapters show how to generate .o files.
-   [Chapter #5: Extending the Language: Control Flow](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl05.html) \- With the basic language up and running, we show how to extend it with control flow operations (‘if’ statement and a ‘for’ loop). This gives us a chance to talk about SSA construction and control flow.
-   [Chapter #6: Extending the Language: User-defined Operators](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl06.html) \- This chapter extends the language to let users define arbitrary unary and binary operators - with assignable precedence! This allows us to build a significant piece of the “language” as library routines.
-   [Chapter #7: Extending the Language: Mutable Variables](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl07.html) \- This chapter talks about adding user-defined local variables along with an assignment operator. This shows how easy it is to construct SSA form in LLVM: LLVM does *not* require your front-end to construct SSA form in order to use it!
-   [Chapter #8: Compiling to Object Files](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl08.html) \- This chapter explains how to take LLVM IR and compile it down to object files, like a static compiler does.
-   [Chapter #9: Debug Information](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl09.html) \- A real language needs to support debuggers, so we add debug information that allows setting breakpoints in Kaleidoscope functions, print out argument variables, and call functions!
-   [Chapter #10: Conclusion and other tidbits](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl10.html) \- This chapter wraps up the series by discussing ways to extend the language and includes pointers to info on “special topics” like adding garbage collection support, exceptions, debugging, support for “spaghetti stacks”, etc.















2.1. Kaleidoscope: Implementing a Language with LLVM[](http://llvm.org/docs/tutorial/index.html#kaleidoscope-implementing-a-language-with-llvm "Permalink to this headline")

[My First Language Frontend with LLVM Tutorial](http://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html)

This is the “Kaleidoscope” Language tutorial, showing how to implement a simple language using LLVM components in C++.

2.2. Kaleidoscope: Implementing a Language with LLVM in Objective Caml[](http://llvm.org/docs/tutorial/index.html#kaleidoscope-implementing-a-language-with-llvm-in-objective-caml "Permalink to this headline")

-   [1\. Kaleidoscope: Tutorial Introduction and the Lexer](http://llvm.org/docs/tutorial/OCamlLangImpl1.html)
-   [2\. Kaleidoscope: Implementing a Parser and AST](http://llvm.org/docs/tutorial/OCamlLangImpl2.html)
-   [3\. Kaleidoscope: Code generation to LLVM IR](http://llvm.org/docs/tutorial/OCamlLangImpl3.html)
-   [4\. Kaleidoscope: Adding JIT and Optimizer Support](http://llvm.org/docs/tutorial/OCamlLangImpl4.html)
-   [5\. Kaleidoscope: Extending the Language: Control Flow](http://llvm.org/docs/tutorial/OCamlLangImpl5.html)
-   [6\. Kaleidoscope: Extending the Language: User-defined Operators](http://llvm.org/docs/tutorial/OCamlLangImpl6.html)
-   [7\. Kaleidoscope: Extending the Language: Mutable Variables](http://llvm.org/docs/tutorial/OCamlLangImpl7.html)
-   [8\. Kaleidoscope: Conclusion and other useful LLVM tidbits](http://llvm.org/docs/tutorial/OCamlLangImpl8.html)

2.3. Building a JIT in LLVM[](http://llvm.org/docs/tutorial/index.html#building-a-jit-in-llvm "Permalink to this headline")

-   [1\. Building a JIT: Starting out with KaleidoscopeJIT](http://llvm.org/docs/tutorial/BuildingAJIT1.html)
-   [2\. Building a JIT: Adding Optimizations – An introduction to ORC Layers](http://llvm.org/docs/tutorial/BuildingAJIT2.html)
-   [3\. Building a JIT: Per-function Lazy Compilation](http://llvm.org/docs/tutorial/BuildingAJIT3.html)
-   [4\. Building a JIT: Extreme Laziness - Using Compile Callbacks to JIT from ASTs](http://llvm.org/docs/tutorial/BuildingAJIT4.html)
-   [5\. Building a JIT: Remote-JITing – Process Isolation and Laziness at a Distance](http://llvm.org/docs/tutorial/BuildingAJIT5.html)

2.4. External Tutorials[](http://llvm.org/docs/tutorial/index.html#external-tutorials "Permalink to this headline")

[Tutorial: Creating an LLVM Backend for the Cpu0 Architecture](http://jonathan2251.github.com/lbd/)

A step-by-step tutorial for developing an LLVM backend. Under active development at [https://github.com/Jonathan2251/lbd](https://github.com/Jonathan2251/lbd) (please contribute!).

[Howto: Implementing LLVM Integrated Assembler](http://www.embecosm.com/appnotes/ean10/ean10-howto-llvmas-1.0.html)

A simple guide for how to implement an LLVM integrated assembler for an architecture.

2.4. Advanced Topics[](http://llvm.org/docs/tutorial/index.html#advanced-topics "Permalink to this headline")

1.  [Writing an Optimization for LLVM](https://llvm.org/pubs/2004-09-22-LCPCLLVMTutorial.html)













