





# DISTILL-dsPlanner




>  Examples are REPLICA (Garc ́ıa-Dur ́an et al., ress) which extractsa set of prototypes from the instances or DISTILL (Winner and Veloso, 2003) which builds a highlycompressed instances library by generalizing and merging solution plans
> .  DISTILL  (Winner  and  Veloso,  2003)  incorporates  exampleplans into a structure calleddsPlanner.  DISTILL  converts the plan into a parameterized if-statementand  searches  through  each  of  the  if-statements  already  stored  in  thedsPlannerto  merge  them.  If  thelearneddsPlanneris  accurate  it  can  be  used  directly  to  solve  any  problem  from  the  domain  withoutsearch

researchgate.net/publication/2945471_DISTILL_Learning_domain-specific_planners_by_example

Winner, E. and Veloso, M. (2003).  DISTILL: Towards learning domain-specific planners by example.  InInternational Conference on Machine Learning, ICML’03
DISTILL：通过示例学习特定领域的计划者

一个与领域无关的计划的有趣替代方法是提供示例计划，以演示如何解决特定领域中的问题并使用该信息来学习特定领域的计划者。其他人使用示例计划进行基于案例的计划，但是不可避免的大型案例库的检索和调整机制引起了人们关注的效率问题。在本文中，我们介绍dsPlanners或自动生成的特定于领域的计划器。我们介绍了DISTILL算法，用于从示例计划中自动学习dsPlanner。DISTILL将计划转换为dsPlanner，然后将其与以前学习的dsPlanners合并。我们的结果表明，由DISTILL自动学习的dsPlanners紧凑地代表了其特定于领域的计划经验。此外，dsPlanner会根据情况概括给定的示例计划，从而使他们能够有效解决以前未遇到的问题。最后，我们提出了DISTILL程序，该程序可以自动从示例计划中获取单步循环，从而将从小问题中获得的经验应用于解决任意大问题。

LoopDISTILL：从示例计划中学习特定于循环域的计划者   researchgate.net/publication/266864770_LoopDISTILL_Learning_Looping_Domain-Specific_Planners_from_Example_Plans
许多大型计划问题都表现出循环结构，这转化为昂贵的重复问题解决工作，导致许多通用计划制定者无法扩大规模。相反，特定领域的计划者可以通过推理特定领域的特性（例如重复结构）来提高效率。尽管手写此类特定于领域的计划者可能会遇到挑战，但给出具有重复结构的具体问题的示例计划非常简单。在这项工作中，我们介绍了LoopDISTILL算法，用于从示例计划中自动获取特定于域的计划程序。LoopDISTILL在示例计划中标识重复的结构，然后将循环计划转换为特定于域的计划器或dsPlanner。循环dsPlanners能够将从解决方案中获得的经验应用于小的示例问题，以解决任意大的问题。我们证明，自动学习的dsPlanners能够更有效地解决大规模问题，并且能够解决比通用计划员可以解决的数量级大许多数量级的问题。


































