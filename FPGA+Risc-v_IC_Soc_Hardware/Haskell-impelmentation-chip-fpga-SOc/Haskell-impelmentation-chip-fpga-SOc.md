


# Haskell-implementation-chip-fpga-SoC



如何将lisp/scheme翻译成llvm IR，并通过llvm生成机器码？ - LdBeth的回答 - 知乎
https://www.zhihu.com/question/24378697/answer/589195962




话说沒人关注过 GCC MELT 嗎，直接用 Lisp like syntax 做 IR 了，除此之外还能直接用來写 pass 和 plugin。虽然 2017 年項目挂了。(原因似乎是因爲缺钱)

主要的问题是沒人给 LLVM 写 binding。

直接写 emitter 的话 "LLVM IR has weird nesting rules to be honest"。似乎就连 Haskell 也是要用 LLVM binding 做 Code gen。说明 LLVM IR 吹得再爆，也不见得比直接生成 x86 汇编简单。

结论是大家都说好，结果沒有多少人 really motivated。當然这和社区相对较小有关。但更明显的是，能用 Lisp 就行的事为什么要 fuc$ with C/C++/JSON/⋯⋯

编译到靜态类型不是很难，Kyoto Common Lisp 系就是。

Clasp 这个被科学计算需求驱动的項目用的编译器前端是 Cleavir 。IR Gen 用 C++ 写的。目前來讲 benchmark 还比不上 SBCL 和 CCL，不過一直有显著提升。堪比 Chromium 的编译时间让人望而却步：CCL 不到一分就能自举。



顺带 StackOverflow 里面那个提到 GC 并不是说和生成 LLVM IR 有关，而是说 C foreign function call 需要在一个 GC 语言里手动管理内存（废话）不符合直觉之类的，意思是反驳题目中用 LLVM 能让 CFFI 实现得更简单的观点。当然 Lisp 实现 CFFI 本身就不是多难的事，能通过 LLVM 交互 C++/Haskell 这些 ABI 不稳定的才是最主要的好处。



# Haskell on a Xilinx FPGA



https://clash-lang.org/

CλaSH is a neat cross compiler from Haskell to VHDL, Verilog and SystemVerilog. Most examples were tested on an Altera FPGA (the DE0-Nano), and not Xilinx (the other major FPGA producer). This blog post demonstrates the procedure for getting Haskell code running on a Xilinx FPGA, which is as (relatively) straightforward as the Altera versions.




Retrocomputing with Clash: Haskell for FPGA Hardware Design (book)
retrocla.sh





# haskell-to-hardware-via-cccs

conal.net/blog/posts/haskell-to-hardware-via-cccs

将 lambda 表达式转换为 CCC 形式。
优化 CCC 表达式。
插入 GHC，将 Haskell 源代码转换为 CCC。
本翻译的应用，包括以下内容：
电路
时序分析
严格性/需求分析
类型简化（规范化）去年秋天以来，我一直在Tabula工作，这是一家硅谷初创公司，开发一种名为“Spacetime”的创新可编程硬件架构，有点类似于 FPGA，但更灵活、更高效。2011 年 2 月，我在湾区 Haskell 黑客松上遇到了创始人 Steve Teig。他描述了他的时空架构，该架构基于同名几何学，由 Hermann Minkowski 开发，以优雅地捕捉爱因斯坦的狭义相对论。在听到史蒂夫在做什么的前 30 秒左右，我知道我想帮忙。

Steve 与我分享的愿景不仅包括为硬件设计人员提供更好的替代方案（使用 Verilog 和 VHDL 等硬件语言进行编程），还包括一个用于大规模并行执行以纯函数式语言编写的软件的平台。最近，我主要研究后一方面，特别是如何编译 Haskell 的问题。我们的计划是公开开发 Haskell 编译器并鼓励合作。如果您在本博客系列中看到的任何内容对您感兴趣，尤其是如果您有任何建议或想在该项目上进行合作，请告诉我。

在我的下一系列博客文章中，我将描述一些我一直在使用的用于编译 Haskell 以实现大规模并行执行的技术理念。现在，我想介绍一个我用来解决问题的中心思想。


Lambda 演算和**笛卡尔封闭范畴**ccc



我习惯于将类型化的 lambda 演算视为描述函数和其他数学值的语言。例如，如果表达式的类型e是Bool → Bool，则 的含义e是从布尔值到布尔值的函数。（在像 Haskell 这样的非严格纯语言中，两种布尔类型都包括⊥。在假设的纯严格语言中，范围扩展到 include ⊥，但域不是。）

但是，还有其他方法可以解释类型化的 lambda 演算。

您可能听说过“笛卡尔封闭类别”（CCC）。CCC 是一个具有相关法律的小词汇表的抽象：

“类别”部分意味着我们有一个“态射”（或“箭头”）的概念，每个都有一个域和共域“对象”。结合组合算子有恒等态射。如果态射和对象的这种描述听起来像函数和类型（或集合），那是因为函数和类型就是一个例子，其中id和(∘)。
“笛卡尔”部分意味着我们有产品，具有投影函数和一个运算符，将两个函数组合成一个对产生函数。对于 Haskell 函数，这些操作是fstand snd，以及(&&&)from Control.Arrow。
“封闭”部分意味着我们有一种通过对象表示态射的方法，称为“指数”。对应的运算是curry、uncurry和apply。由于 Haskell 是一种高阶语言，这些指数对象只是（第一类）函数。
CCC 接口的一个奇妙之处在于它足以翻译任何 lambda 表达式，正如 Joachim Lambek 所发现的那样。换句话说，lambda 表达式可以系统地翻译成 CCC 词汇表。因此，对该词汇的任何（守法）解释都是对 lambda 演算的解释。

除了求知欲之外，为什么人们会关心用 CCC 来解释 lambda 表达式，而不是我们通常认为的函数式程序呢？我之所以感兴趣，是因为我一直在考虑如何将 Haskell 程序编译为“电路”，包括标准的静态类型和更动态的变体。由于 Haskell 是一个类型化的 lambda 演算，如果我们可以将电路表示为 CCC，我们将拥有我们的 Haskell-to-circuit 编译器。其他解释可以分析时间和需求传播（包括严格性）。Conal Elliott » From Haskell to hardware via cartesian ...

-----------------------------------------------------------------------------------------------------------


 http://www.megacz.com/berkeley/garrows/ GArrows ( http://www.cs.berkeley.edu/~megacz/garrows/ )，它实现了将 Haskell 术语翻译成箭头语言的 GHC pass，但如果没有，您可能会发现该链接很有用。
 
http://clash.ewi.utwente.nl/ClaSH/Home.html










































































































































































































































