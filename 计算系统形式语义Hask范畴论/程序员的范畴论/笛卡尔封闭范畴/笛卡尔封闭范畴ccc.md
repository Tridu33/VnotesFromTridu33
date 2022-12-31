


https://zh.wikipedia.org/wiki/%E7%AC%9B%E5%8D%A1%E5%84%BF%E9%97%AD%E8%8C%83%E7%95%B4


# 笛卡尔封闭范畴ccc
haskell-to-hardware-via-cccs

conal.net/blog/posts/haskell-to-hardware-via-cccs

如何理解笛卡尔闭范畴以及它与函数式编程的关系？ - 知乎
https://www.zhihu.com/question/35553452/answer/117880521










Cartesian closed category - dreday的文章 - 知乎
https://zhuanlan.zhihu.com/p/72619250 Cartesian closed category是lambda calculus的基础。或者说lambda calculus就是Cartesian closed category的一个模型。其实Cartesian closed category非常简单，就是又Cartesian又closed再curry。但是这样的东西就能构建出lambda calculus，而lambda calculus又是图灵完备的，能达到普通编程语言的能力。


语言背后的代数学（九）：笛卡尔闭范畴 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/35281476




关于haskell - 为什么在 Haskell 中为 Curry 类考虑局部小笛卡尔封闭类别是公平的？

Control.Category.Constrained 是一个非常有趣的项目，它展示了笛卡尔封闭类别的类 - Curry .
然而，我不明白为什么我们会想到所有允许 curry 的笛卡尔封闭范畴。和 uncurry ( Hom(X * Y, Z) ≅ Hom(X, Z^Y) 在范畴论方面)。 Wikipedia说这样的性质只适用于局部小的笛卡尔封闭类别。下 this post很多人建议哈斯克 本身并不小(另一方面，每个人都说 Hask is not a cartesian closed category ，我认为这是纯粹而无趣的形式主义)。
在 this post在 Math.SE谈到假设所有类别都是局部小的。但它是从我们讨论属性的数学角度给出的。我想知道为什么我们决定专注于 curry和 uncurry如 Curry 的方法。是不是因为几乎每个了解 Haskell 的人也都知道这些函数？还是有其他原因？


https://stackoverflow.com/questions/62994618/why-is-it-fair-to-think-of-just-locally-small-cartesian-closed-categories-in-has



作为图书馆作者，我可以自信地回答这个问题，答案是 是 : 是因为curry和 uncurry是 Haskell 白话中公认的一部分。 constrained-categories从来没有打算从根本上改变 Haskell 和/或使其在某种意义上在数学上更可靠，而是巧妙地概括现有的类层次结构——主要是为了允许定义无法给出的仿函数等 Prelude.Functor实例。
是否Curry坦率地说，我不知道可以根据本地的小规模进行正式化。我也不确定这个和其他“数学基础”方面是否可以在 Haskell 库的上下文中进行有意义的讨论。 前面有点跑题了 Haskell 是一种非完整语言，这只是一个事实，是的，这意味着几乎任何公理都可能被某些 undefined 所阻挠。攻击。但我也不认为这是一个问题。许多人似乎认为 Haskell 是一种恐怖谷:在实际应用中使用限制太多，但没有任何东西可以被正确证明。我的看法正好相反:Haskell 有一个足够强大的类型系统，能够表达对现实世界应用程序有用的数学思想，而不会使其值语义陷入底层基础中太深而无法实用在现实世界中实际使用。 (也就是说，你不会经常花几周时间证明一些“显然这是真的……”定理。我在看着你，Coq……)我们没有写出 100% 严格的证明，而是尽可能地缩小类型尽可能，然后使用 QuickCheck 来查看某些东西是否通常按数学要求工作。
不要误会我的意思，我认为形式化基础也很重要，依赖类型的总语言很棒，但是所有这些都有些忽略了 Haskell 的潜力真正所在的点。至少这不是我开发 Haskell 的目标，包括 constrained-categories .如果有人对纯数学有更深入的了解，我很高兴听到这个消息。













