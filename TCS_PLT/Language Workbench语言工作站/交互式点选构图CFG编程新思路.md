


# 1. 交互式点选构图CFG编程新思路

> 我tridu33有一个梦想 i have a dream：



可视化数据结构，可查看，可编辑的语言工作台，不能只是一个玩具。


New就像编程猫一样点击实现结构化编程

demo直观跟着数字编程

谓词集断言节点状态

点选边上的谓词动作进行编程

改动source code然后debug无误程序的时候，需要点击更新图像一起渲染改动



！直观编程，分层分类


不但为了理解，也是更好分层排除错误


同时，因为parser转换*.smv，可以喂进入NuSMV自动LTL验证"G goalState"是否成立来判断程序是否终止，是否已经考虑到足够多的情况。

把有向无环图CFG转换为树状AST/linear AST-S-expresion/各种各样文本源码/目前最佳源码终点是LLVM-IR和wasm或者是运行在GraalVM通用虚拟机上，这样标准化的流程不但简单方便甚至连后端代码优化都能白嫖LLVM的太棒了。

解析program最直观有效的中间表示将会是**HFSC等CFG控制流图**(况且现在也有商用source code 2 CFG来检查判断的工具)，有了它打通所有关窍脉络(pddl/UML等设计人类方便理解阅读的DSL然后输入需求分析,智能搜索控制指令流(PDDL文法符号自动机planner/solver 或者 Coq等代数推演先设后 或者 B方法之类形式化抽象机自动机推演-->求递归循环不变式指令sequence)得到CFG，coding功能实现，debug调试,valid验证)，毕竟人类的时间最为宝贵，计算机的时间是很廉价的，要让人类方便起来才能充分发挥主观能动性，创意和把精力投入更有意义的方面上研究，这才是进一步丰富补充各种丰富性，发展更好用的语言。




因为有用，人们看到有利可图，才会大力发展其中LTL描述逻辑或者其他的，从编程猫开始的算法题


just Call it Coding Asistant/LeeCode Solver编程助手/LeeCode求解器。































