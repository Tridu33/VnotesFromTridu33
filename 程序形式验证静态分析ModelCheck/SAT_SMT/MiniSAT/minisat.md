
首先，各人的背景、需求不同，这种问题很难有大而全的回答。。下面只针对“深刻理解求解原理，跟进一些最新成果“，给一点小建议。。。

说明一下，这里不考虑3-SAT，＃SAT，MaxSAT，"SMT-opt"(SMT + 最优化）, "SMT-ind"（SMT with inducetive pred)，"SMT-CLP"(SMT + constraint logic programming)等变种/扩展。。

SAT：当前最主流、成功的架构是CDCL（Conflicit-Driven Lemma-Learning)，之所以说“架构“，是因为它本质上还是基于DPLL(Davis-Putnan-Logemann-Loveland)算法，只是加了一些lemma learning, restarting, phase selection等策略，和很多简化算法（如hidden tautology elimination, bloked clause elimination)。个人建议是好好花时间阅读、理解Minisat的代码。当前相当大一部分SAT引擎都是基于Minisat的。

SMT：

SMT求解器可能包涵各种theory如real, integer, bit-vector,等等。为了求解不同theory，可能涉及特定算法如线性规划、高斯消元等；但是这些thery的求解基本都有会SAT solver参与。
SAT solver是怎么参与的呢？大体分为“lazy approach“和“eager approach"两类（此处略去 xx 字）..如果想通过动手实现加深理解，对于“lazy aproach“，简单点的可以考虑EUF(theory of equality with uninterpreted function)或DL(difference arithmetic)...

如何学习 SMT/SAT（可满足性理论）的数学基础？ - rainoftime的回答 - 知乎
https://www.zhihu.com/question/65438076/answer/233925406










总览历代知名的基于DPLL算法的SAT求解器，回溯的依据无外乎以下三种：

冲突分析（回溯到引起冲突的决策变量的最小决策深度）

子句记录（将引起冲突的子句的矛盾变量记录下来，同时取非，做析取式，成为学习到的子句，因此该过程也称之为子句的学习）
通过检测文字进行布尔约束传播（BCP）。

我们称以上风格的SAT solver为矛盾驱动式SAT求解器。

泛泛而谈，这些求解器总的来说有三个特点：

表现形式：无论是怎样的算法，sat solver总需要一个精心设计的数据结构来解决。

推理论证：暴力搜索从来不是解决问题的最好的方法，一个良好的求解器需要具有一个成体系的机制来从当前形势推理计算和前/后向传播挖掘或学习到的知识（比如，冲突子句，回溯深度）。

搜索求解：推理往往与搜索相辅相成，适当的遍历也可以从中挖掘出有用的信息（这一定程度上是依赖于搜索的策略，比如选择决策变元的策略）。


学习子句约束是在把布尔函数转换为CNf 的时候要额外添加的约束向量么


miniSAT求解器(updating) - Eigenvalue的文章 - 知乎
https://zhuanlan.zhihu.com/p/103679514

怎么把布尔函数转换成cnf范式，而后用miniSAT求解啊？或者miniSAT可以直接对布尔函数求解吗?


把表达式里的文字用数字表示?比如aΛbΛ-a可以表示为1Λ2Λ－1，负数字(序号)表示文字的取反

就是比如说我有x+y＝0这种，x和y是取0或者1。然后怎么转化为cnf范式，因为我的等式比较大，拿手推比较困难

可以为每个文字创建一个节点吧，表示约束式的时候用节点在某种数据结构(比如数组)里的索引来表示，比如x用1表示，y用2表示，以后但凡约束里出现x就转换为1，出现-x就转换为－1，同理-y就是2，就变成cnf范式了吧













# 1. minisat

minisat-user-gude-cnf.txt

```
p cnf 5 3
1 -5 4 0
-1 5 3 4 0
-3 -4 0
```

(x1 | -x5 | x4)&(-x1 |  x5 | x3 | x4)&(-x3 | -x4)

```
p$ ./minisat minisat-user-gude-cnf.txt minisat-user-gude-outputSAT.txt
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |       3        9 |       1       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 0              (-nan /sec)
decisions             : 6              (inf /sec)
propagations          : 5              (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0 s

SATISFIABLE
```


```
SAT
-1 -2 -3 -4 -5 0
```



# 2. 第二个解

追加第一个解的负形：

```
1 2 3 4 5 0
```

然后运行命令行，得到第二个解答：

```
-1 2 -3 -4 -5 0
```







































































