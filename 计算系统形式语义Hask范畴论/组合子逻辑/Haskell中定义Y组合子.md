
如何理解面向组合子编程? - 何幻的回答 - 知乎
https://www.zhihu.com/question/26352139/answer/101033939

可以读一下这本书：Lambda-Calculus and Combinators (豆瓣)
本书对比了lambda演算和combinatory logic，这是两套简洁但图灵完备的形式系统。

人们经常提到的是lambda演算，很多函数式语言可以建立在这套系统之上，
（另外TAPL也是从untyped lambda演算讲起的。。
它引入了变量绑定，更名，函数应用等概念，确实是大多数编程语言的抽象版本。


而combinatory logic提到的人不多，虽然它形式上更简洁一些，去掉了绑定这一层，
只是几个组合子互相作用来进行演算。（然后居然还可以与lambda演算图灵等价。








Y不动点组合子用在哪里？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/21099081/answer/23893046

用来实现递归。
在正统的 Lambda 演算里函数全部是没有名字的，因此递归函数无法实现


任务就是写出一个闭合的 Lambda 表达式和 Y 等效，所幸 Haskell B. Curry 找到了一个


Y不动点组合子用在哪里？ - 红日照小池的回答 - 知乎
https://www.zhihu.com/question/21099081/answer/18830200
不动点理论
博文重新发明 Y 组合子 Python 版）。http://picasso250.github.io/2015/03/31/reinvent-y.html js 王垠lisp实现 http://picasso250.github.io/2015/03/31/reinvent-y.html







# 1. Haskell中定义Y组合子





在Haskell中定义Y组合子 - 湖海平生洛可可的文章 - 知乎
https://zhuanlan.zhihu.com/p/137588848








Y Combinator 的名字是怎样来的？有什么故事？ - Rio的回答 - 知乎
https://www.zhihu.com/question/19849896/answer/13148866





推导Y组合子 - 湖海平生洛可可的文章 - 知乎
https://zhuanlan.zhihu.com/p/137588168



















