
https://zhuanlan.zhihu.com/p/61049063


# 1. 堆栈数据区JVM
**寄存器**：最快的存储区, 由编译器根据需求进行分配,我们在程序中无法控制.

**栈**：存放基本类型的变量数据和对象的引用，但对象本身不存放在栈中，而是存放在堆（new 出来的对象）或者常量池中（字符串常量对象存放在常量池中。）

**堆**：存放所有new出来的对象。

**静态域**：存放静态成员（static定义的）

**常量池**：存放字符串常量和基本类型常量（public static final）。

**非RAM存储**：硬盘等永久存储空间

从堆和栈的功能和作用来通俗的比较,**堆主要用来存放对象的，栈主要是用来执行程序的**.
https://blog.csdn.net/sivyer123/article/details/17139443

**内存分配策略**

　　按照编译原理的观点,程序运行时的内存分配有三种策略,分别是静态的,栈式的,和堆式的.

**静态存储分配**是指在编译时就能确定每个数据目标在运行时刻的存储空间需求,因而在编译时就可以给他们分配固定的内存空间.这种分配策略要求程序代码中不允许有可变数据结构(比如可变数组)的存在,也不允许有嵌套或者递归的结构出现,因为它们都会导致编译程序无法计算准确的存储空间需求.

**栈式存储分配**也可称为动态存储分配,是由一个类似于堆栈的运行栈来实现的.和静态存储分配相反,在栈式存储方案中,程序对数据区的需求在编译时是完全未知的,只有到运行的时候才能够知道,但是规定在运行中进入一个程序模块时,必须知道该程序模块所需的数据区大小才能够为其分配内存.和我们在数据结构所熟知的栈一样,栈式存储分配按照先进后出的原则进行分配。

　　静态存储分配要求在编译时能知道所有变量的存储要求,栈式存储分配要求在过程的入口处必须知道所有的存储要求,而**堆式存储分配**则专门负责在编译时或运行时模块入口处都无法确定存储要求的数据结构的内存分配,比如可变长度串和对象实例.堆由大片的可利用块或空闲块组成,堆中的内存可以按照任意顺序分配和释放.




**JVM中的堆和栈**

　　JVM是基于堆栈的虚拟机.JVM为每个新创建的线程都分配一个堆栈.也就是说,对于一个Java程序来说，它的运行就是通过对堆栈的操作来完成的。堆栈以帧为单位保存线程的状态。JVM对堆栈只进行两种操作:以帧为单位的压栈和出栈操作。

　　我们知道,某个线程正在执行的方法称为此线程的当前方法.我们可能不知道,当前方法使用的帧称为当前帧。当线程激活一个Java方法,JVM就会在线程的 Java堆栈里新压入一个帧。这个帧自然成为了当前帧.在此方法执行期间,这个帧将用来保存参数,局部变量,中间计算过程和其他数据.这个帧在这里和编译原理中的活动纪录的概念是差不多的.

　　从Java的这种分配机制来看,堆栈又可以这样理解:堆栈(Stack)是操作系统在建立某个进程时或者线程(在支持多线程的操作系统中是线程)为这个线程建立的存储区域，该区域具有先进后出的特性。

　　每一个Java应用都唯一对应一个JVM实例，每一个实例唯一对应一个堆。应用程序在运行中所创建的所有类实例或数组都放在这个堆中,并由应用所有的线程共享.跟C/C++不同，Java中分配堆内存是自动初始化的。Java中所有对象的存储空间都是在堆中分配的，但是这个对象的引用却是在堆栈中分配,也就是说在建立一个对象时从两个地方都分配内存，在堆中分配的内存实际建立这个对象，而在堆栈中分配的内存只是一个指向这个堆对象的指针(引用)而已。


































在Java中，栈stack内存是用来存储函数的主体和变量名的。Java中的代码是在函数体中执行的，每个函数主体都会被放在栈内存中，比如main函数。加入main函数里调用了其他的函数，比如add（），那么在栈里面的的存储就是最底层是main，mian上面是add。栈的运行时后入先出的，所以会执行时会先销毁add，再销毁main。  
在Java中，堆内存是用来存储实例的。比如main函数里面声明了一个people的类per，people per；这个per是存储在栈stack内存中的，实例化后（per = new people（））；实例后的对象实体是存在堆heap内存中的。栈stack内存中存储的per存储着指向堆heap内存的地址指向。堆heap内存的存在是为了更好的管理内存，实现garbage collection。当per不再指向堆heap内存中的实例的时候，garbage collection机制就会把这个堆heap内存中的new people（）实例删除，释放内存。

  
  
