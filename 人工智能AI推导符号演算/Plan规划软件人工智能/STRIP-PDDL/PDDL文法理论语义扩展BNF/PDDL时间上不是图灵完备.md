

chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://icaps16.icaps-conference.org/proceedings/summer-school/Rintanen.pdf

Computational Complexity in AutomatedPlanning and Scheduling




# 1. PDDL时间上不是图灵完备
[In defense of PDDL axioms](https://www.sciencedirect.com/science/article/pii/S0004370205000810
```
<domain>                ::= (define (domain <name>)
[<constant-def>]
[<predicates-def>]
[<axiom-def>*]
<action-def>*)

<constants-def>         ::= (:constants <name>+)
<predicate-def>         ::= (:predicates <skeleton>+)
<skeleton>              ::= (<predicate> <variable>*)
<predicate>             ::= <name>
<variable>              ::= ?<name>
<axiom-def>             ::= (:derived <skeleton> <formula>)
<formula>               ::= <atomic-formula>
<formula>               ::= (not <formula>)
<formula>               ::= (and <formula> <formula>+)
<formula>               ::= (or <formula> <formula>+)
<formula>               ::= (imply <formula> <formula>)
<formula>               ::= (exists (<variable>+) <formula>)
<formula>               ::= (forall (<variable>+) <formula>)
<atomic-formula>        ::= (<predicate> <term>*)
<ground-atomic-formula> ::= (<predicate> <name>*)
<term>                  ::= <name>
<term>                  ::= <variable>
<action-def>            ::= (:action <name>:parameters (<variable>*)<action-def body>)
<action-def body>       ::= [:precondition <formula>]:effect <eff-formula>
<eff-formula>           ::= <one-eff-formula>
<eff-formula>           ::= (and <one-eff-formula><one-eff-formula>+)
<one-eff-formula>       ::= <atomic-effs>
<one-eff-formula>       ::= (when <formula> <atomic-effs>)
<one-eff-formula>       ::= (forall (<variable>+) <atomic-effs>)
<one-eff-formula>       ::= (forall (<variable>+)(when <formula> <atomic-effs>))
<atomic-effs>           ::= <literal>
<atomic-effs>           ::= (and <literal> <literal>+)
<literal>               ::= <atomic-formula>
<literal>               ::= (not <atomic-formula>)
<task>                  ::= (define (task <name>)(:domain <name>)<object declaration><init><goal>)
<object declaration>    ::= (:objects <name>*)
<init>                  ::= (:init <ground-atomic-formula>*)
<goal>                  ::= (:goal <formula>)
```


Syntax of PDDL 

https://www.quora.com/What-is-difference-in-expressive-power-between-PDDL-and-Prolog


PDDL代表规划域定义语言。它是用于计划任务的标准编码。请注意，PDDL有不同版本，并且具有各种扩展名。实际上，许多“ PDDL”求解器仅支持PDDL的某些子集。

通常，对计划任务的描述由特定组件组成，例如：

初始状态
一个目标
可以执行的动作
等等。
如果您的计划框架足够通用，那么这种特定于领域的计划语言实际上可以是Turing-complete ，因此与通用编程语言（例如Prolog）具有相同的计算能力：

证明图灵机领域可以看作是经典的计划领域

但是，PDDL并非如此：在PDDL中，通常需要对某些有限域（例如整数的有限间隔）进行推理。如果域是有限的，则无法建模无限的磁带，因此PDDL的表达能力明显低于Prolog。

此外，您通常只对多项式长度的计划感兴趣，甚至仅限于多项式长度的计划。在这种情况下，PDDL是PSPACE或EXPTIME完整的，具体取决于您使用的扩展名和变体。这尤其意味着存在许多无法在PDDL中表达的计算任务。

从实践的角度来看，即使PDDL在理论上足够强大，可以对所有计算任务进行建模，但在计划任务的预期应用领域之外使用它是否是方便或可取的仍值得商bat。

另一方面，Prolog是图灵完备的编程语言。这尤其意味着你可以表现一切任何编程语言，你可以也表达序言。您可以通过使用Prolog模拟图灵机来显示此信息：

https://www.metalevel.at/prolog/showcases/turing.pl

简介：PDDL是一种用于表达计划任务的领域特定语言，而Prolog是一种成熟的编程语言，可让您表达所有可能的计算（包括解决计划任务）。

以下是一些其他参考资料，希望对您有用：

https://www.cs.toronto.edu/~sheila/2542/s14/A1/introtopddl2.pdf

在PDDL中编写计划领域和问题

PDDL背景

http://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf

http://users.cecs.anu.edu.au/~thiebaux/papers/ijcai03.pdf

https://fai.cs.uni-saarland.de/hoffmann/papers/ki11.pdf












