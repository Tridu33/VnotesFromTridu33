
[Java中常用到的几种数据结构 Queue， List ，ArrayList](https://blog.csdn.net/qq_33608638/article/details/79600657)




# 1. javadeQue


```
Queue queue=new LinkList(); 
```

Java中的Queue是接口（所以 不可以 new Queue<...>()来创建），这个接口的实现有两个常见的类来实现。



```
Java 队列 queue的一些操作，
    add        增加一个元索                     如果队列已满，则抛出一个IIIegaISlabEepeplian异常
　　remove   移除并返回队列头部的元素    如果队列为空，则抛出一个NoSuchElementException异常
　　element  返回队列头部的元素             如果队列为空，则抛出一个NoSuchElementException异常
　　offer       添加一个元素并返回true       如果队列已满，则返回false
　　poll         移除并返问队列头部的元素    如果队列为空，则返回null
　　peek       返回队列头部的元素             如果队列为空，则返回null
　　put         添加一个元素                      如果队列满，则阻塞
　　take        移除并返回队列头部的元素     如果队列为空，则阻塞
```























