[TOC]




binary decision diagram


multi-value decision diagram















# 二叉判别图BDD-OBDD


## 

[https://github.com/pytest-dev/pytest-bdd](https://github.com/pytest-dev/pytest-bdd)

pytest-bdd实现了Gherkin语言的子集，以实现自动化项目需求测试并促进行为驱动的开发。  
与许多其他BDD工具不同，它不需要单独的运行程序，并从pytest的功能和灵活性中受益。  
它可以统一单元测试和功能测试，减轻持续集成服务器配置的负担，并允许重用测试设置。  
为单元测试编写的Pytest固定装置可以通过依赖项注入重新用于功能步骤中提到的设置和操作。  
这允许对需求进行真正的BDD正当说明，而无需维护任何包含Gherkin命令性声明的副作用的上下文对象。











## OBDD

C\/C++

[https://github.com/skmuduli92/BDDLib](https://github.com/skmuduli92/BDDLib)

一个库，用于从布尔表达式生成OBDD并为生成的BDD转储.dot文件。




C++

[https://github.com/AndreCascais/OBDD](https://github.com/AndreCascais/OBDD)


Java 硕士论文中的实验性OBDD生成器An experimental OBDD generator from my masters thesis

[https://github.com/h3ssto/OBDDimal](https://github.com/h3ssto/OBDDimal)



julia的OBDD

[https://github.com/albertocasagrande/BinaryDecisionDiagrams](https://github.com/albertocasagrande/BinaryDecisionDiagrams)

Haskell的OBDD

[https://github.com/jwaldmann/haskell-obdd](https://github.com/jwaldmann/haskell-obdd)


## software
[http://biddy.meolic.com/](http://biddy.meolic.com/)


[https://github.com/meolic/biddy](https://github.com/meolic/biddy)


支持多核的二元决策图算法

Biddy是一个多平台的Binary Decision Diagrams程序包。  
它支持纯ROBDD，具有互补边的ROBDD，0-sup-BDD，具有互补边的0-sup-BDD和带标记的0-sup-BDD。



精简和有序的二进制决策图（又名[ROBDD](http://en.wikipedia.org/wiki/Binary_decision_diagram)，尽管为简单起见，在本文中将其称为BDD）是布尔函数的非循环图表示形式。由于此表示形式提供了规范形式，并且在大多数情况下非常简洁，因此被广泛用于协议和数字电路的形式验证。BDD可用于寻找令人满意的布尔表达式分配，并比较两个布尔表达式是否等效。因为为某些大型和复杂的布尔函数构造BDD可能非常耗时，所以我们认为并行化BDD操作以在多核CPU上实现高效执行将很有趣。

我们的并行BDD是基于BuDDy（开源BDD软件包）开发的。在本文中，我将介绍BDD操作的一些关键算法，并介绍我们使它们并行化的方法。我们通过为13位乘法器构建BDD来测试并行BDD的性能，并在16核计算机上获得了10倍的加速。\


（更详细的性能结果在[此博客](https://software.intel.com/content/www/us/en/develop/articles/multicore-enabling-a-binary-decision-diagram-algorithm.html)的第4节中提供。）

BDDNOW：并行BDD软件包


\[1\] Implementation of an Efficient Parallel BDD Package.  Tony Stornetta  and Forrest Brewer.  
\[2\] A Parallel Algorithm for Constructing Binary Decision Diagrams.  Shinji Kimura and Edmund M. Clarke.  
\[3\] BDDNOW: A Parallel BDD Package.  Kim Milvang-Jensen.























