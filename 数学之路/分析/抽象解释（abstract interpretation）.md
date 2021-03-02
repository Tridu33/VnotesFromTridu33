

https://www.zhihu.com/question/27789493/answer/38107549
# 如何理解抽象解释（abstract interpretation）？



作者：陈炜  
链接：https://www.zhihu.com/question/27789493/answer/38107549  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

CMU的PL专家Robert Harper在[一篇文章](https://link.zhihu.com/?target=https%3A//existentialtype.wordpress.com/2011/03/15/boolean-blindness/)里说计算里分两个流派, 一是逻辑学家, 另一类是组合学家. 逻辑学家告诉你什么是合理的世界, 组合学家教你怎样去建造世界. 这么说:

> Fritz Henglein recently pointed out to me that the world of theoretical Computer Science is divided into two camps, which I’ll call the logicians (who are concerned with languages and semantics) and the combinatorialists (who are concerned with algorithms and complexity). The logicians love to prove that programs work properly, the combinatorialists love to count how many steps a program takes to run. Yet, curiously, the logicians hate the Booleans, and love abstractions such as trees or streams, whereas the combinatorialists love bits, and hate abstraction! (Or so it often seems; allow me my rhetorical devices.)  

抽象解释算是告诉你这么一个世界观: 分析程序, 不要死磕在最底层的具体的细节上, 要在更高的视野上去思考. 传统的解释器知道每个变量最具体的值, 是1, 是2, 还是false. 每个变量的值域就是它原始的值, 姑且称之为具体值域(concrete domain). 这种解释器其实就是具体解释器(concrete interpreter). 所以抽象解释之所以有这个名字就是因为每个变量的值域不是原始的值, 而是一个更高阶的抽象值域(abstract domain). 如果你写好了一个传统的解释器, 迁移到抽象解释器, 差不多就是写一个函数把具体值域映射到抽象值域. 当然你还要适当地修改一下解释器处理抽象值的代码, 也就是语义(semantics), 如之前传统的解释器里1+1返回2, 但是对于做类型推导的抽象解释器看到的是int+int返回的是int.

但是怎么样设计这个抽象值域以及对应语义函数, 抽象解释不管这个, 人家只是告诉你需要这么些东西.

当你辛辛苦苦想出了这些, 抽象解释又跳出来, 哒哒, 你的抽象值域满不满足Galois Connection呀? 你的语义函数是不是单调函数哇?

......

所以知道抽象解释为啥叫这个名字, 也没啥用. 真正要应用它, 就得撸起袖管, 拿起笔分析程序.


\# 资料  
1\. CMU的Soonho Kong博士写过一个很好看的[PPT](https://link.zhihu.com/?target=http%3A//www.cs.cmu.edu/~soonhok/talks/20111109.pdf), 介绍了抽象解释的那些理论的东西.  
2\. AIWS15的[PPT](https://link.zhihu.com/?target=http%3A//janmidtgaard.dk/aiws15/) 讲得也不错。



[http://www.di.ens.fr/~cousot/AI/](https://link.zhihu.com/?target=http%3A//www.di.ens.fr/~cousot/AI/)

两篇安利神文，先洗洗脑。。  
Abstract Interpretation: Past, Present, and Future, LICS 14的invited paper  
Constructive design of a hierarchy of semantics of a transition system by abstract interpretation, TCS 02

  
  
作者：rainoftime  
链接：https://www.zhihu.com/question/27789493/answer/89839656  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


抽象解释就是用来计算程序某些属性的静态分析。但是呢一个程序完全可以有无数种具体的运行时状态（可以理解为变量的值的组合），静态不可能穷举完，不然就变成动态分析了。这时候就要取舍了。

抽象解释牺牲精度换取时间。它将程序某些具体值（concrete value，不一定是变量的值）概括成一个抽象值（abstract value），这样有些语句只用遍历有限次就可以概括它所有运行时的…呃，这个具体属性。一个sound（不知道怎么翻译…）的抽象解释可以把所有具体值可以映射到一个相应的抽象值，但反过来却不行，反过来只能把抽象值映射成相应的具体值的集合，最后抽象解释的结果是抽象值，丢失了精度。但仍然能正确地总结出程序的某些属性。

最经典又简单的例子就是把无限的整数的具体值抽象成正、负、0这三个有限的抽象值。网上随便找个抽象解释的课件都有这个例子。

  
  
作者：甜品专家  
链接：https://www.zhihu.com/question/27789493/answer/38090669  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
















































































































