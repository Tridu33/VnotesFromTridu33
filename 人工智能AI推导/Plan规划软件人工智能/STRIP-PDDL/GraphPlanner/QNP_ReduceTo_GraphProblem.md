
[QN_GraphPlanner本地文件](file:///D:/tridu33/Py/jupyternotebook/QN_GraphPlanner)



Qualitative Number Problem input text file format: Q = < F,V,丨,O,G >

其中：

> 状态编码S=<F,V>=一个二进制转十进制的数。如：状态S16={f1,-f2,-f3,v1>0,v2>0}编码为二进制10000即十进制16。经此操作，每个独立S=<F,V>均编码为数字。

- F：Boolean proposition 

  | $f_1$ | ...  | $f_n$ | $-f_1$ | ...  | $-f_n$ |
  | ----- | ---- | ----- | ------ | ---- | ------ |
  | 1     | 1    | 1     | 0      | 0    | 0      |

- V：

  | $v_1>0$ | ...  | $v_m>0$ | $v_1=0$ | ...  | $v_m=0$ |
  | ------- | ---- | ------- | ------- | ---- | ------- |
  | 0       | 0    | 0       | 1       | 1    | 1       |

- I起始状态

- G目标状态同样只是一个状态编码。

- O动作集={a1,a2,a3,a4,...}定义为：到映射，然后允许缺省值自动枚举状态，比如放下石头动作，唯一的直观形式化表示<-E非空手,变成E空手>动作对应的状态变迁 -->。

注：QNP问题中原问题的一般使用V={v1,v2,v3...}作为非确定性动作 $a_x$ 的 if conditions条件判断依据，决定着当前状态采取行动$a_x$的后继影响effects。比如积木世界中，确定性动作Pick-above-x捡起来x上方积木，只要if (x上方积木数量n-1 !=0)执行动作Pick-above-x后继状态就是“-clear(x)非空”;if (x上方积木数量n-1 !=0)执行动作Pick-above-x后继状态就是“clear(x)空”。

在本算法求解问题的时候，先考虑relaxed problem，放松(动作执行后if condition条件判断决定后续结果effect的)约束，直接暂时先假装动作“Pick-above-x”是非确定的，执行后既有可能clear(x)也有可能-clear(x)。等到使用图论算法找到一条从$S_i$-->$S_G$有向有环通路图$G_{Solution}$之后，再恢复if condition的功能,从生成唯一可执行的动作序列{a1,a1,a1,a2,a3,......}解。

----------------------------------------

先把标准QNP问题reduce to经典有向图Directed graph问题G=<Node节点，Edges边>: 

QNP中S=<F,V>(包括汾,而)有限状态集reduce to图G中的点集Nodes;

QNP中的O动作集则reduce to图G中的节点之间有向边Edges。 

原问题QNP从此变成一张有向有环图G中，找到一条从$S_i$-->$S_G$有向有环通路图$G_{Solution}$的问题。

- 算法第一步：利用《系统工程》中的解析结构模型化技术ISM算法，去除孤立节点(缺省值自动枚举的“不可能发生的”状态)，和不包含$S_i,S_G$的**有向有环子图**$G_{pruning}$------至于为什么不从$s_i$开始枚举动作集O破圈搜索到$S_G$呢？感觉也行，结果应该是一样的。反正都是建立一张$G=<N,E>$图，觉得写成矩阵格式的图用ISM算法处理起来更方便。
- 算法第二步：破环，tarjan等图论算法找到SCC，（可逆地）合并SCC强连通分量为“一个个虚拟节点”，原图合并后变成一张**有向无环图**$G_{DirectedAcyclicGraph}$。
- 算法第三步：针对有向无环图$G_{DirectedAcyclicGraph}$，找一条从节点到的路径有很多算法可以实现，可以直接dijkstra找到一条从$S_i$-->$S_G$**有向有环通路图**$G_{HalfSolution}$。
- 算法第四步：向有环通路图$G_{HalfSolution}$应用第二步的可逆合并操作，解除SCC的合并(第二步要记录入度点和出度点们，SCC还原的时候要用)，得到**有向有环通路图**$G_{Solution}$
- 再从放松约束relaxed problem收紧，变成前文提到的“含if条件的确定性动作"，应用V数值的if条件condition判断功能,从图$G_{Solution}$生成唯一可执行的Policy：$S_{F,V}\rightarrow O_{actions}$,可以对应动作序列{a1,a1,a1,a2,a3,......}解。

![qnp图法设计_1598498581_30912](.\_v_images\qnp图法设计_1598498581_30912.png)





