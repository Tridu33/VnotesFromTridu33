# lumen为WebAssembly而生的一个新的BEAM实现







Lumen 项目架构：

- 编译器，用于将Erlang转换为给定目标的本地代码的编译器（x86，ARM，WebAssembly），基本代码处理流程： EIR （Erlang中间码） -> MEIR -> LLVM IR -> LLVM 。
- 解释器，基于 EIR，用于测试和执行 Erlang代码的另一种方式。
- 运行时，对应于Erlang运行时系统（ERTS），提供了实现OTP所需的核心功能。

Lumen开发的主要动机，是能够编译可能针对WebAssembly的Elixir应用程序，从而能够将Elixir用作前端开发的语言。










