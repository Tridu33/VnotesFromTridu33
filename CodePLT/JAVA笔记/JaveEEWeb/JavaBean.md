# 1. JavaBean[https://zh.wikipedia.org/wiki/JavaBeans](https://zh.wikipedia.org/wiki/JavaBeans)

1、所有属性为private  
2、提供默认构造方法  
3、提供getter和setter  
4、实现serializable接口



https://www.zhihu.com/question/19773379



java bean

https://www.liaoxuefeng.com/wiki/1252599548343744/1260474416351680


. Java代码助手

在线运行java

https://www.liaoxuefeng.com/wiki/1252599548343744/1252598088725056



对于一个Bean 来说，如果你依赖别的Bean , 只需要声明即可， spring 容器负责把依赖的bean 给“注入进去“， 起初大家称之为控制反转(IoC)

https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513118&idx=1&sn=487fefb8fa7efd59de6f37043eb21799#rd 
后来 Martin flower 给这种方式起来个更好的名字，叫“依赖注入”。










哦，Bean就是特定写好的一些类，写好的编译成.class,用来以后使用的方法组件，就像咖啡豆，等需要泡咖啡的时候ioc核心容器映射来管理调用他，然后泡出“一杯Java咖啡”，简单来说就是写好准备供人调用的“工具人”代码？

至于定义中满足的get,set，序列化等等特定，都是Bean这种类要满足的条件，就像数学上的定义需要各种条件满足，则定义为Bean。

尽管有定义，我们还是看不同数学定义的“约定”提出的思路想法，也是不能理解这个定义是怎么空降的？数学分析应该从理解的角度，老妪能懂而不是用术语去解析术语（装逼行话效率，但不是新手友好的理解方式）的东西。



但是认识一个名词不能靠粗浅的比喻，“苹果”不能解析为“一种水果”，但是也不能仅仅通过色香味的口语描述来讲解，学习一个新事物最好的方法是实现一个最小可重现程序，基本原理的粗略框架，因为：

数学不关心叫什么，关心事物内在练习和它们之间的满足的约束/条件/关系。

名词党知道名词没有用，代码是一种动手写，一聊天就知道深浅的“手上功夫”。




























