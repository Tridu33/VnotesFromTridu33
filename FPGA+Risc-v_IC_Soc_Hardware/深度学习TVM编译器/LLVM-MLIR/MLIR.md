

https://mlir.llvm.org/getting_started/

```
$ git clone https://github.com/llvm/llvm-project.git
$ mkdir llvm-project/build
$ cd llvm-project/build
$ cmake -G "Unix Makefiles" ../llvm \
     -DLLVM_ENABLE_PROJECTS=mlir \
     -DLLVM_BUILD_EXAMPLES=ON \
     -DLLVM_TARGETS_TO_BUILD="host" \
     -DCMAKE_BUILD_TYPE=Release \
     -DLLVM_ENABLE_ASSERTIONS=ON 
$ cmake --build . --target check-mlir
```
构建之后可以在 llvm-project/build/bin/ 路径下找到可执行文件。
# MLIR Multi-Level Intermediate Representation!


https://mlir.llvm.org/docs/



https://mlir.llvm.org/




如何看待Google的MLIR项目？ - 杨军的回答 - 知乎
https://www.zhihu.com/question/319145946/answer/643929592




但学完之后，一直存在两个问题：

MLIR解决什么问题，整体架构是什么；
MLIR如何像TVM那样，做计算调度优化？


以下是个人的思考：

核心目的：弥补框架和底层硬件之间的gap，连通上层框架和下层硬件；
解决方案：Dialect，DialectConversion；
实现方案：a. 实现Dialect -> C++定义Dialect/ODS定义（包含Operation, Attribute, Type, Constraint, Interface, Trait）；b. Dialect内部转换 -> Transformation；c. Dialect之间转换 -> DialectConversion；d. Pass优化。其中bcd均可以采用C++代码或者DRR方式去实现。





众所周知，MLIR通过progressive lowering来实现不同抽象层面IR的组合与优化，这个也不能算啥新颖思路了。但最近我看MLIR在CGO2021的论文，发现还可以搞“逆练MLIR”。

什么是“逆练MLIR”呢？这是我随便起的名字，它的正式名称是progressive lifting，和lowering刚好反过来，是**从低抽象水平IR反向合成高抽象水平的IR**。

这有什么用呢？让我们考虑MLIR优化的经典流程，大致是AST->MLIR dialect->LLVM IR->machine code。MLIR dialect这一步包含着progressive lowering，可能涉及到多个方言。






MLIR: 编译器基础架构重定义 - 吴建明wujianming的文章 - 知乎
https://zhuanlan.zhihu.com/p/379063169