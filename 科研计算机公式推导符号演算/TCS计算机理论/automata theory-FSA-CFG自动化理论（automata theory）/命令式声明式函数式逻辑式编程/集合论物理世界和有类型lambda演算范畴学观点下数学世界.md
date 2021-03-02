

Curry-Howard同构反映了推理系统和程序语言之间的相似性，或表示了计算机程序与数理逻辑之间的直接联系


Curry-Howard同构
chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/file:///C:/Users/HUMAN/Desktop/lambda%E6%BC%94%E7%AE%97.pdf

•人们在研究形式逻辑的证明系统和程序语言的类型系统时发现的一个“巧合”

•两者的所有规律是同构的

Curry-Howard同构

•程序语言（演算）与逻辑系统之间的对应

•简单类型λ演算对应着（最小）命题逻辑

•依赖类型对应着一阶谓词逻辑

•SystemF（加了多态后的λ演算）对应于二阶（构造）逻辑


Curry-Howard同构

•类型即命题

•程序即证明

•Curry-Howard同构是基于构造主义逻辑的

•基于Curry-Howard同构的证明辅助助手：Coq，Agda，Idris等


https://hopl.info/showperson.prx?PeopleID=643 



Scott Dana (1964) Scott Dana "Outline of a mathematical theory of computation"  E A
      in Proc. (1970) Proc. 4th Ann. Princeton Conf. on Information Sciences and Systems (1970)  E

Scott, Dana and Strachey, Christopher (1966) Scott, Dana and Strachey, Christopher "Toward a mathematical semantics for computer languages"  E A
      in Proc. (1971) Proc. Symp. on Computers and Automata vol. 21 (1971)  E

Scott, Dana; (1969) Scott, Dana; "A Type-Theoretical Alternative to CUCH, ISWIM, OWHY", Oxford U 1969.  E A
      in Proc. (1971) Proc. Symp. on Computers and Automata vol. 21 (1971)  E

Scott, Dana (1971) Scott, Dana "Outline of a Mathematical Theory of Computation", TM PRG-2, PRG, Oxford U, 1971.  E A Page at OUP Abstract
      in Proc. (1971) Proc. Symp. on Computers and Automata vol. 21 (1971)  E

Scott, D., (1976) Scott, D., "Data Types as Lattices", SIAM J.Comput 5, pp.523-587, (1976).  E A
      in Proc. (1971) Proc. Symp. on Computers and Automata vol. 21 (1971)  E

Scott, Dana (2000) Scott, Dana "Some Reflections on Strachey and His Work"  E A
      in (2000) Higher-Order and Symbolic Computation April 2000 Volume 13 Issue 1-2  E


# 1. 集合论物理世界和有类型lambda演算范畴学观点下数学世界



https://b23.tv/EtPmxG  本期课程是由X-Order Lab主办的CuteNoise系列课程之理论计算机基础(一)，给大家带来集合论和Lambda演算的讲解，将由X-Order Lab研究员周缅来博士主讲。周缅来，荷兰亚原子物理国家研究所博士后。
关于X-Order Lab：
X-Order Lab成立于2018年，致力于成为世界顶尖的计算智能与经济实验室。X-Order Lab在专注于机器学习、计算经济学、算法设计等方面研究的同时，也会对学科内最前沿的研究成果进行传播，并发起了一系列学术交流活动“CuteNoise”。
lambda演算 本次课程PPT下载链接为：
链接：https://pan.baidu.com/s/1IbzPzR-h_a1vZu5wgID4Rw 
提取码：j3ss​




在20世纪70年代与英国计算机科学家克里斯托弗·斯特雷奇打下的数学（或指称）语义的基础，计算机编程语言。这项工作的结果导致斯科特（Scott）引入了领域理论，特别是提供了λ微积分或lambda微积分（1936年由美国逻辑学家阿隆佐·丘奇（Alonzo Church）发明的正式数学逻辑系统）的数学模型。相关理论。斯科特（Scott）是第一位首席编辑《计算机科学中的逻辑方法》（Logical Methods in Computer Science），创建于2005年的在线开放获取期刊。


<TOWARD A MATHEMATICAL  SEMANTICS FOR  COMPUTER LANGUAGES

指称语义，又称数学语义：给lambda项提供功能“意义”，即在某个数学论域里对应于某个数学对象。•如果把所有lambda项的集合定义为X，那么必须要有X->X的函数的集合属于X，违背了集合论的基数性质

**无类型lambda演算**的指称语义难以构造

1969 DanaScott hristopher Strachey 1969年DanaScott和ChristopherStrachey取得了突破，构造了lambda演算的模型，把lambda项所需要的X->X对象限制为X到X的连续函数上（在特定的Scott拓扑下）

因此，递归（最小不动点）和数据类型（整型，数组，列表）都有了“含义”

•两人因此获得了图灵奖


**有类型的lambda演算**

•类型理论（TypeTheory）

•有类型的λ演算更接近于实际的有类型编程语言

•λ演算里的类型对应于编程语言里的类型系统

