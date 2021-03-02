# recommendation logic to data

>在数据结构中排列代码块以实现替代的计算模型。


martinfowler.com/articles/refactoring-adaptive-model.html





自适应模型允许您在命令式语言中实现替代计算模型。为此，您可以定义一个模型，其中元素之间的链接表示计算模型的行为关系。该模型通常需要引用命令性代码部分。然后，您可以通过在模型上执行代码（过程样式）或在模型本身内执行代码（面向对象样式）来运行模型。



第47章中的DSL书

encode these using a JavaScript data structure of a list of two production rule objects and execute the model with a simple function.

他也用了json表达if-then rules