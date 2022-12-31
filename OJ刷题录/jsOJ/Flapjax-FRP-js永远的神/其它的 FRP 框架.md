# 1.  FRP 框架


FRP 最早发源于 Haskell 社区，在 Haskell 社区里有许多关注点不同实现方式各异的 FRP 框架，比如：

Fran

Yampa

Reactive

…

FrTime 是用 Racket(Scheme) 语言实现的一款 FRP 框架，它背后的团队和 Flapjax 的团队是同一个，所以它们在理念、设计和实现上都极为相似。

LuaTime 是笔者在几年前为 Lua 语言实现的 FRP 框架，它在 API 的设计上主要参考了 FrTime，但是底层的实现采用了 pull 的方式。这个项目计划在今年年内开源。





九、相关研究

Microsoft Reactive Extensions

微软用于解决实时互动、异步编程问题的跨语言的开发框架，基本思想和 FRP 极为类似：将变化的数据抽象出来，称之为 IObservable，并为其定义各种转换和组合操作。它背后的主要设计者是 Haskell 社区的大牛。


Arrowlets

FRP 关注数据流，Arrowlets 和 callback 一样关注控制流，但它利用 Arrow ">http://en.wikipedia.org/wiki/Arrow_(computer_science) ) 这种计算模型使得控制流具备了很好的组合能力。


Promise or Future

在 JavaScript 社区中很流行的对异步编程的解决方案，有无数的实现库。

Sandglass

笔者所在团队设计的一种基于 Behavior Tree 模型的 AI 编程语言，为 Behavior Tree 引入了协作式多任务机制和显式的时间控制机制，支持以同步化的思维来写异步程序，能编译成标准的 JavaScript。




https://www.infoq.cn/article/functional-reactive-programming 函数式反应型编程 (FRP) —— 实时互动应用开发的新思路







