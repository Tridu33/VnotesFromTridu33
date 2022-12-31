https://en.wikipedia.org/wiki/Datalog

Datalog初步理解
https://note.youdao.com/ynoteshare1/index.html?id=270970f9e5d6f35babba3d022b436fc8&type=note#/

## 1.1. 应用场景

知识补全：通过推理补充图谱中还未存在的关系(边)

一致性检查：新录入的知识与已有知识的冲突检查

## 1.2. Prolog

Prolog语言是以一阶谓词逻辑为理论基础的逻辑程序设计语言，是人工智能程序设计语言族中应用最为广泛的的一种。

Prolog的基本语句有三种：事实 规则 目标

- 事实 用来说明一个问题中已知的对象和它们之间的关系，如 妻子(姚明,叶莉) 表示 姚明 的妻子是 叶莉
- 规则 用来描述事实之间的依赖关系，如 bird(x) :- animal(x),has(x,feather) 表示 凡是动物且有羽毛那么它是鸟
- 目标 向prolog询问的问题就是程序运行的目标，如 ?- student(bill) 表示 bill是学生吗？

## 1.3. DataLog

Datalog是一种基于逻辑的编程语言。它是一阶谓词逻辑中Horn子句逻辑的一种受限形式，只允许变量或常量作为谓词的自变元，不允许函数作为谓词的自变元。Datalog的语句由事实和规则组成，同Prolog一样，它可以实现对知识库的演绎推理，即可以从已知事实中根据跟着推理得到新的事实。

Datalog是Prolog的一种适应于知识库的改进形式语言，是一种受限的Prolog语言

一条DataLog规则由三部分组成：

- 规则头,是关系原子(比如 student(x) )
- 蕴含符号 :- （可以读为if，蕴含表明的是一种逻辑关系，而不是一种运算符号）
- 规则体，即一个或多个子目标P1,P2,…,Pn，子目标可以是关系原子或算数原子(算数结果是布尔值,如 a>10 )，各子目标之间相当于AND连接。规则的含义描述为：检查规则中变量的所有可能的取值，当这些变量使规则体中所有子目标均为真时，规则头为真。

举例：P :- P1,P2,…,Pn //若P1,P2,…Pn均为真，则P为真

![img](https://private-alipayobjects.alipay.com/alipay-rmsdeploy-image/skylark/png/2d687835-86a6-4a1a-b936-d7f171edf572.png)

## 1.4. DataLog规则表示的基本运算

### 1.4.1. 交

Q(x1，x2，⋯ ，xn) :- R(x1，x2，⋯， ) , S(x1，X2，⋯ ，xn)

举例:智能手机(x) :- 手机(x),智能设备(x)

### 1.4.2. 并

两个关系的并要用两个规则来构造

Q(x1,x2,..,xn) :- R(x1,x2,...,xn)

Q(x1,x2,..,xn) :- S(x1,x2,...,xn)

### 1.4.3. 差

Q(x1，x2，⋯，xn) :- R(x1，x2，⋯，xn) , NOT S(x1，X2，⋯ ，xn)

举例：弟弟(X,Y):- 兄弟(X,Y) ,NOT 哥哥(X,Y)

### 1.4.4. 选择

 Q(x1，x2，⋯，xn) :- R(x1，x2，⋯，xn), x>10

举例：哥哥(X,Y) :- 弟弟(Y,X),性别(Y,a),a='男'

### 1.4.5. 投影

 Q(x1，x2，x3) :- R(x1，x2，⋯,xn)

举例：memberOf(X,Y) :- member(Y,X)

### 1.4.6. 乘积

P(a,b,c,x,y,z) :- R(a,b,c), S(x,y,z)

### 1.4.7. 连接

P(a,b,c) :- R(a,b),S(b,c)

举例：岳父(X,Z) :- 妻子(X,Y), 父亲(Y,Z)

## 1.5. Datalog推理

(1) 规则：岳父(X,Z) :- 妻子(X,Y), 父亲(Y,Z)

(2) 事实：妻子(姚明，叶莉)

(3) 事实: 父亲(叶莉，叶大)

(4) 推理：岳父(姚明,Z) :- 妻子(姚明,叶莉), 父亲(叶莉,Z) 由 (1) (2)

(5) 推理：岳父(姚明,叶大) :- 妻子(姚明,叶莉), 父亲(叶莉,叶大) 由 (4) (3)

最终得到事实：岳父(姚明,叶大)

## 1.6. Datalog优缺点

优点

- 简单容易学习
- 克服Prolog语言的缺点：表示方法不够规范，不宜在计算机中使用和处理；
- 适合于处理具有大容量的数据和知识；
- 可以改善递归查询算法。

缺点

• 不带有函数，建模能力差，描述现实世界中的一些复杂问题存在困难



















# 2. Datalog-逻辑编程语言Prolog的子集





https://www.zhihu.com/topic/20002624/hot
Topic





为什么prolog/datalog使用一阶逻辑而不是高阶逻辑？ - LdBeth的回答 - 知乎
https://www.zhihu.com/question/61293085/answer/716459837


Prolog 的出现是 1972 年，System U 的 inconsistency 同年由 Jean-Yves Girard 刚证出來，Higher Order Logic 的 inference rule 都沒完善，很明显不可能把这应用的这么快，自然是用已经成熟的 sound and complete 的 first order logic。不过 Prolog 也不是一成不變的，如楼下所说 ISO Prolog 現在也有 call/N 做 higher order programming。Prolog style 的 higher order logic programming, 或者 higher order style 的 Prolog，是 1982 年 HiLog 实現的。至于怎么解決这个 Paradox 嘛，就有了后來的 intuitionistic type theory of Martin-Löf。










编译原理不就是Datalog嘛 - bhuztez的文章 - 知乎
https://zhuanlan.zhihu.com/p/19945892
编译原理里很多很多东西确实就是Datalog能自然的表示的东西。
Dataflow analysis和Pointer analysis都是这类。事实上很多库/工具就是用Datalog做前端的，像是bddbddb和Doop

























