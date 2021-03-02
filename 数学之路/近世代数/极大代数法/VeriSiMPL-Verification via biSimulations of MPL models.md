[TOC]

# 1. [VeriSiMPL-Verification via biSimulations of MPL models](https://www.researchgate.net/publication/262205228_VeriSiMPL_verification_via_bisimulations_of_MPL_models)


VeriSiMPL (“very simple”) is a software tool to obtain finite abstractions of Max-Plus-Linear (MPL) models. MPL models (Sect. 2), specified in MATLAB, are abstracted to Labeled Transition Systems (LTS). The LTS abstraction is formally put in relationship with the concrete MPL model via a (bi)simulation relation. The abstraction procedure (Sect. 3) runs in MATLAB and leverages sparse representations, fast manipulations based on vector calculus, and optimized data structures such as Difference-Bound Matrices. LTS abstractions can be exported to structures defined in the PROMELA. This enables the verification of MPL models against temporal specifications within the SPIN model checker (Sect. 4). The toolbox is available at http://sourceforge.net/projects/verisimpl/

VeriSiMPL（“非常简单”）是用于获得Max-Plus-Linear（MPL）模型的有限抽象的软件工具。
在MATLAB中指定的MPL模型（第2节）被抽象到标签转换系统（LTS）。 
LTS抽象通过（双向）模拟关系正式与具体的MPL模型建立关系。
抽象过程（第3节）在MATLAB中运行，并利用稀疏表示，基于矢量演算的快速操作以及优化的数据结构（例如差分界限矩阵）。 
LTS抽象可以导出到PROMELA中定义的结构。
这样可以在SPIN模型检查器（第4节）中根据时间规范验证MPL模型。
该工具箱位于http://sourceforge.net/projects/verisimpl/


哈佛学生开发的[https://www.cs.ox.ac.uk/teaching/studentprojects/303.html](https://www.cs.ox.ac.uk/teaching/studentprojects/303.html)


该项目旨在增强软件收费箱VeriSiMPL（“非常简单”），该收费箱已开发用于支持Max-Plus-Linear（MPL）模型的抽象。MPL模型是在MATLAB中指定的，并抽象到标签转换系统（LTS）。LTS抽象通过（双向）模拟关系正式与其MPL对应关系。抽象过程在MATLAB中运行，并利用稀疏表示，基于矢量演算的快速操作以及优化的数据结构（例如，差值绑定矩阵）。LTS可以通过Graphviz工具以图形方式表示，并导出为PROMELA语言。这样就可以根据SPIN模型检查器中的时间规范来验证MPL模型。

课程：计算机辅助形式验证，微分方程数值解

先决条件：熟悉动力学系统，MATLAB和C的工作知识



VeriSiMPL概述
通过Max-Plus-Linear模型的biSimulations进行验证

该工具箱用于在R ^ n上生成自治的Max-Plus-Linear（MPL）系统的有限抽象。抽象的特征是有限状态标记过渡系统（LTS）。LTS有限抽象被显示为模拟或双模拟原始MPL系统。LTS模型要根据线性时序逻辑（LTL）和计算树逻辑（CTL）中的公式表示的给定规范进行验证。该工具箱打算利用NuSMV模型检查器。模型将以C ++语言表示。抽象过程在C ++中运行。生成的LTS导出为NuSMV语言。这样，它可以与感兴趣的规范一起被馈送到NuSMV模型检查器。

如果您更熟悉JAVA语言，建议您尝试完全基于JAVA的VeriSiMPL 2.0版。

如果您更熟悉MATLAB语言，建议您尝试完全基于MATLAB的VeriSiMPL 1.4版。



这项工作提出了一种新颖的技术，可以生成自治和非自治的Max-Plus-Linear（MPL）模型的有限抽象，该模型是一类离散事件系统，用于表征与自动同步的连续事件相关的时序动态。MPL模型的非自治版本嵌入其动态不确定性内，即通常被视为外源控制或时间表的信号选择。本文将MPL模型的抽象特征描述为有限状态标记过渡系统（LTS）。
首先通过划分MPL模型的状态空间（对于非自治模型，通过覆盖输入空间）并将LTS的状态与所引入的分区相关联来获得LTS，然后通过基于MPL状态空间的相应分区之间的动态转换定义LTS的状态之间的关系，最后根据原始MPL模型的事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。最后根据原始MPL模型事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。最后根据原始MPL模型事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。


## 1.1. C++

% Verification via biSimulations of MPL models (VeriSiMPL) Toolbox
% Version 3.0 (17-May-2017)

Webpages:
sourceforge.net/projects/verisimpl
sites.google.com/site/diekyadzkiya
www.cs.ox.ac.uk/people/alessandro.abate/home.html

Authors:
Dieky Adzkiya and Alessandro Abate

Email contacts:
dieky@matematika.its.ac.id
alessandro.abate@cs.ox.ac.uk

Mail contacts: 
1) Department of Mathematics
   Institut Teknologi Sepuluh Nopember
   Kampus ITS Sukolilo, Surabaya 60111 
   Indonesia
