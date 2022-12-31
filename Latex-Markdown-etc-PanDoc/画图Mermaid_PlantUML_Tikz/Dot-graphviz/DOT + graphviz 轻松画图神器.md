

```
dot -Tpng -o hello.png tmp.dot
```
[文档 https://graphviz.org/documentation/](https://graphviz.org/documentation/)




Graphviz 画图的一些总结  https://www.cnblogs.com/shuqin/p/11897207.html#vsc




[dot命令生成流程图](https://blog.csdn.net/ac_dao_di/article/details/57427609)

https://graphviz.org/doc/info/lang.html


```
digraph G {
# 定义全局属性
    fontname = "Courier New"
    fontsize = 8
    # 从下往上
    rankdir = BT
# 定义节点属性
    node [
            shape = "record" # 矩形，默认是椭圆
            color = "blue" # 边框蓝色
    ]

# 定义边的属性
    edge [
            fontsize = 9
    ]
# 换行符是\l，而要新建一个新的单元格，则需要是用|。{}里面的是内容
    Reportable [
	    label = "{Reportable | + getSummary() : Map\<String, Integer\> | + getDetail() : Map\<String, Integer\> | + isDetailVisible() : boolean}"
    ]
# 特殊字符要转义
    LineCounter [
	    label = "{LineCounter | + count(String line) : boolean | + getType() : String}"
    ]

    CharCounter [
	    label = "{CharCounter | + count(Character c) : boolean | + getType() : String}"
    ]

   AbstractCharCounter [
	    label = "{AbstractCharCounter | characterMap : Map\<Character, Integer\> | + count(Character c) : boolean | + getSummary() : Map\<String, Integer\> | +getDetail() : Map\<String, Integer\> }"
    ]
   
   AbstractLineCounter [
	    label = "{AbstractLineCounter |  + count(String line) : boolean | + getSummary() : Map\<String, Integer\> | +getDetail() : Map\<String, Integer\> }"
    ]

   PredicateCharacter[label = "{Predicate\<Character\> | + apply(Character c) : boolean}"]
   PredicateString[label = "{Predicate\<String\> | + apply(String line) : boolean}"]

   BlankCharCounter[label = "{BlankCharCounter | + apply(Character c) : boolean | + getType() : String | + isDetailVisible() : boolean }"]
   ChineseCharCounter[label = "{ChineseCharCounter | - chinesePattern : Pattern | + apply(Character c) : boolean | + getType() : String | + isDetailVisible() : boolean }"]
   LetterCharCounter[label = "{LetterCharCounter | - chinesePattern : Pattern | + apply(Character c) : boolean | + getType() : String | + isDetailVisible() : boolean }"]
    NumberCharCounter[label = "{NumberCharCounter | + apply(Character c) : boolean | + getType() : String | + isDetailVisible() : boolean }"]
    LineNumberCounter[label = "{LineNumberCounter | + apply(Character c) : boolean | + getType() : String | + isDetailVisible() : boolean }"]
   

    parentInterface [label = "parent interface" color = "green" style=filled]
    childInterface [label = "child interface" color = "green" style=filled]
    abstractClass [ label = "abstract class : implement some methods using the abstract methods" color = "green" style=filled]
    specificClass [ label = "specific class : implement all unimplemented methods" color = "green" style=filled]

    LineProcessor [label = "{LineProcessor\<List\<Reportable\>\>}" ]
    ReportableLineProcessor [ label = "{ReportableLineProcessor | + ReportableLineProcessor() | + processsLine(String line) : boolean | + getResult() : List\<Reportable\>}"]

    # 定义在同一层
    {rank = same; parentInterface; Reportable; LineProcessor}
    {rank = same; childInterface; LineCounter; CharCounter; PredicateCharacter; PredicateString}
    {rank = same; abstractClass; AbstractLineCounter; AbstractCharCounter;}
    {rank = same; specificClass; LineNumberCounter; BlankCharCounter; ChineseCharCounter; LetterCharCounter; NumberCharCounter; ReportableLineProcessor}
    
   # 箭头为空心，接口之间的继承
   LineCounter -> Reportable[arrowhead="empty"]
   CharCounter -> Reportable[arrowhead="empty"]
   AbstractCharCounter -> CharCounter[arrowhead="empty"]
   AbstractLineCounter -> LineCounter[arrowhead="empty"]

   AbstractCharCounter -> PredicateCharacter[arrowhead="empty"]
   AbstractLineCounter -> PredicateString[arrowhead="empty"]

   # 实现类的UML
   BlankCharCounter -> AbstractCharCounter[arrowhead="empty", style="dashed"]
   ChineseCharCounter -> AbstractCharCounter[arrowhead="empty", style="dashed"]
   LetterCharCounter -> AbstractCharCounter[arrowhead="empty", style="dashed"]
   NumberCharCounter -> AbstractCharCounter[arrowhead="empty", style="dashed"]
   LineNumberCounter -> AbstractLineCounter[arrowhead="empty", style="dashed"]

   ReportableLineProcessor -> LineProcessor[arrowhead="empty", style="dashed"]
  
}

```




```

digraph otherOp{
        node [
            shape = "record"
            color = "blue"
    	]
	edge[
	    arrowhead = "empty"
	]
	
	// 子图，必须以cluster开头
	subgraph cluster0{
		// 子图用浅灰色填充
		style = filled
		color = lightgray
		// 子图名字
		label = "web server"
		// 制定整个client_socket填充，且填充的颜色为red，这时边缘是蓝色。不指定颜色，则会用上面的边缘颜色blue填充，导致无法看到边缘。
        	// 这里使用s0,s1...占位符号
		client_socket [label = "{<s0>|<s1>head|<s2>|<s3>...|<s4>|<s5>tail|<s6>}" style = "filled" fillcolor = "red"]

       		// 指定边上的文字
		master_thread -> client_socket : s1[label = "produce socket"]

		worker_thread [label = "{<w0> worker_thread 1| <w1> worker_thread 2 | <w2>worker_thread 3}"]
		client_socket : s5 -> worker_thread : w0
        	client_socket : s4 -> worker_thread : w1 [ label = "consume socket"]
        	client_socket : s3 -> worker_thread : w2
  	
		producer[ label = "producer" style = filled fillcolor = "green"]
		consumer[ label = "comsumer" style = filled fillcolor = "green"]
		Queue[ label = "Queue" style = filled fillcolor = "green"]
		{rank = same; producer; master_thread}
		{rank = same; consumer; worker_thread}
		{rank = same; Queue; client_socket}
	}

	request1 -> master_thread[color = "red"]
	request2 -> master_thread[color = "red"]
	request3 -> master_thread[color = "red"]
	// 边是虚线，且是橙色
	request1 -> worker_thread : w0 [ style = "dashed" color = "orange", label = "process request"]
	request2 -> worker_thread : w1 [ style = "dashed" color = "orange" label = "process request"]
	request3 -> worker_thread : w2 [ style = "dashed" color = "orange" label = "process request"]

        Browser[ label = "Browser" style = filled fillcolor = "green"]
	{rank = same; Browser; request1; request2; request3}

}


```



----------------------------------------------------









graphviz,dot,及dot图可视化




dot图可视化pydotplus









```
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO
from sklearn import tree
import os
import pydotplus
from IPython.display import Image
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
dot_data = StringIO()
tree.export_graphviz(clf)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')
```




scikitlearn的决策树方法时候，会产生一个dot格式的文件来表示最终的结果,这个dot树可视化,pydotplus可以
https://www.jianshu.com/p/1733b994d7a7















-------------------------------------------------------------------------------------------------------

[DOT + graphviz 轻松画图神器](https://blog.csdn.net/stormdpzh/article/details/14648827)

1. dot

DOT是一种文本图形描述语言。DOT语言文件通常具有.gv或是.dot的文件扩展名。当然，在编写好.dot或者.gv的文件之后，需要有专门的程序处理这些文件并将其渲染成为图片，dot就是其中一款程序，它可以将DOT语言描述的图形渲染成.png、.jpg、.pdf等多种类型。
    当然，作为工具，dot本身是很原始的，就像gcc之于c代码，g++之于cpp代码一样，或许某些程序员会热衷于在终端使用这些工具，但也有很多人喜欢交互式的界面，所以就有了gvedit之类的工具，它提供交互式的窗口来使用dot等工具渲染DOT语言描述的图形。

2. graphviz
    graphviz是一个开源软件包，上述dot和gvedit等工具都在该软件包中。
    所以，不妨简单的认为DOT是一门图形描述语言而graphviz是处理该语言文件的一个集成化的工具。

很多程序都可以处理DOT文件。其中的一些，例如dot，neato，twopi，circo, fdp与sfdp，会读取DOT文件并将之渲染成为图形格式。其它的一些，比如gvpr，gc，accyclic，ccomps，sccmap和tred，可以读取DOT文件并对它代表的图形进行一些处理。类似于GVedit，lefty，dotty和grappa则提供了交互式的界面。以上程序大部分都包括在了Graphviz软件包中。
https://zh.wikipedia.org/wiki/DOT%E8%AF%AD%E8%A8%80






gvedit.exe



## 1. SVG2DOT








https://convertio.co/zh/svg-dot/

online


















































































