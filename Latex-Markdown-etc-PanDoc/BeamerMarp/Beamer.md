[TOC]

# Beamer

https://github.com/SunYanCN/Latex-Beamer-Template

-   [LaTeX制作Beamer(一)](https://zhuanlan.zhihu.com/p/36868831)
-   [LaTeX制作Beamer(二)](https://zhuanlan.zhihu.com/p/39177705)

CTeX 中文 beamer 模板 https://blog.csdn.net/xueshengke/article/details/53045880


如何找到好看的模板：

https://www.overleaf.com/gallery/tagged/presentation#.Wv7RVIiFPIU

https://github.com/martinbjeldbak/ultimate-beamer-theme-list

https://hartwork.org/beamer-theme-matrix/

有什么好的beamer主题和配色方案？ - Dwzb的回答 - 知乎 https://www.zhihu.com/question/29676847/answer/396667384

https://github.com/zbowang/BeamerTheme


> texdoc beamer



# 利用Pandoc甚至可以直接实现Markdown到Beamer的转换！


Beamer——基于LaTex的Slides制作 - 郑哲的文章 - 知乎 https://zhuanlan.zhihu.com/p/132750772




























## latex 语法

正如 latex 的特点，不必过于关心排版问题，幻灯片中可以方便编写公式（equation），（规范）引用参考文献（bibtex），导入矢量图片，特别是在学术用途的展示会议上，虽然上手比 powerpoint 难，但是却比 powerpoint 方便许多，制作出的幻灯片没有很花哨的效果，但也是非常美观大方。

## 中文支持

因为是国外开发的工具，所以对中文的支持一向不友好。但是经过了程序员们辛苦的努力， 已经可以直接制作编辑带中文的 beamer 幻灯片，并且兼容性相当不错。之前一直想找一种解决方案，在幻灯片中加入中文；也尝试了几种方法，但是本文给出的方案（CJKutf8+pdflatex）最方便、稳定。

## DIY 设计

可以根据自己的喜好设计不同风格的 beamer 文档，本人为了以后用于学术用途的展示，准备了一个专用的模板文件，代码共享给读者，如果需要下载完整的工程，可以转到 [Github](https://github.com/xueshengke/ISEE-template "Github") 下载全部文件。

### 公式字体

```latex
\documentclass[10pt, mathserif]{beamer} % font and size
```

这里设置的是文字的大小和英文公式的字体，为了公式更美观，个人觉得 serif 最合适，在下方的图片中可以看出。

### 半透明显示

```latex
\setbeamercovered{dynamic}  % translucent when using pause
```

使用 translucent，可以在 \\pause 使用时将其之后的内容变为半透明显示，演示者自己可以看到，但是又能体现出分步展示的层次感。

### 隐藏导航栏

```latex
\setbeamertemplate{navigation symbols}{}    % hide navigation bars
```

beamer 默认在右下角显示导航栏，但是一般情况用处不大，可以使用这个命令隐藏；如果需要，注释此句即可。

### 背景图片

```latex
\setbeamertemplate{background}{\includegraphics[height=\paperheight]{ISEE.pdf}} 
```

beamer 默认没有背景图片，可以自己添加一些特殊的图片作为背景。

### 页码

```latex
\setbeamertemplate{footline}{\footnotesize \insertframenumber/\inserttotalframenumber \hfill}   
```

beamer 默认没有页码显示，在演示时有时候需要把握进度，添加页码便于查看，是一种很好的提醒方式。可以在页面的左下角的位置添加，又不影响美观。

### 中文字体

```latex
\usepackage{CJKutf8}
\usepackage{times}  
...
\begin{document}
\begin{CJK}{UTF8}{song}	
...
\end{CJK}
\end{document}
```

beamer 默认没有中文支持，所以需要添加额外的包 CJKutf8（[CTeX](http://www.ctex.org/HomePage "CTeX") 安装包自带），在 begin{document} 之后 和 end{document} 之前加上两句话，指定中文使用 UTF-8 编码，字体为宋体；英文则使用 Times New Roman 字体显示，比较适合显示。

### 中文书签

```latex
\usepackage{hyperref}
\hypersetup{bookmarks, unicode}
```

beamer 加入中文还需注意，中文一旦出现在书签中，需要额外加命令设置，编码为 unicode；否则会在书签中出现乱码。













Beamer主题预览：
https://deic-web.uab.cat/~iblanes/beamer_gallery/index.html


























































































































