risc-v手册（中文版） http://riscvbook.com/chinese/





risc-v手册（官网） https://riscv.org/technical/specifications/




爆肝6万字的 Bluespec SystemVerilog (BSV) 中文教程上线了 - WangXuan的文章 - 知乎
https://zhuanlan.zhihu.com/p/469917984


# Bluespec (BSV) 教程


Bluespec 学习之状态机 - 水生植物的文章 - 知乎
https://zhuanlan.zhihu.com/p/435829042





bluespec和verilog相比有什么区别？ - WangXuan的回答 - 知乎
https://www.zhihu.com/question/26816009/answer/2374215712


Open Source RISC-V Cores and Tools | Bluespec
https://bluespec.com

Chisel、Bluespec、SystemC、HLS https://blog.csdn.net/u011329967/article/details/109504081









# bluespec





bluespec和verilog相比有什么区别？ - parker liu的回答 - 知乎
https://www.zhihu.com/question/26816009/answer/1257445442


Bluespec的历史则更悠久了，这是一家2003年成立的公司。设计Bluespec这个工具的人是Haskell语言的创始人之一，其合作者（也是该公司的创始人）则成功设计过10Gb级别的路由网络芯片，现在在MIT教书。从2003年起他们就开始用Bluespec来设计芯片了，然后逐渐成为一个商用的集成电路逻辑设计工具，有其他商业公司付费使用这个工具来设计芯片，比如IBM的一款powerpc芯片。这是一套有着完整的从硬件电路的Spec描述，硬件架构设计，硬件电路逻辑设计，到验证系统设计流程支持的工具。也是经过流片验证可用的，作出了实际可以运行的芯片。最近Bluespec公司还将其设计的三款Risc-V的mcu的源代码给开源了，其中有一款是支持乱序执行和超标量的性能较高的6级流水的mcu。

Bluespec是一种用Haskell实现的高层次抽象的硬件描述语言，在可靠的Term Rewrite System的基础上，用Haskell来将函数式编程的理念应用到了硬件电路的逻辑设计的编程中。利用Haskell中的强有力的类型系统，可以定义非常清晰的硬件电路的操作语义，能够进行一定程度的形式推导，各个模块在设计和实现时有很强的类型约束，以及编译期的类型检查（Type Check）。这些特点更好的保障了正确性，消除了在verilog中因为粗心而导致的不一致的bug，这样的bug在verilog中是非常难以避免的，且难以查找。Bluespec更重要的是将硬件电路计算中的副作用和纯计算分离出来了，使得在硬件电路的并行和并发的设计上更加清晰，能更好的确保正确性，具有良好的组合能力。

具有新意的是，相对于传统的Verilog，利用Haskell的高级编程语言的特性，强大的抽象能力和丰富的表达能力，使得电路的逻辑设计不再局限于低层次的RTL级别的抽象，能够更直接的将人脑中的算法以更接近人的思维的方式将电路描述出来。在硬件电路的逻辑设计中引入了软件设计中常用的概念和方法，比如类型系统、多态、类型类、对象和实例、继承、多层次的结构化的数据结构（代数数据类型）、高阶函数、模式匹配等。特别是将Bluespec中支持的数据类型都作为一等公民（first class）对待，典型的如module、interface、action、function等都可以作为参数和返回值，简化了电路设计中的逻辑，能够更方便的嵌套组合起来，并使得Bluespec设计的电路有良好的参数化定制的能力。

-------------------------------------------------------------------

编程实际上是不分软件和硬件的，最初出现的电子计算机的编程就是插线，实际上就是类似现在的硬件电路的逻辑设计编程工作。然后早期的计算机都是软硬件一起设计的，典型的例子是世界上非常著名的克雷计算机，就是克雷一个人打造的软硬件设计。再然后，计算机系统复杂了以后才渐渐的演变为现在泾渭分明的软件编程和硬件电路设计。编程活动就是把人脑中的系统设计和算法通过编程语言描述出来。所不同的是软件编程是将这些设计和算法通过软件编程语言描述出来，然后通过编译器将其翻译为可以在冯.诺伊曼的计算模型上运行的指令流，解释执行后变成CPU内部的硬件电路的动作，驱动CPU的外围电路，和现实世界进行交互。而硬件电路设计则是将这些设计和算法通过Bluespec和Verilog这些语言将硬件电路描述出来，翻译为数字电路的逻辑门的连接和时序的控制，直接变换为硬件电路的动作，驱动外围电路，和现实世界交互。








# SpinalHDL



众所周知最好的haskell参考书是functional programming in scala，所以直接学基于scala的spinalHDL吧























