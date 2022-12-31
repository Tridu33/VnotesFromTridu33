对于神经网络，硕士博士不需要弄明白原理，只需要应用，是这样吗？ - 老王的回答 - 知乎
https://www.zhihu.com/question/433274875/answer/1613656010

# 整理不同网络结构cover不同特性任务搭积木


核心观点，可解释性不是为了让人“以为自己理解了”，不是为了让人心里觉得爽或者无意义不可靠的试验来battle(当然，可靠思辨有意义的实验设计验证很重要)，而是要通过理解“设计的超参给定网络函数组要能cover对问题对应数据分布的解空间任一函数.

神经网络是一个可微函数族，那就让这个函数族能覆盖任务的特点；

关键应该是结构的设计，所谓结构的设计，要遵循的原则就是函数族覆盖问题的特性。

可解释性是为了能指导生产生活，我们的观点是“用来指导网络设计”，

比如整理好不同网络结构cover不同特性的任务，然后在此基础上算法网络结构搭积木，从而批量化排列组合生成可靠有效的神经网络产品。

https://blog.csdn.net/qq_35082030/article/details/73368962 一文看懂25个神经网络模型
25种神经结构和 https://www.asimovinstitute.org/neural-network-zoo/ 对应github原仓库
DL之NN：目前最全、最完整的Neural Networks中，各种算法系统原理结构图
http://www.aicheatsheets.com/
https://github.com/Niraj-Lunavat/Artificial-Intelligence
Awesome AI Learning with +100 AI Cheat-Sheets, Free online Books, Top Courses, Best Videos and Lectures, Papers, Tutorials, +99 Researchers, Premium Websites, +121 Datasets, Conferences, Frameworks, Tools











先搭建对应任务特征求解的一个多层网络，不需要知道具体映射，不需要知道具体参数大小，只需要知道大概解函数映射中，大概需要”因子谁和谁建立联系，谁和谁有关联”，设计神经网络结构初始训练函数族的时候就要**cover**这种相关关系。

这很重要！

换句话说，神经网络学习设计中，利用可解释性，在特定问题设计时，针对该问题数据概率分布特点，分析问题解映射的特点，数据关联，去设计能cover这种特点的最适合的网络结构，去train自动获取参数(就像turing的P/A/B型机器内生计算)。

比如要让计算机自发理解年龄和出生年月的(线性)关系y=2x+b=2(1*x+c1)+c2 = …… ,只要能正确激活括号内函数就能很多种写法，可以有无穷多种网络写法,就像异或网络可以很多种结构。其实非线性分类机也同理，只是都多组合几个决策而已。











