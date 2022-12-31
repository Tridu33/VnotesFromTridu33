




# Rascal



homepages.cwi.nl/~storm/rascal-tutorial/Rascal 是用于源代码分析和转换的编程语言。主要应用领域是（传统）系统改造，逆向工程和再工程，以及领域特定语言（DSL）的实现。DSL是为特定应用程序域量身定制的语言。示例包括SQL，Excel，Make，Latex，VHDL等。今天，我们将在某些方面使用Rascal，以为状态机实现特定于域的小型语言。该示例摘自Martin Fowler的有关领域特定语言的书。相关章节在线发布：

http://www.informit.com/articles/article.aspx?p=1592379

状态机可用于描述状态相关的行为，例如控制机器或工作流程引擎。有关这种状态机理论的更多信息，您可能需要查阅Wikipedia http://en.wikipedia.org/wiki/Finite_state_transducer。

在本教程中，我们将通过遇到以下DSL实现方面来探索Rascal语言和环境：

用于描述状态机语言语法的无上下文语法

用于描述状态机抽象语法树（AST）的代数数据类型（ADT）

重置事件（请参见上面的链接）是语法糖：可以将它们分解为不使用它们的等效状态机。

从状态机中提取关系。这使状态机分析更加容易。这些关系可以连接到状态机可视化器（由我们提供）。

状态机的一致性检查器。例如，此组件突出显示未定义状态或事件的使用，标记重复的状态，命令或事件并检测不可达状态。

一个代码生成器，它生成使用并生成令牌的Java代码。

转换需要两个状态机，并产生一个新的状态机，该状态机可以并行运行两个原始机。可以将结果状态机输入到原始代码生成器和可视化器。

为状态机提供特定于域的IDE功能：用于调用代码生成器的上下文菜单，大纲视图，折叠，错误标记。


http://www.cwi.nl/~storm/rascal-tutorial/miss-grant.zip  miss-grant 那个例子


http://tutor.rascal-mpl.org/


























