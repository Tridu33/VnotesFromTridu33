[TOC]


# Extern

www.blogjava.net/wxb_nudt/archive/2007/09/11/144371.html





```
__declspec(dllexport) void FuncInDll (void)
```
   

```
extern "C" __declspec(dllexport) void FuncInDll (void);
```


显式调用显得非常复杂，每次都要LoadLibrary，并且每个函数都必须使用GetProcAddress来得到函数指针，这对于大量使用dll函数的客户是一种困扰。而隐式调用能够像使用c函数库一样使用dll中的函数，非常方便快捷

何时使用显式调用？何时使用隐式调用？我认为，只有一个时候使用显式调用是合理的，就是当客户端不是C/C++的时候。这时是无法隐式调用的。例如Plant Simulation软件混合编程

在进行隐式调用的时候需要在客户端引入头文件，并在链接时指明dll对应的lib文件（dll只要有函数输出，则链接的时候会产生一个与dll同名的lib文件）位置和名称。然后如同调用api函数库中的函数一样调用dll中的函数，不需要显式的LoadLibrary和GetProcAddress。使用最为方便。客户端代码如下：dll_withlibAndH_client.cpp

dll和exe放在同一个目录、dll放在系统目录、dll放在PATH环境变量中的目录，exe都能正常运行

静态链接库(Lib)与动态链接库(DLL)的区别 

https://blog.csdn.net/yusiguyuan/article/details/12649737

# 从其它语言调用DLL

从其它编程语言中调用DLL，有两个最大的问题，第一个就是函数符号的问题，前面已经多次提过了。这里有个两难选择，若使用extern “C”，则函数名称保持不变，调用较方便，但是不支持函数重载等一系列c++功能；若不使用extern “C”，则调用前要查看编译后的符号，非常不方便。

第二个问题就是函数调用压栈顺序的问题，即__cdecl和__stdcall的问题。__cdecl是常规的C/C++调用约定，这种调用约定下，函数调用后栈的清理工作是由调用者完成的。__stdcall是标准的调用约定，即这些函数将在返回到调用者之前将参数从栈中删除。

这两个问题DLL都不能很好的解决，只能说凑合着用。但是在COM中，都得到了完美的解决。所以，要在Windows平台实现语言无关性，还是只有使用COM中间件。

总而言之，除非客户端也使用C++，否则dll是不便于支持函数重载、类等c++特性的。DLL对c函数的支持很好，我想这也是为什么windows的函数库使用C加dll实现的理由之一。









































































