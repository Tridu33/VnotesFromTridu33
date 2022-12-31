







1. domain theory，Dana Scott 将可计算性解释为（拓扑）连续性。



2. Stone duality（句法-语义对偶），以及 Makkai 和 Awodey-Forsell 对一阶逻辑的拓展（基于topos理论）。



3. univalent基础的单纯模型（Kapulkin-Lumsdaine-Voevodsky），同伦类型论就发生在数理逻辑与同伦论的交汇处。等等……


https://www.zhihu.com/question/67150635/answer/250108694




Lambda演算的指称语义

•指称语义，又称数学语义：给lambda项提供功能“意义”，即在某个数学论域里对应于某个数学对象。

•如果把所有lambda项的集合定义为X，那么必须要有X->X的函数的集合属于X，违背了集合论的基数性质

•无类型lambda演算的指称语义难以构造


Lambda演算的指称语义

•1969年DanaScott和ChristopherStrachey取得了突破，构造了lambda演算的模型，把lambda项所需要的X->X对象限制为X到X的连续函数上（在特定的Scott拓扑下）

•因此，递归（最小不动点）和数据类型（整型，数组，列表）都有了“含义”

•两人因此获得了图灵奖




https://hopl.info/showlanguage.prx?exp=6953



https://en.wikipedia.org/wiki/Domain_theory





# 1. DomainTheory-Dana Scott


B站讲lambda演算视频的配套pdf：


lambda的语义……domain theory嘛？这方面有哪些书籍呢？谢谢。 
这个最经典的教材，The lambda calculus : its syntax and semantics / H.P. Barend
regt，barendregt大神写的，如果你想了解付型的话也是他的，lambda calculus with types。

























