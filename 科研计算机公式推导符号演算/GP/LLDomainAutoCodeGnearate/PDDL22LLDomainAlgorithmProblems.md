# PDDL22LLDomainAlgorithmProblems




The interest of general solvers is rooted in the origins of Artificial Intelligence (Newell et al., 1959) with the motivation of mimicking the human thinking process. One possible interpretation of a general solver, is the capability of solving problems from any domain independently. Part I of the thesis starts with Classical Planning, whose solvers fall into the category of being domain independent, so instances from different planning domains can be solved using the same classical planning solver (see Chapter 1). Another possible interpretation of a general solver, is the generalization over a set of problems, also known as Generalized Planning (see Chapter 2). In other words, the general solver must find a solution that solves each problem from a set of planning problems (Hu and De Giacomo, 2011). The solution to a generalized planning problem is a generalized plan. In the rest of this thesis we show multiple representations and computations of generalized plans.

We mainly represent and compute generalized plans as planning programs in Part II. A planning program is a set of instructions enhanced with conditional gotos that can be programmed and executed (see Chapter 3). We show a methodology to compile a set of planning problems into a single PDDL domain and instance. Then, we can use any off-the-shelf classical planner to synthesize and validate programs.

We continue with an extension of planning programs with a call stack that simulates a computer stack in PDDL (see Chapter 4). This allows to include and call previous knowledge in form of planning programs as procedures. We can even synthesize recursive solutions when procedures call themselves, and if procedures have parameters they can find solutions like a depth-first search (DFS) algorithm for traversing a binary tree. In addition to planning program formalism and influenced by Baier et al. [2007], we show results when instructions are lifted such that they are used as Domain Control Knowledge (DCK). We define planning programs with lifted actions as non-deterministic planning programs (see Chapter 5).

Programs synthesis (Gulwani et al., 2017) is the problem of automatically finding a program given some input specification. These programs are represented in many different formalisms, i.e. from logical formulae (Cresswell and Codding-ton, 2004; Patrizi et al., 2011), to Finite State Controllers (FSCs) (Bonet et al., 2010; Hu and De Giacomo, 2013). Thus, in Part III we explore the connection of program synthesis as generalized planning with FSCs. In Chapter 6 we show how to synthesize FSCs following a similar approach to planning programs. Furthermore, the call stack already implemented in Chapter 4 can be used to generate a hierarchy ofFSCs.

In Part IV, we extend planning programs with the concept of choice instruction. The first approach includes the formalism of planning programs with procedures, and adds a non-deterministic choice function that can call online any of the previous procedures to solve a planning instance. This problem of choosing the correct procedure to execute is connected to plan recognition (Ramirez and Geffner, 2010). Thus, we call unsupervised classification of planning instances (see Chapter 7) the process of automatically determining the procedure that correctly solves a planning problem. In the second approach, the non-determinist choice function is programmed on the first line of each procedure, and the planner has to choose online a valid program line to jump and execute a piece of code. This representation is equivalent to a context-free grammar (CFG) from which we can perform the tasks of string parsing and production using a classical planner (see Chapter 8).

The last part of the thesis (Part V) is to discuss the related work (see Chapter 9) of the previous chapters. The idea of dedicating a chapter to this topic is to avoid repeating citations because some previous work is connected to many chapters. The last chapter is to wrap-up the dissertation (see Chapter 10) and explain some future work to move towards a general AI.




---------------------------------------




一般求解器的兴趣源于人工智能的起源（Newell等，1959），其动机是模仿人类的思维过程。通用求解器的一种可能解释是独立解决任何领域问题的能力。本文的第一部分从古典规划开始，其求解器属于领域独立的类别，因此可以使用相同的古典规划求解器来求解来自不同规划领域的实例（请参阅第1章）。通用求解器的另一种可能解释是对一组问题的通用化，也称为通用规划（参见第2章）。换句话说，通用求解器必须从一组计划问题中找到解决每个问题的解决方案（Hu和De Giacomo，2011）。广义计划问题的解决方案是广义计划。在本文的其余部分，我们将展示广义计划的多种表示形式和计算形式。



