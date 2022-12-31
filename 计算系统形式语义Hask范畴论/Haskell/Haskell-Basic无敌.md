


type 作为关键字用来给类型起别名，作为术语表示类型
data 作为关键字用来新建数据类型
newtype 作为关键字用来重新实现原类型
kind 类型的类型
typeclass 类型类（类似于trait或interface）




单行注释: --

多行注释 {- -}

多行注释还可以声明一些GHCi扩展，比如：

```haskell
{-#LANGUAGE OverloadedStrings#-}

{-#LANGUAGE QuasiQuotes#-}

{-#LANGUAGE TemplateHaskell#-}

{-#LANGUAGE TypeFamilies#-}

```
以下是另一种写法

{-# OPTIONS_GHC -XTypeFamilies -XTemplateHaskell -XQuasiQuotes #-}

在GHCI控制台情况下要使用扩展，可以使用:set命令:


https://aducode.github.io/posts/2015-07-02/learn_haskell_lession1.html

```hs
Prelude>:set -XOverloadedStrings
Prelude>:set -XQuasiQuotes
Prelude>:set -XTemplateHaskell
Prelude>:set -XTypeFamilies
```

或者在启动GHCi的时候加上-X


```hs
ghci -XOverloadedStrings -X TemplateHaskell -ddump-splices
# 1. If you want to see the expansion of splices, 
# 2. use the flag -ddump-splices when starting GHCi

```
关于扩展的资料详见24 Days of GHC Extensions



```haskell
$ cat tmp/functions.hs 
function3 :: Int -> [Int]
function3 x = [a | a <- [1..x], mod a x == 0]

$ ghci
GHCi, version 8.0.1: http://www.haskell.org/ghc/  :? for help
Prelude> :l tmp/functions.hs 
[1 of 1] Compiling Main             ( tmp/functions.hs, interpreted )
Ok, modules loaded: Main.
*Main> :t function3 
function3 :: Int -> [Int]
*Main> 
```


--split [1 .. 10] [] []



```haskell
:{
add1 a = (+) a 1
add1 :: Num a => a -> a
:}
```
教程

https://slides.com/fp-ctd

https://haskell.mooc.fi/

本地文件

D:\Program Files\Haskell Platform\8.6.5\lib

C:\ProgramData\chocolatey\lib\ghc\tools\ghc-8.10.2\lib

[file:///D:/Program%20Files/Haskell%20Platform/8.6.5/doc/html/index.html](file:///D:/Program%20Files/Haskell%20Platform/8.6.5/doc/html/index.html
)


[file:///D:/Program%20Files/Haskell%20Platform/8.6.5/doc/html/libraries/index.html](file:///D:/Program%20Files/Haskell%20Platform/8.6.5/doc/html/libraries/index.html)


Allin https://downloads.haskell.org/



https://downloads.haskell.org/~ghc/6.10.1/docs/html/

https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/


http://dev.stephendiehl.com/hask/#basics **这教程无敌**

高级课程 https://www.cis.upenn.edu/~cis552/current/resources.html

 Haskell编程语言
、https://www.liaoxuefeng.com/article/00154755631869315a51131478a4ce8b4bb69bc0d35a1e1000




https://www.zhihu.com/question/61301947/answer/632138904

https://zhuanlan.zhihu.com/p/47897608







haskell语言兴亡
https://blog.csdn.net/g9yuayon/article/details/1713549


```
Commands available from the prompt:

   <statement>                 evaluate/run <statement>
   :                           repeat last command
   :{\n ..lines.. \n:}\n       multiline command
   :add [*]<module> ...        add module(s) to the current target set
   :browse[!] [[*]<mod>]       display the names defined by module <mod>
                               (!: more details; *: all top-level names)
   :cd <dir>                   change directory to <dir>
   :cmd <expr>                 run the commands returned by <expr>::IO String
   :complete <dom> [<rng>] <s> list completions for partial input string
   :ctags[!] [<file>]          create tags file <file> for Vi (default: "tags")
                               (!: use regex instead of line number)
   :def <cmd> <expr>           define command :<cmd> (later defined command has
                               precedence, ::<cmd> is always a builtin command)
   :doc <name>                 display docs for the given name (experimental)
   :edit <file>                edit file
   :edit                       edit last module
   :etags [<file>]             create tags file <file> for Emacs (default: "TAGS")
   :help, :?                   display this list of commands
   :info[!] [<name> ...]       display information about the given names
                               (!: do not filter instances)
   :issafe [<mod>]             display safe haskell information of module <mod>
   :kind[!] <type>             show the kind of <type>
                               (!: also print the normalised type)
   :load[!] [*]<module> ...    load module(s) and their dependents
                               (!: defer type errors)
   :main [<arguments> ...]     run the main function with the given arguments
   :module [+/-] [*]<mod> ...  set the context for expression evaluation
   :quit                       exit GHCi
   :reload[!]                  reload the current module set
                               (!: defer type errors)
   :run function [<arguments> ...] run the function with the given arguments
   :script <file>              run the script <file>
   :type <expr>                show the type of <expr>
   :type +d <expr>             show the type of <expr>, defaulting type variables
   :type +v <expr>             show the type of <expr>, with its specified tyvars
   :unadd <module> ...         remove module(s) from the current target set
   :undef <cmd>                undefine user-defined command :<cmd>
   :!<command>                 run the shell command <command>

 -- Commands for debugging:

   :abandon                    at a breakpoint, abandon current computation
   :back [<n>]                 go back in the history N steps (after :trace)
   :break [<mod>] <l> [<col>]  set a breakpoint at the specified location
   :break <name>               set a breakpoint on the specified function
   :continue                   resume after a breakpoint
   :delete <number>            delete the specified breakpoint
   :delete *                   delete all breakpoints
   :force <expr>               print <expr>, forcing unevaluated parts
   :forward [<n>]              go forward in the history N step s(after :back)
   :history [<n>]              after :trace, show the execution history
   :list                       show the source code around current breakpoint
   :list <identifier>          show the source code for <identifier>
   :list [<module>] <line>     show the source code around line number <line>
   :print [<name> ...]         show a value without forcing its computation
   :sprint [<name> ...]        simplified version of :print
   :step                       single-step after stopping at a breakpoint
   :step <expr>                single-step into <expr>
   :steplocal                  single-step within the current top-level binding
   :stepmodule                 single-step restricted to the current module
   :trace                      trace after stopping at a breakpoint
   :trace <expr>               evaluate <expr> with tracing on (see :history)

 -- Commands for changing settings:

   :set <option> ...           set options

   :seti <option> ...          set options for interactive evaluation only
   :set args <arg> ...         set the arguments returned by System.getArgs
   :set prog <progname>        set the value returned by System.getProgName
   :set prompt <prompt>        set the prompt used in GHCi
   :set prompt-cont <prompt>   set the continuation prompt used in GHCi
   :set prompt-function <expr> set the function to handle the prompt
   :set prompt-cont-function <expr>set the function to handle the continuation prompt
   :set editor <cmd>           set the command used for :edit
   :set stop [<n>] <cmd>       set the command to run when a breakpoint is hit
   :unset <option> ...         unset options

  Options for ':set' and ':unset':

    +m            allow multiline commands
    +r            revert top-level expressions after each evaluation
    +s            print timing/memory stats after each evaluation
    +t            print type after evaluation
    +c            collect type/location info after loading modules
    -<flags>      most GHC command line flags can also be set here
                         (eg. -v2, -XFlexibleInstances, etc.)
                    for GHCi-specific flags, see User's Guide,
                    Flag reference, Interactive-mode options

 -- Commands for displaying information:

   :show bindings              show the current bindings made at the prompt
   :show breaks                show the active breakpoints
   :show context               show the breakpoint context
   :show imports               show the current imports
   :show linker                show current linker state
   :show modules               show the currently loaded modules
   :show packages              show the currently active package flags
   :show paths                 show the currently active search paths
   :show language              show the currently active language flags
   :show targets               show the current set of targets
   :show <setting>             show value of <setting>, which is one of
                                  [args, prog, editor, stop]
   :showi language             show language flags for interactive evaluation

```



资源
软件
Glorious Glasgow Haskell编译系统（GHC）版本8.8.3。有关安装GHC，VS代码IDE和相关工具的信息，请参见我们的GHC设置说明。

版本控制。您将需要使用git版本控制系统来共同完成家庭作业。我们已准备好安装说明，以帮助您入门。

参考
Haskell.org。Haskell开源社区的顶层页面。

寻找功能但不知道它叫什么吗？是否想查看特定功能的文档？Hoogle搜索许多标准库，并且可以按名称或类型进行搜索。

标准库文档。

Stackage是Haskell库的精选集合，可以保证可以协同工作，可以通过该stack工具进行访问。

黑客是Haskell软件包的巨大仓库。
可以使用cabal-install工具从Hackage自动下载并安装软件包。

我希望我在学习Haskell时所学的知识能使您超越CIS 552，但是对于Haskell生态系统是一个很好的参考。

阅读（在线免费）
向您了解Haskell的伟大成就！是一个异想天开且易于遵循的Haskell教程，其中包含超棒的插图。

真实世界的Haskell，由Bryan O'Sullivan，Don Stewart和John Goerzen撰写，由O'Reilly出版。对Haskell的详尽而详尽的介绍，深入探讨了在“现实世界”中有效使用Haskell的本质。可以免费在线阅读或以枯树形式阅读。

Haskell学校通过高级Haskell程序员为初学者提供教程。

阅读（推荐书籍）
在Haskell中进行编程，第二版。Haskell教育硕士Graham Hutton最近更新了他的教科书。它以柔和的方式开始，并以清晰和优雅的方式覆盖了此类的核心材料。

Haskell中的并行和并发编程描述了功能编程在多线程和多核体系结构中的重要性。

Haskell入门：基于项目的方法新教科书---包括对现代高级功能的处理。

观看
Haskell eXchange会议提供针对高级Haskell从业人员的演讲和教程。查看2016年，2015年，2014年，2013年和2012年的技能广播。

西蒙佩顿琼斯的讲座“课程，吉姆，而不是我们所知道它们”从2013年OPLSS视频是在 3个 部分。也可以使用幻灯片。

帮助/社区


我们将在Piazza上回答您的所有问题。别害羞

函数式编程松弛为许多fp语言（包括Haskell）提供了松弛通道。

tryhaskell.org在浏览器中为您提供了ghci会话，并包括一个非常简单的教程。它还具有到#haskell IRC通道的接口。

该#haskell IRC频道是一个伟大的地方，以获得帮助。如果您曾经在其他IRC频道中度过，这似乎很奇怪，＃haskell总是充满友好，乐于助人的人。

该哈斯克尔-初学者邮件列表是一个很好的地方，要求初学者级别的问题。

该哈斯克尔咖啡厅的邮件列表也可以是一个很好的地方要问的问题，但很多的流量更高。

Planet Haskell汇总了Haskell社区的博客文章。

有一个Haskell subreddit，用于汇总与Haskell相关的网站，博客文章和新闻。


https://functionalprogramming.slack.com (numerous FP channels on there and a number of great Haskell ones)
Are there popular conferences for Haskell? (If so, what are some examples?)

http://www.lambdadays.org
http://lambdaconf.us
Are there popular newsletters for Haskell?

https://haskellweekly.news




Reddit: https://www.reddit.com/r/haskell/

University courses (freely available):

NICTA: https://github.com/SystemFw/NICTA-Haskell-course
Data62 Functional Programming Course (Formerly NICTA): https://github.com/data61/fp-course
CIS 194: Introduction to Haskell (2016): https://www.seas.upenn.edu/~cis194/fall16/
IRC: freenode: #159
All things haskell: https://wiki.haskell.org/Haskell

Microsoft employs Simon Peyton-Jones as a researcher; he's one of the founders of the language.

Facebook employs Simon Marlow; key developer of the GHC (compiler for Haskell)

Haskell community information: https://haskell-lang.org/community



“Monad提供了一种对函数计算过程的通用抽象机制，关键是统一形式，统一操作模式，统一概念集合, 复用代码”，“一些程序语言会提供语法糖来方便编写”。 






