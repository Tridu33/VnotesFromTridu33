
 callCC（call with current continuation）

https://www.cnblogs.com/lsgxeva/p/10159163.html
call/cc合成所有控制结构while for.goto


模板元能实现λ-Calculus， 详见Matt Might/灼弦巨巨的TemplatePL


https://www.zhihu.com/answer/156587235


https://www.cnblogs.com/lsgxeva/p/10159181.html
call/cc


【后现代魔法小组 第一次群talk-哔哩哔哩】 https://b23.tv/BX5Lahf


https://zhuanlan.zhihu.com/p/180473795


https://zhuanlan.zhihu.com/p/111501907
用call/cc实现yield
然后yield from直到generator
最后async await协程

【原来 yield 要这样用才叫真正的协程 | Python AsyncIO 从入门到放弃05-哔哩哔哩】 https://b23.tv/cujYB0p


coroutines，fibers
与generator原理类似，但略有不同，基本上每一本scheme语言的教材都有相关的代码，可以看the scheme programming language,4th edititon,就不给代码了。https://www.cnblogs.com/lsgxeva/p/10159163.html


【后现代魔法小组 第一次群talk-哔哩哔哩】 https://b23.tv/MjbQM7C
prompt E(control (k expr))







--------------------------





[TOC]





- lisp词法作用域之后实现(upvalue+纯函数 绑定)闭包实现了进一步:

- CPS把函数调用完之后接下来要执行的代码通过闭包包裹并作为函数参数调用要执行的函数。

- lua,js的可调用对象从闭包开始，进而函数（可调用对象）也可以作为参数和返回值first class，就能实现函数式了



「CPST 就是 Gödel–Gentzen 变换的 Curry–Howard 像而已，这有什么难理解的？」



# Continuation




栈编程和函数控制流: 从 continuation 与 CPS 讲到 call/cc 与协程
https://www.cnblogs.com/rzbdz/p/15192140.html


【小程序语言讲座（9）CPS变换-哔哩哔哩】 https://b23.tv/vruJLlC



什么是「continuation」? - 圆角骑士魔理沙的回答 - 知乎
https://www.zhihu.com/question/61222322/answer/564847803

Continuation入门指南 https://thzt.github.io/2015/01/18/continuation/ 何幻

continuation实现了类似goto语句的功能，

只是goto可以跳转到任何的代码标签处开始执行，

而continuation只能跳转到执行过的工作状态。

好的编程实践指导我们尽量不要使用goto，因为它会影响求值环境，

然而，continuation不会，它更函数式，没有副作用（side effect）

怎样理解 Continuation-passing style? - Guannan Wei的回答 - 知乎
https://www.zhihu.com/question/20259086/answer/141162748


# call/cc

https://stackoverflow.com/questions/9050725/call-cc-implementation


如何解释 Lisp 中 call/cc 的概念？ - 脚趾头的回答 - 知乎
https://www.zhihu.com/question/21954238/answer/522888860

>call/cc强大的是它引入的“return”是「first-class」的（当然call/cc本身也是个函数），它不仅仅可以当做参数传来传去，装进各种数据结构里，在lisp你甚至可以配合set!造出各种各样的黑魔法。。。甚至你可以将这个“return”序列化，传送到别的机器上，然后调用这个“return”。


call/cc 和 Coroutine 分别与 continuation的关系? - Belleve的回答 - 知乎
https://www.zhihu.com/question/31191824/answer/54549793



Continuation : $\wedge \alpha.\neg \alpha$，无法居留到闭合表达式

Call/CC：$\wedge \alpha.(\neg \alpha \rightarrow \alpha)$，在经典逻辑下重言，可作为公理加入 SKI/STLC/System F……

Coroutine：Call/CC 的某种封装



#  cps（continuation-passing style ）及 cps变换
函数式编程中cps（continuation-passing style ）是什么意思？ - airtrack的回答 - 知乎
https://www.zhihu.com/question/24453254/answer/37161363

