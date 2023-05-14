```
pythran -e demo.py -o  demo.hpp
```

pythran/pythonic/ 目录下是 python 标准库的 C++ 等价实现，翻译出来的 C++ 代码需要 include 这些头文件

```
g++ -g -std=c++11 main.cpp -fopenmp -march=native -DUSE_XSIMD -I /usr/local/lib/python3.6/site-packages/pythran/ -o pythran_demo
```

windows

```
g++ -g -std=c++11 main.cpp -fopenmp -march=native -DUSE_XSIMD -I C:\Users\HUMAN\anaconda3\envs\cudatf2torch\Lib\site-packages\pythran -o pythran_demo
```

```
> ./pythran_demo.exe
[[2, 3], [4, 5]]*[[1, 2], [3, 4]]
=
[[11, 16], [19, 28]]

arc_distance [0.129384 0.309546 0.403747],[ 0.25193 0.521009 0.306377],[ 0.729877  0.998712 0.0354819],[ 0.998372 0.0240817  0.738881]
=
```

Pythran 是一个 AOT (Ahead-Of-Time - 预先编译) 编译器。 给科学计算的 python 加注解后，pythran 可以把 python 代码变成接口相同的原生 python 模块，大幅度提升性能。

并且 pythran 也可以利用 OpenMP 多核和 SIMD 指令集。

支持 python 3 和 Python 2.7 。

https://link.zhihu.com/?target=https%3A//ppythran 并不支持完整的 python， 只支持 python 语言特性的一个子集:

- polymorphic functions 多态函数(翻译成 C++ 的泛型模板函数)
- lambda
- list comprehension 列表推导式
- map, reduce 等函数
- dictionary, set, list 等数据结构
- exceptions 异常
- file handling 文件处理
- 部分 numpy

不支持的功能：

- classes 类
- polymorphic variables 可变类型变量

ythran.readthedocs.io/en/latest/MANUAL.html