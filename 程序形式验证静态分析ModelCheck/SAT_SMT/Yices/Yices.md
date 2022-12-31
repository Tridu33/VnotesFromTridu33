




Yices: An SMT solver. http://yices.csl.sri.com/.

ices 2是可满足性模理论 （SMT）问题的解决方案。Yices 2可以处理以SMT-LIB语言或Yices自己的规范语言编写的输入。我们还提供了Java，Python，Go和OCaml的C API 和绑定。

https://github.com/SRI-CSL/yices2

该存储库包括Yices 2的源代码，文档，测试和示例。

Yices 2由SRI International计算机科学实验室的Bruno Dutertre，Dejan Jovanovic，StéphaneGraham-Lengrand和Ian A. Mason开发。要联系我们或获取有关Yices的更多信息，请访问我们的 网站。

https://yices.csl.sri.com/papers/tool-paper.pdf
the yices DPPL-based SAT Solver


Solving Exists/Forall Problems With Yices https://yices.csl.sri.com/papers/smt2015.pdf


# 1. Yices
SMT代表可满足性模理论。SMT求解器确定具有相等性的理论中命题复杂公式（例如算术和未解释函数）的可满足性。SMT解决方案在自动定理证明，硬件和软件验证以及计划和计划问题中具有众多应用。本文介绍了由IRI International开发的高效SMT求解器Yices。Yices支持在软件和硬件建模中经常发生的一阶理论的丰富组合：算术，未解释的函数，位向量，数组，递归数据类型等。除了纯粹的SMT解决方案之外，Yices还可以解决MAX-SMT加权问题，计算不满意的核以及构建模型。Yices是SAL模型检查环境使用的主要决策过程，并且已集成到PVS定理证明者中。作为MAX-SMT求解器，Yices是SRI的CALO系统中使用的概率一致性引擎的主要组成部分。 https://www.researchgate.net/publication/228358762_The_Yices_SMT_solver





https://yices.csl.sri.com/








Yices SMT解算器

Yices 2是一种SMT 求解器，用于确定包含具有相等性，实数和整数算术，位向量，标量类型和元组的未解释函数符号的公式的可满足性。

Yices 2支持线性和非线性算法。

Yices 2可以处理以SMT-LIB https://smt-lib.org/
表示法编写的输入 （同时支持版本2.0和1.2）。另外，您可以使用Yices 2自己的规范语言（包括元组和标量类型）编写规范。您也可以将Yices 2用作软件中的库。



```
sudo add-apt-repository ppa:sri-csl/formal-methods
sudo apt-get update
sudo apt-get install yices2
```

https://yices.csl.sri.com/yices2-documentation.html 文档



































