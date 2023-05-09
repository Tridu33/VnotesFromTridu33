# 五种网络IO模型和并发模型演进

深度长文：从bio到nio到aio，再到响应式编程 - 小姐姐味道的文章 - 知乎

https://zhuanlan.zhihu.com/p/400927380
Linux有**5种常见的IO模型**。其中，阻塞IO就是bio，IO复用就是nio，异步IO就是aio。



- 阻塞I/O (Blocking I/O)

- 非阻塞I/O (Non-Blocking I/O)

- I/O复用（I/O Multiplexing)

- 信号驱动的I/O (Signal Driven I/O)

- 异步I/O (Asynchrnous I/O)


在网络编程中，Reactor模型是必须要了解的。现在，大多数与IO相关的组件，都会使用Reactor模型，比如Tomcat、Redis、Nginx等，可见Reactor应用的广泛性。

Reactor是NIO的基础。





阻塞、非阻塞、同步、异步 I/O 的概念



阻塞 I/O等待的是「内核数据准备好」和「数据从内核态拷贝到用户态」这两个过程。

非阻塞 I/O，非阻塞的 read 请求在数据未准备好的情况下立即返回，可以继续往下执行，此时应用程序不断轮询内核，直到数据准备好，内核将数据拷贝到应用程序缓冲区，read 调用才可以获取到结果。


![](https://pic1.zhimg.com/80/v2-51e052e2beecef41da3aed3ebc2b80bd_720w.webp?source=1940ef5c)



真正的异步 I/O 是「内核数据准备好」和「数据从内核态拷贝到用户态」这两个过程都不用等待。

![](https://picx.zhimg.com/80/v2-b01988dd44a5edbe596a280d1c266033_720w.webp?source=1940ef5c)


















































