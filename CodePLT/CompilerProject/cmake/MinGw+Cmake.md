# MinGw+Cmake
    CMake的所有的语句都写在一个叫:CMakeLists.txt的文件中。当CMakeLists.txt文件确定后,可以用ccmake命令对相关 的变量值进行配置。这个命令必须指向CMakeLists.txt所在的目录。配置完成之后,应用cmake命令生成相应的makefile（在Unix like系统下）或者 project文件（指定用window下的相应编程工具编译时）。

    其基本操作流程为：

$> ccmake directory
$> cmake directory
$> make

其中directory为CMakeList.txt所在目录；
第一条语句用于配置编译选项，如VTK_DIR目录 ，一般这一步不需要配置，直接执行第二条语句即可，但当出现错误时，这里就需要认为配置了，这一步才真正派上用场；
第二条命令用于根据CMakeLists.txt生成Makefile文件；
第三条命令用于执行Makefile文件，编译程序，生成可执行文件；
CMake的执行就是这么简单，其难点在于如何编写CMakeLists.txt文件，



https://blog.csdn.net/u012150179/article/details/17852273


第2行指定生成的工程名为test_math

第4行指定头文件目录为include

第8行指定源文件目录为src，并将其赋值给环境变量DIR_SRCS

第10行设定环境变量TEST_MATH的值为环境变量DIR_SRCS的值，此处用于显示如何用环境变量对环境变量进行赋值

第14行将数学函数库赋值给环境变量LIBRARIES，当然，可以不用这个环境变量，而在后面直接使用该库名

第18行用于指定生成文件，将环境变量TEST_MATH目录下的所有文件编译生成../bin目录下的可执行文件bin

第20行指定../bin/bin执行时的链接库为环境变量LIBRARIES的值－libm.so


```cmake
#project name
第二行PROJECT(test_math)
#head file path
INCLUDE_DIRECTORIES(
include
)
#source directory
AUX_SOURCE_DIRECTORY(src DIR_SRCS)
#set environment variable
SET(TEST_MATH
${DIR_SRCS}
)
#set extern libraries
SET(LIBRARIES
libm.so
)
#add executable file
ADD_EXECUTABLE(../bin/bin ${TEST_MATH})
#add link library
TARGET_LINK_LIBRARIES(../bin/bin ${LIBRARIES})

```

https://blog.csdn.net/afei__/article/details/81201039











版本比较久，可能有问题


https://blog.csdn.net/isscollege/article/details/78038921

cmake [<options>] (<path-to-source> | <path-to-existing-build>)
cmake [(-D<var>=<value>)...] -P <cmake-script-file>
cmake --build <dir> [<options>] [-- <build-tool-options>...]
cmake -E <command> [<options>...]
cmake --find-package <options>...

生成编译工程文件
cmake <CMakeLists.txt_Path>就是生成可以编译工程文件。当时运行的目录在哪里，生成的可编译工程文件就在哪个目录。比如CMakeLists.txt文件在f:cmake目录，而当时在f:cmakebuild目录运行cmake ..，则生成的编译工程文件在f:cmakebuild目录。

也可以再生成编译工程文件的时候通过-D来添加变量值，比如CMakeLists.txt内容如下：

 
1
2
3
4
cmake_minimum_required (VERSION 2.6)
project (a)
message(${EXECUTABLE_OUTPUT_PATH})
add_executable(b b.cpp)
我们可以通过-D选择来设置EXECUTABLE_OUTPUT_PATH的值，也是编译的文件的输出目录：

 
1
cmake -D EXECUTABLE_OUTPUT_PATH="another_output" ..
这样，我们就给CMakeLists.txt编译脚本传递了新的EXECUTABLE_OUTPUT_PATH值。

编译工程
CMake除了生成编译工程文件，它也可以调用系统的编译工程来编译工程，如：

 
1
cmake --build .
默认是编译debug模式，也可以传递在–后面传递MSBUILD参数来控制：

 
1
cmake --build . -- /p:Configuration=Release
 

命令行工具模式
CMake有一个-E的命令行工具模式，提供了一些常用的功能，比复制文件、创建目录、读写注册表、读写环境变量、计算md5值等等。脚本可以调用这些功能。

编写CMakeLists.txt
创建可以执行程序工程
首先从创建一个最简单的可执行程序开始，CMakeLists.txt内容如下：

 
1
2
3
4
5
cmake_minimum_required (VERSION 2.6)
project (LearnCMake)
message(${LearnCMake_SOURCE_DIR})
message(${LearnCMake_BINARY_DIR})
add_executable(FirstExecutable hello_world.cpp)
第1行是cmake需要的最低版本，目前这个是VERSION 2.6，一般不用修改。

第2~4行表示我们创建了一个名为LearnCMake工程，对应生成一个LearnCMake.sln。project函数表示创建一个工程。同时，也生成了4个变量：

