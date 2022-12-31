

https://github.com/topics/control-flow-graph?o=asc&s=stars

github 主题各种项目，其中比较重要的几个github开源项目

























# 1. code2ControlFlowGraph
https://stackoverflow.com/questions/50913708/how-to-draw-a-control-flow-graph-from-this-code
火花带闪电，使用带讲解























 https://stackoverflow.com/questions/1542010/tools-for-generating-a-control-flow-graph-from-source-code


请参阅我公司的（语义设计）Java Front End。它将从源代码计算方法的控制流程图。

Java前端建立在DMS软件再造工具包的基础上，该工具包提供了用于操纵（解析，分析[例如，提取控制流程图]，转换和生成）代码的通用机制。

如果有一个特定的控制流程图，则DMS提供了一种机制，使您能够构建图形漫游器，从而可以合理地构建Java AST，然后将其用于生成Java源代码。显然，您的控制流程图将必须使用能够轻松转换为Java概念的词汇表（例如，没有Prolog可以“统一”此运算符），否则您将很难生成相应的Java代码。如果您是从Java代码生成图形的，那么情况显然是这样。




https://www.imagix.com/products/source-code-analysis.html








```
免费软件调用图生成器
运行时调用图（列出的大多数工具是具有调用图功能的探查器）：
gprof  ：包含在BSD或GNU Binary Utilities的一部分中
callgrind：Valgrind的一部分
KCachegrind  ：基于callgrind生成的数据生成和分析调用图的强大工具
Mac OS X活动监视器：Apple GUI进程监视器活动监视器具有内置的调用图生成器，可以对进程进行采样并返回调用图。此功能仅在Mac OS X Leopard中可用
OpenPAT：包括从运行时测量中control_flow自动创建Graphviz调用图图片的工具。
pprof，用于可视化和分析配置文件数据的开源工具，可与gperftools结合使用。
CodeAnalyst从AMD（GPL下发布）
makeppgraph是一个依赖关系图生成器（在模块级别），用于使用makepp执行的构建。
英特尔®单事件API（免费，开源）
用于在不运行应用程序的情况下获取调用图的静态方法：
C / C ++
**Sourcetrail**创建一个静态调用图，用户可以动态浏览它。还支持Python和Java
doxygen  ：使用Graphviz生成静态调用/继承图
cflow  ：GNU cflow能够生成C程序的直接调用图和反向调用图
egypt  ：一个小的Perl脚本，它使用gcc和Graphviz生成C程序的静态调用图。
Analizo：计算源代码指标，生成依赖图。
CCTree  ：本机Vim插件，可以通过读取cscope数据库来显示静态调用图。适用于C程序。
codeviz  ：静态调用图生成器（程序未运行）。作为gcc的补丁实施; 适用于C和C ++程序。
calltree.sh：Bash  shell函数将cscope，graphviz和一些点渲染工具粘合在一起，以在您指定的C函数的上方，下方和/或之间显示“调用者”和“被调用者”关系。
tceetree  ：像calltree.sh一样，它连接Cscope和Graphviz，但是它是可执行文件而不是bash脚本。
去
go-callvis  ：用于Go程序的交互式调用图生成器，其输出可以使用Graphviz绘制
。网
NDepend：是用于.NET代码的静态分析工具。该工具支持大量代码指标，允许使用有向图和依赖矩阵可视化依赖关系。
PHP，Perl和Python
Devel :: NYTProf  ：Perl性能分析器和调用图生成器
phpCallGraph  ：使用Graphviz的PHP程序的调用图生成器。它是用PHP编写的，至少需要PHP 5.2。
pycallgraph  ：使用Graphviz的Python程序的调用图生成器。
pyan  ：使用Graphviz的Python程序的静态调用图生成器。
gprof2dot  ：用Python编写的调用图生成器，可将多种语言/运行时的性能分析数据转换为Graphviz调用图。
**code2flow**：使用Graphviz的Python和Javascript程序的调用图生成器
rcviz  ：Python模块，用于使用Graphviz渲染运行时生成的调用图。每个节点代表一个函数的调用，该函数具有传递给它的参数和返回值。
XQuery
XQuery Wikibook中的XQuery调用图：使用Graphviz的XQuery功能模块的调用图生成器
专有调用图生成器
项目分析员
静态代码分析器和Visual Basic代码的调用图生成器
视觉专家
适用于Oracle PL / SQL，SQLServer Transact-SQL，C＃和PowerBuilder代码的静态代码分析器和调用图生成器
英特尔VTune性能分析器
检测分析器以显示调用图和执行统计信息
DMS软件再造工具包
可定制的程序分析工具，具有针对C，Java和COBOL的静态整个程序全局调用图提取
其他相关工具
Graphviz
将任何图（包括调用图）的文本表示形式转换为图片。
```



## 1.1. LLVm
有一个用于Clang / LLVM的opt模块[ 1 ] ，它将使用DOT表示法转储调用图。根据您的Clang发行版本，可能尚未opt安装。在这种情况下，您将必须自己构建Clang。告诉Clang吐出LLVM源（“ --emit-llvm -S”）并用处理结果opt。

您需要传递的标志opt是--dot-callgraph，您将需要GraphViz 呈现输出的工具。






# 2. ControlFlowGraph2Code




**CoFlo** is a Free and Open Source source code analysis tool which generates and analyzes control flow graphs from C and C++ source.









