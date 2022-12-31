http://minikanren.org/minikanren-and-prolog.html




http://www.infoq.com/interviews/byrd-relational-programming-minikanren

# 1. Prolog和miniKanren之间的主要技术区别



https://www.codenong.com/28467011/




有关miniKanren和Prolog之间差异的详细讨论，请参见此处。

在逻辑编程方面，Prolog和miniKanren之间的主要技术差异是什么？ https://cloud.tencent.com/developer/ask/100973


这是一个棘手的问题，主要是因为miniKanren和Prolog都有很多变种。miniKanren和Prolog实际上是语言的家族，这使得难以比较它们的特征，甚至难以在实践中使用它们。正因为如此，请谨慎对待我所说的一切：如果我说Prolog使用深度优先搜索，请注意许多Prolog实现支持其他搜索策略，并且可以在元数据中编码替代搜索策略 - 解释器级别。不过，miniKanren和Prolog有不同的设计理念，并做出不同的折衷。

这个关系版本append可以很容易地用Prolog来表示，而且实际上在许多Prolog教程中都有介绍。实际上，更复杂的Prolog程序倾向于使用至少一些额外的逻辑特征，例如剪切，这会抑制将结果程序视为关系的能力。相比之下，miniKanren明确地被设计为支持这种类型的关系编程。最近miniKanren的版本有象征性的约束求解的支持（symbolo，numbero，absento，不平等限制，名义上的逻辑规划），以便更容易地写出不重要的程序作为关系。在实践中，我从不使用miniKanren的任何额外逻辑特征，并将所有我的迷你坎恩节目编写为关系。最有趣的关系程序是Scheme的子集的关系解释器。


Prolog 这类逻辑式编程语言为什么没有得到广泛应用？ - 抽象猴的回答 - 知乎
https://www.zhihu.com/question/31895071/answer/86812645














