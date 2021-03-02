
[TOC]

# Crash Course-Computer Scienc






bilibli有翻译 https://www.bilibili.com/video/av21376839/











youtube.com/watch?v=zltgXvg6r3k&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=9



- 指令jump 10跳转行指令，而通常break跳出循环代码段，continue跳出本次循环进入下一次循环代码段：HALT停机指令



##  一个jump制造循环的例子循环


ATT 指令和Intel指令不一样，这里AT&T不影响理解就行。


RAM指令：

|         |            |
| ------- | ---------- |
| address | data       |
| 0       | LOAD_A 14  |
| 1       | LOAD_B 15  |
| 2       | ADD B A    |
| 3       | STORE A 13 |
| 4       | JUMP 2     |
| 5       | HALT       |
| 6       | 0          |
| 7       | 0          |
| 8       | 0          |
| 9       | 0          |
| 10      | 0          |
| 11      | 0          |
| 12      | 0          |
| 13      | 0          |
| 14      | 1          |
| 15      | 1          |
| ...     | ...        |

执行上述前观察，地址14，地址15已经提前赋值int 1

地址14的int 1存到 寄存器A---LOAD_A

寄存器B加载int 1，地址15的值---LOAD_B 15  

add 1+1 =2保存在寄存器A中---ADD B A   


A中int 2保存到地址13中---STORE A 13 


**跳转**第二行地址---JUMP 2

这时候寄存器A（int 2）B(int 1)
add 1+2 =3保存在寄存器A中---ADD B A   


...i++...死循环如果只是这样的话，



>0    a = 1;
1    b =1;
2    c = b + a;
3    register_c = c+a;
4    c = register_c;//寄存器值保存在地址c中
5    jump 3;


**等价**

```a = 1;b =1;c = b + a;while(true) {c = c+a};```

A中int 2保存到地址13中---STORE A 13 

停机指令---HALT


### **conditional 条件jump**

- 指令jump_negative，当今当ALU为负数跳转，比如for(int i =10;i>0:i--) {...10,...,3,2,1,0,当0-1=-1跳出循环jump_neg};

- 指令jump if equal相等时jump

- jump if greater大于时jump


RAM指令(从上往下读可以看作指令stack)：

|         |                                                                  |
| ------- | ---------------------------------------------------------------- |
| address | data                                                             |
| 0       | LOAD_A 14                                                        |
| 1       | LOAD_B 5                                                         |
| 2       | **SUB B A** 循环体用a-B，11-5=6存入寄存器A                          |
| 3       | JUMP_NEG 5 当6，1正数不跳转，-4跳转第五地址的指令                     |
| 4       | JUMP 2                                                           |
| 5       | **ADD B A**      循环体逆运算一次，撤销恢复为上一状态。A中-4+ B中5 = 1 |
| 6       | STORGE A 13           c=1                                        |
| 7       | HALT                                                             |
| 8       | 0                                                                |
| 9       | 0                                                                |
| 10      | 0                                                                |
| 11      | 0                                                                |
| 12      | 0                                                                |
| 13      | 0                                                                |
| 14      | 11                                                               |
| 15      | 5                                                                |
| ...     | ...                                                              |

连续-5直到负数

**等价**

```
a =11;
b = 5;
do{a = a - b}while(a<0);
```


目的是
```
11%5 = 1算余数，循环两次
```

同理可以打包这种步骤 实现为语法糖for：
>for(int i =0;i<10:i++) {...};



- 定长指令长度
- 变长指令长度


**inmediate value立即数**，HALT，JUMP 5中的**5**
指令 = 操作码+操作之地址；当指令 = 操作码+操作值 时，这个操作数就是立即数。




>while{...},

>do{...} while;







































































































