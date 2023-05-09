# 1. Structured prediction




https://en.wikipedia.org/wiki/Structured_prediction






结构化预测是机器学习的一个领域，重点在于具有组合结构的空间表示以及这些结构的推理和参数估计算法。核心方法既包括诸如动态编程和生成树算法之类的易于处理的精确方法，也包括诸如线性编程松弛和贪婪搜索之类的启发式技术。



https://paperswithcode.com/task/structured-prediction



http://blog.sciencenet.cn/blog-795431-668770.html
结构化预测(structured prediction)是由SVM发展而来的。SVM是一种最大间隔(max-margin)的方法，最擅长处理二分类问题，后来也被用于处理多分类问题。SVM的优点在于有很好的理论基础，即它的泛化能力很强。它的缺点在于1）训练复杂度高；2）不能用于预测结构化问题。
结构化问题的例子有很多：给定一个句子，找出它对应的依存树(dependency tree)；对一个图进行分割(image segmentation)等。
结构化预测(structured prediction)通过修改SVM的约束条件以及目标函数，将SVM从二分类问题扩展到可以预测结构化问题。



闲聊结构化预测（structured learning） - 忆臻的文章 - 知乎
https://zhuanlan.zhihu.com/p/39745877




在机器学习过程中，对数据的拟合其实就是在找一个拟合函数f：


比如对于回归问题（Regression）来说，这个函数输出一个标量（scalar）

对于分类问题（Classification）来说，这个函数输出一个类别（一个one-hot的向量）



但是有一类的预测，它并不是输出一个标量或者一个类别，而是输出些有结构的输出，比如，一个序列，一个句子，一个图，一颗树...

比如把数学问题MWP表达式看成一个计算树逆波兰表达式 `(单价 + 2)*nums数量 = predicate支付价格`计算结构



那么我们将输出这些结构化结果的过程叫做结构化预测（Structured Prediction）
















