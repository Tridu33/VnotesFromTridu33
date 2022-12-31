[TOC]

# 1. 讨论工作开展下一步

1. 传递闭包性质的扩展的SMT solver

2. 需要#x计数功能实现counting的SMT solver扩展

3. 需要$n(x)\darr$表示下降的扩展谓词



## 1.1. SMT solvers

理论角度提出logic中解决传递闭包问题的方法：

​    [First-Order Transitive Closure Axiomatizationvia Iterative Invariant Injections](https://asa.iti.kit.edu/downloads/a.a.elghazi_m.taghdiri_m.herda_nfm2015.final.pdf)  文中提出  an  approach  for  proving  the  validity of  first-order  relational  formulas  that  involve  transitive  closure.  Given a  formula $F$ that  includes  the  transitive  closure  of  a  relation $R$,  our approach can deduce a complete (pure) first-order axiomatization of the paths of $R$ that occur in $F$. Such axiomatization enables full automated verification  of Fusing  an  automatic  theorem  prover  like  Z3.This paper presents a proof for the correctness of the approach, and reports on its application to non-trivial Alloy benchmarks.


## 1.2. z3
  [Z3](http://rise4fun.com/z3)

Supported theories:

uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, nonlinear arithmetic, arrays, bit-vectors, datatypes, floating point arithmetic, quantifiers

**例**：

传递关系，$R(a,b),R(b,c)$。则有$TCR(a,c)$成立。

```z3
from z3 import *
B = BoolSort()
S = DeclareSort('S')
a, b, c = Consts('a b c', S)
R = Function('R', S, S, B)
TCR = TransitiveClosure(R)
s = Solver()

s.add(R(a, b) == True)
s.push()     # If this line is uncommented (or both are) the result is sat, which is wrong.
s.add(TCR(a, b) == False)
s.push()     # But if THIS line is uncommented (or neither are), the result is unsat, which is correct.

print(s)
print(s.check())
```



```z3
from z3 import *

def main():
A = DeclareSort('A')
R = Function('R', A, A, BoolSort())
TC_R = TransitiveClosure(R)
# TRC_R = TransitiveReflexiveClosure(R)
s = Solver()
a, b, c = Consts('a b c', A)
s.add(R(a, b))
s.add(R(b, c))
s.add(Not(TC_R(a, c)))

print(s.check())


if __name__ == "__main__":
main()
```
## 1.3. yices

  [Yices](https://yices.csl.sri.com/)

Supported theories:

uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors

Alloy教材 《[Software Abstractions](http://softwareabstractions.org/)》 第二章有一个例子传递闭包addressBook3d，针对这个例子，《Analyzing Alloy Constraints using an SMT Solver:A Case Study》用alloy形式化描述输入然后使用SMT solver中的Yices 2进行求解样例讨论。

>**Alloy** is a first-order **relational logic** with **transitive closure**,有一个软件能直接求alloy输入的问题。
>
>其中relational logic：[standford课程介绍关系逻辑](http://logic.stanford.edu/intrologic/chapters/chapter_06.html#:~:text=In%20Relational%20Logic%2C%20the%20precedence,both%20quantifiers%20and%20logical%20operators),在论文[Automating First-Order Relational Logic](https://groups.csail.mit.edu/sdg/pubs/2000/alcoa-algorithm.pdf)中提到 **Relational  logic**  adds  to  first-order  logic  the  ability  to  combine  predicates  with  special  operators.  For  example,  we  can  write  the  formula $∀x,y. S(x)∧R(x,y)⇒ T(y) $as S.R in T, where S.R denotes the image  of  the  set  S  under  the  relation  R.  The  logic  is  more  than  a  definitional  extension  of  first-order  logic,  because  it  includes  **transitive closure**. 文中把Z语言规范的输入Alloy Analyzer 转成CNF调用随便一个SMT solver就能求解。
>
>**Yices**是一种SMT 求解器，用于确定包含具有相等性，实数和整数算术，位向量，标量类型和元组的未解释函数符号的公式的可满足性。Yices支持线性和非线性算法。Yices可以处理以SMT-LIB 表示法 https://smt-lib.org/ 编写的输入。


## 1.4. CVC4

  [CVC4](https://cvc4.github.io/app)

 Supported theories:

uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors, datatypes, strings, quantifiers

[Relational Constraint Solving in SMT](http://theory.stanford.edu/~barrett/pubs/MRT+17.pdf)文中提到Relational logic is useful for reasoning about computational problemswith relational structures, including high-level system design, architectural con-figurations  of  network  systems,  ontologies,  and  verification  of  programs  withlinked  data  structures.A把能描述传递闭包的Alloy描述建模为关系逻辑然后[Relational Constraint Solving in SMT](http://theory.stanford.edu/~barrett/pubs/MRT+17.pdf)使用CVC4求。

[《Analyzing Alloy Constraints using an SMT Solver:A Case Study》](http://asa.iti.kit.edu/a.a.elghazi_m.taghdiri_afm2010.final.pdf)

### 1.4.1. 各种SMT solvers

- [MathSAT](https://mathsat.fbk.eu/)

Supported theories: uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors, floating point arithmetic

- [OpenSMT](verify.inf.unisi.ch/opensmt.html)

Supported theories: uninterpreted functions, real and integer difference logic, linear real arithmetic, bit-vectors

- [SMT Interpol](ultimate.informatik.uni-freiburg.de/smtinterpol)

[Supported theories](https://github.com/ultimate-pa/smtinterpol): uninterpreted functions, linear integer and real arithmetic

- [SONOLAR](http://www.informatik.uni-bremen.de/florian/sonolar)

Supported theories: bit-vectors, floating-point arithmetic

- [STP](sites.google.com/site/stpfastprover)

Supported theories: arrays, bit-vectors

- [veriT](www.verit-solver.org)

Supported theories:uninterpreted functions, integer and real difference logic, quantifiers

#### 1.4.1.1. SMT solvers能力范围

[**AUFLIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#AUFLIA)

Closed formulas over the theory of linear integer arithmetic and arrays extended with free sort and function symbols but restricted to arrays with integer indices and values.

[**AUFLIRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#AUFLIRA)

Closed linear formulas with free sort and function symbols over one- and two-dimentional arrays of integer index and real value.

[**AUFNIRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#AUFNIRA)

Closed formulas with free function and predicate symbols over a theory of arrays of arrays of integer index and real value.

[**LIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#LIA)

Closed linear formulas over linear integer arithmetic.

[**LRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#LRA)

Closed linear formulas in linear real arithmetic.

[**QF_ABV:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_ABV)

Closed quantifier-free formulas over the theory of bitvectors and bitvector arrays.

[**QF_AUFBV:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_AUFBV)

Closed quantifier-free formulas over the theory of bitvectors and bitvector arrays extended with free sort and function symbols.

[**QF_AUFLIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_AUFLIA)

Closed quantifier-free linear formulas over the theory of integer arrays extended with free sort and function symbols.

[**QF_AX:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_AX)

Closed quantifier-free formulas over the theory of arrays with extensionality.

[**QF_BV:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_BV)

Closed quantifier-free formulas over the theory of fixed-size bitvectors.

[**QF_IDL:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_IDL)

Difference Logic over the integers. In essence, Boolean combinations of inequations of the form *x - y < b* where *x* and *y* are integer variables and *b* is an integer constant.

[**QF_LIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_LIA)

Unquantified linear integer arithmetic. In essence, Boolean combinations of inequations between linear polynomials over integer variables.

[**QF_LRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_LRA)

Unquantified linear real arithmetic. In essence, Boolean combinations of inequations between linear polynomials over real variables.

[**QF_NIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_NIA)

Quantifier-free integer arithmetic.

[**QF_NRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_NRA)

Quantifier-free real arithmetic.

[**QF_RDL:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_RDL)

Difference Logic over the reals. In essence, Boolean combinations of inequations of the form *x - y < b* where *x* and *y* are real variables and *b* is a rational constant.

[**QF_UF:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UF)

Unquantified formulas built over a signature of uninterpreted (i.e., free) sort and function symbols.

[**QF_UFBV:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UFBV)

Unquantified formulas over bitvectors with uninterpreted sort function and symbols.

[**QF_UFIDL:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UFIDL)

Difference Logic over the integers (in essence) but with uninterpreted sort and function symbols.

[**QF_UFLIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UFLIA)

Unquantified linear integer arithmetic with uninterpreted sort and function symbols.

[**QF_UFLRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UFLRA)

Unquantified linear real arithmetic with uninterpreted sort and function symbols.

[**QF_UFNRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#QF_UFNRA)

Unquantified non-linear real arithmetic with uninterpreted sort and function symbols.

[**UFLRA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#UFLRA)

Linear real arithmetic with uninterpreted sort and function symbols.

[**UFNIA:**](http://smtlib.cs.uiowa.edu/logics-all.shtml#UFNIA)

Non-linear integer arithmetic with uninterpreted sort and function symbols.

