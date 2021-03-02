# makrdown2beamer



 [使用Markdown+Pandoc+LaTex+Beamer制作幻灯片](https://www.cnblogs.com/aquastone/p/markdown_slide.html)



```
texdoc beamer
```

帮助

## 利用Pandoc甚至可以直接实现Markdown到Beamer的转换！

利用这个方法，甚至不需要复制粘贴的重复，一行命令直接实现幻灯片的制作：  
1\. 安装pandoc,并且让它支持中文，可以这么做：

```text
brew install pandoc
```

-   导出pandoc自动转换时的用到的模版文件

```text
pandoc -D beamer > template.tex
```

-   在模版文件中添加 \\XeTeXlinebreaklocale "zh"，这个命令用于在中文下实现自动换行

```text
$if(mathfont)$     
    \setmathfont(Digits,Latin,Greek)
    [$for(mathfontoptions)$$mathfontoptions$$sep$,$endfor$]{$mathfont$} 
$endif$  
\XeTeXlinebreaklocale "zh"
```

-   命令行转换！完成！

```text
pandoc -t beamer 
--latex-engine=xelatex 
--template=template.tex 
-V mainfont='STHeiti'  
/Users/zz/Desktop/Diary/xxxx.md -o xxxx.pdf 
```

不过，第二个方法有一个缺点，公式和图片太多的时候，很容易出错。我的笔记里数学公式和图片很多，就不适合这个方法了。


Beamer——基于LaTex的Slides制作 - 郑哲的文章 - 知乎
https://zhuanlan.zhihu.com/p/132750772























