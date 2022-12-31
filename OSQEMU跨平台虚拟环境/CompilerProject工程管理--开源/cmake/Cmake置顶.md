[TOC]
# 1. Cmake越来越Fashion,,读取执行CMakeLists.txt生成Makefile


```
mkdir build
cd build
cmake ..
```
直接生成visual studio 2019文件，使用的工具链是cl.exe

如果想用Ninja工具链
```
cmake -Bbuild -GNinja
cd build
ninja
pause
```
如果想用GNU的Mingw64工具链



```
mkdir build
cd build
cmake -G "MinGW Makefiles" ..
make
```



CMake命令/函数汇总（翻译自官方手册）


https://www.cnblogs.com/52php/p/5684588.html

https://cmake.org/cmake/help/v3.4/manual/cmake-commands.7.html



























帮助


```
>cmake -h
Usage

  cmake [options] <path-to-source>
  cmake [options] <path-to-existing-build>
  cmake [options] -S <path-to-source> -B <path-to-build>

Specify a source directory to (re-)generate a build system for it in the
current working directory.  Specify an existing build directory to
re-generate its build system.

Options
  -S <path-to-source>          = Explicitly specify a source directory.
  -B <path-to-build>           = Explicitly specify a build directory.
  -C <initial-cache>           = Pre-load a script to populate the cache.
  -D <var>[:<type>]=<value>    = Create or update a cmake cache entry.
  -U <globbing_expr>           = Remove matching entries from CMake cache.
  -G <generator-name>          = Specify a build system generator.
  -T <toolset-name>            = Specify toolset name if supported by
                                 generator.
  -A <platform-name>           = Specify platform name if supported by
                                 generator.
  -Wdev                        = Enable developer warnings.
  -Wno-dev                     = Suppress developer warnings.
  -Werror=dev                  = Make developer warnings errors.
  -Wno-error=dev               = Make developer warnings not errors.
  -Wdeprecated                 = Enable deprecation warnings.
  -Wno-deprecated              = Suppress deprecation warnings.
  -Werror=deprecated           = Make deprecated macro and function warnings
                                 errors.
  -Wno-error=deprecated        = Make deprecated macro and function warnings
                                 not errors.
  -E                           = CMake command mode.
  -L[A][H]                     = List non-advanced cached variables.
  --build <dir>                = Build a CMake-generated project binary tree.
  --install <dir>              = Install a CMake-generated project binary
                                 tree.
  --open <dir>                 = Open generated project in the associated
                                 application.
  -N                           = View mode only.
  -P <file>                    = Process script mode.
  --find-package               = Run in pkg-config like mode.
  --graphviz=[file]            = Generate graphviz of dependencies, see
                                 CMakeGraphVizOptions.cmake for more.
  --system-information [file]  = Dump information about this system.
  --log-level=<ERROR|WARNING|NOTICE|STATUS|VERBOSE|DEBUG|TRACE>
                               = Set the verbosity of messages from CMake
                                 files.  --loglevel is also accepted for
                                 backward compatibility reasons.
  --log-context                = Prepend log messages with context, if given
  --debug-trycompile           = Do not delete the try_compile build tree.
                                 Only useful on one try_compile at a time.
  --debug-output               = Put cmake in a debug mode.
  --debug-find                 = Put cmake find in a debug mode.
  --trace                      = Put cmake in trace mode.
  --trace-expand               = Put cmake in trace mode with variable
                                 expansion.
  --trace-format=<human|json-v1>
                               = Set the output format of the trace.
  --trace-source=<file>        = Trace only this CMake file/module.  Multiple
                                 options allowed.
  --trace-redirect=<file>      = Redirect trace output to a file instead of
                                 stderr.
  --warn-uninitialized         = Warn about uninitialized values.
  --warn-unused-vars           = Warn about unused variables.
  --no-warn-unused-cli         = Don't warn about command line options.
  --check-system-vars          = Find problems with variable usage in system
                                 files.
  --help,-help,-usage,-h,-H,/? = Print usage information and exit.
  --version,-version,/V [<f>]  = Print version number and exit.
  --help-full [<f>]            = Print all help manuals and exit.
  --help-manual <man> [<f>]    = Print one help manual and exit.
  --help-manual-list [<f>]     = List help manuals available and exit.
  --help-command <cmd> [<f>]   = Print help for one command and exit.
  --help-command-list [<f>]    = List commands with help available and exit.
  --help-commands [<f>]        = Print cmake-commands manual and exit.
  --help-module <mod> [<f>]    = Print help for one module and exit.
  --help-module-list [<f>]     = List modules with help available and exit.
  --help-modules [<f>]         = Print cmake-modules manual and exit.
  --help-policy <cmp> [<f>]    = Print help for one policy and exit.
  --help-policy-list [<f>]     = List policies with help available and exit.
  --help-policies [<f>]        = Print cmake-policies manual and exit.
  --help-property <prop> [<f>] = Print help for one property and exit.
  --help-property-list [<f>]   = List properties with help available and
                                 exit.
  --help-properties [<f>]      = Print cmake-properties manual and exit.
  --help-variable var [<f>]    = Print help for one variable and exit.
  --help-variable-list [<f>]   = List variables with help available and exit.
  --help-variables [<f>]       = Print cmake-variables manual and exit.

Generators

The following generators are available on this platform (* marks default):
  Visual Studio 16 2019        = Generates Visual Studio 2019 project files.
                                 Use -A option to specify architecture.
  Visual Studio 15 2017 [arch] = Generates Visual Studio 2017 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 14 2015 [arch] = Generates Visual Studio 2015 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 12 2013 [arch] = Generates Visual Studio 2013 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 11 2012 [arch] = Generates Visual Studio 2012 project files.
                                 Optional [arch] can be "Win64" or "ARM".
  Visual Studio 10 2010 [arch] = Generates Visual Studio 2010 project files.
                                 Optional [arch] can be "Win64" or "IA64".
  Visual Studio 9 2008 [arch]  = Generates Visual Studio 2008 project files.
                                 Optional [arch] can be "Win64" or "IA64".
  Borland Makefiles            = Generates Borland makefiles.
* NMake Makefiles              = Generates NMake makefiles.
  NMake Makefiles JOM          = Generates JOM makefiles.
  MSYS Makefiles               = Generates MSYS makefiles.
  MinGW Makefiles              = Generates a make file for use with
                                 mingw32-make.
  Unix Makefiles               = Generates standard UNIX makefiles.
  Green Hills MULTI            = Generates Green Hills MULTI files
                                 (experimental, work-in-progress).
  Ninja                        = Generates build.ninja files.
  Ninja Multi-Config           = Generates build-<Config>.ninja files.
  Watcom WMake                 = Generates Watcom WMake makefiles.
  CodeBlocks - MinGW Makefiles = Generates CodeBlocks project files.
  CodeBlocks - NMake Makefiles = Generates CodeBlocks project files.
  CodeBlocks - NMake Makefiles JOM
                               = Generates CodeBlocks project files.
  CodeBlocks - Ninja           = Generates CodeBlocks project files.
  CodeBlocks - Unix Makefiles  = Generates CodeBlocks project files.
  CodeLite - MinGW Makefiles   = Generates CodeLite project files.
  CodeLite - NMake Makefiles   = Generates CodeLite project files.
  CodeLite - Ninja             = Generates CodeLite project files.
  CodeLite - Unix Makefiles    = Generates CodeLite project files.
  Sublime Text 2 - MinGW Makefiles
                               = Generates Sublime Text 2 project files.
  Sublime Text 2 - NMake Makefiles
                               = Generates Sublime Text 2 project files.
  Sublime Text 2 - Ninja       = Generates Sublime Text 2 project files.
  Sublime Text 2 - Unix Makefiles
                               = Generates Sublime Text 2 project files.
  Kate - MinGW Makefiles       = Generates Kate project files.
  Kate - NMake Makefiles       = Generates Kate project files.
  Kate - Ninja                 = Generates Kate project files.
  Kate - Unix Makefiles        = Generates Kate project files.
  Eclipse CDT4 - NMake Makefiles
                               = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - MinGW Makefiles
                               = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Ninja         = Generates Eclipse CDT 4.0 project files.
  Eclipse CDT4 - Unix Makefiles= Generates Eclipse CDT 4.0 project files.
  
```


