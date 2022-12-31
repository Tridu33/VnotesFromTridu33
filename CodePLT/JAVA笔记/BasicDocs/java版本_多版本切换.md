# java版本

多版本切换

```
$ sudo update-alternatives --config java

There are 2 choices for the alternative java (providing /usr/bin/java).
Processing triggers for hicolor-icon-theme (0.17-2) ...
  Selection    Path                                            Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      manual mode
  2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode

Press <enter> to keep the current choice[*], or type selection number: 0

```

cloud.tencent.com/developer/article/1162527

```
$ sudo update-alternatives --config java


There are 2 choices for the alternative java (providing /usr/bin/java).
Processing triggers for hicolor-icon-theme (0.17-2) ...
  Selection    Path                                            Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      manual mode
  2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode

Press <enter> to keep the current choice[*], or type selection number: 0
tridu33@Tridu:/home/windesktop/hush/myND/myND/src$ sudo update-alternatives --config javac
There are 3 choices for the alternative javac (providing /usr/bin/javac).

  Selection    Path                                          Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-11-openjdk-amd64/bin/javac   1111      auto mode
  1            /usr/bin/ecj                                   143       manual mode
  2            /usr/lib/jvm/java-11-openjdk-amd64/bin/javac   1111      manual mode
  3            /usr/lib/jvm/java-8-openjdk-amd64/bin/javac    1081      manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

指此命令可以运行其它命令包括，但不限于：`keytool`，`javadoc`和`jarsigner`



```
sudo nano /etc/environment
```



```
 sudo update-alternatives --config java
```

查看安装位置

在此文件的末尾，添加以下行，确保使用您自己复制的路径替换突出显示的路径
比如：

```
JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin/java"
```

```
 source /etc/environment
```


其他用户需要执行命令source /etc/environment或注销并重新登录才能应用此设置。


```
 echo $JAVA_HOME
```


## 1.6
```
sudo nano /etc/environmentPATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/$
CLASSPATH="/usr/lib/java/jdk1.6.0_45/lib:/usr/lib/java/jdk1.6.0_45/jre/lib"
```
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





































