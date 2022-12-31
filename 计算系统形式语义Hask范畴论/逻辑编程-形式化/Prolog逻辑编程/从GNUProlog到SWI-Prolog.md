# 从GNUProlog到SWI-Prolog
www.lamda.nju.edu.cn/daiwz/slides/Abduction.html#/slide-org66c668c
神奇的在线PPT

-   [SWI-Prolog](http://www.swi-prolog.org/): Prolog解释器
-   [YAP Prolog](https://github.com/vscosta/yap-6.3): 速度更快的Prolog解释器
-   [Metagol](https://github.com/metagol/metagol): Meta-Interpretive Learning
-   [PySwip](https://github.com/yuce/pyswip): Python调用Prolog的包







牛逼哄哄的作者，还有很多关于Prolog的文章，可以点进去链接看





[从GNU Prolog转换到SWI Prolog](http://blog.sina.com.cn/s/blog_4513dde60102vs81.html)

2012年看了*Seven Languages in Seven Weeks*之后，就对Prolog非常感兴趣。虽然日常工作中几乎用不到，但这门与众不同的语言总是非常吸引我。试着用它解了几个问题（见[《用GNU Prolog算Magic Hexagon》](http://blog.sina.com.cn/s/blog_4513dde60101hhmd.html)，[《用Prolog解狐狸、鹅、豆子问题》](http://blog.sina.com.cn/s/blog_4513dde60101hihy.html)，[《在Matlab中调用Prolog（一）》](http://blog.sina.com.cn/s/blog_4513dde60101hk9k.html)，[《传教士，恶魔，贪心的丈夫和夫人们》](http://blog.sina.com.cn/s/blog_4513dde60101hm1e.html)，[《Finite Domain Constraint Solver是个宝》](http://blog.sina.com.cn/s/blog_4513dde60102vrh2.html)，[《用Prolog求解操作数间合适的运算符》](http://blog.sina.com.cn/s/blog_4513dde60102vs5c.html)），感觉非常不错，用它编程的时候感觉到它能让我从不同的角度看待问题。  
    由于这本书使用GNU Prolog来介绍这门语言，所以我一直用的也是GNU Prolog。但是最近我了解到SWI Prolog似乎比GNU Prolog提供了更丰富的功能和更完善的环境，因此打算迁移到SWI Prolog中。作为两种不同的Prolog，两者有些许差异，尤其是使用了扩展功能的GNU Prolog代码，需要一定的修改才能在SWI Prolog中运行。  
    值得高兴的一点，SWI Prolog像GNU Prolog一样，提供了Finite Domain的扩展，但是语法形式不太一样。之前在[《用GNU Prolog算Magic Hexagon》](http://blog.sina.com.cn/s/blog_4513dde60101hhmd.html)给出的GNU Prolog代码无法直接在SWI Prolog中运行，查看文档中关于clpfd的内容（见[http://www.swi-prolog.org/man/clpfd.html](http://www.swi-prolog.org/man/clpfd.html)），并进行相应修改之后，终于可以用SWI Prolog运行了。代码如下：  
  
% 2012.06.12 PM 10:51 Created  
% 2015.09.30 AM 10:02 Modified  
% SWI Prolog  
% magichex.pl  
% xialulee  
  
:- use_module(library(clpfd)).  
  
check38(X, Y, Z) :- X+Y+Z #= 38.  
check38(W, X, Y, Z) :- W+X+Y+Z #=38.  
check38(V, W, X, Y, Z) :- V+W+X+Y+Z #= 38.  
  
magichex(Solution) :-  
  Solution = \[  
            A1,   A2,   A3,  
        A4,   A5,   A6,   A7,  
    A8,   A9, A10, A11, A12,  
        A13, A14, A15, A16,  
           A17, A18, A19  
  \],  
  Solution ins 1..19,  
  all_different(Solution),  
  
  check38(A1, A2, A3),  
  check38(A4, A5, A6, A7),  
  check38(A8, A9, A10, A11, A12),  
  check38(A13, A14, A15, A16),  
  check38(A17, A18, A19),  
  
  check38(A1, A4, A8),  
  check38(A2, A5, A9, A13),  
  check38(A3, A6, A10, A14, A17),  
  check38(A7, A11, A15, A18),  
  check38(A12, A16, A19),  
  
  check38(A3, A7, A12),  
  check38(A2, A6, A11, A16),  
  check38(A1, A5, A10, A15, A19),  
  check38(A4, A9, A14, A18),  
  check38(A8, A13, A17),  
  
  label(Solution).  
  
几处修改如下：  

-   不同于GNU Prolog内置了Finite Domain Solver，SWI Prolog中的Finite Domain支持是以库的形式存在的，所以在代码一开始需要添加一句“:- use_module(library(clpfd)).”;
-   GNU Prolog使用fd_domain来限定变量的可行域，而在SWI Prolog的CLPFD中使用ins运算符，如代码中的“Solution ins 1..19,”;
-   GNU Prolog中fd\_all\_different在SWI中的对应物为all_different；
-   GNU Prolog中的fd_labeling在SWI中的对应物为label。  
    

修改完成之后，在SWI Prolog的交互界面中加载代码文件：  
2 ?- \['c:/lab/prolog/magichex.pl'\].  
true.  
  
加载成功。试着对问题进行求解：  
3 ?- magichex(Solution).  
Solution = \[3, 17, 18, 19, 7, 1, 11, 16, 2|...\]  
  
然而结果在显示的时候并不完全，只显示了变量中的九个，还有十个没有显示出来，用...表示了。如何让它显示出全部的变量呢？看了[http://www.verydemo.com/demo\_c230\_i3607.html](http://www.verydemo.com/demo_c230_i3607.html)才知道，此时按下w即可让其输出完整的一组解（按下h可以查看所有可用命令）：  
3 ?- magichex(Solution).  
Solution = \[3, 17, 18, 19, 7, 1, 11, 16, 2|...\] \[write\]  
Solution = \[3, 17, 18, 19, 7, 1, 11, 16, 2, 5, 6, 9, 12, 4, 8, 14, 10, 13, 15\] ;  
  
不同于GNU Prolog，命令a不是用来输出所有的解，而是终止搜索。想要得到下一组解，可以按下分号“;”，如何一次性输出所有的解，我还不知道。全部的输出如下所示：  
3 ?- magichex(Solution).  
Solution = \[3, 17, 18, 19, 7, 1, 11, 16, 2|...\] \[write\]  
Solution = \[3, 17, 18, 19, 7, 1, 11, 16, 2, 5, 6, 9, 12, 4, 8, 14, 10, 13, 15\] ;  
Solution = \[3, 19, 16, 17, 7, 2, 12, 18, 1, 5, 4, 10, 11, 6, 8, 13, 9, 14, 15\] ;  
Solution = \[9, 11, 18, 14, 6, 1, 17, 15, 8, 5, 7, 3, 13, 4, 2, 19, 10, 12, 16\] ;  
Solution = \[9, 14, 15, 11, 6, 8, 13, 18, 1, 5, 4, 10, 17, 7, 2, 12, 3, 19, 16\] ;  
Solution = \[10, 12, 16, 13, 4, 2, 19, 15, 8, 5, 7, 3, 14, 6, 1, 17, 9, 11, 18\] ;  
Solution = \[10, 13, 15, 12, 4, 8, 14, 16, 2, 5, 6, 9, 19, 7, 1, 11, 3, 17, 18\] ;  
Solution = \[15, 13, 10, 14, 8, 4, 12, 9, 6, 5, 2, 16, 11, 1, 7, 19, 18, 17, 3\] ;  
Solution = \[15, 14, 9, 13, 8, 6, 11, 10, 4, 5, 1, 18, 12, 2, 7, 17, 16, 19, 3\] ;  
Solution = \[16, 12, 10, 19, 2, 4, 13, 3, 7, 5, 8, 15, 17, 1, 6, 14, 18, 11, 9\] ;  
Solution = \[16, 19, 3, 12, 2, 7, 17, 10, 4, 5, 1, 18, 13, 8, 6, 11, 15, 14, 9\] ;  
Solution = \[18, 11, 9, 17, 1, 6, 14, 3, 7, 5, 8, 15, 19, 2, 4, 13, 16, 12, 10\] ;  
Solution = \[18, 17, 3, 11, 1, 7, 19, 9, 6, 5, 2, 16, 14, 8, 4, 12, 15, 13, 10\] ;  
false.  
  
各解的输出顺序与GNU Prolog完全一致，大概两者构造的搜索树也是完全一样的。但是SWI Prolog在求解的过程中可以感觉到明显的延迟（秒量级），不像GNU Prolog那样瞬间输出。难道GNU Prolog的Finite Domain Solver相比SWI有明显的性能优势？也许SWI和GNU Prolog的关系类似于gawk和mawk的关系（功能丰富/性能优异）？  
    接下来试试前几天由表达式列表构造表达式树并执行的代码。这里基本上没有使用什么扩展功能，原以为可以不加修改的执行，但是在SWI Prolog中加载时还是报错了，说没有名为nth的东西。nth是我在构造表达式树时用来获取列表中优先级最低的运算符用的。大概nth是GNU Prolog的扩展。我查了一下，SWI Prolog确实没有  
nth，但是更好的是，它提供了nth0和nth1，可以让我们选择用0还是1作为列表第一个元素的下标：  
22 ?- nth0(2, \[a,b,c,d\], Elem).  
Elem = c.  
  
23 ?- nth1(2, \[a,b,c,d\], Elem).  
Elem = b.  
  
把之前的代码修改之后，终于可以在SWI Prolog中执行了。全部的代码如下：  
calc(Operator, Left, Right, Value) :-  
  Operator = opadd  -> Value is Left + Right;  
  Operator = opsub  -> Value is Left - Right;  
  Operator = opmul  -> Value is Left * Right;  
  Operator = opdiv  -> Value is Left / Right;  
  Operator = opjoin -> Value is Left * 10 ** ceiling(log10(Right)) + Right.  
  
getPriority(Operator, Priority) :-  
  Operator = opadd  -> Priority = 1;  
  Operator = opsub  -> Priority = 1;  
  Operator = opmul  -> Priority = 2;  
  Operator = opdiv  -> Priority = 2;  
  Operator = opjoin -> Priority = 3;  
  Priority = -1.  
  
  
checkOp(Node) :-  
  Node = opadd;  
  Node = opsub;  
  Node = opmul;  
  Node = opdiv;  
  Node = opjoin.  
  
  
evalTree(Tree, Value) :-  
  \[Operator |  Operands\] = Tree,  
  \[Left     |   \[Right\]\] = Operands,  
  \[HL       |        TL\] = Left,  
  \[HR       |        TR\] = Right,  
  (TL = \[\] -> ValueLeft  = HL; evalTree(Left,  ValueLeft)),  
  (TR = \[\] -> ValueRight = HR; evalTree(Right, ValueRight)),  
  calc(Operator, ValueLeft, ValueRight, Value).  
  
  
findRootOp(\[\], -1, -1, _).  
findRootOp(\[Head | Tail\], Priority, Index, Counter) :-  
  \\+checkOp(Head) -> findRootOp(Tail, Priority, Index, Counter+1);  
  findRootOp(Tail, NewPriority, NewIndex, Counter+1),  
  getPriority(Head, CurrentPriority),  
  ((NewPriority > 0, CurrentPriority >= NewPriority) ->  
    (Index = NewIndex, Priority = NewPriority)  
  ;  
    (Index is Counter, Priority = CurrentPriority)  
  ).  
  
  
leftList(_, 1, \[\]).  
leftList(\[Head | Tail\], Index, LeftList) :-  
  NewIndex is Index - 1,  
  leftList(Tail, NewIndex, TempList),  
  LeftList = \[Head | TempList\].  
  
rightList(List, 0, List).  
rightList(\[_ | Tail\], Index, RightList) :-  
  NewIndex is Index -1,  
  rightList(Tail, NewIndex, RightList).  
  
createTree(List, Tree) :-  
  findRootOp(List, _, OpIndex, 1),  
  (OpIndex >= 0 ->  
    leftList(List, OpIndex, LeftList),  
    createTree(LeftList, LeftTree),  
  
    rightList(List, OpIndex, RightList),  
    createTree(RightList, RightTree),  
  
    nth1(OpIndex, List, Op),  
    Tree = \[Op, LeftTree, RightTree\]  
  ;  
    Tree = List  
  ).  
  
evalExpr(Expr, Value) :-  
  createTree(Expr, Tree),  
  evalTree(Tree, Value).  
  
  
createExprList(\[\], \[2.0\]).  
createExprList(\[Head | Tail\], ExprList) :-  
  checkOp(Head),  
  createExprList(Tail, TempList),  
  ExprList = \[2.0, Head | TempList\].  
  
solve(ExprList) :-  
  length(OpList, 15),  
  createExprList(OpList, ExprList),  
  evalExpr(ExprList, 1991.0).  
  
  
这段代码最后的createExprList和solve是用来求解[《用Prolog求解操作数间合适的运算符》](http://blog.sina.com.cn/s/blog_4513dde60102vs5c.html)中的问题的。让我们试一下：  
2 ?- time(solve(Expr)).  
% 6,648,187,874 inferences, 603.797 CPU in 609.394 seconds (99% CPU, 11010636 Lips)  
Expr = \[2.0, opadd, 2.0, opadd, 2.0, opadd, 2.0, opadd, 2.0|...\] \[write\]  
Expr = \[2.0, opadd, 2.0, opadd, 2.0, opadd, 2.0, opadd, 2.0, opadd, 2.0, opmul, 2.0, opmul, 2.0, opjoin, 2.0, opmul, 2.0, opjoin, 2.0, opadd, 2.0, opmul, 2.0, opjoin, 2.0, opadd, 2.0, opdiv, 2.0\] .  
  
SWI不像GNU Prolog那样会自动记录运行的时间，需要手动使用time。将结果翻译成易于阅读的形式，如下：  
2+2+2+2+2+2\*2\*22\*22+2\*22+2/2  

-   前面五个2相加等于10；
-   中间2\*2\*22*22等于1936；
-   最后2*22+2/2等于45；
-   10+1936+45 = 1991

耗时十分钟，较GNU Prolog短。得到的结果与GNU Prolog一致，也许两者使用的搜索树是一样的。














































