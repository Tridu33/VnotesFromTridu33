# sphin数学公式

```
.. math::
    \int_a^{b}f=\left[f(a+\dfrac{dx}{2})+f(a+dx+\dfrac{dx}{2})+(f(a+2dx+\dfrac{dx}{2})+\cdots \right]dx

```

能行













[基础 https://blog.csdn.net/enjoyyl/article/details/97820201](https://blog.csdn.net/enjoyyl/article/details/97820201)






有关Sphinx中对数学公式的支持, 参考手册 [Math support in Sphinx](http://www.sphinx-doc.org/en/stable/contents.html#document-ext/math)部分, 下面简单介绍使用.

note
Sphinx提供了两种数学公式的渲染方式 ( 二选一 ):

'sphinx.ext.imgmath' : 通过 LaTex 渲染成图片( png 或 svg ).
'sphinx.ext.mathjax' : 通过 MathJax 渲染.
使用LaTex渲染公式
如上所述, 在 extensions 列表变量里添加项 'sphinx.ext.imgmath', 即可.
数学公式通过LaTex引擎渲染成图片, 然后在HTML中显示.
但要求PC机安装有LaTex.

如果你不使用默认配置, 请参考 Math support in Sphinx.

使用KaTex渲染公式
KaTex 具有比 MathJax更快的解析速度. 使用 pip install sphinxcontrib.katex 安装 KaTex 扩展. 如上所述, 在 extensions 列表变量里添加项 'sphinxcontrib.katex', 即可. 数学公式通过KaTex引擎渲染公式在HTML中显示.

使用MathJax渲染公式
如上所述, 使用MathJax (准确说是Render math via JavaScript) 渲染公式,需要在 extensions 列表变量里添加项 'sphinx.ext.mathjax', .

此外, 你还需要配置MathJax的路径 mathjax_path , Sphinx默认使用 MathJaxCDN 提供的 JS 文件.Sphinx默认使用的MathJax的路径值为
https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML但你可能发现不管用, 可能是 https 安全协议的问题, 改成 http 即可,即设置配置文件 conf.py 中的mathjax_path = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'.

当然你也可以使用本地的MathJax, 参考 Installing Your Own Copy ofMathJax, 到 这里下载MathJax包 (约34.1MB) 并解压放到 “_static” 目录, 然后设置路径, 即在conf.py 文件中添加代码: mathjax_path = MathJax/MathJax.js . 重新make html 即可.

更多细节问题请参考 Math support inSphinx.



























