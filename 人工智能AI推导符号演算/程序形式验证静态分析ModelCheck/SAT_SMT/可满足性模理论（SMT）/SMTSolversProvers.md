SRI研制了 Yices，Microsoft 推出了 Z3，New York 大学研发了 CVC3 等。各机构的研究目标不尽相同，Microsoft 公司旨在研发适用于所有理论域的高效商业工具并推出最新研制成果 Z3 求解器，New  York 大学的工作组旨在研发一个主要服务于教学科研的并且适合求解各种理论域的，具备较好求解能力的开源工具并推出了CVC3 求解器




# 1. SMT solvers

主要的问题描述语言是alloy,DPPL,SMT-lib等形式，alloy2SMT-lib描述，其中z3适用输入格式最广，yices2也很多人用。主要的任务集是[SMT-lib](http://smtlib.cs.uiowa.edu/),讨论各种SMT solver。[求解能力测试实验比较问题集的文章](https://spreadsheets.ist.tugraz.at/wp-content/uploads/sites/3/2015/06/DS_Hoefler.pdf)

常见的大大小小的SMT solvers及其能力：


- 软件名Alt-Ergo

https://alt-ergo.ocamlpro.com/

Supported theories:uninterpreted functions, linear integer and real arithmetic, nonlinear arithmetic, polymorphic arrays,bit-vectors, records, enumerated datatypes, ACsymbols, quantifiers

- Barcelogic

www.lsi.upc.edu/oliveras/bclt-main.html

Supported theories:uninterpreted functions, integer and real difference logic, linear integer and real arithmetic


- Boolector

fmv.jku.at/boolector

Supported theories:arrays, bit-vectors都说这个做布尔向量专业点

- CVC4

cvc4.cs.nyu.edu

https://cvc4.github.io/app

Supported theories:uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors, datatypes, strings, quantifiers

- MathSAT

https://mathsat.fbk.eu/

Supported theories:uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors, floating point arithmetic

- OpenSMT

verify.inf.unisi.ch/opensmt.html

Supported theories:uninterpreted functions, real and integer difference logic, linear real arithmetic, bit-vectors

- SMTInterpolL

ultimate.informatik.uni-freiburg.de/smtinterpol

Supported theories:uninterpreted functions, linear integer and real arithmetic

- SONOLAR

http://www.informatik.uni-bremen.de/ ̃florian/sonolar

Supported theories:bit-vectors, floating-point arithmetic

- STP

sites.google.com/site/stpfastprover

Supported theories:arrays, bit-vectors

- veriT

www.verit-solver.org

Supported theories:uninterpreted functions, integer and real difference logic, quantifiers

●SMTInterpol

https://github.com/ultimate-pa/smtinterpol

- Princess

http://logicrunch.it.uu.se:4096/~wv/princess/

- Yices

https://yices.csl.sri.com/

Supported theories:uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, arrays,bit-vectors

- Z3

http://rise4fun.com/z3

Supported theories:uninterpreted functions, integer and real difference logic, linear integer and real arithmetic, nonlineararithmetic, arrays, bit-vectors, datatypes, floating point arithmetic, quantifiers

[ACL2](https://www.cs.utexas.edu/users/moore/acl2/)（A Computational Logic for Applicative Common Lisp，应用式 Common Lisp 计算逻辑）是由一个程序语言、一套一阶逻辑的可拓理论、以及一个机械化的定理证明器所组成的软件系统。和pddl很像都是来自lisp类似的语法描述，有一致输入形式的优势，但是扩展看起来不是很丰富。

初步估计还是要用最主流的z3或者yices。


--------------------------------------------------------------------------------

任务描述：把STRIPS.pddl用parser读进去任务，qnp用parser读进去，还有一个细化映射+限制公式的config配置信息，然后把读入内存的描述进行各种翻译扩展，把低阶语言中无法表达的高阶语言特性“程序翻译”得到等效低阶语言描述(或者必要时添点老师今天说的约束公式)。用细化映射，高阶抽象的东西会变成低阶抽象同等级的语言的一堆公式，就变成：

*高阶细化映射后公式==低阶语言公式*的定理证明问题

现在主要就是需要SMT有或者自己手动扩展这些特性：传递闭包，$\#$计数高阶特性，表达下降算子$x\darr$。

-------------------------------------------------

- 传递闭包

1. 理论角度提出logic中解决传递闭包问题的方法：


​    [First-Order Transitive Closure Axiomatizationvia Iterative Invariant Injections](https://asa.iti.kit.edu/downloads/a.a.elghazi_m.taghdiri_m.herda_nfm2015.final.pdf)  文中提出  an  approach  for  proving  the  validityof  first-order  relational  formulas  that  involve  transitive  closure.  Givena  formulaFthat  includes  the  transitive  closure  of  a  relationR,  ourapproach can deduce a complete (pure) first-order axiomatization of thepaths ofRthat occur inF. Such axiomatization enables full automatedverification  ofFusing  an  automatic  theorem  prover  like  Z3.This paperpresents a proof for the correctness of the approach, and reports on itsapplication to non-trivial Alloy benchmarks.

2. 实践应用现有软件SMT solvers角度看：

- Yices:

Alloy教材 《[Software Abstractions](http://softwareabstractions.org/)》 第二章有一个例子传递闭包addressBook3d，针对这个例子，《Analyzing Alloy Constraints using an SMT Solver:A Case Study》用alloy形式化描述输入然后使用SMT solver中的Yices 2进行求解样例讨论。

>Alloy：Alloy is a first-order **relational logic** with **transitive closure**,有一个软件能直接求alloy输入的问题。
>
>其中relational logic：[standford课程介绍关系逻辑](http://logic.stanford.edu/intrologic/chapters/chapter_06.html#:~:text=In%20Relational%20Logic%2C%20the%20precedence,both%20quantifiers%20and%20logical%20operators),在论文[Automating First-Order Relational Logic](https://groups.csail.mit.edu/sdg/pubs/2000/alcoa-algorithm.pdf)中提到 **Relational  logic**  adds  to  first-order  logic  the  ability  to  combine  predicates  with  special  operators.  For  example,  we  can  write  the  formula $∀x,y. S(x)∧R(x,y)⇒ T(y) $as S.R in T, where S.R denotes the image  of  the  set  S  under  the  relation  R.  The  logic  is  more  than  a  definitional  extension  of  first-order  logic,  because  it  includes  **transitive closure**. 文中把Z语言规范的输入Alloy Analyzer 转成CNF调用随便一个SMT solver就能求解。
>
>Yices 2是一种SMT 求解器，用于确定包含具有相等性，实数和整数算术，位向量，标量类型和元组的未解释函数符号的公式的可满足性。Yices 2支持线性和非线性算法。Yices 2可以处理以SMT-LIB 表示法 https://smt-lib.org/ 编写的输入。

- CVC4:

[Relational Constraint Solving in SMT](http://theory.stanford.edu/~barrett/pubs/MRT+17.pdf)文中提到Relational logic is useful for reasoning about computational problemswith relational structures, including high-level system design, architectural con-figurations  of  network  systems,  ontologies,  and  verification  of  programs  withlinked  data  structures.A把能描述传递闭包的Alloy描述建模为关系逻辑然后[Relational Constraint Solving in SMT](http://theory.stanford.edu/~barrett/pubs/MRT+17.pdf)使用CVC4求。

- Z3:

 [z3文档#传递闭包](https://theory.stanford.edu/~nikolaj/programmingz3.html#sec-transitive-closure)Z3应该是已内置了对传递闭包的支持，但是[有点问题的样子](https://github.com/Z3Prover/z3/issues/4691)

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

看反应，大家都好像对这个存疑[Forums](https://github.com/Z3Prover/z3/issues/4901)

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

但是感觉z3有微软大公司背书，论文有什么算法新特性都尽快及时加进去使用，还是要用z3？但是都是Yices更火，一些资料得到的结论是YICES一般会比Z3要快，YICES和CVC4更新可能频繁些，Z3那些主要theory更稳定（虽然很多拓展功能开发中，要两个都看比较才知道那个在此问题上更加适合）。

- $\#$计数算子，
- - $\darr$下降算子？

或者手动展开问题的实例低阶公式？写个转化？











