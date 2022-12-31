> CHEN: Topos 这一块纯数学里面也很深入了，代数几何里面跟 Grothendieck topology 有关，最开始 Grothendieck 搞这个是为了弄 etale topology，然后证明 Weil 猜想。后来把 topos 用到逻辑里面是 Lawvere 的工作。要学一块的东西很不容易，得有很深的数学背景。
假如要开始学习的话，可以先选择系统地学范畴论，用 Awodey 的就可以了，后面 topos 的有意思的教材我只知道 Johnstone 1977年的一本书跟 Maclane 的 1991 年的书，有需要的话我可以把pdf发到你邮箱里。




如何理解亚历山大·格罗滕迪克？ - 知乎
https://www.zhihu.com/question/26525972/answer/33094038

> 亚历山大·格罗滕迪克格罗滕迪克用代数K理论证明的指标定理是已知最简单的证明，思想内涵完全类比了stokes定理证明：抽象，组合（分解），基元。思想的动机是源自1958年世界数学大会论文――他对于Weil之问的思考的结果：**如何在离散数学数据结构上建立类比连续数学的结论**――这也是希尔伯特的理想（模素理想得到点集拓扑的结论，理想是仿射空间的在点集拓扑意义下的子集，而在点集拓扑基础上就有了微分积分等高级运算――这就是交换代数意义，建立类比点集拓扑理论）


















# Grothendieck-scheme理论
学习代数几何前，为何要先学范畴论？ - CHEN的回答 - 知乎
https://www.zhihu.com/question/404650641/answer/1324818131


Etale Theory I: Etale Cohomology An Introduction - CHEN的文章 - 知乎
https://zhuanlan.zhihu.com/p/364923718
















代数几何里最有名的就是教皇 Grothendieck 了，他构造的scheme就仿佛来自虚空。其实从最开始，至少有两个人想到要给一般的交换环的spec加上Zariski topology，但是他们都放弃了，其中一个是 Wolfgang Krull，不过那时候他在巴黎讲这个的时候被在场的数学家嘲笑，于是他就放弃了这个想法。

Grothendieck 为什么能成功？他把自己的一部分原因归结到范畴论的兴起，迪厄多内也是承认这一点的。事实上最开始Serre在他的FAC里面对于coherent sheaf的探讨是很成功的，不过他所采用的是 etale space 那一套方法，有些基础的证明着实复杂且不清晰，不过他省略了一些繁琐步骤，论文一共83页。Grothendieck在EGA里面明言，说不用etale space，他只用范畴的语言，事实上EGA里面他对sheaf跟presheaf的区分你得自己判别，他不跟你说，因为照那种方法我们不用通过etale space才能把presheaf跟sheaf挂钩，而是可以直接探讨presheaf。于是他用1800页的EGA简化了Serre 83页的FAC。同时利用范畴论可以发现很多以前没发现的东西。

而这一切都是为了解决Weil猜想，Serre告诉Grothendieck，只要在Weil的那个“space”里面建立一个 Lefschetz Fixed Point 成立的上同调理论，那么Weil猜想就可以解决了。Grothendieck直言当时可能只有他跟Serre是确信是存在这样一个上同调理论的。Serre的FAC就是这样的一个尝试，因为他们最开始的想法是通过 sheaf 来建立上同调，使这样的上同调既有同调的信息，也有代数的信息。这种想法在当时很平常，因为嘉当的sheaf cohomology就是既有同调信息也有复分析的信息，就跟de rham cohomology既有同调信息也有微分的信息一样。

但是首先他们要解决的就是Weil构造的那个空间没有分离性质，FAC里面或者说sheaf cohomology的很多结论都得建立在分离性质比如Hausdorff, paracompact等的基础上。这个在流形上是自动满足的，嘉当他们根本不需要考虑这些，可以直接假设空间性质足够好。但是Serre跟Grothendieck不行。Weil的那个空间实在是太差了，甚至定义都不良好，怎么能在上面做同调呢？

