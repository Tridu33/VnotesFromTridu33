# Spark和Scala版本对应





spark.apache.org/docs/latest/index.html



Spark可在Windows和类似UNIX的系统（例如Linux，Mac OS）上运行，并且应在运行受支持的Java版本的任何平台上运行。这应该包括x86_64和ARM64上的JVM。在一台机器上本地运行很容易-您所需要做的就是java在系统上安装PATH或JAVA_HOME指向Java安装的环境变量。

Spark可在Java 8/11，Scala 2.12，Python 2.7 + / 3.4 +和R 3.1+上运行。从Spark 3.0.0开始不推荐使用Java 8之前的版本8u92。从Spark 3.0.0开始不推荐使用3.6版之前的Python 2和Python 3。从Spark 3.0.0开始不推荐使用3.4版之前的R。对于Scala API，Spark 3.0.0使用Scala 2.12。您将需要使用兼容的Scala版本（2.12.x）。

对于Java 11，-Dio.netty.tryReflectionSetAccessible=trueApache Arrow库另外需要。这样可以防止java.lang.UnsupportedOperationException: sun.misc.Unsafe or java.nio.DirectByteBuffer.(long, int) not availableApache Arrow在内部使用Netty的情况。

>Note that, Spark 2.x is pre-built with Scala 2.11 except version 2.4.2, which is pre-built with Scala 2.12. Spark 3.0+ is pre-built with Scala 2.12.


scala-lang.org/download/all.html



spark.apache.org/downloads.html


archive.apache.org/dist/spark/


































