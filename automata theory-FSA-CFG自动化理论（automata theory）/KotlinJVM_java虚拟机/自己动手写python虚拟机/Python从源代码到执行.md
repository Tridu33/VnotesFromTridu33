# 1. Python从源代码到执行



https://00kai0.github.io/cpy-compile-and-runtime-en/

Matz先生（Yukihiro Matsumoto）在解释语言处理器的结构时列出了一种通用的体系结构。



```
source code
    |
    |
   \./
----------                 ---------
|Compiler| ---mid code---> |Runtime|
----------                 ---------
                              /.\
                               |
                               |
                           ---------    
                           |  Lib  |
                           ---------    
```







处理器由三部分组成：编译器，运行时和lib。

编译器：顾名思义。它是编译源代码的程序。通常，它将源代码编译为将在运行时运行的中间代码。但是有时候，例如在C语言中，它们不是运行时，它将直接输出机器代码。此外，编译器可能会优化源代码并删除一些不必要的信息，例如注释和宏定义。

运行时：该程序用于执行代码。最熟悉的是JVM，因此我认为我们可以将其称为vm。

库：库很容易理解，就像字典一样，并具有运行程序所需的一些额外支持。


Java在这里非常有代表性。它以适当的方式遵循此过程。
首先，java编译器（javac）将源代码编译成包含字节码的.class文件。
然后将这些文件中的字节码放入JVM（vm）中，在JVM中，JVM负责执行Runtime的任务。
在运行过程中，所需的库（Lib）是从JDK导入的。


最基本的标准库应该包含IO库之类的东西，例如stdio.h，平台提供的ans系统调用。在Python中，编译器只占相对较小的工作量，因为它们没有复杂的语法检查和类型检查，因此大部分工作都是在运行时完成的。而且大多数错误只能在运行过程中找到。
像这样的语言（运行时部分负责大部分工作）看起来像直接从源代码执行的语言，因此它们被称为解释性语言。

因此，Python的效率远远低于Java和C（它们是静态编译的语言）。






python编译器大致分为以下四个步骤：

>将源代码解析为解析器树。
>从解析器树转换为抽象语法树。
>从ast转换为控制流程图。
>根据流程图将字节码发送到虚拟机



虚拟机（VM）：此处提到的虚拟机不是KVM或VMware vm。它指的是在软件层对CPU执行的仿真，最著名的应该是JVM。

Python和Ruby还以非翻译语言包含用于执行程序的虚拟机。



字节码：字节码与机器代码非常相似。机器代码是CPU可以读取的机器指令。然后，字节码是虚拟机执行的指令。





```python
import dis

def hello(): 
    print("Hello World")

print(dis.dis(hello))

# 0 LOAD_GLOBAL              0 (print)
# 2 LOAD_CONST               1 ('Hello World')
# 4 CALL_FUNCTION            1
# 6 POP_TOP
# 8 LOAD_CONST               0 (None)
# 10 RETURN_VALUE

"""
LOAD_GLOBAL：将全局变量推print入堆栈
LOAD_CONST：将常量推Hello World入堆栈
CALL_FUNCTION：执行print函数，弹出常量Hello Word和print变量，然后将结果压入堆栈
POP_TOP：弹出堆栈的顶部元素，它是print函数的返回值。
LOAD_CONST：将常量推None入堆栈
RETURN_VALUE：弹出堆栈的顶部元素作为最终返回值
"""
```

CPython版本3.8.4中，有163条指令。它们在不同的CPython版本之间可能会有一些差异。尝试时，您会看到不同的说明。不用担心，没错。如果您对这些说明感兴趣，可以在源代码（Include / opcode.h）中查看它们。




CPython is baesed on a 栈虚拟机stack virtual machine architecture. Another architecture is 寄存器register virtual machine.

仍然存在一些问题：如何CALL_FUNCTION查找函数并调用它？说明旁边的数字是什么意思？

指令前面的数字0、2、4，..，10。看来字节码的长度。0-2表示字节码的长度为2个字节。换句话说，完整的字节码实际上是一个字（1个字= 2个字节）。
实际上，被称为“字码”更为合适。



然后就是单词代码的组成。一个字有16位。

如前所述，CPython当前支持163条指令。我们如何保存它们？

指令占用8位，因此目前可以扩展为256条指令，其余8位节省了参数长度。

这样，一个函数只能推送256个参数（我以前没有试过，但是如果您感兴趣的话可以）。



因此，您看到的指令后的0和1实际上是当前参数长度。调用时，虚拟机将从堆栈顶部通过参数长度检索调用位置以进行调用。











