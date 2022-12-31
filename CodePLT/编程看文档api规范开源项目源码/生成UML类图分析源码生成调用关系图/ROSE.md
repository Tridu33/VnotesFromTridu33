# 1. ROSE





ROSE的目标是：
http://rosecompiler.org/ROSE_HTML_Reference/index.html




https://github.com/rose-compiler/rose/wiki#basic-info










一个库（和一组相关工具），用于快速轻松地将编译器技术应用于自己的代码，以提高应用程序性能和开发人员的生产力。
研究和开发编译器基础结构，用于编写自定义的源到源转换器以执行源代码转换，分析和优化。


ROSE是一个开放源代码的编译器基础设施建设源到源程序转换和分析工具

为大型C（C89和C98），C ++（C ++ 98和C ++ 11），UPC，Fortran（77，95，2003），OpenMP，Java，Python，PHP和Binary应用程序。ROSE的用户从经验丰富的编译器研究人员到库或工具开发人员，他们对编译器的经验最少。ROSE特别适合于构建用于静态分析，程序优化，任意程序转换，特定于域的优化，复杂的循环优化，性能分析和网络安全的自定义工具。


```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:rosecompiler/rose-development # Replace rose-development with rose-stable for release version
sudo apt-get install rose
sudo apt-get install rose-tools # Optional: Installs ROSE tools in addition to ROSE Core
```

安装时lic-lib在wsl安装[报错](https://github.com/microsoft/WSL/issues/4760)就行。


https://github.com/matzke1/sawyer
About
用于开发C ++库和工具，命令行解析，诊断输出，断言，容器等的库。


用于有条件地发出诊断的流，包括逻辑断言和基于文本的进度条

用于程序命令行的解析器，并自动生成Unix手册页。

容器，包括Graph，IndexedList，IntervalSet，IntervalMap，Map和BitVector。

杂项：内存池分配器，小对象支持，类似于秒表的计时器，可选值。

























