# miklatex+latexmaker























最后，对LatexTool的配置文件进行配置，主要是将对应的位置的路径改为自己的安装路径：

    "windows": {
    // For TeXlive 2011 (or other years) use
      "texpath" : "E:\\Program Files\\texlive\\2016\\bin\\win32;$PATH",
    // TeX distro: "miktex" or "texlive"
    "distro" : "texlive",
    // Command to invoke Sumatra. If blank, "SumatraPDF.exe" is used (it has to be on your PATH)
    "sumatra": "E:\\Program Files\\SumatraPDF\\SumatraPDF.exe"
    },

到此，windows下的latex环境配置完成。
 
--------------------- 
作者：Chaos_92 
来源：CSDN 
原文：https://blog.csdn.net/sjtu_mc/article/details/79111368 
版权声明：本文为博主原创文章，转载请附上博文链接！









这种方式参考文献按照期刊规定的格式直接写在.tex文件中，在引用处直接\cite{}该文件。 
另一种我比较熟悉的引用方式是把参考文献写在.bib文件中，然后和.tex放在同一文件夹下，.tex直接引用.bib中的参考文献。这种方法比较简单，不需要你根据期刊的格式每个都改动，只需要你找到相关的文件，按照Bibtex格式放到.bib文件中，在tex文件中会按照指定的参考文献格式现实。接下来就介绍这种方法：

1. 首先从google学术或者百度学术上找到参考文采用，然后引用->Bibtex，就会显示如下格式：

@article{Sniffen1992A, 
  title={A net carbohydrate and protein system for evaluating cattle diets: II. Carbohydrate and protein availability.}, 
  author={Sniffen, C. J. and O’Connor, J. D. and Van Soest, P. J. and Fox, D. G. and Russell, J. B.}, 
  journal={Journal of Animal Science}, 
  volume={70}, 
  number={11}, 
  pages={3562-77}, 
  year={1992}, 
} 
解释如下： 
@article{name1, 
title = {标题}, 
author = {作者, 多个作者用 and 连接}, 
journal = {期刊名}, 
volume = {卷20}, 
number = {页码}, 
pages={}, 
year = {年份}, 
}

2. 在.tex文件夹下新建一个.bib文件，将该内容拷贝到.bib文件中。

3. 在.tex文件中引用文献

在文章中使用 \cite{name1}（name1为参考文献Bibtex名称）引用文章 
设置参考文献类型 如 \bibliographystyle{IEEEtran} 
在结尾处声明 参考文献文件名称 \bibliography{XX}就是你建的.bib文件名称。

4. 编译.tex文件和.bib文件，.tex文件的编译和以前一样，.bib直接用BibTeX编译。

这样就可以了，不需要自己每个参考文献都调整。
--------------------- 
作者：芳草碧连天lc 
来源：CSDN 
原文：https://blog.csdn.net/leichaoaizhaojie/article/details/53956310 
版权声明：本文为博主原创文章，转载请附上博文链接！









