[TOC]






《数据结构与问题求解》<https://www.academicwork.com>
# 1. JDK查看源码

https://www.cnblogs.com/lxmyhappy/p/7084097.html
导入源码查看复制问题

https://blog.csdn.net/weixin_38719347/article/details/72593990

# 2. debug

https://blog.csdn.net/maritimesun/article/details/7815903




# 3. 关于Java，J2EE，JSP，Servlet，Tomcat之间是什么关系

这个问题，首先了解它们是什么，然后理解它们相互之间的关系。
作者：乔冬  
链接：https://www.zhihu.com/question/57205755/answer/282751360  
 

> [Java](http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/Java/85979)是一门[面向对象](http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%25E9%259D%25A2%25E5%2590%2591%25E5%25AF%25B9%25E8%25B1%25A1)编程***语言，用来进行开发。*** *j*ava EE*(*Java Enterprise Edition)：Java平台企业版，适用于创建服务器应用程序和服务。

***javaEE*是*Java*平台的3个版本之一。**

> 【规范】: A servlet is a Java™ technology-based Web component, managed by a container, thatgenerates dynamic content.

【译文】: Servlet是基于Java技术的、容器托管的、用于生成动态内容的***Web组件***。

***Servlet*是用*Java编写*的服务器端程序，属于*JavaEE体系*的重要组成部分。**

> JSP全名为Java Server Pages，中文名叫java[服务器](http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8)页面。

