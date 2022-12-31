


PYNQ(ZYNQ)入门资料合集 - sazc的文章 - 知乎
https://zhuanlan.zhihu.com/p/92935984


请问ZYNQ有什么比较好的教程？ - 王天祺的回答 - 知乎
https://www.zhihu.com/question/56596019/answer/233388461


PYNQ-Z2上怎么移植RISC-V？ - 圆圆的回答 - 知乎
https://www.zhihu.com/question/357498834/answer/908969658
RISC-V在PYNQ-Z2的移植结束。


https://news.ycombinator.com/item?id=10873137
RISC-V 能在 A101040 (Epiphany III) Parallella 的板载 Xilinx Zynq 7020 FPGA 中实现




# zynq



Zynq可扩展处理平台是赛灵思新一代 FPGA的可编程技术的产品系列。与采用嵌入式处理器的FPGA不同，Zynq产品系列的处理系统不仅能在开机时启动，而且还可根据需要配置可编程逻辑。采用这种方法，软件编程模式与全功能的标准ARM处理SoC毫无二致。

与之相关和不同的是，PYNQ = Python + ZYNQ，即将ZYNQ部分功能的Python化，直接调用Python库和FPGA硬件库进行功能的开发。
ZYNQ系列——ZYNQ7000
PYNQ系列——PYNQ_z2
zynq是xilinx soc架构的fpga芯片，是zynq-7000系列的统称，包括单核cpu的fpga芯片，比如zynq-7015（带高速bank），zynq-7007，双核CPU的芯片，比如zynq-7010，zynq-7020，zynq-7035，不同之处是他们的PL部分使用的FPGA系列不同，像7010和7020的PL部分是A7的，7035以上的是K7的FPGA，还带有高速bank。可以把它想象成两部分，一部分是arm，就是我们说的PS，procesing system，处理系统，包括单核或者双核的，另一部分就是PL，programable logic，可编程逻辑，就是FPGA，PS和PL之间交互是通过AXI总线，可想而知AXI总线的重要性了吧！

PS可以做主机，也可以做从机，同样PL可以做主机，也可以做从机，非常典型的一个应用就是通过AXI DMA 去读写DDR，配置AXI DMA是通过AXI lite，PS通过MGP配置的时候主机，PL被配置时候做从机，PL通过HP结构读写DDR的时候作为主机，PS则是从机。

ug585可以说是zynq的圣经


ZYNQ用FPGA+ARM组成Soc整个开发流程从Vivado到SDK到LInux，知识范围从HDL设计到Linux内核和Dirver，即将量产的MPSoc还会出现Android的开发，再加上号称强大无比的SDSoc，在你眼前的是一片海洋大部分人不知道该怎么开始。

我的建议是从你熟悉的部分开始，然后再向未知前进。如果你英文阅读没有问题建议的起点是UG585，国内的教材基本都是对UG585的翻译和理解再加上若干实例，几乎不可能覆盖ZYNQ开发所需的知识体系范围。而UG585是一个非常好的起点，权威而且清晰，同时附录和引用中能够很好地扩展阅读，这和单独从某一本中文教程学起会很不一样。

数字电路部分：PL端基本都能实现你自己的RTL功能；
ARM软件部分：PS端有丰富周边（UART, IIC, SPI, USB, Ethernet等），CPU也很强，可以上linux。
Xilinx ZYNQ+TCP通信+Python上位机 实现实时视频传输系统 - IC设计者笔记的文章 - 知乎
https://zhuanlan.zhihu.com/p/511452931
有1+1＞2的效果，即 ZYNQ ＞FPGA+ARM ，且优越性不止一点半点。

可以先利用ZYNQ的PL端逻辑资源学习FPGA设计硬件电路，然后再学习ARM程序开发(具体包括裸机程序设计、进阶版的Linux程序开发、高阶版的Linux驱动设计)。

FPGA和ARM都入门以后就可以真正开始ZYNQ 的精髓部分学习: 软硬件协同设计。即一个系统适合硬件做的部分就写RTL，在FPGA上实现，比如实时性要求比较高的数据处理。然后把RTL封装成IP用ARM去控制。一通操作下来，简直溜到飞起。

如果再完善一些，可以开发一个Python的上位机，直接在PC控制自己的电路并实时获取FPGA的数据。下面这篇文章就是自己之前用ZYNQ做过的一个有趣的项目，涉及的知识包括：用FPGA 编写RTL实现图像传感器的实时数据采集，ARM端读取FPGA采集数据并通过TCP/IP通信发送给PC端的Python上位机。虽然涉及的内容较多，但都很容易上手，是个不错的学习项目。





