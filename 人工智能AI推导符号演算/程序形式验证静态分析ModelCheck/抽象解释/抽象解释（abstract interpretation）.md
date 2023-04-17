
http://janmidtgaard.dk/aiws15/
抽象解释国外课程

https://www.di.ens.fr/~cousot/AI/
很全的抽象解释online电子书


http://cea.ceaj.org/CN/abstract/abstract19639.shtml
《抽象解释理论框架及其应用》



Abstract Interpretation: Past, Present, and Future, LICS 14的invited paperConstructive design of a hierarchy of semantics of a transition system by abstract interpretation, TCS 02

作者：rainoftime
链接：https://www.zhihu.com/question/27789493/answer/89839656
















如何理解抽象解释（abstract interpretation）？ - 陈炜的回答 - 知乎
https://www.zhihu.com/question/27789493/answer/38107549


CMU的PL专家Robert Harper在一篇文章里说计算里分两个流派, 一是逻辑学家, 另一类是组合学家. 逻辑学家告诉你什么是合理的世界, 组合学家教你怎样去建造世界. 这么说:
Fritz Henglein recently pointed out to me that the world of theoretical Computer Science is divided into two camps, which I’ll call the logicians (who are concerned with languages and semantics) and the combinatorialists (who are concerned with algorithms and complexity). The logicians love to prove that programs work properly, the combinatorialists love to count how many steps a program takes to run. Yet, curiously, the logicians hate the Booleans, and love abstractions such as trees or streams, whereas the combinatorialists love bits, and hate abstraction! (Or so it often seems; allow me my rhetorical devices.)
抽象解释算是告诉你这么一个世界观: 分析程序, 不要死磕在最底层的具体的细节上, 要在更高的视野上去思考. 传统的解释器知道每个变量最具体的值, 是1, 是2, 还是false. 每个变量的值域就是它原始的值, 姑且称之为具体值域(concrete domain). 这种解释器其实就是具体解释器(concrete interpreter). 所以抽象解释之所以有这个名字就是因为每个变量的值域不是原始的值, 而是一个更高阶的抽象值域(abstract domain). 如果你写好了一个传统的解释器, 迁移到抽象解释器, 差不多就是写一个函数把具体值域映射到抽象值域. 当然你还要适当地修改一下解释器处理抽象值的代码, 也就是语义(semantics), 如之前传统的解释器里1+1返回2, 但是对于做类型推导的抽象解释器看到的是int+int返回的是int.

但是怎么样设计这个抽象值域以及对应语义函数, 抽象解释不管这个, 人家只是告诉你需要这么些东西.

当你辛辛苦苦想出了这些, 抽象解释又跳出来, 哒哒, 你的抽象值域满不满足Galois Connection呀? 你的语义函数是不是单调函数哇?

......

所以知道抽象解释为啥叫这个名字, 也没啥用. 真正要应用它, 就得撸起袖管, 拿起笔分析程序.

1. 资料
1. CMU的Soonho Kong博士写过一个很好看的PPT, 介绍了抽象解释的那些理论的东西.
2. AIWS15的PPT 讲得也不错。





基于抽象解释理论的程序验证技术
http://www.jos.org.cn/1000-9825/19/17.pdf





>“e purpose of abstraction is not to be vague,  but to create a new semantic level in which  one can be absolutely precise.”- Edsger W. Dijkstra



# 1. 抽象解释（abstract interpretation）








如何理解抽象解释（abstract interpretation）？ - 甜品专家的回答 - 知乎
https://www.zhihu.com/question/27789493/answer/38090669

抽象解释就是用来计算程序某些属性的静态分析。但是呢一个程序完全可以有无数种具体的运行时状态（可以理解为变量的值的组合），静态不可能穷举完，不然就变成动态分析了。这时候就要取舍了。

抽象解释牺牲精度换取时间。它将程序某些具体值（concrete value，不一定是变量的值）概括成一个抽象值（abstract value），这样有些语句只用遍历有限次就可以概括它所有运行时的…呃，这个具体属性。一个sound（不知道怎么翻译…）的抽象解释可以把所有具体值可以映射到一个相应的抽象值，但反过来却不行，反过来只能把抽象值映射成相应的具体值的集合，最后抽象解释的结果是抽象值，丢失了精度。但仍然能正确地总结出程序的某些属性。

最经典又简单的例子就是把无限的整数的具体值抽象成正、负、0这三个有限的抽象值。网上随便找个抽象解释的课件都有这个例子

------------------------------------------------------------------------------------------

科普 - 程序验证（9）- 区间分析 - FRONTIERS的文章 - 知乎
https://zhuanlan.zhihu.com/p/325018769

以上符号分析的过程，实际上可以抽象为一个更一般的算法框架。 我们称之为抽象解释（Abstract Interpretation）框架。 目前，大部分的静态分析方法都基于抽象解释框架。 抽象解释的数学基础是格论（Lattice Theory），在此不做过多引入。 有兴趣的读者可以自行查阅Abstract Interpretation相关资料，一般都有介绍。


