


# 1. 控制流分析




分析程序代码的流程，control flow analysis






基本代码块basic block:中途不会跳转，也不会从其他代码跳转过来的代码块。比如下面的if语句后then部分和else部分都是“基本代码块”：


```
int i,ret;
for(i = 0;i<10;i++){
    if(i<5){
        int x = i + 5;
        ret = x*x;
    }else{
        int y = i*2 +1;
        ret = y*y;
    };
    }
```



# 2. SSA形式Static single assignment form

GCC第四个版本就是使用SSA形式的中间代码













```
int i = x +5；
i+= 6；
i*= 2；

```




变成SSA形式：

```
int i0 = x +5;
i1 = i0 +6;
i2 = i1*2;
```






























