[TOC]

# VscodeCmake
vscode c/c++ 相关文档：https://code.visualstudio.com/docs/languages/cpp  
cmake-tools 文档：https://vector-of-bool.github.io/docs/vscode-cmake-tools/index.html  
clang-format 文档：https://clang.llvm.org/docs/ClangFormatStyleOptions.html




# vscode task setting launch



3.VSC不支持单文件编译，需要创建一个目录，在这个目录下进行编译，例如TEST，写一个简单的main.cpp文件保存在这各目录下；
4.使用【Ctrl+Shift+p】，输入C/Cpp:Edit Configurations生成配置文件 c_cpp_properties.json


.使用【Ctrl+Shift+p】，输入Tasks: Configure task生成配置文件 tasks.json

6.使用【Ctrl+Shift+p】，输入Open launch.json生成配置文件launch.json


[VScode tasks.json和launch.json的设置https://zhuanlan.zhihu.com/p/92175757](https://zhuanlan.zhihu.com/p/92175757)

## 预定义变量[#](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/editor/variables-reference%23_predefined-variables)

支持下面的预定义变量:

-   **${workspaceFolder}** \- 当前工作目录(根目录)
-   **${workspaceFolderBasename}** \- 当前文件的父目录
-   **${file}** \- 当前打开的文件名(完整路径)
-   **${relativeFile}** \- 当前根目录到当前打开文件的相对路径(包括文件名)
-   **${relativeFileDirname}** \- 当前根目录到当前打开文件的相对路径(不包括文件名)
-   **${fileBasename}** \- 当前打开的文件名(包括扩展名)
-   **${fileBasenameNoExtension}** \- 当前打开的文件名(不包括扩展名)
-   **${fileDirname}** \- 当前打开文件的目录
-   **${fileExtname}** \- 当前打开文件的扩展名
-   **${cwd}** \- 启动时task工作的目录
-   **${lineNumber}** \- 当前激活文件所选行
-   **${selectedText}** \- 当前激活文件中所选择的文本
-   **${execPath}** \- vscode执行文件所在的目录
-   **${defaultBuildTask}** \- 默认编译任务(build task)的名字

## 预定义变量示例:

假设你满足以下的条件

1.  一个文件 `/home/your-username/your-project/folder/file.ext` 在你的编辑器中打开;
2.  一个目录 `/home/your-username/your-project` 作为你的根目录.

下面的预定义变量则代表:

-   **${workspaceFolder}** - `/home/your-username/your-project`
-   **${workspaceFolderBasename}** - `your-project`
-   **${file}** - `/home/your-username/your-project/folder/file.ext`
-   **${relativeFile}** - `folder/file.ext`
-   **${relativeFileDirname}** - `folder`
-   **${fileBasename}** - `file.ext`
-   **${fileBasenameNoExtension}** - `file`
-   **${fileDirname}** - `/home/your-username/your-project/folder`
-   **${fileExtname}** - `.ext`
-   **${lineNumber}** \- 光标所在行
-   **${selectedText}** \- 编辑器中所选择的文本
-   **${execPath}** \- Code.exe的位置












7.默认生成的.vscode就是用来管理你的项目的设置，可以直接使用F5进行调试，或者点击调试按钮选择在不调试的情况下启动（直接编译运行），编译调试的时候需要切换到自己的main.cpp文件；
8.生成的.exe文件也可以像linux中一样使用./main.exe进行运行。

作者：Zbertj
链接：https://www.jianshu.com/p/6369cbd14528
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


```
mkdir build
cd build
cmake -G "Unix Makefiles" ../
```

have:

```

Generators
* Visual Studio 16 2019        = Generates Visual Studio 2019 project files.
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
  NMake Makefiles              = Generates NMake makefiles.
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



















































































