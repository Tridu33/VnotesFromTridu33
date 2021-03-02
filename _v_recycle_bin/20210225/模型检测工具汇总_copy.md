# 模型检测工具汇总


[https://blog.csdn.net/yingzinanfei/article/details/54808684?utm\_medium=distribute.pc\_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase&depth\_1-utm\_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase](https://blog.csdn.net/yingzinanfei/article/details/54808684?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase)




面向形式化规格语言的模型检测工具

SMV(Symbolic Model Verifier) 符号模型检测工具

SMV用以检测一个有限状态系统是否满足CTL公式。
它的建模方式是以模块为单位，模块可以同步或异步组合，模块描述的基本要素包括非确定性选择，状态转换和并行赋值语句。
其模型检测的基本方法是以二叉图表示状态转换关系，以计算不动点的方法检测状态的可达性和其所满足的性质。
> http://www.cs.cmu.edu/~modelcheck/smv.html
NuSmv(New Symbolic Model Verifier) 新符号模型检测工具

对SMV重构的一个模型检测工具
支持计算树逻辑CTL和线性时序逻辑LTL描述的所有规范
整合了以SAT为基础的有界模型检测技术
> http://nusmv.fbk.eu/
nuXmv 分析同步有限状态和无限状态系统的新符号模型检测工具

扩展于NuSMV
对于有限状态的情形，nuXmv特点是基于SAT算法的有效验证引擎
对于无限状态的情形，nuXmv特点是基于SMT的验证技术，与MathSAT5紧密集成
> https://nuxmv.fbk.eu/
Uppaal(Uppsala University & Aalborg University) 时间自动机的模型检测工具

建模和模拟及验证实时系统的工具
> http://www.uppaal.org/
STeP(Stanford Temporal Prover) 斯坦福时间验证器

用模型检测器处理子系统的验证问题
用定理证明器将结果汇总处理
不限于有限状态系统
用推论方式联合模型检测应用于更广泛的系统，包括无限数据域的程序
> http://www-step.stanford.edu/
CWB(Concurrency Workbench) 适用于并发系统操作与分析的自动化工具

可以检测系统模型之间的等价关系、FRE-ORDER关系和系统是否能够满足$\mu$-演算的公式
建模方法使用CCS语言或LOTOS语言的子集
- 能分析给定程序的状态空间及检测多种语义的等价性和序列性
> http://homepages.inf.ed.ac.uk/perdita/cwb/
VIS(Verification Interacting with Synthesis) 用于形式验证、综合和模拟有限状态系统的工具

能够综合有限状态系统并验证这些系统的属性
> http://vlsi.colorado.edu/~vis/
面向源程序语言的模型检测工具

SPIN(Simple Promela Interpreter) 显式模型检测工具

SPIN用以检测一个有限状态系统是否满足PLTL公式及其他一些性质，包括可达性和循环。
建模方式是以进程为单位，进程异步组合，进程描述的基本要素包括赋值语句，条件语句，通讯语句，非确定性选择和循环语句。
基本方法是以自动机表示各进程和PLTL公式，以计算这些自动机的组合可接受的语言是否为空的方法检测进程模型是否满足给定的性质。
建模语言为PROMELA(PROcess MEta LAnguage)，基于进程结构，有类似C语言的结构
> http://spinroot.com/spin/whatispin.html
BLAST(Berkeley Lazy Abstraction Software Verification Tool) C程序的时序安全属性自动验证工具

基于反例引导的抽象求精框架对C语言程序进行检测
采用懒惰抽象(lazy abstraction)技术，有效地提高了效率
> http://cseweb.ucsd.edu/~rjhala/blast.html
SLAM C程序模型检测工具

将原C语言程序抽象为布尔程序进程验证工作
抽象后的程序仅剩下布尔变量
依靠C2bp,Bebop,**Newton**3个工具分别负责完成抽象、检测和抽象求精任务
> https://www.microsoft.com/en-us/research/project/slam/
JPF(Java Path Finder) Java程序验证工具

实现了一个MC-JVM来解决内存分配和垃圾回收等问题
> http://babelfish.arc.nasa.gov/trac/jpf
VeriSoft 直接测试C源代码

Eraser 能够检测Java代码
Jchecker C程序模型检测工具 
基于谓词抽象理论
采用基于谓词抽象的反例引导的抽象求精框架
能够针对C程序源码抽象出模型并完备地搜索其状态空间，以此验证程序的安全属性
最大限度缩减状态空间
Bandera 并发Java程序的模型检测工具

工具平台
基于程序切片技术，将Java程序转换成中间代码
后端接口适应多种模型检测器，包括SPIN和SMV
> http://bandera.projects.cs.ksu.edu/
Klocwork InsightPro 可以检测多种语言类型的多种质量缺陷和安全漏洞

CMC 可以检测C语言程序在执行时OS层级的调度
MaceMC 用于检测分布式系统 
http://www.macesystems.org/wiki/macemc
Chess 用于检测多线程的Windows程序

> https://www.microsoft.com/en-us/research/project/chess-find-and-reproduce-heisenbugs-in-concurrent-programs/
FDR

> https://www.cs.ox.ac.uk/projects/fdr/
Murphi 一种枚举显示状态的模型检测器，针对C语言

> http://formalverification.cs.utah.edu/Murphi/
MoonWalker 针对.NET应用的模型检测工具

XMC 对JAVA程序中同步操作算法检测
FLAVERS(FLow Analysis for VERification of Systems 针对ADA语言的工具

> http://formalverification.cs.utah.edu/Murphi/
Mocha 针对C语言的模型检测工具

> https://www.cis.upenn.edu/~mocha/
CBMC 针对C语言/C++的模型检测工具

> http://www.cprover.org/cbmc/
MAGIC(Modular Analysis of proGrams In C) 针对C语言的模型检测工具

> http://www.cs.cmu.edu/~chaki/magic/
其他模型检测工具

OFMC 一种用于安全协议的符号模型检测工具
CoPS 持久安全性检测器
Rational Tau
F-Soft
IMPACT
Astree analysis tool
Saturn
Calysto
Terminator
SATABS
Terminator
mCRL2(micro Common Representation Language) 并发系统检测工具
LTSA(Labeled Transition System Analyzer) 并发系统检测工具
Maude 基于逻辑语义的工具
ISP MPI程序的检测工具
CHIC(Checker for Interface Compatibility) 模块行为兼容性的验证工具
MRMC(Markov Reward Model) 对离散和连续时间的马尔可夫激励模型
UMLChecker UML模型检测工具
BACH(Bounded ReachAblity CHecker) 用于分析线性混成自动机有界可达性分析
LDPChecker 针对正环闭合自动机(Positive Loop-closed Automata)检验线性时段性质
QRDChecker 针对时段时序逻辑QRDC(Quantified Restrictred Duration Calculs)的检验工具
Kronos
HyTech
AUTOABS
FeaVer
3VMC
aSpin
其他分类方式

结合模型检测与定理证明 
STeP
符号模型检测 
用有序二叉图OBDDs(Ordered Binary Decision Diagrams)描述状态迁移图
用布尔逻辑公式描述系统属性
定界模型检测技术(bounded model checking) 
依赖于布尔可满足性问题(boolean satisfiability problem, SAT)的求解器
在限定步数k内，确定系统是否满足性质。
若不能确定，则增加k值，重新进行验证
其他分类方式

基于自动机理论 
SPIN
基于不动点定理 
SMV
其他分类方式

针对实时系统的模型检测工具 
UPPAAL, Kronos, STeP
针对并发系统的模型检测工具 
Spin, JPF, Verisoft
针对混成系统的模型检测工具 
HyTech, HySAT, BACH, LDPChecker
模型检测的步骤：

抽象出系统的数学模型 
迁移系统
马尔可夫链
Kripke结构
给出能够描述该系统性质的语言 
线性时序逻辑LTL 
关心系统的任意一次运行中的状态以及它们之间的关系
分支时序逻辑CTL 
分叉时序逻辑，用来描述状态的前后关系和分支情况
$\mu$-演算 
关心系统的动作与状态之间的关系
















