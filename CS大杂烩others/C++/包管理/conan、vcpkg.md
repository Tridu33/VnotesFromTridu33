
# 1. vcpkg


**vcpkg**dependency manager

比如用来安装https://github.com/kkos/oniguruma

```
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.bat
./vcpkg integrate install
./vcpkg install oniguruma
```





如何看待 Windows 的 C++ 包管理器 vcpkg？ - 周杰的回答 - 知乎
https://www.zhihu.com/question/263416411/answer/268970544



https://blog.csdn.net/qq_41023270/article/details/109274433
为了之后方便与Visual Studio以及其他C/C++编译器链接，建议使用类似 C:\src 或者 C:\dev ，可以理解为在本地建立一个库的仓库，之后所有的安装都在该目录下，否则会由于路径的缘故会遇到某些端口构建系统的路径问题。

建议使用类似 C:\src 或者 C:\dev ，可以理解为在本地建立一个库的仓库，之后所有的安装都在该目录下，否则会由于路径的缘故会遇到某些端口构建系统的路径问题。

1、打开Git CMD命令行工具，使用 cd 到建立的目标路径（如：C:\src）；
2、输入命令：git clone https://github.com/Microsoft/vcpkg ，将开启vcpkg下载；
3、下载完成后，会自动建立一个vcpkg文件夹，就需要再次使用 cd 命令到vcpkg文件路径内；
4、运行 .\bootstrap-vcpkg.bat 等待运行完成。至此vcpkg安装完成。



集成到全局：vcpkg integrate install
移除全局：vcpkg integrate remove
集成到工程：vcpkg integrate project（在“\scripts\buildsystems”目录下，生成nuget配置文件）
查看库目录：vcpkg search
查看支持的架构：vcpkg help triplet
指定编译某种架构的程序库：vcpkg install xxxx:x64-windows（x86-windows）
卸载已安装库：vcpkg remove xxxx
指定卸载平台：vcpkg remove xxxx:x64-windows
移除所有旧版本库：vcpkg remove --outdated
查看已经安装的库：vcpkg list
更新已经安装的库：vcpkg update xxx
导出已经安装的库：vcpkg export xxxx --7zip（–7zip –raw –nuget –ifw –zip）











# 2. conan、

Conan 基于 Python 编写，故需要在开始前安装好 Python3。然后使用标准的 pip 安装即可。

http://chu-studio.com/posts/2019/%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E7%9A%84C++%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8CONAN%E4%B8%8A%E6%89%8B%E6%8C%87%E5%8D%97

Conan 会在第一次启动时自动配置好默认的 Profile 和 Remote 设置。它的配置以及本地的二进制仓库均存储在用户目录下~/.conan/中（Windows上，是%USERPROFILE%\.conan\）。

其中用户配置文件为conan.conf，通常情况下无需修改，但当需要设置代理时，可以对其进行编辑。


默认情况下 Conan 只把包装在用户目录下。用户目录的软件包仓库被称为本地缓存（Local Cache）；

那么同样的，服务器上也有一个软件包的仓库，文档中称为远端（Remote）。
conan-center: https://bintray.com/conan/conan-center
conan-transit（废弃）: https://bintray.com/conan/conan-transit
bincrafters（开源社区源） : https://bintray.com/bincrafters/public-conan
conan-community（类似测试源，不稳定） : https://bintray.com/conan-community/conan




Conan 提供了一个环境变量CONAN_USER_HOME来让用户指定一个 Conan 的工作目录，这样就能起到类似于 Python 的 Virtual Environment 的作用。


Conan client：命令行工具，用于创建包和使用包，可创建本地仓库支持离线使用
Conan server：可私有化部署的服务
JFrog Artifactory：可私有化部署的仓库
JFrog Bintray：公开&公共仓库



JFrog Artifactory Community edition for C/C++：：https://bintray.com/jfrog/product/JFrog-Artifactory-Cpp-CE/view

Conan：https://conan.io/downloads.html





C++ 包管理工具中，Conan 用的人多

Conan：https://github.com/conan-io/conan
CPM：https://github.com/iauns/cpm
biicode：https://github.com/biicode


集成 Conan
Conan支持的集成方式很多：https://docs.conan.io/en/latest/integrations.html。

这里我们以 makefile 工程来做简单说明，我们要用到 conanfile.py 以及 AutoToolsBuildEnvironment。

源码：https://github.com/memsharded/conan-example-makefiles
步骤：https://docs.conan.io/en/latest/howtos/makefiles.html
文档：https://docs.conan.io/en/latest/reference/conanfile.html



