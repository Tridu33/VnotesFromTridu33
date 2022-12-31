





不支持的特征：https://docs.google.com/document/d/13_Bc-l2FKMgwPx4dZb0sv7eMfYMHhRVgBRShha8kgbU/edit# word文档



>http://pythontutor.com/visualize.html#code=%23%20%5Bofficial%20Python%20Tutor%20example%5D%0A%0A%23%20when%20the%20string%20%23break%20is%20the%20last%20thing%20on%20a%20line,%20then%20only%0A%23%20trace%20the%20execution%20of%20those%20lines.%20this%20can%20make%20it%20possible%20to%0A%23%20trace%20longer-running%20programs%20by%20stopping%20only%20at%20selected%20lines%0A%0A%23%20normally%20execution%20would%20halt%20after%201000%20steps,%20so%20you'd%20never%0A%23%20get%20to%20print%20everything%20...%20but%20if%20you%20put%20'%23break'%20on%20line%2012%0A%23%20then%20it%20will%20stop%20and%20print%20out%20all%20the%20desired%20numbers%0Afor%20i%20in%20range%2810000%29%3A%0A%20%20%20%20if%20i%20%3E%200%20and%20i%20%25%201000%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28i%29%20%23break&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

其中 %20 就是空格，URL编码。这行代码对应网站上直接打开：
%23井号键

$3A

https://tool.chinaz.com/tools/urlencode.aspx 在线工具解码

%0A换行

```python
# [official Python Tutor example]

# when the string #break is the last thing on a line, then only
# trace the execution of those lines. this can make it possible to
# trace longer-running programs by stopping only at selected lines

# normally execution would halt after 1000 steps, so you'd never
# get to print everything ... but if you put '#break' on line 12
# then it will stop and print out all the desired numbers
for i in range(10000):
    if i > 0 and i % 1000 == 0:
        print(i) #break
```


如果尝试在线编码，则是：

```
for i in range(10000):
    if i > 0 and i % 1000 == 0:
        print(i)
```

>http://pythontutor.com/visualize.html#code=这里填写被替换的代码部分URL编码&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

需要修改换行键为%0A 

>http://pythontutor.com/visualize.html#code=for+i+in+range(10000)%3a%0A++++if+i+%3e+0+and+i+%25+1000+%3d%3d+0%3a%0A++++++++print(i)
&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

办法就是vs code中ctrl + H 替换正则表达式 \n 为%0A

我很傻逼地发现官方网站已经有直接生成网址链接的按钮：**Generate permanent link**,但是也是不能生成的
。


>http://pythontutor.com/visualize.html#code=for%20i%20in%20range%2810000%29%3A%0A%20%20%20%20if%20i%20%3E%200%20and%20i%20%25%201000%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28i%29&cumulative=false&curInstr=999&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


