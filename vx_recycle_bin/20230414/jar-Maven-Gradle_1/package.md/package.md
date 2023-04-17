# package


https://www.sxt.cn/java.lang/java.lang.html



不需要导包的类：

1.同包下的类


2.java.lang下的类（System，String，Math..…）


如果要使用非同包下的其他类时，需要导包：


1.权限定名（指明完整路径：包名+类名），只在当前处有效，每使用一次都要指明一次，使用比较麻烦


2.import导入
位置：类的上面
方式：import 包名+类名；


3.使用的类可以一个一个导入
也可以批量导入
通配符，匹配当前包下的多个类，会降低编译效率，不影响运行效率


4.静态导入只导入静态内容（变量，方法..）import static 包名+类名+变量名|方法名；



https://www.bilibili.com/video/BV1Mt4y1e7RQ?p=2&spm_id_from=pageDriver




1.java.lang-语言包：语言中常用的功能，如：String、Math、System、Integer、Thread.

2.java.util-工具包：提供一些实用的工具类，如：容器（List、Set、Map..），日期类3.java.io-输入输出包：提供操作读取文件的相关类，如：File、InputStream、OutputStrem…

4.java.net-网络包：操作远程资源的类，如：InetSocketAddress、DatagramPacket、ServerSocket...

5.java.sql-数据库包：操作DBC的类，Connection、Statement、ResultSet..…






用法：jar {ctxu}[vfm0Mi] [jar-文件] [manifest-文件] [-C 目录] 文件名 ...
选项：
-c 创建新的存档
-t 列出存档内容的列表
-x 展开存档中的命名的（或所有的〕文件
-u 更新已存在的存档
-v 生成详细输出到标准输出上
-f 指定存档文件名
-m 包含来自标明文件的标明信息
-0 只存储方式；未用ZIP压缩格式
-M 不产生所有项的清单（manifest〕文件
-i 为指定的jar文件产生索引信息
-C 改变到指定的目录，并且包含下列文件：
如果一个文件名是一个目录，它将被递归处理。
清单（manifest〕文件名和存档文件名都需要被指定，按'm' 和 'f'标志指定的相同顺序。
示例1：将两个class文件存档到一个名为 'classes.jar' 的存档文件中：
jar cvf classes.jar Foo.class Bar.class
示例2：用一个存在的清单（manifest）文件 'mymanifest' 将 foo/ 目录下的所有
文件存档到一个名为 'classes.jar' 的存档文件中：
jar cvfm classes.jar mymanifest -C foo/ .
示例3：war：jar cvf ycportal.war ycportal/
ear: jar cvf ycportal.ear ycportal/