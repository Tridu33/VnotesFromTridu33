




如何从零基础开发一个 Java 虚拟机？ - RednaxelaFX的回答 - 知乎
https://www.zhihu.com/question/51403067/answer/125878915
从表到里学习JVM实现 书单 
https://www.douban.com/doulist/2545443/









现在国内跟JVM相关的中文书有下面这么几本（有疏漏的欢迎评论提醒我补充）：

Java虚拟机规范(Java SE 7版)
深入理解Java虚拟机（第2版）
HotSpot实战
实战Java虚拟机
自己动手写Java虚拟机 <- 作者用Go语言按照JVM规范自己写的一个非常简单的JVM实现
Java性能优化权威指南 <- Charlie写的对应JDK6的版本
Java性能权威指南 <- Scott写的对应JDK7的版本
（深入Java虚拟机(原书第2版)比较过时所以我就不再推荐了。要读的话也请读原版）



上面的《自己动手写Java虚拟机》一书写的还真是作者自己从零开始实现简单JVM的历程。它虽然没有实现GC（依靠Go语言的运行时自身的GC）也没有实现JIT编译器（只用解释器），但是在核心运行时部分该做的许多东西都做了，挺好的。
虽说简易JVM与高性能JVM之间有巨大的差距，要最终达到能实现高性能JVM的水平的话总归得迈出第一步。

高性能的JVM实现涉及的知识面既广又深，有纯粹的编译原理，有垃圾回收，有体系结构，有操作系统，有并行/并发编程，并不是说写一个JVM只要知道JVM自身的规范和一门编程语言（如C++）的入门知识就够的。上面的书单列举的几本进阶书籍是这些额外知识的引导入门和稍微进阶一点的书，供同学们参考。

要说培训机构…我是没听说国内有哪些培训机构做深入的JVM相关知识的培训的。我以前在淘宝的时候有在淘宝技术大学（当时淘宝的内部技术培训部门）开过深入JVM系列的课程，不过讲得还不够好，经常把来听课的同事讲得睡着了（orz
我离开了阿里之后应该也还有其它同事做类似的内部培训吧。毕竟有自己的JVM团队在，不怕没人懂行。

我以前在JavaEye / ItEye组织过一个讨论区是专门讨论跟高级语言虚拟机相关话题的，高级语言虚拟机。里面有写老讨论串还挺有营养的，欢迎大家参考。
其中我的一些帖子的集合的链接我发在博客里了：自己关于VM的帖的目录

# 1. 官网
https://docs.oracle.com/javase/tutorial/java/IandI/usinginterface.html
  
    
      
        
          
            
              
                
                  
                    
                      
                        
                          
                            
                              
                                
                                  
                                    
                                      
                                        







# 2. 一个牛人给JAVA初学者的建议

https://blog.csdn.net/yaya_free/article/details/79086603

**推荐网站**  
www.javaeye.com //java视线论坛，Hibernate国内的权威  
dev2dev.bea.com //bea的dev2dev社区，用WebLogic首选的好去处  
www-128.ibm.com/developerworks //ibm developer works社区，ibm产品的老家  
www.jdon.com //j道，Jboss国内相对讨论会多一点的地方，有自己的框架  
www.matrix.org.cn //matrix，有自己的框架，很清新的论坛  
jcp.org //JCP，前面说到过了   
sourceforge.net //开源的东西几乎这里都可以找到，除java外还有游戏共享等  
saloon.javaranch.com //我常去，人气不错   
www.apache.org //阿帕奇老家   
www.jboss.com //Jboss和Hibernate老家  
www.springframework.org //Spring老家  
www.wiki.org //非常好的百科站点，可惜国内被封，创始人加入了Eclipse zone  
www.google.com //你要的这里有，不信？输入关键字再按一下那个靠左的白色按钮试试  
  
**书籍**  
《Thinking in Java》 //实话说，一般，尤其是翻译后的版本，原版还行  
《Java教程》 //电子工业出版社出版的那本，上下册，很厚，但翻译得不错  
《21天学通Java》 //入门极好，但是《21天学通j2ee》极烂，不要买  
《Mastering EJB》 //翻译过的书质量我不清楚，估计不怎样，请看原版书籍  
《精通Hibernate》 //看清楚作者，孙卫琴，其它人的别买  
  
其它的可以不用了，网络上的远比书上来得多，来得好，虽然也来得杂   
  
