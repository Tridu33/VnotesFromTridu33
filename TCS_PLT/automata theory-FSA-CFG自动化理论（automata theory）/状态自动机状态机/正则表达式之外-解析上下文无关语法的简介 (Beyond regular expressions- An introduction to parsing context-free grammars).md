# 1. 正则表达式之外-解析上下文无关语法的简介 (Beyond regular expressions- An introduction to parsing context-free grammars)by Christopher Diggins


https://blog.csdn.net/cumian8165/article/details/108157427







正则表达式非常适合查找或验证**许多类型的简单模式**，例如电话号码，电子邮件地址和URL。 但是，当将它们应用于可以具有**递归结构**的模式时，它们就不够用了，例如：

    HTML / XML open/close tags
    HTML / XML打开/关闭标签
    open/close braces {/} in programming languages
    用编程语言打开/关闭大括号{/}
    open/close parentheses in arithmetical expressions
    在算术表达式中打开/关闭括号


要解析这些类型的模式，我们需要更强大的功能。 我们可以进入称为**上下文无关语法 (CFG)**的形式语法的下一个层次。



运行CFG解析器所生成的树结构称为解析树 


## 1.1. 表达CFG语法有两种流行的方法：

Extended Bachus-Naur Form (EBNF) — describes a CFG in terms of production rules. These are rules that, when applied, can generate all possible legal phrases in the language.扩展的Bachus-Naur形式 (EBNF)-根据**生产规则**描述CFG。 这些规则在应用时可以生成该语言中所有可能的合法短语。

Parsing Expression Grammar (PEG) — describes a CFG in terms of recognition rules. These are rules that can be used to match valid phrases in the language.解析表达语法 (PEG)-根据**识别规则**描述CFG。 这些规则可用于匹配语言中的有效短语。


与EBNF相比，PEG形式主义具有一个优势，即到解析器的映射是明确的，并且可以轻松实现自动化。







## 1.2. 解析器生成器与解析库 (Parser generators versus parsing libraries)



通常有两种创建解析器的选择：


1. 使用解析器生成器 -一种从解析器的抽象定义生成解析器源代码的工具。 在JavaScript中一些流行的例子包括Jison ， PEG.js ， nearley和ANTLR 。


2. 使用解析库 ，该库允许将解析规则表达为API。 在JavaScript的一些例子包括八哥 ， Parsimmon和鼷鹿科 。



使用Myna解析库以TypeScript / JavaScript编写解析器 (Writing parsers in TypeScript / JavaScript using the Myna Parsing Library)




从具体语法树(CST)到抽象语法树(AST) (From concrete syntax tree (CST) to abstract syntax tree (AST))


当解析器处理输入时，可以将每个成功匹配的规则(又称语法产生)映射到解析树中的节点。 生产规则到树中节点的文字映射是一个具体的语法树 (CST)。

在某些情况下，CST用途有限，因为它包含许多语法混乱，例如源代码中的注释，或者字符串文字是带双引号还是单引号。 它可能包含规则创建的结果，这些规则是为了使语法更易于使用而创建的，但并不表示要进行分析的预期树结构。


最简单的操作是**仅在输出树中为特定规则创建节点**，并跳过其他规则。 解析树的简化版本称为抽象语法树 (AST) 。 可能会对AST执行多次处理，以将其转换为其他AST表示形式，以简化后续处理步骤。






使用生成的Myna抽象语法树 (Using the generated Myna abstract syntax tree)
如果您想了解有关创建和使用解析器的更多信息，无论Myna库是否满足您的特定需求，我建议您花一些时间通读Myna解析库的源代码 。
Myna用TypeScript编写(对于大多数程序员来说，语法都很熟悉)，包含在一个没有依赖性的文件中，并且少于1200行，包括详细的文档。
如果您希望看到Myna应用于更复杂的场景，请查看Chickadee编程语言 。 这完全在TypeScript中实现，并且仅取决于Myna解析库 。 Chickadee是一种微小的编程语言，专门用于帮助人们学习实现编程语言的技术。







































































































