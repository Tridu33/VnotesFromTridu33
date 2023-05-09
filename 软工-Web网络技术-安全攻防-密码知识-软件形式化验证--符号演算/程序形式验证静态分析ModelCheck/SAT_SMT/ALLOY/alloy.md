[TOC]




http://softwareabstractions.org/


丹尼尔·杰克逊（Daniel Jackson） 在《软件抽象》中介绍了一种新的软件设计方法，该方法借鉴了传统的形式化方法，但可以利用自动化工具尽早发现缺陷。这种方法（杰克逊称之为“轻量级形式方法”或“敏捷建模”）从形式规范中采用了基于简单而健壮的概念的微小核心的精确而富有表现力的表示法，但以完全证明取代了基于定理证明的传统分析。自动化分析，可为设计人员提供即时反馈。杰克逊开发了Alloy，这是一种语言，它使用最少的数学概念工具包来简单，简洁地捕获软件抽象的本质。

此修订版更新了文本，示例和附录，以与最新版本的Alloy（合金4）完全兼容。设计人员不仅可以使用自动分析来纠正错误，而且可以使模型更精确，更美观。杰克逊说，这种方法可以使设计师摆脱“实施技术的苦恼”，并使他们重新思考底层概念。软件抽象介绍了关键要素：逻辑，它提供了语言的基本组成部分；一种语言，在结构化描述的逻辑中添加了少量语法；分析，一种约束求解的形式，它既提供模拟（生成样本状态和执行）又提供检查（查找所要求属性的反例）




Mondex case study with alloy.http://www.eleves.ens.fr/home/ramanana/work/mondex







# 1. alloy

