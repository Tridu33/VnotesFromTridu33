


https://link.springer.com/chapter/10.1007/978-3-642-37036-6_8 paper

http://why3.lri.fr/try/ online


http://why3.lri.fr/doc/

http://why3.lri.fr/doc/exec.html 

https://github.com/AdaCore/why3




input

ML或者C的annotated imperative program带标注命令式程序

output
表达为什么程序终止，为什么程序正确的**属性集合**，Coq只是其中一个选择。 cvc4


# 1. Why3



Why3 是一个演绎程序验证的平台。

它为规范和编程提供了一种丰富的语言，称为WhyML，并依赖于自动化和交互式的外部定理证明器来解除验证条件。（请参阅下面支持的证明器列表。）

Why3 带有逻辑理论（整数和实数算术、布尔运算、集合和映射等）和基本编程数据结构（数组、队列、哈希表等）的标准库。 ）。



用户可以直接编写WhyML程序，并通过自动提取机制获得正确构造的OCaml程序。

**coq的Extraction**


WhyML 还用作验证 C、Java 或 Ada 程序的中间语言。（参见使用Why3的项目下。）Why3 可以很容易地扩展支持新的定理证明。通过 OCaml API，Why3 可以用作软件库。


http://why3.lri.fr/




https://www.thinbug.com/q/31426510 将WhyML映射到SMT逻辑的确切机制



















