# 《Z形式规约的自动求精研究》












王宏生 手下的硕士学生文章 http://cdmd.cnki.com.cn/Article/CDMD-10142-2005083087.htm Z规格说明中一阶逻辑算子自动求精的研究与实现




随着计算机产业的快速发展,软件的开发规模不断扩大,对软件开发效率和安全性的要求也越来越高,各种开发方法应运而生。Z语言作为一种软件工程语言和形式化方法,在软件文档规范化的应用中成效显著。近年来,国内外对Z语言的研究也逐渐增多。Z语言与其它符号系统相比,一个显著特点是它的规格说明可以用于推理和求精。

以往的这种求精过程都由人工完成的,它自动求精实现却进展缓慢。

本文以Z规格说明的自动求精为目的,通过约束Z语言中计算机不能实现或不易实现部分,设计出Z语言的一个子集Smart Z,并以标准C++和STL为工具,运用编译技术实现了Smart z规格说明中一阶逻辑算子自动求精。 判断计算机是否可以完成自动求精,关键取决于能否找到实现规格说明的语法、语义的算法。本文将语法、语义的实现问题归约到某一个可解问题,并通过在“通用计算机模型”——图灵机上运行这个可解问题的算法,来证明规格说明求精可判定性。

Smart Z继承了Z语言的整型、集合和谓词等,同时保证了其规格说明可求精性,并以一套形式化的方法——正则表达式和EBNF范式描述了它的语言体系。本文使用编译技术实现Smart Z的语法分析、语义分析及向目标代码的转换,本文又针对规格说明的自身特点,对相关算法加以改进,为一阶逻辑算子自动求精的实现创造条件。

Smart z的一阶逻辑算子包括量词和连接词等,本文给出它们的求精算法,并以一个**实例**演示了规格说明和逻辑算子的自动求精过程。

本文最后的结论是“Z语言经过适当的约束后,一阶逻辑算子的自动求精是可以实现的”,这是Z规格说明自动求精目标实现的一个重要前提,也是为实现自动化程序设计做出的一次有意义的尝试。



