在第二部分中，我们主要代表和计算广义计划作为计划程序。计划程序是一组可以通过编程和执行的条件条件增强的指令（请参见第3章）。我们展示了一种将一组计划问题编译到单个PDDL域和实例中的方法。然后，我们可以使用任何现成的经典计划器来合成和验证程序。



我们继续使用调用堆栈扩展计划程序，该调用堆栈在PDDL中模拟计算机堆栈（请参见第4章）。这允许以计划程序的形式包括和调用以前的知识作为程序。当过程调用自身时，我们甚至可以合成递归解，并且如果过程具有参数，它们可以找到诸如遍历二叉树的深度优先搜索（DFS）算法之类的解决方案。除了规划程序形式主义和拜耳等人的影响。[2007]，我们显示了解除指令后将其用作域控制知识（DCK）的结果。我们将行动被取消的计划程序定义为不确定的计划程序（请参阅第5章）。



程序综合（Gulwani et al。，2017）是在给定某些输入规范的情况下自动查找程序的问题。这些程序可以用许多不同的形式主义来表示，即从逻辑公式（Cresswell和Codding-ton，2004年； Patrizi等人，2011年）到有限状态控制器（FSC）（Bonet等人，2010年； Hu和De Giacomo， 2013）。因此，在第三部分中，我们探索了作为综合计划与FSC的程序综合的联系。在第6章中，我们将说明如何按照类似的计划程序来合成FSC。此外，已经在第4章中实现的调用堆栈可用于生成FSC的层次结构。



在第四部分中，我们以选择指导的概念扩展了计划程序。第一种方法包括使用程序对计划程序进行形式化，并添加非确定性选择功能，该功能可以在线调用以前的任何程序来解决计划实例。选择正确的程序执行的问题与计划识别有关（Ramirez和Geffner，2010）。因此，我们将计划实例的无监督分类（请参阅第7章）称为自动确定正确解决计划问题的过程的过程。在第二种方法中，不确定性选择功能被编程在每个过程的第一行，并且计划者必须在线选择有效的程序行来跳转并执行一段代码。



论文的最后部分（第五部分）是讨论前几章的相关工作（请参阅第9章）。为该主题专门安排一章的想法是避免重复引用，因为一些先前的工作与许多章节相关。最后一章是对论文的总结（请参见第10章），并解释了将来向通用AI迈进的一些工作。









---------------------------------------













9.2具有控制知识的计划

在本节中，我们将从与广义计划相关的多个领域中回顾相关工作。必须提到的是，从计划和学习的角度研究了广义计划（请参阅第2章）。



9.2.1宏动作

宏观行动（即行动子序列）是计算一般知识以进行规划的最早建议之一，文献中有几种方法可以用来计算这些知识（Botea等，2005； Coles和Smith，2007； Jonsson，2009）。 。但是，由宏操作确定的顺序执行流程通常过于僵化，即使将宏参数化，也必须将它们与控制流结构结合起来，才能推广到更多的规划实例。



9.2.2通用政策

广义策略是比宏更为灵活的形式主义。广义策略是将状态和目标映射为操作的一组规则。因此，广义策略是被动的，没有明确表示动作序列。但是，计算好的通用策略很复杂。早期的用于计算广义策略的算法（Khardon，1999； Martin和Geffner，2004）首先计算顺序计划，然后尝试从这些计划中概括策略规则，这是一项艰巨的任务，因为通常会出现大量对称性和转置。顺序计划。而且，不能以直接方式将广义策略添加到领域理论中。但是，我们在前面的章节中介绍了几种与广义策略有关的形式主义。例如，



9.2.3程序域控制知识