[含字幕) 使用 VSCode CMake 构建 C/C++ IDE](https://www.bilibili.com/video/av93037182/)
[cmake链接https://www.bilibili.com/video/BV1A7411f7jT?p=1](https://www.bilibili.com/video/BV1A7411f7jT?p=1)


[https://github.com/bhlzlx/cplusplus_tutorial/blob/master/CMakeLists.txt](https://github.com/bhlzlx/cplusplus_tutorial/blob/master/CMakeLists.txt)











[gcc-cmake基础https://www.bilibili.com/video/av83986896/?spm\_id\_from=333.788.b_636f6d6d656e74.108](https://www.bilibili.com/video/av83986896/?spm_id_from=333.788.b_636f6d6d656e74.108)

[入门https://github.com/wzpan/cmake-demo](https://github.com/wzpan/cmake-demo)







[https://www.hahack.com/codes/cmake/](https://www.hahack.com/codes/cmake/)






* 设置工程文件
* 设置包含目录
* 设置库目录
* 添加静态库
* 添加动态库
* 添加可执行程序


简单的Cmake文件->生成链接库（静态&动态）->如何引用链接库（内布&外部）->更简单的组织Cmake的编译方式

当程序复杂时候，一般用Cmake和autotools，qmake工具集自动生成Makefile

https://github.com/szza/LearningNote/blob/master/Tools/2.%20CMake_%E5%BA%94%E7%94%A8.md

# 2. ***`cmake`***

https://github.com/szza/LearningNote/blob/master/Tools/1.%20CMake.md#cmake%E4%B8%AD%E7%9A%84%E5%8F%98%E9%87%8F  `CMake`中的变量

-   变量和含义
    
    | 常用变量 | 含义 |
    | :-: | :-: |
    | ***`PROJECT_NAME`*** | 工程名变量 |
    | ***`PROJECT_SOURCE_DIR`*** | 顶层的项目目录 |
    | ***`PROJECT_BINARY_DIR`*** | 使用`cmake`的路径 |
    | ***`CMAKE_ROOT`*** | `CMAKE`安装的根目录 |
    | ***`CMAKE_BUILD_TYPE`*** | 编译类型：`empty`，`Debug`，`Release`... |
    | ***`CMAKE_SOURCE_DIR`*** | 顶层的`CMakeLists.txt`所在路径 |
    | ***`CMAKE_BINARY_DIR`*** | 顶层的`CMakeLists.txt`的`build`所在目录 |
    | ***`CMAKE_<LANG>_COMPILER`*** | 设定某个语言`LANG`的编译器，比如`g++` |
    | ***`CMAKE_INSTALL_PREFIX`*** | 指令`install`的路径 |
    | ***`CMAKE_CURRENT_SOURCE_DIR`*** | 当前`CMakeLists.txt`所在路径 |
    | ***`CMAKE_CURRENT_BINARY_DIR`*** | 当前`CMakeLists.txt`的`build`所在目录 |
    | ***`EXECUTABLE_OUTPUT_PATH`*** | 可执行文件输出路径 |
    | ***`LIBRARY_OUTPUT_PATH`*** | 库输出路径 |
    
-   个别变量解释 [源码](https://github.com/szza/LearningNote/blob/master/Tools/smuduo)目录结构
    
    ```shell
        jmudou   
        ├── build.sh
        ├── CMakeLists.txt
        └── muduo
           └── base
               ├── Atomic.h
               ├── CMakeLists.txt
               ├── copyable.h
               ├── tests
               │   ├── Atomic_unittest.cc
               │   ├── CMakeLists.txt
               │   └── Timestamp_unittest.cc
               ├── Timestamp.cc
               ├── Timestamp.h
               └── Types.h
    ```
    
    三个`CMakeLists.txt`输出
    
    ```cmake
        jmuduo/CMakeLists.txt: 
            PROJECT_SOURCE_DIR= 11/jmuduo
            PROJECT_BINARY_DIR= 11/build/debug 
            CMAKE_SOURCE_DIR= 11/jmuduo            # 指定顶层的CMakeLists.txt的，因此所有的都相同
            CMAKE_BINARY_DIR= 11/build/debug
            # 上面四项都是与整个项目相关，因此都是一致的。
            CMAKE_CURRENT_SOURCE_DIR= 11/jmuduo     # 指定当前层的CMakeLists.txt的，因此与层相关
            CMAKE_CURRENT_BINARY_DIR= 11/build/debug
    
        muduo/base/test/CMakeLists.txt: 
            PROJECT_SOURCE_DIR= 11/jmuduo
            PROJECT_BINARY_DIR= 11/build/debug
            CMAKE_SOURCE_DIR= 11/jmuduo
            CMAKE_BINARY_DIR= 11/build/debug
            CMAKE_CURRENT_SOURCE_DIR= 11/jmuduo/muduo/base/tests
            CMAKE_CURRENT_BINARY_DIR= 11/build/debug/muduo/base/tests
    
        muduo/base/CMakeLists.txt: 
            PROJECT_SOURCE_DIR= 11/jmuduo
            PROJECT_BINARY_DIR= 11/build/debug
            CMAKE_SOURCE_DIR= 11/jmuduo
            CMAKE_BINARY_DIR= 11/build/debug
            CMAKE_CURRENT_SOURCE_DIR= 11/jmuduo/muduo/base
            CMAKE_CURRENT_BINARY_DIR= 11/build/debug/muduo/base
    ```
    

https://github.com/szza/LearningNote/blob/master/Tools/1.%20CMake.md#%E5%87%BD%E6%95%B0  函数`

所有的函数列表中，`<>`表示的参数必须要有，`[]`表示的参数为可选。

-   ***`set`*** 可以设置三个类型的变量值：正常变量，`cache variable`、环境变量。
    
    -   `Normal Variable`:*`set(<variable> <value>... [PARENT_SCOPE])`*
    -   `cache`：`set(<variable> <value>... CACHE <type> <docstring> [FORCE])`
    -   `env`：`set(ENV{<variable>} [<value>])`
-   ***`OPTION`***：提供用户可以选择的选项
    
    -   格式：`option(<variable> "description" [initial value])`
    -   比如：
        
        ```cmake
            option(
                USE_MYPATH
                "user path"
                ON
            )
        ```
        
-   ***`aux_source_directory`***
    
    -   语法：`aux_source_directory(<dir> <variable>)`
    -   查找目录`dir`下的所有源文件(即.c, .cpp, .cc等文件)，并将名称保存到 `variable` 变量
-   ***`add_subdirectory`***
    
    -   `add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])`
    -   添加一个将被编译的子目录。指明`CMakeLists.txt`所在目录下包含了一个子目录`source_dir`。这样`source_dir`下的源文件和`CMakeLists.txt`等也会被处理。
-   ***`target_link_libraries`***
    
    -   `target_link_libraries(exec libs)`
    -   表示可执行程序`exec`需要链接到一个名为`libs`的链接库。
-   ***`add_library`***
    
    -   `add_library (name dir)`
    -   用在目录`dir`下的源文件生成一个名为`name`的静态链接库：`libname.a`
-   ***`configure_file`***
    
    -   加入一个配置头文件，用于处理 CMake 对源码的设置
        
        ```cmake
            configure_file (
                "${PROJECT_SOURCE_DIR}/config.h.in" # config.h.in文件目录
                "${PROJECT_BINARY_DIR}/config.h"    # config.h 生成的头文件目录
            )
        ```
        
        在配置文件`config.h`中，配置相关项，比如`options`中的`USE_MYPATH`：
        
        ```cmake
            #cmakedefine USE_MYMATH
        ```
        
-   ***`include`***
    
    -   `include(file [optional])`：读取`CMake`的相关文件。
    -   `include(moudle [optional])`  
        the file with name .cmake is searched in the `CMAKE_MODULE_PATH`。
-   ***`include_directories`***
    
    ```cmake
        include_directories([AFTER|BEFORE] [SYSTEM] dir1 [dir2 ...])
    ```
    
    添加指定目录到编译器搜索路径。
    
-   ***`install`***  
    使用：`cmake`之后，`sudo make install`就可以执行相应的库和头文件的安装。
    
    -   `TARGET`格式
        
        ```cmake
        install(TARGETS targets...
                [[ARCHIVE|LIBRARY|RUNTIME]
                [DESTINATION <dir>]
                [PERMISSIONS permissions...]
                [CONFIGURATIONS [Debug|Release|...]]
                [COMPONENT <component>]  
                [OPTIONAL]
                ] [...])
        ```
        
    -   `targets`的类型  
        可以安装的库有`[ARCHIVE|LIBRARY|RUNTIME]`三种：  
          1) 可执行程序视为`runtime`  
          2) 静态库视为`archieve`  
          3) `Module Library`视为`library`  
          4) 共享库和平台有关
    -   参数
        -   `DESTINATION`：  
            指定一个文件将要被安装的目录。如果给的是一个全路径，那么就直接使用；如果是相对路径，默认是相对`CMAKE_INSTALL_PREFIX`,其值默认是`/usr/local/`。  
              1) 头文件:`inclide`  
              2) 可执行文件:`bin`  
              3) 库:`lib`
            
        -   `PERMISSIONS`： 指定安装文件的权限：  
              1) user : `OWNER_READ, OWNER_WRITE, OWNER_EXECUTE`  
              2) group：`GROUP_READ, GROUP_WRITE, GROUP_EXECUTE`  
              3) other：`WORLD_READ, WORLD_WRITE, WORLD_EXECUTE`  
              4) uid ：` SETUID, and SETGID`。
            
        -   `CONFIGURATIONS`：为安装规则建立一个配置文件列表。
            