类型理论（TypeTheory）•原始类型a,b,c,...•扩展类型a->b,b->c,...•如果x为类型a，M为类型b，则λx.M具有类型a->b•如果M为类型a->b，N为类型a，则(MN)具有类型b






































































## 1.1. ADT

https://computersciencewiki.org/index.php/Abstract_data_structures



在计算机科学中，抽象数据类型（ADT）是一种数据类型的数学模型，其中数据类型是从数据用户的角度通过其行为（语义）定义的，特别是在可能的值，可能的方面此类数据的操作，以及这些操作的行为。这与数据结构形成对比，数据结构是数据的具体表示形式，是实现者而不是用户的观点。

形式上，ADT可以定义为“一类对象，其逻辑行为由一组值和一组操作定义”；这类似于数学中的代数结构。“行为”的含义因作者而异，行为的形式规范的两种主要类型是公理规范（代数）规范和抽象模型。这些分别对应于抽象机器的公理语义和操作语义。一些作者还包括时间（用于计算操作）和空间（用于表示值）方面的计算复杂性（“成本”）。[2]

我们使用抽象结构的原因是因为它们根据存储在其中的数据的设计有效地使用了内存。使用大量数据或频繁更改数据时，数据结构可能会极大地影响计算机程序的效率（运行时间）。

用更通用的语言来说，抽象数据结构只是我们已构建为有序排列的某种数据排列。

静态和动态数据结构
数组
二维数组
堆
队列
链表
树
二叉树
馆藏
递归


这其实是软件层面的一种现有知识库**打包，封装，a higher level of abstract**，提供简单调用的接口，用来进一步开发程序，制作框架，系统编程。










# 2. 打通ADT语义真实世界---范畴学 数学对象 理论世界

https://wk.baidu.com/view/99c45d20647d27284b735152?pcf=2&bfetype=new
结构化定理英文？
任意正规程序都能函数等价于一个基集合{序列,if-then-else,while-do}产生的结构化程序。


19世纪的数学家克罗内克(Leopold Kronecker)提出了一个著名观点：

    God created the natural numbers, and all else is the work of man.


http://blog.sciencenet.cn/blog-2349385-1262980.html
科学思想的元语言 集合论

http://blog.sciencenet.cn/blog-2349385-1241376.html
离散数学是什么

集合论的哲学认知 系列——读《Naive Set Theory》：空集和无序对公理 http://blog.sciencenet.cn/blog-2349385-1027996.html



集合论语言符号手册，要基于“集合论模型构造世界万物”


「集合」的出现不是作为被研究的数学对象，而是作为定义、描述其它数学对象的语言。在这个意义上集合语言，就是数学的母语。因此，不仅仅是学习离散数学，学习所有数学的基础就在于学会用集合语言定义、描述、解释其它数学对象。所谓的「数学思维」、「数学思想者」，其中一个重要因素就是熟练使用集合语言表达数学定义，并可以从定义、公理出发证明定理。


Dijkstar的最弱前条件技术<啊discipline of program>: wp（pre,effect)
https://wk.baidu.com/view/0fc3f8f74693daef5ef73d68?pcf=2&bfetype=new


指称语义/数学与语义：

给定项提供功能“意义”，即在某个数学论语中对应某个数学对象



指称语义:数学语义，给lambda项提供功能意义，即在某个数学论语里对应某个数学对象

指称语义 下的 ADT 数据结构们=范畴学，抽象规律世界，数学对象=转换为 命令式编程语言的数据结构和算法，真实世界


https://en.m.wikipedia.org/wiki/Structured_program_theorem
Böhm–Jacopini theorem
《B方法》裘宗燕译第九章:递归操作定义为 非递归抽象 的一种精化。


https://computersciencewiki.org/index.php/Abstract_data_structures
语义指称，从语义学角度 如何提取规矩，找到
具体问题到数学规矩的映射一般规律？例如hanoi递归到二进制数

数学 范畴学 观点理解下 的数据结构
看刘新宇 《算大新解》haskell部分对应

看ADT

how to describe data structure in math language

元学习，如何数学语言，人为构造性出发，来定义数据结构和算法的 纯数学描述，基于集合论模型出发



张淞讲hanoi,递归 zipper-《算法新解》中数据结构对比 函数式 命令式

haskell logic逻辑推理包  while to for  递归怎么办 表格驱动算法生成case 语句 for while  do等价转换递归  

？自动机data structure automatas 需要生成递归语句吗？

结构化定理 。

递归自动生成里面，不能做吗？汉诺塔怎么算？难道要手工栈递归转循环吗？ 

栈匹配lisp s-expression括号代表的 层次结构。为什么 llvm webassembly用的是s-expression，查《深入浅出》 汉诺塔迭代版本，

>logic角度来看：

**情景演算**汉诺塔求解案例，能不能学习出 递归算法。

数学推理**数学对象**，自动定理证明 coq 能不能提炼出 递归算法

https://www.zhihu.com/question/446059671 提了个知乎问题





# 3. B方法形式化

教学资源汇总 https://www.labri.fr/perso/sutre/Teaching/B/

还有 裘宗燕主页教学 https://www.math.pku.edu.cn/teachers/qiuzy/fm_B/

