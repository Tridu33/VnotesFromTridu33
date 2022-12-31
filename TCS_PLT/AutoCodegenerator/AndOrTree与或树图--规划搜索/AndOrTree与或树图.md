# 1. AndOrTree与或树图


AndOrSearch是一种用于搜索由不确定环境生成的And-Or图的算法。它返回在所有情况下都达到目标状态的条件计划。（符号[x | l]表示通过将对象x添加到列表l的前面而形成的列表。）

该功能摘自《人工智能：现代方法》一书。

状态空间表示法

您可以通过两种方式将“与或或图”搜索作为搜索算法进行查看：

**在状态空间中进行搜索**：这里，来自Wikipedia定义的“项目”是状态，而“在一组项目中具有指定属性的项目”是目标状态。通过“与或或图”搜索，通常仅找到一个这样的项目是不够的。在这种观点下，维基百科上的定义太狭窄了。

**在部分条件计划的空间**中进行搜索时：这里的“项目”是部分条件计划，而“在一组项目中具有指定属性的项目”是总条件计划，即具有指定属性的部分条件计划确保经过有限的步骤后才能达到目标状态。与总条件计划不同，部分条件计划可能包含叶节点，这些叶节点既不是目标节点，也不是计划中的关联动作。此搜索空间中的搜索步骤是通过一个动作扩展部分条件计划的步骤，即这些步骤采用一个局部计划P并返回一个类似于P的新的局部计划P'，但其中一个非目标叶子被有效动作替换了分配给该叶节点。

两种观点都是合法的，第二种观点与Wikipedia定义完全一致。

常规图形搜索中的类似区别是在搜索目标状态和搜索通往目标状态的路径之间。












https://en.m.wikipedia.org/wiki/And%E2%80%93or_tree


https://blog.csdn.net/starter_____/article/details/91756741
与或树

什么叫状态空间树？

就是问题的解空间树，分为子集树和排列树。

什么是与或树？什么是可解节点？什么是解树？
一棵树中的弧线表示所连树枝为“与”关系，不带弧线的树枝为或关系。这棵树中既有与关系又有或关系，因此被称为与或树。 
满足下列条件的节点为可解节点。①终止节点是可解节点；②一个与节点可解，当且仅当其子节点全都可解；③一个或节点可解，只要其子节点至少有一个可解。解树实际上是由可解节点形成的一棵子树，这棵子树的根为初始节点，叶为终止节点，且这棵子树一定是与树。



https://blog.csdn.net/starter_____/article/details/91775939
博弈树是与或树一种

https://baike.baidu.com/item/%E4%B8%8E%E6%88%96%E5%9B%BE/1669575
与或图

https://www.itranslater.com/qa/details/2325922824445232128

带权与或树转化为AOE-网
http://wap.cnki.net/lunwen-2010188801.nh.html

https://www.cnshu.cn/qygl/804840.html
与或树的搜索策略搜索的完备性与效率(PPT 43页)-战略管理 ...



TensorFlow 中的所有计算都会被转化为计算图上的节点。
TensorFlow 是一个通过计算图的形式来表述计算的编程系统。
TensorFlow中的每个计算都是计算图的一个节点，而节点之间的边描述了计算之间的依赖关系。
TensorFlow 的计算模型是有向图,采用数据流图 (Data Flow Graphs)，其中每个节点代表一些函数或计算，而边代表了数值、矩阵或张量



https://www.dtreg.com/methodology/view/decision-trees-compared-to-regression-and-neural-networks

神经网络更像是一个“黑匣子”，可以交付结果，而无需解释结果是如何得出的。因此，很难或不可能解释如何基于网络的输出做出决策。

如果对基于神经网络的决策提出了挑战，那么很难向非技术人员解释和证明决策的正确性。相反，决策树易于解释，并且可以轻松显示特定决策“流经”决策树的过程。

如果不为模型使用专用的“解释器”，则很难将神经网络模型合并到计算机系统中。因此，如果目标是要生成一个可以与内置预测模型一起分发的程序，则通常有必要随同发送一些其他模块或库来进行神经网络解释。相反，一旦建立了**决策树模型，就可以将其转换为if ... then ... else语句**，这些语句可以在大多数计算机语言中轻松实现，而无需单独的解释器。




# 2. Solvers

AND/OR graph *AND/OR Graph Algorithm * AND/OR searching *AO* Algorithem



http://netclass.csu.edu.cn/jpkc2003/rengongzhineng/rengongzhineng/kejian/AI/Ai/chapter2/222.htm
人工智能课程与或树
https://cs.nyu.edu/courses/spring01/G22.2560-001/andor.html

