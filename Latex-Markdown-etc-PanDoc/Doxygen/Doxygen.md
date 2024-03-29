
[TOC]

 线上版本中文手册索引


Doxygen是可用于C++、 C、 Java、 Objective-C、 Python、 IDL (Corba 和 Microsoft flavors)以及部分PHP、 C#和 D语言的文档系统。

它能通过以下三种方式帮助你：  
　　1，它能从一系列源文件中生成在线浏览文档（HTML形式）或离线参考手册（LATEX形式）。还支持RTF（MS-Word），PostScript，带超链接的PDF，压缩的HTML和Unix man页。文档是直接从源文件中提取出来的，这使得文档与源代码很容易保持同步。  
　　2，通过配置doxygen，你可以从未文档化的源文件中提取出代码结构。这对于从大的源码包中快速理清头绪是非常有用的。它还能自动产生出包含关系图、继承图和协作图，使你能直观地看出各种元素间的关系。  
　　3，你甚至可以“滥用“doxygen来创建平常的文档（就像本文档）。

doxygen是在Linux和Mac OS X下开发的，但是它被设计成高可移植的。这使得它可运行在其它Unix变种操作系统上。此外，它还能在windows下运行。

本手册分为三部分，其中每个部分又分为几节。

**第一部分是用户手册：**

-   Installation一节讨论了如何在你的平台上下载、编译和安装doxygen。
-   Getting started一节告诉你如何快速地产生你的第一块文档。
-   Documenting the code 一节示范了代码被文档化的多种方法。
-   Lists 一节展示了如何创建项目列表。
-   Grouping一节展示了如何将各种东西集合在一起以组成一个项目列表。
-   Including formulas一节展示了如何在文档中插入规则。
-   Graphs and diagrams描述了doxygen可生成的图表和图形。
-   Preprocessing一节说明了doxygen是如何处理宏定义的。
-   Automatic link generation一节展示了如何在文档中链接文件、类和成员。
-   Output Formats一节展示了如何生成doxygen支持的各种输出格式。
-   Linking to external documentation一节说明了如何使doxygen创建到外部文档的链接。
-   Frequently Asked Questions一节给出常见问题的解答。
-   Troubleshooting一节告诉你遇到难题时该怎么做。

**第二部分是参考手册：**

-   Features一节概述了doxygen能做什么。
-   Doxygen History一节显示了doxygen开发过程中的变化和不变之处。
-   Doxygen usage一节告诉你如何使用doxygen程序。
-   Doxytag usage一节告诉你如何使用doxytag程序。
-   Doxywizard usage一节告诉你如何使用`doxywizard`程序。
-   Installdox usage一节显示了如果你在使用tag文件时如何运用doxygen产生的installdox脚本。
-   Configuration一节显示了如何调整doxygen以生成你要的文档。
-   Special Commands一节显示了可在文档中使用的特殊命令的概述。
-   HTML Commands一节显示了可在文档中使用的HTML命令的概述。
-   XML Commands一节显示了可在文档中使用的XML命令的概述。

**第三部分是为开发者提供的信息：**

-   Doxygen's Internals一节给出了doxygen内部构造的一个整体概述。
-   Perl Module output format documentation 显示了如何使用PerlMod的输出。
-   Internationalization 一节说明了如何增加对新的输出语言的支持。











# 1. 文档
https://www.doxygen.nl/manual/config.html

https://www.doxygen.nl/manual/doxywizard_usage.html


手把手 http://blog.sina.com.cn/s/blog_a459dcf50102v7ft.html

https://www.cnblogs.com/z-z-z/articles/6604379.html


中文注释在文档中是乱码。
解决：在expert中的INPUT选项页的INPUT_ENCODEING中填入“GB2312”，这样基于GB的文本编辑器生成的代码就可以正常使用了。



输出chm的问题：如何输出.chm文件
在expert中的HTML页：选中“GENERATE_HTMLHELP”，然后在CHM_FILE中填上想要的chm文件名。
HHC_LOCATION中输入hhc.exe文件的路径。hhc.exe可以通过安装HTML Help Workshop获得。
HTML Help Workshop 地址：
http://www.microsoft.com/downloads/details.aspx?FamilyID=00535334-c8a6-452f-9aa0-d597d16580cc&displaylang=en 这样，基本上就能够用doxygen生成漂亮的文档了。代码方面，doxygen支持多种格式的注释风格，根据manual选择自己喜欢的就好。





