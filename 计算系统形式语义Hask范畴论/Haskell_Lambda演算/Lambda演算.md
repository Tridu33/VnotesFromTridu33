





《Type theory and Formal Proof An Intruduction》


ruby实现lambda演算

https://github.com/tomstuart/nothing
最初是作者的博客文章，叫Programming with Nothing
https://rubywebapp.com/
@knifefire 666.这么说好多书都源自博客呀，martin的《DSL》,《数学之美》......才知道作者正忙着出新书用Ruby编写Web应用程序原型







# 1. Lambda演算

https://thzt.github.io/2015/04/11/lambda-calculus/ Lisp程序员眼中的λ演算

形式系统是一套符号化的系统，

这些符号，遵循了某些规则，

模型化了待研究的现实世界。



例如：

(lambda (x) x)

是由符号“(”，“)”，“lambda”和“x”构成的。

它们符合“S表达式”的语法规则，

以及Lisp函数调用的推导规则，

表示了一个数学函数f(a)=a。



区分符号和它指称的事物，

是很重要的。



我们要研究的这些符号构成了一种语言，

称为目标语言。

而符号所指称的事物也构成了一种语言，

称为元语言。



例如：

符号1，我们通常认为它是自然数1。

但这只是通俗的说法。



事实上，符号1，符号2，符号3，…属于目标语言范围，

而自然数1，自然数2，自然数3，…属于元语言范围。



符号1和自然数1是不同的，

如果愿意，我们当然可以用符号a表示自然数1。



λ演算——形式语法
λ演算系统，是一个形式系统，

用来研究编程语言。



在内容上，大体分为几个部分。

形式语法，公理语义，不动点，操作语义，指称语义。



形式语法，

用来说明合法表达式的组成方式。

定义如下：

M ::= x | MM | λx.M



这是一个递归定义，

它表示，在λ演算系统中，合法的表达式，

要么是一个变量x，

要么是一个函数调用（application），

要么是一个函数抽象（lambda abstraction）。



例如：如下表达式就是合法的，

x，变量x

(λx.x)5，函数调用

λx.y，函数抽象



我们看到合法的lambda表达式，

在语法上和Lisp中的S表达式很相似。



x <=> x

(λx.x)5 <=> ((lambda (x) x) 5)

λx.y <=> (lambda (x) y)



事实上，Lisp语言的语法，

确实受到了λ演算的影响。



在不影响歧义的情况下，

我们将采用Lisp语言来讨论λ演算。

因为，他们可以看做只是语法不同的两套形式系统。



λ演算——公理语义
公理语义，

是一套等式证明系统，

用来区分一个形式系统中的两个表达式，

是不是等价。



正如不同的语法规则，给出了不同的形式语言，

不同的等价性条件，给出了有不同公理语义的形式系统。



给λ演算添加不同的等价性规则，

会导致不同的λ演算系统。



最常用的两种等价规则是，

α等价，和β等价。



α等价指出，

函数的形参只是占位符，

替换形参和函数体中相应名字的符号，

所产生的新表达式与原表达式等价。



例如：

(lambda (x) x)和(lambda (y) y)

是等价的。



这里还没有谈到这两个表达式的指称语义。

无论这些符号指称什么，

在公理语义的约束下，都是等价的。



β等价指出，

函数调用表达式，等价于，

把函数体中的形参替换成实参后的表达式。



例如：

((lambda (x) (+ a x)) y)等价于(+ a y)



需要注意的是，

实参含有自由变量，

可能会与替换后环境中的绑定变量冲突。



例如：

(

    (lambda (x)

        (lambda (y)

            (+ x y)))

    (- a y)

)



如果我们单纯把形参x替换成(- a y)

结果如下：

(lambda (y)

    (+ (- a y) y))

其中，函数体(+ (- a y) y)中，

第一个y就会被绑定的符号y所捕获。



这容易引起歧义，

因此，在这种情况下，我们需要为绑定变量更名。即，

(lambda (z)

    (+ (- a y) z))



λ演算——不动点
我们看到λ演算中，所有函数都是匿名的，

这样在函数体内部引用函数本身，是很困难的事情。



例如，阶乘函数，

(define fact

    (lambda (n)

        (if (= n 1)

            1

            (* n (fact (- n 1))))))

函数内部引用了函数本身。



改写成等式形式，

fact = (lambda (n)

    (if (= n 1)

        1

        (* n (fact (- n 1)))))

我们发现，在等式两边都出现了fact。



这使得我们回忆起了代数学中，

求解以下方程式。

x = G(x)。



其中，

G(f) = (lambda (n)

    (if (= n 1)

        1

        (* n (f (- n 1)))))

或，

G = (lambda (f)

        (lambda (n)

            (if (= n 1)

                1

                (* n (f (- n 1))))))



待求取的函数fact，是这个方程的解。即，

fact = G(fact)。

我们称，方程x = G(x)的解为函数G的不动点。



那么这个方程有解吗？

幸运的是，人们已经找到了求解不动点的办法。



方法如下：

人们发现存在一个称为Y组合子（Y combinator）的函数，