后来利用同调代数的工具逐渐把握到 sheaf cohomology跟Cech cohomology的实质跟条件，比如要有acyclic的特殊sheaf，并且可以让任何层都能嵌入这样一个sheaf，这就是injective sheaf。这在Grothendieck的Tohoku里面有充分的讨论。但是这还不行，之前说了Weil猜想的难度在于空间太差了，一般的sheaf cohomology还是得建立在空间上。于是Grothendieck搞出了 Grothendieck topology，而著名的etale topology就是一种特殊的Grothendieck topology。他们不在空间上做同调了，直接在范畴上做。利用这种新的topology，我们可以在范畴里面定义“开集”的概念，那是一组满足某些公理的泛射。这样或许就可以避免使用Weil的空间。事实也是如此。

后面Grothendieck也陆陆续续地发展了topos理论，topos是定义在范畴上的sheaf，而不再像以前那样定义在拓扑空间上了，这个概念具有的优越性是它自带上同调信息。比如所有拓扑空间决定了一个带有sheaf cohomology的topos，所有group决定了一个带有群上同调信息的topos。Serre后来还补充了，所有的profinite group决定了一个带有Galois cohomology信息的topos。Grothendieck之后把topos的思想萌芽归结到了他的Tohoku里面，但那时候应该没有人可以料想到topos。

Grothendieck的工作其实跟各种同调是分不开的，而这一切的基础都是范畴论，而Grothendieck对范畴论不是照搬当时的成果，而是自己去建立一套体系......

我先说交换代数为什么可以是代数几何的基础，最后讲代数几何里面的范畴论。

交换代数是研究交换环的，实际上交换代数主要就应用在代数数论跟代数几何上。我们先讲代数数论上的应用然后再讲代数几何。

它可以用在代数数论上，主要因为 the rings of integral algebraic numbers。举个例子：

Proposition: For a prime number [公式] the following conditions are equivalent:
(i) There exist integers [公式] satisfying [公式] .
(ii) [公式] .

第一个推导第二个是很简单的，第二个推导第一个就难了很多。假设 [公式] ,我们首先把正整数环扩大到高斯环 [公式] 。然后证明高斯环是欧几里得环（带上 [公式] ），因此是主理想环 PID，因此是可分解环（factorial ring）。

由威尔逊定理知道 [公式] 然后设 [公式] 那么在高斯环内， [公式] ，但是 [公式] ,所以 [公式] 在高斯环上不是素的(prime)，因此不是不可约(irreducible),于是我们有 [公式] ,然后 [公式] ，由于素数的性质，我们有 [公式] 。

这里我们最重要的工具高斯环就是一个很特殊的交换环。也正是对像高斯环这样给正整数环 [公式] 再加上n次单位根 [公式] ，所形成的环 [公式] 的研究才有了后面ideal、unique prime factorization等概念。很多后面交换代数的概念跟理论都是由此而来。

至于交换代数在代数几何上的应用，主要是源自下面这个交换环 [公式] ，其中 [公式] 是域。而代数几何主要研究的就是多个多项式的公共零点(代数簇)的性质。可以这么说对多项式环的研究本身就是对代数几何的研究，而研究过程中对更普遍精致的技巧的需求导致了交换代数的产生。下面是非常简略的介绍。

交换代数里面有Hilbert basis theorem就是说 [公式] 是Noetherian Ring, 即该环内任何理想都是有限生成的。这个理论最开始是源自Hilbert对不变量理论的研究，跟他的第十四个问题有关。那时候还没有Noetherian Ring的概念，这个概念是Noetherian在充分洞悉Hilbert最原始的对Hilbert basis theorem的证明后提出来的，要求给环加上一个特殊的公理。同时恰好，这个公理可以很简单地推导出Lasker 原先为多项式环准备的 primary decomposition 。这种公理化不仅普遍了过去数学家对多项式环的研究，而且利用Noetherian Ring的Ascending Chain Condition (ACC)，可以简化很多过去对多项式环性质的证明。

不变量理论：当一个群(群里面的元素可以看成是自同构)作用在一个多项式环上的时候，在群的所有元素作用下保持不变的元素形成多项式环的子代数(子环)，那么该子代数是否总是有限生成的？(反例被Nagata在1959年找到。)


------------------------------------------------------

从上面这些定义就可以看出来**交换代数跟范畴论在代数几何里面的基础作用**。





Algebraic Geometry: The Roots of Scheme I - CHEN的文章 - 知乎
https://zhuanlan.zhihu.com/p/330793163
