Doxygen快速入门 - 路明的文章 - 知乎
https://zhuanlan.zhihu.com/p/100223113


https://www.doxygen.nl/manual/doxygen_usage.html 文档

D:\Program Files\doxygen


https://github.com/doxygen/doxygen



运行doxygen wizard.exe 

通过图形界面运行doxygen，在doxygen的bin目录中运行doxywizard.exe，这时按照doxygen根目录下的文档（doxygen_manual-1.5.2.chm）中 Doxywizard usage一节的说明设置即可。主要包括，源码路径、工作路径、输出路径等。


Doxygen 中文文档 - grassofsky的文章 - 知乎
https://zhuanlan.zhihu.com/p/122523174


除了doxygen

Java集成有javadoc

C#也集成有XML Documentation Comment

Python里面有pydoc

Ruby里面有rdoc





Doxygen主要解决说明书问题，可以在我们写代码的时候讲注释转化为说明书，Graphviz主要是用于图形展示，html help workshop主要使用生成CHM文档。

1.Doxygen

Doxygen能将程序中的特定批注转换成为说明文件。它可以依据程序本身的结构，将程序中按规范注释的批注经过处理生成一个纯粹的参考手册，通过提取代码结构或借助自动生成的包含依赖图（include dependency graphs）、继承图（inheritance diagram）以及协作图（collaboration diagram）来可视化文档之间的关系， Doxygen生成的帮助文档的格式可以是CHM、RTF、PostScript、PDF、HTML等。

2.graphviz

Graphviz(Graph Visualization Software)是一个由AT&T实验室启动的开源工具包,用于绘制DOT语言脚本描述的图形。要使用Doxygen生成依赖图、继承图以及协作图，必须先安装graphviz软件。



3.HTML Help WorkShop

微软出品的HTML Help WorkShop是制作CHM文件的最佳工具，它能将HTML文件编译生成CHM文档。Doxygen软件默认生成HTML文件或Latex文件，我们要通过HTML生成CHM文档，需要先安装HTML Help WorkShop软件，并在Doxygen中进行关联

【工具篇】把代码注释生成技术文档 - ZhengN的文章 - 知乎
https://zhuanlan.zhihu.com/p/104334500

默认支持的语言有：C, C++, C#, Objective-C, IDL, Java, VHDL, PHP, Python, Fortran and D.



# 2. Doxygen
## Run

### 运行Doxywizard建立配置文件。
能够直接点“Save...”按钮，将保存默认的配置文件，名为Doxyfile，内容是Doxygen的默认设置。Doxyfile是普通文本文件，咱们能够直接打开手动编辑。不过在Doxywizard的界面上填写也很方便，每一个参数都有详细提示。建议用Doxywizard完成第一次设置。之后若是须要调整个别参数，能够直接编辑Doxyfile。程序员

上述Doxywizard界面中提供了生成Doxygen文档的4个步骤，按照上述步骤一步步执行就能够生成漂亮的文档了。windows

第一步是生成配置文件，提供三种方式，Wizard方式指简约方式，在其中只提供一些重要的参数设置，其他的均为默认值；Expert方式为详细设置方式，经过该选项能够详细地配置Doxygen的各个配置项；最后一种是Load方式，用于导入之前生成的Doxygen配置文件，导入后能够再点击Expert进行修改。微信


### 命令行执行
https://www.cnblogs.com/rongpmcu/p/7662765.html命令行sdoxygen和规范
命令行

使用doxygen

1. 生成配置文件(推荐doxyward选择生成)

doxygen -g config_file_name

打开这个配置文件，修改参数。
一定要修改的三个参数：INPUT ， RECURSIVE ， output

2. 可以根据上述图形界面来修改参数，或者：在图形界面自己选好配置，然后导出配置文件。

