[Golog] http://www.cs.toronto.edu/cogrobo/main/systems/index.html

[SitCalc] http://en.wikipedia.org/wiki/Situation_calculus

[Haskell] http://www.haskell.org/

[ECLiPSe]  http://www.eclipseclp.org/

[Mercury]  http://www.mercurylang.org/

[prGolog-old]  https://github.com/schwering/prgolog-old

[HP] http://schwering.github.io







https://schwering.github.io/commonsense-2013-slides/#(1)

这个博士后还写了这些内容相关 github 主页都写了


# 1. A Golog Interpreter in Haskell
https://github.com/schwering/golog/tree/master/golog 

这个cabal安装就行


除玩具示例外，它目前还用于交通领域的计划识别和视频游戏TORCS中的赛车控制。

它结合了许多功能：

    过渡语义：可以逐步执行程序。
    标准命令式构造：顺序，循环，if-then-else。
    非确定性构造：分支，通过交错进行并发（可以通过将部分标记为原子来局部限制），以及一些宏，例如从列表中挑选最佳。
    决策理论：不确定性可以通过寻求最高奖励来解决。
    真实世界的效果：使用Haskell的IO系统产生的副作用，可以在线执行具有真实世界效果的动作来执行程序。同样，程序可以首先离线执行（例如，搜索最佳执行），并且结果可以与现实世界同步。
    渐进和回归：解释者对是否使用渐进或回归作为推理机制并不关心。这是解释器隐藏的实现细节。这允许进行非常快速的渐进式BAT！


解释器在Golog.Interpreter中实现。







# 2. Golog in Haskell and a few Aplications

同一个作者github又发布了些demo内容用他写的golog解决situation例子


This is a Golog interpreter written in Haskell and applications of it.
https://github.com/schwering/golog

[Golog](http://www.cs.toronto.edu/cogrobo/main/) is an action language based on
the [situation calculus](http://en.wikipedia.org/wiki/Situation_calculus).
There are many dialects of Golog; this is one of them.

* The [Golog interpreter code](golog/).
* A few [toy examples](golog-examples/) are available.
* A [plan recognition system](plan-recog/), particularly for automotive traffic.
  We model the world with a situation calculus theory and define Golog programs
  which represent typical behavior. The plan recognition system then simulates
  execution of these Golog programs and compares the effects of this simulation
  with observations of the real world.
  [Check out these slides for an overview how it works.](http://schwering.github.io/commonsense-2013-slides/)
* An [agent for a racing car](torcs-agent/).
  The car is controlled by Golog programs and Basic Action Theories.
  This work is at a very early stage.



















































