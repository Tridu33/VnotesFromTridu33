# 栈编程和函数控制流=从 continuation 与 CPS 讲到 call/cc 与协程 




https://www.cnblogs.com/rzbdz/p/15192140.html 
栈编程和函数控制流: 从 continuation 与 CPS 讲到 call/cc 与协程 



CPS 编程本质是基于闭包的无栈编程（当然其解释器如何工作则另说）。

当然程序上的 CPS 变换 太过于复杂，我目前还是先略过，附上论文地址供将来学习魔法的时候异步回调学习。。。。[Representing Control: A study of the CPS transformation ](http://dotat.at/tmp/danvy-filinski-mscs92.pdf)以及一个 PL 课程：PL


「CPST 就是 Gödel–Gentzen 变换的 Curry–Howard 像而已，这有什么难理解的？」 CPS 变换有什么作用？ - Belleve的回答

Curry-Howard Correspondence 是一个理论说命题的证明和程序是同构的，然后 Gödel–Gentzen 变换 不过是逻辑学里的一个定理：对于任意的经典逻辑下的证明，我们可以把它转换为一个直觉主义逻辑下证明而不损失任何证明能力，对于经典逻辑和自觉逻辑的区别请有兴趣的同学自行学习魔法。所以 CPS 变换的一个程序其实是哥德尔-根岑变换这个定理的证明通过 Curry-Howard 同像理论在程序集中的一个对应。


果所有的函数都 CPS 变换后，就能用简单的方法实现一个名为call/cc的在 FP 中实现控制流的函数，这个函数本身是无法用 FP 语言定义的，为了能够理解 call/cc 与 CPS 变换的关系，我们想要知道 call/cc干什么，在那之前我们先学习 C 语言中的一个简化版的 call/cc。













