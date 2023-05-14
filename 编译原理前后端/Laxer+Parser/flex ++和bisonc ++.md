# flex ++和bisonc ++




flex和bison生成的解析器是C代码而且它们不是重新检测的。 谷歌搜索，我发现了flex ++和bisonc ++。 不幸的是，没有简单的入门教程。 大多数例子都基于bison / flex。 

有些人以某种方式将bison / flex解析器集成到他们的C ++代码中。

flex ++和bisonc ++的文档对我和我没有帮助。 教程和示例，它们都从stdin获取输入并在stdout上打印一些消息。





我在解析器中需要这些功能：

解析器应该是一个C ++类，以正常方式定义（头文件和cpp文件）

解析器从std :: string或std :: stringstream或以null终止的char *接收数据。

我感到很困惑。 我应该使用flex ++ / bisonc ++还是flex / bison？ 如何做到这一点，满足上述条件？










有flex / bison，flex ++ / bison ++和flexc ++ / bisonc ++。我认为最好选择这三对中的一对，而不是混合/匹配flex ++和bisonc ++。以下是Flexc ++和Bisonc ++的用户教程。

来自Flexc ++网站：

与flex和flex ++相反，Flexc ++生成明确打算供C ++程序使用的代码。众所周知的flex（1）程序生成C源代码，而flex ++（1）仅围绕由flex（1）生成的yylex函数提供类似C ++的shell，并且几乎不支持当前关于C ++软件开发的想法。与此相反，flexc ++创建了一个C ++类，它提供了一个预定义的成员函数lex，匹配正则表达式的输入，并在正则表达式匹配时可能执行C ++代码。 flexc ++生成的代码是纯C ++，允许其用户应用该语言提供的所有功能。

来自Bisonc ++网站：

Bisonc ++是一个通用的解析器生成器，它将LALR（1）无上下文语法的语法描述转换为C ++类来解析该语法。一旦熟练掌握了bisonc ++，就可以用它来开发各种语言解析器，从简单的桌面计算器到复杂的编程语言。 Bisonc ++与Alain Coetmeur编写的程序bison ++高度可比：所有正确编写的bison ++语法应该在很少或没有变化后转换为bisonc ++语法。任何熟悉bison ++或其前身，野牛的人都应该能够轻松使用bisonc ++。您需要熟练使用C ++编程才能使用bisonc ++或理解本手册。

因此，flexc ++ / bisonc ++不仅仅是旧的flex / bison实用程序的包装器。它们生成完整的C ++类，用于重入扫描/解析。


