%23!%2fusr%2fbin%2fenv%20python%20%0A%23%20-*-%20coding%3aUTF-8%20-*-%0A%23%0A%22%22%22%0A%22%22%22%0Aclass%20Node%3a%0A%20%20%20%20def%20__init__(self%2c%20data)%3a%0A%20%20%20%20%20%20%20%20self.data%20%3d%20data%0A%20%20%20%20%20%20%20%20self.next%20%3d%20None%0Aclass%20SLL%3a%0A%20%20%20%20def%20__init__(self%2c%20head%3dNone)%3a%0A%20%20%20%20%20%20%20%20self.head%20%3d%20head%0A%20%20%20%20def%20print_list(self)%3a%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%e9%81%8d%e5%8e%86%e9%93%be%e8%a1%a8%ef%bc%8c%e5%b9%b6%e5%b0%86%e5%85%83%e7%b4%a0%e4%be%9d%e6%ac%a1%e6%89%93%e5%8d%b0%e5%87%ba%e6%9d%a5%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20print(%22linked_list%3a%22)%0A%20%20%20%20%20%20%20%20temp%20%3d%20self.head%0A%20%20%20%20%20%20%20%20new_list%20%3d%20%5b%5d%0A%20%20%20%20%20%20%20%20while%20temp%20is%20not%20None%3a%0A%20%20%20%20%20%20%20%20%20%20%20%20new_list.append(temp.data)%0A%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3d%20temp.next%0A%20%20%20%20%20%20%20%20print(new_list)%0A%20%20%20%20def%20reverse(self)%3a%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%e5%b0%86%e9%93%be%e8%a1%a8%e5%8f%8d%e8%bd%ac%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20prev%20%3d%20None%0A%20%20%20%20%20%20%20%20current%20%3d%20self.head%0A%20%20%20%20%20%20%20%20while%20current%3a%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20next_node%20%3d%20current.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20current.next%20%3d%20prev%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20prev%20%3d%20current%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20current%20%3d%20next_node%0A%20%20%20%20%20%20%20%20%20%20%20%20next_node%2c%20current.next%20%3d%20current.next%2c%20prev%0A%20%20%20%20%20%20%20%20%20%20%20%20prev%2c%20current%20%3d%20current%2c%20next_node%0A%20%20%20%20%20%20%20%20self.head%20%3d%20prev%0A%20%20%20%20def%20initlist(self%2c%20data_list)%3a%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%e5%b0%86%e5%88%97%e8%a1%a8%e8%bd%ac%e6%8d%a2%e4%b8%ba%e9%93%be%e8%a1%a8%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20%23%20%e5%88%9b%e5%bb%ba%e5%a4%b4%e7%bb%93%e7%82%b9%0A%20%20%20%20%20%20%20%20self.head%20%3d%20Node(data_list%5b0%5d)%0A%20%20%20%20%20%20%20%20temp%20%3d%20self.head%0A%20%20%20%20%20%20%20%20%23%20%e9%80%90%e4%b8%aa%e4%b8%ba%20data%20%e5%86%85%e7%9a%84%e6%95%b0%e6%8d%ae%e5%88%9b%e5%bb%ba%e7%bb%93%e7%82%b9%2c%20%e5%bb%ba%e7%ab%8b%e9%93%be%e8%a1%a8%0A%20%20%20%20%20%20%20%20for%20i%20in%20data_list%5b1%3a%5d%3a%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3d%20Node(i)%0A%20%20%20%20%20%20%20%20%20%20%20%20temp.next%20%3d%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3d%20temp.next%0Adef%20main()%3a%0A%20%20%20%20%23print(%22Python%20template%22)%0A%20%20%20%20mylist%20%3d%20SLL()%0A%20%20%20%20mylist.initlist(%5b1%2c2%2c3%2c4%2c5%5d)%0A%20%20%20%20mylist.print_list()%0A%20%20%20%20mylist.reverse()%0A%20%20%20%20print(%22After%20reverse%3a%22)%0A%20%20%20%20mylist.print_list()%0Aif%20__name__%20%3d%3d%20%27__main__%27%3a%0A%20%20%20%20main()

可视化动画工具，真是一个非常棒的帮手。这类工具/网站，

-   **旧金山大学数据结构和算法的可视化学习工具**

> http://hao.jobbole.com/visualizing-algorithms-and-data-structure/
-   **VisuAlgo：通过动画学习算法和数据结构**

> http://hao.jobbole.com/visualgo/

-   **Algomation：查看、创建和分享算法的学习平台**

> http://hao.jobbole.com/algomation/

  

一个同类型的新网站 Algorithm Visualizer，做得很好。  

  

网址是：http://algorithm-visualizer.org

但是直接生成也没有%20






# 1. pythontutor可视化python原理

课代表  https://www.bilibili.com/video/BV1gz411z7bx 来啦  
1\. 基本功能  
a. 网站浏览：pythontutor.com  
i. 左边代码  
1) 坐下步骤控制（随意调节）  
ii. 右边  
1) 涉及到的对象、命名、命名空间、内存使用  
2) 比如递归时，可以逐步显示栈  
b. 特点：  
i. 程序单步运行  
ii. 断点设置  
1) 右边栏会图形化显示当前内存分配情况，方便检查是否使用同一个内存地址  
iii. 演示用，超大/∞步数（eg.斐波那契）仅显示999步  
1) 为了使得图更简介 可以隐藏变量显示，在变量前使用#pythontutor_hide: 变量名称 的注释  
2) 可以使用断点 #break  
  
  
  
2\. PythonTutor的基本使用  
a. 可以选择python各种版本，甚至其他语言（包括java，c—++  
b. 两种运行模式：  
i. 可视化运行  
1) 一次编程  
2) 运行时演示动画  
ii. 现场编程模式  
1) 实时动画  
c. 下面还有教材和推荐的课程以及示例  
3\. 本地搭建  
a. https://fly51fly.lanzous.com/ibrhwuh  
b.