作者：Chloe  
链接：https://www.zhihu.com/question/24807877/answer/139282174  

栈和堆不是Java特有的概念，几乎所有的可执行程序，不论操作系统，都会有这两个内存区域的定义。在网上随机搜了几篇文章，看了之后应该能够解决你的困惑。  

-   [Memory Management/Stacks and Heaps](https://link.zhihu.com/?target=http%3A//en.wikibooks.org/wiki/Memory_Management/Stacks_and_Heaps)
-   [Stack-based memory allocation](https://link.zhihu.com/?target=http%3A//en.wikipedia.org/wiki/Stack-based_memory_allocation)
-   [http://www.seas.upenn.edu/~ese112/spring09/programming/lectures/references.pdf](https://link.zhihu.com/?target=http%3A//www.seas.upenn.edu/~ese112/spring09/programming/lectures/references.pdf)

  
  
作者：孙立伟  
链接：https://www.zhihu.com/question/24807877/answer/29048779  


















https://zhuanlan.zhihu.com/p/44694290






我们首先明确一个观念，我们的数据都是存在内存里的，但是不同的数据，在内存中存放的区域是不同的。有的数据存放在栈，有的数据存放在堆。具体谁放在哪，我们首先要明确数据的类型。

**基础类型（又叫值类型）**：我前面讲的都是基础类型，byte，short，int，long，float，double，boolean，char，基础类型全部存在**栈**里面。

**引用类型**：数组，类，接口，引用类型变量存在**栈**，对象存在**堆**，通过引用确定关系。
https://zhuanlan.zhihu.com/p/38757793
![](_v_images/1555246661_3362.png)

.class文件是一段包含着虚拟机指令、程序和数据片段的二进制文件，即字节码，为什么叫字节码？因为这种类型的代码以一个字节8bit为最小单位储存。

类从被加载到虚拟机内存中开始，到卸载出内存为止，它的整个生命周期包括：**Loading(加载)、Verification(验证)、Preparation(准备)、Resolution(解析)、Initialization(初始化)、Using(使用)和Unloading(卸载)**7个阶段。其中验证、准备、解析3个部分统称为**连接(Linking)**



**这里需要注意：从类的加载→验证→准备→初始化，过程是按顺序依次开始的，但是解析比较特殊。为了支持java语言的晚期绑定/动态绑定，有时解析可以在初始化之后才开始。而且，这只是开始顺序，一个阶段通常执行的过程中会激活调用另一个阶段，所以各个阶段只是按照这个顺序开始，而不会等一个阶段完全完成后才进行下一个阶段，各个阶段是交叉混合进行的，所以各阶段并不会严格按照此顺序结束。**



双亲委派模型








 #  官方资源
 https://docs.oracle.com/javase/8/docs/api/
 

[目前 Java 后端有哪些不是很有必要去学的？https://www.zhihu.com/question/305924723/answer/557800752](https://www.zhihu.com/question/305924723/answer/557800752)

https://docs.oracle.com/javase/8/docs/api/overview-summary.html

本人19本科应届生，专注Java后台学习，已签腾讯WXG的offer（日后转c++)。

众所周知，鹅厂后台一直以C++为重，面试官也是做C++开发。但是语言只是工具，对代码的理解才是核心。面试时重点考察的是基础知识，以及解题的思考过程。凭借着对Java的理解去回答，也受到了面试官的认可，最终幸运的拿到offer。

一直以来，通过知乎这个程序员大牛聚集地，学习到了很多经验方法，也少走了很多弯路。感谢这个平台给予我的帮助，同时也分享一下我的Java学习经验。


**Java基础**

做java开发，java基础是最需要下功夫的一项。在校招时最注重的就是基础，拿不出像样的项目没关系，但是基础万万不可不牢固。

1.  想要基础扎实，看书沉淀是必须的，有一些编程基础的同学推荐阅读**《JAVA核心技术 卷1》**，可以跳过图形程序设计、事件处理、Swing、applet以及部分日志章节，如果比较吃力也可以先跳过多线程章节。
2.  看完一本书，一定要多加练习去理解和吸收。科班的同学可以用java写实验，写的同时一定要多多运用学到的特性。练习阶段各种设计模式套上去用，不要怕笨重，即使是滥用特性和设计模式也是一种有效的学习。
3.  有了一定量的编程经验后，可以再回过头将**《JAVA核心技术 卷1》**速读一遍，查漏补缺。同时我们开始扩宽我们的知识领域，开始进行JavaWeb的学习。


**JavaWeb基础**

JavaWeb是一系列技术的综合，也是大多数Java学习者日后的技术方向。及早的了解JavaWeb也有利于更深层面理解，Java在完整的应用中，是如何与各个模块交互并发挥作用的。

基础篇包括Servlet和JSP的学习、tomcat的使用、理解MVC分层模式、mysql的基础用法及JDBC、了解http协议。

1.  这部分的学习，我是通过**《Head First Servlets and JSP》** 。这本书轻松幽默读起来很愉快，但是实在是很厚，而且部分技术已经过时，有时间的同学可以选读。
2.  可以看到这部分的内容是很杂且多的，此阶段注重广度的基础学习，日后慢慢深入。这里推荐个在线教程：

-   ***[Servlet系列教材 （一）- 基础 - 教程：开发第一个Servlet - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/servlet/servlet-eclipse/558.html%3Fp%3D974)***
-   ***[mysql系列教材 （一）- 安装mysql-server - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/mysql/mysql-install/377.html%3Fp%3D974)***
-   ***[Tomcat系列教材 （一）- 教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/tomcat/tomcat-tutorial/541.html%3Fp%3D974)***
-   ***[JSP系列教材 （一）- 教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/jsp/jsp-tutorials/530.html%3Fp%3D974)***
-   ***[HTTP协议系列教材 （一）- 教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/http/http-tutorials/568.html%3Fp%3D974)***
-   ***[JDBC系列教材 （一）- Java 使用JDBC之前，先要准备mysql](http://link.zhihu.com/?target=http%3A//how2j.cn/k/jdbc/jdbc-mysql/386.html%3Fp%3D974)***
-   ***[MVC系列教材 （一）- 教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/mvc/mvc-tutorials/561.html%3Fp%3D974)***

3\. 重点要理解Servlet的原理以及生命周期。在完成这一部分的学习后，可以简单的做个小网站，包括注册登陆，增删改查等功能。如果想继续折腾，可以考虑将项目部署在阿里云或者腾讯云上，一个完整可供他人访问的项目，所获得的成就感是非凡的。

***[部署到Linux系列教材 （一）- 介绍 - 如何把J2EE应用部署到Linux - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/deploy2linux/deploy2linux-breif/1591.html%3Fp%3D974)***


**Java进阶**

Java始终是我们JavaWeb开发体系中最核心的一环，唯有不停地探索，才能把握住方向和机遇。

1.  在做完一个简单完整的JavaWeb项目后，我们对代码的认知和理解会提高不少，这对接下来的深入学习打下基础。Java圣经：**《JAVA编程思想》** 值得仔细品读，作者的功力十分深厚，即使很多内容还无法理解，但每次读完一定会有所收获。同样建议跳过“图形化用户界面“章节，这是一本伴随我们技术成长的好书，买一本放在旁边，摸着就有底气。
2.  读完编程思想，建议写一个有一定复杂度和代码量的后台项目。可以是一个http服务器，一个大型聊天室，也可以参考我的项目实现一个DBMS：***[wwwyanxin/wyxDBMS](http://link.zhihu.com/?target=https%3A//github.com/wwwyanxin/wyxDBMS)*** 这一部分要强化我们的Java基础，同时也为日后的招聘积累项目经验。
3.  做完项目我们又该看书沉淀技术了，此时我推荐**《Effective Java》**，这本书并不厚但是干货十足，作者讲述Java的最佳实践和经验规则。它能帮助我们写出清晰、健壮、高效的代码，同时这本书涵盖了非常多的面试考点，一定要牢记于心！
4.  最后还要深入学习Java多线程技术以及Java虚拟机原理，这两部分难度较大，理解起来比较抽象。也许日后工作中，我们很少遇到并发问题，不一定有机会进行JVM调优，但是这部分一定要认真对待，越理解底层写出的代码越高效，查bug时越准确，另外更重要的是面试常考！推荐两本书**《Java并发编程的艺术》《深入理解Java虚拟机》，**以及并发编程网：***[并发编程网 \- ifeve.com](http://link.zhihu.com/?target=http%3A//ifeve.com/)*** 重点掌握java内存模型，各种锁的原理及应用，JVM GC垃圾回收原理。


**JavaWeb进阶**

围绕整个java体系学习，我们要筑起高高的城墙。

1.  **Linux**，现在的服务器基本都是Linux系统，也不存在图形化操作界面。作为开发工程师推荐阅读**《The Linux Command Line》**，有中文在线免费版本**[TLCL](http://link.zhihu.com/?target=http%3A//billie66.github.io/TLCL/index.html)。**那本《鸟哥的Linux私房菜》更适合运维工程师，就不推荐给大家了。学习的时候，可以去阿里云或腾讯云租一个学生服务器，每个月大概10元左右，直接ssh到云服务器上操作，能更好地模拟公司的开发及生产环境。
2.  **操作系统原理**，主要学习进程控制调度、进程通信、存储和设备管理、文件管理以及系统安全。这一部分可以通过看教材或者自行找一些网课补充。
3.  **数据库**，可以买一本**《MySQL必知必会》**小册子作为基础入门，没有什么理论的堆砌，是一本实践指南。学习数据库原理可以阅读**《MySQL技术内幕》**索引优化、事务、锁、范式都是重点。
4.  **网络协议**，入门可以读**《图解HTTP》《图解TCP/IP》**如果要深入研究可以读**《UNIX网络编程 卷1》**和**《TCP/IP详解 卷1》**大多数开发者接触http和tcp、udp、ip协议比较多，但是对整体网络协议栈有个完整了解是必要的。
5.  **数据结构与算法，**数据结构是算法的基础，一定要清晰明了。算法则是笔试面试中无法绕过的难关，推荐去LeetCode刷题，现在也有了中文官方网站：***[力扣 (LeetCode) 中国官网 - 全球极客挚爱的技术成长平台](http://link.zhihu.com/?target=https%3A//leetcode-cn.com/)*** 从easy难度开始刷起，积累一定题量之后，做算法题会很快找到类型方法。
6.  **SSM框架**，Spring+SpringMVC+MyBatis可以说是开发必备了，但框架只是锦上添花，不要太依赖框架进行学习。当我们能不依赖任何框架开发完整项目时，才是真正掌握了它。最为重要的是理解Spring的两个特性：IOC 反转控制和DI 依赖注入。明白实现原理以及为什么要使用Spring，只有这样才能在层出不穷的框架中灵活应对，立于不败之地。

-   [Spring系列教材 （一）- 教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/spring/spring-ioc-di/87.html%3Fp%3D974)
-   [Spring MVC系列教材 （一）- 教程](http://link.zhihu.com/?target=http%3A//how2j.cn/k/springmvc/springmvc-springmvc/615.html%3Fp%3D974)
-   [Mybatis系列教材 （一）- 基础 - 入门教程 - how2j.cn](http://link.zhihu.com/?target=http%3A//how2j.cn/k/mybatis/mybatis-tutorial/1087.html%3Fp%3D974)


**加分技能**

1.  **前端**，一些岗位要求全栈，即使不是全栈，懂得前端技术的后台能写出更加合理的接口，与前端工程师合作起来会更顺利，理解项目更通透，解决问题准确迅速。
2.  学习一门**动态语言**，动态语言开发起来更灵活迅速。同时比较动态静态语言的特点，可以更好去提炼跳出语言束缚的代码思想。推荐学习JavaScript或者Python等。
3.  **大数据**，大数据开发近几年也是热门方向之一，有兴趣的同学可以学习。
4.  **热门工具及框架**，包括分布式Dubbo、缓存优化redis、nginx、虚拟化技术docker等。一般来说本科应届生不会要求很高，但是要对热门技术有一定的了解。


**常用网站推荐**

1.  **GitHub： *[Build software better, together](http://link.zhihu.com/?target=https%3A//github.com/)***
2.  **Java学习：*[How2J 的 Java教程](http://link.zhihu.com/?target=http%3A//how2j.cn%3Fp%3D974)***
3.  **Linux命令行：*[TLCL](http://link.zhihu.com/?target=http%3A//billie66.github.io/TLCL/index.html)***
4.  **算法： *[力扣 (LeetCode) 中国官网 - 全球极客挚爱的技术成长平台](http://link.zhihu.com/?target=https%3A//leetcode-cn.com/)***
5.  **正则表达式测试：*[PHP, PCRE, Python, Golang and JavaScript](http://link.zhihu.com/?target=https%3A//regex101.com/)***









如何快速打好Java基础？ - 沈世钧的回答 - 知乎 https://www.zhihu.com/question/50904128/answer/521519858
我学习java的时候，先是通读了《Java编程思想》，然后是《Java核心技术》。当时这两本书还不像现在这么厚，而刚才我把案头的《Java核心技术》第9版翻了翻，上下两册已经1700多页了，可想而知，如果要把它通读一遍，且不说把所有的代码都调通，就是当小说读，估计也需要些时间。

但我现在教学依然首推《Java核心技术》，主要是体系完整，实例多，可操作性强。但对初学者，我一般是只讲前6章，也就是下面的内容：

1.  Java程序设计概述
2.  Java程序设计环境
3.  Java的基础程序设计结构
4.  对象与类
5.  继承
6.  接口与内部类

就《Java核心技术》第9版来说，也就是到250页为止，加把劲，1个月拿下完全没问题。

因为你是自学，所以建议你一定要把其中的代码都调通，课后的作业尽量去做。除此之外，还有两点特别重要：

  
  
作者：沈世钧  
链接：https://www.zhihu.com/question/50904128/answer/521519858  



目前 Java 后端有哪些不是很有必要去学的？ - 沈世钧的回答 - 知乎 https://www.zhihu.com/question/305924723/answer/557800752
# 2. basestone
“==”常用于用于比较引用和比较基本数据类型时是否具有不同的功能，比较基本数据类型，如果两个值相同，则结果为true而在比较引用时，如果引用指向内存中的同一对象，结果为true。
 直接用==做比较的时候就是比较对象的首地址，肯定是不相等的。
 
equals 方法的特点：

1、自反性：x.equals（x）返回true；

2、对称性：若x.equals（y）为true，则y.equals（x）亦为true；

3、传递性：若x.equals（y）为true且y.equals（z）也为true，则x.equals（z）亦为true；

4、一致性：x.equals（y）的第一次调用为true，那么x.equals（y）的第二次、第三次、第n次调用也均为true，前提条件是没有修改x也没有修改y；

5、对于非空引用x，x.equals（null）永远返回为false。

```
访问修饰符 返回值类型 方法名(参数列表){
    方法体 
}

public  void  functionName(Object arg){ 

}
```
4.**参数列表**：是传递给方法的参数列表，参数可以有多个，多个参数间以逗号隔开，每个参数由参数类型和参数名组成，以空格隔开。当方法被调用时，传递值给参数。这个值被称为实参或变量。参数列表是指方法的参数类型、顺序和参数的个数。参数是可选的，方法可以不包含任何参数。

5.**方法体**：方法体包含具体的语句，定义该方法的功能。



少了训练：

数组成绩






[方法重写与方法重载的区别](https://www.cnblogs.com/zheting/p/7751787.html)

# 3. 怎样理解JAVA的“构造方法”和“主方法

https://jingyan.baidu.com/article/380abd0a6b94701d90192cca.html

# 4. Java构造方法和析构方法
www.weixueyuan.net/view/5987.html




# 5. Java构造方法
c.biancheng.net/view/976.html



Java中引用变量有两个类型：
1、编译时类型，由声明该变量时使用的类型决定；
2、运行时类型，由实际赋给该变量的对象决定；
在编译时类型与运行时类型不一致时，就可能出现——多态
多态就是“多种形态“；在程序运行过程中才决定用哪个方法，多态性是允许你将父类对象设置成和它的一个或多个子对象相等的技术，赋值后，父对象就可以根据当前赋值给它的子对象的特性运作，即为多态。
多态是面向对象编程领域的核心概念。（面向对象三大特性：封装，继承，多态）
注意：重载方法在编译期间就确定了，是静态的；方法重载与多态无关，真正与多态相关的是重写（覆盖Override）；

多态的存在有3个条件，1)要有继承 2)要有重写3)父类引用指向子类对象

多态的特点：
变量：编译看父类
方法：运行看子类

多态从实现的角度分为：静态多态和动态多态
      静态多态也叫做编译时多态
      动态多态也叫做运行时多态  
多态：同一个符号在不同语义环境下具有不同的解释
一、多态是通过
    1、接口和实现接口并覆盖接口中同一个方法的几种不同的类体现的。
    2、父类和继承父类并覆盖父类中同一方法的几个不同子类实现的。

多态的实现方式：
1、重写
2、接口
3、抽象类和抽象方法
基本上是重载、接口、继承 可通过这三种方式实现 多态
方法的重载，继承或实现接口，父类引用指向子类对象


# 6. 实验楼3泛型集合
泛型即参数化类型，也就是说数据类型变成了一个可变的参数，在不使用泛型的情况下，参数的数据类型都是写死了的，使用泛型之后，可以根据程序的需要进行改变。

定义泛型的规则：

-   只能是类类型，不能是简单数据类型
-   泛型参数可以有多个
-   可以用使用 extends 语句或者 super 语句 如`<T extends superClass>`表示类型的上界，T 只能是 superClass 或其子类， `<K super childClass>`表示类型的下界，K 只能是 childClass 或其父类。
-   可以是通配符类型，比如常见的 `Class<?>`

https://www.shiyanlou.com/courses/running






































































































