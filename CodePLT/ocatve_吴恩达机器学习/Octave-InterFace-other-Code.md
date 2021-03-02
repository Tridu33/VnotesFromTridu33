# 1. Octave-InterFace-other-Code





Appendix A External Code Interface













话虽如此，Octave提供了一个通用接口，用于将已编译的代码块作为动态链接的扩展包括在内。  
可以以与任何普通函数相同的方式从解释器中调用这些动态链接的函数。  
接口是双向的，外部代码可以调用Octave函数（例如plot），否则可能很难开发。  
该界面以支持C ++，C和Fortran语言为中心。  
八度本身是用C ++编写的，可以通过其本机八进制文件接口调用外部C ++ / C代码。  
还通过mex-file接口支持C语言，以与MATLAB兼容。  
最容易通过八文件接口访问Fortran代码。  
由于许多其他语言都提供C或C ++ API，因此在Octave与其他语言之间建立桥梁相对简单。  
这也是桥接通常使用C语言编写的设备驱动程序的硬件资源的方法。







