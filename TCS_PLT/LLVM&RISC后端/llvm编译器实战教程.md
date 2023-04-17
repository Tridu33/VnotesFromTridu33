# llvm编译器实战教程



好多书

https://www.packtpub.com


getting-started-llvm-core-libraries

https://www.packtpub.com/application-development/getting-started-llvm-core-libraries


机械工业出版社华章公司

www.hzbook.com/index.php/Index/index.html



源码下载

www.hzcourse.com/web/teachRes/detail/4635/231






如何利用LLVM写一个编译器？ - 求是老伯的回答 - 知乎 https://www.zhihu.com/question/30479779/answer/48352221




```-###```查看驱动程序为了完成你的命令过程中，调用到的其他工具，比如：

```
PS C:\Users\admin\Documents\Tridu33\！wasm-js-node\LLVm编程实战notes> clang -### hello.c -o hello
clang version 10.0.0 
Target: x86_64-pc-windows-msvc
Thread model: posix
InstalledDir: C:\Program Files\LLVM\bin
 "C:\\Program Files\\LLVM\\bin\\clang.exe" "-cc1" "-triple" "x86_64-pc-windows-msvc19.25.28614" "-emit-obj" "-mrelax-all" "-mincremental-linker-compatible" "-disable-free" "-disable-llvm-verifier" "-discard-value-names" "-main-file-name" "hello.c" "-mrelocation-model" "pic" "-pic-level" "2" "-mthread-model" "posix" "-mframe-pointer=none" "-fmath-errno" "-fno-rounding-math" "-masm-verbose" "-mconstructor-aliases" "-munwind-tables" "-target-cpu" "x86-64" "-dwarf-column-info" "-resource-dir" "C:\\Program Files\\LLVM\\lib\\clang\\10.0.0" "-internal-isystem" "C:\\Program Files\\LLVM\\lib\\clang\\10.0.0\\include" "-internal-isystem" "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.25.28610\\include" "-internal-isystem" "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.25.28610\\atlmfc\\include" "-internal-isystem" "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.18362.0\\ucrt" "-internal-isystem" "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\shared" "-internal-isystem" "C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\um" "-internal-isystem" "C:\\Program Files (x86)\\Windows 
Kits\\10\\include\\10.0.18362.0\\winrt" "-fdebug-compilation-dir" "C:\\Users\\admin\\Documents\\Tridu33\\锛wasm-js-node\\LLVm佺紪绋嬪疄鎴notes" "-ferror-limit" "19" "-fmessage-length" "121" "-fno-use-cxa-atexit" "-fms-extensions" "-fms-compatibility" "-fms-compatibility-version=19.25.28614" "-fdelayed-template-parsing" "-fobjc-runtime=gcc" "-fdiagnostics-show-option" "-fcolor-diagnostics" "-faddrsig" "-o" "C:\\Users\\admin\\AppData\\Local\\Temp\\hello-6197ce.o" "-x" "c" "hello.c"
 "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.25.28610\\bin\\Hostx64\\x64\\link.exe" "-out:hello" "-defaultlib:libcmt" "-libpath:C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.25.28610\\lib\\x64" "-libpath:C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.25.28610\\atlmfc\\lib\\x64" "-libpath:C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.18362.0\\ucrt\\x64" "-libpath:C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.18362.0\\um\\x64" "-nologo" "C:\\Users\\admin\\AppData\\Local\\Temp\\hello-6197ce.o"
```


























