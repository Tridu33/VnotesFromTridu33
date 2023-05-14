[TOC]
# 1. LLVM官网教程入门




 
[https://releases.llvm.org/](https://releases.llvm.org/)














[https://llvm-doc-zh-cn.readthedocs.io/zh_CN/latest/index.html](https://llvm-doc-zh-cn.readthedocs.io/zh_CN/latest/index.html)

LLVM中文手册


 LLVM中文网







https://llvm.zcopy.site










[https://llvm.zcopy.site/docs/langref/](https://llvm.zcopy.site/docs/langref/)









如何学好用好LLVM？ - 蓝色的回答 - 知乎
https://www.zhihu.com/question/309889585/answer/594694544










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




# 2. LLVM书入门资料


LLVM 怎样入门和上手？ - 宓俊的回答 - 知乎
https://www.zhihu.com/question/20236606/answer/14436040


深入研究Clang(十四) clang-tidy的使用 - 小乖他爹的文章 - 知乎 https://zhuanlan.zhihu.com/p/105703209


深入研究Clang(十三) clang-tidy简介 - 小乖他爹的文章 - 知乎 https://zhuanlan.zhihu.com/p/102248131


（四）LLVM IR概述 - Euler Chen的文章 - 知乎 https://zhuanlan.zhihu.com/p/102716482




这是 The Architecture of Open Source Applications 一书中关于 LLVM 的章节，由 LLVM 作者 Chris Lettner 亲自撰写。是我见过最好的 LLVM 入门读物。
http://www.aosabook.org/en/llvm.html





















LLVM 怎样入门和上手？ - 宓俊的回答 - 知乎 https://www.zhihu.com/question/20236606/answer/14436040













如果你想实践，结合编译原理与LLVM的话，请跟着LLVM Tutorial一步一步做下来吧，你会收获很多的，请猛击：[LLVM Tutorial: Table of Contents](https://link.zhihu.com/?target=http%3A//llvm.org/docs/tutorial/index.html)




[http://www.aosabook.org/en/llvm.html](https://link.zhihu.com/?target=http%3A//www.aosabook.org/en/llvm.html)  
这是 The Architecture of Open Source Applications 一书中关于 LLVM 的章节，由 LLVM 作者 Chris Lettner 亲自撰写。是我见过最好的 LLVM 入门读物。








er和passer了．[LLVM Tutorial: Table of Contents](https://link.zhihu.com/?target=http%3A//llvm.org/docs/tutorial/index.html)　這個tutorial看完3，就要學llvm的api，從下面的  
[Getting Started with the LLVM System](https://link.zhihu.com/?target=http%3A//llvm.org/docs/GettingStarted.html%23id17)開始吧．  
開始回答這個問題，當然是看官網，源碼和作者的鏈接:  
１．還有不要下官網svn的代碼，用github上的mirror，方便自己建立branch，方便自己checkout到某個commit point，然後一點點patch，感覺像放電影．不過這樣也是很坑的，我說的是時間．  
[Getting Started with the LLVM System](https://link.zhihu.com/?target=http%3A//llvm.org/docs/GettingStarted.html%23id17)原來本來就有git，我也是剛學，不好意思，本來真不想這麼狂妄的～～  
２．官網的有很多文檔，沒有翻完，每篇前面都有introduction和toc，這個真不錯的．  
３．作者的官網，太好了，有很多他自己寫的文檔，下載地址都在官網～～，還有就是好多undocumented的文檔．真是寶庫，不解釋．這條線最成體系吧．recommend:-)  
Reference:  
[Chris Lattner's Homepage](https://link.zhihu.com/?target=http%3A//www.nondot.org/sabre/)  
[LLVM](https://link.zhihu.com/?target=http%3A//en.wikipedia.org/wiki/LLVM) \-\- wiki中的reference我幾乎都點過了:-(





















