# 阅读FF planner论文的引言



# 学习如何介绍研究现状

-------------------------------------------------------

## 范例FF planner 文章中的引言部分是这样写的：

综述未来发展方向

FF was the most successful automatic planner in 2001 planning competion.

- 主流的研究方法there are mainly three new approaches in plan generation.

不同的分类一：

1. GRAPHPLAN system; In fact, unlike the state-space graph in which a plan is a path through the graph, in a Planning Graph a plan is essentially a flow in the network flow sense.  Planning Graphs are closer in spirit to the Problem Space Graphs (PSGs) of Etzioni。使用图论方法解决问题  much faster than any other technique known at this time. 2001。
2. planning as satisficability method。translate planning to propositional satisfiability使用命题推理系统的知识解决问题
3. heuristic-search planing.   from *HSP: Heuristic search planne*r松弛问题启发式 to *FF planner*(搜索技术是an enforced form of hill-climbing, combining local and systematic search+剪枝）.

分类二：

1. 经典求解是generic problem solving methods, developed following some theoretical concept, and tested on examples from the literature afterwards.

2. In our approach, exploring the idea of heuristic search, there is no such clear distinction between development and testing.

实验benchmark：

 benchmark examples from the Biocfesworid，Grid，Gripper, Logistics，Mjsteiy, Mprime，and Tireworiddomains.

实验结论：

In almost all of the existing benchmark domains, a non-optimal plan can, in principle, be generated in polynomial time

Using the benchmarks for inspiration during development, we have been able to come up with a heuristic method that is not provably efficient, but does work well empirically on a large class of planning tasks

全文结构简述：

FF 架构

STRIPS简述

核心启发式+搜索技术+剪枝手段

扩展ADL domain问题

larify the performance differences between F F  and HSP，区分适用场景，测试哪种情况下谁更有效。

outlines 总结

-----------------

## 引言如何介绍研究现状

- 综述别人是怎么做的，主流的研究方法是什么？

阐述相关研究的主要方法，常见现有paper的主流ideas,相关ideas发展情况和动机。

- 按照不同的方法对已有工作分类实验比较对比多种方案的优缺点，

1. 最优先分类方法是：从直觉性解决问题的“motion”的角度进行区分

   同一个问题，有人用归结到图论相关知识求解；有的人归结到命题推理系统求解；有的人使用启发式搜索解空间的一个案例。强调有些求解方法动机出发点相同，但是又有所改进或者不同着力点，就像 from *HSP to *FF 。重点是每种发展分支要先写“开山之作论文”怎么做的，然后就是现在这条分支进展到什么程度。

2. 其次就是high-level;地分类。

   因为前面分类是可能会过分细致专注与细节，这些方法可能因为论文不同有所不同，但是要找出来一些宏观的分类方案来看这些求解方案的区别。比如文章中分成两类：

   (1)纯理论方法推导，实践只是为了验证

   (2)实例学习，泛化解法齐头并进。

3. 我觉得很多时候high-level分类可以从这些角度分类：

   (1)理论分析，local 解找到某一个policy的求解策略。

   (2)精确全局解找到很多个的solution方案；

   (3)数据学习，实例处理，概率方案



- 实验结论新方法是怎么做的，有什么好处不足。

benchmark实例上跑。

- 全文段落分布简述,方法介绍，最后的conclusion最精炼。

不能光强调自己的方案好的地方，缺点适用范围要写明。如果实验中的确不如现有某些方案的地方也要坦白说清楚。

要做实验区分适用场景，测试哪种情况下谁更有效。

如果是现有方向的改进，或者相同出发点不同着力点，要重点区分自己的工作改进了什么具体的方向。







--------------------

阅读体会之研究现状的介绍方法：
先给出总的结论，肯定已有工作对领域的贡献，选择特定的角度对现有工作进行类别划分；
然后逐次介绍各个类别的代表工作，使用简洁的语言介绍这些代表工作的主要贡献；
总结现有工作仍然存在的不足（可以是现有工作没有关注到的问题，可以是方法上的缺陷，也可以是实验上的不足），作为自己文章所研究的动机；
