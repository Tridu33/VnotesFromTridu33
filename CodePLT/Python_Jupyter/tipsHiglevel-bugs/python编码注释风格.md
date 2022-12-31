
```
私有变量：实例._类名__变量名
私有方法：实例._类名__方法名()

_xxx 单下划线修饰的成员变量，表示只有类实例或者子类实例可以访问，类似于protect
__xxx 双下划线修饰的成员变量，表示只有类对象自己能访问，类似于private
__xxx__ 系统定义名字，表示特殊方法专用的标识，如__init__()，代表类的构造方法
```



PEP 0257中对docstring的定义：

> A docstring is a string literal that occurs as the first statement in 
a module, function, class, or method definition. Such a docstring 
becomes the __doc__ special attribute of that object.

简单来说，就是出现在模块、函数、类、方法里第一个语句的，就是docstring。会自动变成属性__doc__。
可通过foo.__doc__访问得到






# 1. python注释风格




https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/

确保对模块, 函数, 方法和行内注释使用正确的风格
文档字符串应该包含函数做什么, 以及输入和输出的详细描述. 

- 文档字符串

Python有一种独一无二的的注释方式: 使用文档字符串. 文档字符串是包, 模块, 类或函数里的第一个语句. 这些字符串可以通过对象的__doc__成员被自动提取, 并且被pydoc所用. (你可以在你的模块上运行pydoc试一把, 看看它长什么样). 
对文档字符串的惯例是使用三重双引号”“”( PEP-257 ). 一个文档字符串应该这样组织: 

首先是一行以句号, 问号或惊叹号结尾的概述(或者该文档字符串单纯只有一行). 接着是一个空行. 接着是文档字符串剩下的部分, 它应该与文档字符串的第一行的第一个引号对齐. 


下面有更多文档字符串的格式化规范.

```python
def Foo(object):
    """
    Args:
        列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.
        如果描述太长超过了单行80字符,使用2或者4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 
        如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar.

    Returns: (或者 Yields: 用于生成器)
        描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.

    Raises:
        列出与接口有关的所有异常.
    """
    pass
```







- 模块


每个文件应该包含一个许可licenses. 根据项目使用的许可(例如, Apache 2.0, BSD, LGPL, GPL), 选择合适的证书.


- 函数-方法

下文所指的函数,包括函数, 方法, 以及生成器.

一个函数必须要有文档字符串, 除非它满足以下条件:

外部不可见\_\_inner\_function\_private
非常短小lambda matched:print("hello")
简单明了


通常, 不应该描述”怎么做”, 除非是一些复杂的算法. 文档字符串应该提供足够的信息, 当别人编写代码调用该函数时, 他不需要看一行代码, 只要看文档字符串就可以了. 对于复杂的代码, 在代码旁边加注释会比使用文档字符串更有意义.


```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```

- 类

类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.


```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```




- 块注释和行注释

最需要写注释的是代码中那些技巧性的部分. 如果你在下次 代码审查 的时候必须解释一下, 那么你应该现在就给它写注释. 

对于复杂的操作, 应该在其操作开始前写上若干行注释. 

对于不是一目了然的代码, 应在其行尾添加注释.


```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:        # True if i is 0 or a power of 2.
```


为了提高可读性, 注释应该至少离开代码2个空格.

另一方面, 绝不要描述代码. 假设阅读代码的人比你更懂Python, 他只是不知道你的代码要做什么.

```python
# BAD COMMENT: Now go through the b array and make sure whenever i occurs
# the next element is i+1
```









Google风格 https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/ 








































