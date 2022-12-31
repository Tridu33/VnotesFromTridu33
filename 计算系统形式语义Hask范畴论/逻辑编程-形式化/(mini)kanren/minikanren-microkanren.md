[TOC]






https://www.cnblogs.com/skabyy/p/13199800.html 逻辑式编程语言极简实现（使用C#） 

- 逻辑式编程语言介绍

能不能有人简单的解释下 miniKanren 的实现方式？ - bhuztez的回答 - 知乎 
https://www.zhihu.com/question/34416029/answer/58588651
https://www.zhihu.com/question/34416029
minikanren实现 合一 回溯 github有很多版的语言实现




相信很多朋友对于逻辑式编程语言，都有一种最熟悉的陌生人的感觉。一方面，平时在书籍、在资讯网站，偶尔能看到一些吹嘘逻辑式编程的话语。但另一方面，也没见过周围有人真正用到它（除了SQL）。

遥记当时看《The Reasoned Schemer》（一本讲逻辑式编程语言的小人书），被最后两页的解释器实现惊艳到了。看似如此复杂的计算逻辑，其实现竟然这么简洁。不过碍于当时水平有限，也就囫囵吞枣般看了过去。后来有一天，不知何故脑子灵光一闪，把图遍历和流计算模式联系在一起，瞬间明白了《The Reasoned Schemer》中的做法。动手写了写代码，果然如此，短短两百来行代码，就完成了解释器的实现，才发现原来如此简单。很多时候，并非问题本身有多难，只是没有想到正确的方法。

本系列将尽可能简洁地说明逻辑式编程语音的原理，并实现一门简单的逻辑式编程语言。考虑到C#的用户较多，因此选择用C#来实现。实现的这门语言就叫NMiniKanren。文章总体内容如下：

    NMiniKanren语言介绍
    语言基础
    一道有趣的逻辑题：谁是凶手
    NMiniKanren运行原理
    构造条件关系图，遍历分支
    代入消元法解未知量
    实现NMiniKanren
    流计算模式简介
    代入消元法的实现
    遍历分支的实现




#  minikanren


能不能有人简单的解释下 miniKanren 的实现方式？ - 知乎
https://www.zhihu.com/question/34416029/answer/130195618

能不能有人简单的解释下 miniKanren 的实现方式？ - bhuztez的回答 - 知乎
https://www.zhihu.com/question/34416029/answer/58588651








minikanren-


http://minikanren.org/

https://github.com/miniKanren/miniKanren

https://github.com/minikanren

https://en.wikipedia.org/wiki/MiniKanren

python逻辑编程之kanren
https://github.com/logpy/logpy

https://pypi.org/project/kanren/

 https://www.yiibai.com/ai_with_python/ai_with_python_logic_programming.html





miniKanren是用于关系编程的一系列编程语言。[1]由于关系是双向的，因此如果给miniKanren一个表达式和所需的输出，则miniKanren可以运行表达式“向后”，找到该表达式的所有可能的输入，以产生所需的输出。这种双向行为使用户可以同时限制程序的输入和程序的结果。miniKanren执行交错搜索，最终将找到存在的任何解决方案，即使搜索树的任何一个分支都无限长且不包含任何解决方案。如果不存在任何解决方案，则如果搜索树是无限的，miniKanren可能会永远搜索。

miniKanren代码的一个示例是evalo，一个关系目标，该关系目标使表达式与其求值的值相关联。当evalo被称为miniKanren像这样：(evalo q q)，它会产生基内斯，就是表情q，当运行将评估自己。[2]

《The Reasoned Schemer》一书使用miniKanren演示关系编程，并在Scheme中提供了完整的实现。[3]该语言的核心适合两页印刷。miniKanren的Scheme实施旨在易于理解，修改和扩展。

αleanTAP是用αKanren编写的程序，αKanren是miniKanren的标称逻辑的扩展。给定一个定理，它可以找到一个证明，使其成为定理证明者。给定证明，它可以找到定理，使其成为定理检验器。给定证明的一部分和定理的一部分，它将填充证明和定理的缺失部分，从而使其成为定理探索者。[1]

在Haskell，Racket，Ruby，Clojure，JavaScript，Scala，Swift和Python中有miniKanren的实现。规范的实现是Scheme中的嵌入式语言。Clojure的core.logic库是受miniKanren启发的。

kanren这个名字来自日语单词（关连），意思是“关系”。





