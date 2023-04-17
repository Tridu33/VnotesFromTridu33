# vscode配置c++c库



https://www.zhihu.com/question/44844423

可以在编译命令里用 “-I” 来添加其他include路径，c\_cpp\_properties.json那个只是给cpptools用的吧，实际还是执行shell命令编译和产生debug信息的。



同时修改c\_cpp\_properties.json（intellisense可以找到头文件）和task.json（编译时不报错）

CMakeLists.txt使用include_directories添加所需要的库的路径

c\_cpp\_properties.json是给vscode的c/c++插件用的, task.json和lauhch.json才是具体需要送给编译器的,工作原理大概就是吧这两个配置文件的信息传递给cmd命令行,类似于"gcc x.c -o x.exe \[-args...\]"所以如果在确定好编译器已经没有问题的时候, 是需要利用编译器"-I"参数来指定定义位置的(不管是内置的还是自定义的)

```
g++ -I /your/source/root /your/source/root/A/code.cpp
g++ -I /your/source/root /your/source/root/A/a/code2.cpp
```


在includePath中添加头文件目录好像就是为了使用intellisense，在编译的时候还是要传给gcc头文件所在的目录，可以在task.json中 用-I 和-L命令添加头文件和库文件目录

不过还是没有办法使用 gdb.exe 进行调试，报错还是说没有引用到头文件。照这个思路，launch.json 就是配置 gdb.exe 的，里面也有个 args\[\] 参数，但貌似 gdb 没有提供类似 gcc -I 的命令，也可能是我没找到。

Visual Studio Code的includePath该如何添加？ - Amberrrr的回答 - 知乎 https://www.zhihu.com/question/44844423/answer/148830687









































[VSCode中C/C++库文件的配置](https://www.cnblogs.com/jerry323/p/9174859.html)


再输入edit或者configuration，选择"C/Cpp:Edit Configurations"：
之后会在你的工作空间生成./.vscode/c_cpp_properties.json文件，我们需要做的就是配置这个文件的参数；

在“includePath”的属性中添加你的库文件的地址就行了，类似：


```
                "/home/**/Tools/opencv/cpu-install/include",
                "/home/**/Tools/opencv/gpu-install/include"

```






Windows环境下使用VSCode和CMake学习Eigen库的使用
https://blog.csdn.net/sinat_38245860/article/details/881
82226



YOUTUBE LINK:  [https://www.youtube.com/watch?v=wP4cwAtU-g8](https://www.youtube.com/watch?v=wP4cwAtU-g8)

Eigen： [http://eigen.tuxfamily.org/index.php?title=Main_Page](http://eigen.tuxfamily.org/index.php?title=Main_Page)

CMake：[https://cmake.org/](https://cmake.org/)   记得添加环境变量

Mingw64： [https://sourceforge.net/projects/mingw-w64/](https://sourceforge.net/projects/mingw-w64/)   记得添加环境变量

VSCODE插件：CMake CMake tools