***JSP由html代码嵌入java代码组成，本质上*是一个简化的*[Servlet](http://link.zhihu.com/?target=https%3A//baike.baidu.com/item/Servlet)，*在*Tomcat下运行。***

> Tomcat是Apache 软件基金会的Jakarta 项目中的一个核心项目。

***Tomcat*由*java*开发的，可以作为*servlet组件以及jsp的*容器来使用，同时承担Web服务器功能。**


















**容器类**
https://www.cnblogs.com/jamesvoid/p/9778907.html
![容器](_v_images/容器_1555239539_1798.png)
https://zhuanlan.zhihu.com/p/58809207


https://img-blog.csdn.net/20160124221843905


# 4. Java高级编程语言

  

  

  

\[Java之数组array和集合list、set、map\](https://www.cnblogs.com/liyiran/p/4607817.html)

  

  

世间上本来没有集合,(只有数组参考C语言)但有人想要,所以有了集合

有人想有可以自动扩展的数组,所以有了List

有的人想有没有重复的数组,所以有了set

有人想有自动排序的组数,所以有了TreeSet,TreeList,Tree**

而几乎有有的集合都是基于数组来实现的.

因为集合是对数组做的封装,所以,数组永远比任何一个集合要快

  

但任何一个集合,比数组提供的功能要多

一：数组声明了它容纳的元素的类型，而集合不声明。这是由于集合以object形式来存储它们的元素。

二：一个数组实例具有固定的大小，不能伸缩。集合则可根据需要动态改变大小。

三：数组是一种可读/可写数据结构－－－没有办法创建一个只读数组。然而可以使用集合提供的ReadOnly方法，以只读方式来使用集合。该方法将返回一个集合的只读版本。




















## 4.1. 接口

https://www.zhihu.com/question/20111251/answer/14760353

接口的作用对于很多新手来说很不容易理解，我给大家举个例子。  
接口只是一个规范，所以里面的方法都是空的。  
假如我开了一个宠物粮店，声明所有宠物都可以来我这里买粮食，这就相当于一个接口，

```
public interface PetRestaurant {  
public void buy();  
}
```

当一只狗看到了，知道自己是宠物，所以它去实现这个接口  
```
public class DogPet implements PetRestaurant {  
@Override  
public void buy() {  
System.out.println("我是狗，我要买狗粮");  
}  
}  
```
当一只猫看到了，知道自己也是宠物，所以也去实现这个接口  
```
public class CatPet implements PetRestaurant {  
@Override  
public void buy() {  
System.out.println("我是猫，我要买猫粮");  
}

}  
```
当狗和猫来我的店之前，我是不知道他们到底是什么，但是当他们来到我的店，我就知道一个要猫粮食，一个要狗粮食。因为他们都实现了 我这个接口，都可以买。下面这个类相当于一个接待顾客的类，即店小二，他接待所有实现了我这个宠物店接口的动物，传进来一个PetRestaurant 类型的宠物，注意，这个PetRestaurant 是接口  
```
public class test {  
public void buy(PetRestaurant pet)  
{  
pet.buy();  
}  
}

```
好了，这个时候我这个老板出现了，我可以给他们卖粮食了，相当于测试类  
```
public class Tests {  
public static void main(String\[\] args) {  
PetRestaurant dog = new DogPet(); //实例化一个狗，相当于把狗顾客实例化  
PetRestaurant cat = new CatPet();//实例化一个猫，相当于把猫顾客实例化  
  
test t = new test(); //实例化一个店小二  
t.buy(cat); //把猫交给店小二  
t.buy(dog); //把狗交给店小二  
}

}  
```
这样运行的结果就是  
```
我是猫，我要买猫粮  
我是狗，我要买狗娘
```

你知道吗，整个过程我这个店主其实根本不知道来的到底是猫是狗还是其他什么，我只要有一个店小二，把这些来的不知什么动物都全部交给店小二，店小二就知道怎么去卖了，因为这些狗啊猫啊都实现了我这个宠物店的接口，而店小二就负责接待所有实现了我这个接口的动物。这就有一个好处，假如明天来了一头小猪，只要它实现了我这个接口，我只管交给店小二处理就OK了，我这个店小二根本不需要变化，我这个店主也只需要实例化一下这个动物就OK  
你想，假如没有接口，会怎么办，来一个猫，我要去创造一个猫，还要实例化，来一只狗，我要创建一只狗，同样要实例化，还要配备专门的店小二去接待，就会相当麻烦




大家需要统一标准。甚至有的编程语言（Object-C）已经不把接口叫 interface，直接叫 protocol。













https://zhuanlan.zhihu.com/p/31153642
接口的两种含义：一，Java接口，Java语言中存在的结构，有特定的语法和结构；二，一个类所具有的方法的特征集合，是一种逻辑上的抽象。前者叫做“Java接口”，后者叫做“接口”。
https://www.zhihu.com/question/48503724/answer/118893099
[  # Java中接口继承接口有什么实际意义？
编程](https://www.zhihu.com/people/s.invalid/creations/19554298) 话题的优秀回答者


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













## 4.2. 反射


https://zhuanlan.zhihu.com/p/24789506
https://zhuanlan.zhihu.com/p/29390534




















## 4.3. 多态

https://www.cnblogs.com/liuweiqiang11188/p/6677605.html
向上向下多态123







C++与java多态的区别 ？ - 二律背反的回答 - 知乎 https://www.zhihu.com/question/30064509/answer/64630337

面向对象和面向过程五子棋

https://blog.csdn.net/DreamLike_zzg/article/details/86749069

https://blog.csdn.net/lb565867230/article/details/45700185


mindhacks.cn/2008/06/13/why-is-quicksort-so-quick/










**泛型通配符**
https://www.ibm.com/developerworks/cn/java/j-jtp04298.html


[Java 泛型总结（一）：基本用法与类型擦除](https://segmentfault.com/a/1190000005179142)

https://segmentfault.com/a/1190000005179142

https://www.zhihu.com/question/58800149/answer/159649487

https://zhuanlan.zhihu.com/p/40925435
https://www.zhihu.com/question/33304378/answer/91877656

伪泛型

https://www.zhihu.com/question/19701421/answer/32361102
学习 Java 泛型有没有精华的材料、好的学习方法？

**  https://cn.bing.com/search?q=刚读了《Java编程思想》和《Java核心技术》两书的泛型章节，简单做了点笔记，仅供参考：+使用泛型编写的代码可以被不同类型的对象重用（核309，思352），泛型通过指定类型参数的方式来声明（核310）。+类型参数使程序具有更好的可读性和安全性（核310）。但类型参数不能是基本类型（核320，思400）。+泛型对集合类尤其有用（核309，思353），但不能创建参数化类型的数组，如List<Integer>%5B10%5D，应以List<List<Integer>>代替（核321）。+泛型类是具有一个或多个类型参数的类（核311，思353）。如List<T>。+泛型方法是具有类型参数的方法（核313，思361）。如<T>+T+getT(T...+t)。+泛型擦除指编译时擦除实际类型，替换为限定类型或Object（核316，思372），并在必要处自动强制转型为实际类型。这使一个类中的同名异参方法，如果参数是只有类型参数不同的同一个泛型类，则无法重载，如f(List<Integer>+l)+和+f(List<String>+l)。（核327，思403）+在泛型类方法体中不能使用new+T()的形式实例化变量（核323），在泛型类方法体中，无法获得具体类型信息，除非显式传入Class<T>。+在泛型类的静态上下文中不能使用T，如static+T+t，这是非法的（核325）。**


！！！！ https://zhuanlan.zhihu.com/p/62292650




https://www.zhihu.com/question/53697315/answer/136126893
## 4.4. 如何正确理解java中的泛型类型推导？

stackoverflow问题链接：

> [I am confused about function return generic in java?](https://link.zhihu.com/?target=http%3A//stackoverflow.com/questions/41176574/i-am-confused-about-function-return-generic-in-java)?

java中的泛型的具体类型都可以从什么地方推导出来？



## 4.5. 泛型中的通配符

**1\. 作用：**规定只允许某一部分类作为泛型；

**2\. 分类：**

1.  *无边界通配符(<?>)：*  
    　　无边界的通配符的主要作用就是让泛型能够接受未知类型的数据。
2.  *固定上边界通配符(<? extends E>):*  
    　　使用固定上边界的通配符的泛型, 就能够接受指定类及其子类类型的数据。  
    要声明使用该类通配符, 采用<? extends E>的形式, 这里的E就是该泛型的上边界. 注意: 这里虽然用的是extends关键字, 却不仅限于继承了父类E的子类, 也可以代指显现了接口E的类.
3.  *固定下边界通配符(<? super E>):*  
    　　使用固定下边界的通配符的泛型, 就能够接受指定类及其父类类型的数据。  
    要声明使用该类通配符, 采用<? super E>的形式, 这里的E就是该泛型的下边界.

> **注意:** 你可以为一个泛型指定上边界或下边界, 但是不能同时指定上下边界。





有人将上面的原则总结了一下，写作"in out"原则, 归纳起来就是:

-   in或者producer就是你要读取出数据以供随后使用(想象一下List的get), 这时使用extends关键字, 固定上边界的通配符. 你可以将该对象当做一个只读对象;
-   out或者consumer就是你要将已有的数据写入对象(想象一下List的add), 这时使用super关键字, 固定下边界的通配符. 你可以将该对象当做一个只能写入的对象;
-   当你希望in或producer的数据能够使用Object类中的方法访问时, 使用无边界通配符;
-   当你需要一个既能读又能写的对象时, 就不要使用通配符了.


https://blog.csdn.net/s10461/article/details/53941091/









































































