-   ***`install`***
    
    -   `FILES`格式
        
        ```cmake
        INSTALL(FILES files... 
                DESTINATION <dir>
                [PERMISSIONS permissions...]
                [CONFIGURATIONS [Debug|Release|...]]
                [COMPONENT <component>]
                [RENAME <name>] [OPTIONAL])
        ```
        
        -   `files`：即文件名
-   测试
    
    -   ***`enanle_testing()`***：启动测试
    -   ***`add_test(testname Exename arg1 arg2 ...)`***：
        -   需要先运行测试程序`enanle_testing()`，这个指令才有效。
        -   `Exename`是可执行程序名，参数`arg1, arg2`。
    -   ***`set_tests_properties(...)`***
        -   括号内格式：`(Exename [Exename2...] PROPERTIES prop1 value1 prop2 value2)`，其中`PROPERTIES`是固定的单词不能改
        -   为`Exename`设置属性，如果没有这个属性，就报错，有如下属性：  
              1) `WILL_FAIL`：如果设置为`true`，那么会反转测试结果的`pass/fail`标志。  
              2) `PASS_REGULAR_EXPRESSION`： 匹配正则表达式，只少有一个匹配，则`pass`   2) `FAIL_REGULAR_EXPRESSION`： 匹配正则表达式，则`fail`
    -   宏测试
        
        ```
            macro(<name> [arg1 [arg2 [arg3 ...]]])
                COMMAND1(ARGS ...)
                COMMAND2(ARGS ...)
                ...
            endmacro(<name>)
        
        ```
        
        就类似于写一个函数，用宏实现，调用：`name(arg1,arg2,...)`。