2) Department of Computer Science
   University of Oxford
   Wolfson Building, Parks Road, Oxford, OX1 3QD,
   United Kingdom

Main bibliographical references:
1) D. Adzkiya and A. Abate,
   ``VeriSiMPL: Verification via biSimulations of MPL Models''
   In Proceedings of the 10th Quantitative Evaluation of Systems
   volume 8054 of Lecture Notes in Computer Science, pages 253-256, Springer, Heidelberg
   Buenos Aires, September 2013.
2) D. Adzkiya, B. De Schutter and A. Abate,
   ``Finite Abstractions of Max-Plus-Linear Systems''
   IEEE Transactions on Automatic Control 58(12), pages 3039-3053, December 2013.
3) D. Adzkiya, B. De Schutter and A. Abate,
   ``Computational Techniques for Reachability Analysis of Max-Plus-Linear Systems''
   Automatica 53(0), pages 293-302, 2015.
4) D. Adzkiya, Y. Zhang and A. Abate,
   ``VeriSiMPL 2: An open-source software for the verification of max-plus-linear systems''
   Discrete Event Dynamic Systems 26(1), pages 109-145, 2016.
5) G. Holzmann, 
   ``The SPIN Model Checker''
   Addison-Wesley, 2003. 

Additional bibliographical references:
1) D. Adzkiya, B. De Schutter and A. Abate,
   ``Abstraction and Verification of Autonomous Max-Plus-Linear Systems''
   In Proceedings of the 31st American Control Conference, pages 721-726
   Montreal - CA, June 2012.
2) D. Adzkiya, B. De Schutter and A. Abate,
   ``Finite Abstractions of Nonautonomous Max-Plus-Linear Systems''
   In Proceedings of the 32nd American Control Conference, pages 4387-4392
   Washington, June 2013.
3) D. Adzkiya, B. De Schutter and A. Abate,
   ``Forward Reachability Computation for Autonomous Max-Plus-Linear Systems''
   In Proceedings of the 20th International Conference on Tools and Algorithms for the Construction and Analysis of Systems
   volume 8413 of Lecture Notes in Computer Science, pages 248-262, Springer, Heidelberg
   Grenoble, April 2014.
4) D. Adzkiya, B. De Schutter and A. Abate,
   ``Backward Reachability of Autonomous Max-Plus-Linear Systems''
   Proceedings of the 12th IFAC - IEEE International Workshop on Discrete Event Systems, pages 117-122, May 2014, Paris.
5) Muhammadun, D. Adzkiya and I. Mukhlash,
   ``Object Oriented Design of Software Tool for Finite Abstractions of Max-Plus-Linear Systems using Unified Modeling Language''
   International Journal of Computing Science and Applied Mathematics 3(1), pages 32-39, 2017.

Description
===========

This toolbox is used to generate finite abstractions of autonomous
Max-Plus-Linear (MPL) systems over R^n. Abstractions are 
characterized as finite-state Labeled Transition Systems (LTS). 
The LTS finite abstractions are shown to either simulate or to bisimulate
the original MPL system. LTS models are to be verified against given 
specifications expressed as formulae in Linear Temporal Logic (LTL) and
Computation Tree Logic (CTL). The toolbox intends to leverage the NuSMV model checker. 

该工具箱用于在R ^ n上生成自治的Max-Plus-Linear（MPL）系统的有限抽象。
抽象的特征是有限状态标记过渡系统（LTS）。 
LTS有限抽象被显示为模拟或双模拟原始MPL系统。 
LTS模型要根据线性时序逻辑（LTL）和计算树逻辑（CTL）中的公式表示的给定规范进行验证。
该工具箱打算利用NuSMV模型检查器。

Models are to be expressed in the C++ language. 
The abstraction procedure runs in C++. 
The generated LTS is exported to the NuSMV language. 
As such, it can be fed, along with a specification of interest, to the NuSMV model checker.

If you are more familiar with JAVA language,
we suggest you to try VeriSiMPL version 2.0 which is fully based on JAVA.
If you are more familiar with MATLAB language,
we suggest you to try VeriSiMPL version 1.4 which is fully based on MATLAB.





Installation
============

This toolbox consists of the following main classes: 

This toolbox calls the 该工具箱包含以下主要类：

1) StateMatrix
   This class is used to store the state matrix of an MPL system.

StateMatrix此类用于存储MPL系统的状态矩阵。

2) AffineDynamics
   This class is used to store an affine dynamics generated from an MPL dynamics.

AbstractionTree这是用于存储抽象转换系统的主类。

