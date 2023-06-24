# immutable 




什么是 immutability? 其实细分起来有语法上的 immutable (例如 Java 里的 final 关键字), 和运行时对象的 immutable (一个变量名可以修改指向不同对象, 但对象的内容不可变). 两者的联系是: 如果语法上规定所有变量都是 "final" 的, 那么运行时对象就相当于都 immutable 了. 但如果语法上部分变量是 final, 部分不是, 那么就不能得出运行时对象全都 immutable 的结论.


在运行时对象都是 immutable 的情形下, 很多优势才会显现出来.



函数式编程（Functional Programming）相比面向对象编程（Object-oriented Programming）有哪些优缺点？ - luikore的回答 - 知乎
https://www.zhihu.com/question/19732025/answer/36771857


函数式编程immutable data不是本质上性能就差点 - 知乎
https://www.zhihu.com/question/448731585/answer/2453366967


# Haskell实现mutable struct

https://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/poptics.pdf Profunctor Optics - Modular Data Accessors
lens + 语法糖 + fbip 你就实现了像 c 一样的 mutable struct 
