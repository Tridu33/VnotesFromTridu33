











# 1. 查看exe源代码软件



windows上可以做反编译的工具一般有几种，动态调试的话会用x64dbg （x64dbg开源动态调试工具） ，静态分析最牛逼的工具是IDA，这个软件收费很高，但是目前来说最强大，可以分析各种平台上的可执行文件，IDA有个著名的F5插件，是可以把汇编转成c语言，有符号的情况下效果会更佳（当然不可能跟源码保持一致），但是帮助理解代码逻辑效果会很方便。

另外一个美国NSA开源的工具叫做Ghidra，这个工具是java编写，支持跨平台运行，效果跟ida类似，可以做为另一个替代的选择。


.net的反编译我推荐ilspy






.net制作的exe可以用reflector（不过现在似乎有新款软件，我只用过老的）；

python用记事本什么操作，这个我倒是没看懂，如果是用PyInstaller打包的，可以还用PyInstaller还原，不过这个需要另外安装Python解释器，并且版本要相同（emmm这个难度可能有点大了），不过好在网上已经有在线解包链接了；

另外还有java用jd-gui没话说（曾经用这个解开了Minecraft源码，当然一般的软件都会加代码混淆，看起来会很不爽）； https://github.com/java-decompiler/jd-gui  a standalone graphical utility that displays Java sources from CLASS files.










如果宁是大触，直接刚汇编也是可以的，解汇编的软件也很多，似乎大体上就是调试功能的区别，如果只是想要其中的代码就用里面的导出功能即可（这个大多数软件都有）。



