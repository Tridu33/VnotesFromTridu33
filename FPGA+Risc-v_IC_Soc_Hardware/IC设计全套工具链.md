![](https://pic3.zhimg.com/e5a47164b974320c0de3b2ff64ef19b7_r.jpg?source=1940ef5chttps://pic3.zhimg.com/e5a47164b974320c0de3b2ff64ef19b7_r.jpg?source=1940ef5chttps://pic3.zhimg.com/e5a47164b974320c0de3b2ff64ef19b7_r.jpg?source=1940ef5c)

IC设计从前端（比如verilog编写）到后端直至流片出来，完成这一整套流程要用到哪些具体工具？谢谢。 - Forever snow的回答 - 知乎
https://www.zhihu.com/question/23256567/answer/24077262

前端
design：vi ，nlint，lec

verify：nc ，debussy， nwave

synthesis：dc，dct/rc，rcp

sta：pt

test：dc/rc

大后端需要的工具

DC综合--synthesis

STA分析--prime time

PR实现 -- ICC

基本流程 DC - STA - PR - STA - DC 迭代

插DFT也是使用--synthesis

一般会做ECO

这样就需要RTL和netlist做formality

后端验证

calibre -- DRC LVS ERC

starrc -- 抽取寄生

totem -- IRdrop EM分析



















