域控制知识是指有关计划解决方案的结构的知识。使用DCK进行计划也可以看作是广义计划的一种形式，它限制了可能的解决方案的空间，但是需要计划者针对特定的经典计划实例生成完全指定的解决方案。这种方法与具有控制规则的计划（Bacchus和Kabanza，2000； Veloso等人，1995）和分层计划（Shivashankar等人，2012； Nau等人，2003）有关。



以类Golog程序的形式出现的过程性DCK（请参阅第4章）（Baier等，2007； Fritz等，2008）包括条件和循环以及不确定性选择动作，这些行为限制了对解决方案的搜索。但是，它们不是适当的广义计划，因为仍然有必要应用计划程序来解决每个单独的计划问题。与我们在第5章中介绍的方法相反，它们是手工制作的，并未实现用于过程调用的PDDL机制。



9.2.4有限状态机

先前有关计算有限状态机（FSM）的工作（Bonet等人，2010年）还使用了一种编译程序，该程序在验证FSM满足一组测试用例的情况下对FSM进行编程。但是，FSM的生成是不同的，因为它从部分可观察的计划模型开始，并使用从一致计划到经典计划的汇编（Palacios和Geffner，2009）。FSM可以理解为一种表示和计算过程DCK的方式，该过程（1）不实现过程调用和递归；（2）不会将FSM重新用于类似任务。另一个区别是，我们的条件goto指令可以在任何流利语言上分支，而无需预先定义观察值的子集，尽管我们也将从限制分支条件的数量中受益。



9.2.5分层计划

分层计划是在给出高级目标规范的情况下找到行动的有序序列的问题。它被正式定义为分层任务网络（HTN），这是表示计划库的强大机制（Nau等，2003； Shivashankar等，2012）。HTN被定义为一组原始任务，一组分解为更简单任务的复合任务，分解方法和一组目标任务。达到目标任务的规范水平与CFG的生产规则有很大关系（请参阅第8章）。



以前生成HTN的工作（Hogg等人，2008； Lotinac和Jon-sson，2016）表明，可以从问题中计算出HTN，以编码可应用于任何域实例的域知识。因此，生成HTN类似于广义规划任务，这为扩展我们从平面动作序列计算HTN的方法打开了有趣的研究方向。这也与归纳逻辑编程（ILP）（Muggle-ton，1999）有关，后者从示例中学习逻辑程序。与逻辑程序或HTN不同，我们生成的CFG是命题的，不包含变量，但允许递归求解。



9.2.6基于案例的计划

有两种称为自上而下或自下而上的主要策略来计算广义计划任务的解决方案（请参阅第2.3.3节）。在我们的方法中，我们使用自上而下的策略，在程序空间中进行搜索以覆盖整个计划实例集。在基于案例的计划（CBP）中（Borrajo等，2015），他们使用第二种方法。为了解决一般化的计划任务，他们查看单个计划实例，计算一个解决方案，将其概括化，然后将合并方法与先前找到的解决方案应用于当前解决方案。CBP技术逐渐增加了广义计划的覆盖范围，但需要复杂的合并方法。这种方法与计划修复工作有关（Fox等，



Distill系统（Winner和Veloso，2003年）属于这一类，正如我们在第3章中所做的工作一样，它使用程序来表示广义计划。但是，它的表示形式是不同的，并且没有像我们在第3章，第4章和第5章中所做的那样，在各种各样的广义规划任务中测试了它的性能。



9.3程序综合

程序综合（Gulwani et al。，2017）是自动生成满足给定高级输入规范的程序的任务。该研究领域的许多想法都与广义规划有关，但是由于广义规划遵循领域独立方法并处理其针对状态，动作和目标的特定表示，因此它们并不立即适用。在这里，我们回顾了最成功的程序综合方法：



9.3.1实例编程

通过示例编程（PbE）可计算与一组给定的输入输出示例一致的程序集。输入输出示例对于非程序员来说很直观，可以创建程序。此外，这种类型的规范使程序综合比使用抽象程序状态进行推理更容易处理。PbE技术已经在现实世界中部署，并且是Office 2013中Excel的Flash Fill功能的一部分（请参见4.6节），该功能生成用于字符串转换的程序（Gulwani，2011年）。在这种情况下，使用称为版本空间代数的数据结构以受限的领域特定语言（DSL）简洁地表示了一组合成程序。（Mitchell，1982）使用实现分而治之方法的特定领域搜索来计算程序。