http://web.cs.ucla.edu/~rosen/161/notes/search2.html 人工智能笔记

https://users.cs.cf.ac.uk/Dave.Marshall/AI2/node25.html

chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://cse.iitkgp.ac.in/~pallab/ai.slides/lec4.pdf PPT
Problem Reduction Search:AND/OR Graphs & Game TreesAND/OR Graphs & Game Trees

Course: CS40002Instructor: Dr. Instructor: Dr. Pallab DasguptaPallab Dasgupta





Best-First AND/OR Search for Most Probable Explanations
http://reasoning.cs.ucla.edu/samiam/





https://users.cs.duke.edu/~brd/Teaching/Previous/AI/Lectures/Summaries/search.html#AND/OR%20Graphs

AND/OR Graphs

In AND/OR graphs, nodes typically represent complete subproblems; the root node is the original problem to be solved, and the leaves are solved problems. Edges represent problem reduction operators, which decompose a problem into subproblems. If only one of the subproblems needs to be solved, the node is an OR node. If all of its subproblems must be solved in order to solve it, it is an AND node.

A solution to an AND/OR graph is a **subgraph** that contains the root node, an edge from every OR node, and all the branches from every AND node, with only goal states as terminal nodes.

Such graphs are most suitable for problems for which tree structures are the natural representation for the solution, as opposed to a simple path.

Example: symbolic integration. The OR links represent the integrand (find some way to integrate the expression), while the AND links represent individual summands within the integrand, all of which must eventually be integrated. The solution required is a partially-ordered sequence of actions.




## 2.1.  AO* is one of the  major  AND-OR  graph  search  algorithms. 
simple implementation of the a-star path finding algorithm in python https://github.com/jrialland/python-astar



This is a wumpus world game that is solved using the A* algorithm for cs 370  一个经典的强化学习例子 ,恰恰用的就是 经典搜索算法，得到的algrithm-like CFG就是完美翻译的解子图。 https://github.com/deepwritescode/Wumpus-World-Android

A* puzzle implementation https://github.com/sohamsadhu/hellogit
很多可以借鉴的例子

A* Search Algorithm implemented in Prolog https://github.com/cifinn/a-star


A Python3 implementation of path finding algorithms: BFS, DFS, and A* search
https://github.com/gmpalaganas/maze_solver

https://github.com/rapidclock/pacman-search 吃豆人也是用A*规划Implementation of BFS, DFS, USC and A-Star for Pacman food grid search.
DFS - Stack
BFS - Queue
UCS - PriorityQueueWithFunction
A* Search - PriorityQueueWithFunction

the RushHour puzzle (A* search algorithm)
https://github.com/fabiandev/rushhour


C++ Implementation of A* Algorithm https://github.com/niwtr/Nova













https://github.com/davetcoleman/visibility_graph





Visual graphic A Star search implementation https://github.com/oxalorg/visual-astar-js
demo https://oxal.org/projects/visual-astar-js/ 这分明就是强化学习值迭代Q-functino的思路！







```
1. Let GRAPH consist only of the node representing the initial state. 
   Call this node INIT, 
   Compute VINIT.
2. Until INIT is labeled SOLVED or until INIT's h' value becomes greater than FUTILITY, 
   repeat the following procedure:
     a. Trace the labeled arcs from INIT and select for expansion one of the as yet 
        unexpanded nodes that occurs on this path. Call the selected node NODE.
     b. Generate the successors of NODE. If there are none, then assign FUTILITY as
        the h' value of NODE. This is equivalent to saying that NODE is not solvable. 
        If there are successors, then for each one (called SUCCESSOR) that is not also 
        an ancestor of NODE do the following:
            i. Add SUCCESSOR to GRAPH
           ii. If SUCCESSOR is a terminal node, label it SOLVED and assign it an h'
               value of 0
          iii. If SUCCESSOR is not a terminal node, compute its h' value
     c. Propagate the newly discovered information up the graph by doing the 
        following: Let S be a set of nodes that have been labeled SOLVED or whose h' 
        values have been changed and so need to have values propagated back to 
        their parents. Initialize S to NODE. Until S is empty, repeat the, following 
        procedure:
           i. If possible, select from S a node none of whose descendants in GRAPH 
              occurs in S. If there is no such node, select any node from S. Call this 
              node CURRENT, and remove it from S.
          ii. Compute the cost of each of the arcs emerging from CURRENT. The 
              cost of each arc is equal to the sum of the h' values of each of the 
              nodes at the end of the arc plus whatever the cost of the arc itself is. 
              Assign as CURRENT'S new h' value the minimum of the costs just 
              computed for the arcs emerging from it.
         iii. Mark the best path out of CURRENT by marking the arc that had the 
              minimum cost as computed in the previous step.
          iv. Mark CURRENT SOLVED if all of the nodes connected to it through the 
              new labeled arc have been labeled SOLVED.
           v. If CURRENT has been labeled SOLVED or if the cost of CURRENT was 
              just changed, then its new status must be propagated back up the 
              graph. So add all of the ancestors of CURRENT to S.
```

