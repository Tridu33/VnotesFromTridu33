# 1. 使用egypt+graphviz生成函数调用关系图示例


https://www.bbsmax.com/A/6pdDrx2LJw/




有什么工具可以生成函数调用流程图？ - Quasars的回答 - 知乎
https://www.zhihu.com/question/34495043/answer/59051167
说看这里：
https://blog.csdn.net/solstice/article/details/488865
绘制函数调用关系图对理解大型程序大有帮助


函数调用关系图（call graph）是图（graph），而且是有向图，多半还是无环图（无圈图）——如果代码中没有直接或间接的递归的话。Graphviz是专门绘制有向图和无向图的工具，所以很多call graph分析工具都以它为后端(back end)。

google 关键字 "graphviz 函数" 或 "graphviz call graph".
维基 "call graph" 也有不少工具.



用CodeViz绘制cpp函数调用关系图(call graph)
https://developer.aliyun.com/article/245865

cpp项目生成jpk https://github.com/peiyake/mkjpg





# 2. 使用pycallgraph生成函数关系图
https://www.cnblogs.com/anliven/p/10004665.html
可用于创建python函数关系图，依赖于dot命令，需要先安装 graphviz；
HomePage：http://pycallgraph.slowchop.com/
Docs：https://pycallgraph.readthedocs.io/en/master/



```
$ pycallgraph graphviz -- ./test.py
```

默认将生成一个名为pycallgraph.png的函数关图

api


```
$ cat TempTest.py
#! python3
# -*- coding: utf-8 -*-
 
 
def testStr(key):
    print("testStr is :", key)
 
$ cat CallGraphTest.py
#! python3
# -*- coding: utf-8 -*-
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
 
import TempTest
 
 
def testNum(key):
    TempTest.testStr(key)
    print("testNum is :", key)
 
 
g = GraphvizOutput(output_file=r'./trace.png')
with PyCallGraph(output=g):
    TempTest.testStr("111")
    testNum(222)
 
$
 
$ py -3 CallGraphTest.py
testStr is : 111
testStr is : 222
testNum is : 222
 
$ ls -l
total 14
drwxr-xr-x 1 guowli 1049089    0 May 23 16:07 __pycache__/
-rwxr-xr-x 1 guowli 1049089  350 May 23 15:56 CallGraphTest.py*
-rwxr-xr-x 1 guowli 1049089   92 May 23 15:59 TempTest.py*
-rw-r--r-- 1 guowli 1049089 9141 May 23 16:07 trace.png
 
$
```
生成指定名称的函数关系图trace.png

