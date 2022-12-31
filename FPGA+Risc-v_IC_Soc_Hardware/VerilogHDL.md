

# verilog HDL
https://hdlbits.01xz.net/wiki/Main_Page HDLBits

verilog有符号数的计算

https://www.cnblogs.com/zhongguo135/p/9600144.html






[置顶]想学VHDL的同学可以下载这个文档，是我自己根据网上的内容整理的笔记。
链接：https://pan.baidu.com/s/1gRXiik9p5onDtP_7l5TUIA  提取码：2333 
fpga verilog
进阶版要自己看书咯同学，https://www.runoob.com/w3cnote/verilog-tutorial.html推荐这个专栏






如何学习verilog HDL? - wizard的回答 - 知乎
https://www.zhihu.com/question/57676593/answer/2352533700


https://www.runoob.com/w3cnote/verilog-tutorial.html






IC设计经典书籍
https://blog.csdn.net/limanjihe/article/details/52674827

 




HDLBits: 在线学习Verilog(Problem 127-130) - 真垃圾的文章 - 知乎
https://zhuanlan.zhihu.com/p/135987493






正版新书 Verilog HDL与FPGA数字系统设计 第2版 电子信息类教材













# Verilog

作者：跌宕的月光  
链接：https://www.zhihu.com/question/23732223/answer/26178381  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

eda技术包含的含义太多了，芯片的前端(verilog, vhdl等rtl, 仿真验证等等)还有后端(布局布线啊等等)，甚至研究综合布局布线等软件算法也都跟eda相关。

不过看你的意思，应该是指想学习verilog这个层面的，比较偏向于前端。

那么就得回答怎么样才能成为一个比较精进的前端工程师。

首先学习verilog HDL方面，一定要知道HDL和c/c++ java等软件语言的不同。HDL是hardware description language也就是硬件描述语言；再看看c，叫c/c++ programming language，程序设计语言。那verilog为什么不叫硬件设计语言呢？这是因为两种语言在思路上有很大不同，你用verilog的时候，其实是在描述一个数字电路，包括组合逻辑电路和时序逻辑电路；而c/c++是在指导计算机以一定过程执行指令，或者一些更好层次的抽象，例如对象啊等等。既然是这样，学好verilog的基础是，学好数字电路，其中最最主要的，是要弄清楚组合逻辑电路和时序逻辑电路，这是最基本最基本的了。然后学学verilog的语法。这个意思也就是，如何用verilog描述一个组合电路，如何用verilog描述一个时序电路，如何描述一个状态机？这是非常非常具体而基本的问题，你肯定能找到答案的当你写出一个模块，基本就知道综合器大概会综合成什么样子之后，你的前端功力算是入了一点点门。

之后要更精进的话，一般是两个方向，算法和架构。  
算法在于你要有稍好的数学基础，了解算法。更重要的是，要知道有哪些重要的算法结构，例如怎么用verilog很高效的实现一个循环？什么是流水线？如何给流水线定级？建议这方面可以看看xilinx的high level synthesis手册，看看有哪些基本的算法实现结构。

架构类的就是对整个设计，要么是一个芯片，要么是一个fpga设计，对他们整体设计方案、性能参数等等进行确定，相当于总体把关的一个角色。这个对人的整体水平要求很高的。

另外还有验证方面，有一套验证方法学。

上边这些东西，都是和你的专业和项目经历相关的。算法和算法是不同的，架构和架构是不同的，经过慢慢的积累，你就可以形成自己的竞争力。这些东西都要实际去做去实践的，工作中，平时业余爱好中。比方你是做通信方面，你可以整整通信的一些算法啊；图像方面的，你可以做做图像处理的流水线啊，架构方面，可以先从一些小的、通用的开始，比方说DDR控制器啊神马的，自己去找去发现。

还可以找一些实习，接触实际项目，接触实际的需求。

其实你看，verilog神马的，就是一个工具，进阶的都是对一个功能，一个系统有深刻的理解和把握，然后用verilog实现。verilog无非是一个工具而已。就像锤子和凿子一样，是个工具，学会一个工具很简单，但是能用锤子和凿子敲打出一个板凳和敲打出一个美丽的雕塑，甚至敲打出一个木屋，层次和境界都是不一样的。

如何从零开始学精EDA技术（Verilog-HDL ）? - 跌宕的月光的回答 - 知乎
https://www.zhihu.com/question/23732223/answer/26178381

STEP小脚丫系列是为初学者打造的一个FPGA入门平台，即使没有数字电路的基础和可编程逻辑的知识也能在很短时间内掌握FPGA的应用设计。如果你想开始学习可编程逻辑设计，STEP小脚丫系列无疑是一个非常酷又好玩的平台，你还可以基于STEP小脚丫做二次开发，做出属于自己的创意项目。







https://www.stepfpga.com/doc/verilog













https://hdlbits.01xz.net/wiki/Main_Page


www.verilog.com





https://zhuanlan.zhihu.com/p/56646479






# VHDL




Verilog HDL与VHDL各自的优缺点是什么？ - Wang Kellen的回答 - 知乎
https://www.zhihu.com/question/27587418/answer/72063600

IC设计语言跟软件语言不同，心中要先有电路才能下手，否则写出来的代码无论什么语言都不可能实现为电路。IC设计语言最忌讳学软狗钻语法的空子，因为只有最标准常规的编程风格才能保证电路的可综合性。具体来说，每一个always块，你要先想好希望得到的是什么样的逻辑，如果是组合逻辑应该怎么写，如果是latch应该怎么写（尽量别用这种方式写latch，标准单元例化才靠谱），如果是异步复位寄存器/同步复位寄存器/异步复位+置位寄存器怎么写，芯片所采用的工艺库标准单元是否能支撑你想要生成的这种电路，寄存器的逻辑怎么写，最后最后，管他什么语言，照着标准代码风格写出来就行了（不按标准写综合工具分分钟不知道你想设计的是什么鬼电路）。关于代码风格我之前有博客介绍，长期更新：[What is Good Verilog Coding Style](https://link.zhihu.com/?target=http%3A//kellen.wang/what-is-good-verilog-coding-style/)



























