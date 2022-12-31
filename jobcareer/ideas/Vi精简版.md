# vim精简版教程
分享一篇文章，原文位于：[vim精简版教程](http://link.zhihu.com/?target=https%3A//www.jianshu.com/p/e7f87293c111)
## 编辑器的分类

-   文本编辑器，ASCII码
-   字处理器：word

## 全称

-   vi：Visual interface
-   vim: Visual interface improved

## 分类

-   全屏编辑器,

> vim  
> Emacs  
> notepad++  
> ...

-   模式编辑器

> grep  
> sed  
> awk

## vim模式：

1.  编辑模式（命令模式）
2.  输入模式
3.  末行模式
4.  可视化模式（块）

默认处于编辑模式

## 模式转换

`编辑模式（命令模式） --->>输入模式`

```text
  i：在当前光标所在字符的的前面，转换为输入
    a：在当前光标所在字符的的后面，转换为输入
    o:在当前光标所在字符的行下方，新建一行，并转为输入模式。
    I:在当前光标所在行的行首，转为输入模式
    A:在当前光标所在行的行尾，转为输入模式
    O:在当前光标所在行的上方，新建一行，并转为输入模式。

```

`输入模式--->编辑模式（命令模式)`

```text
ESC键

```

`编辑模式（命令模式）---->>末行模式`

```text
:
10d
10,20d
set nu
!ls /etc

```

`末行模式---->> 编辑模式（命令模式）`

```text
ESC  ESC键

```

## 一.打开文件：

```text
vim filename
vim /path/to/somefile
vim +12 file ：打开文件，光标在12行
vim  +# file :打开文件，光标在N行
vim  +   file：打开文件，光标在最后一行。
vim  +/pattern file ：打开文件，光标在第一个匹配的行首

```

## 二.关闭文件：

```text
1.末行模式关闭文件
:q　　退出
:q!
:wq   保存退出
；w  保存 
：w!  强制保存
:wq   --> :x

2.编辑模式（命令模式）
ZZ:保存退出

```

## 三.移动光标（编辑模式）

```text
1.逐字符移动：
 h:向右
 j:向下
 k:向上
 l:向左
 数字h  
 5h：向右移动5个字符
 
2.逐个单词移动
 w:移动到下一个单词词首
 e：跳到当前单词或下一单词的词尾
 b：跳到当前单词或前一单词的词首
 #w：一次跳n个单词。
 4b:


3. 行内跳转
  0：跳到行首(绝对行首)
  ^:行首的第一个非空白字符
  $:绝对行尾
4.行间跳转
   #G：跳转到n行
   G：最后一行
   GG：第一行

  末行模式   ：#  移动到n行

```

## 四、翻屏

```text
编辑模式（命令模式）
f： 向后翻一屏、
CTRL+b:向上翻一屏

Ctrl+d： 向下翻半屏
Ctrl+u:向上翻半屏

```

## 五、删除单个字符

```text
x：删除光标所在处的单个字符
#x:删除光标所在处及向后n个字符

```

## 六、删除命令：d

```text
d命令跟跳转命令组合使用
dw：
3dw：
#de，#db
dd：删除当前光标所在行
#dd：删除当前光标所在行及下面共#行 


末行模式下
startadd，Endaddd
1,8d
.,5+d
.:表示当前行
$:表示最后一行
+#：向下#行
1,$-3d:

最后一次删除的内容，可以粘贴到别处

```

## 七、粘贴命令p

```text
p:如果删除或复制为整行内容，则粘贴至光标所在行的下方，如果复制或删除的内容为非整行，则粘贴至光标所在字符的后面；
P:如果删除或复制为整行内容，则粘贴至光标所在行的上方，如果复制或删除的内容为非整行，则粘贴至光标所在字符的前面；

```

## 八、复制命令 y

```text
yy：一行
#y：

```

## 九、先删除内容，在转换为输入模式(修改)

```text
c：同d命令
c$:
cc:
5C:

```

## 十、替换

```text
r:替换单个字符
R：进入替换模式

```

## 十一、撤销编辑操作：

```text
u:撤销前一次的操作：
  连续u，撤销此前n次操作
3u
#u：撤销最近#次操作

```

## 十二、撤销上一次的撤销

```text
Ctrl+r
恢复

```

## 十三、重复前一次编辑操作

```text
.

```

## 十四、可视化模式

```text
v：按字符选取
V：按矩形选取
Ctrl+v:

```

## 十五、查找

```text
/pattern
?pattern
n
N

```

## 十六、查找并替换

```text
在末行模式下

用法和sed一样

address1，address2s/pattern/string/gi

1，$

%:表示全文。

```

## 十七、打开多个文件

```text
vim file1 file2
;next 切换至下一个文件
：prev 切换至前一个文件
：last 切换至最后一个文件
：first 切换最前面的一个文件
退出
：qall 全部退出

```

## 十八：分屏显示一个文件

```text
ctrl+w ,s:水平分割窗口
ctrl+w,v:垂直分割窗口

在窗口间切换光标
Ctrl+w，ARRON

：qa 关闭所有窗口

```

## 十九、分窗口多个文件

```text
vim -o file1 file2  file3 ..水平分割窗口
vim -O  file1 file3 ....    垂直分割窗口
二十、将当前文件部分内容另存为另一文件
末行模式下使用w命令
：w
：add1,addr2w /path/to/somewhere

```

## 二十一、将另一个文件的内容填充在当前文件中

```text
：r /path/to/somefile

```

## 二十二、跟shell交互

```text
：!command

```

## 二十三、高级话题

```text
1.显示或取消行号
：set number
set nu
：set nonu
2、显示忽略大小写或区分大小写
set ignorecase
set ic
:set noignorecase
:set noic
3.设定自动缩进
：set autoindent
:set noai

4.查找的文本高亮显示或取消
：set hlsearch
:set nohlsearch

5.语法高亮
:syntax on
:syntax off

```

## 二十四、配置文件

```text
/etc/vimrc
~/.vimrc(家目录下)

```

## 二十五、练习vim的小游戏

```text
vimtutor 
vim -r file
```