


# 1. z3布尔sympy表达式化简




https://stackoverflow.com/questions/65022373/z3-boolean-expression-simplification


对于此类问题，Z3的简化引擎不是一个不错的选择。它确实可以“简化”表达式，但是几乎永远不会与人类认为简单的表达式相匹配。许多“显而易见”的简化将不会应用，因为从SAT解算器的角度来看它们根本无关紧要。您可以在堆栈溢出中搜索许多类似的问题，虽然z3策略可以有效地发挥作用，但它们并不是针对您要尝试的操作而设计的。

如果您正在寻找“最小”（启发式意义上的）简化，则应考虑其他工具。例如，sympy附带了一组例程，这些例程可以很好地转换为规范形式和简化操作：https://stackoverflow.com/questions/64562464/cnf-by-truth-table/64626278#64626278

编码并转换为CNF，


simplify_logic可以根据该form参数转换为CNF或DNF 。


```
Python 3.8.5 (default, Jul 21 2020, 10:48:26)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from sympy import *
>>> x, y, z = symbols('x y z')
>>> simplify_logic((x & y & ~z) | (x & ~y & z), form="cnf")
x & (y | z) & (~y | ~z)
```


请注意，CNF扩展通常可能会很昂贵，并且Tseitin编码是避免这种复杂性的首选方法（https://en.wikipedia.org/wiki/Tseytin_transformation）。但是它具有引入新变量的缺点。





https://reverseengineering.stackexchange.com/questions/3606/how-to-efficiently-simplify-obfuscated-formula-in-qf-bv-logic-with-z3











