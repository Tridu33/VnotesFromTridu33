# NLIL

**The goal of NLIL is to generate data-independent FOL rules.**

LEARN TO EXPLAIN EFFICIENTLY VIA NEURAL LOGIC INDUCTIVE LEARNING

https://github.com/gblackout/NLIL


Baselines: For NeuralLP, we use the ofﬁcial implementation at here. For ∂ILP, we use the thirdparty implementation at here. For TransE, we use the implementation at here. For RotatE, we use the ofﬁcial implementation athere.

https://github.com/fanyangxyz/Neural-LP

https://github.com/ai-systems/DILP-Core

https://github.com/thunlp/KB2E

https://github.com/DeepGraphLearning/KnowledgeGraphEmbedding




















 Neural Logic Inductive Learning (**NLIL( Neural Logic Inductive Learning )**), an efﬁcient differentiable **ILP( inductive logic programming )** framework that learns ﬁrst-order logic rules that can explain the patterns in the data.

近年来，见证了深度学习模型在各种应用中的日益增长的成功。然而，这些模型也因其行为和决策过程缺乏可解释性而受到批评（Lipton，2016 ; Mittelstadt等，2019 ），
>Ali Payani and Faramarz Fekri. Inductive logic programming via differentiable deep neural logic networks. arXiv preprint arXiv:1906.03523, 2019. 
>Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why should i trust you?: Explaining the predictions of any classiﬁer. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, pp. 1135–1144. ACM, 2016.

并且数据量大。解释其决策的能力对于开发负责任且强大的决策系统至关重要（Guidotti et al。，2019）。
>Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. A survey of methods for explaining black box models. ACM computing surveys (CSUR), 51(5):93, 2019.

另一方面，以一阶逻辑（FOL）形式的逻辑编程方法能够发现和表示人类可以理解和检查的显式符号结构中的知识（**Evans＆Grefenstette，2018(总引用这篇，作者是看着文章发展的)**）。
>Richard Evans and Edward Grefenstette. Learning explanatory rules from noisy data. Journal of Artiﬁcial Intelligence Research, 61:1–64, 2018.


在本文中，我们调查了在归纳逻辑编程（ILP）范围内学习解释问题的学习，该过程旨在学习解释数据的一阶逻辑规则。传统的ILP方法（Galarraga等人，2015）
>Luis Gal´arraga, Christina Teﬂioudi, Katja Hose, and Fabian M Suchanek. Fast rule mining in ontologicalknowledgebaseswithamie+. TheVLDBJournalTheInternationalJournalonVeryLarge Data Bases, 24(6):707–730, 2015.

依靠硬匹配和离散逻辑进行规则搜索，这对于模棱两可和嘈杂的数据是不容许的（Evans＆Grefenstette，2018 ）。提出了许多工作来开发可区分的ILP模型，这些模型结合了基于神经和逻辑的计算能力（Evans和Grefenstette，2018; Campero等人，2018; Rocktaschel和Riedel，2017 ;  Payani和Fekri，2019 ; Dong等人）等（2019）。
>


## ILP
归纳逻辑编程（ILP）旨在总结数据中共享的底层模式，并将其表达为一组逻辑程序（或规则/公式）（Lavrac＆Dzeroski，1994）。
传统的ILP方法（例如AMIE +（Gal´arraga等人，2015）和RLvLR（Omran等人，2018））依赖于基于显式搜索的规则，并使用各种修剪技术进行挖矿。
这些作品可以扩展到非常大的知识库。
但是，算法复杂度随着所涉及的变量和谓词的大小呈指数增长。
获得的规则通常限于最大长度小于3的Horn子句，从而限制了规则的表达性。
另一方面，与可微方法相比，传统方法利用硬匹配和离散逻辑进行规则搜索，缺乏对模棱两可和嘈杂数据的容忍度。







**正向链接方法(forward-chainingmethods)**等方法ILP （Evans＆Grefenstette，2018）。

它使用一组预定义的模板构造规则，并且通过将规则多次应用于背景数据来评估它们，以推断出保留集中的新事实（相关工作可在**附录A**中找到）。

**Backward-chaining methods**(e.g NTP)
· Learn explicit rules
· Efficient
· Template based

**Others(e.g NLM)**
· Learn implicitly rules· Exponential complexity


但是，一般的ILP问题涉及NP难的几个步骤：

（i）规则搜索空间在规则的长度上呈指数增长；

（ii）分配要由谓词共享的逻辑变量时，参数的数量呈指数增长，这称为变量绑定问题；
（iii）规则实例化的数量公式评估所需的数据量呈指数增长。为了减轻这些复杂性，大多数工作都将搜索长度限制在3以内，并且诉诸于基于模板的变量分配，从而限制了所学规则的表达能力（详细讨论可参见附录B）。尽管如此，大多数工作仍然限于关系少于10个和1K实体的小规模问题。

