# 从lambda算子到实际的函数式程序设计语言






lambda算子的三条公理描述的可计算性

（1）lambda算子的三条公理，在这个基础上定义了程序设计语言达到的可计算性；
（2）lisp的七个基本操作符定义了lisp在语言实现上的计算能力，但是对于文件操作等并没有定义；
（3）scheme通过在lisp的七个基本操作符基础上定义一些：基本类型（true，false等），基本模式（form）和过程（process）来最小化定义该语言本身，并完成语言本身的形式化语言描述；
（4）scheme标准化种将这些模式和过程按照实际编程需要确定，然后提出R5RS等规范，然后对实际编程中涉及到的扩展编写可移植库（R7RS的努力）；



  lisp的七个基本操作符（quote,atom,eq,car,cdr,cons,cond） 
  


怎么理解从lambda算子到实际的函数式程序设计语言？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/23956920/answer/142867098

你去看 idris 那篇文章《Idris, a General Purpose Dependently Typed Programming Language: Design and Implementation》吧，手把手教你从 idris 编译成 TT（超级简单的带类型 λ 项）

（quote,atom,eq,car,cdr,cons,cond）和 λ 的转换可以靠 Church encoding 做

然后（quote,atom,eq,car,cdr,cons,cond）怎么自举好像有篇文章里面写过……忘了哪里看到了

最后，你可以用 Church number 去实现数学运算，不过 scheme 肯定不会这么干的，太慢了