最后的建议   
一，不要做一个浮躁的人   
二，学好英语，很重要   
三，**阅读源代码和文档**  
四，共享源代码，不要做一个功利的人   
五，热爱Java






















































































javap math.class >math.txt
反汇编


https://www.bilibili.com/video/av45497157?from=search&seid=10098719170838094425




JVM

https://zhuanlan.zhihu.com/p/25713880
![](_v_images/1559284539_21578.png)

# 3. JVM原理最全、清晰、通俗讲解，五天40小时吐血整理

https://blog.csdn.net/csdnliuxin123524/article/details/81303711





https://blog.csdn.net/witsmakemen/article/details/28600127





# 4. 反射调用







'

# 5. interface

作者：invalid s  
链接：https://www.zhihu.com/question/48503724/answer/118893099  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

事实上，实现继承才是辣鸡，接口继承才是被实践证明的、真正有用的技术核心。

  

原因嘛：  
其一，实现继承导致父类-子类间出现强耦合，很容易导致软件复杂度失控；  
其二，面向对象本来想要的便利、也是唯一的优点，就是“无需区别就能处理接口兼容的一系列对象”，说白了玩的是架构设计，玩的是战略层面的问题。结果呢，业界几乎所有教程（超过99%！）都把学生误导到继承、多态相关的一些奇技淫巧上，试图以战术方面猥琐的投机代替战略方面的思考。这不仅进一步加强了前一个危害，而且成功的把初学者的注意力引偏方向，使得他们越学越屎。

以上，就使得面向对象技术成为公害——几乎99%的人都往反方向努力，甚至几乎所有的老师、所有的教材都直接把学生往反方向教的技术，不是公害是什么？——从而在近些年激起业界越来越强烈的反弹。

事实上，早在OO刚刚兴起之时，已经有很多“使用组合而不是继承”之类的忠告。  
遗憾的是，组合太过直白、太不容易用错，所以太不利于半瓶子咣当了；而继承就“完美”得多：复杂、微妙，但又不是太过难懂，甚至死记硬背几条规则就很容易把人唬的一愣一愣：这些特征简直是为半瓶子醋量身定做的。这就使得它飞快的蔓延开来，成为各种教材、各路“大神”装X的门面技能；再加上对类往粗俗处的无限联想……情况就彻底失控了。

  

