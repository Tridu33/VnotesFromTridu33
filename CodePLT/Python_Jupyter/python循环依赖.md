
    上策，拆成不循环引用的
    中策，把import放到最后
    下册，在函数里面import


一般来说，循环导入是不良设计的产物。对程序作更深入的分析可以得到结论：依赖其实是不必的，或者被依赖的功能可以被移动到不会包含循环引用的模块中。

简单的做法是有时两个模块可以合并到一个简单，更大的模块。

然而，合并后的模块可能有一些不相关的函数(强耦合)，并且在两个模块本来就含有大量代码的时候使得合并后的模块非常大。
如果前面的方法不能凑效，另一种方法就是延迟模块2的导入，在需要的时候才导入。

你可能会看到很多代码库中即使不存在循环依赖，仍然使用了延迟导入，这将加快启动速度，因此这并不被当做坏的实践(尽管这可能是坏的设计，但还是取决于你的项目实际情况)。

# 1. C++循环依赖



在开发大C++工程的时候如何判断和避免循环include? - 陈硕的回答 - 知乎
https://www.zhihu.com/question/23178386/answer/23824481











# 2. java spring 循环依赖

经典java面试题
Spring框架是怎么解决Bean之间的循环依赖的


如何手动关闭spring的循环依赖








# 3. python循环依赖

Python 如何理解模块循环导入依赖（Python 3）？ - 老王的回答 - 知乎
https://www.zhihu.com/question/61280844/answer/383314993

Python 中循环 import 造成的问题如何解决？ - 灵剑的回答 - 知乎
https://www.zhihu.com/question/19887316/answer/119484887

Python 中循环 import 造成的问题如何解决？ - 冒泡的回答 - 知乎
https://www.zhihu.com/question/19887316/answer/119584212

最好的做法是能不弄，就不要弄循环import，像**go**这种语言就由编译器禁止你这么搞，搞了就编译错误
py中循环import存在的问题主要在于对于没有导入的模块，import本身就是一次执行，就是把模块代码的global域当成正常代码执行一次，这样如果多个模块的全局变量有循环依赖，就可能异常，比如：
A.py:
```
import B
a = B.a
```
B.py:
```
import A
print A.a
a = 123
```
无论先import谁，都会报它没有属性a，这里import，赋值，print都是py的语句，一条条执行
比如从main.py里面先import A：

1 首次导入，A先进入sys模块的module表
2 由于是首次导入，从A开始执行，执行import B这句
3 B首次导入，进入sys的module表
4 从B.py的第一句开始，执行import A这句，由于A已经在表中，略过，然后执行print A.a，这时候A.py还没执行到给a赋值的地方，所以异常
避免这种情况一般就没什么事了，

个人一个习惯和建议是，全局变量初值都赋值为不依赖其他模块的值，比如None，整数等，如果需要依赖，模块提供init函数，由main模块在程序启动时候手工按顺序初始化好

需要注意的是，和import是可执行语句一样，def和class对于py都是可执行语句，def是把其下的代码块对应的函数对象关联给函数名，等于一个赋值，class要更复杂一点，先把它下面的代码块当成一个普通函数执行，最后执行MAKE_CLASS字节码做convert再赋值给类名，其他的，修饰器也是可执行代码，对py来说，一切都是指令，唯一一个“声明”语法，是global


作者：老王 https://www.zhihu.com/question/61280844/answer/383314993

```
start foo                       <--第一次运行foo.py开始
Is bar imported: False          <--foo.py第一次import bar，bar不在sys.modules中，进入bar.py
start bar                       <--bar.py开始
Is foo imported: False          <--在bar.py中import foo时，foo不在sys.modules中，再次进入foo.py
start foo                       <--第二次运行foo.py开始
Is bar imported: True           <--foo.py第二次import bar时，bar已在sys.modules中了，不再进入bar.py
end foo                         <--第二次foo.py结束
end bar                         <--bar.py结束
end foo                         <--第一次foo.py结束，整个程序结束
```



------------------------------------------------------------------------


似乎在python 3.5（可能还有更高版本）上允许循环导入，但在3.4（可能是波纹管）上不允许。











https://qastack.cn/programming/894864/circular-dependency-in-python
遇到一个常见的问题就是:


图中

(path)Connector需要Node parent, List<Node> children。Node需要入度Connector（path）出度Connector(path)。


如果像java一样写成两个类分开两个文件然后import就会导致“循环一类问题”，java spring 能解决循环依赖问题，


而最简单的办法就是

几个人说过“每个文件不需要一个类”，并带有“不要尝试成为Java”

[导入Python模块](https://web.archive.org/web/20150113060057/http://effbot.org/zone/import-confusion.htm)是一篇很棒的文章，解释了Python中的循环导入。


- 请重构程序以避免循环导入（将内容移至单独的模块通常会有所帮助），

- 或将导入移至模块的末尾（在这种情况下，如果将导入Y移至模块X的末尾，一切都会很好）。
解决此问题的最简单方法是将路径导入移动到节点模块的末尾。



















