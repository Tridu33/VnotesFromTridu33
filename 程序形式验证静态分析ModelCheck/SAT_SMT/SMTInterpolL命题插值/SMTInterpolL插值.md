https://ultimate.informatik.uni-freiburg.de/smtinterpol/





https://theory.stanford.edu/~nikolaj/programmingz3.html#fig-dt

```python

def mk_lit(m, x):
    if is_true(m.eval(x)):
       return x
    else:
       return Not(x)

def pogo(A, B, xs):   
    while sat == A.check():
       m = A.model()
       L = [mk_lit(m, x) for x in xs]
       if unsat == B.check(L):
          notL = Not(And(B.unsat_core()))
          yield notL
          A.add(notL)
       else:
          print("expecting unsat")
          break
```



The (reverse) interpolant between and using vocabulary is . It is implied by and inconsistent with .


```python
A = SolverFor("QF_FD")
B = SolverFor("QF_FD")
a1, a2, b1, b2, x1, x2 = Bools('a1 a2 b1 b2 x1 x2')
A.add(a1 == x1, a2 != a1, a2 != x2)
B.add(b1 == x1, b2 != b1, b2 == x2)
print(list(pogo(A, B, [x1, x2])))
# [Not(And(Not(x2), Not(x1))), Not(And(x2, x1))]插值结果
```

# 1. SMTInterpolL插值

科普 - 程序验证（12）- 谓词抽象 - FRONTIERS的文章 - 知乎
https://zhuanlan.zhihu.com/p/332406712


可以使用SMT求解器来计算插值。 

目前主流的SMT求解器中，对Craig插值计算支持得比较好的有MathSat，以及SMTInterpol。

Z3的Release版本未支持计算插值，但是unstable版本中iZ3分支支持插值计算。 在线版iZ3（或者在线版Z3）具有插值计算功能，我们可以直接使用。























