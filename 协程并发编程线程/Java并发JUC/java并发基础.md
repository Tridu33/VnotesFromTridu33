





# java并发编程


https://javaguide.cn/java/concurrent/java-concurrent-questions-01.htm 
![](https://oss.javaguide.cn/github/javaguide/java/concurrent/640.png)





创建Thread类，

用Runnable创建线程。但是，Runnable缺少的一项功能是，当线程终止时（即run（）完成时），我们无法使线程返回结果。

Java中提供了Callable接口。为实现Callable而必须重写call方法。
为了实现Runnable，需要实现不返回任何内容的run（）方法，而对于Callable，需要实现在完成时返回结果的call（）方法。



```java
//1、线程池实现
ThreadPoolExecutor aa =   (ThreadPoolExecutor)Executors.newFixedThreadPool (100);
//当调用submit的时候，会把Callable对象传递进去初始化一个FutureTask对象，然后调用execute方法。
//FutureTask已有实现好的run方法。run方法中调用了call()方法
Future<Integer> task1 = aa.submit(new Callable<Integer>() {
            @Override
            public Integer call() throws Exception {
                return 11;
            }
        });
//2、直接start
FutureTask<String> task = new FutureTask(new Callable(){
            public String call(){
                return "";
            }
        });
Thread thread = new Thread(task);
thread.start();
```


# synchronized



# wait/notify



# fork/join


# Lock











# Q&A



- 可以直接调用 Thread 类的 run 方法吗？ 
- 
new 一个 Thread，线程进入了新建状态。调用 start()方法，会启动一个线程并使线程进入了就绪状态，当分配到时间片后就可以开始运行了。 start() 会执行线程的相应准备工作，然后自动执行 run() 方法的内容，这是真正的多线程工作。 但是，直接执行 run() 方法，会把 run() 方法当成一个 main 线程下的普通方法去执行，并不会在某个线程中执行它，所以这并不是多线程工作。

总结： 调用 start() 方法方可启动线程并使线程进入就绪状态，直接执行 run() 方法的话不会以多线程的方式执行。
















































































