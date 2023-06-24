# UTF-8与UTF-8(BOM 字节顺序标记(ByteOrderMark))
# 有得选的话：UTF-8最好不要带BOM

简单说就是文件开头的ef、bb、bf

用xxd指令看一下这个文件，可以看到BOM头，这个文件就是带BOM的UTF-8的文件
一开始生成的打印文件编码格式是UTF-8 Unicode text，通过先写入BOM头ef bb bf，生成 UTF-8 Unicode (with BOM) text
```
xxs *.txt
```
![](_v_images/1627789068_11576.png)
- C++ 中出现“error C2001: newline in constant“问题的解决方法

txt记事本打开保存为“utf-8 with BOM”


微软在UTF-8中使用BOM（Byte order mark）是因为这样可以将UTF-8和ASCII等编码明确区分开。 

windows对于utf-8格式的文件存储默认是带有BOM的格式

因为在UNIX环境下，很多的UNIX程序不认识BOM。主要是在UNIX所有脚本语言首行为#！标示，它依赖于shell解析，而很多shell出于兼容的考虑不检测BOM，所以加进BOM时shell会把它解释为某个普通字符输入导致破坏#！标示。比如很多现代脚本语言，例如python，其解释器本身是能处理BOM的，但是shell卡在这里。
因此我们在linux服务器上读取这些txt文件时，会遇到如下报错： 

\xef\xbb\xbf…

解决方法

import codecs

with open("xx.txt",'r','utf-8-sig') as file:

        line = file.readlines()

或者：

#打开文件,此次应指定编码，

fr=open(filename,'r',encoding='utf-8')

#读取文件所有内容

arrayOLines=fr.readlines()

#针对有BOM的UTF-8文本，应该去掉BOM，否则后面会引发错误。

arrayOLines[0]=arrayOLines[0].lstrip('\ufeff')









































