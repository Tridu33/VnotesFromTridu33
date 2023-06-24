


Y组合子（Y Combinator）| The Little Schemer 第九章 - 纸木城的文章 - 知乎
https://zhuanlan.zhihu.com/p/262284625


# 应用序Y组合子




重新发明：applicative-order Y combinator - LONGHORN的文章 - 知乎
https://zhuanlan.zhihu.com/p/89452609
Y组合子（Y Combinator）| The Little Schemer 第九章 - 纸木城的文章 - 知乎
https://zhuanlan.zhihu.com/p/262284625


看两篇知乎文章学到这个
```racket
#lang racket

;; 网上找了知乎文章才学明白 应用序Y组合子 的从实例到抽象的推导bottom-up。回头看才明白《the little schemer》原来也是这个讲解路子。

;; 递归版本fact
(define fact
    (lambda (x) 
        (cond ((= x 1) 1)
            (else (* x (fact (- x 1)))))))

(fact 3)

;; 希望lambda在不等于1的时候复制粘贴一份自己的表达式计算过程，可以写作(f f), 只用lambda实现fact
(
 ((lambda (f) 
    (lambda (x) 
      (cond ((= x 1) 1)
            (else (* x ((f f) (- x 1)))))))
  (lambda (f) 
    (lambda (x) 
      (cond ((= x 1) 1)
            (else (* x ((f f) (- x 1))))))))
 3)
;; 把else中的(f f)抽取出来,作为参数传递进去。抽离出(f f)为独立参数，方便提取通用的Y组合子，循环满足的抽象计算结构
((
  (lambda (f) (f f)) 
  (lambda (f)
    (
     (lambda (factorial) 
       (lambda (x) 
         (cond ((= x 1) 1)
               (else (* x (factorial (- x 1)))))))
     (lambda (x) ((f f) x))
     )
    )
 ) 3)
;; 把(lambda (factorial) ...)提取出来
;; lambda 变量集1.lambda 变量集2. lambda 变量集3. 可以分离
;; target传入通用的计算函数.
((
  (lambda (target) 
    ((lambda (f) (f f))
        (lambda (f) 
            (target 
                (lambda (x) ((f f) x)))))) 
    (lambda (factorial) 
            (lambda (x) 
                (cond ((= x 1) 1)
                    (else (* x (factorial (- x 1)))))))) 3)

;;;;;;;;;;;;;;;;;; fact阶乘函数和计算列表长度的函数是同构的计算过程

;; 穷人版本lambdacalculus实现递归函数
(
((lambda (mk-length)
  (mk-length mk-length))
(lambda (mk-length)
  (lambda (l)
    (cond 
     ((null? l) 0)
     (else (+ 1 ((mk-length mk-length) (cdr l))))))))
 '(1 2 3)
 )
;;

;; 死循环
;;(
;;((lambda (mk-length)
;;  (mk-length mk-length))
;;(lambda (mk-length)
;;  ((lambda (length)
;;    (lambda (l)
;;    (cond 
;;     ((null? l) 0)
;;     (else (+ 1 (length (cdr l)))))))
;;   (mk-length mk-length))))
;; '(1 2 3)
;; )

;; 表达式(mk-length mk-length) 结果为lengthN
;; 函数定义(lambda (x) ((mk-length mk-length) x)) ;; 求值结果和lengthN功能相同
;; 函数不会立即求值而表达式会,求值会导致新的副作用这里是发生了死循环。
(
((lambda (mk-length)
  (mk-length mk-length))
(lambda (mk-length)
  ((lambda (length)
    (lambda (l)
    (cond 
     ((null? l) 0)
     (else (+ 1 (length (cdr l)))))))
   (lambda (x) ((mk-length mk-length) x)))))
 '(1 2 3)
 )

;;解耦合.提取通用的Y组合子，重复计算的代数规律
(
 (
  ;; 传入函数le,返回curry的函数，需要的参数是一个列表
  (lambda (le)
    ((lambda (mk-length)
       (mk-length mk-length))
     (lambda (mk-length)
       (le (lambda (x) ((mk-length mk-length) x))))))
  ;; 传入函数
  (lambda (length)
    (lambda (l)
    (cond 
     ((null? l) 0)
     (else (+ 1 (length (cdr l)))))))
  )
 '(1 2 3)
 )

;; 解耦合,抽象为一个通用的过程

(define Y
  (lambda (le)
    ((lambda (mk-length)
       (mk-length mk-length))
     (lambda (mk-length)
       (le (lambda (x) ((mk-length mk-length) x))))))
)

((Y (lambda (length)
    (lambda (l)
    (cond 
     ((null? l) 0)
     (else (+ 1 (length (cdr l))))))))
 '(1 2 3))

;; -> 3




;; top-down可以从抽象性质满足的不动点方程出发求解泛函。用计算数学迭代法，通过计算机代数高阶方程的泛函求解，得到组合子作为高阶函数的解函数。https://zhuanlan.zhihu.com/p/547191928


```









