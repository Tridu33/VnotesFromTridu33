# Codegenerator_GP_summary



- 逻辑公式演算，谓词等天然形成的Golog类似逻辑式命令式程序运行在prolog上,ROS总用
- 逻辑公式演算还天然形成自然生成OCAML等“函数式编程语言”，具体已经实现的有：Coq 的Extraction 
- DSL，编译原理前端的“语法分析词法分析等形成中间表达”，通过AST等效转换为c-like 程序

# 一直相关工作

## pre code relevant

https://www.sciencedirect.com/science/article/pii/S0004370219300232
广义计划是生成单个解决方案的任务（广义计划）对多个计划实例有效。在本文中，我们引入了一种新颖的形式化形式来表示广义计划，该形式主义借鉴了结构化编程中的两种机制：控制流和过程调用。一方面，控制流结构允许紧凑地表示通用计划。另一方面，过程调用可以表示层次结构和递归解决方案，并可以重用现有的广义计划。本文还提出了从广义计划到经典计划的汇编，这使我们能够与现成的计划者一起计算广义计划。该汇编可以辅助程序的形式结合现有知识，从而将方法的适用性扩展到更具挑战性的任务。实验表明，使用我们的编译器的经典计划器可以计算出广义计划，以解决各种广义计划任务，包括对**可变大小的列表进行排序或遍历可变大小的二叉树**的DFS。另外，当泛化要求没有先验条件的高级状态表示时，本文介绍了用于计算泛化计划的编译的扩展。此扩展为经典计划带来了新的基准环境，因为分类任务自然可以建模为广义计划任务，因此也可以建模为经典计划任务。最后，本文表明，可以将编译结果扩展为为现成的计划者计算控制知识，并解决没有此类额外知识而难以解决的计划实例。




在本文中，我们介绍了一种创新的形式主义，用于表示广义的计划，我们称其为计划程序，并从结构化程序设计中借鉴了两种有效的机制：控制流（以条件goto指令的形式出现）和过程调用。虽然条件goto方法使我们能够有效的为一家集策划实例的紧凑编码复杂的解决方案，过程调用允许我们代表层次和递归解决方案，以及重用现有的推广计划。

我们用于计算此类通用计划的方法是将编译定义为经典计划，从而可以使用现成的经典计划器生成通用计划。简而言之，我们的编译对有限数量的程序行和程序计数器进行编码，并介绍了在不同程序行上对指令进行编程和执行的动作。由编译产生的经典计划任务的解决方案是一系列动作，这些动作对程序行中的指令进行编码，并在广义计划任务的所有实例上执行它们。有趣的是，汇编可以辅助程序的形式结合现有知识，并自动完成剩余程序的定义。

在某些领域，仅当状态的特定高级表示可用时，才可以执行紧凑的广义计划。例如，在经典的blockworld域中，高级状态功能会在一个块处于其目标位置时捕获[6]，[7] 。在广义规划的大多数应用中，此类功能由领域专家手动编码。在本文中，我们提出了扩展的编译方法，以将特征的计算与广义计划的计算相集成，从而生成可以在没有状态的高级表示的情况下进行泛化的解决方案。值得一提的是，此扩展使我们可以对监督分类任务进行建模 作为经典的计划实例。

即使用于表示广义计划的语言具有表达能力，但是如果广义计划任务中的实例没有共享清晰的通用结构，则实现广义化可能仍然很复杂。在这种情况下，用不确定的执行方式表示和计算解决方案可能会有用[8]。这种解决方案更加灵活，因为它们允许仅在特定实例中执行解决方案时才确定的开放段。在本文中，我们介绍了规划程序形式化的两个不同扩展，以通过非确定性执行来实现泛化：选择指令和提升操作指令。

为了清楚起见，我们将每个扩展作为不涉及程序的基本计划程序的修改形式进行单独介绍。但是，直接组合多个扩展，例如高级状态功能和选择指令。所有源代码和相关文档都可以在公共存储库（https://github.com/aig-upf/automated-programming-framework ）中找到，




该文件还说明了如何配置扩展的不同组合。

