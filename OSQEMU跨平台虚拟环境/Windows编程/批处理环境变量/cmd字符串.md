# cmd字符串










截取

@echo off
set str=123456789
echo 第一个字符为：%str:~0,1%
echo 头两个字符为：%str:~0,2%
echo 头5个字符为：%str:~0,5%
echo 去掉最后一个字符后的字符串为：%str:~0,-1%
echo 去掉最后3个字符后的字符串为：%str:~0,-3%
echo 第4个字符为：%str:~3,1%
echo 第4个及其之后的3个字符为：%str:~3,4%
echo 最后一个字符为：%str:~-1%
echo 最后一个字符为：%str:~-1,1%
echo 最后一个字符为：%str:~-1,2%
echo 倒数第4个字符为：%str:~-4,1%
echo 倒数第4个及其之后的字符为：%str:~-4%
echo 倒数第4个及其之后的1个字符为：%str:~-4,2%
echo 倒数第4个及其之后的2个字符为：%str:~-4,3%
pause

路径处理

set TARGET_DSK=%~d1
set TARGET_DIR=%1
set TARGET_DIR_NAME=%~n1

调用自己
if "%1" == "" (
%0 %CD%
goto END
)

```
@echo off
set str=techcomp/menu/navigator/outlook/childMenu.js
for %%a in ("%str%") do md %%~dpa
echo end...
pause
```

bat批处理 变量字符串赋值、设置、拼接、截取 - 让我们平等的认知世界的文章 - 知乎
https://zhuanlan.zhihu.com/p/36137294
