3. 开始执行
4. 命令
```
doxygen config_file_name
```



## 2.1. 4.2  配置选项含义详解

[doxygen本地文件](file:///D:/Program%20Files/doxygen/html/starting.html)


在上述界面中点击Expert按钮，或者用文本方式打开Doxyfile文件，能够看到Doxygen的参数配置项特别多，各个参数的含义其实也并不难掌握，在Doxygen的帮助手册中有详细的介绍，下面我介绍一些经常使用的参数含义，其他的参数大多能够设置为默认值。数据结构

| DOXYFILE_ENCODING函数 | Doxygen文件的编码方式，默认为UTF-8，若但愿支持中文，最好设置为 GB2312 |
| --------------------- | ------------------------------------------------------------ |
| PROJECT_NAME          | Project 的名字，以一个单词为主，多个单词请使用双引号括住。   |
| PROJECT_VERSION       | Project的版本号码。                                          |
| OUTPUT_DIRECTORY      | 输出路径。产生的文件会放在这个路径之下。若是没有填这个路径，将会以目前所在路径做为输出路径。 |
| OUTPUT_LANGUAGE       | 输出语言, 默认为English 。                                   |
| EXTRACT_ALL           | 为NO，只解释有doxygen格式注释的代码；为YES，解析全部代码，即便没有注释 |
| EXTRACT_PRIVATE       | 是否解析类的私有成员                                         |
| EXTRACT_STATIC        | 是否解析静态项                                               |
| EXTRACT_LOCAL_CLASSES | 是否解析源文件（cpp文件）中定义的类                          |
| INPUT                 | 指定加载或找寻要处理的程序代码文件路径。这边是一个表列式的型态。而且可指定档案及路径。 |
| FILE_PATTERNS         | 若是您的INPUT Tag 中指定了目录。您能够透过这个Tag来要求Doxygen在处理时，只针对特定的档案进行动做。例如：您但愿对目录下的扩展名为.c, .cpp及.h的档案做处理。您可设定FILE_PATTERNS = *.c, *.cpp, *.h。 |
| RECURSIVE             | 这是一个布尔值的Tag，只接受YES或NO。当设定为YES时，INPUT所指定目录的全部子目录都会被处理. |
| EXCLUDE               | 若是您有某几个特定档案或是目录，不但愿通过Doxygen处理。您可在这个Tag中指定。 |
| EXCLUDE_PATTERNS      | 相似于FILE_PATTERNS的用法，只是这个Tag是供EXCLUDE所使用。    |
| SOURCE_BROWSER        | 若是设定为YES，则Doxygen会产生出源文件的列表，以供查阅。     |
| INLINE_SOURCES        | 若是设定为YES ，则函数和类的实现代码被包含在文档中           |
| ALPHABETICAL_INDEX    | 若是设定为YES，则一个依照字母排序的列表会加入在产生的文件中。（有不少类、结构等项时建议设为YES） |
| GENERATE_HTML         | 若设定为YES ，就会产生HTML版本的说明文件。HTML文件是Doxygen预设产生的格式之一。 |
| HTML_OUTPUT           | HTML文件的输出目录。这是一个相对路径，因此实际的路径为OUTPUT_DIRECTORY加上HTML_OUTPUT。这个设定预设为html。 |
| GENERATE_HTMLHELP     | 是否生成压缩HTML格式文档（.chm）                             |
| HTML_FILE_EXTENSION   | HTML文件的扩展名。预设为.html。                              |
| HTML_HEADER           | 要使用在每一页HTML文件中的Header。若是没有指定，Doxygen会使用本身预设的Header。 |
| HTML_FOOTER           | 要使用在每一页HTML文件中的Footer。若是没有指定，Doxygen会使用本身预设的Footer。 |
| HTML_STYLESHEET       | 您可给定一个CSS 的设定，让HTML的输出结果更完美。             |
| GENERATE_HTMLHELP     | 如设定为YES，Doxygen会产生一个索引文件。这个索引文件在您须要制做windows 上的HTML格式的HELP档案时会用的上。 |
| GENERATE_TREEVIEW     | 若设定为YES，Doxygen会帮您产生一个树状结构，在画面左侧。这个树状结构是以[JavaScript](http://lib.csdn.net/base/javascript)所写成。因此须要新版的Browser才能正确显示。 |
| TREEVIEW_WIDTH        | 用来设定树状结构在画面上的宽度。                             |
| GENERATE_LATEX        | 设定为YES 时，会产生LaTeX 的文件。不过您的系统必须要有安装LaTeX 的相关工具。 |
| LATEX_OUTPUT          | LaTeX文件的输出目录，与HTML_OUTPUT用法相同，同样是指在OUTPUT_DIRECTORY之下的路径。预设为latex。 |
| LATEX_CMD_NAME        | LaTeX程序的命令名称及档案所在。预设为latex。                 |
| GENERATE_RTF          | 若设定为YES ，则会产生RTF 格式的说明档。                     |
| RTF_OUTPUT            | 与HTML_OUTPUT 用法相同，用来指定RTF 输出档案路径。预设为rtf。 |
| GENERATE_MAN          | 若设定为YES ，则会产生Unix Man Page 格式的说明文件。         |
| MAN_OUTPUT            | 与HTML_OUTPUT 用法相同，用来指定Man Page的输出目录。预设为man。 |
| GENERATE_XML          | 若设定为YES ，则会产生XML 格式的说明文件。                   |
| ENABLE_PREPROCESSING  | 若设定为YES ，则Doxygen 会激活C 的前置处理器来处理原始档。   |
| PREDEFINED            | 可让您自行定义一些宏。相似于gcc 中的-D选项。                 |
| CLASS_DIAGRAMS        | 这个标记用来生成类继承层次结构图。要想生成更好的视图，能够从 Graphviz 下载站点 下载 dot 工具。Doxyfile 中的如下标记用来生成图表： |
| HAVE_DOT              | 若是这个标记设置为 Yes，doxygen 就使用 dot 工具生成更强大的图形，好比帮助理解类成员及其[数据结构](http://lib.csdn.net/base/datastructure)的协做图。注意，若是这个标记设置为 Yes，<CLASS_DIAGRAMS> 标记就无效了 |
| CLASS_GRAPH           | 若是 <HAVE_DOT> 标记和这个标记同时设置为 Yes，就使用 dot 生成继承层次结构图 |
| GRAPHICAL_HIERARCHY   | 设置为YES时，将会绘制一个图形表示的类图结构                  |

 
**更多看doxygen中文文档.pdf**
 如果EXTRACT_ALL标记设置为YES，即使没有可用的文档，doxygen也会假设文档中的所有实体均已文档化。除非EXTRACT_PRIVATE和EXTRACT_STATIC标记设置为YES，否则私有类成员和静态文件成员将被隐藏。 https://stackoverflow.com/questions/4884197/using-doxygen-for-existing-java-code







上面的表格只是描述了一些经常使用的配置，须要更加详细的信息请参考Doxygen的帮助手册。




Doxygen是一种开源跨平台的，以类似JavaDoc风格描述的文档系统，完全支持C、C++、Java、Objective-C和IDL语言，部分支持PHP、C#。注释的语法与Qt-Doc、KDoc和JavaDoc兼容。Doxygen可以从一套归档源文件开始，生成HTML格式的在线类浏览器，或离线的LATEX、RTF参考手册。

官网：http://www.doxygen.nl/



```
sudo apt-get install graphviz doxygen doxygen-gui
```

Doxygen和Graphviz结合使用， 完美的让代码以网页、图形、调用关系图图展现出来。方便阅览代码。

此方法优势： 不需要编译代码。根据需求，配置好参数，可利用命令直接输出结果。




将源码生成调用关系图还有很多方式，比如：

1. drafter 在iOS项目中自动生成函数调用关系图

https://blog.csdn.net/allanGold/article/details/89186582

2. 用Graphviz + CodeViz生成C/C++函数调用图

https://www.cnblogs.com/lanxuezaipiao/p/3450201.html

3. source insight

利用[Relation]功能，可展示几种关系图：树形，左右，上下





## 2.2. cpp注释样式

```
三种格式 　　（推荐前两种）

1.把你的注释包含在/** – */ 块里。

2.把你的注释包含在 /*! – */块里。（推荐）

3.以三条斜杠 ///开始的注释行
```

```
XX.h文件注释：

/**

 * @brief 自定义提示框

 * @author author

 * @date 2021/03/23
属性注释：

/**

 左侧按钮

 */

@property (nonatomic, strong) UIButton *leftBtn;

 

方法注释：

/**

 初始化方法

 @param title     标题

 @param message   内容 需要换行以*隔开

 @param imageName 背景图

 

 @return RGAlertView

 */

- (instancetype)initWithTitle:(NSString *)title message:(NSString *)message backgroundImage:(NSString *)imageName;

 

 

注释标签：

@brief: 使用它来写一段你正在文档化的method, property, class, file, struct, 或enum的短描述信息

@discussion: 用它来写一段详尽的描述。如果需要你可以添加换行。

@param: 通过它你可以描述一个 method 或 function的参数信息。你可以使用多个这种标签

@return: 用它来制定一个 method 或 function的返回值

@see: 用它来指明其他相关的 method 或 function。你可以使用多个这种标签

@sa: 同前一条类似

@code: 使用这个标签，你可以在文档当中嵌入代码段。当在Help Inspector当中查看文档时，代码通过在一个特别的盒子中用一种不同的字体来展示。始终记住在写的代码结尾处使用@endcode标签

@remark:在写文档时，用它来强调任何关于代码的特殊之处
 */

```




# 原理


https://blog.csdn.net/wzsda110/article/details/80977528
doxygen原理




doxygen中文手册v1.63.pdf
![doxygen功能](vx_images/711113159268.png)

不管什么语言都要转换成对应的**C/C++**的元素才能被doxygen理解。
![](_v_images/1626650878_25429.png)


## Config parser（配置解析器）

工程的参数配置文件被Doxygen解析，并将参数存储到一个单独的类Config（src/config.h）文件中。解析器是采用的FLEX框架编写的，源码在src/config.l目录下。因为解析器也被doxywizard（前端向导）直接调用，所以把解析器做成一个单独的库。

每一个配置选项都是五种类型中的一种：String，List，Enum，Int，Bool。这些配置选项的值都可以使用全局函数Config_getXXX()获取到（XXX指选项）。这些函数的参数，是以配置文件中选项的名称命名的字符串。例如：Config_getBool("GENERATE_TESTLIST")，如果test列表启用，返回布尔类型TRUE。

src/doxygen.cpp中的函数readConfiguration()读取了命令行参数，之后调用配置解析器。

 

## C Preprocessor

配置文件里配置的输入文件（默认情况下）被送到C语言预处理器（通过用户定义的筛选器传输）。

预处理器的工作方式不同于标准的C预处理器。默认情况下，它不展开宏，虽然它可以被配置为展开所有宏。典型的用法是只扩展用户指定的宏集合。这是为了允许宏名称出现在函数参数的类型中。

另一个区别是，预处理器分析，但实际上不包含#include的代码（除了{...}里的#include代码）。这么做的原因是为了避免让doxygen的解析器去处理函数/类的重定义的情况。例如当所有源文件都包含一个公共头文件，类和类型定义（以及注释）将存于在每个翻译单元中。

解析器是基于FLEX框架，源码在src/pre.l。条件控制块（#if）需要使用常量表达式。因而使用了基于yacc的解析器，源码在src/constexp.y和src/constexp.l。

C 预处理器会为每个文件调用preprocessFile()函数，并且把处理结果追加到字符缓冲区，缓冲区的格式是

```
0x06 file name 1
0x06 preprocessed contents of file 1
...
0x06 file name n

0x06 preprocessed contents of file n
```

## Language parser（语言解析器）

预处理器的缓冲区被送到语言解析器，后者使用flex（一个词法分析器）实现了一个大型状态机。源码在src/scanner。一种解析器解析所有语言（C/C++/Java/IDL）。状态变量insideIDL和insideJava在某些地方用用于选择特定语言。

解析器的工作是把输入缓冲区转换成条目树（抽象的语法树），在src/entry定义了条目的内容，是一种松散的结构信息。最重要的字段section描述了条目里包含的信息。

为了在以下几个方面可能会改善：
    每种语言各使用一种解析器，而不是一个大型扫描器。
    将文档的第一道解析移动到一个独立的模块。
    解析预定义define（目前预处理器只是把他们集合起来，语言解析器会把他们忽略掉）。



## Data organizer（数据组织器）

这一步包含了很多小步骤，为提取的类、文件、命名空间、变量、函数、包、页面、组创建文件目录，除此之外，在这一步过程中条目之间关系会被计算出来。

在src/doxygen.cpp里有每个一个步骤的函数，这些函数操作条目数，在语言解析期间构建目录。详情需查看“Gathering information”一节。

这一步的结果是许多目录，目录结构在src/doxygen.h的doxygen的“命名空间”中。目录的大部分属性是从类Definition继承而来的。MemberDef类保存了一个成员的全部信息，FileDef类保存了文件的，ClassDef类保存了类，NamespaceDef保存了命名空间，GroupDef保存了组，PackageDef类保存了Java包信息。

## Tag file parser（标签文件解析器）
如果在配置文件中指明标签文件，那么将使用基于SAX的XML解析器来解析它们，源码在src/tagreader.cpp中。解析标签文件后，会像条目树中插入Entry对象。字段Entry::tagInfo用来标记条目是外部的，并保存了标签文件里的信息。

## Documentation parser（注释解析器）
特定的注释块会以字符串形式存储在条目中。简述信息和详细信息都有各自的字符串。文档解析器读取字符串并且执行字符串里的命令（这是注释解析的第二部分）。它会把结果写给输出生成器。

解析器是C++编写，源码在src/docparser.cpp中。解析器处理的符号在src/doctokenizer.l中定义。注释块里的代码段会被传递给源代码解析器。

文档解析器的入口函数是src/docparser.h里的validatingParseDoc()。带有特殊命令的简单文本会使用validatingParseText()函数。

## Source parser（源码解析器）

如果浏览源代码被启用，或者注释汇中出现代码段，源码解析器会被调用。

代码解析试图对文档化的条目生成交叉引用，同样会为源代码做语法高亮，输出直接写给了输出生成器。

代码解析入口程序parseCode()在src/code.h声明。

## Output generators（输出生成器）

在数据被收集和交叉引用之后，Doxygen产生各种格式的输出。为此，输出生成器使用抽象类OutputGenerator提供的方法。为了能生成多种格式的输出，OutputList会被代替。该类维护一个具体的输出生成器列表，其中调用的每个方法都被委派给列表中的所有生成器。

为了让每个特定的输出生成器允许在输出中写入小偏差，可以暂时禁用某些生成器。输出列表类包含了大量disable()和enable()方法。OutputList::pushGeneratorState() 和OutputList::popGeneratorState()用于临时保存堆栈上的启用/禁用输出生成器集。

XML是直接从数据结构中生成的。未来，XML将会被用做中间语言（IL），然后，输出生成器将使用这个IL作为起点来生成特定的输出格式。拥有IL的优点是，各种独立开发的工具以各种语言编写，可以从XML输出中提取信息。

独立工具可能是：
    交互式源码浏览器
    类图生成工具
    计算代码度量

## Debugging 调试

由于doxygen使用了大量的flex代码，所以我们需要了解flex的运行规则以及flex如何处理输入。幸运的是，当Flex与-d选项一起使用时，它输出匹配的规则。这使得很容易跟踪特定输入片段的内容。为了更容易切换给定的Flex文件的调试信息，我编写了以下Perl脚本，它会自动在makefile文件中添加或移除-d。


```
#!/usr/bin/perl
$file = shift @ARGV;
print "Toggle debugging mode for $file\n";
if (!-e "../src/${file}.l")
{
print STDERR "Error: file ../src/${file}.l does not exist!\n";
exit 1;
}
system("touch ../src/${file}.l");
unless (rename "src/CMakeFiles/_doxygen.dir/build.make","src/CMakeFiles/_doxygen.dir/build.make.old") {
print STDERR "Error: cannot rename src/CMakeFiles/_doxygen.dir/build.make!\n";
exit 1;
}
if (open(F,"<src/CMakeFiles/_doxygen.dir/build.make.old")) {
unless (open(G,">src/CMakeFiles/_doxygen.dir/build.make")) {
print STDERR "Error: opening file build.make for writing\n";
exit 1;
}
print "Processing build.make...\n";
while (<F>) {
if ( s/flex \$LEXFLAGSLEXFLAGS -d(.*) ${file}.l/flex \$(LEX_FLAGS)$1 ${file}.l/ ) {
print "Disabling debug info for $file\n";
}
elsif ( s/flex \$LEXFLAGSLEXFLAGS(.*) ${file}.l$/flex \$(LEX_FLAGS) -d$1 ${file}.l/ ) {
print "Enabling debug info for $file.l\n";
}
print G "$_";
}
close F;
unlink "src/CMakeFiles/_doxygen.dir/build.make.old";
}
else {
print STDERR "Warning file src/CMakeFiles/_doxygen.dir/build.make does not exist!\n";
}
# touch the file
$now = time;
utime $now, $now, $file;
```

另一种从flex代码中获取规则匹配/调试信息的方法是，使用make 设置LEX_FLAGS。（make LEX_FLAGS=-d）。

运行doxygen -d lex 你会得知哪里使用了 flex codefile。













原来filter的原理还是很简单的，就是读源代码，然后向stdout输出转换过程序。不管什么语言都要转换成对应的C/C++的元素才能被doxygen理解。https://www.cnblogs.com/windtail/archive/2012/05/12/2623179.html 完全可以写一个filter.lua，然后将Doxyfile里的 FILTER_PATTERNS = *.lua=filter.lua
并且一开始不了解doxygen的格式，甚至可以忽略文件参数，直接输出看看doxygen会得什么格式，

这样的filter.lua将会导致任何的lua文件都能转换成相同的doxygen网页。
了解了原理之后，我们就可以自己动手写filter了，但是lua的语法其实并不简单的，完全映射到C/C++感觉还是有困难的，倒是跟Javascript有几分神似。所以用Lua来写这个filter很难做好。官网的FAQ里也写明了，对于一些与C/C++不太相似的语言，可以考虑修改doxygen源代码中的scanner.l文件，扫了一眼源代码，感觉可以参照源代码中的InsideJS做特殊处理的地方来使doyxgen支持lua，应该是具有可行性的。当然，也可以考虑像tcl一样，写一个专门的Lexer来做filter（用flex或antlr），希望有时间，有能力的同志来完成这件事吧^_^，暂时我还是用那个perl脚本比较好。

## 可执行的 doxytag 

是一种外部文档索引生成工具，当然所谓外部文档也是应由 doxygen 生成的，doxytag 特别适合于所基于的外部文档不包含源程序时的情况。具体查看 Doxytag 用法


Doxygen 是通过文件的扩展名来决定如何处理文件的。如果某个文件扩展名为 .idl 或 .odl，那么这个文件即被认为
是 IDL 文件。如果某个具有 .java 扩展名，那么即被认为是由 Java 语言写成的文件。同样，.cs 是 C# 文件，.py 文件
作为 Python 来处理；.php、.php4、.inc 或 .phtml 被认为是 PHP 源文件。其他的就被认为是 C/C++文件处理，其中
以 .m 结尾的被认为是 Object-C 文件处理。



# 生态关联

Doxygen 与 Sphinx 不能直接关联，即 Sphinx 不能直接使用 Doxygen 生成的内容来生成 Sphinx 文档，它还需要一个插件来做适配，Breathe 就是为了连接 Doxygen 与 Sphinx 而生。https://github.com/xizhibei/blog/issues/139


# 源码阅读和demo雏形自建






https://zhuanlan.zhihu.com/p/45888762
徒手doxygen项目



## 源码编译

doxygen官网：
https://www.doxygen.nl/index.html

```
sudo apt-get install flex
sudo apt-get install bison
```
https://www.doxygen.nl/manual/install.html
官方构造教程说了，winflex，winbison下载安装之后，修改文件名为bison,flex就行。



```
git clone https://github.com/doxygen/doxygen.git
cd doxygen
mkdir build
cd build
cmake -G "Unix Makefiles" .. 
make -j4
sudo make install

```

具体选用build的对象直接在`cmake --help`查询`Visual Studio 16 2019`
windows

```
cd c:\\tools
tar zxvf doxygen-x.y.z.src.tar.gz # http://gnuwin32.sourceforge.net/packages.html


mkdir build
cd build
cmake -G "Visual Studio 16 2019" ..
```


这里看到安装的flex,bison



```
-- Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.19042.
-- The C compiler identification is MSVC 19.29.30038.1
-- The CXX compiler identification is MSVC 19.29.30038.1
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe - works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30037/bin/Hostx64/x64/cl.exe - works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PythonInterp: D:/Users/tridu33/anaconda3/python.exe (found version "3.8.3")
-- Found FLEX: D:/arch/myenv/flex.exe (found version "2.6.4")
-- Found BISON: D:/arch/myenv/bison.exe (found version "2.7")
-- Looking for pthread.h
-- Looking for pthread.h - not found
-- Found Threads: TRUE
-- Looking for iconv_open
-- Looking for iconv_open - not found
-- Performing Test ICONV_COMPILES
-- Performing Test ICONV_COMPILES - Success
-- Found Iconv: D:/tridu33/latex/doxygen/windoxygen/winbuild/iconv64.lib
-- One (and only one) of the ICONV_ACCEPTS_... tests must pass
-- Performing Test ICONV_ACCEPTS_NONCONST_INPUT
-- Performing Test ICONV_ACCEPTS_NONCONST_INPUT - Failed
-- Performing Test ICONV_ACCEPTS_CONST_INPUT
-- Performing Test ICONV_ACCEPTS_CONST_INPUT - Success
-- The javacc executable not found, using existing files
-- Configuring done
-- Generating done
-- Build files have been written to: D:/tridu33/latex/doxygen/windoxygen/build
```
Have you used the "**Visual Studio command prompt 打开而不是cmd,powershell**" from the Tools menu inside Visual Studio? A plain command window does not work.

湖或者命令行版本编译

```
mkdir build
cd build
cmake -G "NMake Makefiles" ..
nmake
```
# 有得选的话：UTF-8最好不要带BOM

简单说就是文件开头的ef、bb、bf

用xxd指令看一下这个文件，可以看到BOM头，这个文件就是带BOM的UTF-8的文件
一开始生成的打印文件编码格式是UTF-8 Unicode text，通过先写入BOM头ef bb bf，生成 UTF-8 Unicode (with BOM) text
```
xxs *.h
```
![](_v_images/1627789068_11576.png)
图中这几个.h文件压缩备份，修改为 带有BOM的utf8就能正确编译

- C++ 中出现“error C2001: newline in constant“问题的解决方法

txt记事本打开保存为“utf-8 with BOM”


微软在UTF-8中使用BOM（Byte order mark）是因为这样可以将UTF-8和ASCII等编码明确区分开。 

windows对于utf-8格式的文件存储默认是带有BOM的格式

因为在UNIX环境下，很多的UNIX程序不认识BOM。主要是在UNIX所有脚本语言首行为#！标示，它依赖于shell解析，而很多shell出于兼容的考虑不检测BOM，所以加进BOM时shell会把它解释为某个普通字符输入导致破坏#！标示。比如很多现代脚本语言，例如python，其解释器本身是能处理BOM的，但是shell卡在这里。
因此我们在linux服务器上读取这些txt文件时，会遇到如下报错： 

\xef\xbb\xbf…

解决方法

```
import codecs

with open("xx.txt",'r','utf-8-sig') as file:

        line = file.readlines()

```
或者：
```

#打开文件,此次应指定编码，

fr=open(filename,'r',encoding='utf-8')

#读取文件所有内容

arrayOLines=fr.readlines()

#针对有BOM的UTF-8文本，应该去掉BOM，否则后面会引发错误。

arrayOLines[0]=arrayOLines[0].lstrip('\ufeff')

```




































