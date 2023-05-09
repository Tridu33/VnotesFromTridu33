






https://blog.jle.im/entries.html 系列博文


https://blog.jle.im/entry/practical-dependent-types-in-haskell-1.html#fnref2 







可训练模型的纯函数类型方法（第 3 部分）
在#machine learning , #differentiable programming , #deep learning , #backprop , #modeling , 

可训练模型的纯函数类型方法（第 2 部分）


可训练模型的纯函数类型方法（第 1 部分）


Haskell 2 中的实用依赖类型：存在神经网络和运行时的类型



介绍反向传播库Haskell 中的实用依赖类型：类型安全的神经网络（第 1 部分）

使用 AD 自动传播不确定性


# 前置知识看仓库







https://github.com/conal/concat 编译到类型  http://conal.net/papers/compiling-to-categories/ 论文



-------------------------------------------------------------------------

neural: Neural Networks in native Haskell https://hackage.haskell.org/package/neural 
该项目的目标是为 Haskell 中的 神经网络 （和类似的参数化模型）提供一个灵活的框架。

Hackage 上已经有几个神经网络库，但据我所知，它们要么

是用另一种语言编写的引擎的包装器，或者
提供有限的网络架构、训练算法或错误函数选择，或者不易扩展。
这个库的目标是在本地 Haskell 中实现（相当高效），提供最大的灵活性。

此外，梯度下降/反向传播应该使用 自动微分自动工作。这意味着可以使用新的和复杂的激活函数和/或网络架构，而无需先手动计算导数。

为了提供强大而灵活的 API，模型是使用组件构建的，这些组件的行为就好像它们实现了 Arrow 和 ArrowChoice类型类。因此，它们可以很容易地组合和转换。

模型构建完成后，可以使用管道将其连接到定制的训练算法中，从而可以在模块中定义算法的各个方面（加载数据、选择随机样本、报告中间结果、停止标准等） ，解耦方式。

尽管神经网络是该项目的主要动机，但任何其他类型的模型都可以在同一框架中定义，只要模型以可微的方式依赖于数值参数的集合。- 一个简单的例子是线性回归。

https://blog.jle.im/entry/purely-functional-typed-models-1.html

https://blog.jle.im/entry/purely-functional-typed-models-3.html


https://blog.jle.im/entry/practical-dependent-types-in-haskell-1.html

https://blog.jle.im/entry/practical-dependent-types-in-haskell-2.html

# haskell 神经网络








https://github.com/capn-freako/Haskell_ML/wiki
haskell神经网络














