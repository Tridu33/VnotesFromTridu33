










值得收藏！史上最全Windows安全工具锦集 - 黑客Anony的文章 - 知乎
https://zhuanlan.zhihu.com/p/349691243



EXEInfoPE

PE侦壳工具，PEiD的加强版，可以查看EXE/DLL文件编译器信息、是否加壳、入口点地址、输出表/输入表等等PE信息：


PEiD
一款著名的PE侦壳工具，可以检测PE常见的一些壳，但是目前已经无法从官网获得：

StudyPE
PE32 & PE64 查看分析集成工具，具有强大的PE结构处理分析功能，在查询方面功能略显薄弱：


调试/反编译工具篇
OllyDbg
Ring3级调试器，支持插件扩展功能，唯一不足的是OD是一个32位调试器，不支持调试64位程序。官方给出的原版程序是无插件的，有需要的童鞋可以在吾爱破解论坛自行搜索：


WinDbg
支持Windows平台，用户态和内核态的调试器，有图形界面和命令行两种调试方式。其强大的内核调试功能收获了众多的追捧者：

x32dbg/x64dbg
一款开源的调试器，从界面和操作使用和OD相似，支持32位和64位应用程序的调试。解决了OD对64位应用程序调试上的缺陷：



dnSpy
一款针对.NET程序的开源逆向程序的工具。包含了反汇编器，调试器和汇编编辑器等功能组件，支持插件功能：





**IDAPro**

全称：InteractiveDisassembler Professional，交互式反汇编器专业版，目前最棒的静态反编译工具，是众多安全人士的首选：



VB Decompiler
针对Visual Basic 5.0/6.0开发的程序的反编译器：


应急工具篇
日志相关

Sysmon
WindowsSysinternals出品的一款Sysinternals系列中的工具。它以系统服务和设备驱动程序的方法安装在系统上，并保持常驻性。用来监视和记录系统活动，并记录到windows事件日志，可以提供有关进程创建，网络链接和文件创建时间更改的详细信息：

LastActivityView
是一款电脑操作记录查看器，直接调用系统日志，显示安装软件、系统启动、关机、网络连接、执行exe 的发生时间和路径：


Regshot
注册表比较工具，通过抓取两次注册表快速比较得出两次注册表的不同之处



Autoruns
基于Windows平台的自动运行程序的管理工具。可以控制登录时的加载程序、驱动程序加载、服务启动、任务计划等 Windows 中各种方面的启动项




进程相关

ProcessHacker
一款功能丰富的开源系统进程辅助工具，可以方便的查看进程的运行情况、内存以及模块信息，还可以对进程进行管理：


PowerTool
一款免费的进程管理器，可以Unlock占用文件的进程，查看文件或文件夹被占用的情况，内核模块和驱动的查看管理，进程模块的内存dump等工具


ProcessLasso
一款独特的调试进程级别的系统优化工具，主要功能是基于其特别的算法动态调整各个进程优先级以实现为系统减负的目的。可以用来监视进程动作：

文件相关

HashTab
文件校验工具，分为免费个人版以及付费版。下载安装后可以通过查看文件属性中的HashTab快速得到文件的哈希值，支持多种哈希算法

HashChecker
一款开源的文件校验工具，安装完成后可以通过文件属性中的文件校验快速得到文件的哈希值。支持右键菜单创建校验文件功能和批量校验功能

Unlocker
一款右键扩充工具，通过删除文件和程序关联的方式解除文件的占用。在解除占用时不会强制关闭占用文件进程




Everything
强大的Windows桌面搜索引擎，可以在NTFS卷上快速地根据名称查找文件和目录




Winhex
是一款优秀的十六进制编辑器，在计算机取证，数据恢复，低级数据处理和IT安全领域非常有用：


BinDiff
一款开源的二进制文件对比工具，可帮助安全人员快速发现反汇编代码中的差异和相似之处。支持x86、MIPS、ARM/AArch64、PowerPC等架构进行二进制文件的对比：


BeyondCompare
一款由ScooterSoftware推出的文件比较工具。主要用于比较两个文件夹或者文件并将差异以颜色标记，比较的范围包括目录，文档内容等：

SfAntiBotPro
内存检索工具，可以根据输入的字符串快速检索计算机内存，输出包含该字符串的进程信息，在进行恶意域名检测时有事半功倍的效果

DumpIt
是一款免安装的Windows内存镜像取证工具，可以使用其轻松地将一个系统的完整内存镜像下来，并用于后续的调查取证工作


设备监控

USBLogView
一款USB设备监控软件，后台运行，可以记录插入或拔出系统的任何USB的详情信息：






集成工具

PC Hunter
一款驱动级的系统维护工具，能够查看各种Windows的各类底层系统信息，包括进程、驱动模块、内核、内核钩子、应用层钩子，网络、注册表、文件、启动项、系统杂项、电脑体检等：



MalwareDefender
一款 HIPS (主机入侵防御系统)软件，用户可以自己编写规则来防范病毒、木马的侵害。另外，MalwareDefender提供了很多有效的工具来检测和删除已经安装在您的计算机系统中的恶意软件：