先前在几篇会议论文[9]，[10]，[11]中首次介绍了该编译及其扩展。与会议论文相比，本论文包括以下新颖材料：
•
我们建立了计划程序形式主义的理论基础，并表明计划程序的计划验证和计划存在是PSPACE完整的。此外，我们提供了可以用我们的形式主义来表示的解决方案的形式化描述，并证明我们不同形式的计划程序的表现力是等效的。

•
我们统一了针对计算计划程序的汇编的不同表述及其对具有程序和高级状态功能的计算计划程序的扩展，并提供了其健全性和完整性的正式证明。

•
我们为计划程序的非确定性执行引入了两种新颖的形式主义：选择指令和提升操作指令。

•
我们展示了如何在我们的编译中为计划程序实现验证机制。我们使用这种机制来表明，重用广义计划并将广义计划用作控制知识使我们能够解决使用当前经典计划器难以解决的计划实例，例如具有100个块的blockworld实例。

•
我们使用不同的现成计划人员编写的报告来报告新的实验结果。此外，我们为与通用编程任务相对应的通用规划引入了新的具有挑战性的领域，以及程序综合的新领域，并讨论了将我们的方法应用于此类任务的利弊。


本文的结构如下，第2节通过回顾先前有关广义规划和计划综合的工作，将我们的工作置于背景之中。第3定义了规划模型，我们将依靠沿着这个工作，经典规划与有条件的效果和推广计划。第4节介绍了代表广义计划的计划程序形式主义，并定义了它们的理论属性。第5节介绍了我们的编译及其扩展，以计算计划程序和具有可调用程序的计划程序来解决广义计划任务。第6节显示了如何扩展编辑以将特征的计算与广义计划的计算集成在一起。第7节显示了如何使用非确定性执行来计算计划程序。最后，第8节总结了我们的工作，并讨论了未解决的问题和未来的工作。








**这篇文章是最最最相关的，他的引用论文有这些**

REFERENCES
Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2016a), Generalized planning with procedural domain control knowledge, ICAPS 2016.

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2016b), Hierarchical finite state controllers for generalized planning, IJCAI 2016.

Lotinac, D., Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2016), Automatic generation of high-level state features for generalized planning, IJCAI 2016.

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2017a), Unsupervised classification of planning instances, ICAPS 2017.

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2017b), Generating context-free grammars using classical planning, IJCAI 2017.

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2018), Computing hierarchical finite state controllers with classical planning, JAIR 2018.

Segovia-Aguas, J. (2018), Program Synthesis for Generalized Planning, PhD Dissertation. 这篇博士论文也要认真看看

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2019), Computing programs for generalized planning using a classical planner, AIJ 2019.

Jiménez, S., Segovia-Aguas, J., and Jonsson, A. (2019), A review of generalized planning, KER 2019

Segovia-Aguas, J., Jiménez, S., and Jonsson, A. (2020) Generalized Planning with Positive and Negative Examples (to be published), AAAI 2020










### DSL领域特定语言代码生成























































































#### **计算广义策略**

*广义策略*是一组规则，它定义状态和目标的映射，成优选*动作接下来要执行。*像宏动作一样，广义策略也允许参数，并且可以从共享相同域理论的经典规划实例的一组解决方案中得出[^57][^99][^21]。但是，通用策略比宏动作更灵活，因为它们可以定义带有分支和循环的执行流。

[^57]: Mario  Mart ́ın  and  Hector  Geffner.   Learning  generalized  policies  fromplanning examples using concept languages.Applied Intelligence, 20(1):9–19, 2004.
[^99]: Sungwook Yoon, Alan Fern, and Robert Givan.  Learning control knowl-edge for forward search planning.The Journal of Machine Learning Re-search, 9:683–718, 2008.
[^21]:  Tomas De la Rosa, Sergio Jim ́enez, Raquel Fuentetaja, and Daniel Bor-rajo. Scaling up heuristic planning with relational decision trees.Journalof Artificial Intelligence Research, 40:767–813, 2011.


#### **计算有限状态控制器**

