# windows的java多版本切换






C:\ProgramData\Oracle\Java\javapath备份在这儿



注意事项
一定要删除在用户变量中的‘C:\ProgramData\Oracle\Java\javapath;’
一定要删除system32中的三个带有Java的exe文件
在修改JAVA_HOME的变量值后要一路确定到底，然后退出当前的cmd命令窗口环境变量才会生效
问题背景
公司项目中应用到的jdk环境为1.6，最近在家学习IntelliJ IDEA中sdk多环境配置时，想安装Jdk1.8,作为学习基础。那么问题来了，公司项目扩展不支持jdk1.8，为了既能满足公司项目开发环境，又能满足学习jdk1.8的需要，当然不能每一次都进行jdk的安装和卸载，需要探索另一种新方法。

分析问题
为了多快好省的解决当前的问题，我的想法是在windows中同时安装jdk1.6和jdk1.8，在中间进行切换，而不需要多次进行重复的安装和卸载，这样简单方便。

解决思路
第一步：在安装之前，本机的jdk环境为jdk1.6，执行: java -version ，显示当前jdk版本为1.6

 

第二步：安装jdk1.8，让两个jdk共存。 安装教程是：直接 下一步 and 下一步 安装完成后，对jdk环境变量进行如下设置:

JAVA8_HOME =jdk1.8的安装路径

JAVA6_HOME =jdk1.6的安装路径 
JAVA_HOME = %JAVA6_HOME% (注意:如果你想切换jdk，就在此处设置即可)

 

 

第三步：添加 %JAVA_HOME%\bin 到环境变量Path中，添加后的Path如下图所示：

 

环境变量配置后，但是安装以后出现以下问题：

通过 java -version 查看显示，jdk显示为：jdk1.8

分析： 

当前jdk版本为1.8,这不科学，因为环境变量中配置的JAVA_HOME是1.6的路径，查看版本应该要是1.6的才对，现在变成1.8，jdk的环境变量未被改变，通过查询后发现问题：

在安装JDK1.8时（本机先安装jdk1.6再安装的jdk1.8），自动将java.exe、javaw.exe、javaws.exe三个可执行文件复制到了C:\Windows\System32目录，由于这个目录在WINDOWS环境变量中的优先级高于JAVA_HOME设置的环境变量优先级。  
解决方案：

删除C:\Windows\System32目录下的java.exe,删除即可。
注意： 如果Path中有 C:\ProgramData\Oracle\Java\javapath; ，删除之。否则会引变量错误。

第四步：以上配置完成后，开启新 cmd 窗口，查看jdk版本显示正常，在环境变量中切换JAVA_HOME的值为： JAVA_HOME=%JAVA8_HOME% ，查看jdk版本，成功切换。如图所示：

blog.csdn.net/qq_40435659/article/details/82184664

























