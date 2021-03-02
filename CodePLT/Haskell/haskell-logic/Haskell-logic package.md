
https://www.reddit.com/r/haskell/comments/k6tqv1/logic_programming_in_haskell/ 埋伏他一手等社区回复





The Haskell Road to Logic, Maths and Programming. Second Edition (Texts in Computing)  https://www.amazon.com/Haskell-Logic-Programming-Second-Computing/dp/0954300696 教程

Theres是一种称为Curry的编程语言，它结合了Haskell和Prolog。

A typed logic programming language embedded in Haskell

https://github.com/acfoltzer/Molog


# Haskell-logic package



https://hackage.haskell.org/package/logict-state

 
https://hackage.haskell.org/package/logict-0.7.1.0/docs/Control-Monad-Logic.html


https://hackage.haskell.org/package/logict

https://hackage.haskell.org/package/logict-0.7.1.0/docs/Control-Monad-Logic-Class.html

为基于逻辑的评估提供支持。基于逻辑的编程使用一种称为回溯的技术将替代值视为逻辑语句的解决方案，并以诸如Prolog和 Datalog之类的语言来举例说明。

基于逻辑的编程用隐式功能代替显式的迭代和排序代码，这些隐式功能在满足明确提供的条件的一组可能值内部“迭代”（通过回溯）。

该软件包使用基于连续性的技术（其改编自 Oleg Kiselyov，Chung-chieh Shan，Daniel P.Friedman，Amr Sabry的论文《回溯，交织和端接Monad变压器》），为Haskell中基于逻辑的编程增加了支持 。本文将先前的研究扩展到了使用MonadPlus 功能（其中mplus用于指定要考虑的值替代品以及mzero用于指定缺少任何可接受值的用途）中，以使用由新MonadLogic类定义的一组操作来增加对公平性和修剪的支



在Prolog逻辑编程的一个典型示例中，有一组事实（表示为无条件语句）：

```
parent(sarah, john).
parent(arnold, john).
parent(john, anne).
```
以及一组满足条件（body子句）的规则：

```
grandparent(Person, Grandchild) :- parent(Person, X), parent(X, Grandchild).
```
执行此规则的查询grandparent(G, anne)将导致以下“值”：

```
grandparent(sarah, anne).
grandparent(arnold, anne).
```
对于此查询执行，Person并且X是Grandchild固定为的“免费”变量 anne。Prolog引擎在内部“回溯”该parent(Person, X)语句以尝试为每个变量使用不同的已知值，然后向前执行以查看这些值是否满足所有结果并产生结果值。





对于上面的示例，使用该logict程序包的Haskell等效项可能类似于以下内容：

```
import Control.Applicative
import Control.Monad.Logic

parents :: [ (String, String) ]
parents = [ ("Sarah",  "John")
          , ("Arnold", "John")
          , ("John",   "Anne")
          ]

grandparent :: String -> Logic String
grandparent grandchild = do (p, c) <- choose parents
                            (c', g) <- choose parents
                            guard (c == c')
                            guard (g == grandchild)
                            pure p

choose = foldr ((<|>) . pure) empty

main = do let grandparents = observeAll (grandparent "Anne")
          putStrLn $ "Anne's grandparents are: " <> show grandparents
```
在这个简单的示例中，每个choose调用都充当回溯选择点，parents 将在该回溯选择点生成数组的不同条目。该回溯是由MonadLogic实例自动处理的Logic，不需要显式地写入代码中。该observeAll函数收集由“产生”的所有值Logic，从而使该程序可以显示：

```
Anne's grandparents are: ["Sarah","Arnold"]
```
该示例作为软件包grandparents生成的可执行文件 提供，logict因此您可以自己运行它并尝试进行各种实验性修改。

上面的示例非常简单，只是对逻辑编程和logict程序包功能的简要介绍。该logict软件包提供了其他功能，例如：

合理的合取与析取，可以帮助潜在的无限输入集。

一个LogicTmonad堆栈，它允许逻辑操作与其他monadic动作一起执行（例如，如果父样本是使用IOmonad从输入文件中流式传输的）。

阿MonadLogic被定义，它允许其他单子类，其提供逻辑的编程能力。



该logict软件包中的实现提供了比相关论文中定义的功能低的回溯功能。回溯是在Alternative类 <|>和中定义的empty，而本文则使用MonadPlus类mplus和mzero函数。由于Alternative是的要求（约束）MonadPlus，因此这两种命名方式均受支持，并可以根据客户代码使用。

Haddock文档中提供了有关使用此软件包以及其他功能（包括公平合取和析取）的更多详细信息 。





























































