火绒剑
一款用于分析、处理恶意程序的安全工具软件，提供了“程序行为监控”、“进程管理”、“文件管理”、“注册表管理”、“系统启动项管理”、”内核程序管理“、“代码钩子扫描”七大功能：





流量分析工具篇
WireShark
一款网络封包分析工具，可以帮助用户深入分析网络协议，涵盖上百种协议以及各类主要平台。通过GUI或TTY-mode浏览数据：


Fiddler
C#编写的http抓包改包工具，相较wireshark更加轻量级，在http和https数据包的抓取上更加专业。还能设置断点，修改请求和响应的数据，模拟弱网络环境。支持插件扩展:

MicrosoftNetwork Monitor
只支持Windows平台的网络数据分析工具，提供了一个专业的网路实时流量图形界面，拥有识别和监控超过300种网络协议的能力：

下载地址：https://www.microsoft.com/en-us/download/details.aspx?id=4865

CapsaPacket Sniffer
网络分析工具，用于网络监控、故障排除和网络诊断等功能：


NetworkMiner
支持Windows平台的网络取证分析工具，通过嗅探或者分析PCAP文件可以侦测到操作系统，主机名和开放的网络端口主机









AngryIP Scanner
这是一款开源的网络扫描仪，支持Linux，Windows和Mac OS X平台，可以在最短的时间内扫描远端主机IP运作情况，包括主机名，目前开放的端口和IP的运作情况：









WebShell查杀工具篇
D盾
D盾是一个专为IIS设计的主动防御保护软件，有一句话免疫，主动后门拦截，SESSION保护，防WEB嗅探，防CC，防篡改，注入防御，防XSS，防提权，上传防御，未知0day防御，异形脚本防御等功能，以内外保护的方式防止网站和服务器被入侵。

WebShellKiller
WebShellKiller是个Web后门专杀工具，不仅支持Webshell扫描，还支持暗链扫描。该工具将传统的技术与人工智能技术相结合、静态扫描和动态分析相结合，更精准地检测出Web网站已知和未知的后门文件：


WEBDIR+
在线WebShell扫描器：


WebShellDetector
在线WebShell扫描器


WEBSHELL.PUB
在线WebShell扫描器



























# 1. DLL逆向工具集




[TOC]




https://github.com/weixinbao/ReverseTool






# 2. ReverseTool
逆向工具集合
- [Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking)

## 2.1. Java & Jar (Android)

