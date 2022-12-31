[TOC]

https://stackoverflow.com/questions/16493792/how-can-i-convert-this-binary-recursive-function-into-a-tail-recursive-form

递归转化为尾递归的CPS写法



-----------------------------------------












什么是「continuation」? - 网易数帆的回答 - 知乎
https://www.zhihu.com/question/61222322/answer/489588936


“call with current continuation”

如何解释 Lisp 中 call/cc 的概念？ - 脚趾头的回答 - 知乎
https://www.zhihu.com/question/21954238/answer/522888860



CPS 变换入门请参考 The Little Schemer
Dan Friedman的the little schemer第八章给出了一个continuation的简单例子。真的很简单。基本上没有讲引入continuation的目的，以及怎么做CPS转换。

王垠的 https://docs.huihoo.com/homepage/shredderyin/wiki/ContinuationNotes.html







怎样理解 Continuation-passing style? - Guannan Wei的回答 - 知乎
https://www.zhihu.com/question/20259086/answer/141162748


continuation 表示为 <e_w_hole, cont> 构成的二元组，在完成当前的 e_w_hole 的求值后，其结果会被填补给下一个 cont 的 hole，直到 cont 是 halt 停机为止。

CPS 作为一种编程方法就是人为地把 continuation 作为一个高阶函数显式地暴露出来，这个函数的参数就是hole，当我们apply这个 continuation（函数）就是在填补这个hole，并进行后续的计算。


至于 call/cc 其实并不属于 CPS 的一部分，call/cc 是语言提供给程序员用以获得当前 continuation 的机制。在语言实现层面为了支持 call/cc 操作可以首先将程序进行CPS变换；或将解释器写为 CPS 形式。



通过获取当前的 continuation，实际上获得了『此刻』以后所有的计算过程，于是便可以做一些有意思的事情，比如实现 non-deterministic 的 amb 操作符、线程和 coroutine 等。

因为最少形式的纯 CPS 的程序只需要有 lambda 和 function application，因此 CPS 程序中所有的递归函数调用都是尾递归。







Continuation 作为程序语言研究中的一个基础概念，历史上被很多人以不同的形式反复发现，例如 SECD Machine 的 J Operator、goto、escape、Monad 等等。John Reynolds 的 The Discoveries of Continuations 和 Olivier Danvy 为 Peter Landin 写的纪念文都是非常好的阅读材料。

在 CPS 中，continuation 被表示为一个高阶函数，那么这个函数本身也可以有其 continuation（被称作 meta continuation）。泛化这个想法，我们便得到了一个可以有 n 级 continuations 的 CPS Hierachy。这种风格也被称作Extended Continuation-Passing Style，ECPS 可以用于方便地实现delimited control operators 比如 shift 和 reset。请参考 Abstracting Control。




Continuation 与 Monad - lsdsjy的文章 - 知乎
https://zhuanlan.zhihu.com/p/28860343


(E)CPS 同 Monad 是“等价”的，理论上任何 Monad 都可以通过等价的 CPS 形式表达（或 shift/reset）出来，这部分可以看 The Essence of Functional Programming 和 Representing Monads。


《A Correspondence between Continuation Passing Style and Static Single Assignment Form》（**SSA**）

CPS 在在过去是函数式语言编译器中常用的**IR**，在编译和程序分析中有很多应用。当程序被转换为 CPS 的时候，Continuation 是直接在 lexical scope 中暴露出来的，而全部的 control flow 转移都是通过调用 continuation 来实现，这样可以直接进行control flow analysis。在进行partial evaluation 的时候 CPS 变换后也可以获得更好的特化效果。

但是 CPS 的可读性太差了，后来 direct style 的 A-Normal Form 在编译和程序分析中流行起来。而 **ANF** 和 CPS 是等价的，A-Normalize 的过程等价于 **CPS convert->Beta normalize->un-CPS convert**，请参考 The Essence of Compiling with Continuation。