[名家吐槽：面向对象编程从骨子里就有问题](https://link.zhihu.com/?target=http%3A//dev.yesky.com/405/34480405.shtml)  
原文：[Object Oriented Programming is Inherently Harmful](https://link.zhihu.com/?target=http%3A//harmful.cat-v.org/software/OO_programming/)

[面向对象编程的弊端是什么？ \- 知乎用户的回答](https://www.zhihu.com/question/20275578/answer/26577791?group_id=752158336673132544)

好的接口设计可以在大的、模块的层次上大幅简化项目，而继承则可在小的、细碎的层次上简化实现。如果过于注重后者、尤其是就着关于类的**比喻**做设计（而不是学术上严格的is-a定义），就很容易琐琐碎碎的搞成一滩，然后怎么都组织不起来。

综上。请搞懂继承和多态的原理/机制/效果，但要明白它们只是小道。如果过于注重、过于挖掘这些小道，不仅解决不了什么问题，反而会搞垮项目。真正应该搞懂的，还是接口设计这个正道。
























# 6. [java深浅克隆https://www.cnblogs.com/wuyudong/p/4399180.html](https://www.cnblogs.com/wuyudong/p/4399180.html)

https://www.zhihu.com/question/23031215

浅克隆不会克隆原对象中的引用类型，仅仅拷贝了引用类型的指向。深克隆则拷贝了所有。也就是说深克隆能够做到原对象和新对象之间完全没有影响。
https://blog.csdn.net/jeffleo/article/details/76737560
而深克隆的实现就是在引用类型所在的类实现*Cloneable*接口，并使用*public*访问修饰符重写*clone*方法。


## 6.1. 总结：

1.浅克隆：只复制基本类型的数据，引用类型的数据只复制了引用的地址，引用的对象并没有复制，在新的对象中修改引用类型的数据会影响原对象中的引用。  
2.深克隆：是在引用类型的类中也实现了clone，是clone的嵌套，复制后的对象与原对象之间完全不会影响。  
3.使用序列化也能完成深复制的功能：对象序列化后写入流中，此时也就不存在引用什么的概念了，再从流中读取，生成新的对象，新对象和原对象之间也是完全互不影响的。  
4.使用clone实现的深克隆其实是浅克隆中嵌套了浅克隆，与toString方法类似


















 p, li { white-space: pre-wrap; } 

  

  

\# https://github.com/silenceyear/zzax/blob/master/java112/doc/memory.md

  

https://www.bilibili.com/video/av49987505?from=search&seid=10098719170838094425

  

  

  

  

  

  

  

  

  

https://www.youtube.com/watch?v=cxh4avYqBFU

  

http://zzax.io/java112/

  

http://zzax.io/java112/doc/transition/

  

  

https://www.zhihu.com/question/29833675

!\[\](\_v\_images/1559228732_20953.png)

  

  

  

  

  

  

  

  

  

  

  

  

  

  

正好开了专栏，写了几篇Java虚拟机相关的文章,关于Java虚拟机的堆、栈、局部变量表等，可以参考下专栏里的这篇—\[Java虚拟机—堆、栈、运行时数据区\](https://zhuanlan.zhihu.com/p/44694290)

**专栏里的文章主要内容总结自-《深入理解Java虚拟机》-周志明第二版和《Java虚拟机规范JavaSE8》,以下是Java虚拟机相关的部分文章:**

  

\[Java虚拟机——字节码、机器码和JVM\](https://zhuanlan.zhihu.com/p/44657693)

  

\[Java虚拟机——类加载机制和类加载器\](https://zhuanlan.zhihu.com/p/44670213)

\[Java虚拟机—堆、栈、运行时数据区\](https://zhuanlan.zhihu.com/p/44694290)

  

\[Java虚拟机—Class文件结构\](https://zhuanlan.zhihu.com/p/45003974)

  

\[Java虚拟机—字节码指令初探\](https://zhuanlan.zhihu.com/p/45050364)

  

\[Java虚拟机—栈帧、操作数栈和局部变量表\](https://zhuanlan.zhihu.com/p/45354152)

  

\[Java虚拟机—对象的内存布局和访问定位\](https://zhuanlan.zhihu.com/p/44948944)

  

\[Java虚拟机—堆内存分代和GC垃圾收集算法\](https://zhuanlan.zhihu.com/p/45558897)

  

作者：Lyon

链接：https://www.zhihu.com/question/29833675/answer/506600010

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

https://github.com/silenceyear/zzax/














# 7. JAVA堆栈内存JVM本质
https://github.com/silenceyear/zzax/blob/master/java112/doc/memory.md

https://www.bilibili.com/video/av49987505?from=search&seid=10098719170838094425









https://www.youtube.com/watch?v=cxh4avYqBFU

http://zzax.io/java112/

http://zzax.io/java112/doc/transition/


https://www.zhihu.com/question/29833675
![](_v_images/1559228732_20953.png)














正好开了专栏，写了几篇Java虚拟机相关的文章,关于Java虚拟机的堆、栈、局部变量表等，可以参考下专栏里的这篇—[Java虚拟机—堆、栈、运行时数据区](https://zhuanlan.zhihu.com/p/44694290)  
**专栏里的文章主要内容总结自-《深入理解Java虚拟机》-周志明第二版和《Java虚拟机规范JavaSE8》,以下是Java虚拟机相关的部分文章:**

[Java虚拟机——字节码、机器码和JVM](https://zhuanlan.zhihu.com/p/44657693)

[Java虚拟机——类加载机制和类加载器](https://zhuanlan.zhihu.com/p/44670213)  
[Java虚拟机—堆、栈、运行时数据区](https://zhuanlan.zhihu.com/p/44694290)

[Java虚拟机—Class文件结构](https://zhuanlan.zhihu.com/p/45003974)

[Java虚拟机—字节码指令初探](https://zhuanlan.zhihu.com/p/45050364)

[Java虚拟机—栈帧、操作数栈和局部变量表](https://zhuanlan.zhihu.com/p/45354152)

[Java虚拟机—对象的内存布局和访问定位](https://zhuanlan.zhihu.com/p/44948944)

[Java虚拟机—堆内存分代和GC垃圾收集算法](https://zhuanlan.zhihu.com/p/45558897)

  
  
作者：Lyon  
链接：https://www.zhihu.com/question/29833675/answer/506600010  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。













# 8. bug

源码报错源码

https://blog.csdn.net/weixin_42163563/article/details/82866440
运行jar文件出现了Exception in thread “main" java.lang.UnsupportedClassVersionError



















https://github.com/silenceyear/zzax/










