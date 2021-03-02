**grep -rn**




https://www.zhihu.com/question/29855417 搜索一个文件夹里面所有txt文件的某个关键字，有什么方法或软件？












＃这是主要的Apache服务器配置文件。它包含
#configuration指令，为服务器提供指令。
＃有关详细信息，请参阅http://httpd.apache.org/docs/2.4/
关于Debian的指令和/usr/share/doc/apache2/README.Debian
#hints。
＃
＃
#Android 2配置在Debian中的工作原理摘要：
#Debian中的Apache 2 Web服务器配置与以下内容完全不同
#streaming建议的配置Web服务器的方法。这是因为Debian的default Apache2安装尝试添加和删除模块，
#Virtual hosts，以及尽可能灵活的额外配置指令
#demand使自动化更改和管理服务器一样简单

＃它被分成几个文件，形成概述的配置层次结构
＃下面，全部位于/ etc / apache2 /目录中：
＃
＃在/ etc / apache2的/
＃|  -  apache2.conf
＃| ` -  ports.conf
＃|  -  mods-enabled
＃| |  -  * .load
＃| ` -  * .conf
＃|  -  conf-enabled
＃| ` -  * .conf
＃` - 已启用网站
＃` -  * .conf
＃
＃
＃* apache2.conf是主配置文件（此文件）。它启动网络服务器时把碎片通过在启动时包含所有剩余的配置文件来＃
＃* ports.conf始终包含在主配置文件中。它是确定传入连接随时定制的侦听端口
＃* mods-enabled /，conf-enabled /和sites-enabled /中的配置文件目录分别包含管理模块的特定配置片段，全局配置片段或虚拟主机配置
＃它们通过符号链接来自它们的可用配置文件来激活
#always * -available /对应。这些应该通过使用我们的管理
#helper a2enmod / a2dismod，a2ensite / a2dissite和a2enconf / a2disconf。看到
＃他们各自的手册页以获取详细信息。
＃
＃*二进制文件名为apache2。由于使用环境变量，在
＃默认配置，apache2需要启动/停止
＃/ etc / init.d / apache2或apache2ctl。直接调用/ usr / bin / apache2不会
＃使用默认配置。


＃全局配置
＃

＃
#ServerRoot：服务器所在目录树的顶部
保留＃配置，错误和日志文件。
＃
＃ 注意！如果您打算将其放在NFS（或其他网络）上
#mount filesystem然后请阅读Mutex文档（可用
＃at <URL：http：//httpd.apache.org/docs/2.4/mod/core.html#mutex>）;
＃你会省去很多麻烦。
＃
＃不要在目录路径的末尾添加斜杠。
＃
#ServerRoot“/ etc / apache2”

＃
＃接受序列化锁定文件必须存储在本地磁盘上。
＃
#Mutex文件：$ {APACHE_LOCK_DIR}默认

＃
＃将存储shm和其他运行时文件的目录。
＃

DefaultRuntimeDir $ {APACHE_RUN_DIR}

＃
#PidFile：服务器应记录其进程的文件
＃启动时的标识号。
＃需要在/ etc / apache2 / envvars中设置
＃
PidFile $ {APACHE_PID_FILE}

＃
#Timeout：接收和发送超时之前的秒数。
＃
超时300

＃
＃KeepAlive：是否允许持久连接（超过
＃每个连接一个请求）。设置为“关闭”以取消激活。
＃
KeepAlive On

＃
#MaxKeepAliveRequests：允许的最大请求数
＃持久连接期间。设置为0以允许无限量。
＃我们建议您保留此号码，以获得最佳性能。
＃
MaxKeepAliveRequests 100

＃
＃KeepAliveTimeout：等待来自的下一个请求的秒数
＃同一连接上的同一客户端。
＃
KeepAliveTimeout 5


＃需要在/ etc / apache2 / envvars中设置
用户$ {APACHE_RUN_USER}
组$ {APACHE_RUN_GROUP}

＃
#HostnameLookups：记录客户端的名称或仅记录其IP地址
＃例如，www.apache.org（on）或204.62.129.132（off）。
＃默认是关闭的，因为如果人们对网络整体更好
＃必须故意启用此功能，因为启用它意味着
＃每个客户端请求将导致至少一个查找请求
#nameserver。
＃
HostnameLookups Off

#ErrorLog：错误日志文件的位置。
＃如果未在<VirtualHost>中指定ErrorLog指令
＃container，与该虚拟主机相关的错误消息将是
#log here here。如果你*为* <VirtualHost>定义错误日志文件
＃container，该主机的错误将记录在那里，而不是在这里。
＃
ErrorLog $ {APACHE_LOG_DIR} /error.log

＃
#LogLevel：控制记录到error_log的消息的严重性。
＃可用值：trace8，...，trace1，debug，info，notice，warn，
#error，crit，alert，emerg。
＃也可以为特定模块配置日志级别，例如
＃“LogLevel info ssl：warn”
＃
LogLevel警告

#include模块配置：
IncludeOptional mods-enabled / * .load
IncludeOptional mods-enabled / * .conf

＃包括列表
#Zhè shì zhǔyào de Apache fúwùqì pèizhì wénjiàn. Tā bāohán
#configuration zhǐlìng, wèi fúwùqì tígōng zhǐlìng.
#Yǒuguān xiángxì xìnxī, qǐng cānyuè http://Httpd.Apache.Org/docs/2.4/
Guānyú Debian de zhǐlìng hé/usr/share/doc/apache2/README.Debian