9.3.2通过草图编程

在草绘编程（PbS）中，程序员提供了部分指定的程序，即表示一种实现的高级结构但留下低级细节却无法由合成器确定的程序（Solar-Lezama等，2006年）。 ）。这种形式的程序综合依靠一种称为SKETCH的编程语言来绘制部分程序。PbS在由两个通信的SAT解算器（归纳合成器和验证器）构建的合成验证循环上实施了反例驱动的迭代，以自动生成测试输入并确保程序满足它们。即使在最坏的情况下，量化布尔可满足性（QBF）的综合问题也是PSPACE完全的，并且可以在时间上以指数形式解决量化变量的数量，



9.3.3有界合成

有界综合解决了满足给定线性时序逻辑（LTL）公式的有限状态转换系统的综合问题（Schewe和Finkbeiner，2007； De Giacomo和Vardi，2015）。有界综合的主流方法是将此任务编译为可满足性模理论（SMT）（Barrett和Tinelli，2018）问题。编译需要在系统参数（例如拒绝状态数）上确定一个界限，并以此提出使用基于SAT的技术解决的理论。在我们的案例中，我们要解决一组计划任务，这些任务必须由广义计划按特定顺序进行覆盖（请参见第2章）。这是受机器学习（ML）和测试驱动开发（TDD）中的单元测试启发的。



9.4 GOLOG



事实证明，GOLOG动作语言系列可用于对能够概括的自主行为进行编程（Levesque等，1997）。除了条件，循环和递归过程外，GOLOG程序还可以包含不确定部分。GOLOG程序不需要代表一个完整指定的解决方案，而只是一个草图，其中不确定的部分是系统要填补的空白。GOLOG程序员可以通过搜索来确定预定义行为与系统要解决的某些部分之间的正确平衡。基本的GOLOG解释器使用PROLOG回溯机制来解析搜索。这种机制基本上相当于盲目搜索，因此在解决计划任务时，除了最小的实例大小以外，它很快就变得不可行了。INDIGOLOG（Sardina等，2004）将GOLOG扩展为包含许多内置的计划机制。此外，可以利用GOLOG和PDDL之间的语义兼容性（Roger等，2008），并可以嵌入PDDL规划器（ClaBen等，2008），以解决本质上是组合的子问题。我们定义了自己的编程语言，该语言定义了可能的广义计划的空间。在这种语言中，分支和循环使用相同的构造（条件gotos）实现，以保持解决方案空间尽可能的减少（请参阅第3章）。我们定义了自己的编程语言，该语言定义了可能的广义计划的空间。在这种语言中，分支和循环使用相同的构造（条件gotos）实现，以保持解决方案空间尽可能的减少（请参阅第3章）。我们定义了自己的编程语言，该语言定义了可能的广义计划的空间。在这种语言中，分支和循环使用相同的构造（条件gotos）实现，以保持解决方案空间尽可能的减少（请参阅第3章）。



9.5分层有限状态控制器

我们专门用一个部分来比较与层次有限状态控制器（请参阅第6章）相关的工作，以说明本文的相关性和该方法的新颖性。与我们的方法和以前的自动生成FSC的方法（Bonet等，2010； Hu and De Giacomo，2013）的主要区别在于，部分可观察的计划模型以观察功能作为输入，而在我们的经典计划中编译时，除了FSC的转换和输出功能外，还综合了观察功能。因此，由于所有流利的流都被认为是可观察的，因此我们生成了在任何流利上分支的分层FSC。此外，我们的方法提供了一种调用机制，使生成递归解决方案并将现有知识纳入现有FSC成为可能。



