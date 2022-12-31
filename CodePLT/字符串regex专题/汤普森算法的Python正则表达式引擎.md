# 1. 汤普森算法的Python正则表达式引擎






github.com/xysun/regex





xysun.github.io/posts/regex-parsing-thompsons-algorithm.html




正则表达式引擎背后的中心思想是非确定性自动机NFA。虽然这个名称很吓人，但它只是一个状态机，可以以某些字符或什么都不转移到其他状态机（称为“ε转换”）

汤普森算法与当前在Python / Ruby / ...中的回溯实现之间的区别在于对多个转换的处理。回溯算法仅一步步跟踪一个过渡（始终选择贪婪过渡），如果当前路由失败，则回溯到另一条路由，而汤普森算法同时跟踪所有可能的过渡。