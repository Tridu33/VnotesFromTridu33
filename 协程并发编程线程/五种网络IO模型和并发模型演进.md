# 五种网络IO模型和并发模型演进

深度长文：从bio到nio到aio，再到响应式编程 - 小姐姐味道的文章 - 知乎

https://zhuanlan.zhihu.com/p/400927380
Linux有**5种常见的IO模型**。其中，阻塞IO就是bio，IO复用就是nio，异步IO就是aio。
- 阻塞式IO （bio）
- 非阻塞式IO
- IO复用 （nio）
- 信号驱动式IO
- 异步IO（aio）


在网络编程中，Reactor模型是必须要了解的。现在，大多数与IO相关的组件，都会使用Reactor模型，比如Tomcat、Redis、Nginx等，可见Reactor应用的广泛性。

Reactor是NIO的基础。










