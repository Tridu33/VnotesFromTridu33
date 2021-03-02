# 1. Win10安装gfortran



























下载链接:

[http://users.humboldt.edu/finneyb/gfortran-windows-20140629.exe](http://users.humboldt.edu/finneyb/gfortran-windows-20140629.exe)

下载好后解压安装。

另外这个网站提供了几个不同系统的安装版本:  

[https://gcc.gnu.org/wiki/GFortranBinaries](https://gcc.gnu.org/wiki/GFortranBinaries)

  

这里有详细的使用说明：

[https://gcc.gnu.org/wiki/GFortranBinariesWindows](https://gcc.gnu.org/wiki/GFortranBinariesWindows)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

软件安装完后，编译自己的fortran文件

在cmd窗口中进入fortran文件所在的目录,如：

C:>cd /D F:MacCopyVTri6_WD2lcdc2015  

F:MacCopyVTri6_WD2lcdc2015>gfortran dc22may2015flop.f -o dctest  

生成dctest.exe，点击即可运行fortran程序。




1、source中未使用外部庫鏈接的，直接執行：

gfortran foo.f/f90 -o foo

./foo

如沒有"-o"選項，生成a.out文件，這顯然不是我想要的。：D

2、gFortran分兩部分：compiler and library。如果gFortran不是標準安裝的，編譯source后執行，可能找不到lib，這時可以加入"-static"選項：

gfortran -static foo.f/f90 -o foo

gFortran會將庫建在所生成程式內部。

3、FortranSource有77和90兩種書寫格式，gFortran默認根據後綴進行compile。如果想自定義，例如foo.f是用90格式寫的，可執行：

gfortran -ffree-form foo.f -o foo

大寫的後綴名，gFortran會預執行該程式。

4、多source文件時，先compile不含PROGRAM語句段的source文件，各自生成foo1.o，foo2.o等。再一起編譯。例如：

gfortran -c foo1.f/f90

gfortran -c foo2.f/f90

gfortran main.f/f90 foo1.o foo2.o -o main

5、foo.f95的，加選項"-std=f95"，.f2003的，目前支援尚不完整。順便說，gFortran unstable版4.3.x將支援pointer。

下面還有一些可能常用到的options。

"-fbounds-check"：检查列表序列脚标是否超出

"-ffree/ffix-line-length-n"：设置最大columns。77默认：72;90默认：132。n若设为"0"或"none"，则不限有效行数

"-fimplicit-none"：等同于在f90每段sub中声明"IMPLICIT NONE"，且source中implicit语句优先

"-fmax-error-n"：意义如词义

"-fsyntax-only"：不编译，只检查语法

"-fexternal-blas"：使用BLAS库函数，替代gFortran默认的函数






































