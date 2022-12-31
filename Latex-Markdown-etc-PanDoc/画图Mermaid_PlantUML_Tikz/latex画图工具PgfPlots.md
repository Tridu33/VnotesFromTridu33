# latex画图工具PgfPlots







LaTeX下面如何画图：[http://pgfplots.sourceforge.net/pgfplots.pdf](http://pgfplots.sourceforge.net/pgfplots.pdf)

其实用jpg或者png转换为eps文件并不是很靠谱的方法。因为不管如何转换，放大的时候图片还是会有瑕疵。那么，LaTeX是否有自己的作图工具呢？那就是著名的PgfPlots了（[http://pgfplots.sourceforge.net/](http://pgfplots.sourceforge.net/)）！这个工具可以在LaTeX中直接绘制高清晰的图表。有多炫呢？比如二维图像（左边是图，右边是代码，图片截取自PgfPlots官方手册）：  

![](https://pic4.zhimg.com/80/4ba16f4368884a28da7a2a41a49b1dc4_1440w.jpg?source=1940ef5c)

甚至三维图像：

![](https://pic3.zhimg.com/80/39f4d9def315cc16346497b472cd84cb_1440w.jpg?source=1940ef5c)

实际上，对于绝大多数Computer Science相关的论文来说，用PgfPlot画图会让审稿人觉得更专业，而且由于图像中的数据必须嵌套在tex文件之中，审稿人会更确信作者是真实进行了实验，数据也是真实的。

不过这个工具用起来有一点复杂，毕竟图像涉及到的内容太多了。最上方的链接是官方说明文档，大家画图的时候可以从目录里面找最接近的例子，然后改改就好了。另外，这个工具是Windows下CTEX自动支持的哦。












