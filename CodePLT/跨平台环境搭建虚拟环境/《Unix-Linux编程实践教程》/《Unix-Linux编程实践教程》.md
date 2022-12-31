https://linux.die.net/man/





https://www.kernel.org/doc/man-pages/








# 1. 《Unix-Linux编程实践教程》







系统函数 `man 2 foo`

标准库 `man 3 bar`


自从看了《Unix/Linux编程实践教程》（五星推荐这本书），查看头文件和函数信息非常方便。

`man -k keyword | grep "name" `查找一个man手册中的简短说明包含keyword的函数，name为函数名的关键字（可以不加管道）
如 `man -k timer | grep "set"` 查找一个man手册中的简短说明包含timer的函数，set为函数名的关键字（可以不加管道），可以查找到以下信息：

```
getitimer (2) - get or set value of an interval timer
setitimer (2) - get or set value of an interval timer
timer_settime (2) - arm/disarm and fetch state of POSIX per-process timer
timerfd_settime (2) - timers that notify via file descriptors
timerisset (3) - timeval operations
```

**函数调用**任君选择。

```
grep "keyword" /usr/include/*.h | grep "typedef"
grep "keyword" /usr/include/*/*.h | grep "typedef"
```

如 `grep "time_t" /usr/include/*.h | grep "typedef"`
可以查找到 `" typedef __time_t time_t; "`

以上方法可以查找关键字为keyword的结构体、类型、函数原型的定义，typedef可以替换为define尝试查找，几次重复查找找到的定义，就能最终确定。



`locate keyword.h` 可以查找名为keyword的头文件所在的目录树

如` locate time.h | grep "/usr/include"` 可以查找到一下信息：

```
/usr/include/time.h

/usr/include/utime.h

/usr/include/i386-linux-gnu/bits/time.h

/usr/include/i386-linux-gnu/sys/time.h

/usr/include/linux/time.h

/usr/include/linux/utime.h

/usr/include/linux/netfilter/xt_time.h

/usr/include/python2.7/datetime.h
```


**头文件**任君选择。


Linux 中如何快速查看 C 库函数的头文件以及相应的函数信息？ - 蒲公英的回答 - 知乎
https://www.zhihu.com/question/25028178/answer/118144386


从此在linux下编程，查找函数原型、头文件、类型定义方便多了。







