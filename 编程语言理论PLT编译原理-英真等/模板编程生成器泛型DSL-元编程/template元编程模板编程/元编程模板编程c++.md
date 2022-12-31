


[TOC]



[电子书c++模板编程](https://wizardforcel.gitbooks.io/effective-cpp/content/50.html)


[大佬牛皮https://github.com/wuye9036/CppTemplateTutorial](https://github.com/wuye9036/CppTemplateTutorial)
# 1. 元编程模板编程c++


[入门](https://www.bilibili.com/video/BV1hE41137cA?from=search&seid=10264141047788244467)
重学C++[Modern C++]:从模板元编程到 constexpr!

卖的c++模板 https://www.bilibili.com/video/BV1UE411j7AC?from=search&seid=10264141047788244467

这里讲了vs 2019调试menmery输入“&aaa”查看变量aaa内存，介绍反汇编代码的执行查看，介绍watch"shift+F9"查看变量，正常加断点之类的操作必须自己会。

一个solution解决方案对应多个projects,然后c++标准可以自行选择

>dumpbin /all  CppTemplateTutorial.obj >> dumpbin_cpp_obj.txt


https://www.bilibili.com/video/BV1Dy4y1i7Ny?from=search&seid=10264141047788244467
搬运
https://www.youtube.com/watch?v=KYMxD9q6Ybc&list=PL1_C6uWTeBDE6KepUEI9XeOpLc4hgD
现代c++编程之模板类型编程。很容易中国人听懂的英语，而且也基本都打字了，就不搬字幕了。还是比较推荐，进一步深入学习c++。



https://github.com/seaside2mm/cplusplus-deeper-resource/tree/master/TypeFunction-Tutorials






浅谈 C++ 元编程 - BOT Man的文章 - 知乎
https://zhuanlan.zhihu.com/p/87917516
https://bot-man-jl.github.io/articles/?post=2017/Cpp-Metaprogramming#%E6%B5%8B%E8%AF%95%E7%B1%BB%E5%9E%8B

>利用元编程，可以很方便的设计出 类型安全 (type safe)、运行时高效 (runtime effective) 的程序。到现在，元编程已被广泛的应用于 C++ 的编程实践中。例如，Todd Veldhuizen 提出了使用元编程的方法构造 表达式模板 (expression template)，使用表达式优化的方法，提升向量计算的运行速度 [21]；K. Czarnecki 和 U. Eisenecker 利用模板实现 Lisp 解释器 [22]。
尽管元编程的应用场景各不相同，但都是三类基本应用的组合：**数值计算 (numeric computation)、类型推导 (type deduction) 和 代码生成 (code generation)**。例如，在 BOT Man 设计的 对象关系映射 (object-relation mapping, ORM) 中，主要使用了 类型推导 和 代码生成 的功能。根据 对象 (object) 在 C++ 中的类型，推导出对应数据库 关系 (relation) 中元组各个字段的类型；将对 C++ 对象的操作，映射到对应的数据库语句上，并生成相应的代码。[23] [24]











































