# 1. SMT solver验证程序等价

不过把 program 转换到 formula ,llvm上加个pass就有了.control flowgraph迁移系统永远的神


用SMT solver验证程序等价 - rainoftime的文章 - 知乎
https://zhuanlan.zhihu.com/p/30520308

```z3
int power3_A(int in) {
  int i, out_a;
  out_a = in; 
  for (i = 0; i < 2; i++) 
    out_a = out_a * in;
  return out_a;
}

int power3_B(int in) {
  int out_b;
  out_b = (in * in) * in; 
  return out_b; 
}
```
如何证明power3_A, power3_B干了同一件事情？一个传统方法是写测试用例，但是这2个程序的输入int型整数取值范围很大....

基于形式逻辑的程序验证.这个例子比较简单，可以对power3_A做循环展开，然后用逻辑公式分别编码power3_A, power3_B的程序语义（需要引入中间变量）。编码$\alpha_a$,$,$\alpha_b$



```mathjax
$$
\begin{align*}
out0_a &= in \wedge \\
out1_a &= out0_a * in \wedge \\
out2_a &= out1_a * in
\end{align*}
$$
```


```mathjax
$$
\begin{align*}
out0_a &= (in * in )* in
\end{align*}
$$
```





```python
from z3 import *
# 创建solver和逻辑变量
solver = Solver()
out0a, out1a, out2a, out0b, In = BitVecs("out0a out1a out2a out0b In", 32)

# 编码A程序语义
fa = And(out0a == In, out1a == out0a * In, out2a == out1a * In)

# 编码B程序语义
fb = (out0b == In * In * In)

# 证明程序等价，需要证明G永真(VALID)
G = Implies(And(fa, fb), out2a == out0b)

# 转化为可满足性问题：将G取反后判断其是否不可满足(UNSAT)
solver.add(Not(G))
print solver.check()
```