CPS把函数调用完之后,接下来要执行的代码通过**闭包**包裹并作为**函数参数**调用要执行的函数。

这几篇文章写的很好：

- Continuation Passing Style Revisited, Part OneContinuation Passing Style Revisited Part Two: Handwaving about control flow
- Continuation Passing Style Revisited Part Three: Musings about coroutines
- Continuation Passing Style Revisited Part Four: Turning yourself inside out
- Continuation Passing Style Revisited Part Five: CPS and Asynchrony









函数式编程中cps（continuation-passing style ）是什么意思？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/24453254/answer/27846244


函数式编程中cps（continuation-passing style ）及 cps变换 - someone的文章 - 知乎
https://zhuanlan.zhihu.com/p/34668011


动态作用域和词法作用域的区别就在于“函数体在什么环境中被求值”。
动态作用域中的函数，在函数调用的环境中被求值。
而词法作用域中的函数，在被定义时的环境中求值。

从实现的角度来看，闭包就是一个数据结构，
它保存了函数的参数列表，函数体和被定义时的环境，并没有什么神秘的地方。

上一篇文章中，我们还对比了闭包与对象，它们都是有内部状态的实体。
引出了我们let over lambda的优雅断言。

什么叫first-class的呢？
某个东西是first-class的，就是说这个东西可以当做函数的参数，也可以当做函数的返回值。
有了高阶函数之后，函数就是first-class的了。

有闭包就能“**传入函数/return 函数**”现在我们来看continuation变成first-class会有什么好玩的事情发生。

call-with-current-continuation

柯里化的前生今世（七）：first-class continuation - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/34064549


-------------------------------------------------------


# continuation实现原理

scheme中的continuation实现原理是什么？ - Belleve的回答 - 知乎
https://www.zhihu.com/question/22063152/answer/20537656

Continuation Implementation http://wiki.c2.com/?ContinuationImplementation
这里提及了四种：

- 在堆上分配 Activation Record
- 复制整个堆栈
- 堆栈分段化
- CPS 变换



- continuation：接下来要执行的计算；

- call/cc：call/cc是个函数，参数是个函数（假设是f），这个f有一个参数，它也是函数（假设是cc）。执行(call/cc f)时，会把当前的continuation传作为参数cc传给f，并调用f，当f中调用到cc时，执行过程就直接跳到当初调用 call/cc 的地方。正如其名：call-with-current-continuation；

- coroutine可以通过coutinuation实现。  作者：吴俊 https://www.zhihu.com/question/31191824/answer/51678148




-----------------------------------------------

# continuation的具体编程语言中的应用，协程，promise v.s. 基于栈的回调异步编程




Programming Languages: Application and Interpretation【译14】 - MrMathematica的文章 - 知乎
https://zhuanlan.zhihu.com/p/32037390

后续传递(continuation)和回调(callback)的差别 - 萧迹的文章 - 知乎
https://zhuanlan.zhihu.com/p/20713184



用continuation实现非确定计算 - 李欣宜的文章 - 知乎
https://zhuanlan.zhihu.com/p/49117340


Continuation 在 JS 中的应用 - 尚春的文章 - 知乎
https://zhuanlan.zhihu.com/p/94611888

如何用JavaScript实现一门编程语言 - Continuations - Hong的文章 - 知乎
https://zhuanlan.zhihu.com/p/460667947






> 即，continuation 是计算机程序控制状态的抽象表示。一个坊间更通俗的说法是：它代表程序的剩余部分。像 continue、break 这类控制流操作符一样，continuation 能够暴露给用户程序从而可以在恰当时机恢复执行，这种基本能力大大扩展了编程语言使用者的发挥空间，也为 excpetion handling、generators、coroutines、algebraic effects 等提供了坚实基础。

C 语言如何实现 continuation？ - sora kasugano的回答 - 知乎
https://www.zhihu.com/question/30918811/answer/50062699 PS：题主确认LUA里真的能实现Full Continuation么。似乎并没有coroutine.clone呀（魔改下LUAEngine加上copy lua_State的函数大概可以？）

