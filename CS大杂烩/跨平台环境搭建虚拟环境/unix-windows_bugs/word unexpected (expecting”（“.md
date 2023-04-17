PRP planner 

在windows上的wsl运行报错，而直接在完整的虚拟机上会报错这个。
```
2. Running preprocessor
./src/preprocess/preprocess: 1: Syntax error: word unexpected (expecting ")")
```

发生这种情况的一种情况是，脚本是通过Microsoft OS编写的或通过Microsoft OS传输的，其文本行结尾为CRLF，而不仅仅是LF。**"Carriage-Return"和"Line-Feed"****CR(回车)**，**LF(换行)** https://stackoverflow.com/questions/36725864/syntax-error-word-unexpected-expecting 在互联网上搜索时，我发现了很多有关此错误的帖子。阅读所有。但是对于这个错误是什么以及如何解决它仍然一无所知。如果有人可以帮助我理解此错误，我将感到非常高兴。


-------------------------------

- windows与unix文件格式转换
https://blog.csdn.net/ydyang1126/article/details/65437694

虽然很多程序不在乎 DOS/Windows 格式的 CR/LF 文本文件，但是有几个程序却在乎 – 最著名的是 bash，只要一遇到回车，它就会出问题。以下 sed 调用将把 DOS/Windows 格式的文本转换成可信赖的 UNIX 格式：

```
sed -e ‘s/.$//’ mydos.txt > myunix.txt
```

该脚本的工作原理很简单：替代规则表达式与一行的最末字符匹配，而该字符恰好就是回车。我们用空字符替换它，从而将其从输出中彻底删除。如果使用该脚本并注意到已经删除了输出中每行的最末字符，那么，您就指定了已经是 UNIX 格式的文本文件。也就没必要那样做了！




- 把Linux/UNIX 文本移至 Windows 系统，使用以下脚本执行必需的格式转换:
```
sed -e ‘s/$/\r/’ myunix.txt > mydos.txt
```

在该脚本中，’$’ 规则表达式将与行的末尾匹配，而 ‘\r’ 告诉 sed 在其之前插入一个回车。在换行之前插入回车，立即，每一行就以 CR/LF 结束。请注意，仅当使用 GNU sed 3.02.80 或以后的版本时，才会用 CR 替换 ‘\r’。






另外还有个方法：
使用命令行工具，如下

```
unix2dos  filename 
dos2unix  filename 
```







https://blog.csdn.net/agn7047/article/details/101563419
趣谈、浅析CRLF和LF




>Dos和windows采用回车+换行CR/LF表示下一行, 
>而UNIX/Linux采用换行符LF表示下一行，
>苹果机(MAC OS系统)也采用换行符LF表示下一行。
>(注：有些人认为Mac Style是CR，我查了一些资料，发现应该是这样的：老的Mac是CR，后来的OSX全部改成了LF)
CR用符号’\r’表示, LF使用’\n’符号表示。



一般操作系统上的运行库会自动决定文本文件的换行格式。 如一个程序在windows上运行就生成CRLF换行格式的文本文件，而在Linux上运行就生成LF格式换行的文本文件。
在一个平台上使用另一种换行符的文件文件可能会带来意想不到的问题, 特别是在编辑程序代码时. 有时候代码在编辑器中显示正常, 但在编辑时却会因为换行符问题而出错。
很多文本/代码编辑器带有换行符转换功能, 使用这个功能可以将文本文件中的换行符在不同格式单互换。
在不同平台间使用FTP软件传送文件时, 在ascii文本模式传输模式下, 一些FTP客户端程序会自动对换行格式进行转换. 经过这种传输的文件字节数可能会发生变化. 如果你不想ftp修改原文件, 可以使用bin模式(二进制模式)传输文本。