*有限状态控制器*（FSC）可以用有限数量的内存来泛化策略[^9]。具有单一状态的FSC表示策略，即无内存控制器。FSC的附加控制器状态为它们提供了内存，允许在给定相同观察值的情况下采取不同的操作。FSC形式主义也可以通过*调用堆栈*进行扩展，以表示分层和递归解决方案[^84]。

现有的用于计算用于广义规划的FSC的算法遵循*自上而下的*方法，该方法将对FSC 进行*编程*与验证相交错，因此它们紧密地集成了规划和归纳。为了使FSC的计算易于处理，它们限制了可能的解决方案的空间，从而限制了FSC的最大大小。另外，他们强加实例来解决共享问题，不仅是领域理论（动作和谓词方案），而且是流利的集合[^83]或*可观察*流利的子集[^10]。

用于广义计划的FSC的计算包括将广义计划任务编译为另一种问题解决形式的工作，因此它们将从现成求解器的最新进展中受益（例如，*经典计划*[^83]，*一致计划*[^10]，*CSP* [^74]或*Prolog程序*[^43]）。最后一种情况需要FSC

的行为规范，该规范包括以下分类的执行历史记录：（1）接受所有导致目标达到满意状态的合法执行历史记录；（2）拒绝包含重复配置的事件执行历史（表明无限循环），并且无法扩展（指示死角）[43]。


[^9]: Blai  Bonet  and  Hector  Geffner.   Policies  that  generalize:  Solving  manyplanning problems with the same policy.IJCAI, 2015.
[^84]:  Javier Segovia-Aguas, Sergio Jim ́enez, and Anders Jonsson.  Hierarchicalfinite state controllers for generalized planning.  InIJCAI, 2016.

[^10]: Blai Bonet, H ́ector Palacios, and Hector Geffner. Automatic derivation offinite-state machines for behavior control.  InAAAI, 2010.
[^43]: Yuxiao Hu and Giuseppe De Giacomo. A generic technique for synthesiz-ing bounded finite-state controllers.  InICAPS, 2013.
[^74]:  C ́edric Pralet, G ́erard Verfaillie, Michel Lemaˆıtre, and Guillaume Infantes.Constraint-based  controller  synthesis  in  non-deterministic  and  partiallyobservable domains.  InECAI, 2010.

#### **计算程序**

程序提高了FSC的可读性，它们将控制流结构与原始动作分开。像FSC一样，程序也可以按照*自上而下的*方法进行计算，例如，利用对状态和动作空间相同的实例进行编程并验证程序的编译[^83]。
[^83]: Javier Segovia-Aguas, Sergio Jim ́enez, and Anders Jonsson.  Generalizedplanning with procedural domain control knowledge.  InICAPS, 2016.
由于这些 *自上而下的*方法在解决方案的空间中进行搜索，因此限制不同的控制流指令集很有帮助。例如，仅使用既可以实现分支又可以实现循环的*条件getos* [^46]。

*DSPlanners* [^97][^98] 是将程序概括为计划的最早尝试之一。一个*DSPlanner* 是可以包含的if-then-else和while结构域的具体方案。这些构造根据关于当前状态和/或计划任务目标的FOL查询分支和循环程序的执行控制流。
[^46]: Sergio Jim ́enez and Anders Jonsson. Computing Plans with Control Flowand Procedures Using a Classical Planner.  InSOCS, 2015.
[^97]: Elly Winner and Manuela Veloso.  Distill:  Learning domain-specific plan-ners by example.  InICML, 2003.
[^98]:  Elly Winner and Manuela Veloso.  Loopdistill:  Learning looping domain-specific planners from example plans.  InICAPS, Workshop on ArtificialIntelligence Planning and Learning, 2007.

该算法计算DSPlanners被称为提炼并实现了一种*自下而上*的一组共享同一个域理论古典的规划实例的方法。给定一个实例，提炼计算该实例并整合其部分有序规划到现有DSPlanner如下。首先，Distill 提起部分订购的计划，选择与现有DSPlanner 相匹配的参数。如果不存在这样的参数化，则Distill 将变量名称随机分配给计划中的对象。然后Distill 尝试确定*语句*和展开的*循环迭代* 解决方案中将其替换为相应的控制流结构。

