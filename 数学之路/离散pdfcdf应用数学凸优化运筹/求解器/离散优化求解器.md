# 离散优化求解器











【学界】运筹学数学规划|离散优化求解器大搜罗 - 留德华叫兽的文章 - 知乎
https://zhuanlan.zhihu.com/p/40579450



## **二、商业整数规划求解器**

1.  **IBM ILOG Cplex**

**没错，就是笔者在意大利Blogna“实习”半年所在的求解器公司**

网址：[IBM ILOG CPLEX Optimization Studio](https://www.ibm.com/products/ilog-cplex-optimization-studio)

  

支持模型：混合整数（平方）规划、Constraint programming

支持语言：C/C++、Java、Python、Matlab等

特点：支持Benders分解模块（仅此一家）、速度Top2

当前版本：12.8

  

**2\. Gurobi**

网址：[The State-of-the-Art Mathematical Programming Solver](http://www.gurobi.com/)

支持模型：混合整数（平方）规划、Constraint programming

支持语言：C/C++、Java、R、Python、Matlab等

特点：速度Top1、价格最高

当前版本：8.0

  

**3\. FICO Xpress**

网址：[FICO® Xpress Optimization | FICO®](http://www.fico.com/en/products/fico-xpress-optimization)

支持模型：混合整数（非线性）规划、Constraint programming

特点：速度Top3，支持鲁棒优化

当前版本：8.5

  

**4\. MOSEK**

网址：[The State-of-the-Art Mathematical Programming Solver](http://www.gurobi.com/)

支持模型：混合整数（平方）规划、Second-order cone programming、Semidefinite programming、General convex nonlinear

支持语言：C/C++、Java、R、Python、Matlab等

特点：解SOCOP、SDP更快

当前版本：8.1

  

**价格：**

因为是商业软件，意味着他们是收费的

以下这份价格列表转自高级建模语言AMPL的官网：

![](https://pic3.zhimg.com/80/v2-186d98af4777ce04a375b3c762864697_1440w.jpg)

https://ampl.com/products/standard-price-list/

MOSEK售价为1950刀起

从价格可以看出，Gurobi是目前的NO.1（一个小插曲，或许是因为SCIP创始人*Tobias Achterberg*从Cplex跳槽至Gurobi以后的事）

好在学生|高校|科研用途都是免费的，只需学校邮箱即可免费下载并使用！









## **三、开源整数规划求解器**

1.  **SCIP**

网址：[SCIP](http://scip.zib.de/)

开发地：德国柏林ZIB研究中心（该中心毕业的博士就职于二中各大求解器公司，share着办公室并一起交流，得益于德国的一个政府项目）

支持：混合整数（非线性）规划、Constraint integer programming

支持语言：C/C++、Java、Python、Matlab等

特点：支持Branch&Price（仅此一家）

当前版本：6.0

  

**2\. GLPK、LP_Solve**

网址：[lp_solve reference guide](http://lpsolve.sourceforge.net/5.5/)、[GLPK](https://www.osc.edu/book/export/html/3422)

摘抄一段Gurobi官网对这俩个开源求解器的介绍：

![](https://pic4.zhimg.com/80/v2-c81e9c432b1072766d06f955a6622879_1440w.jpg)

http://www.gurobi.com/resources/switching-to-gurobi/open-source-solvers

  

**3\. COIN-OR旗下的CBC和SYMPHONY**

网址：[COIN-OR Branch-and-Cut MIP Solver](https://projects.coin-or.org/Cbc)、[SYMPHONY](https://projects.coin-or.org/SYMPHONY)

这里还是重点介绍下COIN-OR这个组织吧

它成立于17th International Symposium on Mathematical Programming (ISMP) conference in Atlanta in the summer of 2000，是一个公益组织，维护着市面上几乎所有的开源优化求解器，并且使得它们之间的交互变得可能。

它的网址：[The COIN-OR Foundation](https://www.coin-or.org/about-the-foundation/)

  

**4\. 华人求解器**

开源求解期

-   中科院的CMIP
-   上海财大|杉数科技主导的Leaves优化求解器

[【资讯】中科院CMIP混合整数规划求解器正式发布](https://zhuanlan.zhihu.com/p/35354471)

  

商业求解器

-   杉数科技的Cardinal

[【资讯】专访葛冬冬：我们做华人该有的求解器，BAT和国内科研单位做不了](https://mp.weixin.qq.com/s/cOKrB1X2Rw-ZSG6zgDHKow)


## **六、高级建模语言**

**GAMS、AMPL、JuMP、Mosel、Glop**


作为一种高级建模语言，首先可以把一个数学规划问题更简单地编程

其次，它可以调用以上任意一种优化求解器（如果兼容，Mosel只能调用Xpress）

这样，你只需写一遍code，便可比较多种不同的求解器，然后取结果最好的那个。



P.S.：其实很多软件，例如Matlab甚至Excel都自带了优化模块，可以解线性规划和整数规划问题。

由于他们不是专门做数学规划的，因此只能说可以用，关于效率和速度，和专门做这个的求解器，是没有对比价值的。








































































































