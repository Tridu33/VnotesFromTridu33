# 1. 王垠谈parser






https://github.com/AlexiaChen/YinWangBak/blob/master/%E8%B0%88%E8%B0%88Parser.md





我喜欢把parser称为“万里长征的第0步”，因为等你parse完毕得到了AST，真正精华的编译技术才算开始。


一个先进的编译器包含许多的步骤：**语义分析，类型检查/推导，代码优化，机器代码生成**，…… 这每个步骤都是在对某种中间数据结构（比如AST）进行分析或者转化，它们完全不需要知道代码的字符串形式。也就是说，一旦代码通过了parser，在后面的编译过程里，你就可以完全忘记parser的存在。

所以parser对于编译器的地位，其实就像ZIP之于JVM，就像JPEG之于PhotoShop。Parser虽然必不可少，然而它比起编译器里面最重要的过程，是处于一种辅助性，工具性，次要的地位。






