Srivastava等人在广义规划方面的工作。在程序中引入了一种强大而紧凑的结构，称为*选择动作，*该结构将存在变量和控制流结合在一起[^90][^91]。这项工作中的输入实例被表示为带有传递闭包的抽象FOL表示形式。这种形式主义允许用无限多个对象来表示计划任务，并保证此类任务的解决方案具有普遍性。

Srivastava等人的广义规划算法。实施*自下而上的*策略。该算法从一个空的广义计划开始，然后通过识别它无法解决的实例，调用经典计划器来解决该实例，将获得的解决方案归纳并将其合并回广义计划中，从而逐步增加其覆盖范围。重复该过程，直到生成一个涵盖整个期望类实例的广义计划（或达到计算资源的预定义限制时）。

程序和FSC都可以编入平面领域理论[^7][^83][^84]。就像政策一样，当给定程序（或FSC）正确时，这种编译是*安全的*（不会将可解决的计划实例转化为不可解决的）。

表1总结了一般计划的已审查方法。该表指示给定的解决方案表示形式是否允许使用 **变量**，**控制流的类型**以及解决方案的**执行**是否需要特定的机制。
[^90]: Siddharth  Srivastava,  Neil  Immerman,  and  Shlomo  Zilberstein.   A  newrepresentation and associated algorithms for generalized planning.Artifi-cial Intelligence, 175(2):615 – 647, 2011.
[^91]:  Siddharth Srivastava, Neil Immerman, Shlomo Zilberstein, and TianjiaoZhang.  Directed search for generalized plans using classical planners.  InICAPS, 2011.
[^7]: Jorge A Baier, Christian Fritz, and Sheila A McIlraith. Exploiting proce-dural domain control knowledge in state-of-the-art planners.  InICAPS,2007.
[^83]: Javier Segovia-Aguas, Sergio Jim ́enez, and Anders Jonsson.  Generalizedplanning with procedural domain control knowledge.  InICAPS, 2016
[^84]: Javier Segovia-Aguas, Sergio Jim ́enez, and Anders Jonsson.  Hierarchicalfinite state controllers for generalized planning.  InIJCAI, 2016.
[^]: 
[^]: 
[^]: 
[^]: 


根据解的表示方法分类Summary of the 

### diverse approaches for generalized planning 

according to the solution representations：

|                    |        Variables	         |        Control-flow	         |                Execution                 |
| ------------------ | ------------------------- | ------------------------------- | ---------------------------------------- |
| Classical plan     | ------                    | ------                          | Ground actions                           |
| Macro-Actions      | Action parameters         | ------                          | Lifted actions                           |
| Generalized Policy | Rule parameters           | Branching and loops             | Lifted  rules                            |
| DSPlanners         | Existential               | Branching and loops             | Lifted predicatesand lifted actions      |
| FSCs               | Quantified                | Branching and loops             | Derived predicates                       |
| Hierarchical FSCs  | Quantified and parameters | Branching, loops and call stack | Derived predicates and Parameter passing |
| Programs           | Quantified and parameters | Branching, loops and call stack | Derived predicates and Parameter passing |

### **GOLOG**

在Golog系列动作语言已被证明是对自主代理[^53]的高级控制一个有用的平均值。除了条件，循环和递归过程外，Golog 程序的一个有趣功能是它们可以包含不确定的部分。甲果洛程序不需要表示完全指明的解决方案，但它的一个草图，其中非确定性部分是间隙要由系统被填充。此功能使Golog 程序员可以灵活地在以下各项之间选择合适的平衡点：

•确定预定义的行为，这通常意味着较大的程序。

•通过搜索保留系统要解决的某些部分，这通常意味着更长的计算时间。

