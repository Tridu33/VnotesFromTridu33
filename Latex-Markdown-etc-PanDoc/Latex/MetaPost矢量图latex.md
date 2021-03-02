# MetaPost矢量图latex


TikZ 与 MetaPost 都是代码作图工具，适合画能用坐标表示的精确图形。不过二者也有差别。

MetaPost 脱胎于字体设计语言 MetaFont，其语法可以用相对直观的方式精确描述 Bézier 曲线，又自带语法方便的线性方程求解功能、图形的线性变换功能，因而有很强的二维曲线造型功能；同时又有宏定义、循环、分支等程序结构，可以表达较复杂的数学图形；同时可以插入 TeX 代码的文字、公式。所以用 MetaPost 来画有数学描述的、数值或半数值化的、有 TeX 公式的曲线或直线图是最适合的，在一些已有的宏支持下也适合数据结构图。举个例子的话，比如说，L-system 定义的分形曲线，集合论里面的 Venn 图，正十七边形或五角星，射影几何里面 Desargues 定理的配图，计算机科学中的 B+ 树，都挺合适。
https://www.zhihu.com/question/27332117/answer/36291713
TikZ 是由 TeX 宏编写的宏包，抽象掉底层 pdfTeX 这样的引擎或 Dvips、dvipdfmx 这样的输出驱动来完成实际的绘图工作。在功能上借鉴 PSTricks，在语法上也部分借鉴 MetaPost。由于 TeX 宏本身的限制，TikZ 在曲线造型、数值计算、复杂数据结构组织上，虽然也能做，但效率比较低；优势是开发比较深入，预定义的功能多，能直接用的包比较多，作为宏包与 TeX 结合也最紧密。适合画简单的小符号，数据结构图，计算量不太大的数学图形等。适合做的图形与 MetaPost 有不少重叠的，比如集合论的 Venn 图，正十七边形或五角星，简单流程图，数据结构图；也包括自己独有优势的如数学符号标记，图表标注，数学交换图等。现在在 luatex 的帮助下也能完成一些复杂计算，比如复杂函数图，图可视化。

# LaTeX画矢量图相关（字体、箭头位置、分组）？

我一直在琢磨一篇论文中的图用 LaTex 怎么绘制出来，问题标题不知如何取比较合适，但是我觉得画该图（链接见后文）需要解决的就是内容分组、设置箭头问题、然后是设定字体。




LaTeX画矢量图相关（字体、箭头位置、分组）？ - 知乎 https://www.zhihu.com/question/20143072


1\. 如果看的懂英文的话，建议认真研读手册：  
[https://www.tug.org/docs/metapost/mpman.pdf](https://link.zhihu.com/?target=https%3A//www.tug.org/docs/metapost/mpman.pdf)

  
  

2\. 如果手册研读明白了大部分，继续研读提高篇：  
[http://texdoc.net/texmf-dist/doc/metapost/metaobj/momanual.pdf](https://link.zhihu.com/?target=http%3A//texdoc.net/texmf-dist/doc/metapost/metaobj/momanual.pdf)

  

3\. 有了上面两篇文档作为基础，之后可以查看实例：  
[http://tex.loria.fr/prod-graph/zoonekynd/metapost/metapost.html](https://link.zhihu.com/?target=http%3A//tex.loria.fr/prod-graph/zoonekynd/metapost/metapost.html)

  

三步走后，基本上就得心应手了！

最后强调一下：一定要亲自去敲键盘！哪怕是被认为很简单的问题！










www.tug.org/metapost.html





www.ctex.org/documents/shredder/metapost.html




https://www.latexstudio.net/archives/category/tex-graphics/metapost-example



科学网还有一个博文：MetaPost介绍 （[http://blog.sciencenet.cn/blog-267716-575504.html](http://blog.sciencenet.cn/blog-267716-575504.html)）

MetaPost是一个矢量制图语言。

MetaPost介绍: 

[http://www.berlinix.com/MetaPost.html](http://www.berlinix.com/MetaPost.html)

在线制图

[http://www.tlhiv.org/mppreview/](http://www.tlhiv.org/mppreview/)

MetaPost示例大全

[http://tex.loria.fr/prod-graph/zoonekynd/metapost/metapost.html](http://tex.loria.fr/prod-graph/zoonekynd/metapost/metapost.html)

王垠的MetaPost介绍

[http://docs.huihoo.com/homepage/shredderyin/metapost.html](http://docs.huihoo.com/homepage/shredderyin/metapost.html)
















































































































































