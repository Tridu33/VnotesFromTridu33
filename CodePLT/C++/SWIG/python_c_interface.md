# 1. python_c_interface









        Ctypes
       Cython
        dll
        python
       SWIG
       
       
Weave : Python version 2.6 or 2.7 required.

ImportError: DLL load failed: %1 is not a valid Win32 application

Then it probably means you have 64 bit python but a 32 bit version of your package. Either find a precompiled version that is listed as 64 bit or you’ll have to compile it yourself.
————————————————
版权声明：本文为CSDN博主「Gavin_YY」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/olfisher/java/article/details/53822010

Ctypes

Cython

dll


python


SWIG