基本的Golog 解释器使用PROLOG回溯机制来解析搜索。这种机制基本上相当于盲目搜索，因此，在解决计划任务时，除了最小的实例大小之外，它很快就变得不可行了。IndiGolog [^80]扩展了Golog，使其包含许多内置的计划机制。此外，可以利用Golog和PDDL之间的语义兼容性[^79]，并且可以嵌入PDDL规划器[^17]来解决本质上是组合的子问题。

[^53]: Hector J Levesque, Raymond Reiter, Yves Lesp ́erance, Fangzhen Lin, andRichard  B  Scherl.   Golog:   A  logic  programming  language  for  dynamicdomains.The Journal of Logic Programming, 31(1-3):59–83, 1997.
[^80]: Sebastian Sardina, Giuseppe De Giacomo, Yves Lesp ́erance, and Hector JLevesque.   On  the  semantics  of  deliberation  in  indigologfrom  theory  toimplementation.Annals of Mathematics and Artificial Intelligence, 41(2-4):259–299, 2004.
[^79]: Gabriele  R ̈oger,  Malte  Helmert,  and  Bernhard  Nebel.   On  the  relativeexpressiveness of adl and golog:  The last piece in the puzzle. InKR, 2008
[^17]: Jens Claßen, Viktor Engelmann, Gerhard Lakemeyer, and Gabriele R ̈oger.Integrating  golog  and  planning:    An  empirical  evaluation.InNon-Monotonic Reasoning Workshop, 2008



### **6.4程序综合**

程序综合是自动生成满足给定高级规范的程序的任务。该研究领域的许多想法都与广义规划有关，但是由于广义规划遵循领域无关的方法并针对状态，动作和目标处理其自己的特定表示形式，因此它们并不立即适用。在这里，我们回顾了两种最成功的程序综合方法：

•  **示例编程**（PbE），计算与一组给定的输入输出示例一致的程序集。输入-输出示例对于非程序员来说很直观，可以创建程序，这种类型的规范使程序综合比对抽象程序状态进行推理更容易处理。PbE技术已在现实世界中部署，并且是Office 2013中Excel 的Flash Fill 功能的一部分，该功能可生成用于字符串转换的程序[^35]。在这种情况下，使用称为**version space algebras** 版本空间代数[^60]的数据结构以受限的特定领域语言（DSL）简洁地表示了一组合成程序。使用实现分而治之方法的特定领域搜索来计算程序。

•在“ **通过草图进行编程**（PbS）”中，程序员提供了部分指定的程序，即表示一种实现的高级结构但留下未定义细节的低级细节的程序，该细节由合成器确定[^89]。这种形式的程序综合依靠一种称为**SKETCH**的编程语言来绘制部分程序。PbS在由两个通信的SAT解算器（归纳合成器和验证器）构建的合成验证循环上实现了反例驱动的迭代，以自动生成测试输入并确保程序满足它们。尽管在最坏的情况下，程序的合成比NP的完成困难，但这种反例驱动的搜索仅在解决了少数SAT实例后就终止了许多实际问题[^50]。



以前的工作是*通过示例*进行 *编程的*从输入/输出示例中合成解析器的技术[^51]。

[^35]: Sumit Gulwani. Automating string processing in spreadsheets using input-output examples. InACM SIGPLAN Notices, volume 46, pages 317–330.ACM, 201
[^60]: Thomas  M  Mitchell.   Generalization  as  search.Artificial  intelligence,18:203–226, 1982.
[^89]: Armando  Solar-Lezama,  Liviu  Tancau,  Rastislav  Bodik,  Sanjit  Seshia,and Vijay Saraswat.  Combinatorial sketching for finite programs.ACMSIGOPS Operating Systems Review, 40:404–415, 2006
[^50]: Brenden  M  Lake,  Ruslan  Salakhutdinov,  and  Joshua  B  Tenenbaum.Human-level  concept  learning  through  probabilistic  program  induction.Science, 350(6266):1332–1338, 2015.
[^51]: Alan Leung, John Sarracino, and Sorin Lerner. Interactive parser synthesisby example. InACM SIGPLAN Notices, volume 50, pages 565–574. ACM,2015





## 使用经典计划器的通用计划计算程序 提到这些：



