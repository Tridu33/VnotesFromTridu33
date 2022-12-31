

# 基于逻辑的形式验证方法（定理证明器COq模型检测）



cnblogs.com/westRiver/articles/5087039.html

近年来, 形式化方法发展很快,一些技术已经产生工业应用。以逻辑系统为主线,分析几个影响力比较大的形式化验证技术和验证工具,以帮助应用工程师选择并使用形式化工具。主要包括命题演算和时态逻辑方面的SAT、BDD、模型检测和SMT, 谓词逻辑方面的ACL2、VDM 方法和B 方法,以及高阶逻辑方面的HOL、PVS和COQ。还介绍形式化方法在学术界和工业界的应用情况,最后给出几个商业化的形式化验证工具。

关键词 形式化方法; 逻辑系统; 验证技术

形式化方法

定理证明、模型检测
Intel: HOL -> FORTE 系统

An Industrially Effective Environment for Formal Hardware Verification
形式验证公司

JASPER
FORMALITY
Calypto











1 命题演算和SAT 求解器
命题演算(propositional calculus)

描述和证明两个组合电路的等价性
基本问题: 可满足性(Satisfiability)和永真性
命题演算证明问题两个重要特点

可判定性, 即可构造出自动化算法, 证明任一命题可满足性
证明复杂性。命题演算判定问题是一NP完全性问题
命题演算自动证明方面两个重大进展

BDD 技术: binary decision diagram
Graph-based algorithms for Boolean
function manipulation
SAT 求解器
David-Putnam搜索技术(DP 方法)
基本SAT 求解技术主要分成两类

基于冲突分析(conflict analysis)技术
Grasp, Sato, Chaff, MiniSat, Berk-Min,Siege 和MaxSAT
基于前向分析(lookahead)技术,
Bohm, Posit, Satz,EqSatz, OKsolver, March_dl 和Kcnf等[5]
2 时态逻辑和模型检测工具
3 类特性

安全性(safty properties)
某些状态(不好的)永远不会到达;
活性(liveness properties)
某种期待的良好性质迟早会成立
公平性(fairness)
系统提供的各项服务都将有平等机会执行
模型检查[6] -> 时态逻辑

模型检测选择因素

特性描述语言:
命题逻辑、LTL 或CTL,PSL(property specification language)
模型描述语言
C, JAVA,VHDL等源代码,或Promela
模型检查工具
CBMC
Behavioral consistency of C and verilog programs using bounded model checking
Cadence SMV
UPPAAL
3 SMT 求解器
SMT[10]
Ackerman 化方法
组合论么？

4 谓词逻辑及一阶定理证明器
谓词逻辑重要证明技术: 消解法(resolution),
核心证明规则是一条消解规则:
¬A∨B,A∨C⇒B∨C

4.1 ACL2
ACL2 [16]: 谓词逻辑定理证明器
4.2 维也纳方法(VDM)
Z 方法[22]
Larch[23
4.3 B 方法
Event-B[26]
5 高阶逻辑和证明助手
高阶逻辑 vs. 类型理论
LEGO[34]
COQ
5.1 HOL
5.2 PVS

5.3 COQ
四色问题
6 形式化方法的应用方式
6.1 对实际系统或系统部分的验证
Contract
基于C#的Spec#[40]
基于Java 的JML[41]
6.2 系统的形式化建模和验证
6.3 基于形式化方法的系统开发
7 商业化的形式化工具
Z3
Z3 source
8 结语
图1 概括描述本文涉及的逻辑系统、证明技术和证明工具


Formality 和JASPER
COQ
Coq
Coq: 证明辅助工具,提供一个函数式编程语言与和一个基于高阶逻辑的推理框架

Coq里面命题是类型，程序则证明
数学上,Coq用于验证四色定理
seL4: formal verification of an OS kernel

CompCert

完全证明的C语言编译器?
Certified Software = Program + Proof
Formal verification of a realistic compiler
其它证明辅助工具

Isabelle
Twelf
Agda
dependent type

Ynot: a library for the Coq proof assistant which turns it into a full-fledged environment for writing and verifying imperative programs.

ATS

Hongwei Xi
辅酶Q10: 同名不同质

Coq演化
1970 年代
LISP 语言 -> 一阶逻辑证明器SAM
System F: 多态 λ 演算
ML语言
1980年代
SOS: 结构化操作语义
Objective Caml 语言 -> Coq 证明器的实现语言
构造演算（Calculus of Constructions）
1990 年代
2000年
图形界面PCoq
Reference
Interactive Theorem Proving and Program Development
交互式定理证明与程序开发 Coq归纳构造演算的艺术, 中文版
Certified Programming with Dependent Types: online
Software Foundations: online book
经典Coq教材
Benjamin C. Pierce
定理证明
Isabelle: 基于高阶逻辑的定理辅助证明系统

PVS: a specification language integrated with support tools and a theorem prover

spin

Promela 不支持如浮点数、引用、指针等语言特性
Java PathFinder

Java -> Promela -> SPIN
相当于语法翻译器，将Java程序转化为Promela程序，再利用SPIN验证
MoonWalker: model checking .NET applications

ref

Reliability analysis in symbolic pathfinder
Java多线程程序的测试
NuSMV: 是SMV的重新实现和扩展,且是第一个基于BDDs

计算树逻辑CTL
CADP

FDR 3: Failures-Divergence Refinement
The CSP refinement checker






























































