-   设置项目的版本号
    
    -   在顶层的`CMakeLists.txt`中：
        
        ```cmake
            # 加入版本号是 1.0
            set (Project_VERSION_MAJOR 1) # 主版本号
            set (Project_VERSION_MINOR 0) # 副版本号
        ```
        
    -   在配置文件`config.h.in`中设置：
        
        ```cmake
            #define Project_VERSION_MAJOR @Project_VERSION_MAJOR@
            #define Project_VERSION_MINOR @Project_VERSION_MINOR@
        ```
        
    -   `main`函数中就可以直接使用这两个宏，代表版本号：
        
        ```c
            printf("Version %d.%d\n",
                    Project_VERSION_MAJOR,
                    Project_VERSION_MINOR);
        ```
        
-   生成安装包  
    需要利用`CPack`工具，也是`CMake`提供的工具。
    
    -   先在顶层`CMakeLists.txt`中末尾添加：
        
        ```cmake
            # 构建一个 CPack 安装包
            include(InstallRequiredSystemLibraries)
            set (CPACK_RESOURCE_FILE_LICENSE
                "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
            set (CPACK_PACKAGE_VERSION_MAJOR "${Project_VERSION_MAJOR}")
            set (CPACK_PACKAGE_VERSION_MINOR "${Project_VERSION_MINOR}")
            include (CPack)
        ```
        
        -   导入`InstallRequiredSystemLibraries`模块，以便之后导入`CPack`模块
        -   设置一些`CPack`相关变量，包括版权信息和版本信息，其中版本信息用了上一节定义的版本号
        -   导入`CPack`模块
    -   生成二进制安装包：`cpack -C CPackConfig.cmake`
    -   or 生成源码安装包
        -   格式：`cpack -C CPackSourceConfig.cmake`  
            在执行该命令的目录下得到：
            
            ```shell
                # Demo8是项目名
                $ ls -l | grep Demo8
                -rwxrwxrwx 1 szz szz  8631 Dec 12 22:03 Demo8-1.0.1-Linux.sh
                -rw-rw-r-- 1 szz szz  3709 Dec 12 22:03 Demo8-1.0.1-Linux.tar.gz
                -rw-rw-r-- 1 szz szz  4982 Dec 12 22:03 Demo8-1.0.1-Linux.tar.Z
            ```
            
        -   安装：`sh Demo8-1.0.1-Linux.sh`。  
            默认的安装路径：
            
            ```c
                By default the Demo8 will be installed in:
                "~/Study/SystemProgram/CMakeExe/Demo8/build/Demo8-1.0.1-Linux"
                
                Do you want to include the subdirectory Demo8-1.0.1-Linux?
                Saying no will install in: "~/Study/SystemProgram/CMakeExe/Demo8/build" [Yn]: 
            ```
            
        -   运行。安装后，就运行该程序
            
            ```shell
                $ ./Demo8-1.0.1-Linux/bin/Demo 2 5
                Now we use our own Math library. 
                2 ^ 5 is 32
            ```
            
        -   Demo8-1.0.1-Linux下的目录结果
            
            ```shell
                Demo8-1.0.1-Linux
                ├── bin
                │   └── Demo        # 可执行程序
                ├── include         # 头文件
                │   ├── config.h
                │   └── MathFunctions.h
                └── lib             # 静态库
                    └── libMathFunctions.a
            ```
            
