
《A History of Erlang》

Worse is Better 的原文：“The good news is that in 1995 we will have a good operating system and programming language; the bad news is that they will be Unix and C++.”


为啥 Erlang 没有像 Go、Scala 语言那样崛起？ - 布丁的回答 - 知乎
https://www.zhihu.com/question/38032439/answer/84176970

# Worse is Better
函数式 + 消息 + 分布式



软件设计有以下四大目标：简单、正确、一致、完整。

但两大流派 MIT Style (MIT AI Lab 是 LISP 重镇) 和 New Jersey Style (C 和 UNIX 的老家贝尔实验室所在地) 对这些目标的优先级排序不同。MIT Style 认为软件正确性要绝对保证，然后优先级 正确 ~= 一致 > 完整 > 简单，简单这一条还得分，为了接口简单，可以忍受实现复杂。而 New Jersey Style 是正好反过来：首先软件实现得简单，做不到宁愿让接口复杂点，为了简单显然可以牺牲完整性，而正确、一致，那就尽力吧…… 反正得简单。

Worse is Better 也能解释别的语言或技术的崛起。你不用很优秀但要有一个点做得好打到痛点，你不用设计完美但至少别犯大错，然后保持简单，保证好上手**易移植**易与现有系统**整合**，就可以了。
