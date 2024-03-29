





Joe Armstrong 在论文中是这样认为的：几乎所有传统的编程语言对真正的并发都缺乏有力的支持——本质上是顺序化的，而语言的并发性都仅仅由底层操作系统而不是语言提供。

而用对并发提供良好支持的语言（也就是作者说的面向并发的语言 Concurrency Oriented Language） 来边写程序，则是相当容易的：

从真实世界的活动中识别出真正的并发活动
识别出并发活动之间的所有消息通道
写下能够在不同消息通道中流通的所有消息
程序的结构要严格保持与问题的结构一致，即每一个 真实世界里的活动都严格映射到我们编程语言中的一个并发进程上。如果从问题 到程序的映射比例为 1:1，我们就说程序与问题是同构(isomorphic)的。
映射比例为 1:1 这一点非常重要。因为这样可以使得问题和解之间的概念隔阂最小化。如果比例不为 1:1，程序就会很快退化而变得难以理解。在使用非面向并发的编程语言来解决并发问题时，这种退化是非常常见的。在非面向并发的编程语言中，为了解决一个问题，通常要由同一个语言级的线程或进程来强制控制多个独立的活动，这就必然导致清晰性的损失，并且会使程序滋生复杂的、难以复现的错误。
在分析问题时，我们还必须为我们的模型选择一个合适的粒度。比如，我们 在编写一个即时通信系统(instant messaging system)时，我们使用每个用户一 个进程的方式，而不是将用户身上的每一个原子对应到一个进程。


其次， 通过定下的九条原则性思想设计，写出来天然支持分布式系统的 erlang 以及OTP框架，真的做到了他说的实现面向并发的语言（ Concurrency Oriented Language）。

一切皆进程
进程强隔离
进程的生成与销毁都是轻量的操作
消息传递是进程交互的唯一方式
每个进程有唯一的名字
你若知道进程的名字，就可以向他发消息
进程之间不共享资源
错误处理非本地化
进程要么正常跑着，要么马上挂掉
就以上九条的观念，设计出的 erlang 语言，成就了可靠性达到99.9999999%的目前世界上最复杂的 ATM 交换机。

其三，let it crash 思想的提出与实现。

程序不可能处理一切错误，因此程序员只要力所能及的处理显然易见的错误就好了，而那些隐藏着的，非直觉性的错误，就让他崩掉吧——本来就很有可能是极少见的错误，经常出现的？就需要程序员人工处理了，这是紧急情况，就算 try catch所有错误也无法避免，因为系统已经陷入崩溃边缘了，苟延残喘下去只是自欺欺人。

要注意的是let it crash ，并不是说你用 golang，C++等语言打包个二进制，用 supervisorctl 等工具监控，错误就让他马上崩，挂了自动重启 - = -，参考我之前的答案应该如何理解 Erlang 的「任其崩溃」思想？



其四，一切进程都是轻量级的，都可以被监控（monitor），有Supervisor 专门做监控。

你可以方便的用一个进程（supervisor）去管理子进程，supervisor 会根据你设定的策略，来处理意外挂掉的子进程（这种情况不多的是，错误处理稍微做不好就会挂） ， 策略有：

one_for_one：只重启挂掉的子进程
one_for_all：有一个子进程挂了，重启所有子进程
rest_for_one：在该挂掉的子进程 创建时间之后创建的子进程都会重启。
老夫敲代码就是一把梭！可不，只要重启就行。

实质上，这是有论文支持的：在复杂的产品系统中，几乎所有的故障和错误都是暂态的，对某个操作进行重试是一种不错地解决问题方法 ——Jim Gray 的论文中指出，使用这种方法处理暂态故障，系统的平均故障间隔时间 (MTBF) 提升了 4 倍。

因此，你就可以创建一课监控树，根节点就是啥事都不做，只负责监控的进程。其他都是它的子进程，如果不是 coredump（几乎不发生），那么根节点就不可能会挂；因此其他子进程就会正确的被处理。

当然，这有前提： 5 秒内重启超于 3 次，就会不再重启，让进程挂掉。为什么呢？因为重启是为了让进程回到当初启动时的稳定态，既然稳定态都不稳定了，重复做重启是没有意义的，这时迫切需要人来处理。







# Erlang 之父 Joe Armstrong




Joe Armstrong 不必说 erlang 与 OTP， 光他的论文《面对软件错误构建可靠的分布式系统》http://www.kaiyuanba.cn/content/other/erlang.pdf 就足以载入史册——领先现在几十年，提出了OOP 等思想本质上不是并发的正确处理方法。


消息传递是进程交互的唯一方式




Erlang 之父 Joe Armstrong 逝世，如何评价他在计算机领域的贡献？ - 山尽的回答 - 知乎
https://www.zhihu.com/question/321011169/answer/658027406










