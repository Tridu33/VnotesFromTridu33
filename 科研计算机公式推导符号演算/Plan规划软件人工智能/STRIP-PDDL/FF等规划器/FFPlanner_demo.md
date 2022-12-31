[TOC]


[书模板编程](https://wizardforcel.gitbooks.io/effective-cpp/content/50.html)


# 1. pddl--- FF Planner
Planning Domain Definition Language


FF Planer online： http://editor.planning.domains/#      注意不要使用https，否则会报malformed url




pddl语法：

基本内容：

•	Domain Name
•	Requirements
•	Types
•	Constants
•	Domain Variables
•	Predicates
•	Actions

以下图为例









演示demo


- spare tire


domain_spare_tire_d.pddl


```pddl
；给出domain名称，语法使用就是(domain 名称)
(define (domain spare_tire )
   ;给出依赖项，比如这里的三个都是依赖项，语法使用是“:依赖项”,
   ;strip---The most basic subset of PDDL, consisting of STRIPS only
   ;equality---This requirement means that the domain uses the predicate =, interpreted as equality.
   ;typing---This requirement means that the domain uses types (see Typing below).
   ;adl---Means that the domain uses some or all of ADL (i.e. disjunctions and quantifiers in preconditions and goals, quantified and conditional effects).
   (:requirements : strips : equality : typing )
   (:types physob location )
   ；定义该domain当中需要使用的类型，比如physic object、location都是类型，直接将你需要定义的类型加入到:type的后面
   (:predicates  ( Tire ?x − physob)
                  ( at ?x − physob ?y − location ))
   ；定义该domain需要使用的谓词，单元谓词表示属性，如这里的Tire x表示x这个physic object是否有轮胎属性。
   ；谓词名称最先给出，然后依次给出该谓词的项，格式为“？参数 – 参数类型”，
   ；比如这里的“？x – physob ？y – physob”表示x这个参数的类型应该是physob的，不能传递其他类型的参数。
   ；整个“Tire ？x – physob”对应Tire(x)这一原子（公式）。
   ；二元谓词表示关系，比如这里的at表示x物体是否在y这个位置，分析与上面的单元谓词类似


    (:action Remove
    :parameters (?x − physob ?y − location )
    :precondition (At ?x ?y)
    :effect (and(not(At ?x ?y) ) (At ?x Ground) )
    )
    ;定义该domain中的操作，这里的remove表示移除操作，这个操作需要给定参数，参数定义规则与前面的谓词一样；
    ;action执行需要一定的前提条件，前提条件是一个逻辑表达式，
    ;根据其真值判断操作是否可以执行；
    ;最后执行这个操作会导致一定的结果，这在effect中指定，指定的effect会改写当前状态（相当于改写知识库中基础原子的真值）
    ;语法上来说，precondition后面可以给出原子公式的与或非组合，
    ;其中原子公式语法前面谓词说过了，非：（not 原子公式）；与：（and 原子公式1 原子公式2 等等）；或与and用法一致，把and换为or即可


    (:action PutOn
    :parameters (?x − physob)
    :precondition (and( Tire ?x) (At ?x Ground)
                   (not(At Flat Axle) ) )
    :effect (and(not(At ?x Ground) ) (At ?x Axle) ) 
    )

    (:action LeaveOvernight
    :effect (and(not(At Spare Ground) ) (not(At Spare Axle) )
             (not(At Spare Trunk) ) (not(At Flat Ground) )
             (not(At Flat Axle) ) (not(At Flat Trunk) )
             )
    )

)
```



spare_tire_p.pddl
```pddl
 (define (problem prob)
  (:domain spare_tire )
  (:objects Flat Spare −physob Axle Trunk Ground − location )
  (:init ( Tire Flat ) ( Tire Spare) (At Flat Axle) (At Spare Trunk) )
  (:goal (At Spare Axle) )
 )
```

- breiefcase world

forall和when的用法,首先讲一下这个domain的含义，然后将下面的forall和when用法

briefcase_d.pddl

```pddl
(define (domain briefcase)
    (:requirements :strips :equality :typing :conditional-effects)
    (:types location physob)
    (:constants B - physob)
    (:predicates (at ?x - physob ?l - location) (in ?x - physob))
    (:action mov-b
        :parameters (?m ?l - location)
        :precondition (and (at B ?m) (not (= ?m ?l)))
        :effect (and (at B ?l) (not (at B ?m))
                    ;注意到写在effect中的这段代码：
                    (forall (?z - physob)
                        (when (and (in ?z) (not (= ?z B)))
                            ;这里意思就是遍历所有的object z，当z在B中，就产生effect
                            ;即将z的位置location设置为l（因为z在briefcase当中，briefcase被携带到了l地点，那么z自然也被移动到l）
                            (and (at ?z ?l) (not (at ?z ?m)))
                            ;这里必须使用forall，因为你无法设置是哪个对象在briefcase中，所以需要遍历判断
                        )
                    )
                ) 
    )
    (:action put-in
        :parameters (?x - physob ?l - location)
        :precondition (not (= ?x B))
        :effect (when (and (at ?x ?l) (at B ?l))
            (in ?x)) 
    )
    (:action take-out
        :parameters (?x - physob)
        :precondition (not (= ?x B))
        :effect (not (in ?x))
    )
)

```

然后就是数据文件，给出这个问题的定义：

它涉及的domain、
问题的参数定义、
问题的初始状态、
问题的目标状态

定义好问题后我们调用求解器，他会给我们求解出一系列的action使得问题从初始状态到达目标状态（如果有解）


briefcase_p.pddl
```pddl
(define (problem get-paid)
    (:domain briefcase)
    (:objects P D -physob home office - location)
    (:init 
        (at B home) (at P home) (at D home) (in P)
    )
    (:goal (and (at B office) (at D office) (at P home)))
)

```

- 8-puzzle



domain_puzzle_d.pddl
```pddl
; Header  and  description
( define (domain puzzle )
    ; remove  requirements  that  are  not  needed
    (:requirements :strips :typing :conditional−effects :equality )
    (:types
    ;todo: enumerate types and their hierarchy here,e.g. car truck bus − vehicle
    num loc
    )
    ;un−comment  following   line  if  constants   are  needed
    ;( :constants  )
    (:predicates
    ; todo:   define  predicates  here
        ( at ?x − num ?y − loc )
        ( adjecent ?x − loc ?y − loc )
    )
    ;(:functions; todo:   define numeric  functions   here
    ;)
    ;define  actions   here
    (:action slide
        :parameters (?x − num ?y − loc ?z − loc )
        :precondition (and( at ?x ?y) ( at num0?z) ( adjecent ?y ?z) )
        :effect (and( at ?x ?z) ( at num0 ?y) (not( at ?x ?y) ) (not( at num0?z) ) )
    )
)    
```


domain_puzzle_p.pddl
```pddl
(define (problem prob) (: domain puzzle )
    (: objects
        num0 num1 num2 num3 num4 num5 num6 num7 num8 − num
        loc1 loc2 loc3 loc4 loc5 loc6 loc7 loc8 loc0 − loc
    )
    (: init
        ; todo:   put  the   initial   state ’ s   facts  and  numeric  values  here
        ( at num1 loc1 ) ( at num2 loc2 ) ( at num3 loc3 )
        ( at num7 loc4 ) ( at num8 loc5 ) ( at num0 loc6 )
        ( at num6 loc7 ) ( at num4 loc8 ) ( at num5 loc0 )
        ( adjecent loc1 loc2 ) ( adjecent loc2 loc1 )
        ( adjecent loc1 loc4 ) ( adjecent loc4 loc1 )
        ( adjecent loc2 loc3 ) ( adjecent loc3 loc2 )
        ( adjecent loc2 loc5 ) ( adjecent loc5 loc2 )
        ( adjecent loc3 loc6 ) ( adjecent loc6 loc3 )
        ( adjecent loc4 loc5 ) ( adjecent loc5 loc4 )
        ( adjecent loc4 loc7 ) ( adjecent loc7 loc4 )
        ( adjecent loc5 loc6 ) ( adjecent loc6 loc5 )
        ( adjecent loc5 loc8 ) ( adjecent loc8 loc5 )
        ( adjecent loc6 loc0 ) ( adjecent loc0 loc6 )
        ( adjecent loc7 loc8 ) ( adjecent loc8 loc7 )
        ( adjecent loc8 loc0 ) ( adjecent loc0 loc8 )
    )

    (: goal (and
        ; todo:   put  the   goal  condition   her e
        ( at num1 loc1 ) ( at num2 loc2 ) ( at num3 loc3 )
        ( at num4 loc4 ) ( at num5 loc5 ) ( at num6 loc6 )
        ( at num7 loc7 ) ( at num8 loc8 ) ( at num0 loc0 )
        ) 
    )

    ; un−comment  the   following   line  if  metric  is  needed
    ; ( : metric minimize  ( ? ? ? ) )
)

```



- blockworld

There are a collection of blocks: a block can be on the table, or on the top of another block.

There are three predicates

:•clear(x): there is no block on top of block x;

•on(x,y): block x is on the top of block y;

•onTable(x): block x is on the table

There are two actions in this task:

•move(x,y): move block x onto block y, provided that both x and y are clear;

•moveToTable(x): move block x on to the table, provided that x is clear and x is not on thetable;


Give initial state and goal state, find the actions change the initial state to the goal state.



domain_blocks_d.pddl

```pddl
; Header  and  description
( define (domain blocks )
    ;remove  requirements  that  are  not  needed
    (:requirements :strips :typing :conditional−effects :equality :universal−preconditions : negative−preconditions )
    (:types
        ; todo: enumerate types and their  hierarchy here , e.g. car truckbus  −  vehicle
        physob
    )

    ;un−comment following  line  if constants are  needed
    ;( :constants  )

    (:predicates; todo: define  predicates here
        (ontable ?x − physob)
        (clear ?x − physob)
        (on ?x ?y − physob)
    )

    ;(:functions; todo:define numeric functions here
    ;)

    ;define actions here
    (:action move
        :parameters (?x ?y − physob)
        :precondition (and( clear ?x) ( clear ?y) )
        :effect (and(on ?x ?y) (not( clear ?y) )
            (when( ontable ?x) (not( ontable ?x) ) )
            (forall (?z − physob) (when(on ?x ?z) (and(not(on ?x ?z) ) (clear ?z) ) ) )
        )
    )

    (:action moveToTable
        :parameters (?x − physob)
        :precondition (and( clear ?x) (not( ontable ?x) ) )
        :effect (and(not( clear ?x) ) ( ontable ?x)
        ( forall (?z − physob) (when(on ?x ?z) (and(not(on ?x ?z) ) (clear ?z) ) ) )
        )
    )
)
```


domain_blocks_p.pddl
```pddl
(define (problem prob) (:domain blocks)
    (:objects
        A B C D E F − physob
    )
    (:init
        ; todo :put  the   initial   state ’ s   facts  and  numeric  values   here
        (clear A) (on A B) (on B C) (ontable C) (ontable D)
        (ontable F) (on E D) (clear E) (clear F)
    )
    (:goal (and
        ; todo :   put  the   goal   condition   here
        (clear F) (on F A) (on A C) (ontable C) (clear E)
        (on E B) (on B D) (ontable D)
        )
    )
    ;un−comment  the   following   line   if   metric   is   needed
    ;(:metric  minimize  ( ? ? ? ) )
)

```

FF规划器并不能生成最优的方案，例如在Puzzle问题中就出现了连续拨动数字6的情况，经过手动验证两个问题的Plan都是正确的。（注：代码中的注释由Vscode插件自动生成）







