- [jd-gui](http://jd.benow.ca/)    jar包浏览工具,对应的IDE插件，JD-Eclipse/JD-IntelliJ 

- [Luyten](https://github.com/deathmarine/Luyten) An Open Source Java Decompiler Gui for Procyon

- [jadx-gui](https://github.com/skylot/jadx) 直接反编译apk

- [Apktool](https://ibotpeaches.github.io/Apktool/) apk的反编译,编译工具(smali格式) 

- [dex2jar](https://github.com/pxb1988/dex2jar) dex转为jar工具

- [AXMLPrinter](https://www.nuget.org/packages/axmlprinter)  XML浏览工具

- [androguard](https://github.com/androguard/androguard) 使用DAD作为反编译器，可以分析恶意软件的可视化软件

- [Enjarify](https://github.com/google/enjarify) Google官方逆向分析工具(Dalvik字节码 -> Java),需python环境

- [ClassyShark](https://github.com/google/android-classyshark) Google官方dex/apk/jar/class/aar浏览工具

- APK Analyzer(AndroidStudio 2.2+) Google官方APK分析工具, [making-the-most-of-the-apk-analyzer](https://medium.com/google-developers/making-the-most-of-the-apk-analyzer-c066cb871ea2) 

- [Smali/baksmali](https://github.com/JesusFreke/smali/wiki/smalidea) APK文件编辑工具

- [Smali2Java](http://www.hensence.com/cn/smali2java) APK图形化浏览工具

- [CodeInspect](https://blogs.uni-paderborn.de/sse/tools/codeinspect/) 

- [bytecodeviewer](https://bytecodeviewer.com/)

- [APKIDE](http://www.xiaomiren.net/ ) 国人开发综合图形化工具

- [bytecode-viewer](https://bytecodeviewer.com/) 集成了J-RET,JHexPane, Dex2Jar等多个反编译工具

- [JEB](https://www.pnfsoftware.com/) 商业反编译软件,支持动态编辑

- [RADARE2](https://github.com/radare/radare2)  可以反汇编、调试、分析和操作二进制文件
		
- [Simplify](https://github.com/CalebFenton/simplify)  反混淆工具
		
- [JAD](https://varaneckas.com/jad/)  Java反编译工具
		
- [Introspy](https://github.com/iSECPartners/Introspy-iOS)  黑盒测试工具

- [ApkStudio](https://github.com/vaibhavpandeyvpz/apkstudio)  跨平台逆向IDE

- [APK DeGuard](http://apk-deguard.com/) 在线Android反编译工具

> Hook Tools

- [Xposed Framework](http://repo.xposed.info/)   运行时修改系统或应用程序方面和行为
	
- [Cydia Substrate](http://www.cydiasubstrate.com/)  注入
	
- [ADBI](https://github.com/samsung/adbi) & [DDI](https://github.com/crmulliner/ddi) 动态跟踪工具
			
- [Frida](https://github.com/crmulliner/ddi) & [Diff-GUI](https://github.com/antojoseph/diff-gui) JavaScript 注入 

> Android 漏洞查询

- [Android Vulnerabilties](http://androidvulnerabilities.org/)

- [Android CVE Details](http://www.cvedetails.com/vulnerability-list/vendor_id-1224/product_id-19997/Google-Android.html)

## 2.2. C++ & So (Android)

- [IDAPro](https://www.hex-rays.com/products/ida/index.shtml)  最强大的静态逆向分析工具,没有之一   [IDA Pro 6.8 + All Decompilers Full Leak](http://www.52pojie.cn/forum.php?mod=viewthread&tid=442702&extra=page%3D1%26filter%3Dtypeid%26typeid%3D123)


## 2.3. C# & Dll & EXE

- [ILSpy](http://ilspy.net/)(免费) 直接使用,dll查看工具

- [.Net Reflector](http://www.red-gate.com/products/dotnet-development/reflector/) & Reflexil RedGate开发的.Net逆向工具(反编译查看)[加上Reflexil插件](https://github.com/sailro/reflexil)(开源)用于编辑,修改/注入

- [Dependency Walker](http://www.dependencywalker.com/)

- [dotPeek](https://www.jetbrains.com/decompiler/)

- [De4Dot(开源) 脱壳/反混淆工具](https://github.com/0xd4d/de4dot)   
使用: de4dot.exe xx.dll -p un

- [DILE Dotnet IL Editor](https://sourceforge.net/projects/dile/) 调试工具

- ilasm & ildasm(微软官方) 把IL文件重新生成DLL的功能,[使用参考](http://www.cnblogs.com/dudu/archive/2011/05/17/ildasm_ilasm_il.html) 

- [Just Decompile](http://www.telerik.com/products/decompiler.aspx)  反编译工具

- [Dotfuscator](https://www.preemptive.com/products/dotfuscator/overview), Visual Studio自带 混淆工具, 目录为"**\Microsoft Visual Studio 14.0\PreEmptive Solutions\Dotfuscator and Analytics CommunityEdition\dotfuscator.exe "

- [Codeguard](https://www.codeguard.com/) 混淆工具

- [Reactor]( https://projectreactor.io/) 混淆工具

- [xeoncode](https://turbo.net/studio) 混淆工具 [破解版](http://download.csdn.net/detail/sndntdkj/6521975)(64位不可用)

- [ConfuserEx]( https://yck1509.github.io/ConfuserEx/  )(开源)混淆工具, [下载地址](https://github.com/yck1509/ConfuserEx/releases) 

- [OllyDbg](http://www.ollydbg.de/)


## 2.4. iOS

- [IDA Pro](https://www.hex-rays.com/products/ida/index.shtml)  反汇编工具 (Windows,Linux, Mac OS X) & [Hopper](https://www.hopperapp.com/) (Mac OS X)

- [Reveal](https://revealapp.com/) & [PonyDebugger](https://github.com/square/PonyDebugger)   UI分析利器

- [iFunbox](http://www.i-funbox.com/zh-cn_index.html) & [iExplorer](https://iexplorer.en.softonic.com/) & [iTools](http://www.itools.cn/) 文件查看工具

- [Charles](https://www.charlesproxy.com/) 网络分析工具

- [Cycript](http://www.cycript.org/) 调试器

- [LLDB](https://lldb.llvm.org/)

- [snoop-it](https://code.google.com/archive/p/snoop-it/) 查看类信息，调试调用类的方法

- [introspy](https://github.com/iSECPartners/Introspy-iOS)

- [class-dump](http://stevenygard.com/projects/class-dump/) 

> Hook Tools

- [Theos](http://iphonedevwiki.net/index.php/Theos/Setup) 越狱程序开发框架

- [iOSOpenDev](http://www.iosopendev.com/)


## 2.5. Others

- [Frida](https://www.frida.re/) 动态二进制插桩(Dynamic Binary Instrumentation)框架, [使用Frida来hack安卓APP（一）](http://bbs.pediy.com/thread-216645.htm)

## 2.6. 实用参考   

- [权威论坛-看雪](http://www.kanxue.com/)

- [看雪iOS安全小组 置顶向导集合贴](http://bbs.pediy.com/thread-212685.htm)

- [Android安全中文站](http://www.droidsec.cn/)

- [<<iOS应用逆向工程>> 论坛](http://bbs.iosre.com/)

- [iOS 安全 Wiki](https://www.gitbook.com/book/wizardforcel/ios-sec-wiki/details)

- [关于 .Net 逆向的那些工具：反编译篇 ](http://www.aneasystone.com/archives/2015/06/net-reverse-decompiling.html)  

- [破解NET的四大神器](http://www.52pojie.cn/thread-174802-1-1.html )    

- [破解Java to C# Converter](http://wzmlj.com/yiyan127/p/CSharp_CrackJava2CSharpConverter.html)   



















