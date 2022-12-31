[TOC]



The HOL Light theorem prover.http://www.cl.cam.ac.uk/jrh13/hol-light/

Isabelle.http://www.cl.cam.ac.uk/research/hvg/Isabelle/



# 1. isabelle

高阶逻辑辅助证明系统isabelle




证明算法程序正确性的三种形式化方法：Floyd 归纳断言法、Hoare 公理法以及Dijkstra 最弱前置谓词法；然后通过几个实例探讨了如何运用 Isabelle 定理证明器形式化验证算法程序的工作流程；最后，阐述了如何使用 Isabelle 证明 PAR平台自动生成系统中部分核心算法的正确性。cnki paper------PAR 方法是薛锦云教授提出的基于分划和递推的算法程序设计方法；它是一种简单实用的支持算法程序开发全过程的形式化方法

操作系统形式化验证实践教程(1) - 证明第一个定理
https://blog.csdn.net/lusing/article/details/107783309
























# 2. isabelle高阶逻辑证明

托比亚斯·尼普科夫、(英)劳伦斯·鲍尔森、玛尔库斯·温泽尔编著的《高阶逻辑辅助证明系统(精)》是在高阶逻辑中使用Isabelle辅助证明系统进行交互式证明的导论，适用于Isabelle系统的潜在使用者，自成体系，分为三部分：第一部分是基本技巧：介绍在高阶逻辑中如何进行函数式程序建模，提供了表(1ist)和自然数的简单证明实例。大多数证明只要两步完成：对所选变量进行归纳以及使用自动策略(auto)。当然，这些粗浅的例子仍然涵盖了嵌套递归和交叉递归等技术。第二部分是逻辑与集合：介绍大量可供选择使用的低级证明策略。本部分描述了Isabelle／HOL如何处理集合、函数、关系以及如何实现递归定义集合，包括模型检验理论和经典教科书中关于形式语言的案例。第三部分是话题：包括实数、记录、重载技术等主题。本部分也讨论了归纳法和递归方法的技巧，还专门给出一章来介绍安全协议的形式化验证。






官网教程文档






isabelle.in.tum.de/documentation.html


各种文档，都是PDF版本，HTML,或者latex版本就要编辑转化一下。













