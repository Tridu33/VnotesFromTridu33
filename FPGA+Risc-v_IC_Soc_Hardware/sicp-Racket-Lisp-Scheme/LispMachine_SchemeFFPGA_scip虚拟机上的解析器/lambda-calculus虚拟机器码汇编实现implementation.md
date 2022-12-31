


# lambda-calculus实现implementation

函数式编程的汇编实现步骤:
https://stackoverflow.com/questions/67594976/example-assembly-machine-instruction-from-lambda-calculus
步骤基本上是：

唯一重命名（可以同时进行范围检查）
选择性或整个程序转换为 ANF 或 CPS（涉及创建新名称）
ANF 或 CPS 特定的优化（一般的事情，如 uncurrying、内联扩展、死代码删除、常量折叠、元组参数展平等）
闭包转换（可能会采用消除策略，例如已知闭包的 lambda 提升、使用 SCC 的修复最小化等）
吊装
进一步降低为更像机器的三（或二）地址代码 IR，它为处理由转换引入的辅助结构提供了更明确的细节
将该 IR 降低为特定于目标的汇编语言
当涉及到严格的函数式语言的编译时，这绝对不是全部。例如，如果我们将我们的语言扩展为具有命名的、相互递归的函数，则希望将闭包共享工作到我们的闭包转换转换中（并消除不需要闭包的情况）。

，编译 Scheme 至少有两个特别有趣的参考资料。

第一个（或几乎是第一个）Scheme 编译器被称为“Rabbit”，由 Guy Steele 编写。我不知道 Rabbit 本身是否仍然可用，但Steele 关于它的论文是，并且这里有一个文本版本，表面上看起来更具可读性，但有问题。

编译的 Scheme 方言 Rabbit 是现代 Scheme 的一个相当遥远的祖先：我认为在论文中对其进行了足够的描述，以了解它是如何工作的。

Rabbit 编译为MACLISP而不是机器语言。所以现在还有另一个问题：你如何编译 MACLISP？但事实上，它编译为 MACLISP 的一个极其受限的子集，我认为它可以相当容易地看出它是如何变成机器代码的。

第二个有趣的参考是向导书：计算机程序的结构和解释。 SICP 的第 5 章是关于注册机及其编译。它为它定义了一个简单的寄存器机器和一个用于Scheme（或Scheme的子集）的编译器的实现。 图 5.17，第 597 页和第 597 页包含factorial书中定义的寄存器机器的明显递归函数的编译输出。

最后：SICP 的那一章有 120 页长：这就是为什么这个问题对于 Stack Overflow 来说太大了。




您可以机械地将 λ-演算转换为另一种语言。如果其他语言有宏和一阶函数之类的东西，它会有所帮助，但如果你愿意努力工作

，编译 Scheme 至少有两个特别有趣的参考资料。

第一个（或几乎是第一个）Scheme 编译器被称为“**Rabbit**”，由 Guy Steele 编写。我不知道 Rabbit 本身是否仍然可用，但Steele 关于它的论文是，并且这里有一个文本版本，表面上看起来更具可读性，但有问题。

编译的 Scheme 方言 Rabbit 是现代 Scheme 的一个相当遥远的祖先：我认为在论文中对其进行了足够的描述，以了解它是如何工作的。

Rabbit 编译为MACLISP而不是机器语言。所以现在还有另一个问题：你如何编译 MACLISP？但事实上，它编译为 MACLISP 的一个极其受限的子集，我认为它可以相当容易地看出它是如何变成机器代码的。

第二个**有趣的参考是向导书：计算机程序的结构和解释**。https://mitpress.mit.edu/sites/default/files/sicp/code/index.html  SICP 的第 5 章是关于注册机及其编译。它为它定义了一个简单的寄存器机器和一个用于Scheme（或Scheme的子集）的编译器的实现。 图 5.17，第 597 页和第 597 页包含factorial书中定义的寄存器机器的明显递归函数的编译输出。

最后：SICP 的那一章有 120 页长：这就是为什么这个问题对于 Stack Overflow 来说太大了。

《计算机程序的构造和解释（SICP）》讨论的核心问题是什么？ - DeathKing的回答 - 知乎
https://www.zhihu.com/question/26549715/answer/34336593


------------------------------------------------------
## scheme-lisp翻译成llvm IR，并通过llvm生成机器码
如何将lisp/scheme翻译成llvm IR，并通过llvm生成机器码？ - LdBeth的回答 - 知乎
https://www.zhihu.com/question/24378697/answer/589195962

------------------------------------------------------

《tapl》 type and program language实现了五类型lambda演算及其F-system
## paper


A Certified Type- Preserving Compiler from Lambda Calculus ...
adam.chlipala.net/papers/CtpcPLDI07/CtpcPLDI07Talk.pdf

https://www.researchgate.net/publication/213880063_A_certified_type-preserving_compiler_from_lambda_calculus_to_assembly_language







----------------------------------------





https://github.com/chrisnevers/lambda-calculus

该项目是 OCaml 中 lambda 演算的实现。希望它可以作为其他想要了解以下内容的指南：

Lambda 演算
门希尔
类型推断
等等。


----------------------------------------



lambda_calculus是 Safe Rust 中纯 lambda 演算的简单零依赖实现。
https://github.com/ljedrz/lambda_calculus


----------------------------------------


GitHub - hallettj/LambdaCalculus: Scala implementation of ...
https://github.com/hallettj/LambdaCalculus

----------------------------------------



Dart实现的Lambda 演算解析器和评估器。
用来使用import 'package:lambda_calculus/lambda_calculus.dart';这个库。

起初我想用函数式语言来编程它Haskell，但后来我决定练习编写函数而不使用递归。我选择使用它进行编程是dart因为它可以在javascript必要时轻松转换并部署到网络上。

目前，它支持纯无类型的 Lambda 演算。接下来我将介绍布尔值和整数等字面量。

有关示例，请参见此处。
https://github.com/sorrowfulT-Rex/Dart-Lambda-Calculus


----------------------------------------


https://jacksongl.github.io/files/demo/lambda/#secondPage
lambda演算在线解析器


----------------------------------------



Implementing the lambda calculus in Ink | Ink
https://dotink.co/posts/lambda

在 Ink 中实现 lambda 演算


----------------------------------------





LCI - A lambda calculus interpeter
www.chatzi.org/lci



----------------------------------------

https://cloudmark.github.io/Lambda-Calculus/定义了一个模型，使用λ-演算可以应用于常见的 SEO 问题，即检索所有站点 URL 的问题和检索所有备用 URL 的问题。





































