官网电子书 https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-26.html#%_sec_4.1
 

# 起手式



学习SICP（《计算机程序的构造和解释》）的一些准备工作 - Clement Li的文章 - 知乎 https://zhuanlan.zhihu.com/p/34313034



DrRacket 的安装与 SICP 的配置 https://zhuanlan.zhihu.com/p/37056659


李欣宜写的“SICP从DrRacket钻了出来” https://notebook.xyli.me/SICP/SICP-with-DrRacket/  局部绑定和内部定义 http://notebook.xyli.me/SICP/local-bindings-and-internal-definitions/  其笔记仓库的目录  http://notebook.xyli.me/categories/SICP/


学习SICP（《计算机程序的构造和解释》）的一些准备工作 - Clement Li的文章 - 知乎 https://zhuanlan.zhihu.com/p/34313034

使用VSCode来做SICP习题 - 雾色的文章 - 知乎
https://zhuanlan.zhihu.com/p/344423980

SICP第二章里的“图形语言”在DrRacket 或者MIT Scheme上有没有办法实现啊？ - ysx001的回答 - 知乎
https://www.zhihu.com/question/20789155/answer/19654179











# Scheme-sicp

Scheme语言简明教程
https://www.ctolib.com/docs//sfile/teach-yourself-scheme/index.html 



 
sicp书本  https://mitpress.mit.edu/sites/default/files/sicp/index.html
https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html

 lecture
http://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/ 

 

parsing-techniques.duguying.net/ebook/1/



## python-sicp
Berkeley 改版后的基于Python 的 SICP

CS 61A: Structure and Interpretation of Computer Programs
https://cs61a.org/


CS61A 通关感想 - 雨巷的文章 - 知乎
https://zhuanlan.zhihu.com/p/150348216

最好的CS入门课：CS61a学后感 - 311zzb的文章 - 知乎
https://zhuanlan.zhihu.com/p/456110373



[2021 Spring] CS61A 学习笔记 索引  https://www.cnblogs.com/ikventure/p/14984919.html
Github: https://github.com/ikventure/cs61a-sp21

码云：https://gitee.com/ikventure/cs61a-sp21


SICP Python 描述 翻译完成 https://github.com/wizardforcel/sicp-py-zh



第四章主要介绍了 一个简单的scheme解释器, 一个简单的prolog解释器
第五章介绍了计算机体系结构的cpu设计，简单的编译器，垃圾回收
# code 

答案：http://community.schemewiki.org/?SICP-Solutions


 Scheme语言简明教程 https://www.ctolib.com/docs//sfile/teach-yourself-scheme/index.html




sicp有github仓库实现代码和问题 多语言版 https://github.com/topics/scip

官方 https://mitpress.mit.edu/sites/default/files/sicp/code/index.html

https://github.com/alXmas/sicp Racket



 


SICP解题集


https://sicp.readthedocs.io/en/latest/




SICP解题集
https://sicp.readthedocs.io/en/latest/

https://github.com/huanguolin/sicp-solutions

https://benjamin-philip.github.io/sicp/ Ben's solutions







http://composingprograms.com/ 伯克利的CS61A Python版
http://berkeley-cs61as.github.io/index.html CS61AS Racket版
https://www.comp.nus.edu.sg/~cs1101s/sicp/ 新加坡大学的JavaScript版

在 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/ 下载到全套的资料、视频与英文字幕。
如果你嫌MIT Press的SICP书排版太难看，可以看非官方的HTML5版本 https://sarabander.github.io/sicp/
UP主个人推荐使用Chez Scheme（https://cisco.github.io/ChezScheme/）作为练习环境，相比mit-scheme要省事很多。







# 评论



《计算机程序的构造和解释（SICP）》讨论的核心问题是什么？ - DeathKing的回答 - 知乎
https://www.zhihu.com/question/26549715/answer/34336593






 SICP 计算 的 本质 Conceptual Mathematics - A First Introduction to Categories（卡着了） Haskell 趣学指南 编译器设计（也卡着了） 从抽象到具体。



