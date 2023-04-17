




归纳逻辑学习




# ILP

《西瓜书》第五章


实际文献中，我看到很多规划问题都和决策树生成相关，关系relationship数据、决策树等logic意义上的rules学习任务：

>rule learning 规则学习。rules通常是指予以明确，能描述数据分布所隐含的客观规律或领域概念、可写作“若。。。则。。。”形式的逻辑规则《西瓜书》
引用论文的话

一条规则形如$\oplus \leftarrow f_1 \wedge f_2\wedge \text{......}\wedge f_L$
右边body规则体，左边规则头head，

规则体body由文字(literal指原子公式atom及其否定)$f_k$组成的合取范式conjunction,其中合取符号"$\vee$"

head规则头一般也是逻辑文字，表示目标类型或者概念“好瓜”。

这样的logic rules叫做“if-then rules”




序贯覆盖sequential covering逐条归纳，分治separate-andd-conquer策略











典型的一阶逻辑系统由3个组成部分：**实体**，**谓词**和**公式**。




**Entities** are objects x ∈ X. For example, for a given image, a certain region is an entity x, and the set of all possible regions is X. 
 
 **Predicates **are functions that map entities to 0 or 1, for example Person : x 7→ {0,1}, x ∈ X. Classiﬁers can be seen as soft predicates. Predicates can take multiple arguments, e.g. Inside is a predicate with 2 inputs. The number of arguments is referred to as the arity. 
 
 Atom is a predicate symbol applied to a logic variable, e.g. Person(X) and Inside(X,X0). A logic variable such as X can beinstantiatedinto any object inX.
A ﬁrst-order logic (FOL) **formula**is a combination of atoms using logical operations {∧,∨,¬} which correspond to logic and, or and not respectively. 











