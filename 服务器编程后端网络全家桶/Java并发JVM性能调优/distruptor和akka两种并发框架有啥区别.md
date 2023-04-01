


java线程原始的使用**共享内存**是最low的， 传统多线程的做法是使用synchronized或ReentrantLock等锁机制来保证资源访问的安全性，但这会带来锁竞争、死锁等问题。

无论是CSP还是Actor模型，他们都完完全全贯彻了一句至理名言：
>Don't communicate by sharing memory; share memory by communicating. (R. Pike)
 “不要以共享内存方式通信，要以通信方式共享内存 


--------------------------------------

akka actor模型和java thread模型各有什么优势？ - Galois的回答 - 知乎
https://www.zhihu.com/question/29472057/answer/141693225
详细讲述了Actor背后的设计思想以及和传统thread-based框架的区别和优势


如何深入浅出地解释并发模型中的 CSP 模型？ - luikore的回答 - 知乎
https://www.zhihu.com/question/26192499/answer/46815754



distruptor和akka两种并发框架有啥区别？ - 代码时光的回答 - 知乎
https://www.zhihu.com/question/316974326/answer/2942835525
传统多线程的做法是使用synchronized或ReentrantLock等锁机制来保证资源访问的安全性，但这会带来锁竞争、死锁等问题。

而Akka框架则采用了Actor模型，每个Actor都是独立的，拥有自己的状态和消息队列，从而避免了锁的问题。
# distruptor和akka两种并发框架有啥区别

## Actor
Actor模式有一点类似面向对象模型，世界上所有的东西都被命名为Actor。

每一个Actor的属性绝不对外暴露，想和外界进行通信必须发送message，所以每个Actor自身都有一个邮箱。


 在使用Java/C# 等语言进行并发编程时需要特别的关注锁和内存原子性等一系列线程问题，而Actor模型内部的状态由它自己维护即它内部数据只能由它自己修改(通过消息传递来进行状态修改)，所以使用Actors模型进行并发编程可以很好地避免这些问题。Actor内部是以单线程的模式来执行的，类似于redis，所以Actor完全可以实现分布式锁类似的应用。
每个Actor都有一个专用的MailBox来接收消息，这也是Actor实现异步的基础。当一个Actor实例向另外一个Actor发消息的时候，并非直接调用Actor的方法，而是把消息传递到对应的MailBox里，就好像邮递员，并不是把邮件直接送到收信人手里，而是放进每家的邮箱，这样邮递员就可以快速的进行下一项工作。所以在Actor系统里，Actor发送一条消息是非常快的。

Actor模型=数据+行为+消息。

由于Actor系统的执行模型是单线程，并且异步，所以凡是有资源竞争的类似功能都非常适合Actor模型，比如秒杀活动。
 
基于以上的介绍，Actor模型在设计层面天生就支持了负载均衡，而且对于水平扩容支持的非常好。当然Actor的分布式系统也是需要服务注册中心的。

虽然Actor是单线程执行模型，并不意味着每个Actor都需要占用一个线程，其实Actor上执行的任务就像Golang的goroutine一样，完全可以是一个轻量级的东西，而且一个宿主上所有的Actor可以共享一个线程池，这就保证了在使用最少线程资源的情况下，最大量化业务代码。



------------------
## CSP
总的来说，Golang 提供了两种不同的方案：一种方案支持协程之间以共享内存的方式通信，Golang 提供了管程和原子类来对协程进行同步控制，这个方案与 Java 语言类似；另一种方案支持协程之间以消息传递（Message-Passing）的方式通信，本质上是要避免共享，Golang 的这个方案是基于 CSP（Communicating Sequential Processes）模型实现的。

Golang 比较推荐的方案是后者。《42 | Actor 模型：面向对象原生的并发模型》https://www.cnblogs.com/xidongyu/articles/12241787.html 

CSP的是Communicating Sequential Processes (CSP)的缩写，翻译成中文是顺序通信进程，不过这个名字比较拗口，下文将用CSP来代替。
CSP的核心思想是多个线程之间通过Channel来通信（对应到golang中的chan结构），有点像是管道的概念。（Pipe）



如何深入浅出地解释并发模型中的 CSP 模型？ - 知乎
https://www.zhihu.com/question/26192499/answer/46345499
一个简单的CSP程序 in golang：package main


```go

import "fmt"

var ch = make(chan string)

func message(){
    msg := <- ch
    fmt.Println(msg)    
}

func main(){
    go message()
    ch <- "Hello,CSP."
}

```
producer customer

```
//生产者
func main(){
	//1.
    ch := make(chan Data, 4)
    //2.
    for _, task := range  {
        ch <- task
    }
    //3.
    for i := 0; i< 10; i++ {
        go consumer(ch)
    }
}

// 消费者
func consumer(ch chan Data){
    for {
        //收取任务并处理
        data := <- ch
        process(data)
    }
}

```

------------


## Disruptor

在编程过程中，加锁通常会严重地影响性能，所以尽量用无锁方式，就产生了 Disruptor 这种无锁高并发框架
 
Disruptor的最常用的场景就是“生产者-消费者”场景，对场景的就是“一个生产者、多个消费者”的场景，并且要求顺序处理。
举个例子，我们从MySQL的BigLog文件中顺序读取数据，然后写入到ElasticSearch（搜索引擎）中。在这种场景下，BigLog要求一个文件一个生产者，那个是一个生产者。而写入到ElasticSearch，则严格要求顺序，否则会出现问题，所以通常意义上的多消费者线程无法解决该问题，如果通过加锁，则性能大打折扣
 
链接：https://juejin.cn/post/7071655437019381774 

------------

如何深入浅出地解释并发模型中的 CSP 模型？ - 夏梓耀的回答 - 知乎
https://www.zhihu.com/question/26192499/answer/75803446
严肃理论和PPT https://www.cs.kent.ac.uk/projects/ofa/jcsp/cpa2007-jcsp.pdf