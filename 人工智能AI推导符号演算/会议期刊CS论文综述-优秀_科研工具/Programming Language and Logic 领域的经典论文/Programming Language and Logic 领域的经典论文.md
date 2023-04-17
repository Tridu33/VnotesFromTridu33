# 1. Programming Language and Logic 领域的经典论文







这里有一份由 Karl Crary 整理的 Programming Language and Logic 领域的经典论文：http://www.cs.cmu.edu/~crary/819-f09/ 。其中有不少划时代意义的 paper ，比如
[Gentzen35] Investigations into Logical Deduction，引入了相继式（Sequent）演算。
[McCarthy60] Recursive Functions of Symbolic Expressions and Their Computation By Machine，引入了 Lisp 。
[Hoare69] An Axiomatic Basis for Computer Programming，提出了关于证明程序正确性的公理化方法（公理语义）。
等等……






如何评价Classic Papers in PL and Logic中的相关论文？ - rainoftime的回答 - 知乎
https://www.zhihu.com/question/43444495/answer/95827958




谢朋友邀请。。谈不上点评，就说几句自己的感受。 （注：不考虑那个列表中太古老（30年代）的以及Monad相关的。）
从三个方面总结：形式语义、语言设计、其他

1. 形式语义和逻辑
先上一个图：


公理语义
C. A. R. Hoare.
An Axiomatic Basis for Computer Programming. 1969. (pdf)
Communicating Sequential Processes. 1978. (pdf)
（我好像漏了几篇？）
公理语义是为了方便证明程序正确性。个人认为可以不限于Hoare-style的框架，
更一般地，一个program可以有不同“program logic”。用于程序建模和验证的还有termporal logic, dynamic logic等等。脑洞大一点，abstract interpretation也可以看作一种，比如可以order by implication, abstract transformation as deduction...

公理语义和操作、指称语义的密切相关的：其推演规则和正确性取决于操作和指称语义。

操作和指称语义
Dana Scott and Christopher Strachey. Towards a Mathematical Semantics for Computer Languages. 1971. (pdf, now with page 20)
Christoper Strachey. Fundamental Concepts in Programming Languages. 1967. (pdf)
Gordon Plotkin. A Structural Approach to Operational Semantics. 1981. (pdf)

必须强调地是，操作、指称语义是很严肃而有技术含量的东西，虽然现在的很多文章中它们并不重要，多为用来装x，还不时有错误。（一代不如一代。。）。举个例子，无类型lambda演算的指称语义到现在还有人在研究！

个人认为Dana Scott对Domain theory的研究比他得图灵奖的那个工作意义大（当然Scott也不怎么把图灵奖当回事。。）

2. 语言设计
John McCarthy. Recursive Functions of Symbolic Expressions and Their Computation By Machine, Part I. 1960. (pdf)。 LISP的诞生

P. J. Landin. The Next 700 Programming Languages. 1966. (pdf) 。预言了未来几十年的发展

John Backus. Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs. 1978. (pdf)，好像是Backus的图灵演讲，函数式语言经典安利文章。

下面是John Reynolds专场：
Definitional Interpreters for Higher-Order Programming Languages. 1972. (ps)
The Essence of Algol. 1981. (ps)
Types, Abstraction, and Parametric Polymorphism. 1983. (pdf)
....
Reynolds真乃神人，推荐上面答主提的The Essence of Reynolds。略遗憾地是，很多人只知道他晚年提出的separation logic。另外Reynolds貌似没获图灵奖（我觉得也不需要了）。。

3. 其他
Linear Logic
Jean-Yves Girard. Linear Logic. 1987. (pdf)
Linear Logic对Logic, Programming Language等领域都有深远影响。不展开了。。。










