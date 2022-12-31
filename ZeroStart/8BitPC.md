# 1. 8Bit PC

https://replit.com/talk/share/TinyComputer-An-8-bit-computer-with-memory-segmentation/28401
8比特计算器模拟器python

SCRIPT-8: An 8 Bit Fantasy Computer Programmed with Javascript | Hacker ...
https://news.ycombinator.com/item?id=19002226

8bit Microprocessor Using VHDL | PDF | Vhdl | Central Processing Unit
https://www.scribd.com/presentation/187233695/8bit...

8bit Microprocessor Using chisel,clash? 本质其实是yoneda局部小范畴映射为集合范畴的一组8位向量，通过抽象用8位向量实现图灵完备的一组基本底层ISA，然后不断在上面建立抽象，不断实现更高层级的用途。这就是多面体模型，抽象解释，为什么计算机的基石是逻辑的原因。因为逻辑就是*亚历山大·格罗腾迪克的*代数几何，就是微分共形几何。

【一个8位二进制CPU的设计和实现-哔哩哔哩】 https://b23.tv/6LkkO9P

>《数字电路设计及VerilogHDL实现》西安电子科技大学出版社的第七章最后一个设计实例 https://www.xduph.com/pages/BookDetail.aspx?doi=0dd39428-1ba5-4615-ad18-e2280d013f07&type=1
用Verilog实现8-bit简单计算机寄存器虚拟机的**简单模型机**设计
https://www.xduph.com/pages/BookDetail.aspx?doi=0dd39428-1ba5-4615-ad18-e2280d013f07&type=1 下载源码只有PPT没公开下载 https://wenku.baidu.com/view/89f43cc165ec102de2bd960590c69ec3d4bbdbcd.html


>基于FPGA技术的8位模型机(CPU)设计与实现 https://download.csdn.net/download/u010125178/9908609 

>FPGA模型机课程设计源代码.docx  这里是32位的付费下载 https://download.csdn.net/download/ly823260355/12657551
主要围绕设计一个完整的模型计算机展开，包括设计模型机的基本架构、数据通路、运算器、存储器、总线、通用寄存器、输入\输出端口等硬件部件，以及指令系统。指令系统可以采用MIPS 32位处理器指令格式实现。要求实现基本的Load-Store-ALU类型20条指令，在此基础上可以自行扩展需要实现的指令，包括乘除运算、条件转移、异常与中断、原子操作等指令。

>（毕设）简易8位risc CPU设计，源码，测试程序，电路图
https://www.cirmall.com/circuit/11293/

-----------------------------------

开源的优质资源有很多：

课程设计名称： 基于8位模型机的汇编指令执行模拟
https://github.com/whoisnian/AnalogCPU
课程设计概述： 在PC上通过C语言程序将汇编指令转换为二进制操作码，模拟汇编语言的编译过程，然后使用Windows的API通过串口通信将指令数据发送到FPGA开发板，开发板接收并写入数据到存储器中，最后8位模拟CPU从存储器中取数据，译码，执行指令，并显示结果。
软件： Quartus Prime Lite 18.0.0，CodeBlocks 17.12
硬件： 黑金FPGA开发板 ALINX ALTERA AX301（芯片为EP4CE6F17C8N）


用VHDL设计的8位模型机系统，包括设计实现指令系统、指令格式、寻址方式、寄存器结构、数据表示方式、存储器系统，运算器、控制器等。用VHDL硬件语言进行逻辑设计与实现
https://github.com/zhangyqCS/ModelMachine_FPGA
这个github用户还写了https://github.com/zhangyqCS/TuringMachine 利用Qt实现的简易图灵机系统（输入初始状态、终止状态和状态转移函数，判断给定的输入带是否能被图灵机接受）

ALINX ALTERA FPGA黑金开发学习板 CYCLONE IV 数电课设八位模型机 
https://github.com/HellooYing/8_bit_cpu

基于FPGA独立设计指令集实现的轻量级8位机 最高主频支持12MHz 8位GPIO接口 
https://gitee.com/nekokami0527/NEKO-8-Bits-Computer


-------------------------


Unicorn – The Ultimate CPU emulator
https://www.unicorn-engine.org

这个一个数字电路设计的verilog实现,自己逐一从基础的门电路到实现一个rsic-v的cpu的笔记
https://gitee.com/greek_man/verilog
