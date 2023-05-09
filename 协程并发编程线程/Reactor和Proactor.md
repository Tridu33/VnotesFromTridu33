# Reactor和Proactor
如何深刻理解Reactor和Proactor？ - 小林coding的回答 - 知乎
https://www.zhihu.com/question/26943938/answer/1856426252

---

Reactor 翻译过来的意思是「响应者」，指「对事件反应」，也就是来了一个事件，Reactor 就有相对应的反应/响应。Reactor 模式也叫 Dispatcher 模式，我觉得这个名字更贴合该模式的含义，即 I/O 多路复用监听事件，收到事件后，根据事件类型分配（Dispatch）给某个进程 / 线程。

Reactor 模式主要由 Reactor 和处理资源池这两个核心部分组成，它俩负责的事情如下：

- Reactor  负责监听和分发事件，事件类型包含连接事件、读写事件；
- 处理资源池 负责处理事件，如 read -> 业务逻辑 -> send；

---

 Reactor 是非阻塞同步网络模式，而 Proactor 是异步网络模式。
 





- Reactor 是非阻塞同步网络模式，感知的是就绪可读写事件。
在每次感知到有事件发生（比如可读就绪事件）后，就需要应用进程主动调用 read 方法来完成数据的读取，也就是要应用进程主动将 socket 接收缓存中的数据读到应用进程内存中，这个过程是同步的，读取完数据后应用进程才能处理数据。


- Proactor 是异步网络模式， 感知的是已完成的读写事件。
在发起异步读写请求时，需要传入数据缓冲区的地址（用来存放结果数据）等信息，这样系统内核才可以自动帮我们把数据的读写工作完成，这里的读写工作全程由操作系统来做，并不需要像 Reactor 那样还需要应用进程主动发起 read/write 来读写数据，操作系统完成读写工作后，就会通知应用进程直接处理数据。


---

akka Actor框架把任务放进队列，然后tell给具体actor去异步执行。

- 指派tell任务的Actor
- 具体执行任务的Actor



---

Reactor，还是 Proactor，都是一种基于「**事件分发**」的网络编程模式。

Java 的 nio 中的 Channel 与 Selector 是为了实现 io 的多路复用和异步，是否可以像 Golang 中的 channel 一样，用于并发实体之间的通信？
```
for{
    select{
        case channel1事件:
            ...
        case channel2事件:
            ...
    }
}
```













