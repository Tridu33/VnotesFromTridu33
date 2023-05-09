# 博客中显示如何拷贝jupyter notebook中markdown




blog.csdn.net/hello_zybwl/article/details/87579106




jupyter notebook编写的以`.ipynb`导出的md文件并不能在csdn中良好的显示，故借助如下方法。

1 . github上上传自己的`*.ipynb`，记住该地址，例如：

> [https://github.com/lsh1994/CodeShare/blob/master/blog/opencv-python2.ipynb](https://github.com/lsh1994/CodeShare/blob/master/blog/opencv-python2.ipynb)

2 在[http://nbviewer.jupyter.org/](http://nbviewer.jupyter.org/) 上输入如上网址，回车获取新的地址。如：

> [http://nbviewer.jupyter.org/github/lsh1994/CodeShare/blob/master/blog/opencv-python2.ipynb](http://nbviewer.jupyter.org/github/lsh1994/CodeShare/blob/master/blog/opencv-python2.ipynb)

也可以根据如上网址组合成 步骤2 形式

3 . 在csdn md的编写状态合适位置处填写步骤2 网址，如下：

```
<iframe src="步骤2的网址" width="100%" height="1000"></iframe>
```




























