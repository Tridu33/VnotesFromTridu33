# 1. 基于LLVM开发编译器

关键是要生成LLVM IR， 
Lexer---->Parser---->AST--(LLVM C++ API)-->LLVM IR---->LLVM Backend


完美官方例子

如何利用LLVM写一个编译器？ - 求是老伯的回答 - 知乎
https://www.zhihu.com/question/30479779/answer/48352221

https://llvm.org/docs/tutorial/index.html



https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html The Kaleidoscope Tutorial

LLVM: Kaleidoscope 生成IR - ustcsse308的文章 - 知乎
https://zhuanlan.zhihu.com/p/57786865

已有本科编译原理课程的基础，想深入学习实用的编译器，是否适合直接阅读源码？选哪种比较好？ - 蓝色的回答 - 知乎
https://www.zhihu.com/question/265066520/answer/289931008



http://frozengene.github.io/blog/compiler/2014/04/27/compiler_tutori_01 01


http://frozengene.github.io/tags.html#compiler-ref 目录


完美流程斯坦福慕课666flex,scanner到LLVM ir到执行
https://online.stanford.edu/lagunita-learning-platform


使用LLVM + PLY 实现一个C语言子集的玩具编译器 - 咸鱼的文章 - 知乎
https://zhuanlan.zhihu.com/p/28637279





-------------------------------------------------------

编译原理语义分析阶段，现在已经做到了能生成语法树，基于语法树怎样实现语义分析和中间代码生成？ - 蓝色的回答 - 知乎
https://www.zhihu.com/question/20860085/answer/23516732



学习编译原理只是研究lex和yacc吗？ - 咸豆脑儿不加卤的回答 - 知乎 

学校 CS 426 Compiler Construction 的课程基于 LLVM，因为我上的时候教授是 Vikram Adve 。
https://www.zhihu.com/question/67908025/answer/258100498

课程主要流程结构是这样的：

Intermediate Representations
Runtime Environments.
Intermediate Code Generation
Optimization Basics
Dataflow Analysis
Global Optimizations
Register Allocation
Instruction Scheduling





 





























