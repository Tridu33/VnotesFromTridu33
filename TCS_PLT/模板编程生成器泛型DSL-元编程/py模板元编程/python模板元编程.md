Python实现模板引擎 - Wayne Shi的文章 - 知乎
https://zhuanlan.zhihu.com/p/21766621
字符串可以通过format函数将数据代入，而模板将format的功能进行了扩展，它可以支持条件判断与循环等逻辑，因此模版也可以看作是format的高级版吧。


这个py文件的生成，有2种方式。



1，直接用代码写

f.write
写出文件的所有内容。

2，使用模板文件，复制这个模板文件。
将相似度很高的代码写模板文件（widget_template.txt）

首先写模板文件，然后打开模板文件，对模板进行字符串格式化处理，最后再将格式化后的字符串保存到新的文件里面。

https://my.oschina.net/yangch/blog/492099








只做一点点修改

比如模板文件里面的类是

class Template

那么新生成的文件里面，类名就做一下修改。

class filename

类名是文件名，首字母大写


# 1. python模板元编程



```python
"""

使用命令行

create.py abc
那么就生成
abc.py

1,abc.py是在create.py里面写的

2，abc.py是根据模板创建的

"""

import sys
import re


list1=sys.argv

while True:
    if len(list1)==1:
        print("请输入参数")
        break
    if len(list1)==2:#刚好获取了参数
        filename=list1[1]+".py"
        print("你要创建的文件是",filename)
        """在本文件里面创建
        with open(filename,"w") as f:
            f.write("import os ")
            f.write("\n")
            f.write("print('hello world')")
        """
        #根据模板创建，相当于复制文件

        with open('template.py','r',encoding="utf-8") as f:
            text=f.read()
        #找到类名，然后做替换
        # class Template(

        
        #字符串替换，正则表达式的熟练程度

        filename2=filename.replace('.py','')
        print(filename2)
        text=text.replace('Template',filename2.capitalize())#替换成文件名abc.py取出.py前面的东西

        
        

        

        with open(filename,'w',encoding="utf-8") as f:
            f.write(text)
        print("文件创建成功")

        
        break
    if len(list1)>2:
        print("只能带1个参数")
        break
```








# 2. python 代码自动生成的方法 （代码生成器）

https://www.cnblogs.com/me115/p/3867382.html














