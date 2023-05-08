

https://github.com/elixir-cn/elixir-china-companies 在生产环境中使用 Elixir 的中国公司列表，按行业来归类：

2020年elixir发展的怎么样？ - 绅士喵的回答 - 知乎
https://www.zhihu.com/question/378317879/answer/1320845738




---




《Programming Erlang: Software for a Concurrent World》Joe老爷子




什么样的语言更容易贴近搭积木的组织方式呢？


提倡使用递归（递归就是以自身为积木）

以pattern matching的方式组织代码（每个代码快尽可能小，只处理一件简单的事情）

语言层面提供解耦的工具（如erlang的process，golang的chan，scala的actor）

系统的一部分损坏，并不影响未损坏的部分

Elixir的VM：BEAM - 李渔的文章 - 知乎
https://zhuanlan.zhihu.com/p/610576733


Erlang/OTP的书，《The Erlang Runtime System》 https://blog.stenmans.org/theBeamBook/。主要是写底层的VM的，有点类似于《深入理解JVM虚拟机》





# Erlang













实际上现在来看，在高并发上 Erlang 已经排不上位置了。Rust 中 Actor 模型的实现 Actix 框架和 Java 的 Vert.x 在并发上都能吊打 Erlang，甚至从数据方面看根本不在一个级别。
因为 Erlang 真正的优势在于**抢占式调度带来的低延时**和**软实时性**。无论是 Actix 还是 Vert.x 都需要将耗时的计算任务分配给原生线程，此时它们的并发性能就会大打折扣，否则直接堵塞。但是这在 Erlang 上是不存在的问题，这是调度方式决定的。Go 也是高并发的语言，Go 很成功，已经是热门语言了。而 Go 的调度实现是不完全的抢占。
为何 Elixir/Erlang 相对冷门？ - 绅士喵的回答 - 知乎
https://www.zhihu.com/question/341832872/answer/810537908

这个**软实时**指的是垃圾回收性能平稳。如果做语音类应用，需要网络传输过程不会因为 GC 回收导致延迟抖动，Erlang 是你的开箱即用的最佳选择，没有之一。




对于现代习惯了 Ruby 和 JavaScript 的程序员来说，Erlang 就是一门老古董。而且，Erlang 也没有现代 Web 应用程序所需的许多功能。

于是，Jose Valim 在 2012 年创建了 Elixir 语言。Elixir 代码会编译成 Erlang 字节码，可以在 Erlang 运行时上运行。甚至你可以直接在 Elixir 中编写 Erlang 代码。


Valim 是 Ruby on Rails 开发团队的语言，甚至还写过一本关于 Rails 开发的书。所以，Elixir 的设计思想很大程度上来源于 Rails。它的语法很像 Ruby，而且比 Erlang 易读得多。而且Elixir还扩展了 Erlang，加入了元编程、多态等功能。


进入互联网时代后，Erlang这种基于actor的分布式计算，简直就是为微服务、分布式计算而生的。Scala就搞了个akka，Erlang也衍生出了Elixir。https://www.zhihu.com/answer/704512665





-----------------------------------------------------

# 宏

不像面向对象语言是通过反射对象来实现**元编程**的，同时与C宏的字符串替换也不一样，Elixir的宏是Lisp系的。






宏有如下三点：

1. defmacro是的参数与返回是: AST in, AST out;

2. 调用macro的代码，编译器会在编译时替换成macro返回的AST，也就是说被替换成macro的body;

3. 如果在macro body里没有对变量进行unquote，那么此变量会编译成atom，而在运行时会对此atom进行引用调用，造成报错;

Elixir劝退指北 - qgymje的文章 - 知乎
https://zhuanlan.zhihu.com/p/100777913
## EMQ

EMQ X 全称 Erlang/Enterprise/Elastic MQTT Broker，


EMQ X 全称 Erlang/Enterprise/Elastic MQTT Broker，
https://www.cnblogs.com/dotnet-org-cn/p/13341888.html

为什么一些网页游戏喜欢用Erlang做服务端？ - 庆亮的回答 - 知乎
https://www.zhihu.com/question/20405300/answer/45747560


也是channel
https://github.com/neugates/neuron
这是一个纯C的工业数据采集和汇聚，通过mqtt转发到云端的项目
iot这块用emq的多吗？见到好几回了，基本上有iot和mqtt的地方就能碰见
emq不是宣传的时候老说自己是iot的基础设施么,它家有这么个项目，然后还在另外搞一套基于erlang虚拟机的编程语言


erlang写的mqtt服务器端


OCaml 5是不允许C栈里触发effect的。所以有可能用effect的C代码需要遵守某些约定（比如至少不能对栈乱搞