分层FSC与计划程序形式化有关，用于表示和计算紧凑和广义的计划（请参见第4章）。这些程序是FSC的特例，通常，FSC可以比计划程序更紧凑地表示计划。另一个相关的形式主义是自动机计划（Backstrom等，2014），它也使用有限状态自动机的层次结构紧凑地存储顺序计划。但是，自动机计划是Mealy机器，其转换取决于显式输入字符串的符号。因此，自动机计划不适合表示广义计划，而是将重点放在顺序计划的压缩上。



除解决方案计划外，有限状态自动机还可以代表计划中的其他对象。例如，域转换图是一个自动机，用于表示计划状态变量的可能值（Chen等，2008）。Toropila和Bartak [2010]还使用有限状态机来表示给定计划实例的状态变量的域。另一个例子是LOCM系统，它使用有限状态机来表示规划领域模型（Cress-well等，2013）或Hickmott等。[2007]使用Petri网表示整个规划实例。



9.6分层强化学习

强化学习（RL）（Sutton and Barto，1998）是通过与世界互动来学习政策的问题，同时获得了正面和负面的奖励。文献探索了不同的方法，例如Shavlik [1990]，Parr和Russell [1998]，Dietterich [2000]和Chentanez等。[2005]利用复杂的顺序问题的层次分解，并了解何时应使用每个控制器。在某些情况下，该知识可以迭代地包含在控制器包中，在其他情况下，此集合是封闭的，但可以重复使用以解决更复杂的任务，选项或学习更复杂的概念。这与第4章有关，在第4章中，层次分解是以带有程序的计划程序的形式进行的；而在第6章中，我们具有允许递归调用的层次有限状态控制器。



尽管在最佳情况下，学习可以收敛到最小化成本函数（或最大化报酬）的解决方案；在具有巨大状态空间，完全可观察性和遥远视野的领域中，RL方法无法实现目标甚至难以收敛，因此我们可以从规划技术中受益的广义规划方法仅可用于探索有希望的领域状态空间部分。



9.7活动识别

一方面，属于广义计划任务的计划实例集可以理解为一种无监督学习方法（请参见第7章），其中输入示例和类标签对应于可达状态和广义计划。因此，泛化计划是学习的集群模型，适用于每个可达状态及其相应的动作。如果我们可以从一组经典计划中得出一个广义计划，则可以将其视为标签。这将对应于监督学习（德拉罗莎等人，2011）。



另一方面，也可以从活动识别的角度来理解CFG的生成（请参阅第8章），这样就可以将活动库正式化为CFG，该库最初是未知的，并且输入字符串会编码CFG的观察结果活动要认识。传统上认为活动识别独立于使用手工制作的活动库和特定算法进行的自动化计划研究（Ravi等，2005）。拉米雷斯和格夫纳[2009; 2010]，通过计划制定并解决了目标识别问题。据我们所知，我们将CFG编译为广义计划（请参见第8章）是第一个使用通用计划模型和现成的经典计划器将语法生成，字符串解析和字符串生成等任务集成在一起的程序。



第10章



概要

在第10章中，我们总结了本论文最相关的贡献，然后讨论了可能扩展该工作的未来方向以及新的挑战。















9.2 Planning with Control Knowledge
In this section we review related work from multiple fields that are connected to generalized planning. We must mention that generalized planning (see Chapter 2) has been studied from planning and learning perspectives.

9.2.1 Macro-Actions
Macro-actions (i.e. action sub-sequences) were among the first suggestions to compute general knowledge for planning and there are several approaches in the literature for computing them (Botea et al., 2005; Coles and Smith, 2007; Jonsson, 2009). However, the sequential execution flow fixed by macro-actions is usually too rigid and, even when macros are parameterized, they have to be combined with control-flow structures in order to generalize to more planning instances.

