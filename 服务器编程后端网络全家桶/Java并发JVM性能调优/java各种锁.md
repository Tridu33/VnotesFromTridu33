









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








