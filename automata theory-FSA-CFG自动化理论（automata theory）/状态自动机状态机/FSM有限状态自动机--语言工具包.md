[TOC]



学习有限自动机后，我应该得到什么启示？

https://qastack.cn/cstheory/14811/what-is-the-enlightenment-im-supposed-to-attain-after-studying-finite-automata












# FSM有限状态自动机

有限状态机（英语：finite-state machine，缩写：FSM）又称有限状态自动机，简称状态机，是表示有限个状态以及在这些状态之间的转移和动作等行为的数学模型。

状态存储关于过去的信息，就是说：它反映从系统开始到现在时刻的输入变化。转移指示状态变更，并且用必须满足确使转移发生的条件来描述它。动作是在给定时刻要进行的活动的描述。有多种类型的动作：

进入动作（entry action）：在进入状态时进行
退出动作：在退出状态时进行
输入动作：依赖于当前状态和输入条件进行
转移动作：在进行特定转移时进行








《Programming Game AI by Example》 C++编写一个有限状态自动机
https://shiheuan.github.io/2019/05/21/FSM_1/

一个**有限状态机的 C++ 实现:** https://www.infoq.cn/article/ft3j9sxtc0ugdbydlzxp https://github.com/DavidLiuXh/kuafu



1.根据业务需要, 拆解抽象出若干个不同状态 State, 并确定此状态机的初始状态;



2 根据实现需要, 抽象出用于触发状态转换的事件 Event;



3.为了处理一个 Event, 需要定义状态的转换过程 Transition;



4.状态机要先判断当前所处的状态是否与当前发生的 Event 匹配(注意: 相同的状态可能同时匹配多个 Event)。










**Javascript Finite State Machine**  ： https://segmentfault.com/a/1190000017328171 很详细的一个js包

>MTP-2，MTP-3，TUP，ISUP，SCCP，TCAP，MAP，Q.921，Q.931，SIP，H.323... 所有的协议定义都有明确的“有限状态机”设计。为了有效地描述使用“有限状态机”，国际电信联盟专门出台了一套标准——规格描述语言SDL（Specification and Description Language）。



**python fsm**:

https://www.python-course.eu/finite_state_machine.php python状态机简易教程

包

```python 
pip install finite-state-machine
```

https://pypi.org/project/finite-state-machine/

Python中的轻量级，面向对象的有限状态机实现，具有许多扩展（transitions）样例很详细很复杂 ;https://github.com/pytransitions/transitions


**Go FSM**
blog.csdn.net/frank3g/article/details/6653943  讲解简单实现

blog.csdn.net/weixin_43672855/article/details/105829182 源码框架

建模到代码详解案例看这个 jianshu.com/p/37281543f506



































































































