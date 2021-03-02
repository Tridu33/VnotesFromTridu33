# noweb




Noweb —一个简单，可扩展的工具，可进行精巧编程




cs.tufts.edu/~nr/noweb/











noweb旨在满足有识字的程序员的需求，同时保持尽可能简单。它的主要优点是简单，可扩展性和语言独立性-与其他识字编程工具相比尤其引人注目。 noweb使用5个控制序列来控制WEB的27个。noweb手册只有4页；另一页介绍了如何自定义其LaTeX输出。 noweb 可使用任何编程语言``开箱即用''，并支持TeX，乳胶，HTML和troff后端。支持完整超文本或索引的后端大约需要250行。一个简单的代码可以用40行awk编写。相对于WEB而言，主要的牺牲是很少打印代码。Noweb是从[CTAN发行的](https://www.ctan.org/pkg/noweb)。

noweb在许多大学和工业站点中已经使用了三十（！）年。它已经被用于awk，C，C ++，Haskell，Icon，Modula-3，Objective Caml，PAL，perl，Promela，R，Turing和Standard ML等语言的成千上万行代码。我维护了[使用noweb](https://www.cs.tufts.edu/~nr/noweb/users)[的人员和项目](https://www.cs.tufts.edu/~nr/noweb/users)的[列表](https://www.cs.tufts.edu/~nr/noweb/users)。

文章

-   安德鲁·约翰逊（Andrew L.Johnson）和布拉德·约翰逊（Brad C.Johnson）。 [使用noweb](https://www.cs.tufts.edu/~nr/noweb/johnson-lj.pdf)[进行](https://www.cs.tufts.edu/~nr/noweb/johnson-lj.pdf)[文字](https://www.cs.tufts.edu/~nr/noweb/johnson-lj.pdf)[编程](https://www.cs.tufts.edu/~nr/noweb/johnson-lj.pdf)。 *[Linux Journal](http://www.linuxjournal.com/article/2188)*，64-69，1997年10月。
-   诺曼·拉姆西（Norman Ramsey）。[精简的编程简化](https://www.cs.tufts.edu/~nr/pubs/lpsimp-abstract.html)。 *IEEE软件*，11（5）：97-105，1994年9月。

用noweb介绍识字编程。*Linux Journal上*的文章比较基础。*软件中*的文章解释了什么使 noweb变得简单和可扩展（以及为什么这些很重要）。















规范的源代码在 [github上](https://github.com/nrnrnr/noweb)。应该使用问题跟踪器报告错误。

对于Linux用户，我建议获取[Debian软件包](http://packages.debian.org/noweb)。对于其他人，请尝试[CTAN](https://www.ctan.org/pkg/noweb)。我还尝试制作 [Red Hat RPM](https://www.cs.tufts.edu/~nr/noweb/nowebm-2.11a-2.i386.rpm)；如果能奏效，我将不胜感激。

提醒老人们：noweb仍然反映在CTAN上，但是自从我在1990年代初开始分发noweb以来，我们关于如何获取事物的想法已经发生了变化，我们对大事物的想法也发生了变化。在糟糕的过去， CTAN动态地构建了压缩的tar文件，以节省磁盘空间。自从2003年该服务崩溃以来，我不再建议从CTAN中获取noweb。） 可以使用 [Debian](http://packages.debian.org/noweb)和 [NetBSD 1.3.x（g）的](http://www.netbsd.org/)[预编译二进制文件](ftp://ftp.netbsd.org/pub/NetBSD/packages/pkgsrc/devel/noweb/README.html) 。[](http://packages.debian.org/noweb)[](http://www.netbsd.org/)

[Jim Pettigrew](http://www.jim-pettigrew.com/)编写[了Windows 7](http://www.jim-pettigrew.com/noweb/install/)（位于mingw之上）的[安装说明](http://www.jim-pettigrew.com/noweb/install/)。
## 万维网资源

可以通过WWW获得详细信息和示例：

-   Noweb [常见问题解答](https://www.cs.tufts.edu/~nr/noweb/FAQ.html)。
-   用户文档采用的Unix的形式[男子 页](http://www.cs.virginia.edu/cgi-bin/manpage?section=1&topic=notangle)，这是在网上。
-   如果您不喜欢阅读文档，或者在记住已阅读内容时遇到麻烦，[可以使用LaTeX与Noweb结合使用](https://www.cs.tufts.edu/~nr/noweb/onepage.ps)的[单页指南](https://www.cs.tufts.edu/~nr/noweb/onepage.ps)。
-   [](https://www.cs.tufts.edu/~nr/noweb/examples/index.html)以HTML呈现的[示例程序](https://www.cs.tufts.edu/~nr/noweb/examples/index.html)，包括从noweb源自动创建的超文本链接。大多数人的文档块都是从乳胶自动转换而来的。
-   自1998年4月以来，许多好心的人已经寄出了[明信片](https://www.cs.tufts.edu/~nr/noweb/gallery/)，这些[明信片](https://www.cs.tufts.edu/~nr/noweb/gallery/)可以在网上查看。
-   一个noweb的最大优点是，你可以通过使用香草系统开始，然后逐渐增加的扩展和定制根据需要，所有甚至没有重新编译。《[Noweb黑客指南》](https://www.cs.tufts.edu/~nr/noweb/guide.ps)详细介绍了 noweb的工作原理，以便您添加新功能。（该指南的[HTML版本](https://www.cs.tufts.edu/~nr/noweb/guide.html)可用，但是由于它是从乳胶源自动转换而来的，因此不具有权威性。）[此处](https://www.cs.tufts.edu/~nr/noweb/extensibility.html)概述了可扩展性策略 。
-   noweb的自定义扩展包括解析和处理nuweb文件的能力，以及将LaTeX转换为HTML的能力。这个用noweb工具格式化的[nuweb程序](https://www.cs.tufts.edu/~nr/noweb/nuweb.html)同时展示了这两种方法。
-   单独的页面讨论了 noweb的[索引](https://www.cs.tufts.edu/~nr/noweb/indexing.html)功能。由于noweb与语言无关，因此出现了几种特质。
-   该[LYX文件处理器](http://www.lyx.org/)，它提供了一个所见即所得的界面，但是是用乳胶兼容，自1999年3月，支持Noweb。
-   从2.8a版开始，发行版包括Thorsten Ohl的 Emacs 的noweb模式。乔·凯尔西（Joe Kelsey）为emacs mmm-mode写了一个很有前途的类，但是它还没有立即可用。
-   Felix Gaertner构建了[Pretzel](http://www.informatik.tu-darmstadt.de/BS/Gaertner/pretzel/)，这是一种可与noweb一起使用的prettyprinter生成器。
-   Felix的学生Sven Kloppenburg构建了 [Noerr](https://github.com/svnk/noerr/)，它重写了错误消息，因此没有#line的语言实现 可以与noweb很好地配合使用。
-   [Dan Schmidt](http://www.dfan.org/index.html)构建了 [dpp和fu](http://www.dfan.org/real/noweb.html)，这有助于使noweb输出看起来像CWEB，以及GNU emacs 的漂亮 [轮廓模式](http://www.dfan.org/real/noweb.html)。
-   [下面](https://www.cs.tufts.edu/~nr/noweb/#ftp-sites)列出了用于noweb的一些[ftp站点](https://www.cs.tufts.edu/~nr/noweb/#ftp-sites)。[](https://www.cs.tufts.edu/~nr/noweb/#ftp-sites)
-   这是我的[近期计划，以及](https://www.cs.tufts.edu/~nr/noweb/wish.html)对noweb进行改进的[愿望清单](https://www.cs.tufts.edu/~nr/noweb/wish.html)。您也可以查看[Noweb 3](https://www.cs.tufts.edu/~nr/noweb/plans3.html)的[计划](https://www.cs.tufts.edu/~nr/noweb/plans3.html)，也可以查看[有关Noweb 3](https://www.cs.tufts.edu/~nr/noweb/why3.html)的 [较早的白皮书](https://www.cs.tufts.edu/~nr/noweb/why3.html)。
-   Rob Partington在支持[纯TeX中的交叉引用](http://browser.org/rp/noweb/)方面做了一些工作 。
-   Noweb的宽松[的版权](https://www.cs.tufts.edu/~nr/noweb/#copyright)给出 [如下](https://www.cs.tufts.edu/~nr/noweb/#copyright)。

## 精巧的编程和精美打印