理论文件展示
[http://isabelle.in.tum.de/library/HOL/](http://isabelle.in.tum.de/library/HOL/)





形式证明档案


[https://www.isa-afp.org/](https://www.isa-afp.org/)

正式证明档案是证据库，示例和更大的科学发展的集合，在定理证明者[Isabelle中进行](http://isabelle.in.tum.de/)机械检查。它以科学期刊的方式组织，由[dblp](http://dblp.uni-trier.de/db/journals/afp/)索引并具有ISSN：2150-914x。提交的内容均经过审核。首选引用风格[\[此处\]](https://www.isa-afp.org/citing.html)。我们鼓励AFP提交会议和期刊出版物。











HOL=函数编程+逻辑


第一部分 基本技巧  

第一章 基础  

1．1 引言  

1．2 theory(理论)  

1．3 类型，项和公式  

1．4 变元  

1．5 交互与界面  

1．6 启动  

第二章 HOL中的函数编程  

第三章 函数式编程  

第四章 theory的表示  

第二部分 逻辑与集合  

第五章 游戏规则  

第六章 集合、函数和关系  

第七章 集合递归定义  

第八章 高级types  


nat cos,tan，log.无穷大omega和无穷小epsilon,无限接近也能定义，非标准实数，极限微分积分很容易实现（Mechanizing non-standrad real anaysis [J]文中写道）

有理数完备实数RComplete理论文件中有完备性定义

HOL_completx理论文件中有rat,real,complex类型

可使用HOL-NSA逻辑的理论文件是Hyperreal理论文件，有超越函数sin......几十个类型类，半环有序半环，环有序环，域有序域，除零等几百条引理。















Ring_and_Field理论文件中有很多数值理论文件，通过公理类型类来组织，a/0=0



第九章 化简与归纳  

第十章 案例学习：验证安全协议  

附录  

参考文献  

译后记一






mathematical Anaysis       isabelle           website:github.com

mathematical Anaysis       isabelle     filetype:PDF


# 3. 周边

www.voidcn.com/article/p-rkuqqdrh-byn.html



我正在阅读 [“Concrete semantics with Isabelle/HOL”](javascript:void()),我对高阶逻辑非常感兴趣.我知道普通的一阶逻辑和一些模态逻辑,但如果之前没有接触到高阶逻辑及其元理论,我几乎没有,所以我想填补空白.我读到HOL本质上是Church的简单类型理论而Pure是前者的直觉变体.问题是“基本上”这个词：Isabelle / HOL和Isabelle / Pure理论与例如 [Andrews’ textbook](javascript:void())有何不同？是否有关于Isabelle / HOL和Isabelle / Pure中使用的高阶逻辑的教科书介绍,并讨论了它们的元理论特性？

关于HOL及其众多变体和方言,可以说很多.这是 [Isabelle](javascript:void())和其他 [HOL](javascript:void())系统邮件列表上的一个经常性主题.例如,以下是2013年1月/ 2月关于isabelle用户的相关帖子： [Where to learn about HOL vs FOL?](javascript:void())以及对相关文献的更多参考.

在[Isabelle/Isar Implementation](javascript:void())手册第2节“原始逻辑”中,还有一些关于Isabelle / Pure(最小HOL)逻辑的内容.





Isabelle系统分布
版本信息
这是Isabelle2019: 2019年6月。
有关用户相关的详细信息，请参阅分发版中的新闻文件
的变化。
安装
Isabelle工作在三个主要的平台家族:Linux, Windows，
和macOS。应用程序从Isabelle web页面绑定
包括所有受支持的源、文档和附加工具
平台。
一些技术背景信息可以在Isabelle中找到
系统手册(目录doc)。
用户界面
Isabelle/jEdit是一个基于jEdit and的高级验证IDE
伊莎贝尔/ Scala。它是应用程序的主要实例
的默认用户界面
伊莎贝尔。它提供了a的连续证明检查的隐喻
理论资源的版本化集合，具有即时反馈
在实时和丰富的语义标记相关的形式化
文本。
其他资料来源
伊莎贝尔页面
Isabelle主页可以从以下镜像访问
网站:
* https://www.cl.cam.ac.uk/research/hvg/Isabelle
* https://isabelle.in.tum.de
* https://mirror.cse.unsw.edu.au/pub/isabelle
* https://mirror.clarkson.edu/isabelle
邮件列表
电子邮件列表isabelle-users@cl.cam.ac。英国提供了一个
论坛为Isabelle用户讨论问题和交流
信息。要加入，请发送消息到
isabelle-users-request@cl.cam.ac.uk。
个人邮件
劳伦斯C保尔森
计算机实验室
剑桥大学
JJ汤姆森大街
剑桥CB3 0 fd
英格兰
电子邮件:lcp@cl.cam.ac.uk
电话:+ 44-223-763500
传真:+ 44-223-334748
或
托拜厄斯Nipkow
为了研究所Informatik
科技想象图
Boltzmannstr。3.
d - 85748来自
德国
电子邮件:nipkow@in.tum.de
电话:+ 49-89-289-17302
传真:+ 49-89-289-17307
_________________________________________________________________
请报告你遇到的任何问题。而我们将努力做到
有益的，我们可以接受没有责任的不足之处
伊莎贝尔和他们的后果。
_________________________________________________________________












```isabella

admin@Tridu ~/Documents/Isabelle/Isabelle2019/src/Doc
$  isabelle build -D .
Running Classes ...
Finished Classes (0:00:04 elapsed time)
Running Codegen ...
Finished Codegen (0:01:40 elapsed time)
Building Datatypes ...
Finished Datatypes (0:01:50 elapsed time)
Running Corec ...
Finished Corec (0:01:31 elapsed time)
Running Eisbach ...
Finished Eisbach (0:00:05 elapsed time)
Running Functions ...
Finished Functions (0:00:05 elapsed time)
Running How_to_Prove_it ...
Finished How_to_Prove_it (0:00:01 elapsed time)
Running Implementation ...
Finished Implementation (0:00:06 elapsed time)
Running Intro ...
Finished Intro (0:00:00 elapsed time)
Running Isar_Ref ...
Finished Isar_Ref (0:00:26 elapsed time)
Running JEdit ...
Finished JEdit (0:00:02 elapsed time)
Running Locales ...
Finished Locales (0:00:03 elapsed time)
Running Logics ...
Finished Logics (0:00:00 elapsed time)
Running Main ...
Finished Main (0:00:02 elapsed time)
Running Nitpick ...
Finished Nitpick (0:00:00 elapsed time)
Running Prog_Prove ...
Finished Prog_Prove (0:00:08 elapsed time)
Running Sledgehammer ...
Finished Sledgehammer (0:00:00 elapsed time)
Running Sugar ...
Finished Sugar (0:00:02 elapsed time)
Running System ...
Finished System (0:00:01 elapsed time)
Running Tutorial ...
Finished Tutorial (0:00:35 elapsed time)
Running Typeclass_Hierarchy ...
Finished Typeclass_Hierarchy (0:00:14 elapsed time)
Building ZF ...
Finished ZF (0:00:27 elapsed time)
Running Logics_ZF ...
Finished Logics_ZF (0:00:00 elapsed time)
0:08:11 elapsed time


```

文件在哪儿？










































