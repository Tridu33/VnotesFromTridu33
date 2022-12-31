# jupyter仓库


[https://nbviewer.jupyter.org/](https://nbviewer.jupyter.org/)




[奇淫怪技https://www.zhihu.com/question/266988943](https://www.zhihu.com/question/266988943)

但是，如果你的内容都已经放在Jupyter里了，再重新导入PPT，太麻烦了，我们自动转换吧。

一种方法是用Jupyter内置的PPT选项，依次点击菜单栏里的View → Cell Toolbar → Slideshow，之后每个单元格上面都会有一个灰色的横条，选**Sub-Slide**。

然后输入以下代码：

```python
1 jupyter nbconvert *.ipynb --to slides --post serve
2 # insert your notebook name instead of *.ipynb
```

好了，现在就变成PPT样式的了，显示在端口8000，你也可以查看源代码找到PPT文件。

  
  
作者：量子位  
链接：https://www.zhihu.com/question/266988943/answer/632279672  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





不过，用PyTorch默认方法生成的PPT代码不能编辑，这个时候就要用到**RISE**插件了。

RISE用到reveal.js来运行PPT，可以不退出PPT，直接运行代码。

先来安装RISE，推荐用conda：

```python
1 conda install -c damianavila82 rise
```

其实不太推荐pip：

```python
1 pip install RISE
```

然后调用JS和CSS：

```python
1 jupyter-nbextension install rise --py --sys-prefix
2 #enable the nbextension:
3 jupyter-nbextension enable rise --py --sys-prefix
```

安装好啦，现在重新打开你的Jupyter Notebook，发现一个新的扩展，名叫“Enter/Exit RISE Slideshow”。

![](https://pic4.zhimg.com/50/v2-eebcfdc5660b8c47a74ed4479a3e4fec_hd.jpg)




## **七、嵌入链接和pdf**

扔链接再跳转实在是太麻烦了，不如直接把素材放进Jupyter里面。

### **嵌入链接**

```python
1 #Note that http urls will not be displayed. Only https are allowed inside the Iframe
2 from IPython.display import IFrame
3 IFrame('https://en.wikipedia.org/wiki/HTTPS', width=800, height=450)

```

操作方式如下，当然你需要把链接换成你要放的链接：

  
### **嵌入pdf**

```python
1 from IPython.display import IFrame
2 IFrame('https://arxiv.org/pdf/1406.2661.pdf', width=800, height=450)
```

同样，把pdf链接换成你需要用的pdf。



















