# Okasaki以来，纯功能数据结构有何新变化





https://qastack.cn/cstheory/1539/whats-new-in-purely-functional-data-structures-since-okasaki







自1998年以来发布的新的纯功能数据结构：
2001年：理想哈希树及其2000年的前身，《快速与节省空间的特里搜索》，作者：Phil Bagwell：显然是Clojure标准库中的基本构建块。

2001：优先搜索队列的简单实现技术，作者：拉尔夫·欣兹（Ralf Hinze）：一种非常简单而优美的技术，用于实现这一重要的数据结构（在Dijkstra算法中很有用）。由于大量使用“视图模式”，因此该实现特别美观且可读。

2002年：拉尔夫·辛兹（Ralf Hinze）引导了一侧灵活的阵列：与Okasaki的随机访问列表类似，但是可以对其进行调整，以改变cons索引之间的时间折衷。

2003年：拉杜·米哈埃斯库（Radu Mihaescu）和罗伯特·塔里扬（Robert Tarjan）提出了可处理和不可分类的双端队列：冈崎（Kaplan＆Tarjan）引用了一些较旧的作品（卡普兰和塔里扬的作品）的新观点（卡普兰和塔里扬作品的最新版本于2000年出版）。此版本在某些方面更简单。

2005年：克里斯·冈崎（Chris Okasaki）撰写的Maxiphobic堆（纸和代码）：并不是作为一种新的，更有效的结构出现，而是作为一种教导优先级队列的方法。

2006：GerthStøltingBrodal，Christos Makris和Kostas Tsichlas撰写的《纯功能最坏情况下恒定时间可排序表》：通过展示具有O（lg n）插入，搜索和删除以及O的结构，回答了Kaplan和Tarjan的一个悬而未决的问题（1）连环。

2008年：有效版本控制的融合持久性尝试，作者：Erik D. Demaine，Stefan Langerman和Eric Price：介绍了几种数据结构，这些结构可在叶子附近进行有效导航和修改。有些纯粹是功能性的。Dietz等人实际上改善了长期存在的数据结构。用于完全持久（但不是融合持久或纯功能）的数组。本文还介绍了纯功能的链接剪切树，有时也称为“动态树”。

2010：Matt Might提出的一种新的纯功能性红黑树删除算法：与Okasaki的红黑树插入算法一样，这不是新的数据结构也不是对数据结构的新操作，而是一种新的，更简单的方法写一个已知的操作。

2012：RRB树：高效不可变向量，作者：Phil Bagwell和Tiark Rompf：对哈希数组映射尝试的扩展，支持不可变向量连接，insert-at和O（lg n）时间分割，同时保持索引，更新，以及原始不变向量的插入速度。

于1997年已知，但在Okasaki的书中没有讨论：
平衡搜索树的许多其他样式。AVL，兄弟，等级平衡，有界平衡和许多其他平衡搜索树可以（并且已经）通过路径复制纯粹在功能上实现。也许值得特别提及的是：

偏向搜索树，由Samuel W. Bent，Daniel D. Sleator和Robert E. Tarjan撰写：Brodal等人2006年论文和Demaine等人2008年论文中的关键要素。
MartínEscardó 提出的允许快速穷举搜索的无穷集：也许本身不是数据结构。

克里斯·奥卡萨基（Chris Okasaki）的三种关于Braun树的算法：Braun树在最坏情况下的O（lg n）中提供了许多堆栈操作。许多其他数据结构都超越了这个界限，但是Braun树cons的第二个参数中有一个懒惰的运算，因此可以以其他结构无法使用的某些方式用作无限堆栈。

轻松的最小-最大堆：可合并的双端优先级队列和KD堆：高效的多维优先级队列，作者：Yuzheng Ding和Mark Allen Weiss：尽管它们未在本文中讨论，但它们恰好是纯功能的。 。我认为实现的时限没有比使用手指树（Hinze和Paterson或Kaplan和Tarjan的树）作为k维优先级队列所能实现的时域更好，但我认为Ding＆Weiss的结构使用的空间更少。

拉链，作者GérardHuet：在许多其他数据结构（例如Hinze和Paterson的手指树）中使用，这是一种将数据结构由内向外的方式。

