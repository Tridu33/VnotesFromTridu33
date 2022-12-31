# 1. 约束编程Constraint programming

http://ibmdecisionoptimization.github.io/docplex-doc/cp.html

约束编程技术用于查找调度和组合优化问题的解决方案。与基于数字线性代数的数学编程相反，它主要基于计算机科学基础，例如逻辑编程和图论。

当处理许多现实世界中的排序和调度问题的复杂性时，约束编程是无价的。

无论当前的问题是调度人员，机器还是流程作业，当决策变量，活动和资源之间存在复杂的逻辑和算术关系时，都需要进行约束编程。约束编程模型以声明方式表示，通过使用必须最小化或最大化的决策变量，约束和目标，如数学编程一样。IBM®ILOG®CPLEX®Optimizer的CP Optimizer功能中可以实现按词典分类的多标准目标。

例如，约束编程可以用作启发式算法，以找到混合整数程序的解。

约束编程首先通过使用逻辑，图论，算术和其他参数来减少满足所有约束的决策变量的可能值集。当无法推断出决策变量域中的某些值时，此信息将通过约束传播，也许可以进行进一步的推断。在将值分配给每个决策变量之前（即找到解决方案之前），还使用了各种搜索策略。找到第一个解决方案后，搜索将继续查找具有更好目标值的其他解决方案。

使用CP Optimizer进行调度的主要好处是不需要枚举时间，即时间段或时间段。因此，无论描述调度问题的相关时间标度是毫秒，分钟还是小时，都可以有效地制定和求解模型。





In constraint programming, a problem is viewed as a series of limitations on what could possibly be a valid solution. This paradigm can be applied to effectively solve a group of problems that can be translated to variables and constraints or represented as a mathematic equation. In this way, it is related to the Constraint Satisfaction Problem (CSP)

https://opensource.com/article/19/9/constraint-programming-example

## 1.1. 约束求解器s

http://www.constraint.org/en/tools/ 超强网站

视频教程
https://www.coursera.org/lecture/solving-algorithms-discrete-optimization/3-1-1-constraint-programming-solvers-LSXuK


https://www.sciencedirect.com/topics/computer-science/constraint-solver


https://developers.google.com/optimization/cp
## 1.2. meeting

https://hal.archives-ouvertes.fr/hal-00754042

组合优化问题的约束程序设计中AI和OR技术集成的国际会议（CPAIOR'12）



发布时间： 2021年2月5日
MINICP：用于约束编程的轻量级求解器 https://link.springer.com/article/10.1007/s12532-020-00190-7
迷你CP 还附带全套练习，单元测试和开发项目。


逻辑编程为约束编程的摇篮[ 1，2，3 ]社群是在80年代中期。现在，它已用于许多商业应用程序中，主要用于调度，路由和时间表设置领域，并且通常通过诸如逻辑Benders分解和列生成之类的分解技术与数学编程混合使用。它由多个商业求解器（例如，CP Optimizer，一种IBM产品）和许多开源求解器支持。在[ 4 ]中可以找到有关CP Optimizer的调度应用程序的有趣综述。



SeaPearl：以强化学习为指导的约束编程求解器 https://arxiv.org/abs/2102.09193

最近的工作表明，强化学习可以成功地用于驱动约束编程（CP）求解器的搜索阶段。但是，也已经显示出这种混合方法很难构建，因为标准CP框架本身并不包含机器学习机制，从而导致效率低下的某些原因。本文介绍了SeaPearl的概念证明，SeaPearl是在Julia中实现的新CP求解器，它支持机器学习例程，以便使用强化学习来学习分支决策。还提供了对学习组件进行建模的支持。我们在两个问题上说明了此新求解器的建模和解决方案性能。尽管尚未与工业求解器竞争，



## 1.3. 二进制编程


来自贝尔实验室的野望

二进制判定程序是由一串两个地址的条件转移指令组成的程序。本文显示了开关电路和二进制决策程序之间的关系，并给出了一组简单的规则，通过这些规则，人们可以将二进制决策程序转换为开关电路。然后表明，在交换函数的计算方面，二进制决策编程表示优于通常的布尔表示。

https://www.researchgate.net/publication/238747248_Representation_of_Switching_Circuits_by_Binary-Decision_Programs
































