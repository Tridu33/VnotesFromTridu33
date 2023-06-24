[TOc]

# 1. DLLwindows DLL教程

dll和exe放在同一个目录、dll放在系统目录、dll放在PATH环境变量中的目录，exe都能正常运行





https://blog.csdn.net/zhouyang209117/article/details/17737413


C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\LaunchDevCmd.bat

cd 文件路径，然后运行就行。其实就是设置一些文件变量



windows中静态库lib和动态dll的区别及使用方法 - freethinker的文章 - 知乎 https://zhuanlan.zhihu.com/p/89106047




（windows平台下）深入详解C++创建动态链接库DLL以及如何使用它（一） - 沈鹏燕的文章 - 知乎 https://zhuanlan.zhihu.com/p/103082370





https://blog.csdn.net/zy0421911/article/details/73187648

https://blog.csdn.net/liujian8654562/article/details/78690359

  

extern "C" __declspec(dllexport)

https://www.cnblogs.com/OleNet/p/3171460.html

  

\[#ifndef, #define, #endif 作用\](https://www.cnblogs.com/challenger-vip/p/3386819.html)

























DLL是对应C语言的动态链接技术，在输出C函数和变量时显得方便快捷；而在输出C++类、函数时需要通过各种手段，而且也并没有完美的解决方案，除非客户端也是c++。

记住，只有COM是对应C++语言的技术。





```
C:\Users\admin>where cl.exe
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.25.28610\bin\Hostx64\x64\cl.exe
```
www.blogjava.net/wxb_nudt/archive/2007/09/11/144371.html

入门手册


https://download.csdn.net/download/hello_jwei/3470592


输入dumpbin -exports dllDemo.dll 命令，然后回车，即可查看DLL中的导出函数


```
dumpbin -exports dllDemo.dll 
```




































