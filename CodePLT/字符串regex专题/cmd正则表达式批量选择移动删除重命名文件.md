# 1. cmd正则表达式批量选择移动删除重命名文件


```
for /f "tokens=*" %%i in ('dir "C:\Users\admin\Documents\Tridu33\postgraduate\STRIPs\strips\examples\starcraft\*.txt" /s /b') do move "%%i" "%%i.pddl"
```
命令行%%i变%i

```
for /f "tokens=*" %i in ('dir "C:\Users\admin\Documents\Tridu33\postgraduate\STRIPs\strips\examples\starcraft\*.txt" /s /b') do move "%i" "%i.pddl"
```



cnblogs.com/txw1958/archive/2012/12/24/cmd-batch-rename.html






```
for /R %i in (*.*) do ren "%i" "*.*.bak"
```




新建文本文档bai，把以下三行复制进去du，然后保存为.bat文件

```
　　@zhiecho off

　　for /f "tokens=*" %%i in ('dir "C:\Abc\*.doc" /s /b') do copy "%%i" "E:\Backup"

　　pause
```

运行后的效果是，将daoC:\Abc目录下所有.doc的文档复制到E:\Backup目录中。

或者在cmd窗口中运行

　　for /f "tokens=*" %i in ('dir "C:\Abc\*.doc" /s /b') do copy "%i" "E:\Backup"

是一样的效果（%%i改成%i）

dir的/s开关可以检索子目录中的文件，for的"tokens=*"选项可以使命令正常作用于文件名中带有空格的文件。













```
for /f "tokens=*" %i in ('dir "C:\Users\admin\Documents\Tridu33\CS_Theories\!!!OJ_DJalgorithm\C&C++\趣题学算法c++\Algorithm-learning-through-Problems\*.cpp" /s /b') do copy "%i" "C:\Users\admin\Documents\Tridu33\CS_Theories\!!!OJ_DJalgorithm\C&C++\趣题学算法c++\Algorithm-learning-through-Problems\cpp"
```























