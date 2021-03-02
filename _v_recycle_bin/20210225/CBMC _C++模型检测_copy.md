# CBMC _C++模型检测



cprover.org/cbmc/




`CBMC`是C和C ++程序的绑定模型检查器。它支持C89，C99，大多数C11以及gcc和Visual Studio提供的大多数编译器扩展。分析Java字节码的CBMC的变体形式为[`JBMC`](http://www.cprover.org/jbmc)。

CBMC验证内存安全性（包括数组范围检查和对指针安全使用的检查），检查异常，检查未定义行为的各种变体以及用户指定的断言。此外，它可以检查C和C ++与其他语言（例如Verilog）的一致性。通过展开程序中的循环并将结果方程式传递到决策程序来执行验证。

`CBMC`适用于大多数Linux版本（预包装在Debian，Ubuntu和Fedora上），Solaris 11，Windows和MacOSX。您还应该阅读 [CBMC许可证](http://www.cprover.org/cbmc/LICENSE)。如有任何疑问`CBMC`，请联系[Daniel Kroening](http://www.kroening.com/)。

CBMC带有一个基于MiniSat的内置位向量公式求解器。作为替代方案，CBMC从3.3版开始就支持外部SMT求解器。我们推荐的求解器为（无特定顺序） [Boolector](http://fmv.jku.at/boolector/)， [MathSAT](http://mathsat.fbk.eu/download.html)， [Yices 2](http://yices.csl.sri.com/)和 [Z3](https://github.com/Z3Prover/z3/wiki)。请注意，这些求解器需要单独安装并且具有不同的许可条件。













