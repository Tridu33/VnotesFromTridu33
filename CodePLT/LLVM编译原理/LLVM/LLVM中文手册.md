# LLVM中文手册










[https://llvm.zcopy.site/docs/langref/](https://llvm.zcopy.site/docs/langref/)





















https://llvm.zcopy.site/docs/programmersmanual/


> 本手册是LLVM程序员手册。 本手册翻译自LLVM官方文档：[http://llvm.org/docs/ProgrammersManual.htm](http://llvm.org/docs/ProgrammersManual.htm)
> 
> **注意**  
> *鉴于本人水平和时间有限，在翻译的过程中难免会有错漏或者不够贴切严谨之处，LLVM官网的文档也会不断更新，本中文手册并保证和官方文档同步更新。*

本文档旨在介绍LLVM中一些重要的类和接口。  
本文档不打算介绍什么是LLVM，LLVM是如何工作的，还有LLVM的代码分析。  
本文假设你已经对LLVM有基本的了解，并对转换，或者分析和维护其中的代码感兴趣。

本文档会给你指导方向，让你可以在不断增长的LLVM架构中的代码中，找到你的方向。请注意，阅读本手册并不能替代LLVM源代码的阅读，所以如果你想查找某些类能做些什么，本文档并不能回答你这个问题，所以你还是得查找源码。LLVM的[doxygen](http://llvm.org/doxygen/)文档，可以方便的让你查找想要的东西。  
本文第一部分介绍使用LLVM过程中，一些常用的知识点，第二部分将会介绍，LLVM的核心类。在日后的文档手册中，将会继续延伸讲解如何使用扩展库，例如dominator，CFG控制流，还有一些有用的工具，例如 `InstVisitor`模版。















