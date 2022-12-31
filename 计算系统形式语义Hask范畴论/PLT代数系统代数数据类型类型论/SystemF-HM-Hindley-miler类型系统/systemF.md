GitHub - Zepheus/SystemF: A System F implementation in Haskell
https://github.com/Zepheus/SystemF

 GitHub - kseo/systemf: An implementation of System F in Haskell
https://github.com/kseo/systemf







https://crypto.stanford.edu/~blynn/lambda/systemf.html
简单类型的 lambda 演算是有限制的。Hindley-Milner的 let 多态性给了我们更多的喘息空间，但我们能做得更好吗？

# System_F 二阶lambda演算

System F 通过在类型级别引入部分 lambda 演算进一步释放了类型系统。我们有类型抽象术语和类型应用 术语，它们定义和应用将类型作为参数并返回术语的函数。与此同时，系统 F 仍在正常化。

系统 F 足够丰富，以至于自我应用程序\xx x是可键入的。


https://en.wikipedia.org/wiki/System_F 二阶lambda演算


二阶逻辑源于 Gottlob Frege 对谓词逻辑的最初介绍，它已经区分了两种不同类型的量化（变量或谓词），但没有将它们作为不同的逻辑分开。当伯特兰·罗素阐述罗素悖论时，他开始区分一阶逻辑和二阶逻辑， 二阶逻辑比一阶逻辑具有更大的表达能力。这种更强的表达能力使得公理化更复杂的数学系统成为可能。也就是说，有些命题不能用一阶逻辑的形式主义精确地形式化，而可以用二阶逻辑正确地形式化。毫无疑问，这最后一个事实构成了一个优势，然而，二阶逻辑的使用涉及某些困难：紧致定理，它指出一阶逻辑的一组逻辑命题是令人满意的当且仅当任何有限的子集这些命题是可满足的，它不适用于二阶逻辑。Löwenheim-Skolem 定理指出，具有有限数量不同符号的一阶逻辑承认可数模型对二阶逻辑无效。 事实上，这两个定理在某些应用中非常有用，但它们不是可以推广到二阶逻辑并降低二阶逻辑对这些应用程序的有用性











SystemF 对应二阶逻辑，Fω 对应高阶逻辑，这个阶是怎么算得？ - Jason Hu的回答 - 知乎
https://www.zhihu.com/question/321025032/answer/702580771


你本质上是在问first order logic、higher order logic里这个order是怎么来的。根本来说，这个order是衡量universal quantifier可以quantify什么object。

从最基础地说，zero order logic是propositional logic。它只有与或和implication，并且操作与给定的symbols里。这个symbols的集合叫做universe或者sort。propositional logic没有quantifier。这是很弱的逻辑，对应的编程语言没有generics。在lambda cube里对应的是simply typed lambda calculus。implication对应简单的函数空间。

加上quantifier以后，包括universal quantifier和existential quantifier，问题就不一样了。首先，你得界定quantifier可以quantify什么东西。first order logic限定universal quantifer只能quantify整个sort或者universe。比方如果你用first order logic描述数字，那么你首先需要定义以下的sort。





[公式]

/x的意思是定义symbol 的arity。比方说0/0的意思是0是一个arity为0的symbol，也就是常量。isNum的arity为1，所以是predicate等。

那么你可能会有以下句子。

[公式]

这个句子的a和b quantify这个universe，包括isNum和+，但是isNum对isNum和+是伪，所以不能apply这个句子。

这是first order logic，对应与 [公式] 也就是simply typed lambda calculus + dependent types.

Second order logic允许高一阶的quantification，也就是允许universal quantification over parameterized symbols。举个例子，

[公式]

这个P的sort是 [公式] 也就是说它是任一arity为1的symbol。这句话的意思是对于所有a和b，如果P成立，那么a + b的P也会成立。这句话在first order logic是无法表达的。当然这句话对不对取决于universe，而且真伪也不重要。

你再看看F，F允许你定义universal type，根据Curry-Howard Isomorphism对应的是quantification over sort，当然就是second order logic。

至于higher order logic，则允许诸如 [公式] 这样的sort。这些都可以在 [公式] 表达。











有没有高阶函数,first-order variables,first-class相关资料推荐？ - 知乎
https://www.zhihu.com/question/531333309









# systemF

https://en.wikipedia.org/wiki/System_F

它由逻辑学家Jean-Yves Girard和计算机科学家John C. Reynolds独立发现的。

Wells的结果暗含着系统F的类型推论是不可能的。


本文用的系统F版本是显式类型的,或邱奇风格的演算。

相反的,介入了多态类型(如系统F)或依赖类型(如逻辑框架)的系统不被当作是简单类型。

各种有类型 lambda 演算系统包括简单类型 lambda 演算,Jean-Yves Girard 的系统F,和 Thierry Coquand 的构造演算都有规范化性质。

系统F通过在所有类型上的全称量化允许多态性;从逻辑的观点看它可以描述可证明在二阶逻辑中是全函数的所有函数

简单类型λ演算,一种高阶逻辑; 直觉类型论; 系统F; LF经常用来定义其他类型论; 构造演算及其衍生理论。

Joe Wells(1994)设立了一个"难为人的公开问题",证明系统 F的Curry-风格的变体是不可判定的,它缺乏明显的类型提示。这意味着有可计算函数不能在简单类型的 lambda 演算中定义(类似的有可计算函数不能在构造演算或系统 F 中计算)。


一个限制版本的系统F叫做"Hindley-Milner",或简称"HM",有一个容易的类型推论算法,并用于了很多强类型的函数式编程语言,比如Haskell和ML。














# Lambda cube



https://en.wikipedia.org/wiki/Lambda_cube


基于Berardi的工作,Barendregt提议了Lambda立方体来系统化纯有类型lambda演算(包括简单类型lambda演算,系统F、LF和构造演算)之间的关系。








