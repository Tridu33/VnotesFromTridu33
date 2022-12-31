https://zhuanlan.zhihu.com/p/32778984 Good,终于知道为什么二分类器最简单的perceptron神经网络的训练BP需要凸优化相关算法解决了，也大概能理解为什么需要二分类器来模拟一阶逻辑了，因为我们只能回答yes/no的判定问题，SAT直到SMT，进而解决其他问题。希尔伯特第十问题涉及所谓的 “ 判定问题 ” ，即此问题包含个数无限的个体问题，每个都要求明确的回答：是或否。判定性问题的本质是要求寻找一个方法，使它对于所有的个体子问题都有明确的答案。



这就串起来“判定问题和停机问题”，能理解了"哥德尔不完备定理决断可判定的意义了"---正如图灵论文中说的可判定性和可计算数，自动机理论描述的是”计算能力的边界“，哪些问题我们无法形式化推演的方法来求解，莱布尼兹的机械法官看来是行不通了。

> 看来动画片《Psycho-Pass 心理测量者》中统治整个社会名叫Sibyl System的先知系统，不合理，无法决断很多问题，不是全能的，也是可证明的！狗头。(虽然最后这个人工智能系统背后的真的是”人工/缸恼“)


哥德尔的不可判定原来是这个意思，就是强如任意能构造皮亚诺算术的人为构造的规则系统，哪怕递归定义的逻辑归纳系统数量无穷，必定存在能被这个逻辑系统的语言所表述，但无法判定是真或假的“不完备公理”表述。





NP理论（2）：“判定问题”与“停机问题”
https://blog.sciencenet.cn/blog-2322490-991454.html
计算机理论中现在流行的一个最基本术语就是“停机问题”（the Halting Problem），其基本意思是：判断任意一个程序是否会在有限的时间之内结束运行的问题。这种解释一开始就隐含了一个主体上的混乱，“判断者”是谁？

这个问题实质源于数学和逻辑基本理论，也就是著名的希尔伯特第十问题（Hilbert's tenth problem）。1900年，德国数学家希尔伯特(David Hilbert 1862─1943)在巴黎第二届国际数学家大会上作了《数学问题》的著名讲演，提出了数学理论中的23个最困难的问题，其中的第10个问题是这样说的: Given a Diophantine equation with any number of unknown quantities and with rational integral numerical coefficients: To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers.
注意希尔伯特的用词，作为一个大数学家和形式主义代表，他并没有用“数学方法”、“函数”或“形式方法”这样现成的术语，而是问：能否 “发明一种过程”（或“设计一种方法”）（To devise a process）去“判定”（determine）任何一个丢番图方程问题是否可解？因此，希尔伯特第十问题隐含着数学家的一种哲学上的反思，面对任何可定义的数学问题，数学的“确定性”能力究竟为何？用今天的表达方式就是：存在或不存在对任何可定义的数学问题可解的判定方法？
图灵理解了希尔伯特第十问题的真正要求，图灵具有对复杂机械过程的强大直觉能力（因此后来也成为了一个密码专家），他把人的进行计算的过程完全以符号化的形式表达出来，成为一种算法的机械模型——“图灵机”，图灵机最大的意义就是展示了算法的机械过程，虽然数学和图灵机都使用符号，但它们的组织性质完全不同，数学是纯粹的形式关系，算法则一定是实时（the Actual Time）过程，这样就把数学意义上的“可计算的”函数表达为“可计算的”机械过程，揭示了算法的“能行性”本质，在数学形式之外表达了算法关系，凸现了“算法”的特殊性质和地位，所以“丘奇－图灵论题”说，“能行可计算的”就是图灵机可计算的。


# 只解决能判定的问题集---一阶逻辑关系逻辑，凸函数(代数)和流形(几何)

无限小区域正交，可微高维boolean vector几何结构的“迁移系统”。

【最优化】凸函数及它的一阶特征 - 忆臻的文章 - 知乎
https://zhuanlan.zhihu.com/p/32778984  希尔伯特第十问题的提出和图灵的否定性回答，现在统称为“判定问题”（Entscheidungsproblem）。
# Logic is the law of thought


https://quod.lib.umich.edu/cgi/p/pod/dod-idx/logic-and-the-laws-of-thought.pdf?c=phimp;idno=3521354.0015.012;format=pdf  

G. Boole, “An Investigation of the Laws of Thought, on Which Are Founded the Mathematical Theories of Logic and Probabilities,” Walton and Maberly, London, 1854, p. 1.






1854年, 乔治 布尔在书The Laws of Thought一书中第一次给出了逻辑的基本规则. 1938年, 克劳德-香农揭示了怎么用逻辑的基本规则来设计电路, 这些基本规则形成了布尔代数的基础.


Since the final exam is upcoming, there should be some review of the basic math. Boolean Algebra is the most fundamental math behind the Application and Design of Digital Logic (ADDL) course. In the pure math's aspect, Boolean Algebra is only one topic in the algebraic structures. However, in the perspective of computer science, Boolean Algebra is the base of all digital logic. Here this paper will give a very brief overview of Boolean Algebra in pure math in the beginning. Following that will be its properties. Specifically, the mathematical tricks will be introduced, turning one expression into its simplest forms, including the sum of products (SoP) and the product of sums (PoS). A powerful device in the simplification will also be introduced in the end, the Karnaugh map. Few digital logic circuits will also be given, serving as vivid examples.https://www.cnblogs.com/chancebeauty/p/14887791.html

There are three fundamental laws of logic. Suppose P is any indicative sentence, say, “It is raining.”

The law of identity: P is P.
The law of noncontradiction: P is not non-P.
The law of the excluded middle: Either P or non-P.