9.2.2    Generalized Policies
Generalized policies are a more flexible formalism than macros. A generalized policy is a set of rules mapping states and goals into actions; hence generalized policies are reactive and do not explicitly represent action sequences. Computing good generalized policies is however complex. Early algorithms for computing generalized policies (Khardon, 1999; Martin and Geffner, 2004) first compute sequential plans, and then attempt to generalize the policy rules from these plans, a difficult task because of the high number of symmetries and transpositions that commonly appear in sequential plans. Moreover, a generalized policy cannot be added in a straightforward way to a domain theory. However, we have introduced several formalisms in previous chapters that are related to generalized policies. For instance, planning programs (see Chapter 3) and Finite State Controllers (see Chapter 6) guide classical planners effectively with Domain Control Knowledge (DCK), similar to previous approaches for generating generalized policies (Yoon et al., 2008; De la Rosa et al., 2011).

9.2.3    Procedural Domain Control Knowledge
Domain Control Knowledge refers to knowledge about the structure of planning solutions. Planning with DCK can also be seen as a form of generalized planning, that constrains the space of possible solutions, but requires a planner to produce a fully specified solution for a particular classical planning instance. This approach is connected to planning with control rules (Bacchus and Kabanza, 2000; Veloso et al., 1995) and hierarchical planning (Shivashankar et al., 2012; Nau et al., 2003).

Procedural DCK (see Chapter 4) in the form of Golog-like programs (Baier et al., 2007; Fritz et al., 2008) include conditionals and loops as well as nondeterministic choice actions that constrain the search for a solution plan. Nevertheless they are not proper generalized plans since it is still necessary to apply a planner to solve each individual planning problem. In contrast to our approach in Chapter 5, they are hand-crafted and do not implement PDDL mechanisms for procedure calling.

9.2.4    Finite State Machines
Previous work on computing Finite State Machines (FSMs) (Bonet et al., 2010) also uses a compilation that interleaves programming a FSM with verifying that it satisfies a set of test cases. The generation of a FSM is however different since it starts from a partially observable planning model and uses a compilation from conformant to classical planning (Palacios and Geffner, 2009). FSMs can be understood as a way of representing and computing procedural DCK that (1) does not implement procedure calls and recursion; (2) does not reuse FSMs for similar tasks. Another difference is that our conditional goto instructions can branch on any fluent without the need to predefine a subset of observations, although we would also benefit from restricting the number of branch conditions.

9.2.5    Hierarchical Planning
Hierarchical planning is the problem of finding an ordered sequence of actions given a high-level goal specification. It is formalized as a Hierarchical Task Network (HTN) that is a powerful mechanism to represent libraries of plans (Nau et al., 2003; Shivashankar et al., 2012). HTNs are defined as a set of primitive tasks, a set of compound tasks that are decomposed into simpler tasks, the decomposition methods and a set of goal tasks. The level of specifications to reach a goal task has a strong relation with the production rules of CFGs (see Chapter 8).

The previous work in generating HTNs (Hogg et al., 2008; Lotinac and Jon-sson, 2016) show that HTNs can be computed from problems to encode domain knowledge that can be applied to any instance of the domain. Thus, generating an HTN is similar to a generalize planning task which opens an interesting research direction to extend our approach for computing HTNs from flat sequences of actions. This is also related to Inductive Logic Programming (ILP) (Muggle-ton, 1999) that learns logic programs from examples. Unlike logic programs or HTNs, the CFGs we generate are propositional and do not include variables but they allow recursive solutions.

9.2.6    Case-Based Planning
There are two main strategies called top-down or bottom-up to compute a solution to a generalized planning task (see Subsection 2.3.3). In our approaches we use the top-down strategy, searching in the space of programs to cover the whole set of planning instances. While in Case-Based Planning (CBP) (Borrajo et al., 2015) they use the second approach. In order to solve a generalized planning task, they look at a single planning instance, compute a solution that solves it, generalizes it, and then applies to the current solution the merging method with the solutions found previously. The CBP techniques incrementally increase the coverage of a generalized plan but require complex merging methods. This approach is related to works on plan repair (Fox et al., 2006) since it demands identifying why a solution does not cover a given instance and adapting it to the uncovered instance.

