









Most modern SAT solver are based on the Davis-Putnam-Logemann-Loveland(DPLL) paradigm

有个新标准是SMT-lib很好用的写法

SMT-Lib: library of benchmarks

http://www.smtlib.org

SMT-LIB and some common theories


The satisfiability modulo theories library (smt-lib).http://goedel.cs.uiowa.edu/smtib






# 1. SMT-LIB















可满足性模理论（SMT）



http://smtlib.cs.uiowa.edu/






创建SMT-LIB的期望是，通用标准和基准库的可用性将极大地促进SMT系统的评估和比较，并以与例如在TPTP库已经做了定理证明，或SATLIB库已初步完成了周六

这些期望基本上得到了满足，这在很大程度上要归功于研究界的广泛贡献以及基于库基准测试的SMT求解器年度竞赛SMT-COMP。但是，该计划仍在进行中，旨在提高SMT-LIB语言的实用性和范围，定义新的背景理论并收集更多基准。

关于SMT
可满足性模理论（SMT）是自动推论的一个领域，它针对感兴趣的某些逻辑理论T研究用于检查一阶公式的可满足性的方法。它与一般的自动推论的不同之处在于，背景理论T不必是有限的，甚至不必是一阶公理化的，并且每种理论都使用了专门的推理方法。通过特定于理论并将其语言限制为某些类别的公式（例如，但不限于无量词公式，通常但不限于此），可以在求解器中实施这些专用方法，与通用定理证明者相比，这些求解器在实践中效率更高。

尽管SMT技术传统上一直用于支持演绎软件验证，但它们现在在计算机科学的其他领域中找到了应用，例如计划，模型检查和自动测试生成。


这些应用中的典型兴趣理论包括**算术，数组，位向量，代数数据类型，与未解释函数的相等性以及这些形式的各种组合的形式化**。

家
关于
消息
标准
语
理论
逻辑学
例子
基准测试
软件
解算器
实用工具
接触
有关的
学分


http://smtlib.cs.uiowa.edu/benchmarks.shtml
SMT-LIB基准存储库托管在SMT-LIB GitLab https://clc-gitlab.cs.uiowa.edu:2443/explore/groups 服务器上。读取访问权限不需要帐户。版本存储在master分支中。当前版本在头。


Non - incremental benchmarks


ABVFP， ALIA， AUFBVDTLIA， AUFDTLIA， AUFLIA， AUFLIRA， AUFNIA， AUFNIRA， BV， BVFP， FP， LIA， LRA， NIA， NRA， QF_ABV， QF_ABVFP， QF_ALIA， QF_ANIA， QF_AUFBV， QF_AUFLIA， QF_AUFNIA， QF_AX， QF_BV， QF_BVFP， QF_BVFPLRA， QF_DT， QF_FP， QF_FPLRA， QF_IDL， QF_LIA， QF_LIRA， QF_LRA， QF_NIA， QF_NIRA， QF_NRA， QF_RDL， QF_S， QF_SLIA， QF_UF， QF_UFBV， QF_UFIDL， QF_UFLIA， QF_UFLRA， QF_UFNIA， QF_UFNRA， UF， UFBV， UFDT， UFDTLIA， UFDTNIA， UFIDL， UFLIA， UFLRA， UFNIA


incremental benchmarks


ABVFP， ALIA， ANIA， AUFNIRA， BV， BVFP， LIA， LRA， QF_ABV， QF_ABVFP， QF_ALIA， QF_ANIA， QF_AUFBV， QF_AUFBVLIA， QF_AUFBVNIA， QF_AUFLIA， QF_BV， QF_BVFP， QF_FP， QF_LIA， QF_LRA， QF_NIA， QF_UF， QF_UFBV， QF_UFBVLIA， QF_UFLIA， QF_UFLRA， QF_UFNIA， UFLRA
有关如何克隆每个存储库的说明，请参见存储库空间。您也可以下载此bash脚本，取消注释与要克隆的逻辑/存储库相关的行，然后运行它。注意：大小为10MB以上的基准是通过Git LFS存储的。克隆任何存储库之前，您将需要安装和设置Git LFS。







tools

http://smtlib.cs.uiowa.edu/utilities.shtml































科普 - 程序验证（2）- 不变式 - FRONTIERS的文章 - 知乎
https://zhuanlan.zhihu.com/p/299781093







