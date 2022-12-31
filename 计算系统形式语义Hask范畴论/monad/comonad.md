
Monad和Comonad到底是什么东西？ - parker liu的回答 - 知乎
https://www.zhihu.com/question/31642688/answer/1147007286






Monad 的对偶概念comonad

extract 是 unit 的对偶，w a -> a

duplicate 是 join 的对偶 w a -> w (w a)













# 1. comonad








Comonad有什么实际用途？ - Patrick的回答 - 知乎
https://www.zhihu.com/question/55316968/answer/569687265



怎样用简单的语言解释 monad？ - 蔡和謙的回答
在上篇回答说过, Monad可以类比成建构工厂的过程, Comonad的用途刚好跟Monad相反, 是建构一个如何消耗产品的过程

可以这麽想, Monad建成的工厂不断产生出产品, 会产生一串待消耗的无穷串流, 至于如何消耗这无穷串流, 可以用Stream来建构, Stream可以用类似Monad的方式建构产品的消耗系统, 但Arrow方向相反, 于是Stream就是Comonad的特例