在线API文档：[http://alloytools.org/documentation/alloy-api/index.html](http://alloytools.org/documentation/alloy-api/index.html)

API examples

-   Example using the compiler ([download](http://alloytools.org/documentation/code/ExampleUsingTheCompiler.java), [view](http://alloytools.org/documentation/code/ExampleUsingTheCompiler.java.html))
    
-   Example using the ast ([download](http://alloytools.org/documentation/code/ExampleUsingTheAPI.java), [view](http://alloytools.org/documentation/code/ExampleUsingTheAPI.java.html))
    
-   Example using the evaluator ([download](http://alloytools.org/documentation/code/EvaluatorExample.java), [view](http://alloytools.org/documentation/code/EvaluatorExample.java.html))



<table style="margin-bottom: 30px; width: 739px; text-align: left; color: rgb(63, 63, 63); border-collapse: collapse; border: 1px solid rgb(232, 232, 232); font-family: &quot;Droid Serif&quot;, Trebuchet, &quot;Times New Roman&quot;, Times, serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: 1px; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"><tbody><tr><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/faq/faq.html" style="color: rgb(20, 119, 203); text-decoration: none;">FAQ</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Frequently asked questions about Alloy</td></tr><tr style="background-color: rgb(247, 247, 247);"><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/download/alloy-language-reference.pdf" style="color: rgb(20, 119, 203); text-decoration: none;">reference</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Download language reference for Alloy 4 (PDF)</td></tr><tr><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/download/comparisons.pdf" style="color: rgb(20, 119, 203); text-decoration: none;">comparisons</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Comparisons to Z, B, VDM and OCL (PDF)</td></tr><tr style="background-color: rgb(247, 247, 247);"><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/download/alloy4-grammar.txt" style="color: rgb(20, 119, 203); text-decoration: none;">grammar</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">A grammar for Alloy 4 in plain text (TXT), also see the<span>&nbsp;</span><a href="https://github.com/AlloyTools/org.alloytools.alloy/blob/master/org.alloytools.alloy.application/src/main/java/edu/mit/csail/sdg/alloy4compiler/parser/Alloy.cup" style="color: rgb(20, 119, 203); text-decoration: none;">cup file</a></td></tr><tr><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/quickguide" style="color: rgb(20, 119, 203); text-decoration: none;">quick guide</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Overview of new features in Alloy 4</td></tr><tr style="background-color: rgb(247, 247, 247);"><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/documentation/alloy-api/index.html" style="color: rgb(20, 119, 203); text-decoration: none;">Alloy API</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Documentation for Alloy API</td></tr><tr><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/documentation/alloy-api-examples.html" style="color: rgb(20, 119, 203); text-decoration: none;">Alloy API Examples</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">examples of using<span>&nbsp;</span><a href="http://alloytools.org/code/ExampleUsingTheCompiler.java.html" style="color: rgb(20, 119, 203); text-decoration: none;">the compiler</a>,<span>&nbsp;</span><a href="http://alloytools.org/code/ExampleUsingTheAPI.java.html" style="color: rgb(20, 119, 203); text-decoration: none;">the ast</a>,<span>&nbsp;</span><a href="http://alloytools.org/code/EvaluatorExample.java.html" style="color: rgb(20, 119, 203); text-decoration: none;">the evaluator</a></td></tr><tr style="background-color: rgb(247, 247, 247);"><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/tutorials/online" style="color: rgb(20, 119, 203); text-decoration: none;">online tutorial</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">A step-by-step walkthrough and tutorial for Alloy 4</td></tr><tr><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://alloytools.org/tutorials/day-course" style="color: rgb(20, 119, 203); text-decoration: none;">tutorial slides</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">Slides for day-long tutorial by Rob Seater and Greg Dennis</td></tr><tr style="background-color: rgb(247, 247, 247);"><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);"><a href="http://blackmesatech.com/2013/07/alloy/" style="color: rgb(20, 119, 203); text-decoration: none;">digital humanities tutorial</a></td><td style="padding: 10px 15px; border: 1px solid rgb(232, 232, 232);">A tutorial introducing Alloy for digital humanities work, by C. M. Sperberg-McQueen</td></tr></tbody></table>

















For more information about Alloy, http://alloytools.org

Questions and comments about Alloy are welcome at the community forum:

Alloy Community Forum: https://groups.google.com/forum/#!forum/alloytools

Alloy experts also respond to https://stackoverflow.com questions tagged alloy.


The official [Alloy website](http://alloytools.org/) provides links to downloads, tutorials and case studies.

A recent [CACM paper](https://cacm.acm.org/magazines/2019/9/238969-alloy/abstract) gives an overview of Alloy and its applications to date, and is accompanied by a video showing Alloy in action.

Some recent applications include: [exploiting Spectre/Meltdown](https://arxiv.org/pdf/1802.03802.pdf), [game design](https://www.hillelwayne.com/post/alloy-randomizer/),[memory models](https://johnwickerson.github.io/papers/memalloy.pdf), [peer-to-peer](https://arxiv.org/abs/1502.06461),[storm surge protection](http://www4.ncsu.edu/~jwb/papers/baugh-abz-2016.pdf), [radiotherapy](https://homes.cs.washington.edu/~ztatlock/pubs/neutrons-pernsteiner-cav16.pdf).




Alloy是描述结构的语言,也是探索结构的工具。从发现安全机制的漏洞到设计电话交换网络,它已被广泛用于各种应用中。该存储库包含该工具的代码。

github可以直接下载release

简短教程 https://www.ics.uci.edu/~alspaugh/cls/shr/alloy.html

官网: alloytools.org/download.html

https://github.com/AlloyTools

https://github.com/AlloyTools/alloytools.github.io

https://github.com/AlloyTools/org.alloytools.alloy

https://github.com/AlloyTools/models

一个公共存储库,用于托管Alloy模型。该存储库拥有用作娱乐的公共模型,示例,教程,实用程序和证明。

https://github.com/AlloyTools/org.alloytools.alloy/releases


## 1.1. sat solver求解器
旧版有：

```
BerkMin
MiniSat
MiniSat with Unsat Core
ZChaff
SAT4J
Output CNF to file
Output Kodkod to file
```

新版有：

```
Glucose41
PLingeling
SAT4J
Output CNF to file
Output Kodkod to file
```















## 1.2. demo
CTRL + ALT + O


`tree /a`

```
+---book
|   +---appendixA
|   +---appendixE
|   +---chapter2
|   +---chapter4
|   +---chapter5
|   \---chapter6
|       \---memory
+---examples
|   +---algorithms
|   +---case_studies
|   +---puzzles
|   +---systems
|   +---toys
|   \---tutorial
\---util

```


直接打开example就有：
`tree /f`

```
├─book
│  ├─appendixA
│  │      addressBook1.als
│  │      addressBook2.als
│  │      barbers.als
│  │      closure.als
│  │      distribution.als
│  │      phones.als
│  │      prison.als
│  │      properties.als
│  │      ring.als
│  │      spanning.als
│  │      tree.als
│  │      tube.als
│  │      undirected.als
│  │
│  ├─appendixE
│  │      hotel.thm
│  │      p300-hotel.als
│  │      p303-hotel.als
│  │      p306-hotel.als
│  │
│  ├─chapter2
│  │      addressBook1a.als
│  │      addressBook1b.als
│  │      addressBook1c.als
│  │      addressBook1d.als
│  │      addressBook1e.als
│  │      addressBook1f.als
│  │      addressBook1g.als
│  │      addressBook1h.als
│  │      addressBook2a.als
│  │      addressBook2b.als
│  │      addressBook2c.als
│  │      addressBook2d.als
│  │      addressBook2e.als
│  │      addressBook3a.als
│  │      addressBook3b.als
│  │      addressBook3c.als
│  │      addressBook3d.als
│  │      theme.thm
│  │
│  ├─chapter4
│  │      filesystem.als
│  │      grandpa1.als
│  │      grandpa2.als
│  │      grandpa3.als
│  │      lights.als
│  │
│  ├─chapter5
│  │      addressBook.als
│  │      lists.als
│  │      sets1.als
│  │      sets2.als
│  │
│  └─chapter6
│      │  hotel.thm
│      │  hotel1.als
│      │  hotel2.als
│      │  hotel3.als
│      │  hotel4.als
│      │  mediaAssets.als
│      │  ringElection.thm
│      │  ringElection1.als
│      │  ringElection2.als
│      │
│      └─memory
│              abstractMemory.als
│              cacheMemory.als
│              checkCache.als
│              checkFixedSize.als
│              fixedSizeMemory.als
│              fixedSizeMemory_H.als
│
├─examples
│  ├─algorithms
│  │      dijkstra.als
│  │      messaging.als
│  │      opt_spantree.als
│  │      peterson.als
│  │      ringlead.als
│  │      stable_mutex_ring.als
│  │      stable_orient_ring.als
│  │      stable_ringlead.als
│  │      s_ringlead.als
│  │
│  ├─case_studies
│  │      chord.als
│  │      chord2.als
│  │      chordbugmodel.als
│  │      com.als
│  │      firewire.als
│  │      firewire.thm
│  │      ins.als
│  │
│  ├─puzzles
│  │      farmer.thm
│  │      handshake.als
│  │      handshake.thm
│  │      hanoi.thm
│  │
│  ├─systems
│  │      file_system.als
│  │      file_system.thm
│  │      javatypes_soundness.als
│  │      lists.als
│  │      lists.thm
│  │      marksweepgc.als
│  │      views.als
│  │
│  ├─toys
│  │      birthday.thm
│  │      ceilingsAndFloors.als
│  │      ceilingsAndFloors.thm
│  │      genealogy.thm
│  │      grandpa.thm
│  │      life.thm
│  │      numbering.als
│  │      railway.thm
│  │
│  └─tutorial
│          farmer.als
│
└─util
        boolean.als
        graph.als
        integer.als
        natural.als
        ordering.als
        relation.als
        seqrel.als
        sequence.als
        sequniv.als
        ternary.als
        time.als

```

## 1.3. alloy过河问题论文

```
module examples/tutorial/farmer

/*
 * The classic river crossing puzzle. A farmer is carrying a fox, a
 * chicken, and a sack of grain. He must cross a river using a boat
 * that can only hold the farmer and at most one other thing. If the
 * farmer leaves the fox alone with the chicken, the fox will eat the
 * chicken; and if he leaves the chicken alone with the grain, the
 * chicken will eat the grain. How can the farmer bring everything
 * to the far side of the river intact?
 *
 * authors: Greg Dennis, Rob Seater
 *
 * Acknowledgements to Derek Rayside and his students for finding and
 * fixing a bug in the "crossRiver" predicate.
 */

open util/ordering[State] as ord

/**
 * The farmer and all his possessions will be represented as Objects.
 * Some objects eat other objects when the Farmer's not around.
 */
abstract sig Object { eats: set Object }
one sig Farmer, Fox, Chicken, Grain extends Object {}

/**
 * Define what eats what when the Farmer' not around.
 * Fox eats the chicken and the chicken eats the grain.
 */
fact eating { eats = Fox->Chicken + Chicken->Grain }

/**
 * The near and far relations contain the objects held on each
 * side of the river in a given state, respectively.
 */
sig State {
   near: set Object,
   far: set Object
}

/**
 * In the initial state, all objects are on the near side.
 */
fact initialState {
   let s0 = ord/first |
     s0.near = Object && no s0.far
}

/**
 * Constrains at most one item to move from 'from' to 'to'.
 * Also constrains which objects get eaten.
 */
pred crossRiver [from, from', to, to': set Object] {
   // either the Farmer takes no items
   (from' = from - Farmer - from'.eats and
    to' = to + Farmer) or
    // or the Farmer takes one item
    (one x : from - Farmer | {
       from' = from - Farmer - x - from'.eats
       to' = to + Farmer + x })
}

/**
 * crossRiver transitions between states
 */
fact stateTransition {
  all s: State, s': ord/next[s] {
    Farmer in s.near =>
      crossRiver[s.near, s'.near, s.far, s'.far] else
      crossRiver[s.far, s'.far, s.near, s'.near]
  }
}

/**
 * the farmer moves everything to the far side of the river.
 */
pred solvePuzzle {
     ord/last.far = Object
}

run solvePuzzle for 8 State expect 1

/**
 * no Object can be in two places at once
 * this is implied by both definitions of crossRiver 
 */
assert NoQuantumObjects {
   no s : State | some x : Object | x in s.near and x in s.far
}

check NoQuantumObjects for 8 State expect 0
```

一篇水期刊的例子


```
open util/ordering[State]·
/*定义农夫和他的财产为Object.*/
abstract sig Object{eats:set Object}
one sig Farmer,Fox,Chicken,Grain extends Object
/* }} */
/*约束当农夫不在时,三个对象吃与被吃的关系.*/
fact eating { eats = Fox -> Chicken + Chicken -> Grain}
/*定义河的两岸.*/
sig State {near,far:set Object}
/*定义初始状态时,所有对象都未过河。*/
fact {first.near = Object && no first.far}
/*农夫至多只能带一个他的财产过河*/
pred crossRiver[from,from',to,to':set Object]{
    one x:from {
        from' = from - x - Farmer - from'.eats
        to' = to + x + Farmer
    }
}
/*约束过河的状态转移关系*/
fact {
  all s:State,s' : s.next{
    Farmer in s.near=>
        crossRiver[s.near,s'.near,s.far,s'.far]
    else 
        crossRiver[s.far,s'.far,s.near,s'.near]
  }
}
/*规定所有对象都过河时状态转移才能完成.*/
run {last.far=Object} for exactly 8 State

```


### 1.3.1. 求解复杂过河问题

```
/*签名的声明.*/
abstract sig Object { risk1,risk2,risk3:set Object}
one sig Cop,Dad,Mum,Criminal,Girll,Girl2,Boyl,Boy2,Boat extends Object
/* }} */
/*约束对象之间的利害关系.*/
fact risks{
risk1 = Criminal -> (Dad + Mum+Girll+Girl2+Boyl+Boy2)
risk2 = Mum -> (Boyl+Boy2)
risk3 = Dad -> (Girll+Girl2)
/*判断利害关系是否成立。*/
pred risking[sx:set Object]{
Cop ! in sx => sx = sx - sx.riskl
Dad ! in sx => sx = sx - sx.risk2
Mum ! in sx => sx = sx - sx.risk3
}
/*定义河的两岸。*/
sig State{
near:set Object,
far:set Object
}
/*定义初始状态时,所有对象都未过河。*/
fact { first.near=Object && no first.far}
pred crossRiver[from,from',to,to':set Object]{
/*只有一个人过河时,此人必须会开船.*/
(one d:from - Boat - (Criminal + Girll + Girl2 + Boyl + Boy2){
    {
        from' = from - d - Boat
        risking[from']
        to'=to+d+Boat 
        risking[to']
    } )
}
/*两个人过河时,必须有一个会开船.*/
(some ds : from - (Criminal + Girll + Girl2 + Boyl + Boy2 + Boat)
| onex:from-Boat |
    {
        from' = from - ds - x - Boat 
        risking[from']
        to' = to + ds + x + Boat 
        risking[to']
    })
}/*妈耶，这高损括号不匹配*/
/*过河的状态转移关系.*/
fact{
all s:State,s':s.next {
        Boat in s.near=>
        crossRiver[s.near,s'.near,s.far,s'.far] else 
        crossRiver[s.far,s'.far,s.near,s'.near]
    }
}
/*规定所有对象都过河时状态转移才能完成.*/
run { last.far=Object } for exactly 18 State
```






