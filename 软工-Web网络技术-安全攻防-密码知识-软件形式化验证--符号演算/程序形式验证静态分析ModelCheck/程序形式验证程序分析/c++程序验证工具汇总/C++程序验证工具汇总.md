




《形式化方法的研究进展与趋势》


目前软件形式化验证工具的主流技术有两种：基于抽象的技术路线和基于循环/递归 展开的技术路线。前者利用抽象技术将程序状态空间映射到一个有限且规模较小的抽象 状态空间，再通过遍历所有可达的抽象状态来判断系统是否正确。采用抽象路线的软件 形式化验证工具包括 SLAM[476]、BLAST[472]、CPAChecker[475]、UAutomizer[477]等。后者 将程序中所有循环和递归按给定的深度展开，得到一个不含循环和递归的简单程序。这 类简单程序的验证问题被归结为一个逻辑公式的可满足性问题，再借助已有的SMT工具 (如Z3、MathSAT、Yi=s) 进行求解。采用循环/递归展开技术路线的软件形式化验证工



具包括 CBMC[474]、ESBMC"479]、215[473]等0以抽象解释为代表的程序分析工具近年来也得到了长足发展。

相关工具不断涌现， 出现了 PolySpace"48。]、Ast2e[481]、aiTWCETAnalyzer"482]、CodeHawk"483]、Sparrow"484]、 Zoncolan % Facebook )、Julia[485]等商业化工具和 Frama-CValueAnalysis[486]、CCCheck % CodeContractStaticChecker) [487]、Interproc"448]、crab-llvm[489]、IK0S[49。]、MemCAD[491]、 Fluctuat[492]、Jandom[493]、JsCFA[494]、MuJS[495]等学术界工具〇 Min6 等人基于 Ast2e 开 发了面向异步实时程序的扩展版本Ast2eA，以支持多线程C程序中运行时错误、数据竞 争、死锁等错误的检测，并成功分析了 ARINC 653航空应用（约220万行代码）[525-526]。

软件形式化验证工具的一个发展趋势是模型检测技术与抽象解释等程序分析技术的融 合。

Beyei•等人在 2007 年提出可配置程序分析 ％ ConfigurableProgramAnalysis，CPA)[478]的 思想，实现了静态分析与模型检测在一个理论框架下的融合。基于可配置程序分析的软 件验证工具CPACheckei•曾4 次 （2012、2013、2015和2018年）夺得国际软件验证大赛 总成绩的冠军。Heizmann等人于2013年提出了一种融合自动机理论[477的软件验证方 法。他们基于该方法实现的UAutomizer工具连续夺得2016年和2017年国际软件验证大 赛总成绩第一名。

作为程序的一种重要形态，并行程序验证成为目前形式化验证的一个热点领域。国 际上出现了较多的并行程序验证工具。

这些工具分别使用了偏序规约、限界模型检测、 抽象精化、组合验证等技术，支持PThread、OpenMP以及MPI等并行框架，可以对常见 静态属性和用户自定义断言属性进行验证。由于并行程序的行为空间异常复杂，目前这 一领域的工具开发还处于学术研究阶段，国际上针对并行程序验证的主流工具有 CBMC[5。7]、ESBMC[479]、Lazy-CSeq[496]、SMACK"497]、以及 CPA-Seq[498]等。随着软件形式化验证工具的日益完善，软件形式化验证在工业界软件，尤其是操作 系统、驱动程序、嵌人式程序的分析与验证中得到了成功应用。耶鲁大学采用形式验证 开发了一个全新的操作系统CertiK0S[499]，号称是世界上第一个“没有Hug”的反黑客攻 击操作系统。美国国防高级研究计划局（DARPA) 在2012~2017年实施了一个HACMS 项 目 ％ High-AssuranceCyberMilitarySystem) [5。。]，采用了形式验证方法，在开发一套开源 的、高安全确保的操作系统和控制系统组件。微软研究院目前正和卡内基梅隆大学等合 作，开展一项雄心勃勃的程序证明项目，即 “珠穆朗玛峰（Ever:)”项目[5。1]。亚马逊 针对其云计算IaaS和PaaS平台的S3 对象存储系统、DynamoDBNoSQL数据库服务、EBS 弹性块存储服务等10个系统上使用了形式化验证，显著提高了系统的安全可靠性[5。2














# 1. C++程序验证工具汇总




https://blog.csdn.net/wcventure/article/details/105301599






























