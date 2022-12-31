如何看待开源指令集RISC-V ? - rredline的回答中有很多开发板介绍 - 知乎
https://www.zhihu.com/question/28368960/answer/157247133








# Hardware开发板


FGPA for RISC-V CPU running Linux 台湾教程
https://marconi1964.github.io/FPGA/index.html

https://marconi1964.github.io/






## fpga




“RISC-V处理器和FPGA生态环境非常匹配，在RISC-V之前，FPGA软核生态主要由各家FPGA厂商进行维护，底层代码不开源，互相之间隔离，导致用户设计无法跨平台，制约了用户对基于FPGA的处理器使用。RISC-V的开源属性，给了SoC FPGA新的选择。随着应用系统越来越复杂，未来FPGA发展一个方向是SoC FPGA，实现软硬件都可以编程，大大扩展了FPGA的应用领域。RISC-V将会在SoC FPGA生态里面发挥重要作用。





目前国内能买到的有：RVBoards-D1-哪吒，玄铁C906，699RMB。VisionFive 昉·星光，U74双核，1100RMB。PicoRio 放出了图纸。

Linux 5.7 将支持国产 RISC-V 芯片 K210 - 知乎专栏
https://zhuanlan.zhihu.com/p/132643185

RISC-V 这么火，可是能跑 Linux 的却不多，SiFive 到是有一款能运行 Linux 的开发板叫做 HiFive Unleashed，但是价格让人望而却步。K210 的 8M SARM 以及友好的价格让广大爱好者看到了希望，
https://www.zhihu.com/answer/633568110

BITK210 https://lkml.org/lkml/2020/4/8/671

iCESugar-pro 开源FPGA开发板 - muselab


## 基于FPGA实现的RISC-V开发板
可以跑Linux的RISC-V计算机、微型电脑、单板机_zoomdy's blog-CSDN博客
https://blog.csdn.net/zoomdy/article/details/108471937


 

risc-v界最近最重磅的新闻应该就是日前在上海举办的risc-v中国峰会上，中科院计算所公布了国内首个开源的通用risc-v处理器-香山。 

Perf-V：国内澎峰科技出品，基于Xilinx Artix-7系列FPGA-XC7A50T实现


SiFive针对服务器新出了一款芯片，perf-v model i 工程板是澎峰科技为risc-v开源社区设计的fpga开发板。 


蜂鸟E203是国内首个开源RISC-V处理器，从2018年发布至今，积累了广泛的用户，得到广大电子设计工程师、教师、学生和爱好者的关注与好评，且获得了中国开放指令生态联盟颁发的科教实践奖。
在全新推出的RISC-V处理器教学平台中，芯来科技对开源蜂鸟E203 SoC进行了全面升级，在保持原本工业级开发标准的同时，内容更加丰富，可扩展性更强，符合当前处理器架构往DSA（Domain Specific Architecture）发展的新趋势，能灵活的满足更多应用需求。
蜂鸟E203：国内芯来科技出品，基于Xilinx Artix-7系列FPGA-XC7A75T，可以配置为RV32IC或RV32EC架构。

小脚丫STEP开发板：国内思得普科技出品，基于Intel公司Cyclone 10系列FPGA芯片10CL016YU256C8G

小脚丫STEP-MXO2 二代FPGA开发板：基于Lattice公司MXO2系列的FPGA芯片LCMO2-4000HC-4MG132

## 基于RISC-V芯片实现的开发板

NXP VEGA织女星开发板：NXP恩智浦出品，基于NXP四核异构处理器，片上集成两个ARM内核和两个RISC-V内核，板载资源丰富。目前还买不到这块开发板和RV32M1芯片，想体验这块RISC-V板子的朋友，可以免费申请：NXP恩智浦VEGA织女星开发板免费申请！官方社区：OPEN-ISA社区

Sipeed M1(荔枝丹)开发板：基于K210 RISC-V芯片，K210是国内嘉楠耘智的团队在2018年研发出一款7nmAI芯片，采用了基于rocket-chip的双核RV64GCC RISC-V CPU。

Lichee Tang(荔枝糖)开发板：基于国产FPGA芯片EG4S20，EG4S20是国内安路科技开发
设计的FPGA芯片，20K逻辑单元，130KB SRAM。

VEGA织女星开发板分为两种，一种是国际版，一种是国内版


【1-2 	 NutShell-本科生设计的可运行Linux的RISC-V芯片 王华强-哔哩哔哩】 https://b23.tv/aOHYJGl