miniKanren是用于逻辑编程的嵌入式领域特定语言。 
miniKanren核心语言非常简单，只有三个逻辑运算符和一个接口运算符。
在这个简短的交互式教程中，介绍了使用Scheme作为宿主语言的核心语言。 

miniKanren已以越来越多的宿主语言实现，包括Scheme，Racket，Clojure，Haskell，Python，JavaScript，Scala，Ruby，OCaml和PHP等许多其他语言。 

miniKanren的设计易于修改和扩展；
扩展包括约束逻辑编程，概率逻辑编程，标称逻辑编程和制表。


--------------------------------------------------------------------


miniKanren是Dan Friedman在他的书《The Reasoned Schemer》中用来介绍逻辑编程的一个小巧的教学语言。其官网有相关资料和各种语言的实现。


μKanren:AMinimalFunctionalCoreforRelationalProgramming  chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://webyrd.net/scheme-2013/papers/HemannMuKanren2013.pdf

对miniKanren进行了进一步的精炼，整个语言的scheme实现只有40多行（参见代码仓库）。亲自动手实现一下microKanren可谓是学习逻辑编程的最佳方法。

目标
为了便于将来理解和修改，我决定采用Rust语言，以更接近命令式语言的思路去实现。

官网上虽然有不少语言的实现，但是感觉都受到原始实现的很大影响，都是一股浓浓的lisp的味道。

参考资料
首先是看原始论文和实现。论文附带的实现虽然只有40多行，但那是得益于scheme的强大表达能力，其实里面的东西还是不少的。

看了一天，感觉对语言大概了解了，但是实现上还有很多点没弄清楚。

这时有个视频对我帮助很大。其实这个视频也没讲什么特别的东西，只是现场把原始实现写了一遍。但是通过展示这40多行代码是怎么一点一点加上来的，每一点修改解决了什么问题。而且里面还通过交互命令行在每一个步骤都展示了例子。这让我一下子就把之前的问题全都想通了。很多时候直接看最终代码，是很难理解的，但是如果看到了过程，就容易多了。


 

# microkanren
microKanren是2013年由Dan Friedman的学生在一篇论文<µKanren: A Minimal Functional Core for Relational Programming>中提出的。http://minikanren.org/workshop/2020/minikanren-2020-paper2.pdf

μKanren:AMinimalFunctionalCoreforRelationalProgramming  chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://webyrd.net/scheme-2013/papers/HemannMuKanren2013.pdf


对miniKanren进行了进一步的精炼，整个语言的scheme实现只有40多行（参见代码仓库）。亲自动手实现一下microKanren可谓是学习逻辑编程的最佳方法。

目标
为了便于将来理解和修改，我决定采用Rust语言，以更接近命令式语言的思路去实现。

官网上虽然有不少语言的实现，但是感觉都受到原始实现的很大影响，都是一股浓浓的lisp的味道。

参考资料
首先是看原始论文和实现。论文附带的实现虽然只有40多行，但那是得益于scheme的强大表达能力，其实里面的东西还是不少的。

看了一天，感觉对语言大概了解了，但是实现上还有很多点没弄清楚。

这时有个视频对我帮助很大。其实这个视频也没讲什么特别的东西，只是现场把原始实现写了一遍。但是通过展示这40多行代码是怎么一点一点加上来的，每一点修改解决了什么问题。而且里面还通过交互命令行在每一个步骤都展示了例子。这让我一下子就把之前的问题全都想通了。很多时候直接看最终代码，是很难理解的，但是如果看到了过程，就容易多了。








https://github.com/mndrix/microkanren-prolog

https://gist.github.com/cheery/d89bfb4c8d6c7a3eb908 python实现







https://github.com/jasonhemann/microKanren




https://rink1969.github.io/learn-microKanren microKanren学习笔记

之前提到逻辑编程对于区块链的Dapp编程模型非常有帮助。

我虽然很早之前也简单的学过一点Prolog，但是对其实现并没有深入的了解。

要实现一个用于Dapp框架的逻辑编程引擎，还是需要不少改动，因此有必要对其实现进行一些了解。



https://stackoom.com/question/4GBS3

https://docs.racket-lang.org/minikanren/index.html


http://minikanren.org/



https://github.com/topics/minikanren
https://github.com/xavierpinho/microKanren-demo

https://github.com/minikanren


# kanren

https://github.com/brandonwillard/kanren

logic programming in python



























