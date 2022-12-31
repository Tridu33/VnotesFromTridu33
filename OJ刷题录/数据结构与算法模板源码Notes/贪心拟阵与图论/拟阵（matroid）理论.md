

[TOC]


# 1. 拟阵（matroid）理论


贪心算法及其理论依据——拟阵
最全理论依据 https://www.cnblogs.com/zhangzefei/p/9749735.html

刘桂真,陈庆华著《拟阵》 https://ishare.iask.sina.com.cn/f/38334686.html https://book.ixueshu.com//////book/bf963b1f8444ba27.html 爱学术chrome弹出警告密码被盗风险

《拟阵论》http://www.tushu007.com/ISBN-9787040105636.html online看 https://max.book118.com/html/2019/0211/5244343341002010.shtm



拟阵（matroid）理论背后的motivation是什么？ - 知乎
https://www.zhihu.com/question/28424181/answer/40821339



贪心算法背后的理论依据——拟阵理论。对于拟阵理论，可以查找一些入门典籍，如刘桂真,陈庆华著《拟阵》。
https://blog.csdn.net/ChiXueZhiHun/article/details/54808939



怎么理解拟阵（matroid）？ - 陈林的回答 - 知乎
https://www.zhihu.com/question/316879980/answer/629921912
拓扑空间是在研究连续映射的时候抽象出来的一种“本质”结构，而拟阵则是出于研究“独立性”和“相关性”的本质。


<算法导论>16章


怎么理解拟阵（matroid）？ - 好地方bug的回答 - 知乎
https://www.zhihu.com/question/316879980/answer/633569574


拟阵及应用（二） - 好地方bug的文章 - 知乎
https://zhuanlan.zhihu.com/p/54072907






https://en.wikipedia.org/wiki/Matroid#Algorithms


https://www.luogu.com.cn/blog/cpp/ni-zhen-yu-zui-you-hua-wen-ti
拟阵与最优化问题



拟阵解决贪心问题的规律便在于此——对于任何能够转换为拟M=(S,L)M=(S,L)的问题，都可以通过如下算法解决(即求出权值最大独立集)：

```
 Set Solve(M,w)//给出拟阵M与权值函数w  (Set这里意为返回一个集合)
{
    清空A;
    将S按w(x)的大小降序排好；
    for(对每一个x∈S,按w(x)降序)
    {
        if(A∪{x}∈L)
            A=A∪{x}；
    }
    return A;//即权值最大独立集
}

```
令n=|S|n=∣S∣,f(n)f(n)表示判断独立集的复杂度，那么上述算法的时间复杂度为O(nlog_2n+nf(n))O(nlog）
​	
 n+nf(n)) 。事实上，在将问题转化为拟阵后，套用该算法的关键便在于如何判断独立集。不同问题有不同的独立集及判定方法，拟阵体现的是这些问题允许贪心的共性。


https://taodaling.github.io/blog/2020/10/22/%E6%8B%9F%E9%98%B5/
题目刷题