CPS 同 Static Single Assignment 也是同构的，在 CPS 中每个变量都通过 lambda 来引入，变量的 mutation 也是通过新的 continuation 来引入；正对应于SSA中每个变量只被赋值一次，并 dominate 接下来的 use，而 Phi node 则在 CPS 中通过对于同一个 cont 传入不同的值来实现。可参考 A Correspondence between Continuation Passing Style and Static Single Assignment Form。











-------------------------



Continuation 在 JS 中的应用 - 尚春的文章 - 知乎
https://zhuanlan.zhihu.com/p/94611888
javascript中的异步编程和continuation-passing style(译) - sniperHW的文章 - 知乎
https://zhuanlan.zhihu.com/p/34370907


----------------------------------------------------

自动 CPS 变换 - 梓文Sola的文章 - 知乎
https://zhuanlan.zhihu.com/p/74068740


王垠的「40 行代码」真如他说的那么厉害吗？ - wsivoky的回答 - 知乎
https://www.zhihu.com/question/20822815/answer/23890076



CPS: Continuation-Passing Style. 有一篇介绍 CPS 通俗易懂的
https://matt.might.net/articles/by-example-continuation-passing-style/ 延续传递风格 (CPS) 起源于 1970 年代的一种编程风格，并在 1980 年代和 1990 年代作为高级编程语言编译器的中间表示而声名鹊起。
它现在被重新发现为非阻塞（通常是分布式）系统的一种编程风格。

本文介绍了 CPS 的两个角色——作为 JavaScript 中非阻塞编程的一种风格，以及（简要地）作为函数式语言的中间形式。

涵盖的主题：

JavaScript 中的 CPS
用于 Ajax 编程的 CPS
用于非阻塞编程的 CPS（在 node.js 中）
用于分布式编程的 CPS
如何使用 CPS 实现异常
用于最小 Lisp 的 CPS 转换器
如何call/cc在 Lisp中实现
如何call/cc在 JavaScript中实现
继续阅读以了解更多信息。


------------------------------------------------------


```scheme
(define cps
  (lambda (exp)
    (letrec
        ([trivs '(zero? add1 sub1)]
         [id (lambda (v) v)]
         [C~ (lambda (v) `(k ,v))]
         [fv (let ((n -1))
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp C)
            (pmatch exp
              [,x (guard (not (pair? x))) (C x)]
              [(lambda (,x) ,body)
               (C `(lambda (,x k) ,(cps1 body C~)))]
              [(,rator ,rand)
               (cps1 rator
                     (lambda (r)
                       (cps1 rand
                             (lambda (d)
                               (cond
                                [(memq r trivs)
                                 (C `(,r ,d))]
                                [(eq? C C~)         ; tail call
                                 `(,r ,d k)]
                                [else
                                 (let ([v* (fv)])
                                   `(,r ,d (lambda (,v*) ,(C v*))))])))))]))])
      (cps1 exp id))))
```

自动 CPS 变换，王垠曾在他的博客GTF - Great Teacher Friedman这样写道：

> 第二个学期，当我去上 Friedman 的进阶课程 B621 的时候，他给我们出了同样的题目。两个星期下来，没有其它人真正的做对了。最后他对全班同学说：“现在请王垠给大家讲一下他的做法。你们要听仔细了哦。这个程序价值100美元！”
下面就是我的程序对于 lambda calculus 的缩减版本。我怎么也没想到，这短短 30 行代码耗费了很多人 10 年的时间才琢磨出来。




```racket
;; A simple CPS transformer which does proper tail-call and does not
;; duplicate contexts for if-expressions.

;; author: Yin Wang (yw21@cs.indiana.edu)


(load "pmatch.scm")


