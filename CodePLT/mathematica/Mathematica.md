# 教程资源
https://www.zhihu.com/question/27834147
# Mathematica 到底有多厉害？
链接：https://www.zhihu.com/question/25039966/answer/36233118  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

零基礎的可以看看 [Wolfram Language Tutorial: A Fast Introduction for Programmers](https://link.zhihu.com/?target=http%3A//www.wolfram.com/language/fast-introduction-for-programmers/) ，官方的快速入門，對浩繁的功能選擇了最核心的一部份做的極簡風格的入門教程，一個小時就入門。2015 年新出了一本 [An Elementary Introduction to the Wolfram Language by Stephen Wolfram](https://link.zhihu.com/?target=http%3A//www.wolfram.com/language/elementary-introduction/)，稍微长一点，系统性一点。

然後讀 Shifrin 的 《[Mathematica programming](https://link.zhihu.com/?target=http%3A//www.mathprogramming-intro.org/) ﹣ An Advanced Introduction》，英文能力夠的讀英文原作。不夠的，可以讀志願者翻譯的中文版（不完整）[http://www.mathcraft.org/wiki/index.php?title=Mathematica_%E7%BC%96%E7%A8%8B%EF%BC%9A%E9%AB%98%E7%BA%A7%E5%AF%BC%E8%AE%BA](https://link.zhihu.com/?target=http%3A//www.mathcraft.org/wiki/index.php%3Ftitle%3DMathematica_%25E7%25BC%2596%25E7%25A8%258B%25EF%25BC%259A%25E9%25AB%2598%25E7%25BA%25A7%25E5%25AF%25BC%25E8%25AE%25BA) 。通讀一遍裨益良多。

在有了一定基礎后，如果要達到精通，需要長期持續學習，主要是在解決實際問題的過程中學，原因是 Mathematica / Wolfram 語言的內容和功能「 包羅萬象」，用了 n 年后你還會有不斷髮現「驚喜」，而且一個新版本發佈出來經常會增加很多新功能（參見：[Mathematica 最新版本和旧版本历史](https://link.zhihu.com/?target=http%3A//www.wolfram.com/mathematica/quick-revision-history.zh.html)）。在解決問題的過程中參考 [Wolfram Language & System Documentation Center](https://link.zhihu.com/?target=http%3A//reference.wolfram.com/language/) （官方幫助文檔），反復看裡面的語法說明、專項說明、例子，自己常用的功能就會越來越熟。官方文檔里有一部份寫成專題的稱為「[tutorial](https://link.zhihu.com/?target=http%3A//www.wolfram.com/learningcenter/tutorialcollection/)」，可以挑自己感興趣的專門拿出來深入學習。

還可以看 [Mathematica Stack Exchange](https://link.zhihu.com/?target=http%3A//mathematica.stackexchange.com) 上的[學習資料表](https://link.zhihu.com/?target=http%3A//mathematica.stackexchange.com/questions/18/where-can-i-find-examples-of-good-mathematica-programming-practice)、[初学者常见错误](https://link.zhihu.com/?target=http%3A//mathematica.stackexchange.com/questions/18393/what-are-the-most-common-pitfalls-awaiting-new-users)，MathCraft.org 整理的[參考資料表](https://link.zhihu.com/?target=http%3A//www.mathcraft.org/wiki/index.php%3Ftitle%3DMathematica_%25E5%25AD%25A6%25E4%25B9%25A0%25E8%25B5%2584%25E6%25BA%2590)。這時候只怕學習時間不夠用了。還可以經常逛逛 [Mathematica Stack Exchange](https://link.zhihu.com/?target=http%3A//mathematica.stackexchange.com)，[Wolfram Community](https://link.zhihu.com/?target=http%3A//community.wolfram.com/)，關注Wolfram 官方微博 [@WolframChina](https://link.zhihu.com/?target=http%3A//www.weibo.com/wolframchina)，有最新的和 Mathematica / Wolfram 語言相關的信息發佈。




展示了如何用Mathematica计算和式，本身是用于验证考研书上的解答对不对， 
在验证自己的想法后，发现计算过程不是很有把握，所以试着在Mathematica里寻求计算你步骤。

解决办法
两个函数：

Trace[]

TracePrint[]

示例
可以参照官方手册。

参考资料
Mathematica官方资料：Tracing Evaluation

Mathematica Documentation Center tutorial/TracingEvaluation






人人小站mathematica
zhan.renren.com/mathilove?checked=true


## matlab mathematica区别
作者后来提出一个很关键的问题,就是以独立工具箱提供的功能模块,他们之间协作能力太差了,最典型的是符号运算工具箱就不能和其他模块一起使用.

https://www.ilovematlab.cn/thread-48952-1-1.html


mathematica整个就是符号计算,至于说究竟那个容易,这个毕竟是见仁见智的事情.
不过不可否认他的优势就是在于能让符号计算几乎贯穿他的所有功能.
其次就是数值精度方面mathematica也比matlab有优势啊.



而mathematica的优势是它包含过程式（比如像c,fortran,matlab），函数式（Lisp），说明式（Prolog）等

但是其优势是体现在使用函数式和说明式，具体是对处理列表（在mathematica里有对列表更广义的定义，这是基于Lisp语言的思想，所以这些函数不只是对通常所想的列表的处理，实际上是相当灵活的，要不然像Lisp这种没有循环语句的语言怎么会成为目前最优秀的语言）的函数使用上，以及模式匹配及替换


















## debug


可以试试 [TracePrint](https://link.zhihu.com/?target=https%3A//reference.wolfram.com/language/ref/TracePrint.zh.html)，[Trace](https://link.zhihu.com/?target=https%3A//reference.wolfram.com/language/ref/Trace.zh.html)，[TraceDialog](https://link.zhihu.com/?target=http%3A//reference.wolfram.com/language/ref/TraceDialog.zh.html) 来解决你的问题。Mathematica 有自带的 deugger 可以在先行选择的断点停止程序运行，然后逐步执行，这里有个例子：[Debugging with Breakpoints](https://link.zhihu.com/?target=http%3A//mathematica.stackexchange.com/questions/31066/debugging-with-breakpoints)，用 [step / 步进 那个按钮](https://link.zhihu.com/?target=http%3A//reference.wolfram.com/language/ref/menuitem/DebuggerControls.html) 来一步一步执行。如果你有 [Wolfram Workbench](https://link.zhihu.com/?target=https%3A//www.wolfram.com/products/workbench/index.zh.html%3Ffooter%3Dlang)，里面有较好用的 debugger，这里有个几分钟的视频：[Wolfram Videos: Basic Debugging with Wolfram Workbench](https://link.zhihu.com/?target=http%3A//www.wolfram.com/broadcast/video.php%3Fc%3D93%26v%3D890)，相关的文档：在 [Wolfram Workbench Documentation](https://link.zhihu.com/?target=http%3A//reference.wolfram.com/workbench/index.jsp) 里搜「Debugging」。大部分情况在 notebook 里 TracePrint 就够用了

  
  
作者：燕南  
链接：https://www.zhihu.com/question/35259081/answer/62312197  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


## 笔记






























































































