3) DBM
   This class is used to represent a DBM and its operations, such as
   computing the canonical-form representation, intersection of two DBM,
   complement of a DBM, emptiness checking, computing the image of a DBM w.r.t. an affine dynamics   and computing the inverse image of a DBM w.r.t. an affine dynamics.

DBM此类用于表示DBM及其操作，例如计算规范形式的表示形式，两个DBM的交集，DBM的补码，空度检查，计算DBM w.r.t.的图像。仿射动力学并计算DBM w.r.t的反像 。仿射动力学。 AffineDynamics此类用于存储从MPL动态生成的仿射动态。 

4) AbstractionTree
   This is the main class that is used to store the abstract transition system.



该工具箱调用NuSMV模型检查器的可执行文件。
请确保将NuSMV可执行文件命名为“ NuSMV.exe”（在Windows中）和“ NuSMV”（在Linux中）。
此外，必须可以从任何位置访问NuSMV可执行文件，这可以通过在PATH中插入NuSMV可执行文件的位置来完成。

There are two ways to run this toolbox:
1) Binary file
If your operating system is windows,
you should execute the file "VeriSiMPL.exe" in the "windows\bin\Debug" folder.
If your operating system is linux,
you should execute the file "VeriSiMPL" in the "linux/bin/Debug" folder.
2) Source file
We suggest to use Code::Blocks run the source code of this toolbox.
Firstly, we open project file "VeriSiMPL.cbp".
If your operating system is windows,
you should open the file in the "windows" folder.
If your operating system is linux,
you should open the file in the "linux" folder.
Lastly, you can execute the toolbox by using the command "Build and Run".


有两种方法可以运行此工具箱：

1）二进制文件如果您的操作系统是Windows，则应在“ windows \ bin \ Debug”文件夹中执行文件“ VeriSiMPL.exe”。
如果您的操作系统是linux，则应在“ linux / bin / Debug”文件夹中执行文件“ VeriSiMPL”。 
2）源文件我们建议使用Code :: Blocks运行此工具箱的源代码。
首先，我们打开项目文件“ VeriSiMPL.cbp”。
如果您的操作系统是Windows，则应在“ windows”文件夹中打开文件。
如果您的操作系统是linux，则应打开“ linux”文件夹中的文件。
最后，您可以使用“构建并运行”命令来执行工具箱。

Support
=======

There is no support! This toolbox is made freely available in the hope 
that you find it useful in solving whatever problems you have at hand.
We are happy to correspond with people who have found genuine bugs. 
If you have any questions or comments, or you observe buggy behavior 
of this toolbox, please send your reports by email to the authors.




## 1.2. matlab


通过MPL模型的双向仿真（VeriSiMPL）工具箱进行的验证
百分比％版本1.4（2014年4月10日）

网页：
http 
：//sourceforge.net/projects/verisimpl http://www.dcsc.tudelft.nl/~aabate/VeriSiMPL.html

作者：
Dieky Adzkiya和Alessandro Abate

电子邮件联系人：
{d.adzkiya，a.abate} @ tudelft.nl 
alessandro.abate@cs.ox.ac.uk

邮件联系人：
1）代尔夫特中心系统与控制
   代尔夫特理工大学-代尔夫特理工大学
   Mekelweg 2，2628CD代尔夫特，
   荷兰
2）计算机科学系
   牛津大学
   沃尔夫森大厦，公园路，牛津，OX1 3QD，
   英国

