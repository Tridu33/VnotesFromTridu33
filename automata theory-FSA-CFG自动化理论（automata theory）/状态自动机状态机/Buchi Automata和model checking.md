# Buchi Automata和model checking
chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://flolac.iis.sinica.edu.tw/flolac09/lib/exe/buechi_automata_4on1.pdf
B ̈uchi Automata and Model Checking PPT

https://github.com/topics/buchi-automaton

https://github.com/rbouar/LTL-to-BA
https://github.com/Axolottl/LTL_to_GBA
LTL to Büchi Automata Translation: Fast and More Deterministic https://arxiv.org/abs/1201.0682
http://jst.tsinghuajournals.com/article/2014/1000-0054/1000-0054-54-2-281.html 线性时序逻辑转换Büchi自动机的按需即时算法

线性时间不动点公式（某些人称其逻辑为 TL）和Buechi自动机的构造等价性是Mads Dam在1992年发表的一篇论文 
《Buchi Automata的不动点》，FST＆TCS 1992。
给出的.有关从Buechi自动机构造 TL公式的信息，请参见第4页。从 TL公式构造Buechi自动机更为复杂，并占用了本文的其余部分。该答复的其余部分只是一个简短的论点，即该结果以远不那么直接的形式存在于文献中。皮埃尔·沃尔珀（Pierre Wolper）表明，存在不能由LTL定义的欧米茄常规特性，并扩展了可以表达欧米茄常规特性的LTL（称为ETL）。时间逻辑可以更具表现力，皮埃尔·沃尔珀（Pierre Wolper），《信息与计算》，1983年。
还众所周知，可以将ETL公式转换为 TL公式，因此，通过组合这些结果，您可以将Buechi自动机的翻译结果读取为

Büchi自动机和线性微积分的等价性 
众所周知，每个LTL公式都可以由Büchi -automaton表示。但是，很明显，Büchi自动机是一种功能更强大的表达模型。我在某处听说过Büchi自动机等效于线性时间 -calculus（即具有常规固定点且只有一个时间运算符 -calculus ）。

hal.archives-ouvertes.fr/docs/00/06/06/08/PDF/LogicOnWords.pdf-尽管我本人不是专家并且尚未完全了解代数，但本文对我来说是一个很好的起点语言的自动机方法。ωω

NBA相当于MSO


常规语言，DFA，NFA和NBA 在字符串上的MSO等效，但在一般意义上（在任意结构上）不等同于MSO。实际上，在字符串上考虑时，二阶逻辑（SO）也等效于单子二阶逻辑（MSO），但SO通常比LTL更具表现力。




LTLNFBA:LTL公式到Büchi自动机的转换
http://cdmd.cnki.com.cn/article/cdmd-10701-1015437406.htm
模型检测是提高软硬件系统可靠性的重要途径.它的基本思想是使用一个时序逻辑公式描述系统期望的性质,使用一个Buchi自动机描述系统的模型,然后将描述性质的时序逻辑公式取非,并转换为一个等价的Buchi自动机.最后将两个Buchi自动机求交,判断交集是否为空.如果为空,则表明系统满足期望的性质;否则,系统不满足期望的性质,并输出反例.线性时序逻辑LTL是模型检测中常用的性质描述语言之一.因此,LTL公式到Buchi自动机的转换是LTL模型检测的关键步骤,转换算法的好坏直接影响着LTL模型检测工具的效率.目前,经典的转换算法包括Gerth等人提出的on-the-fly直接转换算法和Gastin和Oddoux提出的基于VWAA的转换算法.尽管这些算法已经在一些模型检测工具中得到应用,但是对于规模较大,结构较复杂的公式,目前的转换工具都无能为力.为了克服以上问题,本文给出了基于CF范式的转换算法.同时,利用了alternating公式的性质,在算法之中加入了一些相应的改进措施,提高了算法的实用性.另外,利用了有向图中强连通分量的特性,改进了自动机的简化方法,使得最后得到的Buchi自动机规模减小.在以上算法的基础上,开发了LTL公式到Buchi自动机的转换工具LTLNFBA,并与目前国际上处于领先地位的两个同类工具LTL3BA和SPOT进行比较.实验结果表明LTLNFBA在多数情况下转换效率优于其他两个工具.





----------------------------------------------

程序的终止性一直是计算机科学领域研究的热点。一般的程序终止性问题也可规约为图灵机的停机问题。由于图灵机的停机问题不可判定，所以程序的终止性问题也没有通用完备的算法来求解。于是很多科学家从而关注于提出部分正确却不完备的算法来判断一个输入程序是否终止，即通过程序秩函数(ranking function)的存在性来证明程序是否可以终止，如果秩函数存在，则表明返回程序终止，否则程序终止性未知。

2014年德国学者Matthias Heizmann等人提出使用Buchi自动机对程序进行建模，并通过采样的方法对Buchi自动机里面的路径进行采样来逐条通过秩函数的方式证明路径的终止性。证明终止的路径会经过扩展为Buchi自动机之后从原自动机里面删除，当路径全部删除时即证明了程序可终止。此方法是当前最好的程序终止性证明算法，实现此方法的工具Ultimate也是2017年SV-COMP比赛终止性类别的冠军。





