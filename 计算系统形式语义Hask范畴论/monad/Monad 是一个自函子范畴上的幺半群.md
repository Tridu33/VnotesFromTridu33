https://homepages.inf.ed.ac.uk/wadler/topics/monads.html





有没有对Haskell中理解monad比较好的代码例子？ - 何幻的回答 - 知乎
https://www.zhihu.com/question/64207539/answer/217843172

https://wiki.haskell.org/All_About_Monads

https://blog.jle.im/entry/practical-fun-with-monads-introducing-monadplus.html Monad 的实用乐趣 --- 介绍：MonadPlus

https://blog.jle.im/entry/the-list-monadplus-practical-fun-with-monads-part.html




《函数响应式编程》
P76描述monad的实际含义：



```
在函数式编程中，我们将计算声明为表达式，一个表达式可以是简单表达式，也可以是多个表达式的组合。

当我们把领域行为 建模为领域模型的时候，同时也实现了组合器，用类似的方法进化演变。
我们从简单函数开始，然后使用高阶函数的威力，组合成更加大的抽象。一个monad抽象了计算的一个类型。用于建立这种组合器的基本库。

一个monad由三部分组成：
1. 一个类型构造器M【A】 ，Scala中一般表示为trait M[A] ,case class M[A].或者class M[A];
2. 一个unit方法，将一个计算引入monad。在Scala中使用类构造器的调用实现这个目的
3. 一个bind方法，他将计算序列化。在scala中，FlatMap就是这个bind，。


这就暗示了monad是一个代数结构，任何拥有这三个元素的monad同样需要遵守以下三个原则:
1. 一致性identity:对于一个单子m,m Flatmap unit => m
2. 单元性unit:对于一个单子m,unit(v) flatMap f =>f(v)
3. 组合性associativity:对于一个单子m,m flatMap g flatMap h => m flatMap(x=>g(x) flatMap h)
```



群友：
>  你可以把Functor Applicative Monad都当成一个盒子
>>=就是把一个装在盒子里的值应用于一个接收一个值返回一个盒子的函数得到套有一层盒子的值，很容易明白>>=相当于先fmap再两层盒子并一层盒子
<*>就是把装在盒子里的函数作用在装在盒子里的值
pure就是装盒子
fmap就是把函数作用在装在盒子里的值
monad就是hs的first class effect（monad其实就是一个pure和一堆>>=的链表


https://dl.acm.org/doi/10.1145/143165.143169
本文探讨了使用 monad 来构造函数式程序。不需要单子或范畴论的先验知识。

单子增加了修改程序的便利性。它们可以模仿不纯特征的影响，例如异常、状态和延续；并且还提供了利用这些特征不容易实现的效果。程序的类型反映了发生的效果。

第一部分是使用单子的扩展示例。修改了一个简单的解释器以支持各种额外的功能：错误消息、状态、输出和非确定性选择。第二部分描述了 monad 和 continuation-passing 风格之间的关系。第三部分概述了如何在用 Haskell 编写的 Haskell 编译器中使用 monad。



https://dl.acm.org/doi/10.1145/262009.262011
Wadler 试图在函数式编程社区中普及一个流行的话题：使用 monad 将输入/输出集成到纯函数式设置中。与其他方法一样，功能程序计算一个描述交互的值，而不是参与交互本身。然后程序外部的机制执行所描述的交互。monadic 方法的区别在于构成交互描述数据类型的特定操作。一个动作会影响世界，但也会返回一个值。（例如，读取一个字符使光标前进并返回该字符。）因此，对于每种类型 T，都有一个类型 IO[T] 的动作描述符，当执行时，它返回一个 T。有两个构造函数超出原始 I/O 操作的操作描述符。一个取一个 T 类型的值 x 并返回一个 IO[T] 类型的描述符。执行时，没有任何操作结果，并返回 x。另一个构造函数接受一个 IO[T1] 类型的描述符 d 和一个从 T1 到 IO[T2] 的函数 f 并将它们组合起来以产生一个 IO[T2] 类型的描述符。执行复合描述符分为三个步骤：执行 d，将 f 应用于返回的值，并执行步骤 2 计算的描述符。遗憾的是，Wadler 的普及尝试并不完全成功，因为他假设有 Haskell 的阅读知识，这在外面很少函数式编程社区有。由于 Haskell 现在包含 monadic I/O，因此对 Haskell 有过时知识的人将从本教程中受益最多。没有操作结果，并返回 x。另一个构造函数接受一个 IO[T1] 类型的描述符 d 和一个从 T1 到 IO[T2] 的函数 f 并将它们组合起来以产生一个 IO[T2] 类型的描述符。执行复合描述符分为三个步骤：执行 d，将 f 应用于返回的值，并执行步骤 2 计算的描述符。遗憾的是，Wadler 的普及尝试并不完全成功，因为他假设有 Haskell 的阅读知识，这在外面很少函数式编程社区有。由于 Haskell 现在包含 monadic I/O，因此对 Haskell 有过时知识的人将从本教程中受益最多。没有操作结果，并返回 x。另一个构造函数接受一个 IO[T1] 类型的描述符 d 和一个从 T1 到 IO[T2] 的函数 f 并将它们组合起来以产生一个 IO[T2] 类型的描述符。执行复合描述符分为三个步骤：执行 d，将 f 应用于返回的值，并执行步骤 2 计算的描述符。遗憾的是，Wadler 的普及尝试并不完全成功，因为他假设有 Haskell 的阅读知识，这在外面很少函数式编程社区有。由于 Haskell 现在包含 monadic I/O，因此对 Haskell 有过时知识的人将从本教程中受益最多。执行复合描述符分为三个步骤：执行 d，将 f 应用于返回的值，并执行步骤 2 计算的描述符。遗憾的是，Wadler 的普及尝试并不完全成功，因为他假设有 Haskell 的阅读知识，这在外面很少函数式编程社区有。由于 Haskell 现在包含 monadic I/O，因此对 Haskell 有过时知识的人将从本教程中受益最多。执行复合描述符分为三个步骤：执行 d，将 f 应用于返回的值，并执行步骤 2 计算的描述符。遗憾的是，Wadler 的普及尝试并不完全成功，因为他假设有 Haskell 的阅读知识，这在外面很少函数式编程社区有。由于 Haskell 现在包含 monadic I/O，因此对 Haskell 有过时知识的人将从本教程中受益最多。 





