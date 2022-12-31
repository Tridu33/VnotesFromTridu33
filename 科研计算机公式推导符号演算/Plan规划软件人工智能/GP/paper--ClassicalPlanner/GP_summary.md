
[Zotero + Web of Science，如何做文献泛读](https://zhuanlan.zhihu.com/p/259723540)


## 1.1. 经典问题例子

Aminof, B., Giacomo, G. D., Murano, A., & Rubin, S. (2019). Planning under ltl environment specifications. In *Proc. ICAPS,* pp. 31-39.积木世界QNP实例

Bonet, B., Frances, G., & Geffner, H. (2019). Learning features and abstract actions for computing generalized plans. In Proc.AAAI.石头世界 $Q_{clear}$和G ripper例子

Bonet, B., & Geffner, H. (2015). Policies that generalize: Solving many planning problems with the same policy.. In *IJCAI,* pp. 2798-2804.很多经典问题

# 2. Generalized planning通用规划

Jimenez, S., Segovia-Aguas, J., & Jonsson, A. (2019). **综述A review of  Generalized planning**. *The Knowledge Engineering Review, 34.*


Aguas, J. S., Celorrio, S. J., , & Jonsson, A. (2016). **Generalized planning** with procedural domain control knowledge. In *Proc. ICAPS.*

Belle, V., & Levesque, H. J. (2016). Foundations for **Generalized planning** in unbounded stochastic domains. In *KR,* pp. 380-389.

Bercher, P., & Mattmuller, R. (2009). Solving non-deterministic planning problems with pattern database heuristics. In *Proc. German Conf. on AI (KI),* pp. 57-64. Springer.

Bonet, B., Palacios, H., & Geffner, H. (2009). Automatic derivation of memoryless policies and finite-state controllers using classical planners. In *Proc. ICAPS-09,* pp. 34-41.

Bonet, B., De Giacomo, G., Geffner, H., & Rubin, S. (2017). **Generalized planning**: Nondeterministic abstractions and trajectory constraints. In *Proc. IJCAI.*

Bonet, B., & Geffner, H. (2018). Features, projections, and representation change for **Generalized planning**. In *Proceedings of the 27th International Joint Conference on Artificial Intelligence,* pp. 4667-4673. AAAI Press.把GP映射QNP求解

Bonet, B., Palacios, H., & Geffner, H. (2009). Automatic derivation of memoryless policies and finite-state controllers using classical planners. In *ICAPS*.

Bueno, T. P., de Barros, L. N., Maua, D. D., & Sanner,S. (2019). Deep reactive policies for planning in stochastic nonlinear domains. In *AAAI*, Vol. 33, pp. 7530-7537.

Camacho, A., Bienvenu, M., & McIlraith, S. A. (2019). Towards a unified view of ai planning and reactive synthesis. In *Proc. ICAPS,* pp. 58-67.

Cimatti, A., Pistore, M., Roveri, M., & Traverso, P. (2003). Weak, strong, and strong cyclic planning via symbolic model checking. *Artificial Intelligence, 147*(1-2), 35-84.****

Fikes, R., & Nilsson, N. (1971). STRIPS: A new approach to the application of theorem proving to problem solving. *Artificial Intelligence,* 1, 27-120.**紧凑描述STRIPS**规划语言

Geffner, T., & Geffner, H. (2018). Compact policies for fully observable non-deterministic planning as sat. In *Proc. ICAPS.*把FOND问题转换为SAT问题求解那个github源码程序包对应论文

Hu, Y., & De Giacomo, G. (2011). **Generalized planning**: Synthesizing plans that work for multiple environments. In *IJCAI,* pp. 918-923.

Illanes, L., & McIlraith, S. A. (2019). **Generalized planning** via abstraction: arbitrary numbers of objects. In *Proc.* AAAI.

Martin, M., & Geffner, H. (2004). Learning **generalized policies** from planning examples using concept languages. *Appl. Intelligence, 20*(1), 9-19.

Muise, C. J., McIlraith, S. A., & Beck, C. (2012). Improved non-deterministic planning by exploiting state relevance. In *Proc. ICAPS.*

## 2.1. 自动规划

Geffner, H., & Bonet, B. (2013). **A *Concise Introduction** to Models and Methods for Automated Planning.* Morgan & Claypool Publishers.讲FOND问题

Ghallab, M., Nau, D., & Traverso, P. (2016). *Automated planning and acting.* CambridgeUniversity Press.

## 2.2. QNP

Srivastava, S., Zilberstein, S., Immerman, N., & Geffner, H. (2011). Qualitative numeric planning. In AAAI.很详细这里说FOND问题的解对应着QNP问题的解(不是互推)还有SCC算法等学长已经报告过

Srivastava, S., Immerman, N., & Zilberstein, S. (2011). A new representation and associated algorithms for **Generalized planning**. *Artificial Intelligence, 175*(2), 615-647.介绍QNP很有用地表述“GP通用规划”

# 3. 结合逻辑神经机

Garnelo, M., & Shanahan, M. (2019). Reconciling deep learning with symbolic artificial intelligence: representing objects and relations. *Current Opinion in Behavioral Sciences, 29,* 17-23.<--- **将深度学习与符号人工智能相结合：表示对象和关系**

Toyer, S., Trevizan, F., Thiebaux, S., & Xie, L. (2018). Action schema networks: **Generalised policies** with deep learning. In AAAI.神经网络生成通用策略

Groshev, E., Goldstein, M., Tamar, A., Srivastava, S., & Abbeel, P. (2018). Learning generalized reactive policies using deep neural networks. In *Proc. ICAPS,* Vol. 2018, pp. 408-416.神经网络生成策略

Fern, A., Yoon, S., & Givan, R. (2004). Approximate policy iteration with a policy language bias. In *Advances in neural information processing systems,* pp. 847-854.

Boutilier, C., Reiter, R., & Price, B. (2001). Symbolic dynamic programming for first-order MDPs. In *Proc. IJCAI,* Vol. 1, pp. 690-700.一阶马尔可夫过程动态编程（我觉得**MDP**马尔可夫数学化的研究过程很明显就是无缝对接**RL**强化学习的活儿）

Van Otterlo, M. (2012). Solving relational and first-order logical markov decision processes: A survey. In Wiering, M., & van Otterlo, M. (Eds.), *Reinforcement Learning,* pp. 253-292. Springer.

Sukhbaatar, S., Szlam, A., Synnaeve, G., Chintala, S., & Fergus, R. (2015). Mazebase: A sandbox for learning from games. *arXiv preprint arXiv:1511.07401.*

Wang, C., Joshi, S., & Khardon, R. (2008). First order decision diagrams for relational MDPs. *Journal of Artificial Intelligence Research, 31,* 431-472.一阶决策图对应求解MDP

Sanner, S., & Boutilier, C. (2009). Practical solution techniques for first-order MDPs. *Artificial Intelligence, 173*(5-6), 748-788.

Nebel, B. (2000). On the compilability and expressive power of propositional planning. *Journal of Artificial Intelligence Research, 12, 271-315.*

Khardon, R. (1999). Learning action strategies for planning domains. *Artificial Intelligence, 113,* 125-148.

Issakkimuthu, M., Fern, A., & Tadepalli, P. (2018). Training deep reactive policies for probabilistic planning problems. In *ICAPS.*概率规划问题

### 3.1.1. SAT

Een, N., & Sorensson, N. (2004). An extensible SAT-solver. *Lecture notes in computer science, 2919,* 502-518.

### 3.1.2. Complexity 

Rintanen, J. (2004). Complexity of planning with partial observability.. In *Proc. ICAPS,* pp. 345-354.

Levesque, H. J. (2005). Planning with loops. In *IJCAI,* pp. 509-515.指数复杂度

Littman, M. L., Goldsmith, J., & Mundhenk, M. (1998). The computational complexity of probabilistic planning. *Journal of Artificial Intelligence Research, 9,* 1-36.表明QNP问题有着指数的复杂度

## 3.2. 其他相关的论文书籍

Russell, S., & Norvig, P. (2002). *Artificial Intelligence: A Modern Approach.* Prentice Hall. 2nd Edition.书籍人工智能

Sipser, M. (2006). *Introduction to Theory of Computation* (2nd edition). Thomson Course Technology, Boston, MA.教材

Cimatti, A., Roveri, M., & Traverso, P. (1998). Automatic **OBDD-based** 很火的一种紧凑表达结构generation of universal plans in non-deterministic domains. In *Proc. AAAI-98,* pp. 875-881.

Bajpai, A. N., Garg, S., et al. (2018). Transfer of deep reactive policies for mdp planning. In *Advances in Neural Information Processing Systems,* pp. 10965-10975.通用规划无限随机域

Helmert, M. (2002). Decidability and undecidability results for planning with numerical state variables.. In *Proc. AIPS,* pp. 44-53.

Hu, Y., & De Giacomo, G. (2013). A generic technique for synthesizing bounded finite-state controllers. In *Proc. ICAPS.*

Srivastava, S., Zilberstein, S., Gupta, A., Abbeel, P., & Russell, S. (2015). Tractability of planning with loops. In *Proc.* AAAI.

Tarjan, R. (1972). Depth-first search and linear graph algorithms. *SIAM journal on computing, 1* (2), 146-160.

Pnueli, A. (1977). The temporal logic of programs. In *18th Annual Symposium on Foundations of Computer Science,* pp. 46-57. IEEE.

Pnueli, A., & Rosner, R. (1989). On the synthesis of an asynchronous reactive module. In *ICALP,* pp. 652-671.