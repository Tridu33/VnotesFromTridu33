[TOC]




>我发现一定要用他目录下的gcc/g++开发，cmake包含头文件目录目录octave什么的，那样才能与无缝对接，Visual Studio这种情况下误我！
>环境变量C:\Octave\Octave-5.1.0.0\mingw64\bin\gcc.exe移动到最前面才不会有全局污染，最简单的方法还是看liboctave.a,liboctave.so对应的liboctave.pdf类库包，找相应的头文件偷代码,安装目录下的gcc还是不行，内部一定有什么编译约定（比如链接目录之类的）只能用mkoctfile.exe,可能问看好源码问issuse会知道，着急省事儿的话必须直接用mkoctfile.exe编译，或者最好的方法是下载octave源码编译，然后直接在源码找来修改，而不是安装无脑的octave.exe阉割版，真正的勇者还是要硬刚源码。
# 1. c++类in_Octave-liboctave.pdf
"The sum of human wisdom is not contained in any one language"
— Ezra Pound



Octave itself is written in C++ and can call external C++/C code through its native oct-file interface. 
The C language is also supported through the mex-file interface for compatibility with MATLAB. Fortran code is easiest to reach through the oct-file interface. 

```
mkoctfile --link-stand-alone standalonebuiltin.cc -o standalonebuiltin
```

## 1.1. oct

Oct-files are pieces of C++ code that have been compiled with the Octave API into a dynamically loadable object.

Finding a C++ compiler, using the correct switches, adding the right include paths for header files, etc. is a difficult task. Octave automates this by providing the mkoctfile command with which to build oct-files. 


mkoctfile [-选项]文件…[输出，状态] = mkoctfile（…）mkoctfile函数编译用C，C ++或Fortran编写的源代码。

根据与mkoctfile一起使用的选项，可以在Octave中调用已编译的代码，也可以将其用作独立的应用程序。

可以从Shell提示符或Octave提示符调用mkoctfile。

从八度提示中调用它仅会将调用委派给shell提示。
输出存储在输出变量中，退出状态存储在状态变量中。 

mkoctfile接受以下选项，除了要编译的代码的文件名之外，所有这些都是可选的：
```
'-I DIR'将include目录DIR添加到编译命令中。 
“ -D DEF”将定义DEF添加到编译器调用中。 
‘-l LIB’将库LIB添加到链接命令。 
“ -L DIR”将库目录DIR添加到链接命令。 
'-M''--depend'为C和C ++源文件生成依赖文件（.d）。 
“ -R DIR”将运行时路径添加到链接命令。 
‘-Wl，…’将选项传递给链接器，例如“ -Wl，-rpath =…”。
需要使用引号，因为逗号被解释为命令分隔符。 
“ -W…”将选项传递给汇编器，例如“ -Wa，OPTION”。 
'-c'编译但不链接。 
‘-g’启用编译器的调试选项。 
'-o FILE''--output FILE'输出文件名。
除非链接独立的可执行文件，否则默认扩展名是.oct（如果指定为--mex，则为.mex）。 
'-p VAR''--print VAR'打印配置变量VAR。
变量分为三类：用户可以使用环境变量覆盖的八度配置变量。
这些在mkoctfile执行的命令中使用。
```
The procedure entry point XXX could not be located in the dynamic link library XXX.exe
Octave中，因为全局安装了gcc等等不相同版本的gcc,g++导致**全局污染**
原因及分析：

此时由于.library和.dll文件版本不匹配造成的。比如.lib里有20个函数，.dll只有19个函数，当windows加载动态链接库的时候，它检查是否匹配，否则报错。

在项目需要运行多个不同版本的dll文件时候，容易出现此问题。此时隐式调用Dll。

解决办法：

采用显示调用，手工加载的办法。

1）声明函数指针原型。

2）LoadLibrary（）

3）GetProcAddress（）

4）比较重要，在调用此函数指针的时候，判断是否NULL。因为在dll文件里没有实现的函数指针是NULL。








































## 1.2. mex








## 1.3. standalone



```
mkoctfile --link-stand-alone a.cc -o a

```

1
```
#include <iostream>
#include <octave/oct.h>

int
main (void)
{
  std::cout << "Hello Octave world!\n";

  int n = 2;
  Matrix a_matrix = Matrix (n, n);

  for (octave_idx_type i = 0; i < n; i++)
    for (octave_idx_type j = 0; j < n; j++)
      a_matrix(i,j) = (i + 1) * 10 + (j + 1);

  std::cout << a_matrix;

  return 0;
} 

```

2


```
#include <iostream>
#include <octave/oct.h>
#include <octave/builtin-defun-decls.h>

int
main (void)
{
  int n = 2;
  Matrix a_matrix = Matrix (n, n);

  for (octave_idx_type i = 0; i < n; i++)
    for (octave_idx_type j = 0; j < n; j++)
      a_matrix(i,j) = (i + 1) * 10 + (j + 1);

  std::cout << "This is a matrix:" << std::endl
            << a_matrix            << std::endl;

  octave_value_list in;
  in(0) = a_matrix;

  octave_value_list out = Fnorm (in, 1);
  double norm_of_the_matrix = out(0).double_value ();

  std::cout << "This is the norm of the matrix:" << std::endl
            << norm_of_the_matrix                << std::endl;

  return 0;
} 

```
3

```
#include <iostream>
#include <octave/oct.h>
#include <octave/octave.h>
#include <octave/parse.h>
#include <octave/interpreter.h>

int
main (void)
{
  // Create interpreter.

  octave::interpreter interpreter;

  try
    {
      // Inhibit reading history file by calling
      //
      //   interpreter.initialize_history (false);

      // Set custom load path here if you wish by calling
      //
      //   interpreter.initialize_load_path (false);

      // Perform final initialization of interpreter, including
      // executing commands from startup files by calling
      //
      //   int status interpreter.initialize ();
      //
      //   if (! interpreter.initialized ())
      //     {
      //       std::cerr << "Octave interpreter initialization failed!"
      //                 << std::endl;
      //       exit (status);
      //     }
      //
      // You may skip this step if you don't need to do anything
      // between reading the startup files and telling the interpreter
      // that you are ready to execute commands.

      // Tell the interpreter that we're ready to execute commands:

      int status = interpreter.execute ();

      if (status != 0)
        {
          std::cerr << "creating embedded Octave interpreter failed!"
                    << std::endl;
          return status;
        }

      octave_idx_type n = 2;
      octave_value_list in;

      for (octave_idx_type i = 0; i < n; i++)
        in(i) = octave_value (5 * (i + 2));

      octave_value_list out = octave::feval ("gcd", in, 1);

      if (out.length () > 0)
        std::cout << "GCD of ["
                  << in(0).int_value ()
                  << ", "
                  << in(1).int_value ()
                  << "] is " << out(0).int_value ()
                  << std::endl;
      else
        std::cout << "invalid\n";
    }
  catch (const octave::exit_exception& ex)
    {
      std::cerr << "Octave interpreter exited with status = "
                << ex.exit_status () << std::endl;
    }
  catch (const octave::execution_exception&)
    {
      std::cerr << "error encountered in Octave evaluator!" << std::endl;
    }

  return 0;
} 

```



## 1.4. JAva





































































































