我的阅读顺序是： SICP 计算 的 本质 Conceptual Mathematics - A First Introduction to Categories（卡着了） Haskell 趣学指南 编译器设计（也卡着了） 从抽象到具体。

读完sicp后应该做些什么？ - 方应杭的回答 - 知乎
https://www.zhihu.com/question/21885160/answer/695567461








##  第五章scheme2寄存器机器
https://mitpress.mit.edu/sites/default/files/sicp/code/index.html

circuit_simulator.scm

https://gist.github.com/rteja/655533c17009323d01083d2dbc2fd402


```scheme
(define (logical-not s)
    (cond   ((= s 0) 1)
            ((= s 1) 0)))

(define (inverter input output)
    (define (invert-input)
        (let ((new-value (logical-not (get-signal input))))
            (after-delay inverter-delay
                (lambda () (set-signal! output new-value)))))
    (add-action! input invert-input) 
    `ok)

(define (logical-and a1 a2)
    (cond   ((and (= a1 1) (= a2 1)) 1)
            (else 0)))

(define (and-gate a1 a2 output)
    (define (and-action-procedure)
        (let ((new-value (logical-and (get-signal a1) (get-signal a2))))
            (after-delay and-gate-delay
                (lambda () (set-signal! output new-value)))))
    (add-action! a1 and-action-procedure)
    (add-action! a2 and-action-procedure)
    `ok)

(define (logical-or a1 a2)
    (cond   ((or (= a1 1) (= a2 1)) 1)
            (else 0)))

;; 3.28
(define (or-gate a1 a2 output)
    (define (or-action-procedure)
        (let ((new-value (logical-or (get-signal a1) (get-signal a2))))
            (after-delay or-gate-delay 
                (lambda () (set-signal! output new-value)))))
    (add-action! a1 or-action-procedure)
    (add-action! a2 or-action-procedure)
    `ok)

;; A wire in out simulation will be a computational object with two
;; local state variables: a signal-value and collection of action-procedures
;; to be run when the signal changes value.

