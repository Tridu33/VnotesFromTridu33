# VHDL




Verilog HDL与VHDL各自的优缺点是什么？ - Wang Kellen的回答 - 知乎
https://www.zhihu.com/question/27587418/answer/72063600

IC设计语言跟软件语言不同，心中要先有电路才能下手，否则写出来的代码无论什么语言都不可能实现为电路。IC设计语言最忌讳学软狗钻语法的空子，因为只有最标准常规的编程风格才能保证电路的可综合性。具体来说，每一个always块，你要先想好希望得到的是什么样的逻辑，如果是组合逻辑应该怎么写，如果是latch应该怎么写（尽量别用这种方式写latch，标准单元例化才靠谱），如果是异步复位寄存器/同步复位寄存器/异步复位+置位寄存器怎么写，芯片所采用的工艺库标准单元是否能支撑你想要生成的这种电路，寄存器的逻辑怎么写，最后最后，管他什么语言，照着标准代码风格写出来就行了（不按标准写综合工具分分钟不知道你想设计的是什么鬼电路）。关于代码风格我之前有博客介绍，长期更新：[What is Good Verilog Coding Style](https://link.zhihu.com/?target=http%3A//kellen.wang/what-is-good-verilog-coding-style/)











