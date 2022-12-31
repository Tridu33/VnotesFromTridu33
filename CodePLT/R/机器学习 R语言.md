




# 机器学习 R语言

https://cran.r-project.org/web/views/MachineLearning.html




一些附加程序包实现了在计算机科学和统计学之间的边界开发的思想和方法-该研究领域通常称为机器学习。这些软件包可以大致分为以下主题：

-   *神经网络和深度学习* ：单层神经网络在软件包[nnet](https://cran.r-project.org/web/packages/nnet/index.html)中实现 （随R一起提供）。软件包 [RSNNS](https://cran.r-project.org/web/packages/RSNNS/index.html) 提供了到斯图加特神经网络模拟器（SNNS）的接口。实现神经网络深度学习风格的软件包包括 [Deepnet](https://cran.r-project.org/web/packages/deepnet/index.html) （前馈神经网络，受限Boltzmann机器，深度置信网络，堆叠式自动编码器）， [RcppDL](https://cran.r-project.org/web/packages/RcppDL/index.html) （去噪自动编码器，堆叠式去噪自动编码器，受限Boltzmann机器，深度置信网络）和 [h2o](https://cran.r-project.org/web/packages/h2o/index.html) （前馈神经网络，深层自动编码器）。在[ tensorflow ](http://www.tensorflow.org/)中可以使用 [tensorflow](https://cran.r-project.org/web/packages/tensorflow/index.html)的接口 。
-   *递归分区* ：遵循CART手册中的思想，用于树状结构的用于回归，分类和生存分析的[模型](https://cran.r-project.org/web/packages/rpart/index.html)是在 [rpart](https://cran.r-project.org/web/packages/rpart/index.html) （以R为基础）和 [tree中实现的](https://cran.r-project.org/web/packages/tree/index.html)。 建议使用软件包 [rpart](https://cran.r-project.org/web/packages/rpart/index.html)来计算类似CART的树。[ Weka ](http://www.cs.waikato.ac.nz/~ml/weka/)提供了丰富的分区算法工具箱 ，软件包 [RWeka](https://cran.r-project.org/web/packages/RWeka/index.html)提供了此实现的接口，包括C4.8和M5的J4.8版本。该 [立体派](https://cran.r-project.org/web/packages/Cubist/index.html) 程序包将基于规则的模型（类似于树）与终叶中的线性回归模型，基于实例的校正和增强进行拟合。在 [C50](https://cran.r-project.org/web/packages/C50/index.html) 包可以容纳C5.0分类树，以规则为基础的模型，并提振了这些版本。  
    在package [party](https://cran.r-project.org/web/packages/party/index.html) 和 [partykit](https://cran.r-project.org/web/packages/partykit/index.html)中实现了两种具有无偏变量选择和统计停止准则的递归划分算法 。函数 ctree（） 基于非参数条件推理过程，用于测试响应和每个输入变量之间的独立性，而 mob（） 可用于分区参数模型。软件包[party](https://cran.r-project.org/web/packages/party/index.html) 和 [partykit](https://cran.r-project.org/web/packages/partykit/index.html) 中也提供了用于可视化响应的二叉树和节点分布的可扩展工具 。 [maptree](https://cran.r-project.org/web/packages/maptree/index.html)  
    包中提供了用于可视化树的图形工具 。 软件包[REEMtree](https://cran.r-project.org/web/packages/REEMtree/index.html)提供了通过随机效应对纵向数据建模的树 。混合模型的划分由[RPMM](https://cran.r-project.org/web/packages/RPMM/index.html)执行 。[](https://cran.r-project.org/web/packages/maptree/index.html)  
    [](https://cran.r-project.org/web/packages/REEMtree/index.html)[](https://cran.r-project.org/web/packages/RPMM/index.html)  
    在[partykit中](https://cran.r-project.org/web/packages/partykit/index.html)实现了用于表示树木的计算基础结构以及用于预测和可视化的统一方法 。包[evtree](https://cran.r-project.org/web/packages/evtree/index.html)使用此基础 [结构](https://cran.r-project.org/web/packages/evtree/index.html) 来实现全局最优树的进化学习。生存树有各种包装，[LTRCtrees除了](https://cran.r-project.org/web/packages/LTRCtrees/index.html) 允许右截尾外， [还](https://cran.r-project.org/web/packages/LTRCtrees/index.html)允许左截尾和间隔截尾。
-   *随机森林* ：可在软件包[randomForest中](https://cran.r-project.org/web/packages/randomForest/index.html)获得用于回归和分类的随机森林算法的参考实现 。[ipred](https://cran.r-project.org/web/packages/ipred/index.html)软件包 具有用于回归，分类和生存分析以及捆绑的袋装功能，通过集成学习将多个模型组合在一起。此外，在基于条件推断树上任意秤测量响应变量随机森林变体封装中实现 [党](https://cran.r-project.org/web/packages/party/index.html)。 [randomForestSRC](https://cran.r-project.org/web/packages/randomForestSRC/index.html) 对Breiman的随机森林实施生存，回归和分类问题的统一处理。分位数回归林[quantregForest](https://cran.r-project.org/web/packages/quantregForest/index.html) 允许通过随机森林方法对探索变量的数字响应进行分位数回归 。对于二进制数据， [varSelRF](https://cran.r-project.org/web/packages/varSelRF/index.html) 和 [Boruta](https://cran.r-project.org/web/packages/Boruta/index.html) 软件包着重于通过随机森林算法进行变量选择。此外，包 [RANGER](https://cran.r-project.org/web/packages/ranger/index.html) 和 [Rborist](https://cran.r-project.org/web/packages/Rborist/index.html) 为随机森林的快速C ++实现提供R接口。增强学习树以在树中重要的变量拆分为特征，在软件包[RLT](https://cran.r-project.org/web/packages/RLT/index.html)中实现 。 [wsrf](https://cran.r-project.org/web/packages/wsrf/index.html) 实现了用于变量子空间选择的替代变量加权方法，代替了传统的随机变量采样。软件包 [RGF](https://cran.r-project.org/web/packages/RGF/index.html) 是Python实施过程的接口，该过程称为正则化贪婪森林。软件包[trtf](https://cran.r-project.org/web/packages/trtf/index.html)中提供了用于参数模型的随机森林，包括用于估计预测分布的森林。 [](https://cran.r-project.org/web/packages/trtf/index.html)（可能是在审查和截断下进行的预测性转换森林）和 [grf](https://cran.r-project.org/web/packages/grf/index.html) （广义随机森林的实现）。
-   *正则化和收缩方法* ：可以在[lasso2](https://cran.r-project.org/web/packages/lasso2/index.html) 和 [lars](https://cran.r-project.org/web/packages/lars/index.html) 软件包中拟合对参数估计值有约束的回归模型 。套包[grplasso中](https://cran.r-project.org/web/packages/grplasso/index.html)提供了具有同时更新参数组（按组套索）的套索 ；所述 [grpreg](https://cran.r-project.org/web/packages/grpreg/index.html) 包实现许多其它组惩罚模型，如组MCP和组SCAD的。通用线性模型和Cox模型的L1正则化路径可以从软件包 [glmpath](https://cran.r-project.org/web/packages/glmpath/index.html)，整个套索或弹性网正则化路径（也可以在 [elasticnet](https://cran.r-project.org/web/packages/elasticnet/index.html)），用于线性回归，逻辑和多项式回归模型可以从包获得 [glmnet](https://cran.r-project.org/web/packages/glmnet/index.html)。的 [惩罚](https://cran.r-project.org/web/packages/penalized/index.html) 包提供了一种替代实施套索（L1）和脊部（L2）处罚回归模型（GLM两者和Cox模型）的。 当数据无法存储在RAM中时，[biglasso](https://cran.r-project.org/web/packages/biglasso/index.html)程序包 在L1惩罚下适合高斯和逻辑线性模型。包 [RXshrink](https://cran.r-project.org/web/packages/RXshrink/index.html) 可用于识别和显示指定收缩路径的TRACE，并确定适当的收缩程度。软件包[ahaz](https://cran.r-project.org/web/packages/ahaz/index.html)提供了套索处罚下的半参数加性危害模型 。用于线性回归的套索收缩技术的一般化称为松弛套索，可用于package [Relaxo中](https://cran.r-project.org/web/packages/relaxo/index.html)。费舍尔的一个可选的套索处罚LDA投影生成稀疏的解决方案在包中实现 [penalizedLDA](https://cran.r-project.org/web/packages/penalizedLDA/index.html)。压缩的质心分类器和用于基因表达分析的实用程序在软件包[pamr](https://cran.r-project.org/web/packages/pamr/index.html)中实现 [](https://cran.r-project.org/web/packages/pamr/index.html)。封装[土中](https://cran.r-project.org/web/packages/earth/index.html)可以使用多元自适应回归样条的实现 。在[hda](https://cran.r-project.org/web/packages/hda/index.html) 和 [sda](https://cran.r-project.org/web/packages/sda/index.html)软件包中实现了各种形式的惩罚判别分析 。软件包 [LiblineaR](https://cran.r-project.org/web/packages/LiblineaR/index.html) 提供了LIBLINEAR库的接口。该 [ncvreg](https://cran.r-project.org/web/packages/ncvreg/index.html) 线性拟合包下了的SCAD逻辑回归模型，并用坐标下降算法MCP回归处罚。[毕加索](https://cran.r-project.org/web/packages/picasso/index.html)也实行同样的惩罚 [](https://cran.r-project.org/web/packages/picasso/index.html)包。可从[bmrm](https://cran.r-project.org/web/packages/bmrm/index.html)软件包中[获得](https://cran.r-project.org/web/packages/bmrm/index.html)用于正规化风险最小化的bundle方法的实现 。通过[hdm](https://cran.r-project.org/web/packages/hdm/index.html)估计非高斯误差和异方差误差 下的Lasso，还包含对Lasso回归的低维分量的推断以及在高维环境中估计的处理效果。包 [SIS](https://cran.r-project.org/web/packages/SIS/index.html) 在广义线性和Cox模型中实现了确定的独立性筛选。各种条件下的正态和二进制逻辑线性模型
-   *Boosting和Gradient Descent* ：在[gbm](https://cran.r-project.org/web/packages/gbm/index.html)软件包 （基于树的功能梯度下降Boosting）中实现了各种形式的渐变增强 。软件包 [xgboost](https://cran.r-project.org/web/packages/xgboost/index.html) 使用高效的树作为一些和用户定义的目标函数的基础学习器，实现了基于树的增强。铰链损耗通过[bst](https://cran.r-project.org/web/packages/bst/index.html)软件包中的boosting实现进行了优化 。套餐 [GAMBoost](https://cran.r-project.org/web/packages/GAMBoost/index.html) 可通过Boosting算法用于拟合广义加性模型。软件包[mboost中](https://cran.r-project.org/web/packages/mboost/index.html)提供了用于广义线性，加性和非参数模型的可扩展增强框架 。针对Cox模型的基于可能性的增强在[CoxBoost中](https://cran.r-project.org/web/packages/CoxBoost/index.html)实现 ，对于混合模型在 [GMMBoost中实现](https://cran.r-project.org/web/packages/GMMBoost/index.html)。可以使用[gamboostLSS](https://cran.r-project.org/web/packages/gamboostLSS/index.html)增强来拟合GAMLSS模型 。包[gradDescent中](https://cran.r-project.org/web/packages/gradDescent/index.html)提供了基于梯度下降的各种学习算法来处理回归任务 。
-   *支持向量机和核方法* ：函数 SVM（） 从 [e1071](https://cran.r-project.org/web/packages/e1071/index.html) 报价到LIBSVM库和包的接口 [kernlab](https://cran.r-project.org/web/packages/kernlab/index.html) 实现了核学习一个灵活的框架（包括支持向量机，RVM的和其他内核学习算法）。软件包[klaR中](https://cran.r-project.org/web/packages/klaR/index.html)提供了SVMlight实现的接口（仅针对全部分类） 。可以使用[rdetools](https://cran.r-project.org/web/packages/rdetools/index.html)估计内核特征空间中的相关维， 该工具还提供了模型选择和预测的过程。
-   *贝叶斯方法* ：贝叶斯可加回归树（BART）在包[BayesTree](https://cran.r-project.org/web/packages/BayesTree/index.html)， [BART](https://cran.r-project.org/web/packages/BART/index.html)和 [bartMachine](https://cran.r-project.org/web/packages/bartMachine/index.html)中实现，其中最终模型是根据许多弱学习者的总和定义的（与整体方法不同） 。软件包[tgp](https://cran.r-project.org/web/packages/tgp/index.html)提供了包括树状贝叶斯CART和树状线性模型的树状高斯过程的贝叶斯非平稳，半参数非线性回归和设计 。在软件包[BDgraph中](https://cran.r-project.org/web/packages/BDgraph/index.html)实现了无向图形模型中用于多变量连续，离散和混合数据的贝叶斯结构学习 [](https://cran.r-project.org/web/packages/BDgraph/index.html); 可以从package [ssgraph](https://cran.r-project.org/web/packages/ssgraph/index.html)获得依赖于先验先验的相应方法 。朴素贝叶斯分类器是可用 [naivebayes](https://cran.r-project.org/web/packages/naivebayes/index.html)。
-   *使用遗传算法进行优化* ：软件包 [rgenoud](https://cran.r-project.org/web/packages/rgenoud/index.html) 提供了基于遗传算法的优化例程。[Rmalschains](https://cran.r-project.org/web/packages/Rmalschains/index.html)软件包 使用局部搜索链实现模因算法，这是一种特殊的进化算法，将稳态遗传算法与局部搜索相结合以实现实值参数优化。
-   *关联规则* ：包 [规则](https://cran.r-project.org/web/packages/arules/index.html) 提供了有效处理稀疏二进制数据的数据结构，[还](https://cran.r-project.org/web/packages/arules/index.html)提供了Apriori和Eclat实现的接口，用于挖掘频繁项集，最大频繁项集，封闭频繁项集和关联规则。软件包 [opusminer](https://cran.r-project.org/web/packages/opusminer/index.html) 提供了OPUS Miner算法（在C ++中实现）的接口，可使用杠杆或提升以自给自足的项目集的形式有效地查找交易数据中的键关联。
-   *基于模糊规则的系统* ：Package [frbs](https://cran.r-project.org/web/packages/frbs/index.html) 实现了许多标准方法，用于从数据中学习基于模糊规则的系统，以进行回归和分类。软件包 [RoughSets](https://cran.r-project.org/web/packages/RoughSets/index.html) 在单个软件包中提供了粗糙集理论（RST）和模糊粗糙集理论（FRST）的全面实现。
-   *模型选择和验证* ：软件包 [e1071](https://cran.r-project.org/web/packages/e1071/index.html) 具有 用于超参数调整的函数 tune（）和函数 errorest（） （[ipred](https://cran.r-project.org/web/packages/ipred/index.html)）可用于错误率估计。支持向量机的成本参数C可以使用软件包[svmpath](https://cran.r-project.org/web/packages/svmpath/index.html)的功能进行选择 。[ROCR](https://cran.r-project.org/web/packages/ROCR/index.html)软件包提供了ROC分析功能和其他用于比较候选分类器的可视化技术 。软件包 [hdi](https://cran.r-project.org/web/packages/hdi/index.html) 和 [stabs](https://cran.r-project.org/web/packages/stabs/index.html) 为各种模型实现稳定性选择， [hdi](https://cran.r-project.org/web/packages/hdi/index.html) 还提供了高维模型中的其他推理程序。
-   *其他过程* ：证据分类器使用软件包[evclass中](https://cran.r-project.org/web/packages/evclass/index.html)的Dempster-Shafer质量函数来量化有关测试模式类别的不确定性 。该 [OneR](https://cran.r-project.org/web/packages/OneR/index.html) （一个规则）封装报价并增强了复杂的操作与丰富的诊断功能缺失值和数字数据一起的分类算法。
-   *元软件包* ：软件包 [插入符](https://cran.r-project.org/web/packages/caret/index.html) 提供了用于构建预测模型的其他功能，包括参数调整和变量重要性度量。该软件包可以与各种并行实现（例如MPI，NWS等）一起使用。以类似的方式，包 [mlr3](https://cran.r-project.org/web/packages/mlr3/index.html) 为各种统计和机器学习包提供了高级接口。软件包 [SuperLearner](https://cran.r-project.org/web/packages/SuperLearner/index.html) 实现了类似的工具箱。该 [水](https://cran.r-project.org/web/packages/h2o/index.html) 该软件包实现了一个通用的机器学习平台，该平台具有可扩展实现的许多流行算法，例如随机森林，GBM，GLM（具有弹性网络正则化）和深度学习（前馈多层网络）等。
-   *GUI* [嘎嘎声](https://cran.r-project.org/web/packages/rattle/index.html) 是R中数据挖掘的图形用户界面。
-   *可视化（最初贡献的布兰登格林威尔）* 的 统计信息:: termplot（） 功能包可以用来绘制的项在其预测方法支持一个模型 类型=“条款”。的 [效果](https://cran.r-project.org/web/packages/effects/index.html) 包提供图形和表格效果显示用于与线性预测（例如，线性的和广义线性模型）的模型。弗里德曼的偏相关图（PDP）是预测函数的低维图形渲染，它以一些软件包的形式实现。 [gbm](https://cran.r-project.org/web/packages/gbm/index.html)， [randomForest](https://cran.r-project.org/web/packages/randomForest/index.html) 和 [randomForestSRC](https://cran.r-project.org/web/packages/randomForestSRC/index.html) 虽然提供了自己的功能来显示PDP，但仅限于与那些程序包匹配的模型（randomForest中 的 [partialPlot](https://cran.r-project.org/web/packages/randomForest/index.html)函数 受到 更多限制，因为一次仅允许一个预测变量）。包 [PDP](https://cran.r-project.org/web/packages/pdp/index.html)， [plotmo](https://cran.r-project.org/web/packages/plotmo/index.html)和 [冰箱](https://cran.r-project.org/web/packages/ICEbox/index.html) 都比较一般，并允许创建的PDP为各种机器学习模型（例如，随机森林，支持向量机等）; 既 [PDP](https://cran.r-project.org/web/packages/pdp/index.html) 和 [plotmo](https://cran.r-project.org/web/packages/plotmo/index.html) 支持多元显示器（[plotmo](https://cran.r-project.org/web/packages/plotmo/index.html) 被限制为两个预测而 [pdp](https://cran.r-project.org/web/packages/pdp/index.html) 使用网格图形来显示涉及三个预测变量的PDP。默认情况下， [plotmo](https://cran.r-project.org/web/packages/plotmo/index.html) 将背景变量固定在其中间值（或因子的第一级），这比构造PDP更快，但包含的信息较少。 [ICEbox](https://cran.r-project.org/web/packages/ICEbox/index.html) 专注于构建个人条件期望（ICE）曲线，这是对Friedman PDP的改进。ICE曲线以及居中的ICE曲线也可以使用[pdp](https://cran.r-project.org/web/packages/pdp/index.html) 包中的partial（） 函数 构造 。 [ggRandom森林](https://cran.r-project.org/web/packages/ggRandomForests/index.html)[](https://cran.r-project.org/web/packages/pdp/index.html)[](https://cran.r-project.org/web/packages/ggRandomForests/index.html) 提供基于ggplot2的工具，用于对来自[randomForest](https://cran.r-project.org/web/packages/randomForest/index.html) 和 [randomForestSRC](https://cran.r-project.org/web/packages/randomForestSRC/index.html) 软件包的随机森林模型（例如，可变重要性图和PDP）进行图形化探索 。

[CORElearn](https://cran.r-project.org/web/packages/CORElearn/index.html) 实现了相当广泛的一类机器学习算法，例如最近的邻居，树木，随机森林以及几种特征选择方法。类似地，程序包 [rminer可以](https://cran.r-project.org/web/packages/rminer/index.html) 与其他程序包中实现的几种学习算法进行接口，并计算多种性能指标。



































