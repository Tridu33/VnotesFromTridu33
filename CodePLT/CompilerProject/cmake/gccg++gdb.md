# 1. gccg++gdb
```c
-o：指定生成的输出文件；
-E：仅执行编译预处理；
-S：将C代码转换为汇编代码；
-wall：显示警告信息；
-c：仅执行编译操作，不进行连接操作。
```






gcc/g++

预处理
```
gcc/g++ -E hello.c -o hello.i
```


编译
```
gcc/g++ -S hello.i -o hello.s
```

汇编
```
gcc/g++ -c hello.s -o hello.o
```



链接
```
gcc/g++ hello.o -o hello
```

#是注释

## 1.1. 第一层显示规则
#目标文件:依赖文件
#[Tab]指令
#
#第一个目标文件是最终目标，递归，进栈,注意执行顺序
#rm -rf hello.o hello.s hello.i hello
#伪目标，不需要输入输出，只需要得到特定的操作：.PHONY:
#

```bash
hello2:hello2.o
	gcc hello2.o -o hello2

hello2.o:hello2.s
	gcc -c hello2.s -o hello2.o

hello2.s:hello2.i
	gcc -S hello2.i -o hello2.s

hello2.i:hello.c
	gcc -E hello.c -o hello2.i


.PHONY:
clean:
	rm -rf hello2.o hello2.s hello2.i
```
## 1.2. 第二层 
多文件依赖，有需要调用就编译

变量 = （替换） += （追加）  ：= （常量）
     使用变量 $（变量名）  替换


```bash
TAR = test
OBJ = circle.p cube.o main.o
CC  := gcc

$(TAR):$(OBJ)
    $(CC) $(OBJ) -o $(TAR)


circle.o:circle.c
    $(CC) -c circle.c -o circle.o

cube.o:cube.c
    $(CC) -c main.c -o main.o

main.o:main.c
    $(CC) -c main.c -o main.o

.PHONY:
clearall:
    rm -f $(OBJ) $(TAR)
clear:
    rm -f $(OBJ)
```





## 1.3. 第三层
隐含规则   %.c %.o 任意的.c或者.o    *.c  *.o所有的.c,.o


```bash
TAR = test
OBJ = circle.o cube.o main.o
CC  := gcc


$(TAR):$(OBJ)
    $(CC) $(OBJ) -o $(TAR)

%.o:%.c
    $(CC) -c %.c -o %.o

.PHONY:
clearall:
    rm -f $(OBJ) $(TAR)
clear:
    rm -f $(OBJ)

```




## 1.4. 第四层
通配符：

$^所有的依赖文件  $@所有的目标文件  $<所有的依赖文件的第一个文件
等等等，查书api就知道更多



```cmd
TAR=test
OBJ=circle.o cube.o main.o
CC:=gcc
RMRF:=rm -rf

$(TAR):$(OBJ)
    $(CC) $^ -o $@

%.o:%.c
    $(CC) -c $^ -o $@


.PHONY:
clearall:
    $(RMRF) $(OBJ) $(TAR)
clear:
    $(RMRF) $(OBJ)


```


## 1.5. 第五层
函数，入门：





```cmd



```













































