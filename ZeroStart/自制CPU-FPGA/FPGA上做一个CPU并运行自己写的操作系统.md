fpga模拟设计实现自制编写cpu








Build your own RISC-V architecture on FPGA - ModernHackers.com
modernhackers.com/build-your-own-risc-v-architecture-on-fpga







# FPGA上做一个CPU并运行自己写的操作系统





















自己动手设计一个FPGA上可运行的简易CPU及汇编器_Tony ...
https://blog.csdn.net/u012151773/article/details/90749559
https://gitee.com/jianfengtony/risc_t16
设计一款RISC CPU，总线符合哈佛结构，能够在FPGA上进行综合实现。
程序和数据存储器能够利用FPGA上的片上资源。
能够使用汇编进行程序设计，支持的程序架构满足基本的顺序运行和分支跳转，不追求满足程序的通用性和复杂性。
对程序的规模和数据的存储空间不求大，重点集中在可以高性能的进行数学和逻辑运算。
大部分指令是16位设计，部分指令支持32位运算以提高整数运算效率。
占用资源一定要少，目标是FPGA上有多少硬件乘法器以及Block RAM，就可以放下相匹配个数的CPU核心，以方便构建更加复杂的多核心并行计算系统或者流水线计算系统。
寄存器是16位宽，可以支持按照32位的组合方式访问，提高数学运算的便利性和效率。
系统支持的指令集可以根据编写的汇编代码自动生成配置文件，不使用的指令在实际系统中综合时候可以不综合，进一步缩小资源占用。




本科阶段能在FPGA上做一个CPU并运行自己写的操作系统算什么水平？ - 路边的小溪的回答 - 知乎
https://www.zhihu.com/question/377489812/answer/2081849125


重庆邮电大学 潘星雨


https://github.com/RV-AT



https://gitee.com/rpg-7/vostok564








