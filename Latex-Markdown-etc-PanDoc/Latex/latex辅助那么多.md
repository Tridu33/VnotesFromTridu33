# latex辅助那么多



https://www.zhihu.com/question/20585795/answer/347493222



字体识别（仅英文） [https://www.myfonts.com/WhatTheFont/](https://link.zhihu.com/?target=https%3A//www.myfonts.com/WhatTheFont/)

查看字号搭配效果 [https://type-scale.com/](https://link.zhihu.com/?target=https%3A//type-scale.com/)；[https://www.modularscale.com/](https://link.zhihu.com/?target=https%3A//www.modularscale.com/)

设计相关小游戏，对了解TeX基本原理很有帮助 [https://method.ac/](https://link.zhihu.com/?target=https%3A//method.ac/)

TexFriend 这是孙文昌开发的插件，非常好用，输入字符，数学公式示例，表格示例等等；

BibLaTeX 插入参考文献（是时候放弃 BibTeX 了）；

JabRef 管理参考文献

BibDesk ([BibDesk](https://link.zhihu.com/?target=https%3A//bibdesk.sourceforge.io/)) 管理参考文献（Mac only）

Detexify ([http://detexify.kirelabs.org/classify.html](https://link.zhihu.com/?target=http%3A//detexify.kirelabs.org/classify.html)) 的伙伴 shapecatcher（[Draw the Unicode character you want!](https://link.zhihu.com/?target=http%3A//shapecatcher.com/)）;

LaTeX 表格生成 （[http://www.tablesgenerator.com/latex_tables](https://link.zhihu.com/?target=http%3A//www.tablesgenerator.com/latex_tables)）；

LaTeX 数学公式的好帮手 （[http://webdemo.myscript.com/](https://link.zhihu.com/?target=http%3A//webdemo.myscript.com/)）；

数学公式编辑 AxMath ([AxSoft - Axmath equation editor, AxGlyph vector graph editor](https://link.zhihu.com/?target=https%3A//www.axsoft.co/))

另一个LaTeX 数学公式输入辅助工具 （[MathType demo - For Developers](https://link.zhihu.com/?target=http%3A//www.wiris.com/editor/demo/en/developers%23mathml-latex)）；

mathpix 复制公式得到代码，配合equation sheet简直不能更好（[convert images to LaTex.](https://link.zhihu.com/?target=https%3A//mathpix.com/)）；

Excel2LaTeX （[Package Excel2LaTeX](https://link.zhihu.com/?target=https%3A//www.ctan.org/pkg/excel2latex)）;

LaTeX Workshop 可以将 MS 的 visual studio code 配置为 LaTeX 编辑器；

生成随机英文我们有很多选择，但有时候我们需要大量的随机中文来测试代码/模板，此时可以在 Word 中使用公式“”=rand(x, y)“”，详情参考百度经验 [https://jingyan.baidu.com/article/84b4f565ca48f960f6da32e2.html](https://link.zhihu.com/?target=https%3A//jingyan.baidu.com/article/84b4f565ca48f960f6da32e2.html)；

KtikZ tikZ编辑器，避免反复编译，节省时间；

[KtikZ - Editor for the TikZ language​www.hackenberger.at](https://link.zhihu.com/?target=http%3A//www.hackenberger.at/blog/ktikz-editor-for-the-tikz-language/)

[https://github.com/fhackenberger/ktikz​github.com](https://link.zhihu.com/?target=https%3A//github.com/fhackenberger/ktikz)


[https://www.mathcha.io/​www.mathcha.io](https://link.zhihu.com/?target=https%3A//www.mathcha.io/)

不建议使用：

BaKoMa

LyX

Pandoc (a universal document converter)




作者：Clerk Ma  
链接：https://www.zhihu.com/question/20585795/answer/15575381  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

Ghostscript是一个PostScript以及PDF/PDL语言的解释器。这个软件没有我们常常用到的GUI窗口，只有在看ps文件或者pdf文件的时候会产生GUI输出（所以我就在上面贴了个Ghostscript的logo...）。Ghostscript在很多Linux/BSD平台下都有，Mac OS X下的版本则包含在TeX Live中，Windows版本分为32位的和64位的。

Ghostscript现在最大的用途是来转换eps/ps/pdf文件的。TeX Live下面很多处理pdf/eps的工具就是在后台调用了Ghostscript。上面的logo就是使用Ghostscript生成的png图片（原始文件为Ghost.eps）。在转换前，打开终端或者cmd，输入：  

> **gswin32 -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -dEPSCrop -r300 -sOutputFile=a.png Ghost.eps**

  
我这个是在Windows下运行的，如果是其他平台，可将gswin32换成gs执行。这个命令实际上只有后五个参数是有用的。-sDEVICE是输出形式，我们选择了png16m则会生成png图片，如果改为pdfwrite则会生成pdf文件，即为：  

> **gswin32 -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dEPSCrop -sOutputFile=Ghost.pdf Ghost.eps**

回到第一个例子上来，-dEPSCrop是处理EPS文件的，是将EPS进行裁剪进行输出，类似的EPS处理选项还有-dEPSFitPage，这个是将EPS处理成适合如A4页面大小等的选项。

-r300是指的输出的分辨率，可以调低，如-r72就调成72了。另外还有有反锯齿的选项-dTextAlphaBits和-dGraphicsAlphaBits，和两个选项可以填选1、2、4这三个值，如-dTextAlphaBits=4，值越大，效果越好。

-oOutputFile指的是生成的文件名。最后一项是Ghost.eps，其实也可以是以ps或者pdf文件名结尾的文件。

Ghostscript可以在某些情况下来当作阅读器，比如我在Gentoo下没有安装Evince的情况。。Ghostscript读取pdf文件的速度略微慢些，但是处理某些非嵌入字体pdf文件的时候会非常正确，很少会遇到问题。Ghostscript最大的长处还是在ps/eps文件的处理上，使用LaTeX插图用eps文件的很多，处理eps文件基本上是每天都要做的工作，能掌握一点Ghostscript会舒服很多。






















