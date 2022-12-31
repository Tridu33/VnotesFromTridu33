# Autogenerator_ Generation and execution of programming code on demand


gpml.foi.hr/ubl/form.cgi


https://gpml.foi.hr/SCT_Autogenerator_Example/video/SCT%20Autogenerator%20Example.mp4 视频教程







https://gpml.foi.hr/SCT_Autogenerator_Example/




网站凉了，不用看这个了 https://gpml.foi.hr/SCT_Autogenerator_Example/ 没给源码网站还凉凉了，而且Specification视频中写一大坨




Autogenerator核心的源代码生成器基于我们先前介绍的动态框架模型，该模型以以下模型元素命名为SCT：规格，配置和模板（Radošević和Magdalenić，2011b）。SCT模型的高度灵活性使Autogenerator的实现难以通过其他方法（如XVCL（Jarzabek，Bassett，Zhang和Zhang，2003年）或CodeWorker（Lemaire，2010年））实现。





与XVCL不同，Autogenerator依赖于动态框架，这意味着框架是在源代码生成过程中动态创建的（Radošević和Magdalenić，2011b，Radošević等，2012）。

在SCT生成器模型中，生成器由三种元素定义：规范（S），配置（C）和模板（T）（Radošević＆Magdalenić，2011b）。规范包含属性-值对形式的已生成应用程序的功能。


https://generativeprogramming.com/history/


Autogeneration is a programming concept of producing program code and its instant execution:
**on demand **
and
**without storing**

This concept is:
based on our previously introduced **SCT generator model**  closely associated with scripting languages

Some benefits of using Autogeneration are:
 
Changing the application ‘on the fly’ 

– all changes in Specification, Configuration and Templates are instantly updated in the application (even if it is already working)


Imperative statements in Specification

– are used to perform rarely used instructions, usually connected with updating program dependencies, like databases


Code introspection 

– finding the SCT origin of generated action


Optimization opportunities 

– there is no need to regenerate the whole application on each user’s demand i.e. only the needed part (i.e. according to requested action, used dataset, etc.) has to be generated





2001-2004
初期的想法：
–如果使用脚本语言（例如Perl，PHP等）的Web应用程序生成html文档，为什么我们也不生成应用程序脚本？
–使Web应用程序经常执行相同工作但使用不同数据结构（例如，来自数据输入表单的数据）的不同程序脚本。我们为什么不建立一种变体机制来生成可用于不同数据结构的脚本？
–脚本语言在生成型编程中的使用（由面向对象的语言组成），因为它们可以灵活地处理不同的数据类型
第一个生成器是用Perl编写的，因为它具有字符串处理功能，可以在Perl和ASP中生成不同的Web应用程序。这些应用程序主要用于远程数据库内容管理，在线调查表和学生测试。

2005-2006
年建立GSM（发电机脚本模型）。GSM引入了表示发电机的图形图。规范图表示应用程序规范的层次结构，而规范本身由属性值对组成。元脚本图（后来的配置图）通过连接规范数据和代码模板（元脚本）来定义汇编程序文件。

The concept was firstly named SGM (Scripting Generator Model). SGM introduced graphic diagrams aimed specifically for modeling generators. The Specification Diagram defines features of target application to be generated and their hierarchy, while The Configuration Diagram defines the dispersion of these features (i.e. aspects) on the different application parts.


除了使用脚本语言生成Web应用程序外，GSM还用于生成Java和C ++应用程序。一些生成器是用Java编写的。


扩展了
2007-2008 GSM基本模型以支持代码模板的后期绑定，类似于OOP中的动态多态性的概念。由于可以添加新的代码模板而无需更改生成器配置，因此这可以使生成器具有更精确的规范和可扩展性。生成用于生成器的C ++库。这些生成器（用C ++编写）基于生成对象，该对象支持polymorpih功能。

建立了2009-2013年
SCT（规格-配置-模板）模型。它继承了GSM的基本概念和图形图，但启用了完全可配置的代码生成器。不再需要对生成器进行编程，因为它的所有功能都是在配置中定义的，可以轻松更改。由于该语言具有强大的面向对象功能，因此我们在SCT生成器的实现中使用Python，从而保持了脚本语言的类型操作灵活性。SCT生成器使用SCT帧的动态实例化机制，这使生成器的维护更加容易（仅应修改顶级帧）。

SCT可以快速开发发电机并轻松修改发电机。使用相同的程序规范可以实现不同的输出类型（和输出文件）。生成器模型的使用范围已扩展到构建学生考试，其中包括目标编程语言（例如C ++）中的程序代码以及不同学生的任务和解决方案的生成。

2013-
Autogenerator按需生成并执行编程代码。实际上，Autogenerator利用脚本语言的可能性来评估变量中的编程代码。
















