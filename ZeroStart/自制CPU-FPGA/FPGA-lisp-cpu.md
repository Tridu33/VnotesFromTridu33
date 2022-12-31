# lisp-cpu










Lisp CPU 的架构，它应该适合小型 FPGA，就像Spartan-3 Starter Kit中使用的那样。对于“Lisp CPU”，我的意思是核心评估二进制形式的 s 表达式，而不将其编译为较低的机器代码级别，如基于 LISP 的处理器的设计或 SCHEME：介电 LISP 或被认为有害的有限记忆中所述或者，LAMBDA：终极操作码. 我的目标不是一个功能齐全的 Common Lisp 实现，而是一个足以编写游戏等应用程序的 Lisp 方言，而无需像 C 那样进行所有低级处理。虽然应用程序逻辑将用 Lisp 编写，特殊的硬件功能和性能关键任务，如声音生成，将在硬件中实现，并与原始 Lisp 函数一起使用。

https://frank-buss.de/lispcpu/
























