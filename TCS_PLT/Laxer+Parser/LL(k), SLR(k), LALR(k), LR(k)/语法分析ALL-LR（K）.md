# 语法分析ALL-LR（K）











ALL(*)语法分析器
LR(*)与LL(*)
现在主流的语法分析器分两大阵营，LR(*)与LL(*)。

LR是自低向上（bottom-up）的语法分析方法，其中的L表示分析器从左（Left）至右单向读取每行文本，R表示最右派生（Rightmost derivation），可以生成LR语法分析器的工具有YACC、Bison等，它们生成的是增强版的LR，叫做LALR。

LL是自顶向下（top-down）的语法分析方法，其中的第一个L表示分析器从左（Left）至右单向读取每行文本，第二个L表示最左派生（Leftmost derivation），ANTLR生成的就是LL分析器。


确定性自上而下之中：递归向下分析recursive decent parsing为语法中每个词规则定义一个函数。每个函数处理输入句子中符合其规则的短语或者部分。最顶端函数对应规则，规则左边有开始符号。解析器按照语法规则下降。递归下降分析器的构造方法非常简单，简单来说，就是为每一个非终结符写一个递归函数，函数中对该终结符可能转换成的所有情况的第一个token进行判断，做出对应的处理。**消除左递归，提取左因子**

两类分析器各有其优势，适用不同的场景，很难说谁要更好一些。普遍的说法是LR可以解析的语法形式更多，LL的语法定义更简单易懂。

ALL(*)原理
ANTLR从4.0开始生成的是ALL(*)解析器，其中A是自适应（Adaptive）的意思。ALL(*)解析器是由Terence Parr、Sam Harwell与Kathleen Fisher共同研发的，对传统的LL(*)解析器有很大的改进，ANTLR是目前唯一可以生成ALL(*)解析器的工具。

ALL(*)改进了传统LL(*)的前瞻算法。其在碰到多个可选分支的时候，会为每一个分支运行一个子解析器，每一个子解析器都有自己的DFA（deterministic finite automata，确定性有限态机器），这些子解析器以伪并行（pseudo-parallel）的方式探索所有可能的路径，当某一个子解析器完成匹配之后，它走过的路径就会被选定，而其他的子解析器会被杀死，本次决策完成。也就是说，ALL(*)解析器会在运行时反复的扫描输入，这是一个牺牲计算资源换取更强解析能力的算法。在最坏的情况下，这个算法的复杂度为O(n4)，它帮助ANTLR在解决歧义与分支决策的时候更加智能。



https://liangshuang.name/2017/08/20/antlr/






ANTLR语法库
在GitHub上有一个ANTLR 4语法库：https://github.com/antlr/grammars-v4，里边有几乎所有常见语言的语法文件。就算是要设计一个新的语言，也应该首先到这里借鉴一下，对于一些基本的符号定义，比如字符串，整形数字等完全可以照搬过来。

参考
《The Definitive ANTLR 4 Reference》- Terence Parr
Adaptive LL(*) Parsing: The Power of Dynamic Analysis
Comparison of parser generators
Youtube Video: ANTLR v4 with Terence Parr




