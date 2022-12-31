# 1. 本地文件超强资源

# 2. online

https://github.com/mark-gerarts/haskell-learning/tree/master/Data%20Structures%20%26%20Algorithms


https://github.com/Alkesst/DataStructures/tree/master/Haskell/DataStructures


https://github.com/robertjlooby/purely-functional-data-structures



https://github.com/LEDThereBeLight/Haskell-Data-Structures






















A purely functional ring data structure for Haskell.

ghc-vis是在GHCi中可视化Haskell实时数据结构的工具。评估不是强制性的，您可以与可视化的数据结构进行交互。这样就可以看到Haskell的懒惰评估和实际操作中的共享。 https://github.com/def-/ghc-vis








基于CAS https://en.wikipedia.org/wiki/Computer_algebra_system 的数据结构的不同软件包的集合。 https://github.com/rrnewton/haskell-lockfree















## 2.1. 包库数据结构




https://wiki.haskell.org/Applications_and_libraries/Data_structures













## 2.2. 算法

okmij.org/ftp/Haskell/AlgorithmsH1.html









## 2.3. Haskell 常用数据结构
www.voidcn.com/article/p-wvxzhfbz-be.html

www.voidcn.com/article/p-ymptfdsh-be.html




www.voidcn.com/article/p-enyaokzx-buy.html

www.voidcn.com/article/p-amgeivnt-be.html


www.voidcn.com/article/p-yxazuhkc-be.html







www.voidcn.com/article/p-akhkexxv-bsm.html


## 2.4. 数据类型




https://www.cnblogs.com/Iambda/archive/2013/02/03/3933535.html













## 2.5. 泛函



www.voidcn.com/article/p-kaljxhgr-qd.html



















还要一个值得一提的是Zipper，learn you a haskell for good 的例子已经够好了。参考链接 zippers。当然，Haskell这一类fp的语言面前，递归结构书写出来都是很漂亮的。只是遇到状态变更一类的场景时，显得有些别扭，不如直接通过指针修改来得高效。

作者：夜色残阳
链接：https://www.zhihu.com/question/32163076/answer/254083860
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。









## 2.6. JAVA VS Haskell
https://www.zhihu.com/question/67678268/answer/255774559
作者：非构造性雨轩菌  
链接：https://www.zhihu.com/question/67678268/answer/255774559  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

没有，java和haskell都是作为图灵完备的语言而设计的。（逃

嘛，更容易做到的和更难做到的倒是一个很大的话题。这里以我自己的理解和经历取多个方面不完全的列举一些简单的例子吧

和语言的社区、学习相关的：

-   Java更容易利用现有的API、工具链及相关文档实现一些常见的功能性程序。Haskell相对来说存在相关文档可能较少、没有类似的可参考的实现等劣势。这跟语言本身的定位、社区有一定关系。
-   Java在web方面有较多现有的解决方案，技术栈、文档相对来说齐全。相关技术、API都被反复使用过，如果不是在玩各种黑魔法，对已有的坑之类的即使踩中也有能很轻松的找到解决方案。嘛，毕竟Java（www
-   一般来说Haskell的学习曲线较Java陡峭，社区的各类教程不如Java丰富，社区的规模摆在那里。很多基础概念涉及被抽象后的数学概念，前置知识要求较多，毕竟抽象很大程度要站在直观理解的位置才行，没有直观理解的话较难理解抽象背后的意义。自学的话Haskell更需要自身有多尝试、找文档、规划学习过程等能力。
-   有一定数学基础（特别是离散数学、类型论等）学习Haskell相对Java来说更加有用，较容易找到对应的概念，这方面的文档要比Java丰富。容易写一些十几行简单的程序来辅助理解，能写的东西较多。而Java需要在另一种方面去学习，比如通过研究现有的开源程序、学习设计模式、写一些简单的小项目等。这可能会导致“Haskell学语言，Java学姿势”的情况（www
-   Haskell社区的资源更加集中，在学习过程中如果善于去找的话，更容易找到真正需要的资源。比如有[Hoogle](https://link.zhihu.com/?target=https%3A//www.haskell.org/hoogle/)这种好东西，对学习很有帮助。
-   etc.

语言特性方面：

-   说到Haskell那语言特性方面第一个想到的果然还是类型系统相关的吧www，Java的话OOP范式、inheritance、behavioral subtyping、generic（bounded parametric polymorphism）、wildcard（existential bounded polymorphism）、overloading（ad hoc polymorphism）、etc. 。Haskell的话能说的就多了，FP范式、ML系、type inference（Hindley-Milner type system）、parametric polymorphism、typeclass（ad hoc polymorphism）、type constructor（higher kinded type）、lazy evaluation strategy（call-by-need）、经常被提到的monad（www）、etc.。各种扩展更是不计其数，常见的：RankNTypes、ExistentialQuantification、GADTs、DataKinds、TypeFamilies、TypeOperators、MultiParamTypeClasses、FunctionalDependencies、etc.
-   Meta programming的话Java不支持、Haskell有template。
-   Haskell主要后端是编译到native code，也有bytecode。Java主要编译到bytecode然后jvm解释、JIT。内存管理都是GC策略。
-   因为Haskell类型系统相对Java更丰富，可以用类型系统玩各种有趣的东西www，Java的话泛型并不支持higher kinded type，type inference也只是局部的，能玩的东西有限。
-   Java的话并行程序主要还是靠加锁、wait notify、java.util.concurrent、现有的thread safe的数据结构，线程安全靠Java内存模型。Haskell的话有Control.Parallel、Control.Concurrent、Control.Concurrent.STM，用得不多不太好发表评论。
-   etc.

如果假设这里的更容易和更难指的是具体实现一个程序主观上是否更容易的话那么大概Java的长处就是OOP范式本身和丰富的API了。Haskell的长处就是其类型系统了，能够抽象出更多的概念，在高层次处理复杂问题，由类型系统保证程序的正确性，甚至可以玩定理证明www

总之分别有各自的应用领域，我自己是Haskell和Java都在用，各有各的好，嗯。














































































