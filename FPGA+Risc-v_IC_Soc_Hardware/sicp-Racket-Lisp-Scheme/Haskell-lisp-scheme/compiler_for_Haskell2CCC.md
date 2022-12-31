




# A_supercompiler_for_core_Haskell


https://www.academia.edu/es/2719070/A_supercompiler_for_core_Haskell
# compiler_for_Haskell2CCC







2018-03-09, 10:00, 编辑 3364
扬声器
Solène Mirliaz 和 Elisabet Lobo，查默斯
标题
通过范畴理论解释 Lambda 微积分（非专家的实用编程指南）
抽象的

2018-03-09, 10:00, EDIT 3364
Speaker
Solène Mirliaz and Elisabet Lobo, Chalmers
Title
Interpreting Lambda Calculus via Category Theory (A pragmatic programming guide for the non-expert)
Abstract
Many domain-specific languages are often implemented in a deep embedded fashion in order to enable optimizations. Many of the techniques for EDSL soon or later end up repeating the work of the host compilar---for this pearl, that would be GHC. Recently, a new approach called Compiling to Categories has emerged and promises to avoid such replication of work. It relies on understanding the categorical model of Cartesian Closed Category (CCC). That means that, to use this new technique, it becomes necessary to understand basic category theory and CCC. Unfortunately, when learning about such topics and its relation to functional programs, one faces the risk of diving into mathematical books with difficult-to-penetrate notation, getting lost into abstract notions, and eventually giving up. Instead, this pearl aims to guide Haskell developers to the understanding of all of such abstract concepts via Haskell code. We present two EDSLs in Haskell: one for simple-typed lambda terms and another for CCC and show how to translate programs form one into the other---a well-known result by Lambek in 1985. To achieve the translation, our implementation relies on GHC closed type families. By going into CCC, it becomes possible to give many interpretations to lambda terms, but in this work we only focus on a traditional call-by-value semantics. Hence, we also show how to execute CCC programs via the categorical abstract machine (CAM). Moreover, we extend our implementation of simple-typed lambda calculus with primitive operators, branching, and fix points via appropriated enhancements to CCC and CAM based on category theory concepts. All this journey is going to be grounded in Haskell code, so that developers can experiment and stop fearing such abstract concepts as we did.
This talk is based on a joint-work with Alejandro Russo.

许多特定领域的语言通常以深度嵌入的方式实现，以实现优化。EDSL 的许多技术迟早都会重复主机编译器的工作——对于这颗珍珠，那就是 GHC。最近，出现了一种称为“编译到类别”的新方法，并有望避免这种工作重复。它依赖于对笛卡尔封闭类别（CCC）的分类模型的理解。这意味着，要使用这种新技术，必须了解基本范畴论和 CCC。不幸的是，在学习这些主题及其与函数式程序的关系时，人们面临着潜入难以理解符号的数学书籍、迷失在抽象概念中并最终放弃的风险。反而，这颗珍珠旨在引导 Haskell 开发人员通过 Haskell 代码理解所有这些抽象概念。我们在 Haskell 中展示了两种 EDSL：一种用于简单类型的 lambda 术语，另一种用于 CCC，并展示了如何将程序从一种转换为另一种——这是 Lambek 在 1985 年的著名成果。为了实现转换，我们的实现依赖关于 GHC 封闭型家庭。通过进入 CCC，可以对 lambda 术语进行多种解释，但在这项工作中，我们只关注传统的按值调用语义。因此，我们还展示了如何通过分类抽象机 (CAM) 执行 CCC 程序。此外，我们通过基于类别理论概念的 CCC 和 CAM 的适当增强，使用原始运算符、分支和固定点扩展了简单类型 lambda 演算的实现。
本次演讲基于与 Alejandro Russo 的合作。
https://wiki.portal.chalmers.se/cse/pmwiki.php/FP/FPWeeklyMeeting










