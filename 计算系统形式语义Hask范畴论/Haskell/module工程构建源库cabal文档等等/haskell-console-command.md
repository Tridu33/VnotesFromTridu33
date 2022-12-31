# 1. haskell-console-command











```bash

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
   :show <setting>             show value of <setting>, which is one of
                                  [args, prog, editor, stop]
   :showi language             show language flags for interactive evaluation
可从提示符获得的命令:


<声明>评估/运行<声明>

:重复最后一个命令

:{ \ n . . . .\ n:} \ n多行命令

:添加[*]<模块>…向当前目标集添加模块

:浏览![*]]显示模块定义的名称

(!:更多的细节;*所有顶级名称):

:cd

更改目录为
:cmd 运行:::IO字符串返回的命令

:完成 [] 列表完成部分输入字符串

:ctags[![]为Vi创建标签文件(默认:"tags")

(!:使用regex而不是行号)

:def define command:(后定义命令有)

优先级:始终是一个内置命令)

:编辑<文件>编辑文件

:编辑编辑模块

:etags []创建标签文件<文件>为Emacs(默认:“标签”)

::,帮助?显示此命令列表。

:信息!][<名称>…显示给定名称的信息

(!:不过滤实例)

:issafe []显示模块的安全haskell信息

:[!<类型>表示类型为<类型>

(!:亦列印标准版)

:加载!][*]<模块>…加载模块及其依赖项

(!:推迟类型错误)

:主要(<参数>…用给定的参数运行主函数。

:模块(+ / -)[*]< mod >…设置表达式求值的上下文

退出:退出GHCi

:重新加载!重新加载当前模块集

(!:推迟类型错误)

:运行函数[<参数>…使用给定的参数运行函数

:脚本运行脚本

:type 表示类型

:类型+d 显示，违约类型变量的类型。

:type +v 显示了的类型，以及其指定的tyvars

:undef undefine user-defined command:

:!<命令>运行shell命令<命令>


——命令调试:


:在断点处放弃，放弃当前计算

:返回[]返回历史n步(后:trace)

:break [] []在指定位置设置断点。

:break 在指定的函数上设置断点。

:断点续传

:delete 删除指定的断点。

:删除*删除所有断点

:force 打印，强制未评估的部件

:前进，前进，前进，前进，前进，前进在历史上向前走

:history [] after:trace，显示执行历史

列表显示当前断点周围的源代码

:列表显示的源代码

:列表[<模块>]<行>显示围绕行号<行>的源代码

:打印(<名称>…显示一个值而不强制它的计算

:sprint(<名称>…简体版:打印

:在断点处停止后的单步

:步骤单步进入

:在当前顶级绑定中逐步执行本地单步

:stepmodule仅限当前模块

:在断点处停止后的跟踪

:trace 对进行跟踪评估(见:history)


——设置更改命令:


:设置<选项>…设置选项

:seti <选项>…只为交互评估设置选项

:设置参数<参数>…设置System.getArgs返回的参数

:设置prog 设置System.getProgName返回的值。

:设置提示符<提示符>设置GHCi中使用的提示符

:设置提示符-cont 设置GHCi中使用的延续提示符

:设置提示函数设置函数来处理提示。

:设置提示-接触-函数设置函数处理延续提示

:设置编辑器设置用于:编辑的命令。

:设置stop [] 设置断点时运行的命令

:设置<选项>…设置选项


':set'和':unset'选项:


+ m允许多行命令

+r在每次计算后恢复顶级表达式

在每次评估后打印时间/内存统计

+t打印类型评估后

+ c / locat收集类型







```

