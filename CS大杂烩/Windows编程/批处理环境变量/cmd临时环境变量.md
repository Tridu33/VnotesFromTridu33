# cmd临时环境变量



## new name 


1、找到项目所在目录,   //cd D:   ;

2、切换目录： cd  IdeaProject ，cd code(项目根目录);

3、使用echo ”%JAVA_HOME%“查看默认Java环境变量配置；

4、set JAVA_HOME=C:\Program Files\Java\jdk1.8.0_171；--配置临时Java环境变量；

5、set PATH=%JAVA_HOME%\bin;%PATH%   ；--配置环境变量到path；

6、set MVN_HOME=D:\soft\maven\apache-maven-3.3.9  ；--配置maven临时环境变量；

7、set PATH=%MVN_HOME%\bin;%PATH%   ；--配置maven临时环境变量到path；

8、可通过 mvn -version ； Java -version 查看临时环境变量；

9、可以通过  title   XXX  个性化设置CMD窗口名称，加以区分；

10、使用 mvn clean compile 编译项目；

11、使用 mvn package 打包项目。






## path


1、

以 path 为例：

1.1、查看：

　　set path

1.2、添加：

　　set path=%path%;"要添加的路径"

 

 

 

 

附录：下面贴上一些常用的环境变量及作用

%ALLUSERSPROFILE% 局部 返回所有“用户配置文件”的位置。

%APPDATA% 局部 返回默认情况下应用程序存储数据的位置。

%CD% 局部 返回当前目录字符串。

%CMDCMDLINE% 局部 返回用来启动当前的 Cmd.exe 的准确命令行。

%CMDEXTVERSION% 系统 返回当前的“命令处理程序扩展”的版本号。

%COMPUTERNAME% 系统 返回计算机的名称。

%COMSPEC% 系统 返回命令行解释器可执行程序的准确路径。

%DATE% 系统 返回当前日期。使用与 date /t 命令相同的格式。由 Cmd.exe 生成。有关 date 命令的详细信息，请参阅 Date。

%ERRORLEVEL% 系统 返回最近使用过的命令的错误代码。通常用非零值表示错误。

%HOMEDRIVE% 系统 返回连接到用户主目录的本地工作站驱动器号。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。

%HOMEPATH% 系统 返回用户主目录的完整路径。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。

%HOMESHARE% 系统 返回用户的共享主目录的网络路径。基于主目录值的设置。用户主目录是在“本地用户和组”中指定的。

%LOGONSEVER% 局部 返回验证当前登录会话的域控制器的名称。

%NUMBER_OF_PROCESSORS% 系统 指定安装在计算机上的处理器的数目。

%OS% 系统 返回操作系统的名称。Windows 2000 将操作系统显示为 Windows_NT。

%PATH% 系统 指定可执行文件的搜索路径。

%PATHEXT% 系统 返回操作系统认为可执行的文件扩展名的列表。

%PROCESSOR_ARCHITECTURE% 系统 返回处理器的芯片体系结构。值: x86，IA64。

%PROCESSOR_IDENTFIER% 系统 返回处理器说明。

%PROCESSOR_LEVEL% 系统 返回计算机上安装的处理器的型号。

%PROCESSOR_REVISION% 系统 返回处理器修订号的系统变量。

%PROMPT% 局部 返回当前解释程序的命令提示符设置。由 Cmd.exe 生成。

%RANDOM% 系统 返回 0 到 32767 之间的任意十进制数字。由 Cmd.exe 生成。

%SYSTEMDRIVE% 系统 返回包含 Windows XP 根目录（即系统根目录）的驱动器。

%SYSTEMROOT% 系统 返回 Windows XP 根目录的位置。

%TEMP% and %TMP% 系统和用户 返回对当前登录用户可用的应用程序所使用的默认临时目录。有些应用程序需要 TEMP，而其它应用程序则需要 TMP。

%TIME% 系统 返回当前时间。使用与 time /t 命令相同的格式。由 Cmd.exe 生成。有关 time 命令的详细信息，请参阅 Time。

%USERDOMAIN% 局部 返回包含用户帐户的域的名称。

%USERNAME% 局部 返回当前登录的用户的名称。

%UserProfile% 局部 返回当前用户的配置文件的位置。

%WINDIR% 系统 返回操作系统目录的位置。

 

























