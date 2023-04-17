# 机器人编程课程等










科大评课社区

https://icourse.club






https://icourse.club/course/3547/




这门课名为《机器人编程入门》，事实上是在讲智能机器人的基础理论——**知识表达与推理、自然语言处理**等。很多人选了这个暑期学期的课，是为了参加 Robogame 机器人比赛的，结果发现完全不是讲这个的。

知识表达用的是命题逻辑，推理方法用的是 **Answer Set Programming**，一种类似 Prolog 的逻辑编程语言。 [https://en.wikipedia.org/wiki/Answer\_set\_programming](https://en.wikipedia.org/wiki/Answer_set_programming)

作业是用 clingo 推理器来解演绎推理（deductive reasoning）、数独、多米诺骨牌覆盖问题、拉姆塞问题。我还加做了四色问题、八皇后问题、最大团问题、中国邮递员问题等。把这些 NP-hard 问题映射到命题逻辑之后，clingo 都可以在可接受的时间内得到解，比 C 语言写的暴搜 + 剪枝快多了。当然针对上述经典问题，都有特定的算法可以加速搜索，这种特殊算法肯定是比 clingo 快的。然而逻辑编程是一种解决类 SAT 问题的通用解法，对于并不那么规则的现实中的知识推理问题，是很有用的。

代码： [https://github.com/bojieli/answer-set-assignment](https://github.com/bojieli/answer-set-assignment)

自然语言处理部分讲的是经典的**基于规则的自然语言语法树分析**。就是编译原理里面词法分析、语法分析那一套。作业是写一个解析几种简单英文句子语法树的词法和语法分析器。

代码： [https://git.ustclug.org/boj/natural-language-parser/tree/master](https://git.ustclug.org/boj/natural-language-parser/tree/master)

如果以后这门课程仍然开的话，选修前建议先修数理逻辑和编译原理。



















