# 1. 用证明助理来验证“真实世界”的 C 程序





PLDI 2021有什么值得关注的文章？ - 朱俸民的回答 - 知乎
https://www.zhihu.com/question/447986918/answer/1771054197


广告一下贵组的工作：RefinedC (A Foundational Refinement Type System for C) **用证明助理来验证“真实世界”的 C 程序（直接在源码上加标注）正确性的一个框架**，有一定的自动化策略（叫做 Lithium），框架构建基于 Coq-Iris。有个 OCaml 的前端自动为 C 程序生成用 Coq 描述的属性。

我前段时间试着用它证明了基于数组的快速排序的”完整“性质（主要工作量都是在Coq上面）：Fengmin Zhu / RefinedC-QuickSort
p.s. 我之前参考过一个 Dafny 对于快速排序的验证。遗憾地是，那个证明里面没有关于 Permutation 性质的证明（即排序后的数组是排序前数组的一个排列）。或许这个性质用裸一阶逻辑会比较难表达？

作为一个学术工具，RefinedC 的实现有很多很”黑“的地方，离能给”人“用还有一点的距离。但是这个项目一直会进行下去（起码这几年），工具也会越来越完善。




鉴于C在系统软件中继续扮演着重要角色，并且难以编写安全且正确的C代码，因此开发有效的形式化方法来验证C程序仍然是一个巨大的挑战。在本文中，我们提出了一种解决该问题的新方法：一种称为RefinedC的类型系统，该系统将所有权类型（用于共享状态和并发的模块化推理）与细化类型（用于对C数据类型和Hoare风格的精确不变式进行编码）相结合C函数规范）。

RefinedC是自动化的（需要最少的用户干预）和基础的（在Coq中产生程序正确性的证明），同时还处理了一系列的低级编程习惯用法，例如指针算法。尤其是，遵循RustBelt的方法，通过对基于Coq的Iris框架进行解释以实现高阶并发分离逻辑，在语义上证明了RefinedC类型系统的健全性。但是，RefinedC的键入规则也被设计为可以用一种称为“锂”的新“分隔逻辑编程”语言进行编码。通过限制为精心选择（但仍然具有表达力）的分离逻辑片段，Lithium支持可预测的，自动的，目标导向的证明搜索没有回溯。我们在一系列C代码的代表性示例中证明了RefinedC的有效性。


https://plv.mpi-sws.org/refinedc/  

https://gitlab.mpi-sws.org/iris/refinedc



























