# C++数学库



























作为理工科学生，想必有限元分析、数值计算、三维建模、信号处理、性能分析、仿真分析。。。这些或多或少与我们常用的软件息息相关，假如有一天你只需要这些大型软件系统的某一个很有限的功能，你是不是也要因此再用一用那动辄几个g的软件呢？其实我觉得如果系统不是很大，不是很复杂，我们个人完全有可能自己去编写代码来实现这些‘’有限的功能‘’。别以为这是件很困难的事情，我总以为大学期间学的c语言是极其有用的，只要你会基本的c语言语法，你就可以的。

```
 下面我来介绍几个非常有益的c/c++数学计算库，他们基本上都是开源的，你完全不必担心版权问题，他们都是一些自由软件，你要做的仅仅是仔细阅读他们的授权协议确保不要滥用就可以了：

```

计算几何算法库 CGAL  
CGAL ，计算几何算法库，是一个大型C + +库的几何数据结构和算法，如Delaunay三角网，网格生成，布尔运算的多边形，以及各种几何处理算法。 CGAL是用来在各个领域：计算机图形学，科学可视化，计算机辅助设计与建模，地理信息系统，分子生物学，医学影像学，机器人学和运动规划，和数值方法。  
下载网址 [http://www.cgal.org/download.html](http://www.cgal.org/download.html)  
数学软件包 Octave  
Octave 是一个类似matlab和Scilab的数学软件包，可以进行各种运算，编程。它还有丰富的C++接口可以让用户编程时调用。它绘图使用gnuplot。  
Octave的使用也是基于字符终端模式的，当需要绘图时，将会调用Gnuplot进行数据绘图，并显示出来。  
Octave是用C++编写的，它内容丰富的库也可以供用户在编写软件时调用。Octave库的详细介绍在/usr/share/doc/octave-2.1.50/liboctave下，文件是liboctave.dvi，需要PDF文件的，可以运行：  
dvipdfm liboctave.dvi  
将dvi文件转换为PDF文件。  
Octave同时还支持Fortran等的调用，GSL绑定等。可以由用户定制自己的函数、子程序等。  
下载地址 [http://octave.sourceforge.net/packages.html](http://octave.sourceforge.net/packages.html)  
C++ 数学计算库 TooN  
TooN 是一个C++ 数学计算库，其目的是有效运作的大量小型矩阵，并提供方便一些算法包括矩阵分解和优化。  
下载地址[http://mi.eng.cam.ac.uk/~er258/cvd/toon/html-user/index.html](http://mi.eng.cam.ac.uk/~er258/cvd/toon/html-user/index.html)  
有限元分析软件 OpenFEM  
有限元分析，即使用有限元方法来分析静态或动态的物体或系统。在这种方法中一个物体或系统被分解为由多个相互联结的、简单、独立的点组成的几何模型。在这 种方法中这些独立的点的数量是有限的，因此被称为有限元。由实际的物理模型中推导出来得平衡方程式被使用到每个点上，由此产生了一个方程组。这个方程组可 以用线性代数的方法来求解。有限元分析的精确度无法无限提高。元的数目到达一定高度后解的精确度不再提高，只有计算时间不断提高。  
下载地址 [http://sourceforge.net/projects/openfem/files/](http://sourceforge.net/projects/openfem/files/)  
有限元计算框架 OOFEM  
OOFEM 是一个开源多物理并行有限元程序的面向对象的架构。这个项目的目的是提供高效率和强大的有限元计算工具，以及提供高度模块化和可扩展性的发展环境。有限元分析通常借助计算机软件完成，著名工程软件有：MSC.Nastran、ADINA、LS-DYNA、ANSYS、ABAQUS、2D-sigma等。  
下载地址 [http://www.oofem.org/en/download/download.html](http://www.oofem.org/en/download/download.html)  
C++符号计算库 GiNaC  
GiNaC（GiNaC 不是一个 CAS 计算机代数系统））是一个用于符号计算的C++库。它的设计允许集成系统创造，象征性的操作嵌入与更成熟的计算机科学（如计算密集型，图形界面等），数字应用领域。相对于其他情况下，它不会尝试代数提供广泛的功能和简单的编程语言，而是接受一个给定语言（C + +）和扩展了代数功能设置。  
下载地址 [http://www.ginac.de/Download.html](http://www.ginac.de/Download.html)  
类C的数学专用语言EngLab  
EngLab是一个类C的数学专用语言。它语法简单，关键字很少，工程师和那些只会少许编程知识的人便能很好的掌握。  
下载地址[http://sourceforge.net/projects/englab/files/](http://sourceforge.net/projects/englab/files/)  
C++信号处理库 SP++  
TSPL(Template Signal Processing Library) 是一个 C++ 的信号处理库，主要包括滤波器设计、时频分析和小波变换，同时还包含一些关于向量和矩阵的基本算法，所有的算法基于 C++ 模板类编写而成。  
下载地址[http://code.google.com/p/tspl/downloads/list](http://code.google.com/p/tspl/downloads/list)  
偏微分方程求解工具箱 DUNE（目前还不支持windows系统）  
DUNE (Distributed and Unified Numerics Environment)，分布和统一数值解环境，是一种求解偏微分方程的基于网格的方法（PDE）的模块化的工具箱。DUNE是所有这些体现了科学计算的概念从抽象的接口设置第一次。现代C + +编程技术使同样的概念非常不同的实现使用一个非常低的开销一个共同的接口。因此，DUNE确保在科学计算的效率，并支持高性能计算应用。  
下载地址[http://www.dune-project.org/download.html](http://www.dune-project.org/download.html)  
人工智能应用框架 Into  
Into 是一个用 C++ 开发的跨平台的机器智能应用框架。Into 提供一种不同于其他的、快速的方法用以构建高性能图像分析、机器视觉效果、模式识别和人工智能应用。分层的 API 一起超过 20 个完全可互操作的插入式模块用来访问图像和各种数据源等。  
下载地址[http://intopii.com/into/](http://intopii.com/into/)  
高性能计算软件工具包 DAKOTA  
DAKOTA (Design Analysis Kit for Optimization and Terascale Applications) 是一种用于执行系统的分析和高性能计算机的设计通用软件工具包。它提供了设计优化，不确定性量化，参数估计，实验设计，灵敏度分析，以及连接服务的计算和模拟的并行算法范围。  
下载地址[http://www.cs.sandia.gov/DAKOTA/download.html](http://www.cs.sandia.gov/DAKOTA/download.html)  
线性算术的C++模板库 Eigen  
Eigen 是一个线性算术的C++模板库，包括：vectors, matrices, 以及相关算法。功能强大、快速、优雅以及支持多平台。  
下载地址 [http://bitbucket.org/eigen/eigen/downloads/](http://bitbucket.org/eigen/eigen/downloads/)  
多精度整数和有理数 MPIR  
MPIR 是一个开源的多精度的整数和有理数计算库，基于 GMP 库开发。  
下载地址[http://www.mpir.org/mpir-1.3.1.tar.gz](http://www.mpir.org/mpir-1.3.1.tar.gz)  
C/C++数值计算库 mygsl  
mygsl是一个基于GSL库的个性化开源数值计算项目.  
该类库提供了关于数学计算的很多方面，包括：Complex Numbers Roots of Polynomials  
Special Functions Vectors and Matrices  
Permutations Sorting  
BLAS Support Linear Algebra  
Eigensystems Fast Fourier Transforms  
Quadrature Random Numbers  
Quasi-Random Sequences Random Distributions  
Statistics Histograms  
N-Tuples Monte Carlo Integration  
Simulated Annealing Differential Equations  
Interpolation Numerical Differentiation  
Chebyshev Approximation Series Acceleration  
Discrete Hankel Transforms Root-Finding  
Minimization Least-Squares Fitting  
Physical Constants IEEE Floating-Point  
Discrete Wavelet Transforms Basis splines  
下载地址[http://u.115.com/file/f572d894a0](http://u.115.com/file/f572d894a0)  
差不多我所知道的就这些了，其实本文主要参考的是开源中国社区公布的一些项目，我所做的仅仅是整理一下呈现给大家，希望对大家在以后的学习、工作有所帮助。在内心深处里，我其实很想某一天用着比较牛逼的这方面的国产软件，只是不知道会在什么时候。不想带着一种用盗版xp 、office，盗版ug，盗版ansys，盗版GT，盗版AMESim，盗版matlab。。。原来我电脑里装的全是盗版，有时候觉得这是一种多么可笑的事情，可是又没有什么办法。也许，从这一刻开始，我们带着一种新的理念，多少年后这种情况会得到改观。  
话又说多了···