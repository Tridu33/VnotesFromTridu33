# 1. Ubuntujava1.6安装







https://gist.github.com/senthil245/6093389





```java
(base)master@computer:$ sudo update-alternatives --install "/usr/bin/java" "java" \ "/usr/l
ib/jvm/jdk1.6.0_45/bin/java" 1
update-alternatives: error: alternative path is not absolute as it should be:  /usr/lib/jvm/jdk1.6.0_45/bin/java
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ cd /usr/lib/jvm/jdk1.6.0_45/bin/
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ pwd
/usr/lib/jvm/jdk1.6.0_45/bin
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ sudo update-alternatives --install "/usr/bin/java" "java"  "/usr/li
b/jvm/jdk1.6.0_45/bin/java" 1
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ sudo update-alternatives --install "/usr/bin/javac" "javac"  "/usr/
lib/jvm/jdk1.6.0_45/bin/javac" 1
update-alternatives: using /usr/lib/jvm/jdk1.6.0_45/bin/javac to provide /usr/bin/javac (javac) in auto mode
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ sudo update-alternatives --install "/usr/bin/javaws" "javaws"  "/us
r/lib/jvm/jdk1.6.0_45/bin/javaws" 1
update-alternatives: using /usr/lib/jvm/jdk1.6.0_45/bin/javaws to provide /usr/bin/javaws (javaws) in auto mode
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ sudo update-alternatives --config java
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
  0            /usr/lib/jvm/java-14-openjdk-amd64/bin/java      1411      auto mode
  1            /usr/lib/jvm/java-14-openjdk-amd64/bin/java      1411      manual mode
* 2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode
  3            /usr/lib/jvm/jdk1.6.0_45/bin/java                1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
update-alternatives: using /usr/lib/jvm/jdk1.6.0_45/bin/java to provide /usr/bin/java (java) in manual mode
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ sudo update-alternatives --config javaws
There is only one alternative in link group javaws (providing /usr/bin/javaws): /usr/lib/jvm/jdk1.6.0_45/bin/javaws
Nothing to configure.
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ java -version
java version "1.6.0_45"
Java(TM) SE Runtime Environment (build 1.6.0_45-b06)
Java HotSpot(TM) 64-Bit Server VM (build 20.45-b01, mixed mode)
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ javac -version
javac 1.6.0_45
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ javaws -version
Java(TM) Web Start 1.6.0_45
Usage:  javaws [run-options] <jnlp-file>
        javaws [control-options]

where run-options include:
  -verbose              display additional output
  -offline              run the application in offline mode
  -system               run the application from the system cache only
  -Xnosplash            run without showing a splash screen
  -J<option>            supply option to the vm
  -wait                 start java process and wait for its exit

control-options include:
  -viewer               show the cache viewer in the java control panel
  -uninstall            remove all applications from the cache
  -uninstall <jnlp-file>                remove the application from the cache
  -import [import-options] <jnlp-file>  import the application to the cache

import-options include:
  -silent               import silently (with no user interface)
  -system               import application into the system cache
  -codebase <url>       retrieve resources from the given codebase
  -shortcut             install shortcuts as if user allowed prompt
  -association          install associations as if user allowed prompt

(base)master@computer:/usr/lib/jvm/jdk1.6.0_45/bin$ cd ..
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45$ java -version
java version "1.6.0_45"
Java(TM) SE Runtime Environment (build 1.6.0_45-b06)
Java HotSpot(TM) 64-Bit Server VM (build 20.45-b01, mixed mode)
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45$ sudo nano  /etc/environment
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45$ sudo env | grep JAVA_HOME
(base)master@computer:/usr/lib/jvm/jdk1.6.0_45$ echo $JAVA_HOME
```




















