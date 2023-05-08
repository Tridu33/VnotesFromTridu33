synchronized各种加锁场景的作用范围(来自面经总结 https://blog.csdn.net/qq_45140716/article/details/119464196)
1.作用于非静态方法，锁住的是对象实例(this)，每一个对象实例有一个锁。

public synchronized void method() {}

2.作用于静态方法，锁住的是类的Class对象，因为Class的相关数据存储在永久代元空间，元空间是全局共享的，因此静态方法锁相当于类的一个全局锁，会锁所有调用该方法的线程。

public static synchronized void method() {}

3.作用于Lock.class，锁住的是Lock的Class对象，也是全局只有一个。

synchronized (Lock.class) {}

4.作用于this，锁住的是对象实例，每一个对象实例有一个锁。

synchronized(this){}

5.作用于静态成员变量，锁住的时该静态成员变量对象，由于是静态变量，因此全局只有一个。

public static Object monitor = new Object(); synchronized (monitor) {}










# java各种锁
Java 中的锁有三类，一种是关键字 Synchronized，一种是对象 lock，还有一种 volatile 关键字。

- volatile

人称轻量级的synchronized，但其实无关，仅仅修饰可见性等


CAS也不属于加锁，是一种CPU指令，原子类AtomicXXX才是

volatile 作用范围小，只作用在**一个变量**上。


https://www.cnblogs.com/lifegoeson/p/13683785.html

- 隐式锁synchronized，jvm层面管程隐式地加锁



Synchronized 用于**代码块或方法**中，他能是一段代码处于同步执行。




- 显式锁Lock接口(java各种实现聚合为一个同步器AQS:ReentrantLock重入锁ReadLock读锁writeLock写锁)

lock 跟 synchronized 类似，但需要自行加锁和释放锁。必须要手动释放锁，不然会造成死锁。


偏向锁 自旋锁 轻量级锁 重量级锁





18种锁 https://juejin.cn/post/6976622790724026376

![dd9104a9840f4c148b07847928780982~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd9104a9840f4c148b07847928780982~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp)





Java锁总结
https://www.cnblogs.com/lifegoeson/p/13683785.html





