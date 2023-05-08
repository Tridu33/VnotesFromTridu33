[TOC]




# 1. loop








bilibli有翻译 https://www.bilibili.com/video/av21376839/

















## 1.1. 一个jump指令制造循环的例子循环





youtube.com/watch?v=zltgXvg6r3k&list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye&index=9

- 指令jump 10跳转行指令，而通常break跳出循环代码段，continue跳出本次循环进入下一次循环代码段：HALT停机指令

ATT 指令和Intel指令不一样，这里AT&T不影响理解就行。


RAM指令：

| address |    data    |
| ------- | ---------- |
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

















### 1.1.1. **conditional 条件jump**

- 指令jump_negative，当今当ALU为负数跳转，比如for(int i =10;i>0:i--) {...10,...,3,2,1,0,当0-1=-1跳出循环jump_neg};

- 指令jump if equal相等时jump

- jump if greater大于时jump


RAM指令(栈机的话，从上往下读指令，可以看作 指令栈stack)：


| address |                               data                               |
| ------- | ---------------------------------------------------------------- |
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

同理，可以用类似的方法，打包这种步骤 实现为语法糖for：
>for(int i =11;i<0:i=i-5) {...};



- 定长指令长度
- 变长指令长度


**inmediate value立即数**，HALT，JUMP 5中的**5**
指令 = 操作码+操作之地址；当指令 = 操作码+操作值 时，这个操作数就是立即数。




>while{...},

>do{...} while;



## 1.2. demo




函数式，递归.fix point不动点函数
```
summation :: (Num a, Ord a) => a -> a 
summation n 
    | n > 1 = n + summation (n-1) 
    | otherwise = 0
```

```
$>ghci sumamtion.hs
*Main> summation 100
5049
```

while 

```cpp
#include<stdio.h>
int main()
{
    int i=1,sum=0;
    while(i<=100)
    {
        sum+=i;
        i++;
    }
    printf("%d",sum);
    return 0;
}


```

do while

```cpp
#include<stdio.h>
int main()
{
    int i=1,sum=0;
    do
    {
        sum+=i;
        i++;
    }

    while(i<=100);

    printf("%d",sum);
    return 0;
}

//（do while循环体至少执行一次）
```



for
```cpp
#include<stdio.h>
int main()
{
    int i,sum=0;
    for(i=1; i<=100; i++)
    {
        sum+=i;
    }
    printf("%d",sum);

    return 0；
}
```




为什么在汇编语言中需大量使用跳转指令，而在C语言中却尽量避免使用goto语句呢？ - Milo Yip的回答 - 知乎
https://www.zhihu.com/question/66415361/answer/242845780


# 2. while语法糖转换for,do while

for的逻辑基本上是

```
for(each) item in iterable

```
而while要实现相同的逻辑，就需要

```
iter = iterable.iter();

item=iter.next();

while item.is_some() {

……

item=iter.next();

}
```

少了这么多行，就等于少了这么多出错机会。



而while比较常用的场合

while(true)，对应for(;;)(通常被读作forever)



do……while(false)，没有对应，但世界上只有两个语言需要这种操作。

while(flag)，对应for(;flag;)

虽然说for都可以做，但总有一种很奇怪的感觉。总得来说while更灵活一些，而for是为了遍历迭代器特化的。


所以大多数 正常 语言，都是把while作为通用循环，而for作为迭代器遍历来设计的，所以就有了foreach, for…in, for…of(论某语言的for…in居然是遍历key)，而最初的for ;;语法，有些语言就直接删掉了。



for循环与while循环可以相互转换，为什么要有多种循环？ - 「已注销」的回答 - 知乎
https://www.zhihu.com/question/333022884/answer/744626513






实际上程序设计中的loop有三大流派：for，while和goto。

goto是最强大的，可以随意跳转，早期可以起到提高效率的作用，但是后来人们发现精心的设计更复杂的算法大部分时候也能达到相同的目的，而且逻辑上更清楚，人看起来更明白，所以逐渐被放弃了。

for loop是直接控制循环次数的循环方式，个人认为这是一种数理逻辑思维的体现。它出现非常早，Quora上有人提到可能是由Lady Ada Lovelace最早提出来的，早期高级语言中Fortran以Do loop的形式提供支持，Algo以For loop的形式提供支持，当然还有其它一些表达形式，后来因为采用for loop形式的C语言盛行，所以后续语言都用了这个形式。

while loop是控制循环条件，感觉是更符合人类的语言逻辑的方式。早期高级语言中也有很多提供，比如Fortran以while和do while的形式提供，不知道最早提出者是谁，但是在由特定条件决定退出循环时可能更符合人的语言习惯一些。









## 2.1. Go中只for没有while

为Java程序员而准备的Go指南 - 极乐君的文章 - 知乎
https://zhuanlan.zhihu.com/p/24785820





For语句

Go既没有while语句也没有do-while语句。for语句可以用单个条件，如此等价于while语句。如果缺省整个条件将产生一个无限循环。

一个for语句可以包含一个range子句来遍历字符串、数组、切片、maps或者channels，而非写

```go
for i:=0;i<len(a);i++ {...}
```
想要循环a的所有元素，还可以这样写

```
for i,v := range a {...}
```
这为i赋予索引值，v赋予连续的数组，切片或字符串元素。对于字符串而言，i代表一个位的索引，v代表Unicode的code point，类型为rune（rune是int32的别名)。映射(map)的迭代器将产生key-value对，而通道(channel)只有一个迭代值。

Break和Continue

如Java，Go也允许break和continue指定一个标记，但标记必须是指向一个for，switch或select语句。