>标准的ILP方法是困难的，并且涉及已被证明是NP难的几种程序。
复杂性来自3个级别：首先，公式的搜索空间很大。
零售主体可以承受任意长的时间，并且同一谓词可能多次出现，且具有不同的变量，例如，式（2）中的内部谓词出现两次。
大多数ILP工作都将逻辑蕴含约束为Horn子句，即，蕴涵的主体是文字之上的扁平连词，对于大型数据集，其长度限制在3以内。
其次，构造公式还涉及分配不同谓词共享的逻辑变量，我们将其称为可变绑定。
例如，在等式（2）中，表达“某人”在车内，我们用“ X”和“ Y”代表一个人和某车的区域，“内部”中使用两个相同的变量来表达它们之间的关系。
不同的绑定导致不同的含义。
带有参数的公式（等式（2）有7），可能有O（nn）个赋值。
现有的ILP可以通过预先定义的模板（Evans＆Grefenstette，2018; Campero等，2018）或类似链的变量引用（Yang等，2017）来构造公式，从而限制了学习规则的表达能力。
最后，评估公式候选者很昂贵。 
FOL规则与数据无关。
为了对其进行评估，需要用实际实体替换变量并计算其值。
这称为接地或实例化。
公式中使用的每个变量都可以独立接地，这意味着可以将具有n个变量的公式实例化为O（Cn）接地公式，其中C是总数。
例如，公式（2）包含3个逻辑变量：X，Y和Z。
为了评估该公式，需要将这些变量实例化为C3可能的组合，并检查每种情况下该规则是否成立。
然而，在许多领域中，例如物体检测，这样的接地空间是巨大的（例如，图像的所有可能的边界框），使得全面评估是不可行的。 
forILP（Evans＆Grefenstette，2018）等许多前向链接方法在接地空间的大小上呈指数级扩展，因此仅限于少于10个谓词和1K个实体的小规模数据集。


另一方面，针对知识库提出了**多跳推理方法( multi-hop reasoning methods )**（Guu等人，2015; Lao＆Cohen，2010; Lin等人， 2015; Gardner＆Mitchell，2015; Das等人，2016）**知识库（KB）**完成任务。

**NeuralLP **等方法（Yang等人，2017）可以通过搜索从主题到对象的关系路径来回答知识库查询。可以在ILP域中解释这些方法，在该ILP域中，学习的关系路径等效于类似链的一阶规则。与基于emplate-basedcounterparts（模板的对应物）相比，诸如NeuralLP的方法在变量绑定和规则评估中非常高效。但是，它们在两个方面受到限制：

（i）链状规则代表Horn子句的子集，并且在表达复杂的规则（例如图1中所示的规则）时受到限制；

（ii）在以特定查询为条件时生成关系路径，这意味着学习的规则仅对当前查询有效。这使得学习知识库中全局一致的规则变得困难，这是良好解释的重要方面。


在这项工作中，我们提出了神经逻辑归纳学习（NLIL），这是一种可微分的ILP方法，该方法扩展了针对一般ILP问题的多跳推理框架。NLIL高效且富有表现力。我们提出了分而治之的策略，并将搜索空间分解为一个层次结构中的3个子空间，每个子空间都可以通过注意力高效地进行搜索。这样一来，我们搜索规则的时间将是最新方法的10倍，而保留时间则是最新方法的3倍。通过将训练划分为规则生成和规则评估阶段，我们可以保持规则的全局一致性，其中前者仅以全局共享的谓词类型为条件。


更重要的是，我们证明了可扩展的ILP方法广泛适用于监督学习场景中的模型解释。我们将NLIL应用于视觉基因组（Krishna et al。，2016）数据集，以学习有关1M实体上150个对象类别的解释。我们证明，所学规则在保持可解释性的同时，具有与密集监督模型相当的预测能力，并且可以用不到1％的数据很好地概括。




The ILP problem is closely related to the multi-hop reasoning task on the knowledge graph (Guu et al., 2015; Lao & Cohen, 2010; Lin et al., 2015; Gardner & Mitchell, 2015; Das et al., 2016). Similar to ILP, the task operates on a KB that consists of a set of predicates P. 

但是，（P1）生成監督模型的解釋對規則的表達性提出了很高的要求。
鏈狀規則空間的表達能力受到限制，因為它代表了Horn子句規則空間的約束子空間。

例如，等式（2）是Horn子句，並且不是鏈狀的。
在這些方法中仍然缺乏有效搜索超出鏈狀規則空間的能力。
另一方面，（P2）注意生成器T（x; w）依賴於特定查詢q的主題x，這意味著針對目標P ∗生成的解釋可能因查詢而異。
這使得很難學習KB中全局一致的FOL規則。

![](_v_images/1596765727_8836.png)









# 规则生成的分层转换器网络



![](_v_images/1596773599_17010.png)










































































