可以得到任意函数G的不动点。即，

令x = YG，则x = G(x)



因此，上例中，

fact = YG



其中，

Y = (lambda (k)

        ((lambda (g) (g g))

        (lambda (f)

            (lambda (n)

                ((k (f f))

                n)))))

                

这里需要注意，Y本身不是G的不动点，

YG才是。



λ演算——操作语义
操作语义，

是一套推导规则，

据此表达式可以规约成更简单的形式。



与等式证明系统不同的是，

推导规则具有方向性。



相同之处在于，

在不同个数规约规则的限制下，

得到了不同的λ演算系统。



最常用的规约规则，称为β规约。

它是β等价的有向形式。



记法如下：

((lambda (x) (+ a x)) y) -> (+ a y)



另外，某些表达式，β规约不可终止的。

例如：

(

    (lambda (x)

        (x x))

    (lambda (x)

        (x x))

)

->

(

    (lambda (x)

        (x x))

    (lambda (x)

        (x x))

)

-> …



对于β规约可终止的表达式，人们发现，

按不同的次序，对表达式进行规约，

总是可以得到相同的最终表达式，

称为范式（normal form）。

这种性质，称为汇聚性（confluence）。



λ演算——指称语义
指称语义，

是通过为每一个表达式指定一个数学对象，

作为该表达式的指称，

来说明表达式语义的一种办法。



能这样做，是建立在语义合成性（compositionality）前提之下的。

即，表达式的语义，只由它的子表达式语义决定。



例如：

对于加法表达式，

(+ 1 2)



符号+，指称数学函数，加法函数，

符号1，指称自然数1，

符号2，指称自然数2。



整个表达式指称，自然数1与自然数2的加法操作。



记为：
E[[+]] = 加法函数

E[[1]] = 自然数1

E[[2]] = 自然数2

E[[e1+e2]] = E[[e1]]+E[[e2]]

其中，等式右边的+表示自然数加法操作。



结语
λ演算虽然语法简单，但是内涵丰富，

这很符合Scheme语言的设计哲学。



从模型论的角度来看，

如果说物理学是对现实世界的建模，

那么程序设计语言，就是对计算的建模。



λ演算和其他编程语言一样，采用形式方法，

用满足特定规则的一组符号，

建立了计算模型。



图灵机，递归函数论等，采用了其他方式建模，

虽然复杂一些，但是与λ演算具有相同的计算能力。



λ演算很值得学习，

会了解到很多数学上的基础问题，

集合论，证明论，递归论，模型论，

都有不同程度的应用。


















[认知科学家写给小白的Lambda演算https://zhuanlan.zhihu.com/p/30510749](https://zhuanlan.zhihu.com/p/30510749)



终极lambda
http://lambda-the-ultimate.org/



lambda算子系列5b
https://blog.csdn.net/g9yuayon/article/details/1271319







[Lambda calculus引论(目录)
https://zhuanlan.zhihu.com/p/29456156](https://zhuanlan.zhihu.com/p/29456156)







[雾语魔法店https://zhuanlan.zhihu.com/marisa](https://zhuanlan.zhihu.com/marisa)



This is the latex source of Type and proof, a short article about logic, type system, lambda calculus, and curry howard isomorphism.

There may be some mistakes and it is not completed yet. Issues and pull requests are welcomed!

TODO

denotational semantic of UTLC and STLC
logical relation and its applications
C-H isomorphism under sequent calculus
type inference of STLC
type checking VS. proof checking
\beta and \eta reduction VS. prooving
cut elimination and it's role in C-H isomorphism
intro to proof search
intro to category theory
algebra semantic of logic and STLC
intro to lambda cube
linear logic and lienar type
substructural logic and substructural type
focusing/polarizing in type theory
First order logic
basic model theory
Contributors

https://github.com/OpenPAL/TypeAndProof/graphs/contributors

How to publish the PDF
https://openpal.github.io/TypeAndProof/ is where we publish. Here are several steps:

Generate the PDF file from source
Clone another copy of this repo, named like TypeAndProof-www
In that new repo, check out into the gh-pages branch
Copy the new version of PDF here
git add --all; git commit -m "Update PDF"
Make a PR or something to that particular branch




https://github.com/OpenPAL/TypeAndProof

lambda演算对计算理论领域有什么贡献？https://qastack.cn/cstheory/21705/what-is-the-contribution-of-lambda-calculus-to-the-field-of-theory-of-computatio



https://qastack.cn/cstheory/625/relationship-between-turing-machine-and-lambda-calculus  图灵机与Lambda演算之间的关系



可实现性理论：Lambda微积分和图灵机之间的power差异

https://qastack.cn/cstheory/1117/realizability-theory-difference-in-power-between-lambda-calculus-and-turing-mac






chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/file:///C:/Users/HUMAN/Desktop/lambda%E6%BC%94%E7%AE%97.pdf B站视频对应文档


诸多Lambda演算

•λ_omega

•SystemF实现了某些程序语言里的多态（polymorphism）

•依赖类型（dependenttype）λP

•lambdacube









