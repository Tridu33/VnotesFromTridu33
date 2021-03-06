# JetBrains MPS











方言和特定领域的术语帮助人们进行特定而有效的交流。MPS将相同的灵活性带入了编程语言领域。与具有严格语法和语义的传统编程语言不同，MPS允许用户创建，更改或扩展一种语言。

扩展语言的核心问题主要在于解析器。解析器将代码的持久性表示形式与可视化表示符绑定在一起，并且它们无法轻松地与其他解析器结合使用，从而阻止了语言模块化。

这自然导致了程序代码的非文本表示的想法。这种方法的主要优点是消除了解析的需要。我们的解决方案是始终将代码维护在**抽象语法树 （AST）**，由具有属性，子级和引用的节点组成，并完整描述了程序代码。

MPS编辑器的任务是以一种用户友好的方式可视化AST，并提供有效编辑的手段。对于古典文字语言，编辑器应向用户提供以类似文本的方式编辑文本的幻觉，对于图形符号，另一方面，编辑器应养成行为良好的图表编辑器的习惯。

创建语言时，可以定义代码编辑和渲染的规则。您还可以指定语言类型系统和约束。这使MPS可以即时检查程序代码，从而使使用新语言进行编程变得容易且不易出错。

MPS使用生成方法。您可以为一种语言定义生成器，以将用户代码转换为以更常规的，通常是通用的语言编写的可编译代码。当前，MPS特别擅长但不限于生成Java代码。您还可以生成C，XML，FHTML，PDF，LaTeX，JavaScript等。

https://www.jetbrains.com/mps/learn/
