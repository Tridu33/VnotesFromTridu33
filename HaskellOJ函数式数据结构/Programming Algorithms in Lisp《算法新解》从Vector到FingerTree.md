

scheme自学套装：

SICP，EOPL，LiSP，

动手写解释器，开脑洞各种玩，加入first class closure、continuation、hygienic macro，顺手扩展一下语言，写个类型推导器，还可以加个module和object system，在自己实现的scheme上面写一个类似miniKanren的逻辑式DSL，然后再编译成C之类的其他语言，又或者写个虚拟机编译成字节码。


# Programming_Algorithms_In_Lisp开源初稿_-_Vsevolod_Domkin.pdf
本文作者 Vesvolod Dyomkin 正在写一本关于算法和 Lisp 的书。事实上，这件事在几年前就开始了，但这几年来，Vesvolod Dyomkin 一直断断续续地写作，很难抽出大段时间，而且写作时间不多，也没有每天坚持在写。但现在，Vesvolod Dyomkin 终于可以开始出版这本书了。Vesvolod Dyomkin 打算这样做先把这本书的章节发布到博客，然后汇总起来在 Learnpub 上发布最终版：Vesvolod Dyomkin 希望这本书能够在第一批读者的评论下得到改进和润色。本书将使用 CC BY-NC-ND 许可（创作公用许可协议），供公众免费阅读。
https://www.oreilly.com/start-trial/
vseloved.github.io/progalgs.html 就是一本书
https://vseloved.github.io 作者主页
本书将有 16 章，分为 3 个部分：基本数据结构、衍生数据结构和高级算法。Vesvolod Dyomkin 计划大约每周发布一次，争取在今年底前全部发完。https://www.infoq.cn/article/iL2GNgREII_Cv0fpkK2Y
[Programming_Algorithms_In_Lisp开源初稿_-_Vsevolod_Domkin.pdf](file:///C:/Users/tridu33/Desktop/Programming_Algorithms_In_Lisp开源初稿_-_Vsevolod_Domkin.pdf)

在计算机科学领域，Lisp 开创了许多先驱概念，包括：树结构、自动存储器管理、动态类型、条件表达式、高端函数、递归、自主（self-hosting）编译器、**读取﹣求值﹣输出循环**（英语：Read-Eval-Print Loop，REPL）

programming algorithms in lisp pdf
https://github.com/Apress/programming-algorithms-lisp 随书源码

https://github.com/aimacode/aima-lisp
https://github.com/tomwalker/algorithms-lisp
https://www.infoq.cn/article/owJvbjUigBTzjPHKMPVa 链表类算法题

https://github.com/thinkphp/lisp-training lisp算法题
vseloved.github.io/progalgs.html

**leetcodewars用racket**

https://www.ruanyifeng.com/blog/2010/10/why_lisp_is_superior.html
# 《算法新解》从Vector到FingerTree
算法新解Haskell也是lisp
https://github.com/liuxinyu95/AlgoXY 《算法新解》

# 组合式lisp程序应用的自动推理
https://github.com/bmitc/the-little-schemer
最近看了一本书，the little schemer。里面有很多例子，我觉得完全可以丰富为我们论文的程序综合，自动编程实现组合式应用的搜索例子。

pddl给lisp的七个基本操作语义化描述，形式化为五法十戒，然后用我们的fond solver求解可以得到“满足题目形式化输入输出io的lisp组合式程序”。

正如dijstra说的，组合式应用是唯一的编程方法。

类似列表出发生成set集合等，我们可以有包括形式化皮亚诺算术加法，邱奇数从functor,monad等代数结构通用数学规律出发，构造满足数学代数公理体系的逻辑自动推理系统。用来求解“基于邱奇数的算术题型自动搜索求解步骤”，这何尝不是一种公理化后的代数几何吴方法，类似的prolog自动求解搜索答案。

除了上述基础算法题型推导构造，我们fond solver优势在于DSL。给定形式化的复杂度很高的函数io形式化为pddl，然后基于这些高度封装的函数作为原子函数，进行可组合应用的搜索，生成用lisp自动写算法题满足题目io的pddl要求，然后就是想要的了。

难点在于避免递归搜索出现死循环，结果导向a*搜索，快速决策planning出比较合适的方案，
解决循环最简单的方法是我python中全部set记录下来避免重复，但是太憨憨
目的导向，prolog回溯结果导向反向走迷宫，可能是搜索最快的。


http://alumni.media.mit.edu/~jorkin/goap.html
读研做STRIPS的时候遇到过这个GOAP,其实就是纯符号逻辑出发的人工智能在unity游戏AI规划中的应用https://www.lfzxb.top/goal-oriented-action-planning-chinese-document/

问题是递归函数声明的pddl要怎么描述，他只能做qnp那种单调的，所以foldl,foldr的递归函数每次都是单调的。问题是有些单调函数不明显，排序整体无序性质在一些算法中是单调的，但是有些希尔排序什么的本身无序

排序本身需要定义皮亚诺算术(程序代码即数据)，然后才有序关系的定义，接着才有less的比较大小的关系，才能在此基础上定义排序和交换移位。
lisp写冒泡排序

https://blog.csdn.net/zssrxt/article/details/102754988 lisp八大排序算法


-----------------------

## Read-Eval-Print Loop

有时候除了纯函数的lambda演算推理“组合式函数应用app”，我们还需要关心javier 论文中类似scip中env魔法,the little scheme提到的env的闭包中局部变量作用域，

副作用的函数推理需要一个全局变量集env，然后开始定义作用的io规范的pddl，形如
<env',i',o'>=func(<env,i,o>)，然后开始做定理证明和验证推理



