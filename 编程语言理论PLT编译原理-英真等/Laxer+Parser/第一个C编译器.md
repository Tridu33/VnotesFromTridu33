














# 第一个c语言编译器


一般教程 无论使用什么语言都能自举，根据元语言的计算能力能表达自身图灵完备的计算能力。

如果基于C语言开发一款C语言编译器，那么可能会产生鸡生蛋的问题。


但是，其实本质上 递归计算模型lambda演算能力的ffmpeg之类的，或者图灵机，栈机，寄存器机，wasm等等都是图灵完备的“虚拟机/实体机”，

**本质上**就是 ”CFG/计算图/程序AST抽象语法树打平的S表达式“，无论可调用对象（函数）如何封装高级DSL满足更简便，模块化的批处理，本质上就是图灵机的纸带计算能力，如同《计算的本质：深入剖析程序与计算机》所说，只需要最简单的计算能力，比如https://github.com/angrykoala/awesome-esolangs 就是很多底层理论尝试。


1. 中间语言IR,llvm/graal/Common Intermediate Language CIL/wasm等 ，直接编译到C等等高级语言计算模型也可以，如用C编写其他解析器，或者[用C自举一个C语言编译器](https://blog.grabbyte.com/2022/01/757.html)
2. 或者直接crowbar教程一样，从手写计算器 to 汇编执行动作序列的algorithm开发，从mycalc出发实现“c”到“assembly code"

本质上都是规则系统

以最常见risc，x86为例计算模型出发，从布尔逻辑电路抽象层得到目标机器“汇编”寄存器机，那么目标语言生成=“汇编生成”


栈机，用压栈，return 处理递归函数，进而实现进一步计算，软件模拟硬件可以


闭包，带词法作用域链的函数（可调用对象），函数能放在参数回调，函数能放在返回值Promise，构造线程协程promise，continuation,call/cc。


lisp合理管理可调用对象指针，合理管理垃圾回收算法可以实现GC垃圾回收。


把$\lambda x . f x $写成$f(x)$糖化lambda表达式


simula第一个开始 **面向对象建模**（基于结构体go,基于原型链js,lua，基于类的面向对象，...等从零开始抽象解决软件危机）



有哪些关于c4 - C in four function 编译器的文章？ - RednaxelaFX的回答 - 知乎
https://www.zhihu.com/question/28249756/answer/84307453



如何实现 C 语言编译器？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/35226878/answer/132017343























