在抽象解释框架中，先需要定义抽象域（Abstract Domain）。 抽象域标定了我们分析的范围，即仅对抽象域上的元素，也称抽象状态(Abstract State），进行操作。 符号分析的抽象域为[公式]。 而区间抽象的抽象域为区间（Interval），在此我们统一定为[公式]这种形式的闭区间。 我们使用[]表示空区间，使用[B,T]作为区间[公式]的别名。 区间抽象域中，任意一个区间都是一个抽象状态。

接下来，我们需要定义针对我们所验证的程序语言（C语言子集）的抽象后继（Abstraction Successor）算子。 抽象后继算子规定了，如何计算当前抽象状态在经过某一种程序中的操作后，所得到的后继抽象状态。 符号分析中我们所规定的取值变化映射就是其对应的抽象后继算子。 在区间分析中，我们需要引入新的抽象后继算子。



区间分析在抽象解释框架下的全部基本要素，即**抽象域，抽象后继算子，以及状态合并算子**。


事实上，不只是静态分析算法，很多程序验证算法，也都基于抽象解释框架，比较著名的就是谓词抽象算法。 使用谓词抽象算法的程序验证工具ASTREE，曾成功验证了空客系列飞机的主飞控软件。 这些软件规模较大，基本都在10万行C语言代码以上。 抽象解释框架自在1978年由Cousot提出后，40多年来蓬勃发展，在软件分析领域具有不可替代的地位。 Cousot也因此成为软件分析领域，最有希望获得图灵奖的人。






-----------------------------------










近年来，抽象解释的主要研究进展包括提高分析精度、可扩展性、可行性3 方面。

在提高分析精度方面，抽象域本身表达能力的局限性是当前面临的主要问题。为了 弥补抽象域表达能力的局限性，最近的研究进展可分为两类：（1 ) 通过结合符号化方法 来提高分析精度，利用SMT求解器[347’342]、插值[334]等技术来计算程序语句迁移函数的 最佳抽象，以改进抽象域在语句迁移函数上的精度损失；（2 ) 提高抽象域的非线性表达 能力，如基于组合递推分析[345 3461将符号化分析与抽象解释结合起来了以生成多项式、 指数、对数等形式非线性不变式，基于椭圆幂集来生成二次不变式[323]等。另外，在面 向特定应用改进精度方面，最近有研究[326]针对实际计算机程序，尤其是嵌人式系统中 数值都是有限二进制位数表示的问题，提出了改进策略来提高基于抽象域的分析的精度。

在提高可扩展性方面，如何有效降低存储开销和提高计算效率是目前考虑的主要问 题。在这方面，近年来的研究进展包括：

1 ) 利用变量访问的局部性原理，降低当前抽象环境中所涉及的变量维数，并根据数 据流依赖的稀疏性，降低抽象状态的存储开销和传播开销。基于该思想，〇h等人[35M55] 提出了一种通用的全局稀疏分析框架，在不损失分析精度的前提下能够显著降低时空开 销，并在商业化静态分析工具Sparrow上进行了应用，取得了显著的可扩展性提升效果。

2 ) 利用矩阵分解等在线分解优化策略来对抽象域操作的实现算法进行优化。基于该 思想，最近Singh等人对实际静态分析工具中常用的八边形抽象域的实现进行了优化，优 化后八边形分析的性能提升达140多倍[359];对多面体抽象域的实现进行了优化，优化后 多面体分析的性能提升了 2 ~5个数量级，并且很多原有实现分析不出来的规模较大的实 例采用优化后的方法能够分析出来[36°];在此基础上，Smgh等人还提出了一种通用的基 于分解的优化策略[361]，能够在不改变基抽象域的基础上自动实现分解的优化，从而不 需要人工重新实现基抽象域，并基于这一思想实现了开源抽象域库ELINA。这种基于在 线分解的方法在提高抽象域的分析效率时不会造成精度损失。最近，Singh等人[362]还提 出了一种基于强化学习来加速静态程序分析的方法，在每次迭代中，利用强化学习来决 策选哪个转换子，以在精度和不动点迭代收敛速度之间进行权衡。在抽象域编码实现上， Beech:等人[32M25]最近改进了未必封闭多面体域（支持严格不等式约束）的双重描述法， 在表示中避免了松弛变量的引人，极大地提高了分析效率，并在原有广泛使用的多面体 抽象域实现库PPL的基础上开发了新的开源实现PPLite。为了提高形态分析的分析效率， U等人[343]提出一种方法对程序的抽象状态做二次抽象以合并相似的抽象状态，从而降 低形态分析中析取抽象状态数，提高了分析效率。

在提高可行性方面，复杂数据结构自动分析的支持、不同谱系目标程序的支持、活 性性质分析的支持是目前主要的关注点。在复杂数据结构的自动分析方面，最近的研究 重点关注针对数组内容的精确分析[348]、混杂数据结构的建模[344]、数值与形态混合的程 序分析[33°’337]、关系型形态分析[34°]。在支持不同谱系目标程序方面，最近的研究重点关 注多线程程序的自动分析[349]、中断驱动型程序的自动分析[365366’363]、概率程序的分 析[327]、操作系统代码的安全和功能性分析[356,344]、JavaScript等动态语言的分析[458]。在 目标性质支持方面，近年来在抽象解释领域出现了一些新的用来分析时序性质和终止性 的方法[351-352]

以抽象解释为代表的程序分析工具近年来也得到了长足发展。相关工具不断涌现，出现了PolySpacel4801、Astreele1l、aiT WCET Analyzerl4821、CodeHawk[48l、Sparrow's8]、Zoncolan（Facebook）、Julia[451等商业化工具和Frama-C Value Analysisl46l、cccheck
（Code Contract Statie Checker）[4871、Interprocl4881，erab-lIlyml48l、IKoS[9ol、MemCADf4911、Fluctua[421、Jandom[498l、JsCFA[494]、MuJSla1等学术界工具。Mine等人基于Astree开发了面向异步实时程序的扩展版本AstreeA，以支持多线程C程序中运行时错误、数据竞
争、死锁等错误的检测，并成功分析了ARINC653航空应用（约220万行代码）[525526]。