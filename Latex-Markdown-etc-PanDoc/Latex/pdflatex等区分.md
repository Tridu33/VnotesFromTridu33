# pdflatex等区分




**概念：**

  

TeX：一种宏语言。

Plain Tex： Tex中的一个最基本的宏集合与TeX的基础语言构成的一种格式。

LaTex： Tex中的一个宏集合，构成一种与 Plain TeX 不一样的格式。

Tex程序：把Tex语言转换为排版的程序，也叫Tex。为区别，称这个 TeX 程序叫Knuth TeX。

tex命令：Tex程序中的编译命令。tex命令默认用Plain TeX格式进行排版。也就是说tex命令后面默认跟的tex文件应该是用Plain Tex格式写的。

latex命令：tex命令加上某一个选项使用，就会用LaTeX 格式进行排版，也就是说此时后面跟的tex文件应该是用LaTex格式写的。为方便，就把tex 命令与对应编译选项合成为一个命令，叫latex命令。

ε-TeX 程序：Knuth TeX程序的一个扩展，也是一个程序，一般写成 eTeX。增加了少量的几个命令，但一般来说是与Knuth TeX程序没有太多区别的。

实现：在文中的意思就是指“程序”的意思。如文中：eTeX 程序和 Knuth TeX 都是TeX语言的一个实现（也就是说，eTeX 程序和 Knuth TeX 都是把TeX语言转换为排版的程序。程序作用于tex文本文件，把tex文件编译成dvi文件）。

pdfTeX程序：Tex语言的又一个实现，也就是把Tex语言转换为排版的又一个程序。它会把 TeX 语言写的代码直接编译成 PDF 文件。

pdftex命令：pdfTex程序中的命令，用来编译用Plain TeX格式写的tex文件。

pdflatex命令：pdfTex程序中的命令，用来编译用LaTeX格式写的tex文件。

XeTeX程序：TeX语言的新的实现，即把Tex语言转换为排版的一个新程序。支持Unicode 编码和直接访问操作系统字体。

xetex命令：XeTeX程序中的命令，用来编译用Plain TeX格式写的tex文件。

xelatex命令：XeTeX程序中的命令，用来编译用LaTeX格式写的tex文件。

  

**一些解释**

  

pdfLaTeX是比较原始的版本，对Unicode的支持不是很好，所以显示汉字需要使用CJK宏包。它不支持操作系统的truetype字体(*.ttf)，只能使用type1字

体。优点是支持的宏包比较多，有些老一点的宏包必须用pdfLaTeX来编译。

XeLaTeX是新的Unicode版本，内建支持Unicode(UTF-8)，自然也包括汉字在内，而且可以调用操作系统的truetype字体。如果你的文档有汉字，那么推

荐用XeLaTeX。缺点是不支持某一些宏包。



https://blog.csdn.net/chen_shiqiang/article/details/52101836



这里还讲历史：https://blog.csdn.net/henu111/article/details/81239727
