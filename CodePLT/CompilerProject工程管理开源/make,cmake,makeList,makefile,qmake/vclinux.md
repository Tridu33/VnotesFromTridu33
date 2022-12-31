
https://docs.microsoft.com/zh-cn/cpp/build/how-to-create-a-cpp-project-from-existing-code?view=msvc-160
# 1. vclinux



vclinux是微软官方提供的shell脚本，可根据makefile生成vs的工程文件。

下载地址：https://github.com/robotdad/vclinux

下载完成后放到linux上进行解压，找到bash目录中的两个脚本文件，并执行这两个脚本，命令格式如下：


```
./genvcxproj.sh 工程目录 xxx.vcxproj
 
./genfilters.sh 工程目录 xxx.vcxproj.filters
```