如何理解Scala中的定界延续（delimited continuation）？ - 杨博的回答 - 知乎
https://www.zhihu.com/question/39116437/answer/80117466



C++模板元编程怎么在编译期实现Continuation? - 夏之幻想的回答 - 知乎
https://www.zhihu.com/question/55940343/answer/147123676


# delimited continuation比call/cc强大





Delimited Continuation有什么不能用call/cc代替的用处吗？ - Jks Liu的回答 - 知乎
https://www.zhihu.com/question/39921993/answer/83989122



如何解释 Lisp 中 call/cc 的概念？ - 脚趾头的回答 - 知乎
https://www.zhihu.com/question/21954238/answer/522888860










call/cc是Lisp、Scheme等这类语言的特有的 还是绝大多数语言都普遍具备的？ - knifefire的回答 - 知乎
https://www.zhihu.com/question/494984665/answer/2196253368

不过call/cc确实是和goto一样被证明harmful的一个玩意。
除了少数几个例子，callcc直接用就是不合适。现在流行的是delimited continuation和Algebraic Effect，callcc就像达夫设备一样只作为业余时间钻研的小技巧了。像什么用macro和callcc实现协程啥的新手任务我也做过，怎么说呢，在学习上还挺有意义的，而且比用C里面的设施做简单很多，但是不要真的拿来用比较好。实际上如果你不嫌麻烦，在支持first class function的语言里面Cont Monad一造都能用上callcc，但是属实是没收益。
 





Haskell的Cont Monad写法
指令式和函数式语言中的控制流比较 - boards flip的文章 - 知乎
https://zhuanlan.zhihu.com/p/350324914

# Continuation Passing Style CPS 的 monad
https://blog.oyanglul.us/grokking-monad/part2







Cont 是 Continuation Passing StyleCPS 的 monad，也就是说，它是包含 cps 计算 monad。

先看一下什么是 CPS，比如有一个加法

add :: Int -> Int -> Int
add = (+)
但是如果你想在算法加法后，能够继续进行一个其他的计算，那么就可以写一个 cps版本的加法

addCPS :: Int -> Int -> (Int -> r) -> r
addCPS a b k = k (a + b)
非常简单，现在我们可以看看为什么需要一个 Cont monad 来包住 CPS 计算，首先，来看 ADT 定义

newtype Cont r a = Cont { runCont :: ((a -> r) -> r) }
又是一个同构的类型，Cont 构造器只需要一个 runCount，也就是让他能继续计算的一个函数。

完了之后来把之前的 addCPS 改成 Cont

add :: Int -> Int -> Cont k Int
add a b = return (a + b)
注意到 addCPS 接收到 a 和 b 之后返回的类型是 (Int -> r) -> r ，而 Cont 版本的 add 返回 Cont k Int

明显构造 Cont k Int 也正是需要 (Int -> r) -> r ，所以 Cont 就是算了 k 的抽象了。

instance Monad (Cont r) where
    return a = Cont ($ a)
    m >>= k  = Cont $ \c -> runCont m $ \a -> runCont (k a) c
($ a) 比较有意思, 我们都知道 f $ g a 其实就是 f(g a), 所以 $ 其实就是一个 apply 左边的函数到右边表达式的中缀函数, 如果写成前缀则是 ($ (g a) f). 是反的是因为 $ 是有结合, 需要右边表达式先求值, 所以只给一个 a 就相当于 ($ a) = \f -> f a

回到 Monad Cont…



C#中的递归APS和CPS模式详解,https://www.cnblogs.com/zhangyuanbo12358/articles/4469373.html
本文讲解了累加器传递模式、CPS函数、CPS变换、CPS尾递归、尾递归与Continuation等内容


递归的实现 —— 循环，汇编， CPS 与 y 组合子-V2EX-非常论坛
machbbs.com/v2ex/118610






# Kotlin Coroutine 的 CPS 变换






Kotlin Coroutine 的 CPS 变换 - fleuria的文章 - 知乎
https://zhuanlan.zhihu.com/p/156030219
