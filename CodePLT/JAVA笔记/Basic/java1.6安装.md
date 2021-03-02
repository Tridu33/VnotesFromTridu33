# java1.6安装

１、下载JDK1.6,你可以到官网去下载，下载时请看清自己的系统版本，记得一定要下载相应的版本。

　　http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-javase6-419409.html#jdk-6u41-oth-JPR

２、将下载的文件放置到/usr/lib/java目录下(需要手动创建java目录)，并修改文件的可执行权限，如chmod 777 jdk-6u41-linux-x64.bin

３、安装文件，sudo ./jdk-6u41-linux-x64.bin

４、安装完毕后，则需配置系统环境   sudo vi /etc/environment，或配置用户环境变量vi /home/username/.bashrc，建立JAVAHOME,　CLASSPATH,　修改PATH变量

　　如我的设置为：

　　JAVAHOME=/usr/lib/java/jdk1.6.0_41  
　　PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/lib/java/jdk1.6.0\_41/bin:/usr/lib/java/jdk1.6.0\_41/jre/bin"  
　　CLASSPATH=/usr/lib/java/jdk1.6.0\_41/lib:/usr/lib/java/jdk1.6.0\_41/jre/lib

５、执行命令，使配置生效。source /etc/environment　( source /home/username/.bashrc )

６、验证是否安装完毕，使用java -version或者直接使用javac，看其生效与否。

７、如果还未生效，很有可能由于ubuntu中已有默认的jdk，如openjdk，所以，为了使默认使用的是我们安装的jdk，还要进行如下工作。  
　　sudo update-alternatives --install /usr/bin/java java /usr/lib/java/jdk1.6.0_41/bin/java 300  
　　sudo update-alternatives --install /usr/bin/javac javac /usr/lib/java/jdk1.6.0_41/bin/javac 300  
　　通过这一步将我们安装的jdk加入java选单。  
　　然后执行：  
　　update-alternatives --config java




