Optimized AO* Algorithm for and-Or Graph Search
chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://iosrjournals.org/iosr-jce/papers/Vol17-issue4/Version-1/R01741124127.pdf


https://www.goeduhub.com/7063/implement-ao-search-algorithm
一个详细的例子用来学习


https://www.brainkart.com/article/AO--Search(Graph)--Concept,-Algorithm,-Implementation,-Advantages,-Disadvantages_8884/
教程

PPT https://www.slideshare.net/arunsingh660/problem-reduction-and-or-graph-ao-algorithmppt



AO* Algorithm

    Initialise the graph to start node
    Traverse the graph following the current path accumulating nodes that have not yet been expanded or solved
    Pick any of these nodes and expand it and if it has no successors call this value FUTILITY otherwise calculate only f' for each of the successors.
    If f' is 0 then mark the node as SOLVED
    Change the value of f' for the newly created node to reflect its successors by back propagation.
    Wherever possible use the most promising routes and if a node is marked as SOLVED then mark the parent node as SOLVED.
    If starting node is SOLVED or value greater than FUTILITY, stop, else repeat from 2.


https://www.youtube.com/watch?v=ZlaYlm87ctE


https://www.youtube.com/watch?v=u_TE42-uWD0
AO* algorithm in AI (artificial intelligence) in HINDI | AO* algorithm with example

AO* algorithm \ AO* (star) Algorithm in English in artificial intelligence\Artificial intelligence.
https://www.youtube.com/watch?v=PhRayhkbJCo




The search algorithm AO* estimates the cost of the solution graphs rooted at various nodes and is guaranteed to find a cheapest solution if the estimates are optimistic.

Rather than using OPEN and CLOSED lists, AO* uses a graph structure containing the nodes expanded so far. Each node points up to its immediate predecessors and down to its immediate successors. The nodes contain partial solutions, the heuristic estimate h' of the cost of a path to a set of solution nodes. (It is not possible to store g since there may be many paths to the node.)

AO* is a two-step process. 

The first step is a **top-down** algorithm that marks the current, best partial solution. A nonterminal leaf node of this solution is chosen and expanded. 

The second step is a **bottom-up**, cost-revising, connector-marking step. The connectors that give the best estimate for a node are marked "best." Selecting the next node to expand isn't easy; one possibility is to select the node most likely to change the estimate of the best partial path solution graph.




## 2.2. 有比AO *更好的算法吗？

https://www.researchgate.net/publication/200035255_An_Algorithm_Better_than_AO

最近，人们对AO *有了新的兴趣，因为涉及不确定性和反馈的计划问题可以自然地表述为AND / OR图。在这项工作中，我们将进行与其他AND / OR搜索算法有关的AO *的第一个详细的经验评估。我们将AO \*与其他两种方法进行了比较：著名的**值迭代（VI）算法**和一种新的算法，即“深度优先搜索”（LDFS）。

我们考虑来自四个域的实例，使用三个不同的启发式函数，并专注于最坏情况下的成本优化（Max AND / OR图）。粗略地我们发现，尽管在有启发式启发的情况下AO \*的性能优于VI，但在AND / OR图中存在**循环**的情况下，VI的性能优于最近的AO \*扩展。同时，LDFS及其变体Bounded LDFS，


>**值迭代法**，快进到强化学习!!!机器学习，智能算法蚁群信息素等等。


An efficient algorithm for searching implicitAND/OR graphs with cycles
https://www.sciencedirect.com/science/article/pii/S0004370200000631








# 3. github Code

Implementation of A* algorithm.
Given graph and heuristics, this algorithm calculates best possible path from source to destination.

https://github.com/jayantrane/ai-algorithms-codes

Implementation of AO* algorithm.
Given a AND OR graph, AO* algorithms gives minimum cost for the graph


Solving N-Queens problem using And-Or search (AO*).  https://github.com/TienNHM/N-Queens-And-Or-Search
！！！**很好的算法题求解过程**


著名人工智能教材，上课那本的https://github.com/aimacode/aima-python search.py部分讲到这个




https://github.com/jayantrane/ai-algorithms-codes ai-algorithms-codes

















































































































































