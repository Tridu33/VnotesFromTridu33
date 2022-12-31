







# 1. python生成DOT文件dot

- [pygraphviz](https://pypi.org/project/pygraphviz/) – full-blown interface wrapping the Graphviz C library with SWIG
PyGraphviz 是 Graphviz 图形布局和可视化包的 Python 接口。借助 PyGraphviz，您可以使用 Python 创建、编辑、读取、写入和绘制图形，以访问 Graphviz 图形数据结构和布局算法。PyGraphviz 提供了与 NetworkX 类似的编程接口（https://networkx.org）。
网站（包括文档）： https : //pygraphviz.github.io


- [graphviz-python](https://pypi.org/project/graphviz-python/) – official Python bindings ([documentation](https://www.graphviz.org/pdf/gv.3python.pdf))
- [pydot](https://pypi.org/project/pydot/) – stable pure-Python approach, requires pyparsing
是Graphviz的接口
可以解析并转储为GraphViz 使用的DOT 语言，
是用纯 Python 编写的，
并且networkx可以将其图形转换为pydot. https://github.com/pydot/pydot

- [graphviz](https://pypi.org/project/graphviz/)  使用Python中的Graphviz图形绘制软件（主存储库）的DOT语言创建和呈现图形描述。创建一个图形对象，通过添加节点和边来组装图形，并检索其 DOT 源代码字符串。将源代码保存到一个文件中，并使用系统的 Graphviz 安装来呈现它。


anytree专门做树相关的包：https://anytree.readthedocs.io/en/latest/dotexport.html




















































































一个sklearn案例：


Python可视化决策树【Matplotlib/Graphviz】


```
from sklearn import tree
tree.plot_tree(clf,
               feature_names = fn, 
               class_names=cn,
               filled = True);


tree.export_graphviz(clf,
                     out_file="tree.dot",
                     feature_names = fn, 
                     class_names=cn,
                     filled = True)
```
















