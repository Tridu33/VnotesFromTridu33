# haskell_debug







如何高效地调试haskell程序? - 祖与占的回答 - 知乎
https://www.zhihu.com/question/345228369/answer/819148911




如果是用 parsec 的话可以试试 parsec-free https://github.com/jwiegley/parsec-free , 把整个 parse 的过程打出来.

按照这个思路, 写代码的时候可以把 side effect 或者整个流程 free monad 化, debug 的时候换一个可以打 log 的 interpreter 就可以可视化整个执行过程了.

不想手动写? 已经有人给你写好了: Control.Effect.Trace https://hackage.haskell.org/package/fused-effects-1.1.1.0/docs/Control-Effect-Trace.html  https://hackage.haskell.org/package/base-4.12.0.0/docs/Debug-Trace.html  , Polysemy.Trace https://hackage.haskell.org/package/polysemy-1.4.0.0/docs/Polysemy-Trace.html


命令行打印有 trace, traceShowId, traceM 等等, 测试框架有 hspec, 基于属性的随机测试有 quickcheck (不了解的话可以去 stackage上搜索, 熟练使用 hoogle 是学习 Haskell 的必备技能).


人肉debug

```haskell
import Debug.Trace
traceShow 
traceShowId
```

因为Haskell程序本来就是个monad，所以正确用法是看各种monad trace怎么用。

组合子parser基本全靠脑补调试好吧，你用什么语言写都很难调

















































































