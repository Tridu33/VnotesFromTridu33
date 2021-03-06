[TOC]

-   [Index](https://zh-sphinx-doc.readthedocs.io/en/latest/genindex.html)
-   [Module Index](https://zh-sphinx-doc.readthedocs.io/en/latest/py-modindex.html)
-   [Search Page](https://zh-sphinx-doc.readthedocs.io/en/latest/search.html)
-   [Glossary](https://zh-sphinx-doc.readthedocs.io/en/latest/glossary.html#glossary)



# sphinx+reST

牛逼，这个案例学习好
https://github.com/zhaojiedi1992/My_Study_ReStructuredText







教程[https://iridescent.ink/HowToMakeDocs/Basic/index.html](https://iridescent.ink/HowToMakeDocs/Basic/index.html)









[https://documentation.help/Sphinx/config.html](https://documentation.help/Sphinx/config.html)

[https://www.sphinx-doc.org/en/master/usage/configuration.html](https://www.sphinx-doc.org/en/master/usage/configuration.html)








[https://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs](https://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs)


中文Zh-cn,换行坑


[https://readthedocs.org/](https://readthedocs.org/)






https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
中文搜索


[支持https://www.chenyudong.com/archives/sphinx-doc-support-chinese-search.html](https://www.chenyudong.com/archives/sphinx-doc-support-chinese-search.html)



[这什么操作？https://www.jianshu.com/p/354106f89a04](https://www.jianshu.com/p/354106f89a04)




[https://zh-sphinx-doc.readthedocs.io/en/latest/contents.html](https://zh-sphinx-doc.readthedocs.io/en/latest/contents.html)


[https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id3](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id3)


 [reStructuredText简明教程](https://linuxtools-rst.readthedocs.io/zh_CN/latest/helloworld.html#id55)




 reStructuredText入门

www.pythondoc.com/sphinx/rest.html


reStructuredText简明教程等某人的个人笔记 https://python-web-guide.readthedocs.io/zh/latest/skillstack/rst.html

**[https://www.bookstack.cn/read/mba811-Writing/reStructuredText-02.md](https://www.bookstack.cn/read/mba811-Writing/reStructuredText-02.md)**





别人写的笔记：可以直接从这个地方下载[https://github.com/zhaojiedi1992/My\_Study\_ReStructuredText](https://github.com/zhaojiedi1992/My_Study_ReStructuredText)，点击Clone or download按纽即可下载源文档。

然后复制 index.rst文件和 images,基础语法，中级语法三个目录到source目录中去。

具体的文档编写可以参考如下地址： 

-   　　sphinx对rst文档的帮助文档： [http://www.sphinx-doc.org/en/stable/rest.html](http://www.sphinx-doc.org/en/stable/rest.html)
-   　　spinx对rst文档的中文帮助文档：[http://zh-sphinx-doc.readthedocs.io/en/latest/rest.html](http://zh-sphinx-doc.readthedocs.io/en/latest/rest.html)


rst的学习笔记  （实用版）： [http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi\_liunx\_30\_python\_restructuredtext.html](http://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_liunx_30_python_restructuredtext.html)

-   　　rst的官文帮助文档：[http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)







https://zhuanlan.zhihu.com/p/108886400 新建包


官网 https://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs

https://zh-sphinx-doc.readthedocs.io/en/latest/contents.html



[https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)

 Sphinx + GitHub + ReadtheDocs 作为文档写作工具。用 Sphinx 生成文档，GitHub 托管文档，再导入到 ReadtheDocs。


主题[https://documentation.help/Sphinx/theming.html](https://documentation.help/Sphinx/theming.html)






```python
pip install -U Sphinx
C:\......\make.bat html#一定要一模一样，有时候是因为打字不一样报错，M-w,M-y完美解决问题。
```

语法

https://www.cnblogs.com/zzqcn/p/5096876.html




https://pandoc.org/try/  在线pandoc

Pandoc可以把markdown转换reST

命令行


https://ksomemo.github.io/contents/qiita/Install%20pandoc%20and%20convert%20to%20ReST%20from%20markdown.html
















constants.rst中的文件

```
.. _ref-directions:

Coordinates
-----------------


标题
====

章
--

节
~~

小节
####



```



# 2. Sphinx 文档目录

-   [译者前言](https://zh-sphinx-doc.readthedocs.io/en/latest/index.html)
-   [欢迎](https://zh-sphinx-doc.readthedocs.io/en/latest/index.html#id2)
-   [引言](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html)
    -   [不同文档系统的转换](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html#id2)
    -   [在其他系统中使用](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html#id3)
    -   [前提](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html#id4)
    -   [用法](https://zh-sphinx-doc.readthedocs.io/en/latest/intro.html#id5)
-   [Sphinx初尝](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html)
    -   [配置文档源](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id1)
    -   [定义文档结构](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id3)
    -   [添加内容](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id4)
    -   [运行创建工具](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id5)
    -   [文档对象](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id6)
    -   [基本配置](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id7)
    -   [自动文档](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id8)
    -   [其他话题](https://zh-sphinx-doc.readthedocs.io/en/latest/tutorial.html#id11)
-   [调用 sphinx-build](https://zh-sphinx-doc.readthedocs.io/en/latest/invocation.html)
    -   [Makefile 选项](https://zh-sphinx-doc.readthedocs.io/en/latest/invocation.html#makefile)
-   [调用 sphinx-apidoc](https://zh-sphinx-doc.readthedocs.io/en/latest/invocation.html#sphinx-apidoc)
-   [reStructuredText 简介](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html)
    -   [段落](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id1)
    -   [内联标记](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#inlinemarkup)
    -   [列表与引用](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id17)
    -   [源代码](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id34)
    -   [表格](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#rst-tables)
    -   [超链接](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id42)
    -   [章节](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id47)
    -   [显式标记](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id50)
    -   [指令](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#directives)
    -   [图像](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id129)
    -   [尾注](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id132)
    -   [引用](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id135)
    -   [替换](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id138)
    -   [评论](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id145)
    -   [源编码](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id148)
    -   [常见问题](https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html#id151)
-   [Sphinx标记的组成](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/index.html)
    -   [目录树](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/toctree.html)
    -   [段落级别的标记](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/para.html)
    -   [目录表格标记](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/para.html#id2)
    -   [术语](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/para.html#id5)
    -   [语法产品的显示](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/para.html#id6)
    -   [展示示例代码](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/code.html)
    -   [内联标记](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/inline.html)
    -   [未分类标记](https://zh-sphinx-doc.readthedocs.io/en/latest/markup/misc.html)
-   [Sphinx Domains](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html)
    -   [What is a Domain?](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#what-is-a-domain)
    -   [Basic Markup](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#basic-markup)
    -   [The Python Domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#the-python-domain)
    -   [The C Domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#the-c-domain)
    -   [The C++ Domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#id9)
    -   [The Standard Domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#the-standard-domain)
    -   [The JavaScript Domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#the-javascript-domain)
    -   [The reStructuredText domain](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#the-restructuredtext-domain)
    -   [More domains](https://zh-sphinx-doc.readthedocs.io/en/latest/domains.html#more-domains)
-   [Available builders](https://zh-sphinx-doc.readthedocs.io/en/latest/builders.html)
    -   [Serialization builder details](https://zh-sphinx-doc.readthedocs.io/en/latest/builders.html#serialization-builder-details)
-   [The build configuration file](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html)
    -   [General configuration](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#general-configuration)
    -   [Project information](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#project-information)
    -   [Options for internationalization](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-internationalization)
    -   [Options for HTML output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-html-output)
    -   [Options for epub output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-epub-output)
    -   [Options for LaTeX output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-latex-output)
    -   [Options for text output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-text-output)
    -   [Options for manual page output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-manual-page-output)
    -   [Options for Texinfo output](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-texinfo-output)
    -   [Options for the linkcheck builder](https://zh-sphinx-doc.readthedocs.io/en/latest/config.html#options-for-the-linkcheck-builder)
-   [Internationalization](https://zh-sphinx-doc.readthedocs.io/en/latest/intl.html)
-   [HTML theming support](https://zh-sphinx-doc.readthedocs.io/en/latest/theming.html)
    -   [Using a theme](https://zh-sphinx-doc.readthedocs.io/en/latest/theming.html#using-a-theme)
    -   [Builtin themes](https://zh-sphinx-doc.readthedocs.io/en/latest/theming.html#builtin-themes)
    -   [Creating themes](https://zh-sphinx-doc.readthedocs.io/en/latest/theming.html#creating-themes)
-   [Templating](https://zh-sphinx-doc.readthedocs.io/en/latest/templating.html)
    -   [Do I need to use Sphinx’ templates to produce HTML?](https://zh-sphinx-doc.readthedocs.io/en/latest/templating.html#do-i-need-to-use-sphinx-templates-to-produce-html)
    -   [Jinja/Sphinx Templating Primer](https://zh-sphinx-doc.readthedocs.io/en/latest/templating.html#jinja-sphinx-templating-primer)
    -   [Working with the builtin templates](https://zh-sphinx-doc.readthedocs.io/en/latest/templating.html#working-with-the-builtin-templates)
-   [Sphinx Extensions](https://zh-sphinx-doc.readthedocs.io/en/latest/extensions.html)
    -   [Tutorial: Writing a simple extension](https://zh-sphinx-doc.readthedocs.io/en/latest/ext/tutorial.html)
    -   [Extension API](https://zh-sphinx-doc.readthedocs.io/en/latest/ext/appapi.html)
    -   [Writing new builders](https://zh-sphinx-doc.readthedocs.io/en/latest/ext/builderapi.html)
    -   [Builtin Sphinx extensions](https://zh-sphinx-doc.readthedocs.io/en/latest/extensions.html#builtin-sphinx-extensions)
    -   [Third-party extensions](https://zh-sphinx-doc.readthedocs.io/en/latest/extensions.html#third-party-extensions)
-   [Sphinx Web Support](https://zh-sphinx-doc.readthedocs.io/en/latest/websupport.html)
    -   [Web Support Quick Start](https://zh-sphinx-doc.readthedocs.io/en/latest/web/quickstart.html)
    -   [The WebSupport Class](https://zh-sphinx-doc.readthedocs.io/en/latest/web/api.html)
    -   [Search Adapters](https://zh-sphinx-doc.readthedocs.io/en/latest/web/searchadapters.html)
    -   [Storage Backends](https://zh-sphinx-doc.readthedocs.io/en/latest/web/storagebackends.html)
-   [Sphinx FAQ](https://zh-sphinx-doc.readthedocs.io/en/latest/faq.html)
    -   [How do I...](https://zh-sphinx-doc.readthedocs.io/en/latest/faq.html#how-do-i)
    -   [Using Sphinx with...](https://zh-sphinx-doc.readthedocs.io/en/latest/faq.html#using-sphinx-with)
    -   [Epub info](https://zh-sphinx-doc.readthedocs.io/en/latest/faq.html#epub-info)
    -   [Texinfo info](https://zh-sphinx-doc.readthedocs.io/en/latest/faq.html#texinfo-info)
-   [Glossary](https://zh-sphinx-doc.readthedocs.io/en/latest/glossary.html)

# 3. 索引及表格
































