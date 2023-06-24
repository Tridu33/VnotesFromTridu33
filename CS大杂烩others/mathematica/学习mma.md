# 1. 学习mma
{{SeeWikipedia}}

Mathematica是由英国科学家斯蒂芬·沃尔夫勒姆领导的沃尔夫勒姆研究公司（位于美国伊利诺伊州香槟市）开发的一款广泛使用的科学计算软件，它拥有强大的数值计算和符号运算能力。

==Wolfram==
Wolfram 语言 是用于 Mathematica 的编程语言。

受其影响的语言有：[[Julia]]

==数据集==
Mathematica囊括了大量可立即计算的数据。用户可以通过编程访问这些数据，并且也可以通过Wolfram Research的数据服务器自动更新数据。某些数据如股票价格和天气数据都是实时递送的。目前数据集包括：
* 天文数据：155,000个天体的99个属性
* 化学数据：34,000个化合物的111个属性，118个化学元素的86个属性以及1000个亚原子粒子的35个属性
* 地缘政治数据：237个国家的225个属性，以及全世界160,000个城市的14个属性
* 金融数据：186,000个股票和金融工具的历史和实时属性
* 数学数据：187种多面体的89个属性，3000种图的258个属性，6种knots的63个属性，21种晶格结构的37个属性，52个测地学方案的32个属性
* 语言数据：149,000个英语单词的37个属性。26个其他语言的词典
* 生物医学数据：所有40,000个人类基因的41个数据，27,000类蛋白质的30个属性
* 天气数据：全球17,000个气象站的43个实时和历史的测量数据
* Wolfram|Alpha数据：来自[http://www.wolframalpha.com/ Wolfram Alpha]的亿万兆数据

==文档==
*[http://docs.huihoo.com/cufp/2013/Programming-MapReduce-in-Mathematica.pdf Programming MapReduce in Mathematica]

==链接==
*[https://www.wolfram.com/mathematica/ Mathematica官网]
*[https://www.wolfram.com/language/11/improved-machine-learning/ Mathematica 11 增强的机器学习] [https://reference.wolfram.com/language/guide/MachineLearning.html Wolfram 语言之机器学习]
*[http://www.wolframalpha.com/ Wolfram Alpha 是微软的必应和苹果公司的Siri后台所使用的问答系统之一] Wolfram Alpha 第一版是用约一千五百万行的 Mathematica 代码编写的（使用 webMathematica 和 gridMathematica），并且在 10,000 个（为了系统发行的需要，这个数字被升级过）CPU 上运行。
*[http://mathematica.stackexchange.com/a/4456/11992 A list of open-source implementations of the Wolfram language]
*[http://www.gamasutra.com/view/news/212709/The_Wolfram_Language_will_soon_be_integrated_into_Unity Wolfram语言将集成在Unity游戏引擎中。]

[[category:mathematics]]
[[category:numerical analysis]]
[[category:computational science]]
[[category:qt]]












作者：asdasd1dsadsa  
链接：https://www.zhihu.com/question/346321384/answer/935774435  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

知乎上实际上已有许多相关讨论，且有高手参与。这里就不多说Wolfram Language的语言水平了，毕竟我自己也没有什么水平。

但是Wolfram语言内置功能的强大以及上手之容易似乎反而使得大量用户忽视了其作为编程语言的完备性，低估、总是低估它在各种通用问题上的实力。这里我*随心所欲*地设些问来帮助各位区分自己是否入门：

Level1：懂一点基本的语法知识以及基本的操作。可能会自己造一堆轮子，但至少造得出来。

1.  核心概念：什么是表达式？什么是头部？什么是运算符？会不会用广义运算符（f@,~f~,//f）？什么是符号？什么是值？属性是什么？
2.  结构操作：教程里的列表操作函数会用多少了？知道用基本的规则与替换吗？字符串的基本操作和输入转义会吗？怎么在列表、规则、字符串、一般表达式之间转换？Prepend和PrependTo区别在哪？
3.  函数：如何自定义一个函数？有哪些方法？怎么把函数作用于表达式的内部？递归怎么写？
4.  控制（这个范围我设的有点广）：除了Table还会几种迭代？With、Block、Module分得清吗？Return返回到哪一层？
5.  其他内置符号体系：逻辑运算、逻辑判断函数熟悉了吗？Equal和SameQ区别在哪？除了Blank模式你还知道用哪些模式？
6.  数学（不过，数学说到底功夫在语言本身之外）：数和数值有啥区别？公式化简除了Simplify还会啥？各数值计算功能的选项有会用的吗？微分方程会设边界条件吗？绘图功能都熟悉没？绘图选项会调吗？

Level2：各主要模块的帮助文档涉及的基本都会了，写码基本畅快，瓶颈在数学

1.  核心概念：计算顺序是怎么算的？常用运算符的优先级结合性都记得吗？什么是上下文？上值、下值是什么？常见属性的作用懂了吗？
2.  结构操作：Tutorial里出现过的表达式结构操作、列表结构操作都会了吗？
3.  函数：Tutorial里的都会了吗？怎么（尽可能简单地）把Thread返回的结果变回去？
4.  控制：Accumulate相当于FoldList什么？Hold,Evaluate,Inactive系列大概会用一点了吗？$RecursionLimit这样普遍有效的控制参数知道几个？
5.  其他内置符号体系：子表达式序列匹配和子字符串匹配的匹配策略有什么根本不同？Interpreter的参数知道几个？Dynamic系列了解吗？Graph会用吗？
6.  数学：Simplify、NDSolve等数学函数是如何运作的？机器精度和任意精度下的数值计算有何区别？

Level3：堆功底了，需要钻研。对各模块的了解融会贯通（尤其是在编程中能够应用更多的数学），还hack了一些底层的玩意儿。

如何写面向对象范式的代码？SparseArray这样的内置对象有很多是很有用的，你会用多少了？像Dispatch这样的原子表达式呢？

Names\["System`*"\]里面的会多少？Names\["Developer`*"\]乃至Names\["Internal`*"\]呢？

这个那个究竟谁效率高（乃至语言核心函数的底层机制）？Compile支持哪些内置符号（乃至LibraryLink、WSTP）？ToBoxes和MakeBoxes区别是什么（框符）？

程序包怎么写？这不只是说要会用BeginPackage，而是说要知道如何为用户创建服务，mma用户往往不是专业程序设计出身，缺乏系统的服务设计思想（呃，说的其实是我自己）。这其中的细节比如：如何处理各种各样的用户输入、选项；设计一个默认的、“Automatic”计算策略（而不是全部要求用户自己指定）……

不太冷门、接近语言核心的程序包有多少是你所熟悉的？要知道，许多你常用的功能原本是在一个程序包中的，后来才合并到System`上下文中，要想要完全掌握相关内容，你应当了解该程序包本身。比如：你可能经常用到StringTemplate，但你可能没接触过Templating`；你可能熟悉Cell和Notebook表达式，但你可能不了解FrontEnd`的具体细节。

***

有必要一提的是，为了钻研，你往往必须学会：

1.  读程序包源码。可以使用GeneralUtilities`PrintDefinitions。
2.  将单元还原为单元表达式来看。可以使用Ctrl+Shift+E（Windows）。
3.  直接追踪计算过程。可以使用Trace。

当然，以上做法对核函数都无能为力。夸张一点的话，你可以尝试反编译某些dll，不过这应该算是违法破解了，测试测试就得了。






















如何学习和使用Mathematica？ - asdasd1dsadsa的回答 - 知乎 https://www.zhihu.com/question/346321384/answer/935774435
















**一些网址：**

**知乎：[https://www.zhihu.com/question/55683496](https://www.zhihu.com/question/55683496)**

  

博客的前后文也值得一看：

**博客，关于张量运算的程序包：[http://blog.csdn.net/stereohomology/article/details/16848805](https://link.zhihu.com/?target=http%3A//blog.csdn.net/stereohomology/article/details/16848805)**

  

**博客，关于mathematica编写自定义程序包的模板：[http://blog.sina.com.cn/s/blog_5701c6010100npyy.html](https://link.zhihu.com/?target=http%3A//blog.sina.com.cn/s/blog_5701c6010100npyy.html)**

**[http://blog.csdn.net/gw569453350game/article/details/48731673](https://link.zhihu.com/?target=http%3A//blog.csdn.net/gw569453350game/article/details/48731673)**

  
  
作者：李豪豪  
链接：https://www.zhihu.com/question/346321384/answer/826260054  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
























