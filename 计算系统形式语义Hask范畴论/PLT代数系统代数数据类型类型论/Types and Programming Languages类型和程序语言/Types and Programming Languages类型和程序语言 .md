#  类型和编程语言tapl



https://www.cis.upenn.edu/~bcpierce/tapl/ 随书官方网站 课程


- CIS 500, Software Foundations 

  https://www.seas.upenn.edu/~cis500/current/index.html

  University of Pennsylvania. First-year graduate course, required for all computer science MSE and PhD students.

  The 2007 offering of the course is completely formalized in Coq, but doesn't cover as much of TAPL as earlier offerings.

- [CS101, Programming Languages ](http://www.cs.caltech.edu/~jyh/classes/cs101/index.html), Cal Tech. Introductory undergraduate/graduate level course, with a bias toward interpreting type systems using intuitionistic logic.

- A [course at Katholieke Universiteit Leuven](http://www.cs.kuleuven.be/~frank/FST/index.htm) based on TAPL but with examples in Scala.



Rust
https://github.com/lazear/types-and-programming-languages

Ocaml



https://github.com/dannywillems/types-and-programming-languages-pierce-implementation



C++实现



https://github.com/KareemErgawy-TomTom/types-and-programming-languages







Haskell implementations of programming languages from Pierce's Types and Programming Languages

https://github.com/bartfrenk/types-and-programming-languages


































# Types and Programming Languages 



编程语言的设计原理
https://xiongyingfei.github.io/DPPL/2021/main.htm

新兴的程序设计语言层出不穷，这些语言是如何设计出来的？ 主流语言中不断扩展出新的高级语言特征，这些特征是如何定义的？ 为什么说Java语言的设计是有缺陷的？面向对象、函数语言、泛型编程等新型编程模型是否有共通的理论基础？ 本课程将揭示这些问题的答案。

近十多年来，编程语言的发展呈现两个趋势：1）从固定少量语言到大量领域特定语言的变化； 2）从简单语言到复杂高级语言。比如，在2013年9月的TIOBE的编程语言排行榜上， C和Java两个占统治地位的语言只能各自占到16%左右的份额， 大量的份额被近年来涌现的新型编程语言比如Javascript, Scala, Erlang, R占据。 同时，更多的新语言还在不断被设计出来。另一方面，大量经典语言也不断扩展， 引入各种高级语言成分。比如Java起初的设计目标为一个简化版的语言， 但最新的Java 8设计中已经包含了泛型、函数式编程、动态性等多种高级特性。在这样的情况下， 掌握设计新的编程语言的能力，已经不仅限前沿科研人员所掌握的高级技能，而是一线软件开发工程师的基本要求 。同时，对语言设计原理的了解和掌握，也有助于更好的理解高级语言中的各种新特性，以更好的使用主流编程语言。

为指导编程语言的设计，研究人员们已经提出了一系列的原理和方法，其中最核心的就是类型理论。 类型声明是现代语言中避免编程错误的一个基本手段，而类型理论解释了一个良好的类型系统应该具有的特征和复杂类型的定义方法。 本课程将围绕类型理论这个核心进行组织，讲授程序设计语言的现代理论。

本课程具有两个特点：1. 严谨性：课程中的概念元素都将有严格的数学定义，可以进行形式演绎和归纳， 而非空泛的概念介绍。2. 操作性：课程中的所有重要概念都将通过课程作业的方式编程实现，使得同学们在动手过程中真正掌握知识。希望通过本课程的学习，使得同学们在编程语言领域拥有扎实的理论功底和实践能力，在产业方面能胜任设计新语言的任务，在学术方面为开展程序语言相关研究打下基础。


参考书目
Types and Programming Languages , Benjamin C. Pierce, The MIT Press, 2002. (教材)

类型和程序语言





## 课程讲义和作业

| 课程日期  | 讲师     | 课程章节和讲义                                               | 作业                                                         |
| --------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 2021/3/10 | 熊英飞   | [Introduction](https://xiongyingfei.github.io/DPPL/2021/xiong_courseOverview_ch1.pdf) [Untyped Systems](https://xiongyingfei.github.io/DPPL/2021/xiong_ch3.pdf) | 作业1：安装使用OCaml; 3.5.16                                 |
| 2021/3/17 | 赵海燕   | [OCaml Overview](https://xiongyingfei.github.io/DPPL/2021/zhao_OCaml_Overview.pdf) | 作业2：（见胶片最后一页） 阅读第4章，熟悉arith包中的代码， 并在test.f中编写一些表达式进行测试 |
| 2021/3/24 | 熊英飞   | [The Untyped Lambda Calculus](https://xiongyingfei.github.io/DPPL/2021/xiong_ch5.pdf) [Nameless Representation of Terms](https://xiongyingfei.github.io/DPPL/2021/xiong_ch6.pdf) | 作业3：5.3.6; 6.2.5                                          |
| 2021/3/31 | 熊英飞   | [Typed Arithmetic Expression](https://xiongyingfei.github.io/DPPL/2021/xiong_ch8.pdf) [Simply Typed Lambda Calculus](https://xiongyingfei.github.io/DPPL/2021/xiong_ch9.pdf) [Simply Extensions](https://xiongyingfei.github.io/DPPL/2021/xiong_ch11.pdf) [课程项目](https://xiongyingfei.github.io/DPPL/2021/xiong_project.pdf) | 作业4：8.3.7; 9.3.9; 11.11.1                                 |
| 2021/4/7  | 赵海燕   | [Reference](https://xiongyingfei.github.io/DPPL/2021/zhao_ch13_reference.pdf) | 作业5：13.4.1; 13.5.8                                        |
| 2021/4/14 | 熊英飞   | [In-Class Practice](https://xiongyingfei.github.io/DPPL/2021/xiong_practice_public.pdf) | 作业6：上交随堂练习，见胶片最后一页                          |
| 2021/4/21 | 赵海燕   | [Exception](https://xiongyingfei.github.io/DPPL/2021/zhao_ch14.pdf) [Subtyping](https://xiongyingfei.github.io/DPPL/2021/zhao_ch15-p1.pdf) | 作业7：14.3.1; 15.2.2; 15.3.2; 15.3.6                        |
| 2021/4/28 | 各位同学 | 开题报告和期中测验                                           | 无                                                           |
| 2021/5/5  | 赵海燕   | [Metatheory of Subtyping](https://xiongyingfei.github.io/DPPL/2021/zhao_ch16.pdf) | 作业8：16.1.2; 16.2.6; 16.4.1                                |
| 2021/5/12 | 胡振江   | [Case Study: Imperative Objects](https://xiongyingfei.github.io/DPPL/2021/hu_ch18.pdf) [Case Study: Featherweight Java](https://xiongyingfei.github.io/DPPL/2021/hu_ch19.pdf) | 作业9：18.11.1                                               |
| 2021/5/19 | 赵海燕   | [In-Class Practice](https://xiongyingfei.github.io/DPPL/2021/zhao_ch18-19-Practice.pptx) | 作业10：17.3.1; 17.3.3; 18.7.1; 19.4.3;（可选）19.5.5        |
| 2021/5/26 | 胡振江   | [Recursive Types](https://xiongyingfei.github.io/DPPL/2021/hu_ch20.pdf) [Metatheory of Recursive Types](https://xiongyingfei.github.io/DPPL/2021/hu_ch21.pdf) | 作业11：见两张胶片最后一页                                   |
| 2021/6/2  | 胡振江   | [Type Reconstruction](https://xiongyingfei.github.io/DPPL/2021/hu_ch22.pdf) [Universal Types](https://xiongyingfei.github.io/DPPL/2021/hu_ch23.pdf) | 作业12：22.5.5; 23.5.1; 23.5.2                               |
| 2021/6/9  | 胡振江   | [Existential Types](https://xiongyingfei.github.io/DPPL/2021/hu_ch24.pdf) | 无                                                           |











