# JBMC_java模型检测



www.cprover.org/jbmc/


https://github.com/diffblue/cbmc/tree/develop/jbmc




`CBMC`是C和C ++程序的绑定模型检查器。它支持C89，C99，大多数C11以及gcc和Visual Studio提供的大多数编译器扩展。分析Java字节码的CBMC的变体形式为[`JBMC`](http://www.cprover.org/jbmc)。














JBMC是Java程序的绑定模型检查器。它检查运行时异常和用户定义的断言。通过展开程序中的循环并将结果公式传递到决策过程来执行验证。




JBMC [工具文件](http://www.kroening.com/publications/view-publications-ckkst2018.html)已在CAV 2018上接受。

有一个 与JBMC相关的公告的[Google](http://groups.google.co.uk/group/cprover)网上论坛。










## demo






介绍如何使用JBMC。

让我们考虑以下Java程序（[Simple.java](http://www.cprover.org/jbmc/Simple.java)）：

    `1. package my.petty.examples;
 2.
 3. public class Simple {
 4.
 5.     public static void main(String[] args) {
 6.         String s = new String("Abc");
 7.         String u = "bc";
 8.         assert(!s.contains(u)); // This assert failure should be found by JBMC!
 9.     }                           
10.
11. }` 

保存到文件 <some-directory> /my/petty/examples/Simple.java中。首先，我们需要如下编译类文件：

    `<some-directory>$ javac my/petty/examples/Simple.java` 

此命令创建一个类文件 <some-directory> /my/petty/examples/Simple.class。现在，我们准备使用JBMC检查程序中的缺陷。为此，我们在目录<some-directory>中执行以下命令：

    `<some-directory>$ <path-to-jbmc>/jbmc my.petty.examples.Simple --unwind 5 --classpath <path-to-jbmc>/core-models.jar:.` 

注意：用户需要在目录<some-directory>中运行上述命令，因为JBMC在搜索类文件时使用与JVM类似的策略。core-models.jar包含Java运行时库的JBMC模型。

这是JBMC 5.12产生的输出的最后一部分：

```

my/petty/examples/Simple.java function java::my.petty.examples.Simple.main:([Ljava/lang/String;)V
[java::my.petty.examples.Simple.main:([Ljava/lang/String;)V.1] line 6 no uncaught exception: SUCCESS
[java::my.petty.examples.Simple.main:([Ljava/lang/String;)V.null-pointer-exception.1] line 6 Null pointer check: SUCCESS
[java::my.petty.examples.Simple.main:([Ljava/lang/String;)V.assertion.1] line 8 assertion at file my/petty/examples/Simple.java line 8 function java::my.petty.examples.Simple.main:([Ljava/lang/String;)V bytecode-index 16: FAILURE
[java::my.petty.examples.Simple.main:([Ljava/lang/String;)V.null-pointer-exception.2] line 8 Null pointer check: SUCCESS
[java::my.petty.examples.Simple.main:([Ljava/lang/String;)V.null-pointer-exception.3] line 8 Null pointer check: SUCCESS

** 1 of 47 failed (2 iterations)
VERIFICATION FAILED

```

结果“ VERIFICATION FAILED ”表明JBMC已在程序中发现缺陷。为了找到缺陷，我们在结果列表中查找“ FAILURE ”。我们看到该缺陷在我们的Java文件的第8行中。

JBMC提供了许多用于自定义分析的命令行选项。选项在[此处](http://www.cprover.org/jbmc/command_line_options.html)列出 。您还可以使用--help选项获得列表 。























