差异列表是O（1）可连接列表，其中O（n）转换为普通cons列表。自Prolog上古以来，它们显然已广为人知，在那里他们可以将O（1）转换为常规cons列表。O（1）转换在传统的函数编程中似乎是不可能的，但是来自POPL '98的Minamide的hole抽象讨论了一种允许在纯函数编程中进行O（1）追加和O（1）转换的方法。与基于功能闭包的差异列表的常规功能编程实现不同，孔抽象与Prolog差异列表本质上相同（在使用和实现方面）。但是，似乎多年来，唯一注意到这一点的人是Minamide的审阅者之一。

唯一表示的字典支持插入，更新和查找，但要注意的是，任何两个包含相同元素的结构都不能具有不同的形状。举个例子，排序后的单链接列表被唯一表示，而传统的AVL树则没有。尝试也有独特的代表。Tarjan和Sundar在“唯一的二叉搜索树表示形式以及集合和序列的相等性测试”中，展示了一种纯功能唯一表示的字典，该字典支持对数时间的搜索和时间的更新。但是，它使用空间。有一个使用Braun树的简单表示形式，它仅使用线性空间，但更新时间为O(n−−√)O(n)Θ(nlgn)Θ(nlg⁡n)Θ(nlgn−−−−−√)Θ(nlg⁡n)和搜索时间Θ(lg2n)Θ(lg2⁡n)
在Okasaki的书之前，之中和之后的大多数为功能性数据结构：
使数据结构具有持久性，完全持久性或融合持久性的许多过程：Haim Kaplan 对该主题进行了出色的调查。另请参见上文Demaine等人的工作，他们演示了空间中的完全持久性数组（其中是该数组上曾经执行的操作数）和预期访问时间。O(m)O(m)mmO(lglgn)O(lg⁡lg⁡n)
1989年：塞西莉亚·阿拉贡（Cecilia R. Aragon）和莱蒙德·塞德尔（Raimund Seidel）的随机搜索树：在纯功能设置中，盖伊E. Blelloch和玛格丽特·里德-米勒在使用Treaps进行快速设置操作中进行了讨论 ，而丹·布兰福德和盖伊·布莱洛奇在功能集操作中使用了陷阱（代码）。它们提供了纯功能指状树和有偏性搜索树的所有操作，但是需要随机性，这使得它们不完全是功能性的。假设对手可以计时操作并重复长时间操作，这也可能使对挖掘操作的时间复杂度无效。（这与为什么强制性摊销参数在持久性设置中无效的原因相同，但它要求对手使用秒表）

1997年：“ 跳过树”，这是Xavier Messeguer 并发方法中“跳过列表”的替代数据结构，作者是 Brian C. Dean和Zachary H.Jones着的《探索跳过列表和二进制搜索树之间的对偶》，这并不是单纯的跳过列表功能，但是它们可以在功能上实现为树。像开挖一样，它们需要一个随机位源。（可以使确定性确定列表成为可能，但是将它们转换为树后，我认为它们只是查看2-3棵树的另一种方式。）

1998年：冈崎书记中所有摊销的结构！Okasaki发明了这种用于混合摊销和功能数据结构的新方法，这些方法以前被认为是不兼容的。正如Kaplan和Tarjan有时提到的那样，这取决于副作用，实际上是副作用。在某些情况下（例如出于性能原因在SSD上使用PFDS），这可能是不合适的。

1998年：Haim Kaplan，Chris Okasaki和Robert E. Tarjan 撰写的Simple Confluently Persistent Catenable Lists：在引擎盖下使用修改以提供可摊销的O（1）可绑定双端队列，并提供了与早期版本相同的接口（纯功能，但带有备忘录） ）版本出现在Okasaki的书中。Kaplan和Tarjan早先创建了一个纯功能性的O（1）最坏情况结构，但实际上要复杂得多。

2007年：如本页上的另一个答案所述，Sylvain Conchon和Jean-ChristopheFilliâtre提出了半永久性数据结构和持久性联合发现

在Okasaki的书之前，之中和之后验证功能数据结构的技术：
幻像类型是一种旧的创建API的方法，该API不允许某些格式错误的操作。在Oleg Kiselyov和Chung-chieh Shan的“ 轻型静态功能”中可以找到它们的复杂用法。

嵌套类型实际上并不比1998年更新-冈崎甚至在他的书中使用了它们。冈崎的书中没有很多其他的例子。有些是新的，有些是旧的。他们包括：

