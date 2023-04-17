[TOC]


[用maxima解题https://math.pro/db/viewthread.php?tid=709](https://math.pro/db/viewthread.php?tid=709)


Maxima簡介  
[http://zh.wikipedia.org/wiki/Maxima](http://zh.wikipedia.org/wiki/Maxima)  
  
中文教學  
[http://math.nccu.edu.tw/~yenlung ... l/maximalinear.html](http://math.nccu.edu.tw/~yenlung/mynotes/maximalinear_html/maximalinear.html)  
[http://yenlung.math.nccu.edu.tw/index.html/idisk/maximalinear.pdf](http://yenlung.math.nccu.edu.tw/index.html/idisk/maximalinear.pdf)  
[http://math.npue.edu.tw/front/bin/ptlist.phtml?Category=119](http://math.npue.edu.tw/front/bin/ptlist.phtml?Category=119)  
  
其他的教學網頁  
[http://www.eonet.ne.jp/~kyo-ju/maxima.pdf](http://www.eonet.ne.jp/~kyo-ju/maxima.pdf)  
[http://people.ysu.edu/~gkerns/maxima/](http://people.ysu.edu/~gkerns/maxima/)  
[http://www.math.hawaii.edu/home/wxmaxima.html](http://www.math.hawaii.edu/home/wxmaxima.html)  
[http://maxima.sourceforge.net/documentation.html](http://maxima.sourceforge.net/documentation.html)  
101.6.16補充  
[http://math.stanford.edu/~paquin/MaximaBook.pdf](http://math.stanford.edu/~paquin/MaximaBook.pdf)  
討論區  
[http://www.math.utexas.edu/pipermail/maxima/2013/](http://www.math.utexas.edu/pipermail/maxima/2013/)  
  
101.11.13補充  
[http://maxima-online.org/](http://maxima-online.org/)  
線上執行maxima的網頁，輸入指令後點選Calculate。

















# maxima

C:\maxima-5.43.0\share\maxima\5.43.0\doc\html

`? real` 精确查找帮助

`?? real` 模糊查找帮助

`example(realpart)` 查看命令案例

数据类型：整数、有理数、`float` `bfloat`

`%` 表示最后一次运算结果

## 初等数学

`+` `-` `*` `/` `^` `!` 算术运算

> sin() cos() tan() cot() sec csc()  
> sinh() cosh() tanh() coth() sech csch()  
> asin() acos() atan() acot() asec() acsc()  
> asinh() acosh() atanh acoth() asech() acsch()  
> log()

常数：`%e` `%i` `%pi` `inf` `minf` `infinity` 复数无穷

`f(x,y) := sin(x)+cos(x);` 自定义函数

`sum(expr,i,m,n);` 求和，`sum(),simpsum;`

`product(expr,i,m,n);` 累积 `product(),simpproduct;`

`expand(%);` 多项式展开，`pactor(%);` 因式分解

`subst(1/a,x,%);` 等量代换

`ratsimp(%);` 分式化简，`radcan(%);` 对数、根式化简

`assume(x<0);` 假设，`facts();` 查看假设

`forget(x<0);` 取消假设

`trigexpand` 和差化积 `trigreduce` 积化和差

`trigsimp` 用1化简 `trigrat` 简化分数形式

`solve(eq,x);` 解方程 `eq:x+1=0;`

`solve([eq1,eq2],[x,y]);` 解方程组

`allroots(eq);` 数值解 `realroots(eq);` 实数数值解

`z:5+3*%i;` `realpart(z);` `imagpart(z);` 复数

`conjugate(z);` 复共轭 `abs(z);` 模 `carg(z);` 幅角

`rectform` `polarform` 复数直角、极坐标形式

## 矩阵

`entermatrix(m,n);` 交互式输入矩阵

`matrix([1,2,3],[4,5,6]);` 输入矩阵

`a[i,j]:=i+j;` `genmatrix(a,m,n);` 生成矩阵

`diagmatrix(n,x);` 生成对角矩阵

`ematrix(m,n,x,i,j);` 生成单一非0元素矩阵

`+` `-` `*` `/` 对应元素运算，`A . B` 矩阵乘法，有空格

`row(M,i)` `col(M,i)` 矩阵M第 i 行/列

`addcol(M,[1,2,3]);` `addrow(M,[]);` 增加行/列

`submatrix(i1,i2,M,j)` 删除矩阵M第 i1 i2 行 j 列

`determinnant(M);` 行列式

`transpose(M);` 矩阵转置

`invert(M);` 矩阵的逆

`rank(M);` 矩阵的秩

`eigenvalues(M);` 返回 \[\[本征值\],\[对应重数\]\]

`eigenvectors(M);` 返回 \[\[同上\],\[本征向量\]\]

## 微积分

`diff(f(x),x,n);` `diff(f(x,y),x,n,y,m)` 微分

`integrate(f(x),x)` 不定积分

`integrate(f(x),x,a,b)` 定积分

`taylor(f(x),x,a,n)` a点n阶泰勒展开

`laplace(f(t),t,s)` `ilt(f(s),s,t)` 拉普拉斯

`residue(f(z),z,z0)` 在z0点留数

## 微分方程

`eq:'diff(y,x,2)-y=4*x*sin(x);` '表示不计算

`ode2(eq,y,x);` 解一阶/二阶微分方程

`ic2(%,x=0,y=1,'diff(y,x)=2);` `ic1` 初值

`bc2(%,x1,y1,x2,y2)` 二阶边值问题

`atvalue(x(t),t=0,1);` 提供初值

`desolve([eq1,eq2],[x(t),y(t)]);` 一阶微分方程组

## 作图

调用 Gnuplot，基于命令行的函数及数据作图程序。

`plot2d(f(x),[x,minX,maxX],[y,minY,maxY]);`

`plot2d([f1,f2],[x,minX,maxX]);` 多条图

`plot2d(f(x),[x,0,3],[logy])` 对数坐标

`x:[];` `y:[];` `plot2d([discrete,x,y]);` 数据绘图

`tex(expr);` 输出LATEX代码

  
  
作者：ve_故食  
链接：https://www.jianshu.com/p/b8ad1de816e4  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[coeff 函数的应用 https://blog.csdn.net/liyuanbhu/article/details/7603929](https://blog.csdn.net/liyuanbhu/article/details/7603929)











[http://eagle.cs.kent.edu/MAXIMA/maxima_toc.html](http://eagle.cs.kent.edu/MAXIMA/maxima_toc.html)





[http://maxima.sourceforge.net/docs/manual/maxima_singlepage.html](http://maxima.sourceforge.net/docs/manual/maxima_singlepage.html)




```maxima
f(x):=x^2;

g(x) := ''(diff(f(x), x));

or 

define (g(x), diff (f(x), x));

```















[https://wxmaxima-developers.github.io/wxmaxima/help.html](https://wxmaxima-developers.github.io/wxmaxima/help.html)






# Maxima Documentation

-   [Reference Manual](http://maxima.sourceforge.net/docs/manual/maxima.html) ([ PDF version](http://maxima.sourceforge.net/docs/manual/maxima.pdf), [ EPUB version](http://maxima.sourceforge.net/docs/manual/maxima.epub), [ Single-page HTML version](http://maxima.sourceforge.net/docs/manual/maxima_singlepage.html))
-   [Xmaxima Reference Manual](http://maxima.sourceforge.net/docs/xmaxima/xmaxima.html) ([ PDF version](http://maxima.sourceforge.net/docs/xmaxima/xmaxima.pdf))
-   [Maxima by Example](http://www.csulb.edu/~woollett/) by Edwin L. Woollett
-   [A 10 minute tutorial for solving Math problems with Maxima](http://math-blog.com/2007/06/04/a-10-minute-tutorial-for-solving-math-problems-with-maxima/) by Antonio Cangiano
-   [Macsyma’s General Simplifier: Philosophy and Operation](http://maxima.sourceforge.net/misc/Fateman-Salz_Simplifier_Paper.pdf) by Richard Fateman, first published in the Macsyma Users Conference, Washington D.C. 1979, in: MUC-79, 563-582. Notes have been added to the original paper by the author from today's perspective. A subsection that was not written as of 1979 has also been added in 2017.
-   [Introduction to Maxima](http://maxima.sourceforge.net/docs/manual/intromax.html) by Richard Rand ([  PDF version](http://maxima.sourceforge.net/docs/manual/intromax.pdf))
-   [The Computer Algebra Program Maxima](http://maxima.sourceforge.net/docs/tutorial/en/gaertner-tutorial-revision/Contents.htm) by Boris Gaertner ([  zipped version](http://maxima.sourceforge.net/docs/tutorial/en/gaertner-tutorial-revision.zip))
-   [Minimal Maxima](http://maxima.sourceforge.net/docs/tutorial/en/minimal-maxima.pdf) by Robert Dodier
-   [Micro introduction into Maxima](http://www.math.harvard.edu/computing/maxima/) at Harvard U
-   [Symbolic Mathematics Using Maxima](http://arachnoid.com/maxima/) by Paul Lutus
-   [Maxima user interface tips](http://maxima.sourceforge.net/ui-tips.html) — a collection of tips for customizing and interacting with the Maxima user interface.
-   [Graphics with Maxima](http://www.austromath.at/daten/maxima/zusatz/Graphics_with_Maxima.pdf) by Wilhelm Haager
-   [Rules and patterns in Maxima](http://maxima.sourceforge.net/docs/tutorial/en/talon-pattern.pdf) by Michel Talon, a tutorial introduction to the Maxima pattern matching functions

## Publications

Books and articles which mention Maxima or Macsyma.

-   [BibTeX format bibliography of papers on MACSYMA/VAXIMA before 1994](http://www.math.utah.edu/pub/tex/bib/macsyma.html).
-   [*Dynamical systems* by J. E. Villate](http://www.villate.org/doc/sistemasdinamicos/sistdinam-1_2.pdf), in Portuguese and some parts translated to Spanish and English. Book that uses Maxima to teach a course on ”Dynamical systems”.
-   [A. Ben-Israel, R. Gilbert: Computer-Supported Calculus](http://www.springer.com/springerwiennewyork/mathematics/book/978-3-211-82924-0). Springer: Wien 2002. ISBN 3-211-82924-5.
-   [Robert S. Maier ”The 192 Solutions of the Heun Equation”](http://arxiv.org/abs/math/0408317 "arXiv.org e-print"). Mathematics of Computation, vol. 76 (2007), pp. 811-843.
-   [Robert S. Maier ”On Rationally Parametrized Modular Equations”](http://arxiv.org/abs/math/0611041 "arXiv.org e-print").
-   [Joel Moses](http://esd.mit.edu/Faculty_Pages/moses/moses.htm). [”Macsyma: A Personal History”](http://esd.mit.edu/Faculty_Pages/moses/Macsyma.pdf). Invited Presentation in [Milestones in Computer Algebra](http://www.orcca.on.ca/conferences/mica2008/), May 2008, Tobago.
-   [Mathematical Modeling and Simulation](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-3527407588.html) by Kai Velten  
    Kai Velten: Mathematical Modeling and Simulation, Wiley-VCH, 2009.  
    [http://books.google.com/books?id=Czp1N5UWpyEC](http://books.google.com/books?id=Czp1N5UWpyEC)   
    A book on modeling and simulation exclusively based on open source software. It includes many examples from such diverse fields as biology, ecology, economics, medicine, agricultural, chemical, electrical, mechanical, and process engineering. Requiring only little mathematical prerequisite in calculus and linear algebra, this lucidly written text is accessible to scientists, engineers, and students at the undergraduate level. The book addresses a broad range of models from elementary statistical models to ODE and PDE models. The reader is introduced into CAELinux, Calc, Code-Saturne, Maxima, R, and Salome-Meca.
-   [Scientific Programming by Jorge Alberto Calvo](http://www.cambridgescholars.com/scientific-programming)  
    Numeric, Symbolic, and Graphical Computing with Maxima
-   Andreas Öchsner and Resam Makvandi (2019). Finite Elements for Truss and Frame Structures. An Introduction Based on the Computer Algebra System Maxima. Berlin: Springer-Verlag. DOI: [10.1007/978-3-319-94941-3](https://doi.org/10.1007/978-3-319-94941-3)

## Other documents

-   [Some Baseless Opinions About Maxima](http://maxima.sourceforge.net/misc/maxima-opinions.pdf) by Robert Dodier  
    A presentation from [Sage](http://sagemath.org/) [Developer Days 1](http://wiki.sagemath.org/dev1).
-   [The Maxima Book](http://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf)  
    This is a very incomplete and in some places out of date user oriented manual. It is a work in progress, but is provided here in the hope it might be useful.  
    Update: This new version isn't all that different, but it has been updated a bit with regards to plotting and a couple other minor changes. Emaxima and install docs have not been updated yet. Mathematical content is essentially unchanged. Pictures should be of slightly better quality.
-   [MAXIMA: Science and Engineering Applications](http://www.neng.usu.edu/cee/faculty/gurro/Maxima.html) by [Gilberto E. Urroz](http://www.neng.usu.edu/cee/faculty/gurro/)  
    A collection of lecture notes, showing the use of Maxima and WxMaxima in science and engineering problems.
-   [Computer Based Tools for Engineers](http://www.eng.ysu.edu/~jalam/engr6924s07/) by [Javed Alam](http://www.eng.ysu.edu/~jalam/)  
    The different sessions provide the necessary theory and the solution using Maxima for problems encountered in Engineering computing.











# wxMaxima

wxMaxima is a document based interface for the computer algebra system  Maxima. For more information about Maxima, visit  [http://maxima.sourceforge.net/](http://maxima.sourceforge.net/). wxMaxima uses wxWidgets and runs  natively on Windows, X11 and Mac OS X. wxMaxima provides menus and  dialogs for many common Maxima commands, autocompletion, inline plots  and simple animations. wxMaxima is distributed under the GPL license.

wxMaxima is included with the Windows and the Macintosh installer for  Maxima. Packages are also available for many Linux distributions. Screenshots  and documentation can be found at [http://wxMaxima-developers.github.io/wxmaxima/](http://wxMaxima-developers.github.io/wxmaxima/)

Instructions on where to get a complete Maxima package from  can be found at [http://maxima.sourceforge.net/download.html](http://maxima.sourceforge.net/download.html).

Information on how to compile wxMaxima from source instead can be  found at [https://github.com/wxMaxima-developers/wxmaxima/blob/master/Compiling.md](https://github.com/wxMaxima-developers/wxmaxima/blob/master/Compiling.md)

![Travis CI Build Status](https://travis-ci.org/wxMaxima-developers/wxmaxima.svg?branch=master)
