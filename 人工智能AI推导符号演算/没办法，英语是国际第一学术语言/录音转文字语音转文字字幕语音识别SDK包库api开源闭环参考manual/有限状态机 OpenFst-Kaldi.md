# 1. 有限状态机 OpenFst-Kaldi







简书教程[Kaldi中FST(Finite State Transducer)含义及其可视化](https://www.jianshu.com/p/4ad2add56b25)









常用的openfst的命令。help的信息我就不放了，可以自己看。

### 1.1.1. fstaddselfloops：

加一个自旋，一般是在初始节点上。别的节点没试过。。这句在生成L.fst的时候有遇到过。

将自回路添加到 FST 的状态以通过它传播消歧符号  
它们被添加到每个最终状态，每个状态都带有非 epsilon 输出符号  
至少在一个弧状态之外。 与预先确定一起使用

用法：fstaddselfloops in-disambig-list out-disambig-list \[in.fst \[out.fst\]\]  
例如：fstaddselfloops in.list out.list <in.fst> withloops.fst

fstaddselfloops  "echo 122 |" "echo 7 |" | \

#加上自旋，主要是对122 7 的#0进行自旋。注释此句，比较下区别就知道了。  
49 #区别: 0 -> 0 \[label = "#0:#0", fontsize = 14\];  < 0 0 122 7

### 1.1.2. fstisstochastic：

对G.fst进行检查，为什么做这一步？

检查 FST 是否随机，如果有则退出成功。  
打印出最大错误（以日志为单位）。

用法：fstisstochastic \[in.fst\]

fstisstochastic $outlangdir/G.fst

### 1.1.3. fsttablecompose：

用法：fsttablecompose（fst1-rxfilename | fst1-rspecifier）（fst2-rxfilename | fst2-rspecifier）\[（out-rxfilename | out-rspecifier）\]

选项：  
   --compose-filter：使用的合成过滤器，其中之一：“alt_sequence”，“auto”，“match”，“sequence”（string，default =“sequence”）  
   --connect：如果为 true，则在输出前修剪 FST。 （布尔，默认 = true）  
   \- 匹配侧：进行表匹配的组合的一侧，其中一个：“左” 或 “右”。 （字符串，默认 =“左”）

注意顺序 fsttablecompose   A.fst  B.fst > C.fst

可以这样简易理解：A    a:b/0.4   B   b:c/0.3     C    a:c/0.7

### 1.1.4. fstcompile：

从简单文本格式创建二进制 FST。最常用的一个了。

  用法：fstcompile \[text.fst \[binary.fst\]\]

标志：

  --accept：type = bool，default = false  
  以接受者格式输入  
  --allow\_negative\_labels：type = bool，default = false  
  允许使用负面标签（不推荐; 可能会导致冲突）  
  --arc_type：type = string，default =“standard”  
  输出弧类型  
  --fst_type：type = string，default =“vector”  
  输出 FST 类型  
  --isymbols：type = string，default =“”  
  输入标签符号表  
  --keep_isymbols：type = bool，default = false  
  用 FST 存储输入标签符号表  
  --keep_osymbols：type = bool，default = false  
  将输出标签符号表与 FST 一起存储  
  --keep\_state\_numbering：type = bool，default = false  
  不要重新编号输入状态  
  --osymbols：type = string，default =“”  
  输出标签符号表  
  --ssymbols：type = string，default =“”  
  状态标签符号表

库标志：

标志来自：flags.cc  
  --help：type = bool，default = false  
  显示使用信息  
  --helpshort：type = bool，default = false  
  显示简要的使用信息  
  --tmpdir：type = string，default =“/ tmp /”  
  临时目录  
  --v：type = int32，default = 0  
  详细级别

标志来自：fst.cc  
  --fst_align：type = bool，default = false  
  在适当的地方写入 FST 数据  
  --fst\_default\_cache_gc：type = bool，default = true  
  启用缓存的垃圾回收  
  --fst\_default\_cache\_gc\_limit：type = int64，default = 1048576  
  缓存触发垃圾回收的字节大小  
  --fst\_read\_mode：type = string，default =“read”  
  可映射文件的默认文件读取模式  
  --fst\_verify\_properties：type = bool，default = false  
  验证由 TestProperties 查询的 fst 属性  
  --fst\_weight\_parentheses：type = string，default =“”  
  包围印刷复合砝码的第一重量（例如配对重量，元组重量和派生类）的字符以确保嵌套复合砝码的正确 I / O; 必须具有大小 0（无）或 2（开括号和右括号）  
  --fst\_weight\_separator：type = string，default =“，”  
  印刷复合重物之间的字符分隔符必须是单个字符  
  --save\_relabel\_ipairs：type = string，default =“”  
  将输入重新标记对保存到文件  
  --save\_relabel\_opairs：type = string，default =“”  
  将输出重新标记对保存到文件

标志来自：symbol-table.cc  
  --fst\_compat\_symbols：type = bool，default = true  
  适当时需要符号表匹配  
  --fst\_field\_separator：type = string，default =“”  
  用作打印字段之间分隔符的字符集

### 1.1.5. fstarcsort：

排序 FST 的弧线。排序。

  用法：fstarcsort \[in.fst \[out.fst\]\]

计划标志：

  --sort_type：type = string，default =“ilabel”  
  比较方法之一：“ilabel”，“olabel”

库标识：

标志来自：flags.cc  
  --help：type = bool，default = false  
  显示使用信息  
  --helpshort：type = bool，default = false  
  显示简要的使用信息  
  --tmpdir：type = string，default =“/ tmp /”  
  临时目录  
  --v：type = int32，default = 0  
  详细级别

标志来自：fst.cc  
  --fst_align：type = bool，default = false  
  在适当的地方写入 FST 数据  
  --fst\_default\_cache_gc：type = bool，default = true  
  启用缓存的垃圾回收  
  --fst\_default\_cache\_gc\_limit：type = int64，default = 1048576  
  缓存触发垃圾回收的字节大小  
  --fst\_read\_mode：type = string，default =“read”  
  可映射文件的默认文件读取模式  
  --fst\_verify\_properties：type = bool，default = false  
  验证由 TestProperties 查询的 fst 属性  
  --fst\_weight\_parentheses：type = string，default =“”  
  包围印刷复合砝码的第一重量（例如配对重量，元组重量和派生类）的字符以确保嵌套复合砝码的正确 I / O; 必须具有大小 0（无）或 2（开括号和右括号）  
  --fst\_weight\_separator：type = string，default =“，”  
  印刷复合重物之间的字符分隔符必须是单个字符  
  --save\_relabel\_ipairs：type = string，default =“”  
  将输入重新标记对保存到文件  
  --save\_relabel\_opairs：type = string，default =“”  
  将输出重新标记对保存到文件

标志来自：symbol-table.cc  
  --fst\_compat\_symbols：type = bool，default = true  
  适当时需要符号表匹配  
  --fst\_field\_separator：type = string，default =“”  
  用作打印字段之间分隔符的字符集































[http://www.openfst.org/twiki/bin/view/FST/WebHome](http://www.openfst.org/twiki/bin/view/FST/WebHome)



文档

[http://www.openfst.org/twiki/bin/view/FST/ReadMe](http://www.openfst.org/twiki/bin/view/FST/ReadMe)


源码下载
[http://www.openfst.org/twiki/bin/view/FST/FstDownload](http://www.openfst.org/twiki/bin/view/FST/FstDownload)


OpenFst is a library for constructing, combining, optimizing, and searching weighted finite-state transducers (FSTs).

-   [OpenFst](http://www.openfst.org/twiki/bin/view/FST/WebHome)
-   [pyfst](http://pyfst.github.io/index.html)

## 1.2. 学习资源

-   [OpenFst论文、Tutorial](https://www.dropbox.com/s/gzv31ikxr57ucuz/OpenFST.zip)
-   [其他](https://www.dropbox.com/s/cnmaqxntx2nyum2/WFST.zip)





## 1.3. WFST in Kaldi

-   [Decoding graph construction in Kaldi](http://kaldi.sourceforge.net/graph.html)




































































