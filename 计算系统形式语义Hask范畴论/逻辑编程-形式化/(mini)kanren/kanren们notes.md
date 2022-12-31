[TOC]

http://minikanren.org/ most全面的教程


https://github.com/brandonwillard/kanren 直接

```python
pip install miniKanren
```








----------------------------------------------------





http://io.livecode.ch/learn/webyrd/webmk 
scheme教程minikanren
== fresh conde

*==* unifies two terms. 


*fresh*, which syntactically looks like lambda, introduces lexically-scoped Scheme variables that are bound to new logic variables; fresh also performs conjunction of the relations within its body. 

```scheme
(run 1 (y)
  (fresh (x y)
    (== 4 x)
    (== x y))
  (== 3 y))
```

```
(3)
```

*conde*, which resembles cond syntactically, is used to produce multiple answers. Logically, conde can be thought of as 析取范式disjunctive normal form: each clause represents a disjunct, and is independent of the other clauses, with the relations within a clause acting as the conjuncts. 

```scheme
(run 2 (q)
  (fresh (w x y)
    (conde
      (
       (== `(,x ,w ,x) q)
       (== y w)
      )
      (
       (== `(,w ,x ,w) q)
       (== y w)
      )
    )
  ) 
)
```

```
((_.0 _.1 _.0) (_.0 _.1 _.0))
```












































































































































































































































