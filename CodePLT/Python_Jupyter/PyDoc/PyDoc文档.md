[TOC]

# PyDoc文档






[https://cloud.tencent.com/developer/section/1367570](https://cloud.tencent.com/developer/section/1367570)


`pydoc`模块自动从Python模块生成文档。文档可以作为控制台上的文本页面呈现，提供给Web浏览器或保存到HTML文件。

[纠错](javascript:;)

对于模块，类，函数和方法，所显示的文档是从对象的docstring（即`__doc__`属性）派生的，并且是对其可记录成员的递归派生。如果没有文档字符串，则`pydoc`尝试从源文件中的类，函数或方法的定义上方或模块的顶部（请参阅参考资料）中的注释行块获取说明`inspect.getcomments()`。

