https://en.wikipedia.org/wiki/B-Method


the B-book Assigning programs to Meaning《B方法》裘宗燕译P416
(在抽象机操作的上下文中的)递归不是规范相关概念，而是程序设计相关概念:
一个通过递归定义的操作体现的是某个更抽象的，以非递归方法定义的规范所描述的最终计算过程。

Event-B

Atelier B软件 B方法free软件源码？可能人家公司 https://www.clearsy.com/ 没公布，有很多手册文档，也需要看paper

代码生成手册
chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.clearsy.com/wp-content/uploads/sites/3/ressources/DOC/english/translators-user-manual.pdf
https://sourceforge.net/p/atelierbgu




i/wiki/Home/ 图形化用户界面源码 该项目包含Atelier B图形界面源代码。Atelier B是基于B语言的CASE工具，允许开发经过数学证明的默认免费软件。 svn checkout https://svn.code.sf.net/p/atelierbgui/code/trunk atelierbgui-code

> 通过人机界面以QT格式使用Atelier B，或者直接使用命令（命令模式）使用
https://www.atelierb.eu/en/atelier-b-tools/






Atelier B是多用户。在项目开发过程中可以自动执行的任务如下：
–组件的语法验证
–自动产生证明义务
–将B安装自动翻译为C或Ada语言

>自动精炼
集成了自动优化工具（BART）。BART使用可以由用户扩展的细化规则库来实现细化和实现。BART以优化规则为基础。可以添加其他细化规则，以对某些组件进行细化个性化

语法分析仪
这些用于执行B语言文件的所有语法验证：
>模型编辑器已集成到Atelier B中。这集成了语法分析器，自动完成功能以及整个模型的导航功能。
>类型检查器首先对B组件进行语法验证，然后进行一定数量的上下文验证，包括类型控制和标识符范围控制。组件必须经过类型检查器才能通过验证，并且在进行下面的任何其他验证之前
> B0检查器执行特定于安装中使用的BO语言（B语言的子类）的验证，以确保它们可以被翻译。
项目检查器检查项目的所有组件以控制其体系结构（组件之间的链接）。在项目的最终翻译之前，必须先检查项目。

B模型可以pdf，rtf和LaTeX格式保存。

>自动翻译器
这些安装构成了B语言开发的编码阶段。它们是使用B语言子组件编写的，类似于命令式编程语言。为了便于在任何目标系统上生成代码，将安装程序自动翻译为标准编程语言。然后可以将获得的程序编译并组装到目标计算机上，以生成可执行软件。



>项目的图形表示
通过自动在图形上放置它们，将其用于项目组件及其链接的图形表示。用户可以选择不同的显示选项，例如要查看的链接类型，项目的整个依赖图或组件的依赖图的视图。

>证明工具
–使用B语言的组件自动生成证明义务 –证明
其证明义务时B组件是正确的
–在自动模式下进行证明：大多数证明义务在没有用户干预
的情况下进行了证明-在交互模式下使用证明时自动模式失败：用户使用交互命令（引证添加，案例证明等）指导证明者进行证明义务证明
–谓词证明者：谓词证明：证明用户添加的规则
–查看Poof义务，他们的证明义务来源及其状态（琐碎，已证明，未证明）
–已验证规则库的管理，包括2 200多个规则





>项目管理
工作室B提供大型项目管理服务（例如，包括500个组件）。特别是：
–网​​络中的多个用户使用的工作室B。这些用户可以同时处理同一个项目
-归档和还原整个项目
-构建项目或几个子项目或库。这样，Atelier B可以使多个开发人员团队进行大型模块化开发
–通过为每个组件提供其状态（传递给Type Checker，转换为C或Ada），证明数量来查看项目的整体状态。义务和证明的百分比
–自动生成项目组件之间的依赖关系。这样，为了对选定的组件执行操作（通过类型检查器，通过证明义务生成器等），工作室B报告其所依赖的组件所需的操作。



https://github.com/CLEARSY/apero










《B方法》第三章数学对象
基于集合论模型，构造了data structure指称语义数学对象:

ADT自然数，整数，有穷序列，有穷树，标记树，二叉树，良构关系(不动点递归循环相互转换等价性,wp(pre,effect)最弱前条件技术)上定义递归…
想知道linked list相关的抽象机(范畴学 数学对象指称语义)应该怎么样定义？ 要找到范畴学上定义 https://gist.github.com/akoskovacs/5074344

https://cn.bing.com/search?q=linked+list+haskell&qs=n&form=QBRE&pc=U316&sp=-1&pq=linked+list+haskell&sc=4-19&sk=&cvid=B03726E44B2D49E89E10F0FF5FC23A70

张淞书上Zipper表示列表间游走，拉锁；树结构等价的linear tree 前序遍历需要三种操作，包括游历到左右分支，返回上一级。








《b方法》两个模型p204(一个集合对应一个关系，集合变换器)沟通了“广义代换的逻辑世界，物理”和集合论的“数学世界，范畴学物理对象”p258

应该还要有一个“递归22循环转换器”


































































