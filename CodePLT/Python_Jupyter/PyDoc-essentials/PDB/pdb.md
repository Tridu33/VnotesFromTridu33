# pdb




jianshu.com/p/fb5f791fcb18


| 命令 | 解释 |
| --- | --- |
| break 或 b 设置断点 | 设置断点 |
| continue 或 c | 继续执行程序 |
| list 或 l | 查看当前行的代码段 |
| step 或 s | 进入函数 |
| return 或 r | 执行代码直到从当前函数返回 |
| exit 或 q | 中止并退出 |
| next 或 n | 执行下一行 |
| pp | 打印变量的值 |
| help | 帮助 |

1.py

```python
 import pdb 
 a = "aaa"
 pdb.set_trace() 
 b = "bbb"
 c = "ccc"
 final = a + b + c 
 print final
```

2.py

函数

```python
import pdb 
 def combine(s1,s2):      # define subroutine combine, which... 
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ... 
    s3 = '"' + s3 +'"'   # encloses it in double quotes,... 
    return s3            # and returns it. 
 a = "aaa"
 pdb.set_trace() 
 b = "bbb"
 c = "ccc"
 final = combine(a,b) 
 print final
```


调试过程中修改变量值


```
[root@rcc-pok-idg-2255 ~]# python epdb2.py 
 > /root/epdb2.py(10)?() 
 -> b = "bbb"
 (Pdb) var = "1234"
 (Pdb) b = "avfe"
 *** The specified object '= "avfe"' is not a function 
 or was not found along sys.path. 
 (Pdb) !b="afdfd"
 (Pdb)
```