-   *`target_compile_definitions`*
    
    -   格式
        
        ```cmake
            target_compile_definitions(<target>
                                      <INTERFACE|PUBLIC|PRIVATE> [items1...]
                                      [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
        ```
        
    -   作用：编译时定义的宏
-   *`string`*
    
    -   `REPLACE`
        
        ```cmake
            string(REPLACE 
                  <match_string> <replace_string> 
                  <output_variable> <input> [<input>...])
        ```
        
        将所有`input`中出现的`match_String`替换为`replace_string`，并且将结果存在`output_variable`。
-   *`message`*
    
    ```cmake
        message([<mode>] "message to display" ...)
    ```
    
    -   显示信息给用户  
        `mode`取决于信息的类型：
        -   `STATUS`：以简洁的方式显示用户感兴趣的信息。
            
            ```cmake
                message(STATUS 
                        "CXX_FLAGS = " 
                        ${CMAKE_CXX_FLAGS} 
                        " " 
                        ${CMAKE_CXX_FLAGS_${BUILD_TYPE}}
                        )
            ```
            
            可以理解为`printf`，把后面的几个信息以空格相间，然后打印出来。显示结果为(和上面对应分成三段):
            
            ```cmake
                CXX_FLAGS = 
                
                -g -D_FILE_OFFSET_BITS=64 -Wall -Wextra 
                -Werror -Wconversion -Wno-unused-parameter 
                -Wold-style-cast -Woverloaded-virtual 
                -Wpointer-arith -Wshadow -Wwrite-strings 
                -march=native -rdynamic 
                
                -O0
            ```
            
