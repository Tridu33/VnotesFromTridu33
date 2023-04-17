





















https://llvmlite.readthedocs.io/en/latest/index.html



https://llvmlite.readthedocs.io/en/latest/user-guide/index.html

# llvm-lite
LLVM-lite-AST到llcm的python绑定项目

https://github.com/numba/llvmlite
工程之前没有听说过。刚才浏览了一下，example里有ir builder的示例，参考着应该就可以把ast转成llvm ir了。另外llvm官方文档中有一个简单的编译器教程，其中第三章就是把ast转为llvm ir。如果有C++基础的话建议看一下前三章的内容~ 用llvm开发编程语言的步骤是怎样的？ - 和白少两丿的回答 - 知乎
https://www.zhihu.com/question/465770030/answer/1947670255




词法分析就是生成token，并且构建ast，这时候就需要去定义ast，把ast基本框架搭建好再去实现语法分析

后面就是生成ir了，要对定义的ast类去提供ir的生成方法，这一步可以调用llvm的一些内建函数，像irbuilder，module，llvmcontext之类的

如果想再添加优化支持，可以通过pm去添加
























