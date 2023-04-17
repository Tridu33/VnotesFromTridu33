# 1. Python - 使用objgraph生成对象引用关系图




```
$ ls -l
total 1
-rwxr-xr-x 1 guowli 1049089 143 May 23 16:54 TempTest.py*
 
$ cat TempTest.py
#! python3
# -*- coding: utf-8 -*-
import objgraph
 
x = []
y = [x, [x], dict(x=x)]
objgraph.show_refs([y], filename='sample-graph.png')
 
$ py -3 TempTest.py
Graph written to C:\Users\guowli\AppData\Local\Temp\objgraph-i96a8ww9.dot (4 nodes)
Image generated as sample-graph.png
 
$ ls -l
total 13
-rw-r--r-- 1 guowli 1049089 10398 May 23 16:56 sample-graph.png
-rwxr-xr-x 1 guowli 1049089   143 May 23 16:54 TempTest.py*
```
















