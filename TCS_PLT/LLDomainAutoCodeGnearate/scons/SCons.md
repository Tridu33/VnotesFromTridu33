





# 1. SCons
http://www.tastones.com/stackoverflow/scons/ 文档

scons主页： http://www.scons.org
scons文档： http://www.scons.org/documentation.php


SCons 构建工具




https://www.rt-thread.org/document/site/programming-manual/scons/scons/
中文文档






SCons是一个开源软件构建工具。将SCons视为经典的Make实用程序的改进的跨平台替代品，它具有类似于autoconf / automake和编译器缓存（例如ccache）的集成功能。简而言之，SCons是一种更轻松，更可靠和更快的软件构建方式。

是什么使SCons更好？

配置文件是Python脚本-使用真正的编程语言的力量来解决构建问题。

可靠，自动的依赖关系分析内置于C，C ++和Fortran中-不再需要“使依赖”或“使干净”来获取所有依赖关系。通过其他语言或文件类型的用户定义的依赖关系扫描程序，可以轻松扩展依赖关系分析。

对C，C ++，D，Java，Fortran，Yacc，Lex，Qt和SWIG的内置支持，以及构建TeX和LaTeX文档。通过用户定义的Builders可以轻松扩展其他语言或文件类型。

从源代码和/或预建目标的中央存储库中构建。

对Microsoft Visual Studio的内置支持，包括生成.dsp，.dsw，.sln和.vcproj文件。

使用MD5签名可靠地检测构建更改；对传统时间戳的可选，可配置的支持。

支持并行构建-像make -j一样，但无论目录层次结构如何，都能使N个作业同时运行。

集成的类似Autoconf的支持，用于查找#include文件，库，函数和typedef。

所有依赖项的全局视图-不再需要多次构建传递或对目标进行重新排序以构建所有内容。

能够在缓存中共享构建的文件以加快多个构建的速度-类似于ccache，但适用于任何类型的目标文件，而不仅限于C / C ++编译。

专为跨平台构建而设计，已知可在Linux，其他POSIX系统（包括AIX，BSD系统，HP / UX，IRIX和Solaris），Windows 7/8/10，MacOS和OS / 2上运行。

SCons是从哪里来的？

SCons最初是作为ScCons构建工具设计而诞生的，该设计在2000年8月赢得了Software Carpentry SC Build竞赛。该设计又基于Cons软件构建实用程序。该项目已重命名为SCons，以反映该项目不再与Software Carpentry直接连接（嗯，这样做使键入更加容易...）。









