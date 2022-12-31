# CodeWar-Parser题










使用 Haskell 编写灵活的 Parser （下） - 药罐子千里冰封的文章 - 知乎
https://zhuanlan.zhihu.com/p/28162006

CodeWars Challenges
这里列出一些我认为很有趣的 CodeWars 的 Parser 题。我建立了一个 collection 来收藏相关题目， 感兴趣的同学可以去做一下。

下面分别介绍一下各个题目。

Operator Parser
此题非常新颖，给你一个结合性的 List ，里面放的是以优先级排序的二元中缀符号的 Parser ， 然后你需要把它们组合起来成为一个大的表达式 Parser 。这题一看就知道是 foldr/foldl ，哈哈。

前文所使用的 OpTree 就是这道题里面的。

Writing Applicative Parsers From Scratch
此题禁止你使用 Control.Applicative, Prelude 的 fmap 和 Data.Functor（我觉得它很 SB 的一点在于它没有禁止你使用 <$>）， 然后让你从 0 开始写一个 Applicative 的 Parser 。

Regular Expression Parser
这个题目是让你解析正则表达式的，需要特别注意一些结合性的问题（这道题我的解法比较 dirty ，特判了两组数据）。做这题的时候我不知道有 chainr1 ，结果写出来的代码很伤。

Tiny Three Pass Compiler
老经典的题，支持很多语言，写起来贼爽。