很多问题都可以建模成[拟阵](https://taodaling.github.io/blog/2020/10/22/%E6%8B%9F%E9%98%B5/)。

    颜色拟阵：给定n个元素，每个元素都有自己的颜色。一个集合是独立集当且仅当集合中所有元素的颜色不同。
    图拟阵：给定n个顶点和m条边，一个边集是独立集当且仅当集合中的边不形成任意环。
    代数拟阵：给定n个向量，一个向量集合是独立集当且仅当集合中的所有向量线性无关。
    删边图拟阵：给定n个顶点和m条边，一个边集是独立集当且仅当删除这些边后图依旧保持连通。
    下面是一些拟阵的额外命题（这些定理的证明来自拟阵划分）：


**拟阵划分**
拟阵划分是指将集合中的元素划分成最少的不相交的独立集。
https://chaoli.club/index.php/5645





# 2. s思路

图拟阵

动态规划：最优子结构，备忘录记下来子结构的数据后期用到直接调用快一些


贪心算法

控制流图的子结构，求解独立子图，子结构子网，然后拼接子网就是得到的答案



独立无关向量组，子问题

写成矩阵形式的图，多叉树



# 3. 贪心拟阵图论
该理论可用来确定贪心算法何时能产生最优解，它用到了一种组合结构：Matroid(拟阵)。该结构是Whitney于1935年在研究矩阵中线性无关结构时抽象出来的，由Korte于80年代初将该理论发展为贪心算法理论。该理论覆盖了许多贪心法的应用实例，但并未覆盖所有情况(如活动选择问题)，但它仍在发展

chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://home.ustc.edu.cn/~huang83/turing/alg4.pdf
PPT讲述各种贪心题解 http://home.ustc.edu.cn/~huang83/ 这个老师挺溜呀

https://leetcode-cn.com/problems/non-overlapping-intervals/solution/ 无重叠区间

除了动态规划，贪心算法。这题可以转化为图论，然后用dijkstra解决，时间复杂度O(nlogn)

贪心、图论——单源最短路径Dijkstra算法 https://blog.csdn.net/Jayphone17/article/details/101630436








经典《算法导论》提到最小生成树两种算法都是贪心,不是所有贪心都能用拟阵解释，但是拟阵能解释很多贪心


本质就是图论的矩阵表示下**如果是 拟阵，说明描述了子问题独立不相关性，子问题可以贪心求解的局部最优下还能 保证原问题的全局最优。这样就不用dp那样伪线性有可能会因为dp空间增长很大存下来超级多信息防止二次计算的优化**，贪心应该可以比作特殊的DP



https://blog.csdn.net/qq_28013751/article/details/84525657 贪心策略和图论算法教程
https://www.cnblogs.com/yinbiao/p/9220291.html 到底什么叫贪心策略（内含几个经典贪心样例和三大图论算法）


dp是根据迁移过程的状态去推导下一个过程的状态，是有理论依据的，是讲道理的，通过每次完美的检验

而得到最优解，关键是找最优子结构和重复子问题，书上一句原话：dp的子结构必须的独立的，而且是重

叠的，虽然有点矛盾，但确实是这样，扯远了

而贪心每次都只顾眼前最优，目光短浅，这种方式是不讲道理的，不想dp一样，还根据前面的迁移状态推

导后面的子问题，比如最经典的01背包问题（真的是理解dp和贪心的经典例题啊）

其实这些算法还有很多可以优化的地方，比如prim算法可以采用堆优化，迪杰斯特拉算法能用二叉堆优化呀，还能用斐波那契堆优化啊，因为时间有限










# 4. 贪心法,拟阵和亚模函数

https://blog.youxu.info/2008/08/20/geedy-algorithm-matroid-and-submodular-functio/















CLRS 第16章专门讲了贪心算法 (Greedy Algorithm) 的理论基础是拟阵 (matroid) . 具体理论就不重复废话了. 实际上更加贴切的模型叫做 Greedoid. 相关的理论看一下CLRS就好懂了. 注意 CLRS 中间讲到的所谓的带权拟阵, 实际上表明目标函数是线性的 (函数值 F(A) 等于集合A中每个元素权值之和). Edmonds 1970 早在70年代一篇没有摘要的装逼论文中就证明了拟阵结构上对线性函数的贪心算法一定是最优的. (http://portal.acm.org/citation.cfm?id=885912 )

实 际上应用中却不是线性的了, 而是一个叫亚模的(submodular), 具体的细节看维基百科. (http://en.wikipedia.org/wiki/Supermodular ). 亚模这个性质用通俗的话说, 就是随着加入集合的元素越多,  F 函数值获得的受益越少(效用边际递减). 显然世界的很多问题的效用函数都是这个性质. 如信息量 (Information Gain) 等其他效用函数. 这个函数在机器学习, 经济学和博弈论中用途广泛. 比如传感器的安排, Google 最优化广告词的安放, 传感器网络的优化放置, 集合覆盖问题等等. 同时亚模函数和拟阵是有紧密联系的, 如拟阵的秩(rank)的定义, 就必须是一个次模函数.

最好玩的结果是, 除非P=NP, 否则对于拟阵上的亚模函数来说, 贪心算法是多项式时间里面能完成的界最好的最大化算法. 这个就彻底打消了同志们研究新算法的热情鸟：直接用呗，反正没更好的了. 至于呀模函数的最小化, 又是一个多项式的算法. 和线性规划一样, 椭圆方法能解. 其他多项式方法阶也不高.

卡梅. MIT, UIUC 最近都有应用亚模函数做 WSN 或者图分区的文章. 有兴趣的自己去下载吧. 八卦的是, Google 关于 AdWords 最优化拍卖的论文, 一点拟阵和亚模都没扯到, 得到了同样的理论结果, 并且花了很多功夫强证上面贪心算法在界估计上最优这个结论. 不得不说, 学数学还是有点好处滴, 至少不要重新花了老半天重证一个定理鸟. 卡梅的一个团队更加豪言壮语, 说以前的机器学习全是做的啥凸函数的优化 (如 SVM ), 下个十年, 亚模函数就要统治机器学习优化领域啦.

有兴趣的各位老大随喜以下的文章.

An Introduction to Submodular Functions and Optimization. 属于简介
www.ima.umn.edu/optimization/seminar/queyranne.pdf

卡没在ICML上做的tutorial. 讲了和机器学习的联系
http://www.select.cs.cmu.edu/tutorials/submodularity-slides.pdf

Adwords Auctions with Decreasing Valuation Bids.  Google 的论文
www-static.cc.gatech.edu/grads/g/gagang/wine07_full.pdf

Revisiting the Greedy Approach to Submodular Set Function Maximization. MIT Sloan 管理学院的论文
http://www.optimization-online.org/DB_FILE/2007/08/1740.pdf

Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies.卡梅用来做传感器放置的一篇.

http://www.select.cs.cmu.edu/publications/paperdir/jmlr2008-krause-singh-guestrin.pdf

各位随喜了.我还得继续和论文做斗争.















































































































































