-   *`find_package`*
    
    ```cmake
        find_package(<PackageName> 
                    [version] [EXACT] [QUIET] [MODULE]
                    [REQUIRED] [[COMPONENTS] [components...]]
                    [OPTIONAL_COMPONENTS components...]
                    [NO_POLICY_SCOPE])
    ```
    
    主要是寻找和加载外部项目。如果`PackageName`找到了，`PackageName-found`会显出，当没有找到时，默认显示 `PackageName-not found`。通过模式的选择，可以处理在没有找到包时的解决方案。
    
    -   `QUIET`：不显示有用信息，
    -   `REQUIRED`：报错
-   *`find_path`*
    
    ```cmake
        find_path (<VAR> name0|NAMES name1 [path1 path2 ...])
    ```
    
    用以寻找包含着`name1`文件的目录，如果找到了结果存储在`VAR`，没有找到结果结果是`VAR-not found`。成功时，变量被清除`find_path`再次搜索，没有成功,`fin_path`再次以相同的变量被调用时搜索。
    
-   *`find_library`*  
    同上`find_path`
    
    ```cmake
        find_library (<VAR> name0|NAMES name1 [path1 path2 ...])
    ```
    
    -   OPTIONS
        -   `NAMES`  
            为`library`指定一个或多个可能的名字。

***