(define (make-wire)
    (let ((signal-value 0) (action-procedures `()))
        (define (set-my-signal! new-value)
            (if (not (= signal-value new-value))
                (begin  (set! signal-value new-value)
                        (call-each action-procedures))
                `done))
        (define (accept-action-procedure! proc)
            (set! action-procedures 
                (cons proc action-procedures))
            (proc))
        (define (dispatch m)
            (cond   ((eq? m `get-signal) signal-value)
                    ((eq? m `set-signal!) set-my-signal!)
                    ((eq? m `add-action!) accept-action-procedure!)
                    (else (error "unknown operation on WIRE" m))))
        dispatch))

(define (call-each procedures)
    (if (null? procedures)
        `done
        (begin  ((car procedures))
                (call-each (cdr procedures)))))

;; *add-action* asserts that designated procedure should be run whenever
;; signal on the wire changes value. such procedures act as vehicles by
;; which changes in the signal value on the wire are communicated
;; to other wires
(define (get-signal wire) (wire `get-signal))

;; *get-signal* returns the current value of the signal on the wire
(define (set-signal! wire new-value) ((wire `set-signal!) new-value))

;; *set-signal* changes the value of the signal on the wire to the new value
(define (add-action! wire action-procedure) 
    ((wire `add-action!) action-procedure))

;; *after-delay* takes time delay and procedure to be run and executes the 
;; given procedure and executes the given procedure after the given delay

(define (after-delay delay action)
    (add-to-agenda! (+ delay (current-time the-agenda))
                    action
                    the-agenda))

;; We use an agenda data structure, that contains schedule of things
;; we to do. The following operations are defined for agenda

;; agenda is made up of time segments. each time segment is a 
;; pair consisting of a number and a queue the holds the procedures
;; scheduled to be run during the time segment
(define (make-time-segment time queue)
    (cons time queue))

(define (segment-time s) (car s))
(define (segment-queue s) (cdr s))

;; agenda itself is a one-dimensional table of time segments
;; segments will be sorted in the order of increasing time
;; in addition we will store the current time at the head of the agenda
;; a newly constructed agenda has no time segments and has current time
;; of zero

;; *make-agenda* returns an empty agenda
(define (make-agenda) (list 0))

;; *current-time* returns the current simulation time
(define (current-time agenda) (car agenda))
(define (set-current-time! agenda time) 
    (set-car! agenda time))
(define (segments agenda) (cdr agenda))
(define (set-segments! agenda segments) 
    (set-cdr! agenda segments))
(define (first-segment agenda) (car (segments agenda)))
(define (rest-segments agenda) (cdr (segments agenda)))

;; *empty-agenda?* returns true if specified agenda is empty
(define (empty-agenda? agenda) 
    (null? (segments agenda)))

;; *add-to-agenda!* modifies the agenda by adding the given action procedure
;; to be run at specified time
(define (add-to-agenda! time action agenda)
    (define (belongs-before? segments)
        (or (null? segments)
            (< time (segment-time (car segments)))))
    (define (make-new-time-segment time action)
        (let ((q (make-queue)))
            (insert-queue! q action)
            (make-time-segment time q)))
    (define (add-to-segments! segments)
        (if (= (segment-time (car segments)) time)
            (insert-queue! (segment-queue (car segments))
                            action)
            (let ((rest (cdr segments)))
                (if (belongs-before? rest)
                    (set-cdr!
                        segments
                        (cons (make-new-time-segment time action)
                            (cdr segments)))
                    (add-to-segments! rest)))))
    (let ((segments (segments agenda)))
        (if (belongs-before? segments)
            (set-segments! 
                agenda
                (cons (make-new-time-segment time action)
                        segments))
            (add-to-segments! segments))))


;; *first-agenda-item* returns the first item on the agenda
(define (first-agenda-item agenda)
    (if (empty-agenda? agenda)
        (error "Agenda is empty: FIRST-AGENDA-ITEM")
        (let ((first-seg (first-segment agenda)))
            (set-current-time! agenda
                                (segment-time first-seg))
            (front-queue (segment-queue first-seg)))))

;; *remove-first-agenda-item!* modifies the agenda by removing the item
(define (remove-first-agenda-item! agenda)
    (let ((q (segment-queue (first-segment agenda))))
        (pop-queue! q)
        (if (empty-queue? q)
            (set-segments! agenda (rest-segments agenda)))))

;; we use the specific instance called the-agenda
(define the-agenda (make-agenda))

;; simulation is driven by the procedure propagate, which operates
;; on the-agenda
(define (propagate)
    (if (empty-agenda? the-agenda)
        `done
        (let ((first-item (first-agenda-item the-agenda)))
            (first-item)
            (remove-first-agenda-item! the-agenda)
            (propagate))))

;; sample probe on the wire
(define (probe name wire)
    (add-action! wire
        (lambda ()
            (newline)
            (display name) (display " ")
            (display (current-time the-agenda))
            (display " new-value = ")
            (display (get-signal wire)))))

;; sample initialization and run
(define inverter-delay 2)
(define and-gate-delay 3)
(define or-gate-delay 5)

;; now lets define four wires
(define input-1 (make-wire))
(define input-2 (make-wire))
(define sum (make-wire))
(define carry (make-wire))

(probe `sum sum)
(probe `carry carry)

;; define half adder
(define (half-adder a b s c)
    (let ((d (make-wire)) (e (make-wire)))
        (or-gate a b d)
        (and-gate a b c)
        (inverter c e)
        (and-gate d e s)
        `ok))

(half-adder input-1 input-2 sum carry)
(set-signal! input-1 1)

;; run propagate to run the simulation
(propagate)

(set-signal! input-2 1)
(propagate)
```














