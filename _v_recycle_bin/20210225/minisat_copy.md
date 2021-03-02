# minisat

minisat-user-gude-cnf.txt

```
p cnf 5 3
1 -5 4 0
-1 5 3 4 0
-3 -4 0
```

(x1 | -x5 | x4)&(-x1 |  x5 | x3 | x4)&(-x3 | -x4)

```
p$ ./minisat minisat-user-gude-cnf.txt minisat-user-gude-outputSAT.txt
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |       3        9 |       1       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 0              (-nan /sec)
decisions             : 6              (inf /sec)
propagations          : 5              (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0 s

SATISFIABLE
```


```
SAT
-1 -2 -3 -4 -5 0
```



# 第二个解

追加第一个解的负形：

```
1 2 3 4 5 0
```

然后运行命令行，得到第二个解答：

```
-1 2 -3 -4 -5 0
```







































































