




Lisp-machine考古文
https://danluu.com/symbolics-lisp-machines/ 多年来，Richard Stallman 一直在讲述有关 Lisp 机器公司的起源以及对 MIT 人工智能实验室的影响的故事。他在一本书和一篇被广泛引用的论文中发表了它，您可以在http://www.gnu.org/gnu/rms-lisp.html找到该论文。


Lisp machine 这种用 Lisp 代码当机器的汇编指令的硬件实现为什么销声匿迹了？硬件和 Lisp 这样的高级语言两个极端如何融合在一起？ - LdBeth的回答 - 知乎
https://www.zhihu.com/question/20753279/answer/404561702
# Lisp-machine


GitHub - MMcM/lmkbd2: Lisp Machine Keyboard USB driver
https://github.com/MMcM/lmkbd2

符号 Lisp 机器博物馆 https://smbx.org/


Lisp machine 这种用 Lisp 代码当机器的汇编指令的硬件实现为什么销声匿迹了？硬件和 Lisp 这样的高级语言两个极端如何融合在一起？ - LdBeth的回答 - 知乎
https://www.zhihu.com/question/20753279/answer/404561702 答 eBay有 https://www.reddit.com/r/lisp/comments/b2i6ly/want_to_buy_symbolics_lisp_machine/

Lisp Machine 用 Lisp 做汇编指令纯属误传，虽然编译器能将 Lisp 编译成机器指令，也可以将机器转回人可读的 Lisp 代码，从某种角度来说，Lisp 处于直接和机器指令之间转换的层次，和现在常见的计算机的汇编是类似的。但说 Lisp Machin 用 Lisp 做汇编是不严谨的，因为 Lisp Machine 也有自己的汇编语言。
Lisp Machine 出现的背景是 16 位处理器向 32 位的迁移，主流 32 位处理器上运行的 Lisp 实现性能不理想，才有了 Lisp Machine 这一构想。当时的 Lisp Machine 有两大派系，MIT 和 Xerox ，分别对应当时两大主流方言 MacLisp 和 INTERLISP。我对 Xerox Lisp Machin 了解不多，以下主要基于 MIT Lisp Machine 的设计。
(MIT) Lisp Machine 的处理器实际就是个栈机器，**Lisp 代码依次转化为栈操作执行**：参数先依次压入栈，供计算指令调用，执行结果输出到返回栈。函数内部的函数调用就是建立一个新的栈帧，压入参数，输出结果到返回栈。一些特殊的函数直接实现成机器指令，从 destination 接受参数直接输出到返回栈。
Lisp Machine 设计成熟时期，用 Lisp Machine 做数值运算比在当时 32 位处理器上的 Fortran 还快。最大的特色其实是支持大屏图形界面和鼠标。
很显然这种微处理器是复杂指令集设计，在现代已经过气了。后来基本等于免费分发的 Unix 配合摩托罗拉之类的廉价硬件平台很快取代了几十万美元一台的 Lisp Machine，导致本就经营不善的最大 Lisp Machine 公司之一 Symbolics 挂了，对业界又造成了打击。
说 Lisp Machine 没有进程，Lisp 不适合用来描述操作系统云云，至少对于后期的 Lisp Machin 来说是错误的。Symbolics Lisp Machine 用物件导向设计操作系统，包括进程在内几乎所有系统构建抽象成物件，Lisp Machine Manual 的原句就是进程相当于虚拟 CPU。Unix 的一切皆文件就是一种弱层次的物件导向设计，Mach 微内核更是大量采用了物件导向设计，就连 Linux 都不可避免引入了 C艹，明显同时具有高级抽象和底层硬件的 Lisp Machin Lisp 是很合适的，而内核态和用户态的访问直接由定义方法来控制，这些问题在 Lisp Machine 还没过气之前都已经解决了。
两个时代硬件的比较，Lisp Machine 晚期在 DEC Alpha 工作站上用虚拟机运行 Lisp Machine，做一次内存整理花费约 40 分钟，将同样的虚拟机移植到 Linux 后在 Core i7 四核上运行做相同操作，只要不到一分钟。
References:

[1] Guy Steele and Richard Gabriel, The Evolution of Lisp

[2] Richard Stallman, Daniel Weinreb and David Moon, Lisp Machine Manual, 6th Edition

---------------------------------------------------------------------------------
## awesome-lisp-machine





GitHub - ghosthamlet/awesome-lisp-machine: A curated list ...
https://github.com/ghosthamlet/awesome-lisp-machine





## 语言机器

- [历史](https://danluu.com/symbolics-lisp-machines/)- 符号 Lisp 机器的历史。
- [历史]( http://www.andromeda.com/people/ddyer/lisp/ , https://hndex.org/15355979 ) - Lisp 机器简史。
- [博物馆](https://www.ifis.uni-luebeck.de/~moeller/symbolics-info/index.html)- 符号 Lisp 机器博物馆。
- [博物馆](http://smbx.org/)- 符号 Lisp 机器博物馆。
- [Repository](http://www.unlambda.com/) - 各种 lisp 机器相关项目的存储库。
- [复活](https://lm-3.github.io/)- 复活 MIT CADR。
- [PilMCU](http://www.mail-archive.com/picolisp@software-lab.de/msg04823.html) - 芯片上的 Lisp 机器。
- [手册](https://hanshuebner.github.io/lmman/title.xml)- Lisp 机器手册（1984 年）。
- [Architecture](http://www.cs.utah.edu/~mflatt/past-courses/cs6510/public_html/lispm.pdf) - LISP 机器的架构。
- [Story](http://kremlin.enterprises/post/129364443055/your-code-is-so-bad-we-had-to-make-etclocal) - 关于符号 Lisp 机器的故事.
- [链接](http://www.lispmachine.net/)- Lisp/Lisp 机器链接。
- [链接](http://fare.tunes.org/LispM.html)- 关于 LISP 机器。
- [DIY](https://www.jwz.org/blog/2016/11/dick-tracy-wrist-mounted-lisp-machine/) - Dick Tracy 手腕式 Lisp 机器。
- [什么是 Lisp 机器](https://www.quora.com/What-is-a-lisp-machine-and-what-is-so-great-about-them)- 什么是 Lisp 机器，它们有什么了不起的地方？
- [计划机器](http://burgerrg.github.io/TR413.pdf)- 计划机器。
- [K-machine](http://fare.tunes.org/tmp/emergent/kmachine.htm) - Lisp Machine Inc. K-machine.
- [Symbolics](http://lispm.de/symbolics-lisp-machine-ergonomics) - Symbolics Lisp 机器的人体工程学 - 对开发人员生产力的思考。

## Lisp 操作系统

- [关于 LispOS](http://metamodular.com/Common-Lisp/lispos.html) - 多么棒的 LispOS。
- [Specification of LispOS](http://metamodular.com/lispos.pdf) - Lisp 操作系统的规范。
- [Mezzano](https://github.com/froggey/Mezzano) - 用 Common Lisp 编写的操作系统。
- [PilOS](https://picolisp.com/wiki/?PilOS) - 运行 picolisp 的 PilOS.
- [Yalo](https://github.com/whily/yalo) - 在裸机 x86-64 硬件上运行的 Lisp 操作系统。
- [3L](https://3lproject.org/) - 3L 项目正在从头开始构建一个安全、私有、安全和可扩展的计算系统。
- [ChrysaLisp](https://github.com/vygr/ChrysaLisp) - 并行操作系统，带有 GUI、终端、OO 汇编器、类库、C 脚本编译器、Lisp 解释器.
- [ECMAchine](https://github.com/AlexNisnevich/ECMAchine) - 基于 Lisp 的浏览器内玩具操作系统。
- [Losak](https://sourceforge.net/projects/losak/) - 用于通用计算机体系结构的基于 ffLisp 的操作系统。
- [LispOS](https://github.com/robert-strandh/LispOS) - 一个用 Common Lisp 及其交互环境编写的操作系统，但特别受到启发。
- [Flisp](https://github.com/fjames86/flisp) - 一种类似 Scheme 的 Lisp 解释器，也可以作为操作系统运行。
- [Lispix](https://github.com/saniv/lispix) - Lisp 解释器和操作系统。
- [LOS-64](https://github.com/afonsotrepa/LOS-64) - 用 C、asm 和 Common Lisp 编写的用于 x86-64 的小型 LISP-1 操作系统。
- [Lambda Lisp 操作系统](https://github.com/dseagrav/Lambda-system-software)- 此存储库用于跟踪 LMI Lambda 操作系统软件中的问题和更改。
- [DreamOS](https://github.com/AviaNick/DreamOS) - David Joseph Stith 在 Scheme 中编写的小型 x86 操作系统.
- [Links](http://linuxfinances.info/info/lisposes.html) - 基于 Lisp 的操作系统。





















------------------------------------------------------















Lisp Machine 也有自己的汇编语言。


A small Lisp-Machine in an FPGA | Hacker News
https://news.ycombinator.com/item?id=13621953


http://www.aviduratas.de/lisp/lispmfpga/

https://github.com/lisper/cpus-caddr

Verilog FPGA重新实现MIT CADR lisp机器

这是对 MIT CADR verilog 的重写，具有更合理的时钟和同步 RAM。

它包括一个小 nios cpu，用于调试 dram 和 mmc 代码。

它引导负载带并作为 lisp 机器运行。

--------------------------



https://www.allaboutcircuits.com/ip-cores/prototype-board/igor/


语言： VHDL



这是什么？

IGOR 是一个完整的系统，包括：
* 一个带有系统所有组件的 PCB：FPGA、AVR 微控制器、IO 单元、内存......作品。
* 在 FPGA 上运行的已实现处理器。
* 多个 IO 单元，通过并行总线通过 AVR 微控制器连接到主处理器。

处理器是一个微程序处理器，ISA 类似于 Lisp。运行微程序的处理器是类 RISC 的，存储库中目前有两个版本：一个已经在全系统的 FPGA 中运行的多周期处理器，以及一个尚未在开发板上测试的流水线处理器。

正如您所料，将其称为最低级别的完整 LISP 机器是用词不当。尽管有一些自定义，比如支持操作数的类型检查，但最低级别仍然是一个相当简单的类似 MIPS 的 RISC 机器，并且微指令集与您对任何 RISC 处理器的期望相距不远。像所有原始 LISP 机器一样的功能，如硬件支持的 GC 不存在。然而，微程序和 ISA 在很大程度上是一台 Lisp 机器：它实现了垃圾收集、动态类型和许多其他特性，这是除了 LISP 之外的特性。

这个项目是因为挪威科技大学计算机与信息科学研究所的课程“TDT4295 - 计算机设计，项目”。该项目由 Assoc 监督。Morten Hartmann 教授

所有关于电路
IGOR - 微程序 LISP 机器
IGOR - 微程序 LISP 机器
细节
类别：原型板

创建时间： 2009 年 12 月 31 日

更新日期： 2020 年 1 月 27 日






-------------------------------------------------------------------------------------------


Lisp Operating System - MetaModular
metamodular.com/Common-Lisp/lispos.html








# lisp machine simulator


各位观众，您有二手的Lisp Machine能转让给我吗？，对 Xerox InterLisp-D workstations印象挺好，TI Explorer也很棒滴，Symbolics和LMI就屏蔽了吧……如果有能支持Common LISP的LM就更好了。
https://www.zhihu.com/question/21847695/answer/19556481 

lisp machine 模拟器网站 http://www.unlambda.com/
http://unlambda.com/lisp/l-machine.page







Hacking nevermore - A TI-Explorer Lisp Machine emulator ...
https://lisp-machine.org/hacking-nevermore-a-ti-explorer-lisp...

Brad Parker 的usim是一个不错的 C 语言仿真器，用于第一台广泛生产的 Lisp 机器，即 MIT-CADR。据说到 1978 年，麻省理工学院生产了超过 25 台，几乎使它成为第一台“生产”Lisp 机器。随后的商业 Lisp 机器大部分起源于 CADR，因此看到大多数想法的起源非常有趣。


Retrocomputing - Symbolics Lisp Machine Emulation
unlambda.com/lisp/l-machine.page



Retrocomputing - MIT CADR Lisp Machines - unlambda
www.unlambda.com/lisp/cadr.page


http://www.lispmachine.net/

https://github.com/LdBeth/star-lisp
GitHub - klmr/lisp.cpp: Minimal Lisp implementation in C++ ...
破解 LambdaDelta，一个 LMI-Lambda 模拟器

## lisp machine虚拟机上的操作系统  genera
https://archives.loomcom.com/genera/genera-install.html

https://en.wikipedia.org/wiki/Genera_(operating_system)

**Genera**是[Symbolics](https://en.wikipedia.org/wiki/Symbolics)创建的Lisp[机器的](https://en.wikipedia.org/wiki/Lisp_machine)[商业](https://en.wikipedia.org/wiki/Commercial_software) [操作系统](https://en.wikipedia.org/wiki/Operating_system)和[集成开发环境](https://en.wikipedia.org/wiki/Integrated_development_environment)。它本质上是源自[麻省理工学院](https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology)(MIT) [AI 实验室的](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory)[Lisp 机器](https://en.wikipedia.org/wiki/Lisp_machine)的早期操作系统的一个[分支](https://en.wikipedia.org/wiki/Fork_(software_development))，Symbolics 曾与[Lisp Machines](https://en.wikipedia.org/wiki/Lisp_Machines) , Inc. (LMI) 和[德州仪器](https://en.wikipedia.org/wiki/Texas_Instruments)(TI) 共同使用该操作系统。Genera 也由 Symbolics 作为**Open Genera**出售，它在基于[Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation) (DEC) [Alpha的计算机上运行 Genera](https://en.wikipedia.org/wiki/DEC_Alpha) 在[x86_64](https://en.wikipedia.org/wiki/X86_64)和[Arm64 ](https://en.wikipedia.org/wiki/Arm64)[GNU/Linux](https://en.wikipedia.org/wiki/GNU/Linux)以及[Apple M1 ](https://en.wikipedia.org/wiki/Apple_M1)[MacOS](https://en.wikipedia.org/wiki/MacOS)上使用[Tru64 UNIX](https://en.wikipedia.org/wiki/Tru64_UNIX)的处理器。它作为[专有软件发布和](https://en.wikipedia.org/wiki/Proprietary_software)[许可](https://en.wikipedia.org/wiki/Software_license)。

Genera 是一个基于编程语言[Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language))[的面向对象操作系统](https://en.wikipedia.org/wiki/Object-oriented_operating_system)的示例。

Genera 支持使用多种编程风格的复杂软件的增量和交互式开发，并广泛支持面向[对象的编程](https://en.wikipedia.org/wiki/Object-oriented_programming)。

---------------------------------------------------------------------------------



Lisp Machine 操作系统是用[Lisp Machine Lisp 编写](https://en.wikipedia.org/wiki/Lisp_Machine_Lisp)的。它是一个单用户工作站，最初针对[人工智能](https://en.wikipedia.org/wiki/Artificial_intelligence)(AI) 项目的软件开发人员。[[1\]](https://en.wikipedia.org/wiki/Genera_(operating_system)#cite_note-1)该系统有一个大的[位图](https://en.wikipedia.org/wiki/Bitmap)屏幕、一个鼠标、一个键盘、一个[网络](https://en.wikipedia.org/wiki/Computer_network)接口、一个磁盘驱动器和用于扩展的插槽。操作系统支持此硬件并提供（除其他外）：

- 前端处理器的代码
- 意味着启动操作系统
- [虚拟内存](https://en.wikipedia.org/wiki/Virtual_memory)管理
- [垃圾收集](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))
- 各种硬件接口：鼠标、键盘、位图帧缓冲区、磁盘、打印机、网络接口
- Lisp Machine Lisp 的解释器和本机代码编译器
- 对象系统：[风味](https://en.wikipedia.org/wiki/Flavors_(programming_language))
- [图形用户界面](https://en.wikipedia.org/wiki/Graphical_user_interface)( GUI) 窗口系统和[窗口管理器](https://en.wikipedia.org/wiki/Window_manager)
- 本地[文件系统](https://en.wikipedia.org/wiki/File_system)
- 支持[Chaosnet](https://en.wikipedia.org/wiki/Chaosnet) (CHAOS) 网络
- 一个名为[Zmacs的类似](https://en.wikipedia.org/wiki/Zmacs)[Emacs的编辑器](https://en.wikipedia.org/wiki/Emacs)
- 一个名为 Zmail 的邮件程序
- 一个 Lisp 监听器
- [调试](https://en.wikipedia.org/wiki/Debugger)器

这已经是一个完整的单用户基于 Lisp 的操作系统和开发环境。

MIT Lisp 机器操作系统是从 1970 年代中期到 1980 年代初开发的。

2006 年，麻省理工学院的 Lisp 机器操作系统的[源代码作为](https://en.wikipedia.org/wiki/Source_code)[免费和开源软件](https://en.wikipedia.org/wiki/Free_and_open-source_software)发布

------------------------------



从 1980 年代初到 1990 年代初，Symbolics, Inc. 生产了一系列工作站，旨在运行称为“Genera”的高度先进的 Lisp 环境。是什么让这些 Lisp 机器如此特别，是在非常专业的硬件之上运行的强大软件的组合。例如，硬件执行数组边界检查并将数据作为类型而不是像其他通用计算机所做的（并且仍然是）那样作为平面位字段进行操作。反过来，Genera 环境提供了工作站级功能，包括大型高分辨率位图图形显示、重叠窗口和鼠标控制。在 1980 年代初期，甚至在 Macintosh 之前，这都是真正先进的东西。

在 1990 年代初期，Symbolics 迈出了大胆的一步，在 Digital Equipment Corporation 的 Alpha 工作站上发布了 Genera 软件环境，改名为“Open Genera”。为了实现这一点，他们创建了一个在 OSF/1（后来的 Digital UNIX）下运行的“Virtual Lisp Machine”（VLM），并模拟了完整的 Symbolics Lisp Machine 架构。

VLM 的源代码是用 Lisp 编写的，执行时会生成 Alpha 汇编指令。在 2000 年代初期，Brad Parker 有了一个绝妙的主意，想看看他是否可以调整 Alpha 汇编生成器以生成 C 代码片段。它起作用了，结果是为 64 位 Linux 编译的。

在这里，我们到达了一个灰色区域。Symbolics 在 1990 年代中期解散，其知识产权的现状很混乱。VLM 和 Genera 本身的权利人是分散的。不再有任何“Symbolics, Inc.”。

考虑到这一点…

本文档旨在指导您在现代 64 位 Linux 系统上安装 VLM 和 Symbolics Open Genera。如果您选择这样做，请注意您可能会或可能不会侵犯他人的版权。玩得开心，玩得安全！



如果您不熟悉 Genera，则*需要阅读*以下内容。

1. [属概念](http://bitsavers.trailing-edge.com/pdf/symbolics/software/genera_8/Genera_Concepts.pdf)(pdf)
2. [Genera 用户指南](http://bitsavers.trailing-edge.com/pdf/symbolics/software/genera_8/Genera_User_s_Guide.pdf)(pdf)

除了这两本书，我强烈推荐这本书 [Lisp Lore: A Guide to Programming the Lisp Machine](https://archive.org/details/lisploreguidetop00brom)。


Installing & Running Symbolics Open Genera 2.0 Virtual Lisp Machine on Windows 8.1 with VirtualBox
https://www.youtube.com/watch?v=12USa3gU_oU



The days Lisp Machine dominated the world is far away from us. Lisp machine still be alive now adays though Symbolics' business runs out of their money.

I don't know much of LIsp right now, so does Lisp Machine, but I think it's wonderful, and someday I will digg into it. Here is the BT seed of **OpenGenera2.0, open version of one of the oldest Lisp Machine system**. Enjoy it! :-)

-------------------------------------------------------------------


Symbolics Opengenera怎么学习？ - LdBeth的回答 - 知乎 https://www.zhihu.com/question/68319818/answer/377448383

http://bitsavers.trailing-edge.com/pdf/symbolics/software/

https://github.com/ynniv/vagrant-opengenera 
在 Mac OS X 或现代 Linux 上运行 Open Genera 的便捷脚本






-----------------------------------

https://github.com/froggey/Mezzano Mezzano：用 Common Lisp 编写的操作系统 还提供了为 VirtualBox 构建它的说明 



Symbolics 提供了几种用于 Genera 的 [编程语言：](https://en.wikipedia.org/wiki/Programming_language)

- [ZetaLisp](https://en.wikipedia.org/wiki/ZetaLisp) , Lisp Machine Lisp 的符号版本
- [几个版本的 Common Lisp](https://en.wikipedia.org/wiki/Common_Lisp)： Symbolics Common Lisp、Future Common Lisp（ANSI Common Lisp）、CLtL1
- Symbolics Pascal，用 Lisp 编写的[Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language))版本（Lisp 源代码包含在 Genera 发行版中）
- Symbolics C，用 Lisp 编写的[C](https://en.wikipedia.org/wiki/C_(programming_language))版本（Lisp 源代码包含在 Genera 发行版中）
- Symbolics Fortran，用 Lisp 编写的[Fortran](https://en.wikipedia.org/wiki/Fortran)版本（Lisp 源代码包含在 Genera 发行版中）

Symbolics Common Lisp 为大部分 Common Lisp 标准提供了非常多的扩展，其中许多来自 ZetaLisp。



- Symbolics [Prolog](https://en.wikipedia.org/wiki/Prolog)，用 Lisp 编写和集成的 Prolog 版本
- Symbolics [Ada](https://en.wikipedia.org/wiki/Ada_(programming_language))，用 Lisp 编写的 Ada 版本

Symbolics 出售了几个在 Symbolics Genera 上运行的应用程序。

- Symbolics Concordia，文档制作套件
- Symbolics Joshua，一个[专家系统](https://en.wikipedia.org/wiki/Expert_system)外壳
- 符号[学 Macsyma](https://en.wikipedia.org/wiki/Macsyma) , 计算机代数系统
- Symbolics NS，芯片设计工具
- Symbolics Plexi，一种神经网络开发工具
- Symbolics S-Graphics，一套工具：S-Paint、S-Geometry、S-Dynamics、S-Render
- Symbolics S-Utilities：S-Record、S-Compositor、S-Colorize、S-Convert
- Symbolics Scope，使用 Pixar 图像计算机进行[数字图像处理](https://en.wikipedia.org/wiki/Digital_image_processing)
- Symbolics Statice，一个对象数据库

几家公司为 Symbolics Genera 开发和销售了应用程序。一些例子：

- 自动推理工具 (ART)，来自 Inference Corporation 的专家系统外壳
- [3d](https://en.wikipedia.org/wiki/ICAD_(software))参数化CAD系统
- 说明，图形编辑器
- [知识工程环境](https://en.wikipedia.org/wiki/Knowledge_Engineering_Environment)(KEE)，一个专家系统外壳，来自 IntelliCorp
- Knowledge Craft，一个专家系统外壳，来自 Carnegie Group
- 西门子的金属机器翻译系统

[可以在x86-64](https://en.wikipedia.org/wiki/X86-64)或[arm64 ](https://en.wikipedia.org/wiki/Arm64)[GNU/Linux](https://en.wikipedia.org/wiki/GNU/Linux)和[Apple M1 ](https://en.wikipedia.org/wiki/Apple_M1)[MacOS](https://en.wikipedia.org/wiki/MacOS)上运行的 Open Genera 稳定版本已经发布。[[5\]](https://en.wikipedia.org/wiki/Genera_(operating_system)#cite_note-5)

[存在可以在x86-64 ](https://en.wikipedia.org/wiki/X86-64)[GNU/Linux](https://en.wikipedia.org/wiki/GNU/Linux)上运行的 Open Genera 破解版

















-----------------------------------------------------------------------------

用 Haskell 编写的 House，这是另一种函数式（相对于命令式）编程语言：

http://programatica.cs.pdx.edu/House/

https://sites.google.com/site/haskell/house-operating-system



















# 后继者




MQTT erlang 映云科技 Iot物联网



--------------------------------------------------------------------------




你怎么看把Lisp作为开发语言的物联网平台？ - 林灿斌的回答 - 知乎
https://www.zhihu.com/question/26534503/answer/33188354

最近在indiegogo上出现了一款名为Zero Plus (Zero+)的物联网开发平台，https://www.indiegogo.com/projects/zero-plus-prototype-your-iot-product-in-seconds#/ 其独特之处就是使用Lisp作为其开发语言。
我问过一些玩开源硬件和智能家居的朋友，他们说用Lisp语言绝对是最大的败笔 :(
不过看看其在indiegogo上的介绍，感觉还不错，有几个比较有意思的特点：
1. Zero+使用的编程语言是Lisp，这种在人工智能领域常用的编程语言，和人类语言比较相似，可以自定义编程语法，形成属于你自己的个性化编程语言。
2. Web IDE提供调试打印，设置断点，单步执行，查看代码段，查看数据变量等调试功能。
3. 免编译，免烧录，免重启。在终端和云端都运行着由SmartMatrix团队开发的Lisp解释器，在Web IDE里你可以定义云端和硬件终端的执行逻辑。特别值得注意的是，这里提到了定义云端执行逻辑，说明该平台使用了云端的计算能力，并不像常见的平台只提供存储和推送功能。
4. 把Zero+连接入网络，在世界上任何可以联网的地方，打开Web IDE就可以对Zero+进行编程和调试。
我试着玩了一下Lisp的方言Racket,感觉Lisp还是很强大的。

似乎凉了，github 没动静


------------------------------------------------------------------------

## Schemachine
「Schemachine」有希望成为Lisp Machine的后继者，实现OS PL和硬件的大一统吗？ - LdBeth的回答 - 知乎

没戏了 https://www.zhihu.com/question/283383877/answer/430877209


A prototype computer implemented in the project area of a Logic Engine.
Consists of a processor, storage manager, and a dual ported memory organized
to implement a data heap.

All components except the system bus were derived using the DDD transformation
system.

The test system is a codesign environment in which the hardware can be
tested against its own executable specification

https://web.archive.org/web/20030508100532/http://www.cs.indiana.edu/ftp/techreports/TR544.html

https://web.archive.org/web/20030317130643/http://www.cs.indiana.edu/ftp/techreports/TR413.html





scheme 标准


https://small.r7rs.org/


https://www.gnu.org/software/mit-scheme/documentation/stable/mit-scheme-ref/R7RS.html



























# lisp interpreter实现lisp

Sectorlisp 是一个 512 字节的 LISP 实现，能够在裸机上引导 John McCarthy 的元循环评估器。

https://github.com/jart/sectorlisp








----------------------------



用cpp
https://github.com/klmr/lisp.cpp

用模板
GitHub - zick/TempLisp: LISP implementation in C++ templates
https://github.com/zick/TempLisp

用c实现
GitHub - brenns10/lisp: An old lisp implementation of mine ...
https://github.com/brenns10/lisp



SBCL. Steel Bank Common Lisp (SBCL) is a high performance Common Lisp compiler. It is open source / free software, with a permissive license.
Clozure CL. Clozure CL (often called CCL for short) is a free Common Lisp implementation with a long history. ...
ABCL. Armed Bear Common Lisp (ABCL) is a full implementation of the Common Lisp language featuring both an interpreter and a compiler, running in the JVM.
Clasp. Clasp is a new Common Lisp implementation that seamlessly interoperates with C++ libraries and programs using LLVM for compilation to native code
https://www.cliki.net/Common+Lisp+implementation

GitHub - nogw/ocaml-scheme: A lisp implementation in OCaml
https://github.com/nogw/ocaml-scheme


haskell
GitHub - naver/lispe: An implementation of a full fledged ...
https://github.com/naver/lispe






# 

----------------------------------------













































































