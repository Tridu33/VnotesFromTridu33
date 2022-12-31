


https://docs.racket-lang.org/index.html

# 1. Racket文档

Racket主要的工具包括

- racket，核心编译器，解释器，运行系统

- DrRecket 编程环境

- raco 命令行工具，可以用来执行Racket命令，比如安装包，构建库等等。
https://docs.racket-lang.org/raco/exe.html


```
raco pkg install sicp
```


[https://docs.racket-lang.org/](https://docs.racket-lang.org/)




使用define定义自己的函数。尽管你能在REPL里执行define，定义经常被保留并在之后使用。顶部区域-叫做定义区-并使用#lang作为前缀

```scheme
#lang racket
(define (extract str)
(substring str 4 7))
```


保存成"extract.rkt",然后在同一目录运行racket




>(enter! "extract.rkt")
>(extract "the gal out of the city")
"gal"







一种编程语言-一种lisp方言继承自Scheme

一系列的编程语言家族-各种Racket变体

一个工具集-为了使用一个系列的编程语言家族





PLT Scheme更名为Racket，MzScheme也被整合进了Racket，所以只需要安装Racket我们就可以使用MzScheme。






https://racket-lang.org/



https://download.racket-lang.org


# Racket
https://www.zhihu.com/answer/77908199
Racket语言



荐看看： [https://github.com/racket/racket/wiki](https://link.zhihu.com/?target=https%3A//github.com/racket/racket/wiki/Intro-Projects)  
它提供了可以贡献给 Racket 的 project ideas。  
我认为用一个实际的问题来检验自己的学习成果，是很不错的。

PS：  
如果答主需要写一个偏实用的程序的话，Racket 的 [Generic Collections](https://link.zhihu.com/?target=http%3A//lexi-lambda.github.io/racket-alexis-collections/index.html) 应该可以大大简化你的代码（generic collection 的整套方案借鉴自 clojure）。

作者：Shuhan  
链接：https://www.zhihu.com/question/38741213/answer/77908199  












































# 2. DrRacket适配的Scheme






https://docs.racket-lang.org/sicp-manual/Installation.html?q=sicp


安装路径添加环境变量之后mzscheme 进入交互环境REPL

默认的路径是C:\Documents and  Settings\Administrator>


cd .. ：返回上级目录
cd 目录名 ：进入目标目录，需要注意的是当目标目录名中有空格的时候，必须要为目录名加双引号，Tab自动补全


```
#lang sicp
(inc 42)
```


















