The Distill system (Winner and Veloso, 2003) lies in this category and, as our work in Chapter 3, uses programs to represent generalized plans. However, its representation is different and its performance was not tested over a wide range of diverse generalized planning tasks as we did in Chapters 3, 4 and 5.

9.3 Program Synthesis
Program synthesis (Gulwani et al., 2017) is the task of automatically generating a program that satisfies a given high-level input specification. Many ideas from this research field are relevant to generalized planning but they are not immediately applicable since generalized planning follows a domain-independent approach and handles its own specific representation for states, actions and goals. Here we review the most successful approaches for program synthesis:

9.3.1    Programming by Example
Programming by Example (PbE) computes a set of programs consistent with a given set of input-output examples. Input-output examples are intuitive for nonprogrammers to create programs. Moreover, this type of specification makes program synthesis more tractable than reasoning with abstract program states. PbE techniques have already been deployed in the real world and are part of the Flash Fill feature of Excel in Office 2013 (see Section 4.6) that generates programs for string transformation (Gulwani, 2011). In this case the set of synthesized programs are represented succinctly in a restricted Domain-Specific Language (DSL) using a data-structure called version space algebras (Mitchell, 1982). The programs are computed with a domain-specific search that implements a divide and conquer approach.

9.3.2    Programming by Sketching
In Programming by Sketching (PbS), programmers provide a partially specified program, i.e. a program that expresses the high-level structure of an implementation but that leaves low level details undefined to be determined by the synthesizer (Solar-Lezama et al., 2006). This form of program synthesis relies on a programming language called SKETCH, for sketching partial programs. PbS implements a counterexample-driven iteration over a synthesize-validate loop built from two communicating SAT solvers, the inductive synthesizer and the validator, to automatically generate test inputs and ensure that the program satisfy them. Even though in the worst case, the synthesis problem to a quantified boolean satisfiability (QBF) is PSPACE-complete, and can be solved in time exponential in the number of quantified variables, this counterexample-driven search terminates on many real problems after solving only a few SAT instances (Lake et al., 2015).

9.3.3 Bounded Synthesis
Bounded synthesis addresses the synthesis of finite-state transition systems that satisfy a given Linear Temporal Logic (LTL) formula (Schewe and Finkbeiner, 2007; De Giacomo and Vardi, 2015). The mainstream approach for bounded synthesis is compiling this task into a satisfiability modulo theories (SMT) (Barrett and Tinelli, 2018) problem. The compilation requires fixing a bound on the system parameters, such as the number of rejecting states, with which it proposes theories that are solved using SAT-based techniques. In our case we have a set of planning tasks to solve that must be covered in a specific order by a generalized plan (see Chapter 2). This is inspired in Machine Learning (ML) and unit tests in Test-Driven Development (TDD).

9.4 GOLOG

The GOLOG family of action languages has proven useful for programming autonomous behavior that is able to generalize (Levesque et al., 1997). Apart from conditionals, loops and recursive procedures, GOLOG programs can contain nondeterministic parts. A GOLOG program does not need to represent a fully specified solution, but a sketch of it, where the non-deterministic parts are gaps to be filled by the system. The GOLOG programmer can determine the right balance between predefined behavior and leaving certain parts to be solved by the system by means of search. The basic GOLOG interpreter uses the PROLOG backtracking mechanism to resolve the search. This mechanism basically amounts to blind search, so when addressing planning tasks, it soon becomes unfeasible for all but the smallest instance sizes. INDIGOLOG (Sardina et al., 2004) extends GOLOG to contain a number of built-in planning mechanisms. Furthermore the semantics compatibility between GOLOG and PDDL (Roger et al., 2008) can be exploited and a PDDL planner can be embedded (ClaBen et al., 2008) to address the sub-problems that are combinatorial in nature. We defined our own programming language that defines the space of possible generalized plans. In this language branching and loops are implemented with the same construct (conditional gotos) to keep the solution space as reduced as possible (see Chapter 3).

