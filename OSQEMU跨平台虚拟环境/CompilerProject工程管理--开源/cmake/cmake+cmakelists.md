https://zhuanlan.zhihu.com/p/461718845
cmake相关参数


# cmakelists


```cmake
C:\Users\admin\Documents\Tridu33\Cmake\build-codeblock>cmake .. -G"CodeBlocks - MinGW Makefiles"
CMake Error at C:/Program Files/CMake/share/cmake-3.15/Modules/CMakeMinGWFindMake.cmake:12 (message):
  sh.exe was found in your PATH, here:

  C:/Program Files (x86)/Git/bin/sh.exe

  For MinGW make to work correctly sh.exe must NOT be in your path.

  Run cmake from a shell that does not have sh.exe in your PATH.

  If you want to use a UNIX shell, then use MSYS Makefiles.

Call Stack (most recent call first):
  CMakeLists.txt:1 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!

```

删除环境变量C:\Program Files (x86)\Git\bin,cmake ..默认生成垃圾VS工程，享用CodeBlock在Windows环境要这么做！

```
C:\Users\admin\Documents\Tridu33\Cmake\build-codeblock>cmake .. -G"CodeBlocks - MinGW Makefiles"
-- The C compiler identification is GNU 7.2.0
-- The CXX compiler identification is GNU 7.2.0
-- Check for working C compiler: C:/Program Files/Haskell Platform/8.6.3/mingw/bin/gcc.exe
-- Check for working C compiler: C:/Program Files/Haskell Platform/8.6.3/mingw/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: C:/Program Files/Haskell Platform/8.6.3/mingw/bin/g++.exe
-- Check for working CXX compiler: C:/Program Files/Haskell Platform/8.6.3/mingw/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Users/admin/Documents/Tridu33/Cmake/build-codeblock


```

https://blog.csdn.net/u013896064/article/details/82874152
多头文件多项目
https://blog.csdn.net/afei__/article/details/81201039


https://www.jianshu.com/p/bbf68f9ddffa

cmake+codeblock

！https://blog.csdn.net/afei__/article/details/81201039


https://blog.csdn.net/OKasy/article/details/79550781


https://blog.csdn.net/CSDNhuaong/article/details/80895679


# cmake+vs



https://blog.csdn.net/weixin_34088598/article/details/86002994




# Cmake+codeblock+LLVM
https://blog.csdn.net/myjisgreat/article/details/46486675


# CMake配合CodeBlocks编译FLTK


https://blog.csdn.net/huyoo/article/details/44727865










