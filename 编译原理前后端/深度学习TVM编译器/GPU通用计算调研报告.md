# 1. GPU通用计算调研报告






跨平台shader编译的过去、现在和未来 - 叛逆者的文章 - 知乎
https://zhuanlan.zhihu.com/p/25024372跨平台shader编译的过去、现在和未来 - 叛逆者的文章 - 知乎
https://zhuanlan.zhihu.com/p/25024372



图形流水线中可编程单元的行为由Shader单元定义，着色器的性能由DirectX中规定的Shader Model来区分，并可以由高级的Shading语言（例如NV的Cg，OpenGL的GLSL，Microsoft的HLSL）编写。Shader源码被译为字节码，然后在运行时由驱动程序将其转化为基于特定GPU的二进制程序，具备可移植性好等优势。


https://wenku.baidu.com/view/3a8af916ff00bed5b9f31d58.html








最早的GPGPU开发直接使用图形学API编程。这种开发方式要求程序员将数据打包成纹理，将计算任务映射为对纹理的渲染过程，用汇编或者高级着色语言（如GLSL，Cg，HLSL）编写shader程序，然后通过图形学API（Direct3D、OpenGL）执行。



2003年斯坦福大学的Ian Buck等人对ANSI C进行扩展，开发了基于NVIDIA Cg的Brook源到源编译器。Brook可以将类似C的brook C语言通过brcc编译器编译为Cg代码，隐藏了利用图形学API实现的细节，大大简化了开发过程。





AMD在其GPGPU通用计算产品Stream中采用Brook的改进版本Brook+作为高级开发语言。Brook+的编译器工作方式与Brook不同，提高了效率[7]。





OpenCL (Open Computing Language，开放计算语言) 是一个为异构平台编写程序的框架，此异构平台可由CPU、GPU或其他类型的处理器组成。


CUDA是一种将GPU作为数据并行计算设备的软硬件体系，硬件上NVIDIA GeForce 8系列以后的GPU（包括GeForce、ION、Quadro、Tesla系列）已经采用支持CUDA的架构，软件开发包上CUDA也已经发展到CUDA Toolkit 3.2（截止到2010年11月），并且支持Windows、Linux、MacOS三种主流操作系统。CUDA采用比较容易掌握的类C语言进行开发，而且正在开发适用于CUDA架构的用于科学计算的Fortran版本。无论是CUDA C-语言或是OpenCL，指令最终都会被驱动程序转换成PTX（Parallel Thread Execution，并行线程执行，CUDA架构中的指令集，类似于汇编语言）代码，交由显示核心计算[8]。
























































