




# 1. doxygen + doxypypy + docstring 生成python文档


原生的docstring和类似java doc风格的##


```python
"""@package docstring
Documentation for this module.
More details.
"""
 
def func():
    """Documentation for a function.
    More details.
    """
    pass
```
可惜的是，对原生的docstring，在函数多行定义的时候，不仅经常提取不到注释，而且即使提取到注释，也不支持各种注释tag，如@param，@see等。


javadoc-like

对java doc风格的##，虽然支持较好，可惜的是偶使用的是pydev做IDE工具的，pydev显示函数注释信息总是错位的，提取的是下一个函数的注释。

```python
## Documentation for a function.
#
#  More details.
def func():
    pass
```







https://github.com/Feneric/doxypypy



doxygen的input filter的功能，简单一句话描述就是一个文本的预处理。当你定义了input filter之后，doxygen在生成文档时就不会直接读取文件内容，而是先调用input filter处理文件内容，然后将处理结果作为doxygen自己的输入。

再简单介绍一下doxypypy这个工具的工作原理：简单来说就是先提取出docstring，然后去掉docstring开头和结尾的""", 然后插入##作为第一行，再在其余各行注释前面加上#，这样就很简单巧妙的转换为类java doc的##风格了。将转换后的结果作为doxygen的输入，就可以制作出漂亮的文档了。

https://blog.csdn.net/crylearner/article/details/38798455





