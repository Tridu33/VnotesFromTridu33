


[如何用 Github 找到需要的代码？https://www.zhihu.com/question/324686541](https://www.zhihu.com/question/324686541)


一、先看paper里面有没有贴出来代码的链接，有的话最好。

二、大部分实验室都会有统一的代码管理，可以去一作的实验室主页瞅瞅，说不定有惊喜。

三、直接github上搜索关键字。

四、给一作留的邮箱发邮件交流，态度诚恳说清楚用途，一般都会给。













low B毕业设计源码
[http://www.wisdomdd.cn/Wisdom/demo/demo.jsp](http://www.wisdomdd.cn/Wisdom/demo/demo.jsp)






# 论文代码实现网站
**网站地址：**
https://paperswithcode.com/












作者：Jason Gu  
链接：https://www.zhihu.com/question/21980275/answer/19929480  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

1\. 如果这论文很老，论文里的算法在该领域有举足轻重的地位。那么网上很可能有工具包。例如我做的机器学习方向，经典的聚类、分类算法，MATLAB, python等常用语言都有丰富的工具包可供使用，一般有名的算法都会包括在其中。  
2\. 如果论文非常新，或者论文中的算法在该领域并没有多大的影响，这时网上各种编程语言自带的工具包一般是不包括它的。我能想到的大概有以下3种方法：  
a. 在google搜索该论文的名称或者第一作者的姓名，找到该作者的个人学术主页（计算机领域多数科研人员都有自己的学术主页）。在他的主页上看看他是否公开了论文的代码，很多学者乐于分享自己的代码。  
b. 在google搜索该论文中算法的名字+code或者是某种语言，如python等。这是因为阅读这篇论文的科研人员不少，有的人读完会写代码并公布出来。  
c. 邮件联系第一作者。可惜多数情况下邮件都是石沉大海。尤其是一些很忙的大牛，他们收到类似的邮件太多，可能扫一眼就不再过问。相反，如果是一些博士生，有的还是乐于分享代码的，这样自己的文章也更容易被同行引用。  
根据我个人经验，上述a,b,c方案成功的概率分别只有30%, 10%, 10%。当然不同领域的学术气氛习惯也不同。  
另外，还有的办法是，查看该论文被哪些论文引用了，引用者有时需要将自己的算法与引用的算法作比较，所以他们有可能这个算法的代码。这个途径找代码工作量更大，概率更小，所以不推荐，不过我确实有通过这个途径找到过。


最近发现一个神奇的网站，这个网站在看论文找代码的时候提供很大的便利，分享给大家。

Reddit用户rstoj做了一个网站，将ArXiv上的最新机器学习论文与GitHub上的代码（TensorFlow/PyTorch/MXNet /等）对应起来。你可以按标题关键词查询，也可以按流行程度、GitHub星星数排列“热门研究”。这个网站能让你跟上ML社区流行的最新动态。

网站地址：https://paperswithcode.com/




(1）code.google.com

(2) github.com






1\. Papers with Code

首先给出这个网站的网址：

[paperswithcode.com](https://link.juejin.im/?target=https%3A%2F%2Fpaperswithcode.com)

这是 Reddit 的一个用户 rstoj 做的一个网站，将 ArXiv 上的**最新机器学习论文与 Github 上的代码**（TensorFlow/PyTorch/MXNet/等）对应起来

2\. Browse state-of-the-art  
同样先给出网址：

[paperswithcode.com/sota](http://paperswithcode.com/sota)

这个网站主要是解决另一个问题--**寻找一个领域目前最好的（State of the art, Sota）算法的论文以及实现代码。这也是刚接触到一个新领域时候，必须要做的事情，先找到最新最好的算法论文，然后根据这篇论文的代码实现，先跑下代码，接着再去了解细节，或者是根据它的参考论文，来学习这个领域最近几年的论文**（一般是 3 年到 5 年内的），逐渐熟悉这个领域的研究方向和难点所在。

还是 Papers with Code 的团队做出了一个可以查询领域最新算法的网站，它总共包含了 16 个大类，950+的单独子类任务，500+个评估结果（包含 Sota 结果）、700+数据库，8000+论文。

[https://researchcode.com/](https://researchcode.com/)






[AI所有领域最优论文+代码查找神器：966个ML任务、8500+论文任你选https://zhuanlan.zhihu.com/p/56179379](https://zhuanlan.zhihu.com/p/56179379)






# 代码搜索


http://search.csdn.net/  
CSDN搜索，CSDN还是有非常多的编程资源的，用它的搜索能搜出不少东西。代码类别也比较全面。

http://snippets.org/  
简单实用的代码收集网站，强力推荐。比如你要找个DES加密，要找个数据压缩，找个INI文件操作的C代码等，均能手到擒来。

http://www.codase.com/index.html  
它是一个代码搜索引擎，特别是搜索c/c++的开源代码，可以通过函数名、类名等搜索，很酷噢

http://sourceforge.net  
有名的开源代码库，只要能想到的功能，上面都有对应的源码

http://www.tigris.org/  
和上面的sourceforge一样的开源代码库，不过sourceforge用CVS，而这个用SVN版本管理。

http://cosoft.org.cn/  
中文版的开源代码库，好像是由sourceforge直接翻译过来的。其同步性等尚未考察。

http://codeguru.com  
http://codeproject.com  
这两个站点比较类似，放一起吧。以WINDOWS下的Visual studio编程代码、教程为主。在以前可是使用MFC的人的必经之地。

http://www.experts-exchange.com/Programming/  
这是专家问答的网站，在编程方面能够解决不少问题。

http://www.koders.com/  
也是一个代码搜索引擎，与codase差不多，并且能查找指定许可的代码

http://groups.google.com/  
找代码，决不能忘记google的groups。一定要去噢。国内的兄弟可能访问时不稳定，就用代理吧。如果你用firefox，可以使用我开发的xyzproxy切换代理，很方便噢:)

http://www.thefreecountry.com/sourcecode/index.shtml  
这也是个源码码网站。这个网站的资源还是很多的。

http://www.vckbase.com/  
VC知识库，国内比较好的VC资源站　

http://www.programmersheaven.com/  
开发者天堂？有一些教程好像不错。

http://www.cprogramming.com/  
收集C/C++编程方面资源的网站

http://csourcesearch.net  
又一个代码搜索网站，大家试试？

http://www.netlib.org/  
源代库索引，有很多数学方面的库，很好用。要找库，以此网站着手较好











1\. 可以搜一下github。

论文作者的github id来自作者主页，有时候他们会把代码公布在自己的githhub上。 有的时候还有复现实验或者做benchmark/tool box的的研究者会在github上公布自己的代码，包含你想要的论文。但是这种不是原作者的代码不能保证其正确性，也不能当做原作引用，除非他声明已经原作者同意。

2\. 仔细看论文，有的时候代码/数据集公布会在脚注里有标注。

3.关注作者其他工作。有的作者会扩展自己的工作，此时以前的工作会作为baseline.有时候你看的那篇论文是作者扩展其他工作的，顺藤摸瓜，总比没有强。

3.如果论文citation比较高 那就看引作是否有代码。

虽然搜集资料也是科研中重要的环节，但私以为到达一定程度以后可以自己复现实验，这样可以加深理解。即使有代码，特别重要的工作可以自己复现然后对比作者代码，看看细节处理，算法理解是否与自己实现的一致，能学到不少。

  
  
作者：匿名用户  
链接：https://www.zhihu.com/question/21980275/answer/196096287  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。









# 50个c/c++源代码网站

C/C++是最主要的编程语言。这里列出了50名优秀网站和网页清单，这些网站提供c/c++源代码。这份清单提供了源代码的链接以及它们的小说明。我已尽力包括最佳的C/C++源代码的网站。这不是一个完整的清单，您有建议可以联系我，我将欢迎您的建议，以进一步加强这方面的清单。  
  
1、[http://snippets.dzone.com/tag/c/](http://snippets.dzone.com/tag/c/) --数以千计的有用的C语言源代码片段  
2、[http://www.hotscripts.com/category/c-cpp/scripts-programs/](http://www.hotscripts.com/category/c-cpp/scripts-programs/) Hotscripts --提供数以百计的C和C++脚本和程序。所有程序都分为不同的类别。  
3、[http://www.planetsourcecode.com/vb/default.asp?lngWId=3](http://www.planetsourcecode.com/vb/default.asp?lngWId=3) --超过万行C和C++免费的源代码  
4、[http://freshmeat.net/browse/164/](http://freshmeat.net/browse/164/) --超过9000个C编写的项目。  
5、[http://www.daniweb.com/code/c.html](http://www.daniweb.com/code/c.html) --DANIWEB提供的实用代码段。  
6、[http://www.programmersheaven.com/tags/C/](http://www.programmersheaven.com/tags/C/) --programmersheaven.com上的C编程资源。  
7、[http://www.ddj.com/code/ddj.html](http://www.ddj.com/code/ddj.html) --Dr. Dobb’s Journal的源代码。  
8、[http://www.cprogramming.com/cgi-bin/source/source.cgi](http://www.cprogramming.com/cgi-bin/source/source.cgi) --C和C + +编程资源。  
9、[http://www.codecogs.com/](http://www.codecogs.com/) --CodeCogs是一项协作的开放源码库，C/C++的数值方面的组件。  
10、\[URL=http://www.google.com /codesearch?q=programming++lang:c&cs\_r=lang:c \]http://www.google.com/codesearch?q=programming++lang:c&cs\_r=lang:c \[/URL\] --谷歌代码的C源代码。  
11、[http://www.codepedia.com/1/C](http://www.codepedia.com/1/C) --CodePedia是一个开放的关于系统编程和其他与电脑有关的议题。  
12、[http://www.cis.temple.edu/~ingargio/cis71/code/](http://www.cis.temple.edu/~ingargio/cis71/code/) --为学生提供的一个简单的C语言程序的列表。  
13、[http://www.codeproject.com/?cat=2](http://www.codeproject.com/?cat=2) --codeproject提供的C/C++资源代码项目。  
14、[http://www.thefreecountry.com/sourcecode/cpp.shtml](http://www.thefreecountry.com/sourcecode/cpp.shtml) --以下是一些C和C++库的DLL，VCLs，源代码，元件，模块，应用程序框架，类库，源代码片段等，你可以在您的项目中使用而不需要支付费用和版税。  
15、\[URL=http://people.sc.fsu.edu /~burkardt/cpp\_src/cpp\_src.html \]http://people.sc.fsu.edu/~burkardt/cpp\_src/cpp\_src.html \[/URL\] --这是一个全面的关于C++的345个源代码清单。  
16、[http://www.cplusplus.com/src/](http://www.cplusplus.com/src/) --C++写的通用控制台程序和Windows程序代码清单。  
17、[http://users.cs.fiu.edu/~weiss/dsaa_c++/code/](http://users.cs.fiu.edu/~weiss/dsaa_c++/code/) --C++语言数据结构与算法分析（第二版）的源代码。  
18、[http://c.snippets.org/](http://c.snippets.org/) --C源代码片段。  
19、[http://www.bbdsoft.com/downloads.html](http://www.bbdsoft.com/downloads.html) --C++源代码。  
20、[http://www.moshier.net/](http://www.moshier.net/) 天文学和数值软件源代码  
21、[http://cplus.about.com/od/cgames/C\_Games\_with\_Source\_Code.htm](http://cplus.about.com/od/cgames/C_Games_with_Source_Code.htm) --游戏有关的C++源代码。  
22、\[URL=http://cliodhna.cop.uop.edu /~hetrick/c-sources.html \]http://cliodhna.cop.uop.edu/~hetrick/c-sources.html \[/URL\] --免费的C/C++数值计算源代码。  
23、[http://www.mathtools.net/C\_C\_\_/Utilities/index.html](http://www.mathtools.net/C_C__/Utilities/index.html) --C/C++工具。  
24、[http://www.programmerworld.net/resources/c_library.htm](http://www.programmerworld.net/resources/c_library.htm) --免费C++源代码和其它有用的工具。  
25、[http://www.cmcrossroads.com/bradapp/links/cplusplus-links.html](http://www.cmcrossroads.com/bradapp/links/cplusplus-links.html) --布拉德阿普尔顿的C++链接-资源，项目，图书馆，教学和编码。  
26、[http://www.robertnz.net/cpp_site.html](http://www.robertnz.net/cpp_site.html) --这是一个收集了数C/C++网站链接列表的网页。  
27、[http://www.josuttis.com/libbook/examples.html](http://www.josuttis.com/libbook/examples.html) --在这里，你可以看到并下载所有的本书的C++标准库例子。  
28、[ftp://66.77.27.238/sourcecode/cuj/](ftp://66.77.27.238/sourcecode/cuj/) --C/C++用户杂志  
29、[ftp://66.77.27.238/sourcecode/wd/](ftp://66.77.27.238/sourcecode/wd/) --Windows开发者网络  
30、[http://www.einet.net/directory/65892/Developers.htm](http://www.einet.net/directory/65892/Developers.htm) --C程序  
31、[http://www.daniweb.com/code/cplusplus.html](http://www.daniweb.com/code/cplusplus.html) --实用代码段。  
32、[http://snippets.dzone.com/tag/c](http://snippets.dzone.com/tag/c) --C++源代码  
33、[http://www.programmersheaven.com/tags/C](http://www.programmersheaven.com/tags/C) --C++编程资源，programmersheaven.com  
34、[http://www.google.com/codesearch?hl=en&lr=&q=programming](http://www.google.com/codesearch?hl=en&lr=&q=programming) --谷歌代码搜索-C++编程语言  
35、[http://www.codepedia.com/1/Cpp](http://www.codepedia.com/1/Cpp) --CodePedia是一个开放的关于系统编程和其他与电脑有关的议题的网站。  
36、[http://www.codebeach.com/index.asp?TabID=1&CategoryID=3](http://www.codebeach.com/index.asp?TabID=1&CategoryID=3) --C++源代码，Codebeach提供  
37、[http://freshmeat.net/browse/165/](http://freshmeat.net/browse/165/) --5000项目写的C++编程语言  
38、[http://cplus.about.com/od/codelibrary/Code\_Library\_for\_C\_C\_and\_C.htm](http://cplus.about.com/od/codelibrary/Code_Library_for_C_C_and_C.htm) --代码库C、C + +和C＃。  
39、[http://www.c.happycodings.com/](http://www.c.happycodings.com/) --Visual Basic、PHP、ASP技术、C、C++大全。  
40、[http://www.blueparrots.com/](http://www.blueparrots.com/) --Borland C游戏，图像和声音源代码范例。  
41、[http://www.java2s.com/Code/Cpp/CatalogCpp.htm](http://www.java2s.com/Code/Cpp/CatalogCpp.htm) --C++源代码。  
42、[http://www.yeohhs.com/modules/mydownloads/](http://www.yeohhs.com/modules/mydownloads/) --C与C++电子书和源代码示例。  
43、[http://www.brpreiss.com/books/opus4/programs/index.html](http://www.brpreiss.com/books/opus4/programs/index.html) C++的数学方程和公式源代码。  
44、http://users.cs.fiu.edu\]\[/URL\]http://users.cs.fiu.edu/ C++。  
45、http://www.josuttis.com/libbook/examples.html\]\[/URL\]http://www.josuttis.com/libbook/examples.html --C++标准库-教程和参考资料。  
46、[http://emr.cs.uiuc.edu/~reingold/calendars.shtml](http://emr.cs.uiuc.edu/~reingold/calendars.shtml) Edward M. Reingold's Calendar Book, Papers, and Code。  
47、[http://cpp.snippets.org/](http://cpp.snippets.org/) --c++源代码档案。  
48、[http://ubiety.uwaterloo.ca/~tveldhui/papers/techniques/](http://ubiety.uwaterloo.ca/~tveldhui/papers/techniques/) --用C和C++的解决科学问题。  
49、[http://c.ittoolbox.com/topics/core-c/](http://c.ittoolbox.com/topics/core-c/) --C/C++的IT工具框。  
50、[http://www.le.ac.uk/cc/tutorials/c/ccccdbas.html](http://www.le.ac.uk/cc/tutorials/c/ccccdbas.html) --本文件中包含有大量的C示例程序







































































