斯特凡·卡尔斯的红黑树与类型（代码）
罗斯·帕特森（Ross Paterson）的AVL树（镜子）
克里斯·冈崎（Chris Okasaki）的《从快速取幂到方阵：类型上的冒险》
理查德·伯德和罗斯·彼得森的de Bruijn表示法为嵌套数据类型
Ralf Hinze的数值表示形式为高阶嵌套数据类型。
GADT也不是那么新。它们是Haskell和某些ML的最新成员，但我认为，自1970年代以来，它们就以各种类型的Lambda结石存在。

2004-2010：Coq和Isabelle的正确性。一些人已经使用定理证明者来验证纯功能数据结构的正确性。Coq可以将这些验证提取到Haskell，OCaml和Scheme中的工作代码中；Isabelle可以提取到Haskell，ML和OCaml。

辅酶Q：
Pierre Letouzey和Jean-ChristopheFilliâtre 对红黑树和AVL（ish）树进行了形式化处理，并在此过程中在OCaml标准库中发现了一个错误。
我正式确定了Brodal和Okasaki的渐近最优优先级队列。
亚瑟·夏格罗（ArthurCharguéraud）在Okasaki的书中正式确定了ML的1,700行中的825行。
伊莎贝尔：
Tobias Nipkow和Cornelia Pusch 将AVL树正式化。
Viktor Kuncak形式化了不平衡的二叉搜索树。
彼得·拉米奇（Peter Lammich）发布了《伊莎贝尔收藏集》框架，其中包括高效的纯功能数据结构的形式化，例如红黑树和尝试，以及持久使用时效率较低的数据结构，例如两个堆栈队列（没有冈崎的懒惰技巧） ）和哈希表。
彼得·拉米奇（Peter Lammich）还发布了树自动机，Hinze＆Patterson的手指树（与Benedikt Nordhoff和StefanKörner一起）以及Brodal和Okasaki的纯粹功能优先队列（与Rene Meis和Finn Nielsen）的形式化。
RenéNeumann正式确定了二项式优先级队列。
2007年：Joshua Dunfield 撰写的“使用Stardust进行细化类型检查”：本文使用ML的细化类型来查找SMLNJ的红黑树删除功能中的错误。

2008年：Nils Anders Danielsson 对纯功能数据结构的轻型半形式时间复杂度分析：使用带有手动注释的Agda来证明某些PFDS的时限。

命令性数据结构或分析在Okasaki的书中没有讨论，但与纯功能数据结构有关：
软堆：具有最佳错误率的近似优先级队列，作者：Bernard Chazelle：此数据结构不使用数组，因此首先尝试使用#haskell IRC通道，然后尝试使用 Stack Overflow用户，但它包含delete在o（lg n）中，通常在功能设置中是不可能的，而命令式摊销分析在纯功能设置中是无效的。

具有O（1）手指更新的平衡二进制搜索树。James R Driscoll，Neil Sarnak，Daniel D.Sleator和Robert E.Tarjan 在“ 使数据结构具有持久性”中提出了一种在红黑树中对节点进行分组的方法，以便持久性更新仅需要O（1）空间。Tarjan，Kaplan和Mihaescu设计的纯功能双端队列和手指树都使用非常相似的分组技术来允许两端的O（1）更新。Athanasios K. Tsakalidis 用于本地搜索的AVL树的工作方式与此类似。

更快配对堆或更好的界限进行配对堆：由于Okasaki的书出版，必须配对堆了一些新的分析已经出现，包括带O配对堆（日志log n）的降低成本的阿姆鲁Elmasry和迈向配对堆的最终分析通过塞思·佩蒂（Seth Pettie）。可以将其中一些工作应用到冈崎的懒惰配对堆中。

确定性偏向手指树：在偏跳跃列表，弥陀经巴什，亚当L. Buchsbaum，和Michael T.古德里奇，提出了一种确定性的偏见跳表的设计。通过上面提到的跳过列表/树转换，有可能制作确定性有偏向的搜索树。由John Iacono和ÖzgürÖzkan在“可合并字典”中描述的手指偏向跳过列表然后可能在偏向跳过树上出现。Demaine等人提出了一种有偏见的手指树。在他们关于纯功能性尝试的论文中（见上文），作为一种减少尝试中手指更新的时间和空间界限的方法。

字符串B树：一种用于外部存储器中字符串搜索的新数据结构及其应用，Paolo Ferragina和Roberto Grossi进行了深入研究，将 try和B树的优点结合在一起。












