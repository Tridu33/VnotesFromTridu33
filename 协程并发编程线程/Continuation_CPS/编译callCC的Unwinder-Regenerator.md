# 编译callCC的Unwinder-Regenerator



http://facebook.github.io/regenerator/



Prettier 作者 James Long 早些年开发网页游戏编辑器时曾打算制作一款交互式代码调试工具，种种尝试之后，他在友人的指导下学习了 Exceptional Continuations in JavaScript 论文中介绍的高性能方法，并基于当时 Facebook 刚刚开源不久的编译 generator 利器 Regenerator，开发了 Unwinder 来编译 callCC，同时还提供了一个运行时以及实时在线 debug 工具。



---





Yassine Elouafi 在系列文章 Algebraic Effects in JavaScript https://dev.to/yelouafi/algebraic-effects-in-javascript-part-1---continuations-and-control-transfer-3g88 中系统性地介绍了 Continuation、CPS、使用 Generator 改造 CPS 并实现 callCC、进一步支持 Delimited Continuation 以及最终支持 Algebraic Effects 等内容，行文顺畅，内容示例夯实，是研究 JS Continuation 上乘的参考资料。