https://dl.acm.org/doi/pdf/10.1145/143165.143169 《The essence of functional programming》



-----------------------------------------------------


前端中的 Monad - 尚春的文章 - 知乎
https://zhuanlan.zhihu.com/p/47130217



如何解释 Haskell 中的单子（Monad）？ - parker liu的回答 - 知乎
https://www.zhihu.com/question/22291305/answer/21333050


https://www.bilibili.com/video/BV1qh411q7cS

什么地方用得到monad呀?读入，输出，网络通信，这类可能产生副作用的操作，然后…可能还有别的叭……@沉默是金 我记得 A history of Haskell 那篇 paper 里有提过 Monad 出现前 IO 的解决方法，印象里可以用 stream 或者类似 CPS 的方法去抽象https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/history.pdf, Chapter 7



 https://www.jianshu.com/p/31377066bf97 scala代码实现Monad






































## DDD

https://www.youtube.com/watch?v=pMuiVlnGqjk Evans作者谈DDD



```
6:22 例子
    7:38 货运系统设计的弊端
    7:50 软件设计的2个观点
        8:01 观点1：软件设计者
            8:32 货运系统的副作用
                8:43 将复杂的逻辑与数据库更新结合在一起违反了将逻辑与更新状态分开的原则
        9:08 另一个角度：领域
            9:58 更多详情， 10:02 我们不能总是得到如此高层次的讨论
    11:01 我们想要的是能够在发生这种情况时注意到并采取正确的措施 11:18 它会如何影响现有软件 
    11:46 我们必须找到另一种应对方式
14:15 DDD的原则之一：语言非常重要 14:21我注意到的一件事：在谈论软件时，我们使用的语言与软件中所使用的语言不同
```







--------------------------------------------------------




https://en.wikipedia.org/wiki/Monad_(functional_programming) 函数式编程中的单子











如何解释 Haskell 中的单子（Monad）？ - parker liu的回答 - 知乎
https://www.zhihu.com/question/22291305/answer/21333050

https://github.com/tomstuart/nothing
最初是作者的博客文章，叫Programming with Nothing
https://rubywebapp.com/
@knifefire 666.这么说好多书都源自博客呀，martin的《DSL》,《数学之美》......才知道作者正忙着出新书用Ruby编写Web应用程序原型



ruby徒手实现monads：

https://codon.com/refactoring-ruby-with-monads monads








Monad入门  https://thzt.github.io/2015/03/07/monad/





Hask范畴上的Monad https://thzt.github.io/2016/01/11/monad-in-hask-category/







https://www.zhihu.com/question/311415552/answer/600063213


dev.stephendiehl.com/hask/#monads

https://www.zhihu.com/question/22291305/answer/21333050


https://www.zhihu.com/question/24972880/answer/134078723



Monad是一种数学结构，haskell中的Monad意义和数学上的意义是一样的。简单的说单子(Monad)就是自函子范畴上的一个幺半群。这个幺半群的态射是作用在自函子上的自然变换，其单位态射是haskell中class Monad 的return函数(这个实际上是个自然变换)。而这个幺半群的态射的组合操作(composition)则是haskell中class Monad的join函数，也是一个自然变换。  
从几何直观的概念来说，Monad是一个自相似的几何结构，通过自函子的作用和两个自然变换的约束得到一层层嵌套的自相似结构。

  
  
作者：parker liu  
链接：https://www.zhihu.com/question/22291305/answer/21333050  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。







https://zhuanlan.zhihu.com/p/58514370
# 1. 15 分钟了解 Monad
https://www.zhihu.com/question/19635359/answer/172074046
https://www.zhihu.com/question/64207539/answer/217843172
https://www.zhihu.com/search?type=content&q=Monad
https://www.zhihu.com/question/22291305/answer/21333050

https://wiki.haskell.org/Monad_tutorials_timeline


https://en.wikipedia.org/wiki/Monad_%28functional_programming%29



https://www.zhihu.com/question/64207539
有没有对Haskell中理解monad比较好的代码例子？


https://www.zhihu.com/question/22291305/answer/21333050
**单子(Moand)是自函子的Monoidal范畴上的一个幺半群，该Monoidal范畴的张量积（tensor product，⊗:M×M→M）是自函子的复合(composition)，单位元是Id functor。**

https://www.zhihu.com/question/22291305/answer/21333050



Monad是一种数学结构，haskell中的Monad意义和数学上的意义是一样的。简单的说单子(Monad)就是自函子范畴上的一个幺半群。这个幺半群的态射是作用在自函子上的自然变换，其单位态射是haskell中class Monad 的return函数(这个实际上是个自然变换)。而这个幺半群的态射的组合操作(composition)则是haskell中class Monad的join函数，也是一个自然变换。  
从几何直观的概念来说，Monad是一个自相似的几何结构，通过自函子的作用和两个自然变换的约束得到一层层嵌套的自相似结构。

  
  
作者：parker liu  
链接：https://www.zhihu.com/question/22291305/answer/21333050  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。










































































































































































