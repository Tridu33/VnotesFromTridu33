[TOC]

# demo


```C++
#define COUNT 10

void foo(int a,int b,int c,int *d){
    int i = 0;
    do{
    d[i++] = i*a+b*c;//fill in table
    }while(i < COUNT)
}
```

## 预处理
消除注释

定义和扩展宏

条件编译


```C++
void foo(int a,int b,int c,int *d){
    int i = 0;
    do{
    d[i++] = i*a+b*c;
    }while(i < 10)
}
```




包含文件#include <stdio.h>


## 词法分析
关键字


## 语法分析

语义

AST(Abstract syntax tree抽象语法树)

BNF（Backus-Nsur Form巴科斯-诺尔范式）



## 生成中间代码
Virtual Machine

```
FUNCTION foo(p0, p1, p2, p3)
MoV t0,#0  ; temporary 0 stores count
label:
 MUI t1,t0,p0 ; calculate i*a
 MUL t2,p1,p2; calculate b*c
 ADD t3,t1,t2; calculate i*a+b*c
 MUL t4,t0,#4; index= count* sizeof(int)
 ADD t5,p3,t4;  calculate address
 STW [t5],t3; store i*a+b*c in d[i]
 ADD t0,t0,#1; increment loop count
 BRANCHLT t0,#10,label; branch if count < 10
```






## 优化

普通优化

```
FUNCTION foo(p0, p1, p2, p3)
MoV t0,#0  ; 
MUL t2,p1,p2;hoist loop-invariant calculation循环不变式
label:
 MUI t1,t0,p0 
 ADD t3,t1,t2
 MUL t4,t0,#4
 ADD t5,p3,t4
 STW [t5],t3
 ADD t0,t0,#1
 BRANCHLT t0,#10,label
 RET
```

激进的优化(感应变量消除)

```
a(0) = d a(i+1) = a(i) + 4
v(0) = b*c v(i+1) = v(i) + a
```

```
FUNCTION foo(p0, p1, p2, p3)
MUL t1,p1,p2
MOV t2,t3
ADD t3,t2,#40
label:
 STW [t2],t1
 ADD t1,t1,p0
 ADD t2,t2,#4
 BRANCHLT t2,t3,label
 RET
```





## 生成目标代码


```
; In the ARM EABI calling convention, the first four
; arguments are in provided r0-r3

; r0-r3 may also be used as scratch registers without
; saving to the stack

foo::
 mul r1,r1,r2 ;x1=b*c(reuse r1)
 add r2,r3,#40 ;r2=d+40(reuse r2)
label:
 stw [r3],r1; store(i)ata(i)
 add r3,r3,#4;a(i+1)=a(i)+4
 add r1,r1,r0;v(i+1)=v(i)+a
 cmp r3,r2; have we reached(10)yet?
 Blt label; if not,loop
 B lr；return to link address
```

决定到底选是哪个CPU?什么指令集？


























































































































































































































