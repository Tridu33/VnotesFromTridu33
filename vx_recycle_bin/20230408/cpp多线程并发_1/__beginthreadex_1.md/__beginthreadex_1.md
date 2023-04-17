






windows创建线程、IO模型、同步异步 :https://blog.csdn.net/xiongluo0628/article/details/81943964 
一、线程创建函数CreateThread()
二、等待线程返回函数
三、windows下另一个线程函数_beginThreadex()
四、多线程编程之windows同步方式
五、Linux五种IO模型
六、同步、异步、阻塞、非阻塞
七、并发与并行的理解 
八、select/poll/epoll的区别

[Windows内核原理-同步IO与异步IO](https://www.cnblogs.com/Jack-Blog/p/11385686.html)



# __beginthreadex







CreateThread与_beginthreadex的本质区别，相信阅读本文后你能轻松的使用多线程并能流畅准确的回答CreateThread与_beginthreadex到底有什么区别，在实际的编程中到底应该使用CreateThread还是_beginthreadex？[秒杀多线程第1篇](http://blog.chinaunix.net/uid-97185-id-4389566.html)
[秒杀多线程第三篇 原子操作 Interlocked系列函数](https://blog.csdn.net/morewindows/article/details/7429155)

CreateThread()函数是Windows提供的API接口，在C/C++语言另有一个创建线程的函数_beginthreadex()，在很多书上（包括《Windows核心编程》）提到过尽量使用**_beginthreadex()**来代替使用CreateThread()




```
utils::CCriticalSection::Owner Lock(m_csListLock);
```
[秒杀多线程第九篇 经典线程同步总结 关键段 事件 互斥量 信号量](https://blog.csdn.net/MoreWindows/article/details/7538247#comments_17491600)

[秒杀多线程第十篇 生产者消费者问题
](https://blog.csdn.net/MoreWindows/article/details/7577591#comments_17228372)



C++多线程强制终止 - 华为云开发者社区的文章 - 知乎
https://zhuanlan.zhihu.com/p/377913335



































































