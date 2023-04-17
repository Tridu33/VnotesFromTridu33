

邮箱：giantchen_at_gmail.com

主页：http://chenshuo.com/book （正文和脚注中出现的 URL 可从这里找到。 ）

微博：http://weibo.com/giantchen

博客：http://blog.csdn.net/Solstice

代码：http://github.com/chenshuo


本书的示例代码以开源项目的形式发布在 GitHub 上，
地址是 http://github.com/chenshuo/recipes/ 和 http://github.com/chenshuo/muduo/ 。

# 1. linux多线程服务端编程



[《Linux 多线程服务端编程——使用 muduo C++ 网络库》](http://chenshuo.com/book)配套代码 [bookcode.tar.gz](https://github.com/downloads/chenshuo/documents/bookcode.tar.gz) [bookcode.tar.bz2](https://github.com/downloads/chenshuo/documents/bookcode.tar.bz2)

[《Linux 多线程服务端编程——使用 muduo C++ 网络库》](http://chenshuo.com/book)样章下载：

[《Linux 多线程服务端编程——使用 muduo C++ 网络库》前言与目录](https://github.com/downloads/chenshuo/documents/preamble.pdf)

[《Linux 多线程服务端编程——使用 muduo C++ 网络库》第1章：线程安全的对象生命期管理](https://github.com/downloads/chenshuo/documents/chap1.pdf)

[《Linux 多线程服务端编程——使用 muduo C++ 网络库》第6章：muduo网络库简介](https://chenshuo-public.s3.amazonaws.com/pdf/chap6.pdf)

[《Linux 多线程服务端编程——使用 muduo C++ 网络库》附录](https://github.com/downloads/chenshuo/documents/appendix.pdf)

其他文章：

[从《C++ Primer 第四版》入手学习C++](https://github.com/downloads/chenshuo/documents/LearnCpp.pdf)（2012-07-11更新，收入[《Linux 多线程服务端编程》](http://chenshuo.com/book)附录B）

[C++ History and Rationale](https://github.com/downloads/chenshuo/documents/CppHistory.pdf)

[Muduo网络库使用手册](https://github.com/downloads/chenshuo/documents/MuduoManual.pdf)（2012-06-26更新，最新版见[《Linux 多线程服务端编程》](http://chenshuo.com/book)第6、7章）

[C++ 工程实践](https://github.com/downloads/chenshuo/documents/CppPractice.pdf)]（2012-04-20更新，最新版见[《Linux 多线程服务端编程》](http://chenshuo.com/book)第10、11、12章）

[网络编程学习经验](https://github.com/downloads/chenshuo/documents/LearningNetworkProgramming.pdf)（2012-02-13更新，最新版见[《Linux 多线程服务端编程》](http://chenshuo.com/book)附录A）

[当析构函数遇到多线程──C++ 中线程安全的对象回调](https://github.com/downloads/chenshuo/documents/dtor_meets_mt.pdf)（最新版见[《Linux 多线程服务端编程》](http://chenshuo.com/book)第1章）

[多线程服务器的常用编程模型](https://github.com/downloads/chenshuo/documents/multithreaded_server.pdf)（最新版见[《Linux 多线程服务端编程》](http://chenshuo.com/book)第2、3章）









--------------------------------------------------



Linux C++ 服务器端这条线怎么走？一年半能做出什么？ - 陈硕的回答 - 知乎
https://www.zhihu.com/question/22608820/answer/21968467


比如说操作系统，应该把精力主要放在进程管理与调度、内存管理、并发编程与同步、高效的IO等等，而不要过于投入到初始化（从 BIOS 加载引导扇区、设置 GDT、进入保护模式）这种一次性任务上。我发现国内讲 Linux 内核的书往往把初始化的细节放在前几章，而国外的书通常放附录，你可以体会一下。初始化对操作系统本身而言当然是重要的，但是对于在用户态写服务程序的人来说，弄清楚为什么要打开 PC 上的 A20 地址线真的有用处吗？（这不过是个历史包袱罢了。）


再比方说《计算机网络》，关键之一是理解如何在底层有丢包、重包、乱序的条件下设计出可靠的网络协议，这不算难。难一点的是这个可靠协议能达到“既能充分利用带宽，又能做到足够公平（并发连接大致平均分享带宽）”。而不是学会手算 CRC32，这更适合放到信息论或别的课程里去讲。


注意分清知识的层次。就好比造汽车与开汽车的区别，我认为一个司机的技能主要体现在各种道路条件和天气状况下都能安全驾驶（城市道路、高速公路、乡间公路 X 晴、雨、雪、雾），平安到达目的地。作为一名司机，了解汽车运行的基本原理当然是好事，可以有助于更好地驾驶和排除一些常见故障。但不宜喧宾夺主，只要你不真正从事汽车设计工作，你再怎么研究发动机、传动、转向，也不可能比汽车厂的工程师强，毕竟这是人家的全职工作。而且钻研汽车构造超过一定程度之后，对开好车就没多大影响了，成了个人兴趣爱好。“有的人学着学着成了语言专家，反而忘了自己原本是要解决问题来的。”（语出孟岩 快速掌握一个语言最常用的50%）

对于并发编程来说，掌握 mutex、condition variable 的正确用法，避免误用（例如防止 busy-waiting 和 data race）、避免性能 pitfalls，是一般服务端程序员应该掌握的知识。而如何实现高效的 mutex 则是 libc 和 kernel 开发者应该关心的事，随着硬件的发展（CPU 与内存之间互联方式的改变、核数的增加），最优做法也随之改变。如果你不能持续跟进这一领域的发展，那么你深入钻研之后掌握的知识到了几年之后可能反而成为累赘，当年针对当时硬件的最优特殊做法（好比说定制了自己的 mutex 或 lock-free 数据结构）在几年后有可能反而会拖低性能。还不如按最清晰的方式写代码，利用好语言和库的现成同步设施，让编译器和 libc 的作者去操心“与时俱进”的事。





我（孟岩）主张，在具备基础之后，学习任何新东西，都要抓住主线，突出重点。对于关键理论的学习，要集中精力，速战速决。而旁枝末节和非本质性的知识内容，完全可以留给实践去零敲碎打。


很显然，第一遍的时候，我是跳着看的。因为我能看懂代码，看不懂他说的话的背后的含义，所以都是有代码的那一章开看的。之前则使用“量子波动阅读法”进行学习。

先看了51页的shared_ptr部分内容。
然后跳到125页看muduo网络库的简介，“量子波动”
到了177页muduo编程示例，这里开始认真看其中的代码，用6色荧光笔，把重要的6个对象从生成到应用，再到销毁的过程，涂上，这样就有了6个对象的行动轨迹。这样代码的部分就比较容易看懂了。然后再逆推，他书中解释的内容。这样就会把很模糊的内容，在代码的加持下，变得一知半解了。
大概用了7-10天就看到了336页。至此这本书的第一遍就结束了。






























































