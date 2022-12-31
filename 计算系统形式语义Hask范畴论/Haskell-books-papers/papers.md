


https://homepages.inf.ed.ac.uk/wadler/

https://homepages.inf.ed.ac.uk/wadler/topics/monads.html 单子系列文章，很好

https://blog.sumtypeofway.com/









# papers




Haskell有哪些推荐阅读的论文？ - 祖与占的回答 - 知乎
https://www.zhihu.com/question/315005729/answer/618034280

























TBH, Haskell 也快奔三到头, 在上面发表的论文真多如牛毛, 如果没有一个方向或者目的, 列举出来的意义也不是特别大. 下面按方向随便大概列举一下:

### Meta

A History of Haskell: Being Lazy With Class - 到目前为止 Haskell 前半生的故事, 虽然后期 GHC 的实现翻天覆地, 但是还是可以了解到 Haskell 设计的初衷和其中一些概念(例如 Monad)引入的历史, 还有唐凤用实现 Perl6 当 TAPL 练习题干进 Haskell 2010 标准作者之一的故事之类的. 以及对 [为什么 Haskell 始终没法流行呢？](https://www.zhihu.com/question/39115733/answer/79902920) 这种问题心里也有个答案.

Confessions of a Used Programming Language Salesman - Getting the Masses Hooked on Haskell, Haskell 98 标准作者之一 Erik Meijer 把 Haskell 的 idea 到各个语言"发扬光大"后的心路历程, 虽然后面搞了 rx, Dart async spec 这种事情没记录进去.

现在拍脑袋就这两篇.

### Haskell 实现

这个真不是我随便就可以列完整的列表, 而且分支也很多, 我来整个 meta-list:

[A Haskell Implementation Reading List](https://link.zhihu.com/?target=http%3A//www.stephendiehl.com/posts/essential_compilers.html)

[ReadingList - GHC](https://link.zhihu.com/?target=https%3A//ghc.haskell.org/trac/ghc/wiki/ReadingList)

[tweag/asterius](https://link.zhihu.com/?target=https%3A//github.com/tweag/asterius/blob/master/docs/readings.md)

[Haskell 实现相关的 reading list](https://link.zhihu.com/?target=https%3A//archive.fo/RglyT)

以及无脑推荐两个 Simon 的所有 paper

### 类型系统

看 Richard A. Eisenberg 的 PhD 论文 [DEPENDENT TYPES IN HASKELL: THEORY AND PRACTICE](https://link.zhihu.com/?target=https%3A//cs.brynmawr.edu/~rae/papers/2016/thesis/eisenberg-thesis.pdf), 找参考文献看应该会比较好







![img](https://pic1.zhimg.com/80/v2-2708383f66ce9c96c074112a3f5e4c16_720w.jpg?source=1940ef5c)

### 语言抽象/模式

Monad 的推荐看 Philip Wadler 的 - [有没有对Haskell中理解monad比较好的代码例子？](https://www.zhihu.com/question/64207539/answer/217887930)

Applicative: [Idioms: applicative programming with effects](https://link.zhihu.com/?target=http%3A//strictlypositive.org/Idiom.pdf)

其他的可以在 [Typeclassopedia - HaskellWiki](https://link.zhihu.com/?target=https%3A//wiki.haskell.org/Typeclassopedia) 找, Profunctor 最近的还没有

Fun with Semirings 这种玩[代数结构](https://www.zhihu.com/search?q=代数结构&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618034280})也挺好玩的

Parser Combinator, 还是推荐 Graham Hutton, Erik Meijer, 复杂的都要自己看实现. 找更原始的可以看 Parsing Techniques 第二版的参考文献.

Recursion Schemes, Paper 都挺不好看的, 看 [Adventures in Uncertainty](https://link.zhihu.com/?target=https%3A//blog.sumtypeofway.com/) 的介绍好多了, 其他可以到 [passy/awesome-recursion-schemes](https://link.zhihu.com/?target=https%3A//github.com/passy/awesome-recursion-schemes) 找

### 数据结构

Okasaki 全家桶 (

succinct data structure 得看 ekmett 的 talk 和库

### 问题解决方案

估计这个[Functional Pearls](https://link.zhihu.com/?target=https%3A//wiki.haskell.org/Research_papers/Functional_pearls) 密集区了

Expression Problem: Data types a la carte

Oleg Kiselyov 问题终结者: Extensible Effects 系列, Implicit Conﬁgurations, Reﬂection without Remorse

ekmett 所以库相关的都推荐

越列越多, 都看得过来吗?







