Python Tutor 是由 Philip Guo 开发的一个免费教育工具，可帮助学生攻克编程学习中的基础障碍，理解每一行源代码在程序执行时在计算机中的过程。  
[http://www.pythontutor.com/](http://www.pythontutor.com/)

  


左侧是源码，右侧执行过程的图示。点击源码下方的“Forward”和“Back”可进行相应操作。



## 1.1. GitHub 开源：  
 

github地址（完整版）：https://github.com/pgbovine/OnlinePythonTutor 打不开了，不知道是作者github改名字 https://github.com/hcientist/OnlinePythonTutor
(这个应该是最新的Philip Guo 有commit记录，应该还是这个博士写的Philip J. Guo (philip@pgbovine.net) https://pg.ucsd.edu/
)还是网站建设好之后删掉源码

反正这里有备份：
https://gitee.com/lwylswy/OnlinePythonTutor/tree/master

https://github.com/dadashek/OnlinePythonTutor














北邮陈光提供（精简版）：https://fly51fly.lanzous.com/ibrhwuh

**Jupyter noteboo**k magics to **embed pythontutor.com** within an IFrame in the Jupyter (classic or Lab) notebook using the code from a Jupyter code cell.
https://github.com/kikocorreoso/tutormagic











```python
# -*- coding: UTF-8 -*-
t = (1,2,[30,40])
t[2] += [50,60]
```

These examples demonstrate the tool's visualization capabilities but are *not* meant as coding lessons.

Python Examples

Basic: [hello](http://pythontutor.com/visualize.html#) | [happy](http://pythontutor.com/visualize.html#) | [intro](http://pythontutor.com/visualize.html#) | [filter](http://pythontutor.com/visualize.html#) | [tokenize](http://pythontutor.com/visualize.html#) | [insertion sort](http://pythontutor.com/visualize.html#) | [for-else](http://pythontutor.com/visualize.html#) | [user input](http://pythontutor.com/visualize.html#)

Math: [factorial](http://pythontutor.com/visualize.html#) | [fibonacci](http://pythontutor.com/visualize.html#) | [memoized fibonacci](http://pythontutor.com/visualize.html#) | [square root](http://pythontutor.com/visualize.html#) | [gcd](http://pythontutor.com/visualize.html#) | [towers of hanoi](http://pythontutor.com/visualize.html#)

Objects: [OOP 1](http://pythontutor.com/visualize.html#) | [OOP 2](http://pythontutor.com/visualize.html#) | [OOP 3](http://pythontutor.com/visualize.html#) | [inheritance](http://pythontutor.com/visualize.html#)

Linked Lists: [LL 1](http://pythontutor.com/visualize.html#) | [LL 2](http://pythontutor.com/visualize.html#) | [LL sum](http://pythontutor.com/visualize.html#)

Pointer Aliasing:  
[aliasing1](http://pythontutor.com/visualize.html#) | [aliasing2](http://pythontutor.com/visualize.html#) | [aliasing3](http://pythontutor.com/visualize.html#) | [aliasing4](http://pythontutor.com/visualize.html#) | [aliasing5](http://pythontutor.com/visualize.html#) | [aliasing6](http://pythontutor.com/visualize.html#) | [aliasing7](http://pythontutor.com/visualize.html#) | [aliasing8](http://pythontutor.com/visualize.html#) | [sumList](http://pythontutor.com/visualize.html#)

Higher-Order Functions:  
[closure1](http://pythontutor.com/visualize.html#) | [closure2](http://pythontutor.com/visualize.html#) | [closure3](http://pythontutor.com/visualize.html#) | [closure4](http://pythontutor.com/visualize.html#) | [closure5](http://pythontutor.com/visualize.html#) | [list map](http://pythontutor.com/visualize.html#) | [summation](http://pythontutor.com/visualize.html#) | [lambda param](http://pythontutor.com/visualize.html#)

Advanced:  
[list comp](http://pythontutor.com/visualize.html#) | [list/set/dict comp](http://pythontutor.com/visualize.html#) | [decorator](http://pythontutor.com/visualize.html#) | [generator](http://pythontutor.com/visualize.html#) | [genexpr](http://pythontutor.com/visualize.html#) | [varargs](http://pythontutor.com/visualize.html#) | [exception](http://pythontutor.com/visualize.html#) | [metaclass](http://pythontutor.com/visualize.html#)

Python 3 only: [student torture](http://pythontutor.com/visualize.html#) | [nonlocal](http://pythontutor.com/visualize.html#)

Java Examples

Basic: [Variables](http://pythontutor.com/visualize.html#) | [ControlFlow](http://pythontutor.com/visualize.html#) | [Sqrt](http://pythontutor.com/visualize.html#) | [ExecLimit](http://pythontutor.com/visualize.html#) | [Strings](http://pythontutor.com/visualize.html#)

Methods: [PassByValue](http://pythontutor.com/visualize.html#) | [Recursion](http://pythontutor.com/visualize.html#) | [StackOverflow](http://pythontutor.com/visualize.html#)

OOP: [Rolex](http://pythontutor.com/visualize.html#) | [Person](http://pythontutor.com/visualize.html#) | [Complex](http://pythontutor.com/visualize.html#) | [Casting](http://pythontutor.com/visualize.html#)

Data structures: [LinkedList](http://pythontutor.com/visualize.html#) | [StackQueue](http://pythontutor.com/visualize.html#) | [Postfix](http://pythontutor.com/visualize.html#) | [SymbolTable](http://pythontutor.com/visualize.html#)

Java features: [ToString](http://pythontutor.com/visualize.html#) | [Reflect](http://pythontutor.com/visualize.html#) | [Exception](http://pythontutor.com/visualize.html#) | [ExceptionFlow](http://pythontutor.com/visualize.html#) | [TwoClasses](http://pythontutor.com/visualize.html#)

Misc: [Forest](http://pythontutor.com/visualize.html#) | [Knapsack](http://pythontutor.com/visualize.html#) | [StaticInitializer](http://pythontutor.com/visualize.html#) | [Synthetic](http://pythontutor.com/visualize.html#)

(All Java examples created by [David Pritchard](https://github.com/daveagp))

JavaScript Examples

[factorial](http://pythontutor.com/visualize.html#) | [data types](http://pythontutor.com/visualize.html#) | [exception](http://pythontutor.com/visualize.html#) | [closure](http://pythontutor.com/visualize.html#) | [shadowing](http://pythontutor.com/visualize.html#) | [constructor](http://pythontutor.com/visualize.html#) | [inheritance](http://pythontutor.com/visualize.html#)

TypeScript Examples

[hello](http://pythontutor.com/visualize.html#) | [classes](http://pythontutor.com/visualize.html#) | [inheritance](http://pythontutor.com/visualize.html#) | [generics](http://pythontutor.com/visualize.html#)

Ruby Examples

[Containers](http://pythontutor.com/visualize.html#) | [Globals](http://pythontutor.com/visualize.html#) | [Constants](http://pythontutor.com/visualize.html#) | [Blocks](http://pythontutor.com/visualize.html#) | [Block scoping](http://pythontutor.com/visualize.html#) | [More block scoping](http://pythontutor.com/visualize.html#)

[Proc & Lambda](http://pythontutor.com/visualize.html#) | [Proc scoping](http://pythontutor.com/visualize.html#) | [Proc return](http://pythontutor.com/visualize.html#) | [Lambda scoping](http://pythontutor.com/visualize.html#) | [Inheritance](http://pythontutor.com/visualize.html#) | [Symbols](http://pythontutor.com/visualize.html#)

[Protected & private](http://pythontutor.com/visualize.html#) | [Class & instance vars](http://pythontutor.com/visualize.html#) | [Toplevel defs](http://pythontutor.com/visualize.html#) | [Megagreeter](http://pythontutor.com/visualize.html#)

C Examples

[Thesis](http://pythontutor.com/visualize.html#) | [Globals](http://pythontutor.com/visualize.html#) | [Structs](http://pythontutor.com/visualize.html#) | [Nested structs](http://pythontutor.com/visualize.html#) | [Array overflow](http://pythontutor.com/visualize.html#) | [Array param](http://pythontutor.com/visualize.html#)

[String reverse](http://pythontutor.com/visualize.html#) | [Pointer levels](http://pythontutor.com/visualize.html#) | [Pointer chain](http://pythontutor.com/visualize.html#) | [Pointers wild](http://pythontutor.com/visualize.html#) | [Typedef](http://pythontutor.com/visualize.html#)

C++ Examples

[Basic](http://pythontutor.com/visualize.html#) | [Pass by ref](http://pythontutor.com/visualize.html#) | [Class](http://pythontutor.com/visualize.html#) | [Class pointer](http://pythontutor.com/visualize.html#) | [Date class](http://pythontutor.com/visualize.html#) | [Inheritance](http://pythontutor.com/visualize.html#) | [Virtual method](http://pythontutor.com/visualize.html#)

[unsupported features](https://docs.google.com/document/d/13_Bc-l2FKMgwPx4dZb0sv7eMfYMHhRVgBRShha8kgbU/)








本地化PythonTutor，目的是为了更快更方便的使用。

PythonTutor的网站：[http://www.pythontutor.com/](http://www.pythontutor.com/) 

项目的两个下载地址：

github地址（完整版）：[https://github.com/pgbovine/OnlinePythonTutor](https://github.com/pgbovine/OnlinePythonTutor)

北邮陈光提供（精简版）：[https://fly51fly.lanzous.com/ibrhwuh](https://fly51fly.lanzous.com/ibrhwuh)

下载解压后，在cmd中输入：

```bash
pip install bottle
cd OnlinePythonTutor/v5-unity/
python bottle_server.py
```

然后在浏览器中输入：[http://localhost:8003/visualize.html](http://localhost:8003/visualize.html)或者[http://localhost:8003/live.html](http://localhost:8003/live.html)即可使用





https://b23.tv/xJYKh5  这里就是教程


 

```

#pythontutor_hide:arr

tmp = sum(arr) #break

```





pythontutor.bat打开python bottle_server.py


```
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Miniconda3' ;python bottle_server.py"
```






live.bat


```
start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8003/live.html
```


visualize.bat

```
start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8003/visualize.html
```















































































































































































