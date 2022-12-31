
?
如何用矩阵表示一个布尔逻辑fol解析的NFA迁移系统，
然后计算其矩阵不变量和“软件不变量”逻辑公式
的关联?
得到程序综合?
马尔可夫决策过程，强化学习是一个路子，有更准确的吗？无脑fond分支均等概率归一化每一行，保证公平性假设能出去？


# NFA软件不变量有向图矩阵表示高等代数

相同的『数学逻辑运算』，通过笔算，自然语言运算，程序设计语言表示/运算，通过CPU算，通过FPGA算，只不过是状态的『寻址方式』『表示方式』不同（笔算靠笔记和脑子寻址，程序设计语言是通过“变量名”寻址，FPGA通过内部复杂网络寻址，CPU通过寄存器和内存空间寻址...），具体的『映射变换的实现载体』不同而已。最后可能结果的输出“形式”不同而已。

**基于动态分析的软件不变量综合技术**
www.jos.org.cn/html/2020/6/6014.htm


麻省理工18年春软件构造课程阅读11“**抽象函数与表示不变量** ...
https://www.cnblogs.com/liqiuhao/p/8688759.html



软件不变量(software invariant, 以下简称为不变量)是软件运行时在程序某位置必须保持的属性(property).不变量可以有多种表现形式, 例如前条件(pre-condition)与后条件(post-condition)、循环不变量(loop invariant)、断言(assertion)、在面向对象语言中描述对象属性的类不变量(class invariant)以及描述对象之间关系的结构不变量(structural invariant)等等.

**不变量**被广泛应用在程序验证、程序理解、程序优化、程序维护、程序缺陷定位以及程序缺陷修复等领域.一般而言, 不变量可以被编码为逻辑表达式, 从而使用数理逻辑手段进行演算.例如在程序验证中, 不变量可以视为规约(specification), 通过把程序的语义转化为逻辑表达式, 可以使用霍尔逻辑进行演算来验证程序是否满足规约.由于不变量是软件属性的高度抽象, 人工构造不变量非常繁琐复杂, 因此开发人员一般采用软件分析(program analysis)的方法从软件中自动地综合(synthesize)不变量.

不变量理论 https://zh.wikipedia.org/zh-cn/%E4%B8%8D%E5%8F%98%E9%87%8F%E7%90%86%E8%AE%BA


http://www.jos.org.cn/html/2020/6/6014.htm
bonet文中学习逻辑软件不变量就是fond本质：feature learnning
《Guarantees for Sound Abstractions for Generalized Planning》


https://www.sciencedirect.com/science/article/pii/0001870870900150
不变量,变换系统的本质属性


## 自动机形式化为FOL再写成网络结构

为什么都说神经网络是个黑箱？ - Moenova的回答 - 知乎
https://www.zhihu.com/question/263672028/answer/2250289371


Warren S. McCulloch and Walter Pitts. A logical calculus of the ideas immanent in nervous activity. Bulletin of mathematical biophysics, vol. 5 (1943), pp. 115–133.


Computing First-Order Logic Programsby Fibring Artificial Neural Networks 例解

First-order Logic Learning in Artificial Neural Networks

Connectionist Model Generation_ A First-Order Approach


https://github.com/utahnlp/layer_augmentation
Augmenting Neural Networks with First-order Logic
今天，训练神经网络的主要范式涉及最大限度地减少大型数据集上的任务损失。使用世界知识为模型提供信息，同时保留执行端到端训练的能力仍然是一个悬而未决的问题。在本文中，我们提出了一种新的框架，用于将声明性知识引入神经网络架构，以指导训练和预测。我们的框架系统地将逻辑语句编译成计算图，无需额外的可学习参数或手动重新设计即可增强神经网络。我们在三个任务上评估我们的建模策略：机器理解、自然语言推理和文本分块。我们的实验表明，知识增强网络可以大大提高基线，尤其是在低数据情况下。

## 特征学习 高阶布尔变量抽象解释


**DEEPCODER: LEARNING  TOWRITEPROGRAMS**


 Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard S. Zemel.  Gated graph sequence neuralnetworks. InProceedings of the 4th International Conference on Learning Representations (ICLR),2016. 
 
graph neuralnetworks (GNNs) to predict logical descriptions from program states, focusing on data structureshapes instead of numerical and list data. Such GNNs may be a suitable architecture to encode statesappearing when extending our DSL to handle more complex data structures.












## 二值化网络
Rule Extraction From Binary Neural Networks With Convolutional Rules for Model Validation

 we propose an algorithm for decompositional rule extraction (Andrews et al., 1995), called Deep Convolutional DNF Learner (DCDL). A BNN takes binary input and only produces binary outputs in all hidden layers as well as the output layer. 











## 矩阵有向图
图论--图的特征值与图的群表示 - 知乎
https://zhuanlan.zhihu.com/p/404049045




Towards Learning From Graph Representable Formal Models
ceur-ws.org/Vol-2987/paper12.pdf

https://blog.csdn.net/qq_41033507/article/details/105785661
dfanfa

状态迁移矩阵

Reducing NFAs by invariant equivalences | Request PDF
https://www.researchgate.net/publication/220154095...

## SMT

可满足性模块理论(SMT)基础 - 01 - 自动机和斯皮尔伯格算术 ...
https://cloud.tencent.com/developer/article/1127594








## Regex2NFA2DFA
: 编译原理实验1，由正规式生成NFA ...
https://gitee.com/Morphlng/regex2-nfa2-dfa




- 正规表达式转NFA(C++)
https://blog.csdn.net/to_be_better/article/details/52721920



## AC自动机

https://blog.csdn.net/bestsort/article/details/82947639
ac自动机

https://www.cnblogs.com/sduwh/p/13765634.html
其实Ac自动机的Tire树就是一个状态转移图，构造出状态转移矩阵， Mij 表示从Tire树上的第 i 个节点转移到 j 节点的方案数， Mn 就是长度为 n 的串的状态转移矩阵



双数组Trie树与AC自动机简要总结 - 云+社区 - 腾讯云
https://cloud.tencent.com/developer/article/1530997















# 强化学习  马尔可夫链和转移概率矩阵
https://www.cnblogs.com/wlw-x/p/12269114.html


马尔可夫过程中的状态转移矩阵有什么意义？本质内涵是什么呢？ - 知乎
https://www.zhihu.com/question/41423304







https://blog.csdn.net/weixin_44995665/article/details/100804593 计算机CV视觉中的不变量

