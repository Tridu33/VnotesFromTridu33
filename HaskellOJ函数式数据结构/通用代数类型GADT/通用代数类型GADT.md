<译> 简单的代数数据类型
https://blog.csdn.net/weixin_34161064/article/details/89477622



http://zhangyi.xyz/fp-and-domain-model/
函数范式与领域建模

**函数范式领域模型的核心要素为代数数据类型（Algebraic Data Type, ADT）和纯函数。**代数数据类型表达领域概念，纯函数表达领域行为。由于二者皆被定义为不变的、原子的，因此在类型的约束规则下可以对它们进行组合。可组合的特征使得函数范式建立的领域模型可以由简单到复杂，利用组合子来表现复杂的领域逻辑。



https://www.youtube.com/watch?v=YScIPA8RbVE


代数数据类型是什么？ - 王瑞瀚的回答 - 知乎
https://www.zhihu.com/question/24460419/answer/86175783


代数数据类型是什么？ - Jason Hu的回答 - 知乎
https://www.zhihu.com/question/24460419/answer/759928084


Algebraic Data Type 及其在 Haskell 和 Scala 中的表现

http://songkun.me/2018/07/12/2018-07-12-adt-in-haskell-and-scala/


在设计函数式领域模型时，需要遵守一些通用原则：
· 将不可变模型建模为代数数据类型（algebraic data type, ADT）。
· 在模块中将行为建模为函数，这里的模块是指一个粗糙的业务功能单元（比如一个领域服务）。这样，就将状态从行为分离了出来。行为比状态更好组合。因此，在模块中包含相关的行为有助于提升组合性。
· 记住，模块里的行为对ADT中的类型起作用。

引自 1.3 函数化思想

在设计函数式领域模型时，需要遵守一些通用原则：
· 将不可变模型建模为代数数据类型（algebraic data type, ADT）。
· 在模块中将行为建模为函数，这里的模块是指一个粗糙的业务功能单元（比如一个领域服务）。这样，就将状态从行为分离了出来。行为比状态更好组合。因此，在模块中包含相关的行为有助于提升组合性。
· 记住，模块里的行为对ADT中的类型起作用。
引自 1.3 函数化思想《函数响应式编程》>




# 1. GADT










GADT


https://en.wikibooks.org/wiki/Haskell/GADT








