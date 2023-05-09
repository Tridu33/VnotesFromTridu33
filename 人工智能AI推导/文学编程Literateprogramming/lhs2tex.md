[TOC]



# lhs2tex


Hackage上面有

```
cabal lhs2tex
cabal install regex-posix
stack ghci --package regex-posix
ghc-pkg find-module Text.Read
```

github.com/kosmikus/lhs2tex

wiki.haskell.org/Literate_programming


所有以开头的行`>`均被解释为代码，其他所有行均视为注释。另外一项要求是，您始终在代码块之前和之后留空行：








**本节书摘来自异步社区《Haskell函数式编程入门》一书中的第1章，第1.4节.hs和.lhs文件、注释与库函数，作者 张淞，更多章节内容可以访问云栖社区“异步社区”公众号查看**

**1.4 .hs和.lhs文件、注释与库函数**  
GHCi和Hugs可以解析扩展名为.hs和.lhs的文件。两者所写程序在语法上完全相同，它们的差别是.lhs（literate Haskell script）文件是为了能让Haskell的代码生成文档。有效程序代码可以用“大于号（>）”和空格开头。比如：

> add :: Int -> Int -> Int  
> add x y = x + y  
> 不以大于号和空格开头的内容将被视作注释处理，且注释与代码间必须有一行以上的间隔。还有一些.lhs代码文件中的代码以begin{code}以end{code}结尾—如果.lhs文件遵守一定的格式，就可以使用lhs2tex生成非常精美的文档以供人们阅读。如何使用读者可以参阅[http://www.andresloeh.de/lhs2tex/](http://www.andresloeh.de/lhs2tex/?spm=a2c6h.12873639.0.0.298f7b466301Kp)。

使用.lhs文件书写代码的优点很明显。函数式编程的代码往往蕴含了编写者很大的思考量，需要用大段的注释进行解释说明，而代码又不是特别长，这个时候用.lhs最好不过了—哪部分是代码、哪部分是注释一目了然，还能生成.pdf文件方便阅读与传播。

但是，当不需要多行注释还有生成文档的时候就可以用扩展名为.hs的文件。.hs文件里全局的函数要起头写，不可以有其他字符；单行的注释用两个减号（--）开头，多行注释用“{-”开头，以“-}”结尾。全书对编写的函数有非常多的阐述与解释，并不包括在源代码中，所以用.hs文件就可以了。有时需要在文件头处对GHC与GHCi声明一些编译器参数，此时需要在文件首处定义，并且以“{-#”开头，用“#-}”结尾。在后面的章节中，再具体学习使用编译器参数。

在启动GHCi的时候，Prelude中的一些预加载函数已经被导入了。Prelude里有很多常用的函数以及数据。安装hugs的读者可以到C:Program FilesWinHugspackages hugsbase Hugs下找到Prelude.hs库函数文件，有兴趣的读者可以打开prelude或其他文件浏览代码。使用GHCi的读者可以在开始菜单的程序中找到Haskell的网页文档，打开Library链接，找到Prelude，再点击source查看。读者可以通过查看这些源文件来感受Haskell程序的风格。

Haskell的函数库是非常强大的。在发展的多年过程中，有很多库可供用户直接使用，也有像Java一样的API可以查阅。WinGHCi的用户一样可以在开始菜单程序中网页文档中找到,也可以在[http://www.haskell.org/ghc/docs/latest/html/libraries](http://www.haskell.org/ghc/docs/latest/html/libraries)在线浏览。第4章将会对几个库函数使用做简要的介绍。















































