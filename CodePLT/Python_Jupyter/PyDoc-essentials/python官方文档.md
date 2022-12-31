





https://docs.python.org/zh-cn/3/library/typing.html 类型系统

https://docs.python.org/zh-cn/3/library/index.html 标准库 中文文档

对应代码仓库
https://github.com/python/peps






# 1. python官方文档



https://docs.python.org/3/library/index.html

https://docs.python.org/3/index.html





https://docs.python.org/3/tutorial/index.html









中文





https://www.runoob.com/manual/pythontutorial3/docs/html/



https://python3-cookbook.readthedocs.io/zh_CN/latest/preface.html




https://docs.pythontab.com/python/python3.4/introduction.html




python进阶文档


https://docs.pythontab.com/interpy/


流畅的python





源码

https://www.github.com/fluentpython/example-code


第二版

https://github.com/fluentpython/example-code-2e


并发编程python

https://github.com/fluentpython/concurrency2019











python教程文档

[https://pythonspot.com/](https://pythonspot.com/)






# 2. 文档




[https://ipython.readthedocs.io/en/stable/](https://ipython.readthedocs.io/en/stable/)



启动http服务，使用浏览器查看文档：

```
$  pydoc  -b
```


### 2.1.1. inspect

inspect模块可以在运行时帮助我们确定对象类型。对应的函数如下：

-   ismodule()
-   isclass()
-   ismethod()
-   isfunction()
-   isgeneratorfunction()
-   isgenerator()
-   istraceback()
-   isframe()
-   iscode()
-   isbuiltin()
-   isroutine()



使用getmembers()获得对象所有成员：

```
>>>  len(inspect.getmembers(tensorflow))
471
>>>  len(inspect.getmembers(tensorflow,  inspect.isclass))
50

```

使用getdoc获得文档对象：

```
>>>  inspect.getdoc(dict)

"dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"

```

查看inspect帮助：

```
>>>  help(inspect)
```








方法二
在python命令行输入以下内容

print(time.__doc__)               # 较详细的模块文档
print(time.localtime().__doc__)   # 较详细的函数文档
print(range.__doc__)              # 较详细的类的文档
1
2
3
方法三
在python命令行输入以下内容

print(dir(time))                  # 简略的模块函数显示
print(dir(time.localtime()))      # 简略的函数参数显示
print(dir(range))                 # 简略的类构造函数参数显示
————————————————
版权声明：本文为CSDN博主「刘鸿亮」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/csdn_0_001/article/details/79550784


dir()
1.列出模块定义的标识符(类、函数、变量）
  列出对象定义的标识符(函数、变量）
  列出方法定义的标识符(变量）


当你为dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当前模块中定义的名称列表



2.dir的作用:

         定义一个新的变量a并且给它赋一个值，然后检验dir，我们观察到在列表中增加了以上相同的值。我们使用del语句删除当前模块中的变量/属性，这个变化再一次反映在dir的输出中。关于del的一点注释——这个语句在运行后被用来 删除 一个变量/名称。在这个例子中，del a，你将无法再使用变量a——它就好像从来没有存在过一样。
————————————————
版权声明：本文为CSDN博主「Magicbo-_-」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Beiji_Nanji/article/details/7460896






