sciencedirect.com/science/article/pii/S0004370219300232  在线观看


自从AI诞生以来，就已经研究了总体规划策略的计算。已经提出了用于表示概括的计划解决方案的不同形式主义以及用于计算它们的不同算法。

宏动作（即动作子序列）是计算一般知识以进行规划的最早建议之一，文献中有几种方法可以用来计算它们[12]，[13]，[14]。但是，由宏操作确定的顺序执行流程通常过于僵化，即使将宏参数化，也必须将它们与控制流结构结合起来，才能推广到更多的规划实例。

广义策略是比宏更为灵活的形式主义。广义策略是将状态和目标映射为操作的一组规则。因此，广义策略是被动的，没有明确表示动作序列。但是，计算好的通用策略很复杂。用于计算广义策略的早期算法[6]，[7]首先计算顺序计划，然后尝试从这些计划中概括策略规则，这是一项艰巨的任务，因为顺序计划中通常会出现大量对称性和易位。而且，不能将广义策略直接添加到领域理论中。但是，存在有效的利用机制通用策略作为特定于域的控制知识（DCK）来指导启发式计划者的搜索过程[15]，[16]。
[^50]: B .
[^51]: A 

用于广义规划的最新算法将规划和归纳紧密地集成在一起，并通过在多个测试用例上对其进行验证来交错编程该解决方案。遵循此方法的工作不仅对领域理论（作用和谓词方案）而且对状态空间[10]或至少观察空间[2]都具有更大的约束，以解决和共享计划任务。这种算法在可能的解决方案空间中进行搜索，并且与SATPLAN方法[17]中的操作类似，该搜索通常与解决方案的最大大小相关联，以使其易于处理。这种方法包括将广义计划任务编译为一致计划任务的工作[2]，CSP [18]或Prolog程序[5]。本文介绍的工作也包括在该小组中。与以前的工作相比，我们的贡献是：1）以程序表示的广义计划对人类高度直观；2）我们可以使用现成的经典计划器来计算广义计划；和3）我们的计划程序形式化可以代表分层和递归解决方案，可以重用现有的广义计划并计算具有高级状态功能的广义计划。

另一种方法是查看单个计划实例，计算一个解决该实例的解决方案，将其归纳，然后将其与先前找到的解决方案合并，从而逐步增加广义计划的覆盖范围。这种方法与以前有关计划修复 [19]和基于案例的计划（CBP）[20]的工作有关，因为它需要确定为什么解决方案不能覆盖给定的实例并使之适应未发现的实例。Distill系统[1]属于这一类别，并且在我们的工作中，使用程序来表示广义的计划。但是，它的表示形式是不同的，并且其性能尚未在各种多样的广义计划任务中进行测试。

事实证明，Golog动作语言家族可用于对能够概括的自主行为进行编程[21] 。除了条件，循环和递归过程外，Golog程序还可以包含不确定部分。Golog程序不需要表示完全指明的解决方案，但它的一个草图，其中非确定性部分是间隙要由系统被填充。在Golog编程人员能够确定预定义的行为，并保留某些部件之间的平衡由系统通过搜索的方式来解决。基本的Golog解释器使用PROLOG回溯机制来解决搜索。该机制基本上相当于盲目搜索，因此，在解决计划任务时，除了最小的实例大小以外，它很快就变得不可行了。IndiGolog [22]扩展了Golog，使其包含许多内置的计划机制。此外，可以利用Golog和PDDL之间的语义兼容性[23]，并且可以嵌入PDDL规划器[24]来解决本质上是组合的子问题。我们定义了自己的编程语言，该语言定义了可能的广义计划的空间。在这种语言中，分支和循环使用相同的构造来实现（条件的getos），以尽可能减少解决方案空间。

