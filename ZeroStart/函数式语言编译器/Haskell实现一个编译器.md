# Haskell实现一个编译器



如何写一个简单的编译器？ - aaaron7的回答 - 知乎
https://www.zhihu.com/question/36756224/answer/88530013








prerequisite: 懂 state monad就行了

第一篇，《How to build a monadic interpreter in one day》

http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.368.2522

跟着做，可以完成一个简单的backend， 也就是架构基本的AST 并执行的步骤。

然后到frontend， 也就是parser的部分你就会发现你看不懂了， 这个时候看第二篇。（因为该文的 parser 部分其实是 第二篇 的一个浓缩版，所以不看第二篇基本很难看懂这个部分）



第二篇，《Monadic Parser Combinator》 ，

http://www.cs.nott.ac.uk/~pszgmh/monparsing.pdf

看了也就能对照第一篇，把 parser 写出来了， 然后就能和之前的backend 组合，完成一个基本的，完全由自己手写的，monadic的解释器（parser 和 backend 分别由一个自定义的 state monad 实现）。顺便加深对 monad 的理解。

看第二篇的时候，回过头对照第一篇看效果会更高，虽然逻辑一样，但第二篇是用 monad comprehension 的形式来写， 第一篇是用 do notation 来写。有的复杂的地方你两种方式对照看一下，会有茅塞顿开的效果。

然后再看第三篇


第三篇，llvm的haskell 教程，

Implementing a JIT Compiler with Haskell and LLVM ( Stephen Diehl ) https://www.stephendiehl.com/llvm/#code-generation-setup
， 把你的backend 换成llvm. （注：事先对 llvm 不熟的话，可以和 hackage 上面 llvm-general, llvm-general-pure 这两个库的 wiki, 以及
https://llvm.org/docs/LangRef.html#module-structure
LLVM Language Reference Manual
对照着看）

至于frontend， 可以换成Parsec之类，但也可以就不断扩充之前自己写的版本。

齐活儿~

------

今天闲着没事儿，撸了一个 swift 的版本，

GitHub - aaaron7/swift_monadic_parser: A simple haskell-style monadic combinator-based parser written in Swift. https://github.com/aaaron7/swift_monadic_parser
仅包含最基本的 parser 和 interpreter 的功能，写法完全按照前面两篇文章的思路实现，有兴趣可以看看。