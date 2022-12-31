



两大类的区别主要是定义的宏不一样，win32 项目和mfc的为WINDOWS，win32控制台的为CONSOLE，所以：在预处理中把_WINDOWS换成_CONSOLE就行了 。  project  settings  ->  Link  :将/SUBSYSTEM:WINDOWS开关改为/SUBSYSTEM:CONSOLE  。另外， 可将  Win32控制台程序  当成  在Win32项目  使用，反之亦然。/subsystem:windows或/subsystem:console删除,由编译器自己决定也可以

# 1. visual studio 2019


Visual Studio 2017 C/C++使用教程2 https://www.bilibili.com/video/BV1zs411u7vp 

1. Help Viewer安装
2. 解决方案与项目的关系
3. Visual Studio解决方案目录结构
4. Win32控制台与Win32项目区别
5. 如何让程序在小伙伴机器上运行
6. 程序调试

大多数想单纯创建c++工程的新同学，打开vs后很可能不知道选择创建什么工程，这时候请相信我，空项目是你最好的选择。因为空工程不包含任何的源代码文件，接下来你只需要在相应的源代码文件夹和头文件文件夹加入相应的.cpp和.h文件即可。 https://blog.csdn.net/sl850216662/article/details/78642802 windows提供**win32 api**以供程序员完成各种操作，所以控制台，win32，mfc都可直接调用win32 api。但直接使用win32 api，用代码完成诸如创建窗口，显示窗口等操作太过繁杂，于是我们把这些代码结合抽取出来，变成OOP中的类，也就是**微软基础类库（MFC）**

- 第一类包括win32控制台应用程序

没有界面，只有命令符。生成的“.exe”文件直接运行操作即可

Win32控制台程序：初始代码模版以main为程序入口，默认情况下，只链接C++运行时库和一些核心的win32库，链接器subsystem参数为console类型，所以编译出来的程序会有黑色的控制台窗口作为呈现标准输入（stdin）和标准输出（stdout）。



- 第二类win32项目、mfc项目

win32项目包含mfc



Win32项目，有界面。但是界面里面的控件，基本上要自己去实现。
Win32项目：初始代码模版实现一个简单的windows窗口，以WinMain作为程序入口，引用了win32Api头文件和库，链接器subsystem参数为windows，所以生成的程序不带黑色的控制台，直接使用标准输入和标准输出，看不到效果。


MFC应用程序，也有界面，但界面里的控件不需要自己去实现了，常用的控件都已经在MFC库内写好，直接拖动即可。

Win32项目的界面比较符合UI界面设计；而MFC应用程序的界面基本都是一样的，因为它们都是用同一套控件模板。

MFC应用程序：本质上是个win32工程，只是默认帮你引用了mfc框架的头文件和库，并且程序入口由mfc框架提供，不需要自己写






## VS工程目录
解决方案相关的文件：

TestProject.sln： 整个解决方案 ( Solution ) 的配制文件，组织多个工程和相关的元素到一个解决方案中。用鼠标双击它就能用 VS 打开整个工程项目。

TestProject.sdf： 浏览相关的数据库文件，它支持浏览和导航的特性。如跳转到方法、变量的声明，查找所有对象的所有被引用的地方，类视图等等。

TestProject.suo： (solution user opertion) 解决方案用户选项,记录所有将与解决方案建立关联的选项， 以便在每次打开时，它都包含您所做的自定义设置.

TestProject.opensdf： 打开解决方案( Solution ) 时的临时文件，这个文件只有你的解决方案在 VS 打开的状态才会有，工程一关闭文件就被删除了。

工程相关的文件

TestProject.vcxproj： 记录工程( Project )相关的属性配制。

TestProject.vcxproj.filters： 文件过虑器，上图 3“工程结构”中各个文件的组织和编排都是定义在这个文件中的。如果由于某种特殊的原因(如系统或 VS 突然崩溃)导致你打开工程时文件的组织结构是乱的，100%就是这个文件的原因。

TestProject.vcxproj.user： 用户相关的一些配制。

上面这些文件中有几个比较重要的一定不能删的文件是： TestProject.sln、TestProject.vcxproj、TestProject.vcxproj.filters

不要问我是怎样知道这些文件的作用的，请看官方文档：

 VS2010 定义：https://msdn.microsoft.com/en-us/library/3awe4781.aspx. 
 
VS2015 定义：https://msdn.microsoft.com/en-us/library/vstudio/hx0cxhaw(v=vs.110).aspx

https://www.colourso.top/vs-use/ VS开发C++的一些问题——VS项目工程文件、Debug与Relase模式、字符集问题以及_T()宏








External Dependencies： 工程的外部依赖文件，这个目录是 VS 自动生成的，你最好别动它。

Header Files： 头文件，也就是 .h(.hpp) 后缀的头文件。

Source Files： 源文件，也就 .cpp (或.c，针对 C 语言)后缀的文件。

Header Files： 资源文件，如果你创建的是 MFC 的工程，*.rc 文件就会在这里。


VS是使用解决方案来管理项目的，同一个解决方案之下就可以添加多个项目。

----------------------------------------------




sdf文件是一个数据库文件，记录了解决方案的各种信息。

opensdf文件是项目被打开时才会出现的，项目关闭后此文件也会消失，估计是sdf文件的临时文件。

sln文件是整个解决方案的配置文件，（Microsoft Visual Studio Solution），通过VS2013打开sln文件就可以将整个解决方案导入到VS中打开。



sln（Visual Studio.Solution）通过为环境提供对项目、项目项和解决方案在磁盘上的位置的引用，可以将他们组织到解决方案中。



suo文件（Visual Studio Solution User Options）是解决方案用户选项。

suo 解决方案用户选项，记录所有将与解决方案建立关联的选项，存储了用户对界面的自定义配置，包括布局、断点、打开的文件等。



vcxproj文件是项目文件，保存了整个项目的配置信息。经过测试可以通过打开这个文件来直接打开这个项目以及解决方案。

vc5,6的工程文件是.dsp

vc2002-2008工程文件是vcproj

vc2010之后是vcxproj

vcproj和vcxproj都是xml格式的。

vcxproj.filters文件是文件存放工程的虚拟目录信息，也就是在解决方案浏览器中的目录结构信息。



------------------------------------------------------------------------------

Debug文件夹是VS在 Debug 模式下编译链接执行后生成的文件夹， 与之相对应的是 Release 模式，在此模式下就会生成Release文件夹。




打开Debug文件夹，其内有上述这些文件。

log文件是主要记录编译过程中的输出信息、日志。可以打开看看，内容和执行时的内容差不多。

pdb文件是调试的符号文件，程序数据库 (PDB) 文件保存着调试和项目状态信息，使用这些信息可以对程序的调试配置。

obj文件是C、CPP编译后的二进制文件。

VS执行生成的可执行文件放在解决方案目录里的Debug目录里。
exe文件是编译链接后产生的可执行文件。

ilk文件 增量编译（incremental linking）

取消增量编译可以不生成这种文件，对于大工程来说可能会变慢。





---------------------------------------------------

最后摘抄一段话

>一般情况下，如果我们要把源码共享到github中，只需要提交工程相关的配置文件，不提交用户个人偏好相关的配置文件。所谓的个人偏好相关，是指根据用户个人的VS使用习惯而保存的配置信息，比如选择了查看所有文件选项，打开了某一个文件。而工程相关的配置是指工程建立相关的信息，不受用户偏好的影响，比如解决方案的名字是什么，这个解决方案下面有哪些project。所以，我们只需要上传**sln配置文件、vcxproj和vcxproj.filters配置文件**就可以了，当然还包括源码。