9.5 Hierarchical Finite State Controllers
We dedicate a section to compare work related to Hierarchical Finite State Controllers (see Chapter 6) for the relevance in this dissertation and the novelty of the approach. The main difference from our approach with previous work on automatically generating FSCs (Bonet et al., 2010; Hu and De Giacomo, 2013) rely on a partially observable planning model in which the observation function is given as input, while in our classical planning compilation, the observation function is synthesized in addition to the transition and output functions of FSCs. Thus, we generate hierarchical FSCs that branch on any fluent since all fluents, are considered observable. Further, our approach provides a call mechanism that makes it possible to generate recursive solutions and to incorporate prior knowledge as existing FSCs.

Hierarchical FSCs are related to the planning programs formalism for the representation and computation of compact and generalized plans (see Chapter 4). These programs are a special case of FSCs, and in general, FSCs can represent plans more compactly than planning programs. Another related formalism is automaton plans (Backstrom et al., 2014), which also store sequential plans compactly using hierarchies of finite state automata. However, automaton plans are Mealy machines whose transitions depend on the symbols of an explicit input string. Hence automaton plans are not suitable for representing generalized plans, and their focus is instead on the compression of sequential plans.

Apart from solution plans, finite state automata can represent other objects in planning. For instance, the domain transition graph is an automaton for representing the possible values of planning state variables (Chen et al., 2008). Toropila and Bartak [2010] also used finite state machines to represent the domains of the state variables of a given planning instance. Another examples are the LOCM system, that uses finite state machines to represent planning domain models (Cress-well et al., 2013) or Hickmott et al. [2007] that used Petri nets to represent an entire planning instance.

9.6 Hierarchical Reinforcement Learning
ReinforcementLearning (RL) (Sutton and Barto, 1998) is the problem oflearning a policy by interacting with the world while obtaining positives and negatives rewards. The literature explores different approaches like Shavlik [1990], Parr and Russell [1998], Dietterich [2000] and Chentanez et al. [2005] that leverages hierarchical decompositions of complex sequential problems and learn when every controller should be applied. In some cases this knowledge can be iteratively included in the bag of controllers, in other cases this set is closed but can be reused to solve more complex tasks, options or to learn more complex concepts. This is related to Chapter 4 where the hierarchical decomposition is in form of planning programs with procedures or to Chapter 6 where we have hierarchical finite state controllers that allow recursive calls.

Although in the best case, learning converges to a solution that minimizes a cost function (or maximizes a reward); in domains with huge state spaces, full observability and a distant horizon, it may become unfeasible for RL approaches to reach a goal and even harder to converge, so our approach of generalized planning that benefits from planning techniques can be applied to explore only the promising state space sections.

9.7 Activity Recognition
On the one hand, the set of planning instances that belong to a generalized planning task can be understood as an unsupervised learning method (see Chapter 7) where input examples and class labels correspond to reachable states and a generalized plan. Thus, a generalize plan is the learned cluster model that applies to every reachable state its corresponding action. We consider a set of classical plans as labels if we can induce from this set a generalized plan. This would correspond to supervised learning (De la Rosa et al., 2011).

On the other hand, the generation of CFGs can also be understood in terms of activity recognition (see Chapter 8), such that the library of activities is formalized as a CFG, the library is initially unknown, and the input strings encode observations of the activities to recognize. Activity recognition is traditionally considered independent of the research done on automated planning, using handcrafted libraries of activities and specific algorithms (Ravi et al., 2005). An exception is the work by Ramirez and Geffner [2009; 2010] where goal recognition is formulated and solved with planning. As far as we know our compilation of CFGs to generalized planning (see Chapter 8) is the first that integrates the tasks of grammar generation, string parsing and string production using a common planning model and an off-the-shelf classical planner.

Chapter 10

Summary
In this Chapter 10 we show a summary of the most relevant contributions of this dissertation followed by a discussion of possible future directions where this work could be extended and new challenges.






