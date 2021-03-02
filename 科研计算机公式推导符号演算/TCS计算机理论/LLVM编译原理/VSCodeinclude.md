# include

https://www.cnblogs.com/qinghemo/p/11710705.html



具体本地inclue目录看本地文件测试样例/hello

**下面是比较关键的四组代码**

**记得把路径根据自己的具体情况修改**

launch.josn代码：

```

// https://github.com/Microsoft/vscode-cpptools/blob/master/launch.md
{ "version": "0.2.0", "configurations": \[
        { "name": "(gdb) Launch", // 配置名称，将会在启动配置的下拉菜单中显示
            "type": "cppdbg", // 配置类型，这里只能为cppdbg
            "request": "launch", // 请求配置类型，可以为launch（启动）或attach（附加）
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe", // 将要进行调试的程序的路径
            "args": \[\], // 程序调试时传递给程序的命令行参数，一般设为空即可
            "stopAtEntry": true, // 设为true时程序将暂停在程序入口处，我一般设置为true
            "cwd": "${workspaceFolder}", // 调试程序时的工作目录
            "environment": \[\], // （环境变量？）
            "externalConsole": true, // 调试时是否显示控制台窗口，一般设置为true显示控制台
            "internalConsoleOptions": "neverOpen", // 如果不设为neverOpen，调试时会跳到“调试控制台”选项卡，你应该不需要对gdb手动输命令吧？
            "MIMode": "gdb", // 指定连接的调试器，可以为gdb或lldb。但目前lldb在windows下没有预编译好的版本。
            "miDebuggerPath": "gdb.exe", // 调试器路径。
            "setupCommands": \[
                { "description": "Enable pretty-printing for gdb", "text": "-enable-pretty-printing", "ignoreFailures": false }
            \], "preLaunchTask": "Compile" // 调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
 }
    \]
}

```

tasks.josn代码：


```
// https://code.visualstudio.com/docs/editor/tasks
{ "version": "2.0.0", "tasks": \[
        { "label": "Compile", // 任务名称，与launch.json的preLaunchTask相对应
            "command": "clang++", // 要使用的编译器
            "args": \[ "${file}", "-o", // 指定输出文件名，不加该参数则默认输出a.exe
                "${fileDirname}/${fileBasenameNoExtension}.exe", "-g", // 生成和调试有关的信息
                "-Wall", // 开启额外警告
                "-static-libgcc", // 静态链接
                "-fcolor-diagnostics", "--target=x86_64-w64-mingw", // 默认target为msvc，不加这一条就会找不到头文件
                "-std=c++17" // C语言最新标准为c11，或根据自己的需要进行修改
            \], // 编译命令参数
            "type": "shell", "group": { "kind": "build", "isDefault": true // 设为false可做到一个tasks.json配置多个编译指令，需要自己修改本文件，我这里不多提
 }, "presentation": { "echo": true, "reveal": "always", // 在“终端”中显示编译信息的策略，可以为always，silent，never。具体参见VSC的文档
                "focus": false, // 设为true后可以使执行task时焦点聚集在终端，但对编译c和c++来说，设为true没有意义
                "panel": "shared" // 不同的文件的编译信息共享一个终端面板
 } // "problemMatcher":"$gcc" // 如果你不使用clang，去掉前面的注释符，并在上一条之后加个逗号。照着我的教程做的不需要改（也可以把这行删去)
 }
    \]
}

```

settings.json代码：

```

{ "files.defaultLanguage": "cpp", // ctrl+N新建文件后默认的语言
    "editor.formatOnType": true, // 输入时就进行格式化，默认触发字符较少，分号可以触发
    "editor.snippetSuggestions": "top", // snippets代码优先显示补全

   "code-runner.runInTerminal": true, // 设置成false会在“输出”中输出，无法输入
    "code-runner.executorMap": { "c": "cd $dir && clang $fileName -o $fileNameWithoutExt.exe -Wall -g -Og -static-libgcc -fcolor-diagnostics --target=x86_64-w64-mingw -std=c11 && $dir$fileNameWithoutExt", "cpp": "cd $dir && clang++ $fileName -o $fileNameWithoutExt.exe -Wall -g -Og -static-libgcc -fcolor-diagnostics --target=x86_64-w64-mingw -std=c++17 && $dir$fileNameWithoutExt" }, // 设置code runner的命令行
    "code-runner.saveFileBeforeRun": true, // run code前保存
    "code-runner.preserveFocus": true, // 若为false，run code后光标会聚焦到终端上。如果需要频繁输入数据可设为false
    "code-runner.clearPreviousOutput": false, // 每次run code前清空属于code runner的终端消息

   "C\_Cpp.clang\_format_sortIncludes": true, // 格式化时调整include的顺序（按字母排序）
    "C_Cpp.intelliSenseEngine": "Default", // 可以为Default或Tag Parser，后者较老，功能较简单。具体差别参考cpptools扩展文档
    "C_Cpp.errorSquiggles": "Disabled", // 因为有clang的lint，所以关掉
    "C_Cpp.autocomplete": "Disabled", // 因为有clang的补全，所以关掉

   "clang.cflags": \[ // 控制c语言静态检测的参数
        "--target=x86_64-w64-mingw", "-std=c11", "-Wall" \], "clang.cxxflags": \[ // 控制c++静态检测时的参数
        "--target=x86_64-w64-mingw", "-std=c++17", "-Wall" \], "clang.completion.enable": true, "files.associations": { "iostream": "cpp", "ostream": "cpp", "string_view": "cpp", "*.tcc": "cpp", "string": "cpp", "cmath": "cpp" } // 效果效果比cpptools要好
}

```


c\_cpp\_properties.json代码：

```

{
    "configurations": [
        {
            "name": "MinGW",
            "intelliSenseMode": "clang-x64",
            "compilerPath": "C:/Program Files/LLVM/bin/gcc.exe",
            "includePath": [
                "${workspaceFolder}"
            ],
            "defines": [],
            "browse": {
                "path": [
                    "${workspaceFolder}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            },
            "cStandard": "c11",
            "cppStandard": "c++17"
        }
    ],
    "version": 4
}


```

























