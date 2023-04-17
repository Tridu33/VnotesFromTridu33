[TOC]

很明白的教程 https://huminxi.netlify.app/2018/12/18/%E6%80%8E%E4%B9%88%E5%9C%A8%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%BC%96%E8%AF%91%E5%92%8C%E6%89%A7%E8%A1%8C%20java%20%E7%A8%8B%E5%BA%8F/









常见的java项目中


bin 开始是一个空目录，用来保存编译生成的 .class 文件。

lib 包含项目引用到的第三方 jar 包。

src 项目源码。



```
javac -d bin -encoding utf-8 -cp lib/lombok.jar src/com/user/*.java src/com/application/Main.java
```



-d 指定编译后的 .class 文件所存放的目录。这里指定为 bin 目录。
-cp 指定编译时用户的 classpath，会覆盖用户之前在环境变量 CLASSPATH 中配置的路径。如果既没有指定 classpath，也没有配置 CLASSPATH，则默认为当前目录。这里指定为存放 jar 包的 lib 目录。
src/com/user/*.java src/com/application/Main.java 指定待编译的源码目录。


https://docs.oracle.com/javase/1.5.0/docs/tooldocs/windows/javac.html





运行 Java 程序需要用到 java 命令。而且指定的类或 jar 包需要包含如下所示的 Main 方法。

https://docs.oracle.com/javase/1.5.0/docs/tooldocs/windows/java.html


```java
java -cp bin com.application.Main
```













# 1. 命令行执行javac-java大项目多文件

javac


```bash
-classpath，设定要搜索类的路径，可以是目录，jar文件，zip文件（里面都是class文件），会覆盖掉所有在CLASSPATH里面的设定。
-sourcepath， 设定要搜索编译所需java 文件的路径，可以是目录，jar文件，zip文件（里面都是java文件）。
```

所以一个完整的javac命令行应该是这样的，
假设abc.java在路径c:\src里面，在任何的目录的都可以执行以下命令来编译。
```bash
javac -classpath c:\classes;c:\jar\abc.jar;c:\zip\abc.zip -sourcepath c:\source\project1\src;c:\source\project2 \lib\src.jar;c:\source\project3\lib\src.zip c:\src\abc.java
```
表示编译需要c:\classed下面的class文件，c:\jar\abc.jar里面的class文件，c:\zip\abc.zip里面的class文件
还需要c:\source\project1\src下面的源文件，c:\source\project2 \lib\src.jar里面的源文件，c:\source\project3\lib\src.zip里面的源文件，
注意：jar，zip里面的源文件不会有什么改动，目录下的源文件，有可能会被重新编译。


java

-classpath， 设定要搜索的类的路径，可以是目录，jar文件，zip文件（里面都是class文件），会覆盖掉所有的CLASSPATH的设定。
由于所要执行的类也是要搜索的类的一部分，所以一定要把这个类的路径也放到-classpath的设置里面。
表现在，在要执行的类的路径里面执行java时，一定要添加上点号（.）标示本目录也要搜索。

假设abc.class在路径c:\src里面
可以在任何路径下执行以下命令

```bash
java -classpath c:\classes;c:\jar\abc.jar;c:\zip\abc.zip;c:\src abc
```



问题：如果main.class属于c:\jar\abc.jar，并且在com.cnblogs.jeffchen这个包里，那么执行java -classpath c:\classes;c:\jar\abc.jar;c:\zip\abc.zip;com.cnblogs.jeffchen.main即可， 但是如果classpath中包含多个jar包呢？并且其他jar包中也有com.cnblogs.jeffchen会发生什么情况？错误？

在windows下，

文件路径的分割符为反斜杠  \   
类或者java文件列表的分割符为分号 ;

在linux下

文件路径的分隔符位斜杠 /
类或者java文件列表的分隔符为冒号 :

一个linux下编译和运行的例子

```bash
 /usr/local/java/bin/javac -classpath /tmp/javatest/lib/mail-1.3.3.jar -d /tmp/javatest/bin/ /tmp/javatest/src/jp/co/realseed/Capability.java
/usr/local/java/bin/java -classpath /tmp/javatest/lib/mail-1.3.3.jar:/tmp/javatest/bin/ jp.co.realseed.Capability
```



比如algs4
```
C:\Users\HUMAN\.jdks\openjdk-16\bin\java.exe "-javaagent:D:\Program Files\IntelliJ IDEA 2020.2.2\lib\idea_rt.jar=13028:D:\Program Files\IntelliJ IDEA 2020.2.2\bin" -Dfile.encoding=UTF-8 -classpath "C:\Users\HUMAN\algs4\Algorithms, 4th Edition\algs4_java\target\classes" edu.princeton.cs.algs4.StdIn
```


















# 2. bash执行脚本

https://www.jianshu.com/p/e42dc0652b6d



https://blog.csdn.net/chen930724/article/details/49432051

```bash
#!/bin/bash
echo "build start"
 
JAR_PATH=lib
BIN_PATH=bin
SRC_PATH=src
 
# java文件列表目录，使用@文件名来管理java源文件，可以简化命令
SRC_FILE_LIST_PATH=src/sources.list
 
#生所有的java文件列表
rm -f $SRC_PATH/sources
find $SRC_PATH/ -name *.java > $SRC_FILE_LIST_PATH
 
#删除旧的编译文件 生成bin目录
rm -rf $BIN_PATH/
mkdir $BIN_PATH/
 
#生成依赖jar包列表
for file in  ${JAR_PATH}/*.jar;
do
jarfile=${jarfile}:${file}
done
echo "jarfile = "$jarfile

# copy配置文件
cp src/*.properties bin/
cp src/*.xml bin/ 

#编译
/usr/bin/javac -encoding UTF-8  -d $BIN_PATH/ -cp $jarfile @$SRC_FILE_LIST_PATH
 
#运行，添加了GC监控的选项，不适合生产环境
/usr/bin/java -XX:+PrintGCTimeStamps -XX:+PrintGCDetails -verbose:gc -Xloggc:/tmp/gc.log -cp $BIN_PATH$jarfile com.main.BootStrap &
```





















# 算法四执行 有参数函数命令行实现


生成[)

```bash
"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=2976:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.RandomSeq 10000 100.0 200.0 > data.txt
```





均值

```bash
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=2976:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.Average < data.txt
Average is 150.44569000000092
```

管道

```bash
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=2976:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.RandomSeq 10 23 96  |  "C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=2976:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.Average
Average is 60.476
```


plot2D画图例子：

```java
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=8938:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.Point2D 50 50 100
```

从(50,50)出发射线到100随机点


重定向输入

Binary二分查找不在tinyW.txt会员id白名单中,访问用户id列表tinyT.txt (0 4 6 8)

```bash
D:\tridu33\algs4-java>more tinyW.txt
1
2
3
5
7
9

D:\tridu33\algs4-java>more tinyT.txt
9
8
7
6
5
4
3
2
1
0

```

ret:


```bash
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=8938:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.BinarySearch tinyW.txt < tinyT.txt
8
6
4
0

```



res

自动机 + pattern + string

返回正则模式是否匹配string表达式

```java
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=9429:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.NFA a*a aaa
true
```




返回tinyL.txt中不满足"(A*B|AC)D"正则语言的文字串：


```
more tinyL.txt
```

run


```bash
D:\tridu33\algs4-java>
"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=9616:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.GREP "(A*B|AC)D" < tinyL.txt
ABD
ABCCBD
```




```bash
D:\tridu33\algs4-java>"C:\Program Files\Java\jdk-15.0.1\bin\java.exe" "-javaagent:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\lib\idea_rt.jar=9616:D:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1\bin" -Dfile.encoding=UTF-8 -classpath D:\tridu33\algs4-java\target\classes edu.princeton.cs.algs4.GREP StdIn < GREP.java while(StdIn.hasNextLine())    String txt = StdIn.read Line();
```



IDEA带参数运行java程序

1点击Run下的Edit Configurations
2配置Configuration页中的Program arguments选项，就可以在idea中传入参数，参数之间用空格隔开。







# 算法第四版


https://algs4.cs.princeton.edu/code/


```bash
javac -cp .;D:\tridu33\algs4-java\lib\algs4.jar HelloWorld.java
java  -cp .;D:\tridu33\algs4-java\lib\algs4.jar HelloWorld
```
























































