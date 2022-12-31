本群推荐安装教程：

1. https://bitbili.net/gentoo-linux-installation-and-usage-tutorial.html

2. https://www.yafa.moe/post/install-gentoo-on-mac/

3. https://litterhougelangley.life/blog/2021/05/21/gentoo/

4. https://blox.bugsur.xyz/gentoo-handbook-installation/

现在虚拟机内部，安装明白了再到实体机上安装





https://www.gentoo.org.cn/



# gentoo linux


gentoo是所有包都是源码包编译安装，根据硬件自动优化，性能上有一点优势，缺点是编译时间长；


Gentoo,从入门到入土 - eralmtice的文章 - 知乎
https://zhuanlan.zhihu.com/p/140010485











虚拟机开始安装gentoo学会再安装真机
GitHub - oddlama/gentoo-install: A gentoo installer with a ...
https://github.com/oddlama/gentoo-install

GitHub - sergibarroso/gentoo_install: This file is a step ...
https://github.com/sergibarroso/gentoo_install





----------------
为什么 Linux 在桌面会失败？ - silaoA的回答 - 知乎
https://www.zhihu.com/question/20706966/answer/1034986483



bsd和linux都是开源的、各有千秋、、稳定行来说，也相差无几的、、只是linux的发行版比较乱，良莠不齐，很多发行版的确很不稳定的、、bsd是一个整套的、、所以不像linux那么多发行版比较乱、、、用linux的话，企业版：rhel，suse。免费用centos，opensuse（长期支持版），debian都可以的、、ubuntu只用核心也不错。

linux发行版个人推荐suse系列、、yast无敌、、、

话说bsd的驱动比linux更郁闷、、、




 Gentoo的前世今生 (完成版※）https://blog.csdn.net/iteye_13562/article/details/81527246
 
What is Gentoo?   Gentoo is a free operating system based on either Linux or FreeBSD that can be automatically optimized and customized for just about any application or need.

用了快两年的gentoo,感觉很棒,gentoo的心脏portage借鉴了ports做出来的,很强大易用
说区别这种中,最大的就是  gentoo linux 是基于linux内核的,我现在笔记本上的FreeBSD上还chroot跑了一个gentoo-bsd
现在初学FreeBSD, 只懂ports里基本的东西 , 在对两个系统都不熟的情况不敢乱评论,总之,都是好东西 
用好一个就不错了,有时间的话两个都学学吧,嘿嘿




https://www.zhihu.com/answer/20930693
Gentoo: 源码仓库，也提供野包（overlay），数量上绝不输Arch，而且因为定制性极强的USE变量使其灵活性远超Arch，相应的缺点就是软件安装速度太慢，尤其是一些大型软件比如内核、LibreOffice、Chromium等。为了缓解这个问题官方也同时提供了这类包的二进制版，当然是以损失定制能力为代价。

Gentoo的软件树称为Portage，对应的包管理器是emerge，包元文件称为ebuild，Portage相当于Arch里的ABS，emerge相当于Arch里的abs, pacman、makepkg等的集合，而ebuild相当于Arch里的PKGBUILD。在从源码生成安装的角度来讲两者没有明显的优劣之分。甚至两者都可以通过包元文件使用其他发行版提供的二进制包（rpm, deb等）进行安装。Gentoo有一个特别的概念是“slot”，可以让同一软件的不同版本共存，比如gstreamer:1.0和gstreamer:0.10而Arch里只能确定一个主版本，其他的版本只能通过创建不同名的包来解决，比如gstreamer和gstreamer0.10。这方面Gentoo更占优势。

关于USE我多说一句，从依赖的角度来讲，USE变量相当于更微观的“包”，USE有全局的和针对特定包的，前者影响着后者，通过USE变量你可以选择整个系统或某个包具备的特性和功能，全局USE可能会影响到多个包。USE之间也有依赖和冲突关系，包间的依赖和USE间的依赖共同构成了Gentoo包管理问题的核心。

