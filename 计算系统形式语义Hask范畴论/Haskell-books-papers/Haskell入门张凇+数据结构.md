# How Learn
https://www.zhihu.com/question/20193745 如何学习Haskell


1.找本书，把语法看一下  
2.把这里的问题一个个过一遍：[http://www.haskell.org/haskellwiki/H-99:\_Ninety-Nine\_Haskell_Problems](http://link.zhihu.com/?target=http%3A//www.haskell.org/haskellwiki/H-99%3A_Ninety-Nine_Haskell_Problems)  
3.做[http://projecteuler.net](http://link.zhihu.com/?target=http%3A//projecteuler.net) 上的题目  
4.做些小项目

  《仙境中的Haskell》https://zhuanlan.zhihu.com/p/21371274
  
作者：dccmx  
链接：https://www.zhihu.com/question/20193745/answer/14287161  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 练手项目
https://www.zhihu.com/question/61225796/answer/185412037












# 如何使用 haskell 写出高效代码刷算法比赛题目？
https://www.zhihu.com/question/27208859/answer/73683455
由于haskell是纯函数式的，算法比赛中常见的数据结构上update-query模式的问题，都不得不每一次update对整个数据结构进行重建，这样效率会很低，很容易超时。提高haskell代码性能有什么经验？


你认为最优美的数据结构是什么？
如题。https://www.zhihu.com/question/32163076/answer/254083860

https://github.com/bitemyapp/learnhaskell

[Learn You a Haskell for Great Good!](http://learnyouahaskell.com/chapters)

www.iqiyi.com/paopao/u/1355304922/

<算法新解>

www.ituring.com.cn/book/1907

https://github.com/liuxinyu95/AlgoXY






# 源码项目

[有什么值得推荐的Haskell开源项目阅读？](https://www.zhihu.com/question/26875812/answer/34703146)







# Haskell to WebAssembly
https://zhuanlan.zhihu.com/p/53187416





# 剖析Haskell应用架构

https://zhuanlan.zhihu.com/p/21898460
## 有没有比较实用、成熟的 Haskell 应用？

https://www.zhihu.com/question/20246934/answer/15262041

# 工作
Haskell用在工程項目中有什麼優勢？
haskell的wiki上有汇总总结，基本上是一年两期，今年还只有上半年的第一期。https://www.haskell.org/haskellwiki/Haskell_Communities_and_Activities_Report你感兴趣可以去看看那些实践者们都是用在什么场合就大概可以体会一点haskell在工程中的优势了。其实我看这个报告的时候有些失望，因为工程项目确实是少，当然这是符合haskell的热度排名情况的(常年40左右)。haskell最能体现工程层面优势的项目应该是，io少，内存不紧张，业务逻辑特别复杂且多变的项目。

作者：随心所往
链接：https://www.zhihu.com/question/26510008/answer/33050372
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# Google 或者 Facebook 有什么项目用 Haskell 么?
https://www.zhihu.com/question/20574647/answer/23834485
不是 Haskell，其他的 FP 语言也可以.


Haskell的哪些方面的改进和工具支持可以成为一个有趣的project idea？
偶然间看到 haskell summer of code 2016, 感觉挺有意思。想今年也申请个project试试.(不知道今年gsoc会不会又拒了haskell...) 想问问各位大大，有哪些觉得比较有趣的project idea?（比如Template Haskell, JVM backend or LLVM backend for GHC）https://www.zhihu.com/question/55996346/answer/147299275
作者：祖与占  
链接：https://www.zhihu.com/question/55996346/answer/147299275  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

UPDATE: 今年又黄了

找 idea 的话可以先看看这个列表 [{1} Active Tickets](https://link.zhihu.com/?target=https%3A//ghc.haskell.org/trac/summer-of-code/report/1)

你提到去年的两个, 应该都还可以搞:

JVM backend 已经变成 eta, 我过了下文档感觉还有很多坑没填, 尤其并发那块想搞自己的套路, 应该还可以找到 mentor

LLVM backend 本来说 8.2 会搞好, 刚搜下 issue, 拖到 8.4 了, [Implement the &#x27;Improved LLVM Backend&#x27; proposal](https://link.zhihu.com/?target=https%3A//ghc.haskell.org/trac/ghc/ticket/10074%3Fcversion%3D0%26cnum_hist%3D4), general 的 LLVM binding 因为 LLVM 坑爹的兼容性一直有点坑, 详情可以参考Stephen Diehl, Anthony Cowley 等同学在 Twitter 上面的讨论, Anthony Cowley 最近fork 出来了 [llvm-hs/llvm-hs: Haskell bindings for LLVM](https://link.zhihu.com/?target=https%3A//github.com/llvm-hs/llvm-hs)

还有 GHCJS, Purescript 这些compile 2 JS 的项目

编译向的项目应该会挺有趣, 但是也挺有挑战性.

[有哪些知名 IT 企业使用 Haskell/Scala ?](https://www.zhihu.com/question/54095611/answer/137911398)

[@韩冬](//www.zhihu.com/people/73c168246af1fab79b28736c311466e1)

里面提到几个希望改进的地方, 感觉都是挺好的方向

至于工具链方面问 Haskell 有没有 IDE 已经成了月经问题了, 社区也各种不同的解决方案, 当初我比较看好 [haskell/haskell-ide-engine: The engine for haskell ide-integration. Not an IDE](https://link.zhihu.com/?target=https%3A//github.com/haskell/haskell-ide-engine) , Chris Done 评价说这个项目目标太宏大, 后来搞了 intero, 我还是想有人填下这个坑的.

以上都没感觉几个感觉都不会特别"有趣", 都是工程坑, 有趣点的话可以研究下编辑器的根据类型补全或者搞所谓的"Hole-driven Haskell"支持

[post-rfc/sotu.md at master · Gabriel439/post-rfc · GitHub](https://link.zhihu.com/?target=https%3A//github.com/Gabriel439/post-rfc/blob/master/sotu.md) Immature 的领域都可以搞搞事

或者可以到这里看下?

[ghc-proposals/ghc-proposals: Proposed compiler and language changes for GHC and GHC/Haskell](https://link.zhihu.com/?target=https%3A//github.com/ghc-proposals/ghc-proposals)

好多坑, 不一而足, 最好提供相关背景


















https://www.zhihu.com/question/40231767/answer/85483603

https://www.zhihu.com/question/36325022/answer/67605451
作者：科温  
链接：https://www.zhihu.com/question/36325022/answer/67605451  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

SPJ当年确实说过Haskell的纲领是“竭尽全力避免成功”。  

> Haskell has a sort of unofficial slogan: avoid success at all costs  
> ([The A-Z of Programming Languages: Haskell](https://link.zhihu.com/?target=http%3A//www.computerworld.com.au/article/261007/a-z_programming_languages_haskell/%3Fpp%3D10))

不过这几年随着FP的兴起，Haskell社区已经比较关注Haskell的实际应用了。  
Aaron Contorer成立了FP Complete（[Home | FP Complete](https://link.zhihu.com/?target=https%3A//www.fpcomplete.com/)）网罗了一群Haskeller致力于推动Haskell的工业应用，建议题主逛逛他们的站点，看看他们的努力。  
其中[Case Studies](https://link.zhihu.com/?target=https%3A//www.fpcomplete.com/business/resources/case-studies/)列举了Haskell在工业中的应用案例。

说到工业应用，这里需要提一下FP Complete发起或主导的几个项目：  
1、LTS Haskell，简单讲就是一个定期更新的，充分测试的，保证一致性的Hackage源（解决Cabal Hell的）  
[Stackage Server](https://link.zhihu.com/?target=https%3A//www.stackage.org/)  
2、Stack：一个好用的开发工具  
[commercialhaskell/stack · GitHub](https://link.zhihu.com/?target=https%3A//github.com/commercialhaskell/stack)  
3、MinGHC：FP Complete打包的GHC，说实话我比较懒，没看出来和Haskell Platform的本质区别，可能和Stack结合比较好吧。  
[fpco/minghc · GitHub](https://link.zhihu.com/?target=https%3A//github.com/fpco/minghc)

FP Co的github项目页，没事逛逛：  
[FP Complete · GitHub](https://link.zhihu.com/?target=https%3A//github.com/fpco)

PS：喜欢Haskell的话，多关注[http://www.reddit.com/r/haskell](https://link.zhihu.com/?target=http%3A//www.reddit.com/r/haskell)。



https://www.zhihu.com/question/281136471/answer/419861872































































































































