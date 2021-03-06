# DMS ®软件再造工具包


semanticdesigns.com/Products/DMS/DMSToolkit.html










DMS ®软件再造工具包™
...是一套复杂的基础架构和高度可定制的工具，用于自动化：

源程序分析
修改源代码
生成软件
DMS / SRT（或仅是“ DMS”）可以在任意域混合（计算机语言，例如C ++，Java，COBOL，SQL，HTML，Verilog等）上大规模运行。
DMS的目的是提供足够的基础结构，以便自定义工具的构建者可以花时间在自定义工具的细节上， 而不是尝试从头开始构建必要的基础结构机器。通过利用SD已投入的人力资源，这可以节省工具制造商数年的工程设计时间。先进的基础设施使工具制造商能够产生比自定义独立工具更有效的结果。

DMS的术语“软件”非常广泛，涵盖任何正式的表示法，包括编程语言，标记语言，硬件描述语言，设计表示法，数据描述和 特定于域的语言。该工具包是朝实施的第一步设计维护系统®，一个21世纪的软件工程环境的雄心勃勃的目标，支持大型应用系统，通过语义和捕获设计驱动的增量建设和维护。

DMS：通用编译器基础结构
DMS的一个非常简单的模型（请参见下图）是一个非常通用的编译器，它具有

解析器（产生类似编译器的数据结构来捕获代码），
一组语义分析器，
包括各种模式匹配（使用表面语法）引擎
一组编译器数据结构修改引擎，
包括 源到源程序转换引擎（使用表面语法）
和最终的输出格式化组件（将编译器数据结构转换回有效的源代码，而不是二进制代码），
通过要处理的计算机语言描述进行参数化。
与传统的编译器不同，在传统的编译器中，每个组件都特定于其将一种源语言转换为一种目标机器语言的任务，而每个DMS组件都通过所需任务进行了高度参数化，从而实现了多种惊人的效果。这意味着可以以任意方式更改输入语言，更改分析，更改转换和更改输出。
可以“仅”使用DMS来构建生成报告的分析器。或者，它可以用于查找和修复编码和结构问题。使用分析器输出（分析焦点弧）来定位问题，然后选择/应用转换来解决问题。

与传统的编译器不同，DMS可以同时处理来自多种语言的数千个文件，从而可以在复杂的文件系统中进行分析和/或进行一致的代码更改。

一个有趣的特性是DMS可以读取语言的正式描述，进行分析和转换。因此，DMS被用来支持自己，包括产生新的语言描述。DMS功能
DMS为构建软件分析和修改工具提供了一系列强大的集成工具，这些工具 已在数十种真实语言中得到证明：

- 完全基于UNICODE的解析器和词法分析器生成，具有自动错误恢复功能。接受/生成以UTF-8和UTF-16、7位ASCII（ISO-646-US），8位ASCII（ISO-8859-1至-16），EBCDIC（CP-37，CP-500）编码的文件，多个Microsoft代码页（CP-1250至-1258）和日语Shift-JIS（CP-932和JIS-0208）。包括用于读取多个源文件的标准支持，以启用INCLUDE文件管理并构建合适的预处理器。解析器技术基于GLR，甚至可以处理歧义（比YACC / LALR强得多），并且可以处理任何上下文无关的语言。（在此处查看详细信息。）
- 自动构造抽象（非具体）语法树（抑制了不携带值的终端和单位产品；语法列表转换为AST列表节点）。文字值（数字，转义字符串）将转换为本地的标准化二进制值，以进行快速内部处理。捕获源注释并将其附加到AST节点。（在此处查看详细信息。）
- 漂亮打印机会根据指定的布局信息（包括源注释）将AST转换回格式正确的合法源文件格式。在保真打印模式下，保留未更改代码的注释，间距和词法格式化信息。（请参阅此处的详细信息。）自定义允许生成源代码HTML表单，甚至生成为模糊的源文本。树可以直接以XML格式输出。
- 从语法生成多遍属性评估器，以允许根据提供的具体语法指定任意分析（包括名称/类型分析过程）。属性可以是本地或远距离的。（在此处查看详细信息。）
- 完善的符号表支持工具，用于全局，本地，继承，重载以及其他与语言相关的名称查找和名称空间管理规则。这甚至可以处理C ++ 14的复杂性。（在此处查看详细信息。）
- 控制流图构造包括传统的进入/退出/动作/条件节点，但也包括派生/加入节点，以对并行性和/或不确定顺序（例如C序列点）进行建模。有预定义的分析器用于构造（后）支配者，并诱导结构化的控制流区域。其他机器可以计算编译单元本地和系统/全局调用图。
- 数据流分析框架，允许提出和解决数据流分析问题，包括用于构建use-def和def-use链的预定义分析器。（请参阅示例控件和数据流程图）
用于计算本地或全局指向数据的指向分析，已在13+百万行代码的系统上进行了测试。
- 符号范围分析根据其他变量计算程序变量的范围约束。这对于检测阵列访问错误，确定选择哪个开关盒以及其他分析非常有用。
- 二进制（和有限）决策图用于有效地构建和组合符号布尔公式（或排他性选择集上的公式）。将表示布尔公式的AST转换为BDD是很简单的，反之亦然。
可以同时表示多个域（符号/语言）。这样就可以处理或生成由来自一个以上域（COBOL和JCL，C和Makefile等）的部分组成的系统，和/或从一种域语言转换为另一种域语言。
- 转换和模式可以直接以表面到表面域的语法形式编写。模式可以与语法树匹配，并返回参数子树的绑定。或者，过程代码可以实现转换，或者引用现有的转换和模式以实现非常复杂的转换。（在此处查看详细信息。）
在树和DAG上运行的完整的关联/交换重写引擎，可用于应用转换集。
元编程语言XCL提供了控制变换和变换集应用顺序的功能。（未来发布）
- 一个代数规范子系统可以用来指定任意代数（这只是一个DMS域！）。公理可被视为一组重写规则。（这使人们可以编写任意简化程序。（我们已经对布尔方程进行了简化，布尔方程的大小基本为100万个项；我们也以这种方式对晶体管[不是门！]电路的优化进行了建模）。
在2004年国际软件工程大会上发布了详细介绍这些功能的技术论文。您可以获得纸质版 和相应的幻灯片。为了获得DMS的具体感觉，我们提供一个示例，说明如何为Oberon语言指定DMS的各个方面。