(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))]
         [id (lambda (v) v)]
         [ctx0 (lambda (v) `(k ,v))]      ; tail context
         [fv (let ([n -1])
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx)
            (pmatch exp
              [,x (guard (not (pair? x))) (ctx x)]
              [(if ,test ,conseq ,alt)
               (cps1 test
                     (lambda (t)
                       (cond
                        [(memq ctx (list ctx0 id))
                         `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))]
                        [else
                         (let ([u (fv)])
                           `(let ([k (lambda (,u) ,(ctx u))])
                              (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))]
              [(lambda (,x) ,body)
               (ctx `(lambda (,x k) ,(cps1 body ctx0)))]
              [(,op ,a ,b)
               (cps1 a (lambda (v1)
                         (cps1 b (lambda (v2)
                                   (ctx `(,op ,v1 ,v2))))))]
              [(,rator ,rand)
               (cps1 rator
                     (lambda (r)
                       (cps1 rand
                             (lambda (d)
                               (cond
                                [(trivial? r) (ctx `(,r ,d))]
                                [(eq? ctx ctx0) `(,r ,d k)]  ; tail call
                                [else
                                 (let ([u (fv)])
                                   `(,r ,d (lambda (,u) ,(ctx u))))])))))]))])
      (cps1 exp id))))




;;; tests

;; var
(cps 'x)
(cps '(lambda (x) x))
(cps '(lambda (x) (x 1)))


;; no lambda (will generate identity functions to return to the toplevel)
(cps '(if (f x) a b))
(cps '(if x (f a) b))


;; if stand-alone (tail)
(cps '(lambda (x) (if (f x) a b)))


;; if inside if-test (non-tail)
(cps '(lambda (x) (if (if x (f a) b) c d)))


;; both branches are trivial, should do some more optimizations
(cps '(lambda (x) (if (if x (zero? a) b) c d)))


;; if inside if-branch (tail)
(cps '(lambda (x) (if t (if x (f a) b) c)))


;; if inside if-branch, but again inside another if-test (non-tail)
(cps '(lambda (x) (if (if t (if x (f a) b) c) e w)))


;; if as operand (non-tail)
(cps '(lambda (x) (h (if x (f a) b))))


;; if as operator (non-tail)
(cps '(lambda (x) ((if x (f g) h) c)))


;; why we need more than two names
(cps '(((f a) (g b)) ((f c) (g d))))



;; factorial
(define fact-cps
  (cps
   '(lambda (n)
      ((lambda (fact)
         ((fact fact) n))
       (lambda (fact)
         (lambda (n)
           (if (zero? n)
               1
               (* n ((fact fact) (sub1 n))))))))))

;; print out CPSed function
(pretty-print fact-cps)
;; =>
;; '(lambda (n k)
;;    ((lambda (fact k) (fact fact (lambda (v0) (v0 n k))))
;;     (lambda (fact k)
;;       (k
;;        (lambda (n k)
;;          (if (zero? n)
;;            (k 1)
;;            (fact
;;             fact
;;             (lambda (v1) (v1 (sub1 n) (lambda (v2) (k (* n v2))))))))))
;;     k))


((eval fact-cps) 5 (lambda (v) v))
;; => 120
```
# 自动CPS变换的程序
Auto-CPS - 默安的文章 - 知乎
https://zhuanlan.zhihu.com/p/462740212

四小时 CPS 教程。

这份教程试图说明什么是 CPS，以及如何写一个自动 CPS 变换的程序，其内容依据 EOPL-1st 第八章。我所做的，仅仅是对 EOPL-1st 的内容进行了组织，没有什么原创。如果你有所收获，那完全归功于你的努力和 Daniel Friedman 的善巧。

实际上我更推荐你直接去读 EOPL-1st，在这里有其扫描版。










# 土法之寻找关联？

- 《计算的本质》ruby那样编译为对象之上的模拟lambd演算：

递归转循环可以用对象模拟闭包进而用堆里面的对象Stack模拟压栈变成循环 https://www.bilibili.com/video/BV1Vu411m7a5
从程序员角度理解状态机

- 编译为串起来的中间代码IR-CPS
自动CPS来写程序，其中比较好用的处理控制结构的编程接口，语义调用方法call/cc





















