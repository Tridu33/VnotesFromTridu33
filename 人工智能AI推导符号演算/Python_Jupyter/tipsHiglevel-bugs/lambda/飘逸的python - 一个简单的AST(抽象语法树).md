# 1. 飘逸的python - 一个简单的AST(抽象语法树)






https://blog.csdn.net/handsomekang/article/details/39778625









```python
Num = lambda env, n: n
Var = lambda env, x: env[x]
Add = lambda env, a, b:_eval(env, a) + _eval(env, b)
Mul = lambda env, a, b:_eval(env, a) * _eval(env, b)
 
_eval = lambda env, expr:expr[0](env, *expr[1:])
 
env = {'a':2, 'b':5}
tree = (Add, (Var, 'a'),
             (Mul, (Num, 3),
                   (Var, 'b')))
 
print _eval(env, tree)

```