-   参考
    -   [CMake官方文档](https://cmake.org/cmake/help/cmake2.4docs.html)
    -   [CMake API搜索](https://cmake.org/cmake/help/latest/search.html?q=)
    -   [CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)























# 3. ccmake

ccmake is curses (terminal handling library) interface to CMake.

cmake is the CLI (Command Line Interface)

https://blog.csdn.net/arackethis/article/details/42155589








```
ccmake

```

## 3.1. 将其他平台的项目迁移到 CMake


https://www.hahack.com/codes/cmake/



CMake 可以很轻松地构建出在适合各个平台执行的工程环境。而如果当前的工程环境不是 CMake ，而是基于某个特定的平台，是否可以迁移到 CMake 呢？答案是可能的。下面针对几个常用的平台，列出了它们对应的迁移方案。

### 3.1.1. autotools

-   [am2cmake](https://projects.kde.org/projects/kde/kdesdk/kde-dev-scripts/repository/revisions/master/changes/cmake-utils/scripts/am2cmake) 可以将 autotools 系的项目转换到 CMake，这个工具的一个成功案例是 KDE 。
-   [Alternative Automake2CMake](http://emanuelgreisen.dk/stuff/kdevelop_am2cmake.php.tgz) 可以转换使用 automake 的 KDevelop 工程项目。
-   [Converting autoconf tests](http://www.cmake.org/Wiki/GccXmlAutoConfHints)

### 3.1.2. qmake

-   [qmake converter](http://www.cmake.org/Wiki/CMake:ConvertFromQmake) 可以转换使用 QT 的 qmake 的工程。

### 3.1.3. Visual Studio

-   [vcproj2cmake.rb](http://vcproj2cmake.sf.net/) 可以根据 Visual Studio 的工程文件（后缀名是 `.vcproj` 或 `.vcxproj`）生成 CMakeLists.txt 文件。
-   [vcproj2cmake.ps1](http://nberserk.blogspot.com/2010/11/converting-vc-projectsvcproj-to.html) vcproj2cmake 的 PowerShell 版本。
-   [folders4cmake](http://sourceforge.net/projects/folders4cmake/) 根据 Visual Studio 项目文件生成相应的 “source_group” 信息，这些信息可以很方便的在 CMake 脚本中使用。支持 Visual Studio 9/10 工程文件。

### 3.1.4. CMakeLists.txt 自动推导

-   [gencmake](http://websvn.kde.org/trunk/KDE/kdesdk/cmake/scripts/) 根据现有文件推导 CMakeLists.txt 文件。
-   [CMakeListGenerator](http://www.vanvelzensoftware.com/postnuke/index.php?name=Downloads&req=viewdownload&cid=7) 应用一套文件和目录分析创建出完整的 CMakeLists.txt 文件。仅支持 Win32 平台。

## 3.2. 相关链接

1.  [官方主页](http://www.cmake.org/)
2.  [官方文档](http://www.cmake.org/cmake/help/cmake2.4docs.html)
3.  [官方教程](http://www.cmake.org/cmake/help/cmake_tutorial.html)
4.  [Wiki](http://www.cmake.org/Wiki/CMake#Basic_CMakeLists.txt_from-scratch-generator)
5.  [FAQ](http://www.cmake.org/Wiki/CMake_FAQ)
6.  [bug tracker](http://www.cmake.org/Bug)
7.  邮件列表：
    -   [cmake on Gmane](http://dir.gmane.org/gmane.comp.programming.tools.cmake.user)
    -   [http://www.mail-archive.com/cmake@cmake.org/](http://www.mail-archive.com/cmake@cmake.org/)
    -   [http://marc.info/?l=cmake](http://www.mail-archive.com/cmake@cmake.org/)
8.  其他推荐文章
    -   [在 linux 下使用 CMake 构建应用程序](http://www.ibm.com/developerworks/cn/linux/l-cn-cmake/)
    -   [cmake的一些小经验](http://www.cppblog.com/skyscribe/archive/2009/12/14/103208.aspx)
    -   [Packaging Software with CPack](http://www.kitware.com/media/archive/kitware_quarterly0107.pdf)
    -   [视频教程: 《Getting Started with CMake》](http://www.youtube.com/watch?v=CLvZTyji_Uw)

## 3.3. 类似工具

-   [SCons](http://scons.org/)：Eric S. Raymond、Timothee Besset、Zed A. Shaw 等大神力荐的项目架构工具。和 CMake 的最大区别是使用 Python 作为执行脚本。

***

1.  [这个页面](http://www.cmake.org/Wiki/CMake_Projects)详细罗列了使用 CMake 的知名项目

