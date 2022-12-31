

awt和swing的区别：

1.awt是基于本地方法的[C/C++](https://www.baidu.com/s?wd=C%2FC%2B%2B&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)程序，其运行速度比较快；

而swing是基于awt的Java程序，其运行速度比较慢。

2.AWT的控件在不同的平台可能表现不同，而Swing在所有平台表现一致。

3.AWT和Swing的实现原理不同。

AWT的图形函数与[操作系统](https://www.baidu.com/s?wd=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)提供的图形函数有着一一对应的关系。

而Swing 不仅提供了AWT 的所有功能，还用纯粹的Java代码对AWT的功能进行了大幅度的扩充。

4.awt是抽象窗口组件工具包，是 java 最早的用于编写图形节目应用程序的开发包；

但swing是为了解决awt存在的问题而新开发的包，它以awt为基础的。

## 扩展资料：

在实际应用中，应该使用AWT还是Swing取决于应用程序所部署的平台类型。

对于一个嵌入式应用，目标平台的硬件资源往往非常有限，而应用程序的运行速度又是项目中至关重要的因素。

在这种矛盾的情况下，简单而高效的AWT当然成了嵌入式Java的第一选择。

在普通的基于PC或者是工作站的标准Java应用中，硬件资源对应用程序所造成的限制往往不是项目中的关键因素。

所以在标准版的Java中则提倡使用Swing， 即通过牺牲速度来实现应用程序的功能。

# 教程
源代码吗看我老师的基本就够了

c.biancheng.net/swing/
















# 知乎资源




https://www.zhihu.com/question/19608871










































