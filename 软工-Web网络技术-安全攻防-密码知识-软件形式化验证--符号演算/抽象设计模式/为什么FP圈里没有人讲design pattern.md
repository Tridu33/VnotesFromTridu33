

怎么从本质上理解面向对象的编程思想？ - 大宽宽的回答 - 知乎
https://www.zhihu.com/question/305042684/answer/550196442

# 1. 为什么FP圈里没有人讲design pattern

函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - FounderSG的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/597126073



函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/143664626
没啥区别，比如

```
GoF <=> FP
Interpreter <=> Free Monad
Visitor <=> Catamorphism
Singleton <=> Reader Monad
Abstract Factory <=> Modules
Iterator <=> Traversable
AbstractSingletonProxyFactoryBean <=> Zygohistomorphic prepromorphisms
```


圣杯与银弹 · 没用的设计模式 https://draveness.me/holy-grail-design-pattern/




Why OO Sucks
函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - Kaichao的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/661170474









函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - FounderSG的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/597126073

如果有人给你一篇文章，洋洋洒洒数千言，旁征博引，证明了1+1=2，你看完云里雾里，一定觉得这肯定不是字面意义上的1+1=2而是某猜想，资质愚钝所以读不明白。等到某一天你知道这篇文章真的只是在讲字面意思上1+1=2你会怎么想？

当年看GoF的design pattern就不甚明白，排除翻译问题看了原版还云里雾里，直到有一天在F# for fun and profit网站看到一篇文章，解释为什么FP圈里没有人讲design pattern，以及一些所谓的design pattern对应在FP里是如何简单直白不值一提，我豁然开朗，再找来GoF的书读一读，只觉得太多废话太多术语太能忽悠了，真不该妄自菲薄这么多年。

所以我特能理解为什么搞FP的鄙视搞OO的。



# 2. 小云和小吉都很重要


函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - 大宽宽的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/530161703


为什么说面向对象编程和函数式编程都有问题 https://www.aqee.net/post/whats-wrong-with-oop-and-fp.html

有些东西不是对象。函数就不是对象。

有些东西不是纯的。副作用是真实存在的。










有仅支持一种范式的编程语言，例如 Haskell（纯函数式）。

还有支持多种范式的语言，例如 JavaScript，你可以用 JavaScript 编写面向对象的代码或函数式代码，甚至可以将两者混合。

js 面向对象编程(OOP) ps 函数式编程(FP)
https://juejin.cn/post/6844903917059309576




https://medium.com/@shaistha24/functional-programming-vs-object-oriented-programming-oop-which-is-better-82172e53a526






























































































