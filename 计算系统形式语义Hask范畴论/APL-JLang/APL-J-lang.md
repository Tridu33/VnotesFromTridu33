





《A programming language》开山之作
APl 速记符号 https://code.jsoftware.com/wiki/File:J602_RefCard_color_letter_current.pdf 

# APL-J-lang

即使在APL成为计算机编程语言以前，艾佛森表示法（Iverson Notation）作为一种为人们记录算法的语言是很有用的。经典的例子是新型IBM System/360计算机指令集架构的正式定义，该定义见于1965年在IBM系统期刊（IBM System Journal）上发表的由Adin Falkoff、肯·艾佛森（Ken Iverson）、及Ed Sussenguth三人合写的文章中 A. D. Falkoff, K. E. Iverson and E. H. Sussenguth, “A Formal Description of SYSTEM/360,” IBM Systems Journal, vol. 3, no. 3, pp. 198-261, 1964.
这份说明是正式的而非随口说说、而且已通过一套程序实现了、并通过公共变量（common variables）进行交互、还要与辅助表（auxiliary tables）结合使用……尽管这份正式说明是完整且自包含的，但这些内容仅作为提供的一种辅助手段，以便进行初步研究。
http://coder.zoomquiet.top/data/20121102102656/index.html 


1960年，在弗雷德里克·布鲁克斯（Frederick Brooks）的建议下，艾佛森加入了位于纽约州约克镇的IBM研究中心，而弗雷德里克·布鲁克斯在哈佛时曾做过艾佛森的助教注3，并且他那时已就职于IBM。于是二人齐心协力不断发展新表示法。终于在1962年肯出版了那本至今仍被奉为经典的《A Programming Language》[1]一书，为了便于提及该表示法，APL的名字便因该书的书名而得，而在此之前则被非正式地称为“艾弗森表示法”。



J-Lang
https://zh.wikipedia.org/wiki/J%E8%AF%AD%E8%A8%80
J语言支持**AVX2指令集进行SIMD运算**。

 高级向量扩展指令集（英语：Advanced Vector Extensions，简称AVX）是x86架构微处理器中的指令集 AVX是X86指令集的SSE延伸架构，如IA16至IA32般的把寄存器XMM 128bit提升至YMM 256bit，以增加一倍的运算效率。此架构支持了三运算指令（3-Operand Instructions），减少在编码上需要先复制才能运算的动作。在微码部分使用了LES LDS这两少用的指令作为延伸指令Prefix。
AVX2指令集将大多数整数命令操作扩展到256位，并引入了熔合乘法累积（FMA）运算。AVX-512则使用新的EVEX前缀编码将AVX指令进一步扩展到512位。Intel Xeon Scalable处理器支持AVX-512。















# 理论



《计算机语言APL及其应用》

APL is Turing-complete because it has conditionals, branching, and recursive functions. It is also Turing complete because you could code in APL a Random-Access-Machine interpreter. https://softwareengineering.stackexchange.com/questions/284735/is-apl-a-turing-complete-language


APL 最早的用途是在 IBM 內部用来描述算法和硬件。因为这时候还不是编程语言所以就画成流程图可視化。

https://rosettacode.org/wiki/Universal_Turing_machine#J  各种语言实现UTM，通用图灵机(J-Lang也行)


是否可能纯粹使用向量/矩阵变换来实现一般的编程需求？ https://github.com/Co-dfns/Co-dfns


普林斯顿大学和威斯康星大学，标题为《Looped Transformers as Programmable Computers》，旨在探索如何用 Transformer 来实现通用计算机。https://finance.sina.com.cn/tech/roll/2023-02-13/doc-imyfpshw9278724.shtml

ISA 描述了指令和操作如何由编译器编码，然后由处理器解码和执行，它是处理器架构中面向程序员的部分。常见的例子是 Intel 的 x86、ARM、IBM Power、MIPS 和 RISC-V。我们可以将 ISA 视为处理器支持所有操作的词汇表。通常，它由算术指令（如加、乘）、内存操作（加载、存储）和控制操作（例如，在 if 语句中使用的分支）组成。
单一指令计算机（英语：one instruction set computer，**OISC**）也称最简指令集计算机（ultimate reduced instruction set computer，URISC），它是一种抽象计算机，该计算机只有一条指令[1][2][3]。巧妙地选取这一条指令，并且给予无限的资源，单一指令计算机就能成为和其他多指令计算机一样的图灵机[2]:55。在教学上，这种计算机被推荐来帮助理解计算机架构[2]:2 [1]:327，同时，也能用它来研究计算机的结构模型[3]。


# 学习
https://aplcart.info/



有没有比较高效地记忆J/APL中的组合子的方法？ - LdBeth的回答 - 知乎 https://www.zhihu.com/question/32328034/answer/2116998753

https://emacs-china.org/t/apl/12628 如何学习APL
# 脑洞
https://www.realworldtech.com/forum/?threadid=205288&curpostid=205454 If APL and assembly language had a baby


用8 bit向量运算计算机雏形,
32 bit运算risc v的雏形


简单CPU设计实践（转发自Lianera文章） - 菩提无树的文章 - 知乎
https://zhuanlan.zhihu.com/p/630110525













































