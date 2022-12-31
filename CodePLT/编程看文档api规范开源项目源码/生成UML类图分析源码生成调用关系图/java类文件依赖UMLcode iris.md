

https://blog.csdn.net/hy_coming/article/details/80741717

IDEA

2011 IEEE Symposium on Visual Languages and Human-Centric Computing978
paper 《Visualizing Call Graphs》

插件




https://blog.csdn.net/zj420964597/article/details/87856758





idea 看源码关系uml插件推荐 code iris https://blog.csdn.net/u013939918/article/details/107087321

最近看源码就想找个uml的类图工具，网上看了一些，发现都是一些单个类的继承关系图，如果不知道的朋友，可以用uml插件工具搜索uml即可（uml support），然后每次点击右键后在菜单下面找Diagrams，但是我们今天介绍的不是这个，而是另外一个不错的插件，叫code iris。这个是可以显示整个工程所有类关系图的插件。


**实线箭头**表示单向关联，即：关联类知道被关联类的公共属性及操作，但被关联类 并不知道关联类的公共属性及操作。

关联单向、双向之分。双向关联用没有箭头的实线表示 ，实线箭头表示Object Message，也就是类间的消息发送，
比如：方法调用和请求等等，这些都是从一方向另一方主动发出信息。


**虚线箭头**表示两个类之间存依赖关系。即：一个类引用另一个类。只存在单向依 赖。 虚线箭头表示Return Message，
一般用于表示方法调用后的返回信息
代码中的表现：

**实线代表**有引用的关联，一般代码中会直接有关联的类的引用，但**虚线**就没有，一般只是方法上的调用关系。如是而已。


# 1. java类文件依赖UML


http://nettee.github.io/posts/2018/Depview-View-invocation-relationships-in-Java-projects/
java文件类依赖图https://blog.csdn.net/xyzjl/article/details/45269185
idea
https://blog.csdn.net/liumiaocn/article/details/108414583
















