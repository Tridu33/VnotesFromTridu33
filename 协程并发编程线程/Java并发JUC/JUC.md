# JUC
​ JUC主要是指JDK8中java.util.concurrent里提供的一系列线程并发工具，但是线程并发的问题远不止几个工具这么简单。






​ JDK中提供了几个并发工具，能够很好的简化对线程进行各种排队逻辑的编程模型。常用的有三个，CountDownLatch，CyclicBarrier，Semaphore。另外还有一个用得不是很多的SynchronousQueue。






AQS框架




​ JDK中通过Executor可以快速创建四种线程池：











​ 1、Executors.newFixedThreadPool(int nThreads)：固定大小的线程池。

线程池中会维护固定个数的线程，这也意味着，在同一时刻，最多只能有nThreads个线程并发执行。并且，如果在线程池没有进行shutdown的情况下，有一个线程出现了非法中断的情况，线程池中也会创建一个新的线程代替中断的线程，保持线程个数是固定的。内部使用一个LinkedBlockingQueue来保持Runnable任务队列。

​ 2、Executors.newSingleThreadExecutor()：

这是一个单线程的线程池，可以保证所有的线程都是串行执行的。内部同样使用了一个LinkedBlockingQueue来保持Runnable任务队列。

​ 3、Executors.newCachedThreadPool()：

这是一个带缓存功能的无界线程池。这个线程池在需要时可以无限的创建新的线程(最大值是Integer.MAX_VALUE)，但是他会尽量使用之前创建的线程。他非常适合用来运行一些包含非常多声明周期短的异步线程的程序，可以显著的提升程序的运行效率。当线程池内线程不够时，他会主动创建新的线程。但是当已有的线程长期没有使用时(60秒)，线程就会被回收，并从线程池中移除。他内部就是使用一个SynchronousQueue来保持Runnable任务队列。

​ 4、Executors.newScheduledThreadPool(int corePoolSize)：

这是一个带延迟功能的线程池。在执行Runnable任务时，可以指定一个延迟时间delay，或者指定一个执行周期，重复执行。另外还可以创建一个单线程版本的延迟线程池，Executors.newSingleThreadScheduledExecutor(); 他内部使用的一个自定义的DelayedWorkQueue队列来保持Runnable任务队列。

​ 常用的就是这四种线程池。

另外还有一种线程池Executors.newWorkStealingPool(int parallelism)是用来执行fork/join计算的，用得很少。
​ 这四种线程池的实例类型都是ExecutorService的实现类。使用时，可以通过ExecutorService接口定义的submit方法提交一个runnable任务或者一个callable任务。也可以通过Executor接口定义的execute方法提交一个runnable任务。关于runnable和callable的区别就不再多说了。