主要书目参考：
1）D. Adzkiya和A. Abate，
《 Max-Plus-Linear系统的有限抽象》，   IEEE自动控制学报，第58（12）页，第3039-3053页，2013年12月。3）G. Holzmann，   ` “ SPIN模型检查器”，   Addison-Wesley，2003年。   VeriSiMPL: Verification via biSimulations of MPL Models''
   In Proceedings of the 10th Quantitative Evaluation of Systems
   volume 8054 of Lecture Notes in Computer Science, pages 253-256, Springer, Heidelberg
   Buenos Aires, September 2013.
2) D. Adzkiya, B. De Schutter, and A. Abate,




其他书目参考文献：
1）D.Adzkiya，B.De Schutter和A.Abate，
《非自治Max-Plus线性系统的有限抽象   》，《第32届美国控制会议论文集》，第4387-4392页，   华盛顿，2013年6月。3）D.Adzkiya，B.De Schutter和A.Abate，《自主最大加线性系统的后向可达性》   ，《第12届IFAC会议记录-IEEE国际离散事件系统研讨会》，2014年5月，巴黎。   Abstraction and Verification of Autonomous Max-Plus-Linear Systems''
   In Proceedings of the 31st American Control Conference, pages 721-726
   Montreal - CA, June 2012.
2) D. Adzkiya, B. De Schutter, and A. Abate,



   Forward Reachability Computation for Autonomous Max-Plus-Linear Systems''
   In Proceedings of the 20th International Conference on Tools and Algorithms for the Construction and Analysis of Systems
   volume 8413 of Lecture Notes in Computer Science, pages 248-262, Springer, Heidelberg
   Grenoble, April 2014.
4) D. Adzkiya, B. De Schutter, and A. Abate,

描述
此工具箱用于生成
R ^ n上
的自治和非自治Max-Plus-Linear（MPL）模型的有限抽象。抽象的特征是有限状态标记过渡系统（LTS）。
LTS有限抽象被显示为模拟或双模拟
原始MPL模型。LTS模型应根据
线性时序逻辑（LTL）中公式表示的
给定规范进行验证。该工具箱打算利用SPIN模型检查器。

模型应以MATLAB语言表示。
抽象过程在MATLAB中运行。
生成的LTS导出到PROMELA。
这样，它可以与感兴趣的规范一起馈送
到SPIN模型检查器。

该工具箱还可用于
自治和非自治MPL模型的
可达性计算。同样支持向前和向后可达性。
用户可以计算覆盖范围或覆盖范围。


在多参数工具箱（MPT）版本2中，
还具有将自治MPL系统导出到分段仿射（PWA）系统的功能。这使能够将MPT中的功能用于MPL系统的PWA表示。

安装
该工具箱包含以下主要文件： 

mpl2pwa_part.m-生成分区
ts_trans.m-确定过渡（自治模型）
ts_label.m-计算过渡标签（自治模型）
ts_refine.m-优化过程以获取确定的过渡系统（自治模型）
mplnon2pwa_part.m-生成分区
tsnon_trans 
.m- 
确定过渡（非自治模型）tsnon_label.m-计算过渡标签（非自治模型）ts2spin_state.m-生成用于验证状态标签的旋转代码（两个模型）
ts2spin_trans.m-生成用于对过渡标签进行验证的旋转代码（自主）楷模）
tsnon2spin_trans.m-生成用于在过渡标签上验证的旋转码（非自治模型）
mpl2pwa.m-生成分段仿射系统
mpl2pwa_refine.m-优化分段仿射系统的区域以获得分区
ts2graphviz.m-将过渡系统导出到graphviz代码（点）
mpl2pwa_mpt.m-在MPT版本2结构中生成PWA系统
mpl_reachset_back.m-计算自主模型的后向范围
mpl_reachset_for.m-计算
自主模型的前向范围mpl_reachtube_back.m-计算
自主模型的后向范围mpl_reachtube_for.m .m-自主模型的计算前伸管
mplnon_reachtube_back.m-计算非自治模型的后向延伸管
mplnon_reachtube_for.m-计算
非自治模型的前向延伸管maxpl2ts_demo.m-用于提取最大自加线性系统的
GUI maxpl_absver_demo.m-用于提取和验证自定义最大加法的GUI加线性系统
maxpl_reachfor_demo.m-自主最大加线性系统正向可达性的GUI（此版本的新功能）

为了使用此工具箱，请将Matlab路径设置为“ VeriSiMPL /”目录。
此工具箱已通过Matlab R2009b，R2010b，R2011a，R2011b，R2012b成功测试。

支持
没有支持！该工具箱免费提供，希望
您发现它对于解决您遇到的任何问题有用。
我们很高兴与发现真正错误的人联系。
如果您有任何疑问或意见，或者观察
到此工具箱的错误行为，请通过电子邮件将报告发送给作者。








































# 2. [Finite abstractions of max-plus-linear systems](https://pub.deschutter.info/abs/13_018.html)



抽象：
这项工作提出了一种新颖的技术，可以生成自治和非自治的Max-Plus-Linear（MPL）模型的有限抽象，该模型是一类离散事件系统，用于表征与自动同步的连续事件相关的时序动态。MPL模型的非自治版本嵌入其动态不确定性内，即通常被视为外源控制或时间表的信号选择。本文将MPL模型的抽象特征描述为有限状态标记过渡系统（LTS）。首先通过划分MPL模型的状态空间（对于非自治模型，通过覆盖输入空间）并将LTS的状态与所引入的分区相关联来获得LTS，然后通过基于MPL状态空间的相应分区之间的动态转换定义LTS的状态之间的关系，最后根据原始MPL模型的事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。最后根据原始MPL模型事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。最后根据原始MPL模型事件的单步计时属性标记LTS边缘。为了建立形式对等，有限抽象被证明可以模拟或双模拟原始MPL模型。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。通过验证（通过模型检查）有限LTS抽象上的等效逻辑规范，该方法可以研究原始MPL模型的一般属性。详细讨论了与抽象过程相关的计算方面，并在数字基准上测试了其性能。






















[https://ieeexplore.ieee.org/document/6558835](https://ieeexplore.ieee.org/document/6558835)






















