Srivastava等人关于广义规划的系列工作。提出具有选择动作的广义计划的表达形式，以决定未来计划步骤[25]，[4]所使用的对象。这些作品中的输入实例被表示为具有传递闭包的抽象一阶表示形式，该表示形式可以表示无数个对象。从此输入计算广义计划的算法实现了自下而上的为现有的部分广义计划确定开放问题类别并有效生成此类的小型实例的策略。该算法从一个空的广义计划开始，并通过识别它无法解决的问题实例，调用经典的计划器来解决该实例，将获得的解决方案归纳并将其合并回广义计划中，从而逐步提高其适用性。重复该过程，直到生成一个涵盖整个所需类实例的广义计划（或达到计算资源的预定义限制时）。尽管这种方法得益于现成的求解器来生成针对特定实例的解决方案，但它仍需要开发特定的技术来概括，调整和合并计划。机器学习（ML）中的训练集。这些输入任务中的每一个都是以PDDL编码的标准经典计划任务。我们采用自顶向下的方法进行广义规划，在单个规划情节中，仅使用现成的经典规划器就可以计算出涵盖所有输入任务的广义规划。

应急计划[26]可以看作是通用计划的一个示例，其中要解决的所有输入实例（1）具有相同的目标，并且（2）被定义为应急计划任务的可能初始状态的集合。偶然性计划者使用状态抽象将可能状态的集合表示为置信状态，并包括根据所感测变量的值划分给定置信状态的检测动作。应急计划可以被视为广义计划。但是，其树状表示形式可能会成倍增长，从而增加了计算此类计划的复杂性。自动计算有限状态机的先前工作（FSM）建议更改应急方案的表示形式，并允许在大大增加应急方案覆盖范围的同时允许回路显着减小应急方案的规模[2]，[9]。生成用于通用计划的高级状态特征还与先前关于一阶MDP的工作有关[27]，[28] 。这些工作使传统的动态编程算法适应符号设置，并通过一阶回归自动生成值函数的一阶表示。在这里，我们的方法的贡献是遵循编译方法，以与现成的计划程序一起生成有用的状态抽象。

从给定的规范合成程序的任务也与我们在广义规划方面的工作有关。在程序综合领域，有两种最近成功的方法：通过示例编程 [29]和通过草图编程 [30]。在示例编程中，使用领域特定的搜索算法生成了一个程序（或一组程序），使其与一组给定的给定输入-输出示例相一致。通过例如著名的编程开发的技术是部分闪光灯补在Excel中，办公室2013年功能在通过绘制编程程序员提供了部分指定的程序，该程序表达了实现的高级结构，但留下了空缺的位置，以代替合成器要填充的低级细节。这种形式的程序合成依赖于用于勾画部分程序的编程语言SKETCH和基于SAT的归纳综合程序，该程序可以有效地从少量测试用例中综合实现。这种方法能够处理嘈杂的示例，并且最近已应用于实现人类性能结果的有监督和无监督的图像分类[31]。

有界综合解决了满足给定LTL公式[32]的有限状态转换系统的综合问题。有界综合的主流方法是将此任务编译为可满足性模理论（SMT）问题。编译需要对系统参数（例如，拒绝状态的数量）确定界限。用我们的方法的主要区别是，我们指定由明确列举了一组测试案例的推广计划应涵盖，类似于机器学习（ML），或解决任务的单元测试在测试驱动开发。

域控制知识是一个通用概念，指的是有关计划解决方案的结构的知识。使用DCK进行计划也可以看作是广义计划的一种形式，它限制了可能的解决方案的空间，但是需要计划者针对特定的经典计划实例生成完全指定的解决方案。该方法包括先前的工作，用于使用控制规则[33]，[34]和分层计划[35]和[36]进行计划。

最后但并非最不重要的一点是，我们用于计算高级状态特征的方法受到版本空间学习的 启发[37]。要学习的假设由具有合取查询形式的逻辑子句组成，并且示例是限制事实的逻辑事实，迫使该假设与示例保持一致。归纳逻辑编程（ILP）[38]也从与ML和逻辑编程相交的示例中生成假设。传统上，ILP被认为是二进制分类任务，但近年来，它涵盖了机器学习的整个范围，例如回归，聚类和关联分析。关于版本空间学习和ILP的方法的主要贡献是使用经典的计划程序来构建和验证学习的假设。
























