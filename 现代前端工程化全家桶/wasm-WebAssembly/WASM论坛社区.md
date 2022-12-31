# 1. WASM
https://www.w3ctech.com/category/18 
论坛


https://emscripten.org/docs/getting_started/downloads.html
下载并安装

Rust+wasm教程
https://developer.mozilla.org/zh-CN/docs/WebAssembly/Rust_to_wasm

C +wasm教程

https://segmentfault.com/a/1190000011328496


https://blog.csdn.net/sinat_32582203/article/details/73355211


```

(base) C:\Users\admin>cd C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk

(base) C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk>emsdk install latest
Fetching emscripten-releases repository...
Cloning into 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/releases'...
fatal: unable to access 'https://chromium.googlesource.com/emscripten-releases/': Failed to connect to chromium.googlesource.com port 443: Timed out
['C:\\Program Files\\Git\\cmd\\git.exe', 'clone', 'https://chromium.googlesource.com/emscripten-releases', 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/releases'] failed with error code 128!
Fetching all precompiled tagged releases..
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/llvm-tags-32bit.txt from https://s3.amazonaws.com/mozilla-games/emscripten/packages/llvm/tag/win_32bit/index.txt
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/llvm-tags-64bit.txt from https://s3.amazonaws.com/mozilla-games/emscripten/packages/llvm/tag/win_64bit/index.txt, 2435 Bytes
Installing SDK 'sdk-releases-fastcomp-05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-64bit'..
Installing tool 'releases-fastcomp-05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-64bit'..
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-wasm-binaries.zip from https://storage.googleapis.com/webassembly/emscripten-releases-builds/win/05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9/wasm-binaries.zip, 476769129 Bytes
Unpacking 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-wasm-binaries.zip' to 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/fastcomp'
Done installing tool 'releases-fastcomp-05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-64bit'.
Installing tool 'node-8.9.1-64bit'..
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/node-v8.9.1-win-x64.zip from https://storage.googleapis.com/webassembly/emscripten-releases-builds/deps/node-v8.9.1-win-x64.zip, 16940179 Bytes
Unpacking 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/node-v8.9.1-win-x64.zip' to 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/node/8.9.1_64bit'
Done installing tool 'node-8.9.1-64bit'.
Installing tool 'python-2.7.13.1-64bit'..
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/WinPython-64bit-2.7.13.1Zero.zip from https://storage.googleapis.com/webassembly/emscripten-releases-builds/deps/WinPython-64bit-2.7.13.1Zero.zip, 41285159 Bytes
Unpacking 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/WinPython-64bit-2.7.13.1Zero.zip' to 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/python/2.7.13.1_64bit'
Done installing tool 'python-2.7.13.1-64bit'.
Installing tool 'java-8.152-64bit'..
Downloading: C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/portable_jre_8_update_152_64bit.zip from https://storage.googleapis.com/webassembly/emscripten-releases-builds/deps/portable_jre_8_update_152_64bit.zip, 69241499 Bytes
Unpacking 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/zips/portable_jre_8_update_152_64bit.zip' to 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/java/8.152_64bit'
Done installing tool 'java-8.152-64bit'.
Done installing SDK 'sdk-releases-fastcomp-05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-64bit'.

(base) C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk>emsdk activate latest
Writing .emscripten configuration file to user home directory C:\Users\admin/
The Emscripten configuration file C:\Users\admin\.emscripten has been rewritten with the following contents:

import os
LLVM_ROOT = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/fastcomp/fastcomp/bin'
BINARYEN_ROOT = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/fastcomp'
EMSCRIPTEN_ROOT = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/fastcomp/emscripten'
EMSCRIPTEN_NATIVE_OPTIMIZER = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/fastcomp/bin/optimizer.exe'
NODE_JS = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/node/8.9.1_64bit/bin/node.exe'
PYTHON = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/python/2.7.13.1_64bit/python-2.7.13.amd64/python.exe'
JAVA = 'C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk/java/8.152_64bit/bin/java.exe'
SPIDERMONKEY_ENGINE = ''
V8_ENGINE = ''
TEMP_DIR = 'c:/users/admin/appdata/local/temp'
COMPILER_ENGINE = NODE_JS
JS_ENGINES = [NODE_JS]

Adding directories to PATH:
PATH += C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk
PATH += C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\fastcomp\emscripten
PATH += C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\node\8.9.1_64bit\bin
PATH += C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\python\2.7.13.1_64bit\python-2.7.13.amd64
PATH += C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\java\8.152_64bit\bin

Setting environment variables:
EMSDK = C:/Users/admin/Downloads/arch/EmscriptenSDK/emsdk
EM_CONFIG = C:\Users\admin\.emscripten
EMSDK_NODE = C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\node\8.9.1_64bit\bin\node.exe
EMSDK_PYTHON = C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\python\2.7.13.1_64bit\python-2.7.13.amd64\python.exe
JAVA_HOME = C:\Users\admin\Downloads\arch\EmscriptenSDK\emsdk\java\8.152_64bit


Set the following tools as active:
   releases-fastcomp-05f8c01394ddd0838d3cb484ba8ca97a3efc1ac9-64bit
   node-8.9.1-64bit
   python-2.7.13.1-64bit
   java-8.152-64bit

The changes made to environment variables only apply to the currently running shell instance. Use the 'emsdk_env.bat' to re-enter this environment later, or if you'd like to permanently register this environment globally to all users in Windows Registry, rerun this command with the option --global.

```































































































