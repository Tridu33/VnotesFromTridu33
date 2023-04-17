
## 调用图工具

https://marketplace.visualstudio.com/items?itemName=MichaelKissBG8.VS10xCodeMAP

这里有安装教程
仅供Enterprise版本使用**Code Map** Is only available for the enterprise version though
For anyone who's trying, one can use Ndepend extension. Its cool. 14 day trail version though.


VS 2019 扩展：使用 **NDepend** 静态分析您的代码  https://www.ndepend.com/docs/getting-started-with-ndepend 14天免费试用



使用**CodeViz**生成C/C++函数调用关系图




StarUML逆向工程: 通过代码生成类图 https://blog.csdn.net/qq_20480611/article/details/51287038


https://marketplace.visualstudio.com/items?itemName=YaobinOuyang.CodeAtlas
vs 2019

https://github.com/tarun27sh/gdb_graphs 用gdb查看cpp调用图


# 1. cpp2uml




PlantUML PlantUML是一个开源项目，支持快速绘制UML

https://plantuml.com/zh/



## include图
IncludeToolbox  https://marketplace.visualstudio.com/items?itemName=Wumpf.IncludeToolbox include网络

cinclude2dot.pl是一个perl脚本，它分析C / C ++代码并生成#include依赖关系图作为点文件以输入到graphviz。

http://www.flourish.org/cinclude2dot/

如果您不想采用这种手动工具，那么在我看来，迄今为止最成功的工具是ProFactor中称为" IncludeManager"的工具。

http://www.profactor.co.uk/includemanager.php

有一个免费试用版，而且很棒。这是一个完全集成的Visual Studio插件，因此双击此处的内容将带您到那里包含该内容的地方。

工具提示的鼠标悬停可为您提供所有您想要的信息，它使您可以向上/向下钻取，删除不需要的整个子树，查看除图形之外的表示形式，在匹配列表中循环浏览，这真是太好了。

如果您很快了解，则可以在试用期结束之前重构大型项目的#include结构。即使这样，它也不会花费太多，每个许可证约35美元。

就其功能而言，它几乎是完美的。不仅#include图形，而且跨共享文件的项目依赖关系，对构建时间的影响，网格中的详细属性都完美。






-----------------------------------------------------

现在有一个名为IncludeToolbox的Visual Studio插件。 它可以列出您的依赖包含，并执行更多操作，如随机删除和编译，以查看是否需要包含。

编译器还支持/ showIncludes开关 - 它不会为您提供行号，但可以提供一个非常全面的视图，其中包括来自哪里。

它在项目设置下 - ＆gt; 配置属性 - ＆gt; C / C ++ - ＆gt; 高级 - ＆gt; 显示包含。

有一个设置：

项目设置 - ＆gt; 配置属性 - ＆gt; C / C ++ - ＆gt; 高级 - ＆gt; 显示包含

这将生成树。 它映射到编译器开关/ showIncludes

Visual Studio编译器(cl.exe)具有选项/showIncludes，当您编译文件时，该选项将向您显示包含树。

如果您需要单个文件的此信息，则可以在解决方案资源管理器中右键单击该文件，选择"属性"，然后在"命令行"部分中将/ showIncludes添加到"其他选项"。 (请注意，我使用的是VC ++ 2005，因此对于较新的版本可能有所不同)。

您得到的输出有点...令人费解，但是它显示了包含什么内容以及包含什么顺序。

顺便说一句，GCC和Intel C ++编译器(至少是我的版本)中的相同功能是-H。

---------------------------

Visual Studio团队在今年6月份发布的Visualization and Modeling Feature Pack 工具包中，实现了对C/C++代码的可视化功能。https://developer.aliyun.com/article/246608
在安装了这个工具包后，就可以通过创建依赖项关系图（Dependency Graph）来了解和分析已有的C/C++代码工程了。这里我们以VS C++团队编写的Hilo工程 为例，来展示一下如何为C++ 工程创建依赖项关系图，**Hilo**的源代码可以在 http://code.msdn.microsoft.com/Hilo 下载到。
在VS中打开Hilo工程，选择菜单“体系结构”->“生成依赖项关系图”，如下图所示。在子菜单中，“按程序集”、“按名字空间”和“按类和自定义”是在VS 2010发布版中就有的，它们也可以用于C/C++的工程。这里新增加的一个菜单项是 “By Include File”，它是用来生成C/C++文件之间的#include引用关系的，会在另外的博客中进行介绍。注意：Visualization and Modeling Feature Pack仅提供了英文版，它可以安装在其它语言版本的VS 2010上，但显示的内容仍是英文的。




# Visual Studio的CodeMap功能
https://blog.yowko.com/visual-studio-2017-code-map/ 介绍



[SCDN官方安装教程](https://docs.microsoft.com/zh-cn/visualstudio/modeling/map-dependencies-across-your-solutions?view=vs-2019&redirectedfrom=MSDN&viewFallbackFrom=vs-2015)

简单的说，这个工具类似反向工具一样，可以帮我们把想要看的Class关系、 Function关系，用图表关联起起来，甚至还可以点两下后，快速的寻览；    

在我们修复Bug时，我们先要梳理复杂的函数调用关系。通常的做法是我们在纸上去画函数调用关系。对于比较简单的调用，这种方法行之有效，对于复杂的调用关系，这种方法就显得力不从心了。CodeMap正是为了解决这个问题而产生的。
        通常我们从一个方法开始梳理方法中调用到的方法，然后形成一张网状图，如下：

这张图能够很清晰地说明调用关系，并且这个图还有很强大的功能：

1.支持拖拽操作；

2.支持快速定位函数调用（双击即可）；

3.支持共享（通过邮件共享给其他人）；

4.添加注释；

5.保存图件供分析；


更多的内容请大家看官方视频：http://pan.baidu.com/s/1c0niio4

提取码：yx9k














# 如何进行开源项目的学习



https://github.com/zhuangbiaowei/learn-with-open-source/blob/master/zh/Understanding-the-source-code.md




C++ 源码阅读项目推荐 http://coney.github.io/2015/08/cpp-projects-for-source-reading/



-----------------------
# 看代码工具


四个工具链接：https://www.zhihu.com/question/21499539/answer/1958299570
集齐了：


1. javatree. pl: https://github.com/satanson/cpp_etudes/blob/master/javatree.pl

2. java_calltree. pl: https://github.com/satanson/cpp_etudes/blob/master/java_calltree.pl
Java代码阅读工具java_calltree.pl - satanson的文章 - 知乎
https://zhuanlan.zhihu.com/p/371369319

3. cpptree. pl: https://github.com/satanson/cpp_etudes/blob/master/cpptree.pl
C++阅码神器cpptree.pl和calltree.pl的使用 - satanson的文章 - 知乎
https://zhuanlan.zhihu.com/p/339910341

4. calltree. pl: https://github.com/satanson/cpp


工具使用案例

OpenHarmony中c/c++/java源码概况 - satanson的文章 - 知乎
https://zhuanlan.zhihu.com/p/378239703
看看sogou workflow的源代码 - satanson的文章 - 知乎
https://zhuanlan.zhihu.com/p/359104170