PROJECT_SOURCE_DIR, <PROJECT-NAME>_SOURCE_DIR。工程的源代码目录。
PROJECT_BINARY_DIR, <PROJECT-NAME>_BINARY_DIR。工程的二进制文件目录。
第5行表示添加一个名为FirstExecutable的可执行程序项目，它的源代码为hello_world.cpp。下面是add_executable的完整用法：

 
1
2
3
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
               [EXCLUDE_FROM_ALL]
               source1 [source2 ...])
默认的是创建控制台工程，加上WIN32表示创建的是win32工程，如下：

 
1
add_executable(FirstExecutable WIN32 hello_world.cpp)
后面是项目的代码，可以添加多个代码文件，用空格分开。

创建库工程
创建库工程跟创建可执行程序工程类似，创建库工程使用add_library函数，如下例子：

 
1
2
3
4
5
6
cmake_minimum_required (VERSION 3.0)
project (LearnCMake)
add_library(FirstLibrary first_library.cpp)
add_library(SecondLibrary second_library.cpp)
add_executable(FirstExecutable hello_world.cpp)
target_link_libraries(FirstExecutable FirstLibrary)
add_library的用法如下：

 
1
2
3
add_library(<name> [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            source1 [source2 ...])
默认的是静态库，也可以显式的设置库是否为静态库、动态库或者是模块。另外BUILD_SHARED_LIBS也可控制编译成哪种库。

target_link_libraries用来链接库，用法如下：

 
1
2
target_link_libraries(<target> [item1 [item2 [...]]]
                      [[debug|optimized|general] <item>] ...)
 

set设置变量
add_library、add_executable都可以添加多个源文件，如下：

 
1
2
3
4
cmake_minimum_required (VERSION 3.0)
project (LearnCMake)
add_executable(FirstExecutable main.cpp app_util.h app_util.cpp)
add_library(FirstLibrary app_util.h app_util.cpp)
我们可以通过定义一个AppUtilSrc变量来代替app_util.h app_util.cpp，如下：

 
1
2
3
4
5
cmake_minimum_required (VERSION 3.0)
project (LearnCMake)
set(AppUtilSrcs app_util.h app_util.cpp)
add_executable(FirstExecutable main.cpp ${AppUtilSrcs})
add_library(FirstLibrary ${AppUtilSrcs})
效果是跟上面等价的。还可以累积值：

 
1
2
set(AppUtilSrcs app_util.h app_util.cpp)
set(AppUtilSrcs ${AppUtilSrcs} b.cpp)
这样AppUtilSrcs就代表着3个文件了。

设置编译模式
设置mt编译模式：

 
1
2
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
设置md编译模式：

 
1
2
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MD")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")
默认是多字节模式，设置成unicode模式：

 
1
add_definitions(-D_UNICODE)
另外add_definitions还可以设置其他的选项。

添加其他CMakeLists.txt
一个CMakeLists.txt里面的target如果要链接其他CMakeLists.txt中的target，可以使用add_subdirectory，我们以使用googletest库为例：

 
1
2
3
4
5
6
7
8
add_subdirectory("../thirdparty/googletest/googletest/" gtest)
file(GLOB_RECURSE gtest_lib_head_files "../thirdparty/googletest/googletest/*.h")
source_group("gtest" FILES ${gtest_lib_head_files})
include_directories("../thirdparty/googletest/googletest/include")
aux_source_directory("./pbase_unittest/src" pbase_unittest_src_files)
file(GLOB_RECURSE pbase_unittest_include_files "./pbase_unittest/include/*.h")
add_executable(pbase_unittest ${pbase_unittest_src_files} ${pbase_unittest_include_files} ${gtest_lib_head_files})
target_link_libraries(pbase_unittest gtest)
 

代码控制
如果想把./pbase/src目录下的所有源文件加入到工程，可以用aux_source_directory把某个目录下的源文件加入到某个变量中，稍后就可以使用这个变量代表的代码了，如：

 
1
2
aux_source_directory("./pbase/src" pbase_lib_src_files)
add_library(pbase ${pbase_lib_src_files})
添加头文件包含目录是：

 
1
include_directories("../thirdparty/googletest/googletest/include")
但是include_directories中的文件不会体现先visual studio工程中，而aux_source_directory只会添加源文件，会忽略头文件，如果想生存的visual studio工程里面也包含头文件，可以这样：

 
1
2
3
# add head files
file(GLOB_RECURSE pbase_lib_head_files "./pbase/include/*.h")
add_library(pbase ${pbase_lib_head_files})
如果想生存visual studio中的filter，可以使用source_group：

 
1
2
file(GLOB_RECURSE gtest_lib_head_files "../thirdparty/googletest/googletest/*.h")
source_group("gtest" FILES ${gtest_lib_head_files})
最终添加头文件到工程里标准模板是：

 
1
2
3
4
file(GLOB_RECURSE gtest_lib_head_files "../thirdparty/googletest/googletest/*.h")
source_group("gtest" FILES ${gtest_lib_head_files})
include_directories("../thirdparty/googletest/googletest/include")
add_executable(pbase_unittest ${gtest_lib_head_files})
































































