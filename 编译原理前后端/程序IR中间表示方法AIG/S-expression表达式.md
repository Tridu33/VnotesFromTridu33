

马希文老师的《LISP语言》

# 1. S-expression表达式
理解S表达式 https://thzt.github.io/2015/04/02/s-expression/





Lisp的语法元素称为符号表达式（也称为s-expressions）。数据和函数（即Lisp程序）都表示为s表达式，可以是atom或list。 https://www.sciencedirect.com/topics/computer-science/symbolic-expression


github.com/mjsottile/sfsexp


该库供希望从C或C ++程序操纵（读取，解析，修改和创建）Symbolic expression符号表达式的开发人员使用。符号表达式或s表达式本质上是类似于LISP的表达式，例如（a（bc））。S表达式能够表示复杂的结构化数据，而无需描述结构的其他元数据。它们是**递归**定义的（循环会变成递归不方便，但是等价转换的）：s表达式是原子或s表达式的列表。在上面的示例中，表达式包含一个原子“ a”和一个s表达式，后者又包含两个原子“ b”和“ c”。它们简单，有用且广为人知。

该库旨在为上面列出的四个功能提供最少的功能和数据结构集：

读取s表达式（I / O），将包含它们的字符串解析为AST等效项，修改AST表示并将AST转换回转换成格式正确的字符串。

https://zh.wikipedia.org/wiki/S-%E8%A1%A8%E8%BE%BE%E5%BC%8F 

逆波兰表达式 栈机

S-expression parser 很多


https://github.com/dryruby/sxp.rb ruby s-expression parser


https://github.com/fwg/s-expression js parser  [Recursive descent parser] 1 for [S-expressions] 2. It takes a string and returns the value that corresponds to one complete expression, or an Error.

https://github.com/janestreet/parsexp OCaml 

S表达式  http://www.buildyourownlisp.com/chapter9_s_expressions

 From Lisp **S-expressions to Java** source code  

By providing an S- expression based program representation for Java source code, we are able to reuse and extend Lisp macro-expansion techniques to significantly simplify the construction of Java programs.




-------------------------------



**WASI,Wasmer**
WAT格式基于“S-表达式expression”来表达模块的定义过程.

S-expression是一种以人类可读的文本格式来表达半结构化数据的语法约定symbol


[S表达式不直接是AST](https://news.ycombinator.com/item?id=16386702)：它们是很容易与AST匹配的形式（可以是手头的Lisp，也可以是周围有翻译/解析器/解释器的某种语言，或者没有代码的某种语言。在系统中（完全）处理它）。这使s表达式的使用变得简单，开发工具可以处理s表达式，而不必始终知道它们代表什么语言。
如果您的开发工具知道如何处理特定的语言，则它可以处理该语言的AST，但不能处理其他任何语言。您可以向工具说明其他语言，但这需要让工具知道的方法。最后，这类似于静态类型与动态类型的讨论：静态类型不允许任何潜在的不安全数据，而直接与AST配合使用的工具则不允许任何潜在的无效程序，从原理上（或理论上）好的但实际上很难实现，这给工具实现者和用户带来了开销。它可能会占用很多交互性：

因此，我认为S表达式是一个非常务实的概念，如果替换成本不超过收益，它将很难替换






----------------


《深入浅出webAssembly》纸质书第四章WAT中WebAssemblyTextFormat

```c++
int fib(){
    if(X<2){
        return 2;
    }else{
        return FIB(X-1)+FIB(X-2);
    }
}
```


WasmFiddle https://wasdk.github.io/WasmFiddle/ 或者类似线上线下编译平台-->wat


WAT是一种与wasm二进制格式等效的，可以用来对WebASsembly模块及其包含的所有定义(即模块内容)进行编码的一种文本格式

```wasm
(module
 (type $FUNCSIG$i (func (result i32)))
 (type $FUNCSIG$ii (func (param i32) (result i32)))
 (import "env" "FIB" (func $FIB (param i32) (result i32)))
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "fib" (func $fib))
 (func $fib (; 1 ;) (param $0 i32) (result i32)
  (local $1 i32)
  (set_local $1
   (i32.const 2)
  )
  (block $label$0
   (br_if $label$0
    (i32.lt_s
     (get_local $0)
     (i32.const 2)
    )
   )
   (set_local $1
    (i32.add
     (call $FIB
      (i32.add
       (get_local $0)
       (i32.const -1)
      )
     )
     (call $FIB
      (i32.add
       (get_local $0)
       (i32.const -2)
      )
     )
    )
   )
  )
  (get_local $1)
 )
)

```



WAT格式基于“S-表达式expression”来表达模块的定义过程.




S-expression是一种以人类可读的文本格式来表达半结构化数据的语法约定symbol

在S-expression中我们用小括号"（）"来定义每一个的表达式，并子表达式与子表达式之间还可以通过语法规则来互相嵌套，这就在整体上构建出了**AST抽象语法树**的结构

简单起见，这里的+\*完全可以变成程序计算中符号表的任意二元运算符(至于其他0元/三元运算符改成二元的表达或者多个空字段什么的方法,也不是问题)

比如“1+2\*3+4\*5”分别转换为S-expression和WAT:


S-expression一定程度上反映了源代码的AST

```s
(+
    (+ 1
        (* 2 3)
    )
    (* 4 5)
)
```


WAT:

```wat
(module
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "calculate" (func $calculate))
 (func $calculate (; 0 ;) (result i32)
  (i32.add
      (i32.add
          (i32.const 1)
          (i32.mul
              (i32.const)(i32.const 3)    
          )
      )
      (i32.mul
          (i32.const 4)(i32.const 5)
      )
  )
 )
)
```

定义了calculate函数

优化只能看到这个：

```wat
(module
 (table 0 anyfunc)
 (memory $0 1)
 (export "memory" (memory $0))
 (export "calculate" (func $calculate))
 (func $calculate (; 0 ;) (result i32)
  (i32.const 27)
 )
)
```



WAT是一种可读文本类型的AST,wasm二进制文件内的opCode代码是一种Linear Binary AST一种Binary-AST结构

WAT2wasm等工具或者二进制在线编译平台得到等效的wasm二进制模块
https://webassembly.github.io/wabt/demo/wat2wasm/

```wasm
41 02 41 03 6c 41 01 6a 41 04 41 05 6c 6a
```


```wasm
41 02     #i32.const 02
41 03     #i32.const 03
6c        #i32.mul
41 01     #i32.const 01
6a        #i32.add
41 04     #i32.const 04
41 05     #i32.const 05
6c        #i32.mul
6a        #i32.add
```























































