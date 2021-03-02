[Python Tutor](http://pythontutor.com/) ([code on GitHub](https://github.com/pgbovine/OnlinePythonTutor)) supports: Python [3.6](https://docs.python.org/3.6/) and [2.7](https://docs.python.org/2.7/) with limited imports (\_\_future\_\_, abc, array, bisect, calendar, cmath, collections, copy, datetime, decimal, doctest, fractions, functools, hashlib, heapq, io, itertools, json, locale, math, operator, pickle, pprint, random, re, string, time, types, unittest, StringIO (Python 2), typing (Python 3)), Oracle Java 8 (implemented by [David Pritchard](https://github.com/daveagp) and Will Gwozdz, supports `[StdIn](http://introcs.cs.princeton.edu/java/stdlib/javadoc/StdIn.html)`, `[StdOut](http://introcs.cs.princeton.edu/java/stdlib/javadoc/StdOut.html)`, most other [stdlib libraries](http://introcs.cs.princeton.edu/java/stdlib), [Stack](http://introcs.cs.princeton.edu/java/43stack/Stack.java.html), [Queue](http://introcs.cs.princeton.edu/java/43stack/Queue.java.html), and [ST](http://introcs.cs.princeton.edu/java/44st/ST.java.html). To access built-in Stack/Queue classes, write: import java.util.Stack; This won't work: import java.util.*;), JavaScript ES6 and TypeScript 1.4.1 (Node.js v6.0.0), Ruby 2 (MRI 2.2.2), C and C++ (gcc 4.8, C11/C++11, Valgrind Memcheck)

Privacy Policy: By using Python Tutor, your visualized code, options, user interactions, text chats, and IP address are logged on our server and may be analyzed for research purposes. Nearly all web services collect this basic information from users in their server logs. However, Python Tutor does not collect any personally identifiable information from its users. It uses Google Analytics for website analytics.

Terms of Service: The Python Tutor service is provided for free on an as-is basis. Use this service at your own risk. Do not use it to share confidential information. The developers of Python Tutor are not responsible for the chat messages or behaviors of any of the users on this website. We are also not responsible for any damages caused by using this website. Finally, it is your responsibility to follow appropriate academic integrity standards.


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


![秘技](_v_images/秘技_1597720117_3550.png)

```

#pythontutor_hide:arr

tmp = sum(arr) #break

```





# pythontutor可视化python原理



Python Tutor 是由 Philip Guo 开发的一个免费教育工具，可帮助学生攻克编程学习中的基础障碍，理解每一行源代码在程序执行时在计算机中的过程。  
[http://www.pythontutor.com/](http://www.pythontutor.com/)

  


左侧是源码，右侧执行过程的图示。点击源码下方的“Forward”和“Back”可进行相应操作。



GitHub 开源：  
[https://github.com/pgbovine/OnlinePythonTutor/](https://github.com/pgbovine/OnlinePythonTutor/)


一个人写的笔记

[https://github.com/sijichun/PythonTutor](https://github.com/sijichun/PythonTutor)



```python
# -*- coding: UTF-8 -*-
t = (1,2,[30,40])
t[2] += [50,60]
```






pythontutor.bat打开python bottle_server.py


```cmd
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Miniconda3' ;python bottle_server.py"
```






live.bat


```cmd
start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8003/live.html
```


visualize.bat

```cmd
start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8003/visualize.html
```





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



书的话，52pojie的悬赏问答区有完整版（大陆 清华大学出版社）。  
如果指这书配套资料话，deepmind.com.tw 输入书名查询。但下载需要“书号” 我也不知道是什么。  
如果指 PythonTutor 视频的话，油管有很多。但我觉得 陈光教授的视频是目前最棒的，没理由看其他视频。  
更多：github.com/pgbovine/OnlinePythonTutor  
其他补充：关于python调试可参考 《Python Debugging Handbook by R L Zimmerman》  
ISBN: 9798608293733

























































































































































































