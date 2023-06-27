


# 深入浅出WebAssembly


纸质书第四章WAT中WebAssemblyTextFormat

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































