







使用一种可移植的汇编语言，该语言可以由前端生成并由多个代码生成器中的任何一个实现。这种语言应充当高级编译器与可重定目标的优化代码生成器之间的 接口。

前端的作者和代码生成器的作者可以轻松地合作。 C--是那种语言。


https://en.wikipedia.org/wiki/C--



GHC 7, GHC uses LLVM for code generation. Use the -fllvm flag.

有很多原因使C--可以比LLVM更好，也可以解释为什么它们实际上不是完全一样的。
https://stackoverflow.com/questions/815998/llvm-vs-c-how-can-llvm-fundamentally-not-be-better-for-haskell-than-c
C--比LLVM具有更高的抽象级别；例如，我们可以使用C--生成代码，其中的堆栈指针是完全隐式的，并且仅在以后的编译过程中进行显示。这使得应用某些类型的优化变得更加容易，因为更高级别的表示允许更多的代码运动而不变性更小。

在我们积极寻求解决此问题的同时，LLVM也遇到了与Via-C后端同样的问题：它要求我们创建proc点。什么是触发点？从本质上讲，因为Haskell不使用经典的调用/重调用约定，所以每当我们使子过程调用在道德上等效时，我们都需要将连续性推入堆栈，然后跳转到子过程。这个延续通常是一个局部标签，但是LLVM要求它是一个实际的过程，因此我们需要将函数分成较小的部分（每个部分称为proc点）。对于在过程级别上运行的优化而言，这是个坏消息。

C--和LLVM采用不同的方法进行数据流优化。LLVM使用带有phi-nodes的传统SSA样式：C--使用一个名为Hoopl的酷框架，它不需要您维护SSA不变式。我可以确认：尽管某些类型的优化（想到的是一次性使用的变量的内联）在这种数据流设置中并不是最自然的，但是Hoopl中的编程优化非常有趣。




# 1. C--



https://news.ycombinator.com/item?id=6621679


C--也是ghc编译器在代码生成之前的最终代表（即“本机”后端，llvm后端和未注册的gcc C后端）。

我可能还会说几句话，但这涵盖了基础知识。我也参与了GHC开发，实际上在编译器的c相关位上做了一些工作。

相关：我有一些玩具C片段，您可以使用GHC进行编译和基准测试，这是我几个月前发表的演讲https://bitbucket.org/carter/who-ya-gonna-call-talk-may- 2013 ... https://vimeo.com/69025829

我还应该补充一点，GHC <= 7.6中的C--没有函数参数，但是在GHC HEAD / 7.7以及不久的7.8中，您可以在C--函数中使用漂亮的函数args。请参阅https://github.com/ghc/ghc/blob/master/rts/PrimOps.cmm以获取GHC HEAD示例，与 https://github.com/ghc/ghc/blob/ghc-7.6/rts/PrimOps相比较。 cmm为旧样式。


	
X4 ，2013年10月27日 [–]

代码示例：http : //www.cs.tufts.edu/~nr/c--/download/c--exn.pdf
幻灯片：http：//www.cs.tufts.edu/~nr/c--/download/c--exnslides.ps.gz

音频：http：//wino.eecs.harvard.edu：8080 / ramgen / nr-pldi00.rm

手册：http：//www.cs.tufts.edu/~nr/c--/extern/man2.pdf

该手册包含规范和一些代码示例。看起来很容易学习，但与其他语言有点不同。






































