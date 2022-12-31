[TOC]

# stupid
## domain.pddl

```
(define (problem line-0)
(:domain line)
(:objects 
	L1 - location
	L2 - location
)
(:init
	(person-at L1)

	(road L1 L2)
	(road L2 L1)
)
(:goal (person-at L2))
)
```

problem 2 grid move right

```
; Stupid Examples for me to understand this programe 

(define (domain line)
  (:requirements :typing)
  (:types location)
  (:predicates (person-at ?loc - location)
               (road ?from - location ?to - location)
  )            
  (:action move
  ;move动作命名为move才合理。一开始例子没写好，反正后续“move”都理解为move就好。前提约束好像也有点小问题，但是不影响后续理解，就懒得改动了。
    :parameters (?from - location ?to - location)
    :precondition (and (person-at ?from) (road ?from ?to))
    :effect (and (person-at ?to) (not (person-at ?from)))
  )
)
```

```
/src$ python  main.py ../mystupidroad/domain.pddl  ../mystupidroad/stupid.pddl -strong 1 -policy 1
```
中间文件：

## 先生成sas文件

```
begin_version
3
end_version
begin_metric
0
end_metric
1
begin_variable
var0
-1
2
Atom person-at(l1)
Atom person-at(l2)
end_variable
1
begin_mutex_group
2
0 0
0 1
end_mutex_group
begin_state
0
end_state
begin_goal
1
0 1
end_goal
2
begin_operator
move l1 l2
0
1
0 0 0 1
0
end_operator
begin_operator
move l2 l1
0
1
0 0 1 0
0
end_operator
0
```

## 然后p=Parser()读取sas文件生成my_task()对象my_task数据对象存储结构：

```
>>> my_task.print_task()
ATOMS ================================================
(var0=1)
(var0=0)
INITIAL ==============================================
(var0=0)
GOAL =================================================
(var0=1)
ACTIONS ==============================================
('move(l1,l2)', [])
('move(l1,l2)', [['(var0=0)'], ['(var0=1)'], ['(var0=0)']])
('move(l2,l1)', [])
('move(l2,l1)', [['(var0=1)'], ['(var0=0)'], ['(var0=1)']])
>>> print(my_task.action_nondet)
{'move(l1,l2)': [], 'move(l2,l1)': []}
>>> print(my_task.action_cardinality)
{'move': 1, 'move(l1,l2)': 1, 'move(l2,l1)': 1}
>>> print(my_task.mutex_groups)
[['(var0=0)', '(var0=1)']]
>>> print(my_task.compatible_actions)
{'move(l1,l2)': set([]), 'move(l2,l1)': set([])}
>>> print(my_task.mutex_groups_set)
[set(['(var0=1)', '(var0=0)'])]
>>> print(my_task.relevant_actions_atom)
{'(var0=1)': set(['move(l1,l2)', 'move(l2,l1)']), '(var0=0)': set(['move(l1,l2)', 'move(l2,l1)'])}
>>> print(my_task.relevant_actions_atom_aname)
{}
>>> print(my_task.action_names)
set(['move'])
>>> print(my_task.other_actions_name)
{'move': []}
>>> print(my_task.action_name_to_actions)
{'move': ['move(l1,l2)', 'move(l2,l1)']}
```

## Clauses = 70  Variables = 26

实际的输出中：

```
SAT formula generation time = 0.000351
# Clauses = 70
# Variables = 26
```


然后在cnf=CNF类的对象输入my_task数据,


main.py大循环就是高潮部分：留意重点：

```
solver_time = []
for i in range(1000):
    cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)#文件formula-temp.txt这时候是空白的，formula-extra-temp此时空白，仅仅是传入地址方便最终结果存入数据
    ......
    cnf.reset()
    start_g = timer()
    cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)#生成子句Clauses和写入cnf文件合取范式的核心代码!!!
传入字符'n0', 终态'ng'
>>> print(controllerStates)
['n0', 'n1', 'ng']这个是3格的情况，2格的时候是['n0','ng']
>>> len(controllerStates)
3
>>> print(show_gen_info)
False懒得显示这部分，因为和我要关心的重点没关系
这里的p是Parser实例，可能用里面的方法，因为基本看着都是私有变量
    ......
    command = './minisat %s %s' % (name_formula_file, name_output_satsolver)#调用minisat
    ......
    result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)#读取文件name_output_satsolver : outsat-temp.txt输出结果
    ......
```



生成Fomula-temp.txt，和formula-temp.txtheader唯一区别第一行，cnf 1,1。里面保存着所有Clause的cnf格式合取范式公式编号，符号正负应该代表对应子式Clauses正负文字，

26Variables生成70Clauses的cnf文件


Variables 26

```
>>> cnf.printVariables()
reachableG(ng,0)
(ng,move,n0)
(ng,move(l1,l2))
reachableI(n0)
(n0,move)
(ng,move(l2,l1))
(n0,move,ng)
(ng,move,ng)
reachableI(ng)
reachableG(n0,0)
(var0=0)(n0)
(ng,move)
(n0,n0)
reachableG(ng,1)
YR1-n0-n0-0
(ng,n0)
(var0=0)(ng)
YR1-n0-ng-0
(var0=1)(n0)
(n0,move(l2,l1))
(ng,ng)
(n0,ng)
(n0,move,n0)
(var0=1)(ng)
(n0,move(l1,l2))
reachableG(n0,1)
```

```
p cnf 1 1
-1	0
2	0
-3	4	0
-5	1	0
-6	7	0
-8	2	0
-11	-12	0
-12	-11	0
-3	9	0
-5	9	0
-9	11	12	0
-9	3	5	0
-13	-14	0
-14	-13	0
-6	10	0
-8	10	0
-10	13	14	0
-10	6	8	0
-11	9	0
-12	9	0
-13	10	0
-14	10	0
9	0
-11	-5	-1	0
-15	1	-1	3	0
-11	-3	-4	0
-15	4	-4	5	0
-12	-5	-2	0
-16	1	-2	3	0
-12	-3	-7	0
-16	4	-7	5	0
-13	-8	-1	0
-17	2	-1	6	0
-13	-6	-4	0
-17	7	-4	8	0
-14	-8	-2	0
-18	2	-2	6	0
-14	-6	-7	0
-18	7	-7	8	0
-11	15	0
-15	11	0
-12	16	0
-16	12	0
-13	17	0
-17	13	0
-14	18	0
-18	14	0
19	0
-15	-19	19	0
-16	-19	20	0
-17	-20	19	0
-18	-20	20	0
-19	21	0
-20	22	0
23	0
22	0
-24	0
-24	21	0
-23	22	0
-25	-15	24	0
-24	25	0
15	25	0
-26	-16	23	0
-23	26	0
16	26	0
-21	25	0
-21	26	0
21	-25	-26	0
-4	-1	0
-7	-2	0

```



对应命题cnf就是Clauses 70


```
p cnf 1 1
'(var0=1)(n0)'	0
'(var0=1)(ng)'	0
负'(n0,move(l1,l2))'	'(var0=0)(n0)'	0
负'(n0,move(l2,l1))'	'(var0=1)(n0)'	0
负'(ng,move(l1,l2))'	'(var0=0)(ng)'	0
负'(ng,move(l2,l1))'	'(var0=1)(ng)'	0
负'(n0,move,n0)'	负'(n0,move,ng)'	0
负'(n0,move,ng)'	负'(n0,move,n0)'	0
负'(n0,move(l1,l2))'	'(n0,move)'	0
负'(n0,move(l2,l1))'	'(n0,move)'	0
负'(n0,move)'	'(n0,move,n0)'	'(n0,move,ng)'	0
负'(n0,move)'	'(n0,move(l1,l2))'	'(n0,move(l2,l1))'	0
负'(ng,move,n0)'	负'(ng,move,ng)'	0
负'(ng,move,ng)'	负'(ng,move,n0)'	0
负'(ng,move(l1,l2))'	'(ng,move)'	0
负'(ng,move(l2,l1))'	'(ng,move)'	0
负'(ng,move)'	'(ng,move,n0)'	'(ng,move,ng)'	0
负'(ng,move)'	'(ng,move(l1,l2))'	'(ng,move(l2,l1))'	0
负'(n0,move,n0)'	'(n0,move)'	0
负'(n0,move,ng)'	'(n0,move)'	0
负'(ng,move,n0)'	'(ng,move)'	0
负'(ng,move,ng)'	'(ng,move)'	0
'(n0,move)'	0
负'(n0,move,n0)'	负'(n0,move(l2,l1))'	'(var0=1)(n0)'	0
负'(n0,n0)'	'(var0=1)(n0)'	'(var0=1)(n0)'	'(n0,move(l1,l2))'	0
负'(n0,move,n0)'	负'(n0,move(l1,l2))'	负'(var0=0)(n0)'	0
负'(n0,n0)'	'(var0=0)(n0)'	负'(var0=0)(n0)'	'(n0,move(l2,l1))'	0
负'(n0,move,ng)'	负'(n0,move(l2,l1))'	负'(var0=1)(ng)'	0
负'(n0,ng)'	'(var0=1)(n0)'	负'(var0=1)(ng)'	'(n0,move(l1,l2))'	0
负'(n0,move,ng)'	负'(n0,move(l1,l2))'	负'(var0=0)(ng)'	0
负'(n0,ng)'	'(var0=0)(n0)'	负'(var0=0)(ng)'	'(n0,move(l2,l1))'	0
负'(ng,move,n0)'	负'(ng,move(l2,l1))'	'(var0=1)(n0)'	0
负'(ng,n0)'	'(var0=1)(ng)'	'(var0=1)(n0)'	'(ng,move(l1,l2))'	0
负'(ng,move,n0)'	负'(ng,move(l1,l2))'	负'(var0=0)(n0)'	0
负'(ng,n0)'	'(var0=0)(ng)'	负'(var0=0)(n0)'	'(ng,move(l2,l1))'	0
负'(ng,move,ng)'	负'(ng,move(l2,l1))'	负'(var0=1)(ng)'	0
负'(ng,ng)'	'(var0=1)(ng)'	负'(var0=1)(ng)'	'(ng,move(l1,l2))'	0
负'(ng,move,ng)'	负'(ng,move(l1,l2))'	负'(var0=0)(ng)'	0
负'(ng,ng)'	'(var0=0)(ng)'	负'(var0=0)(ng)'	'(ng,move(l2,l1))'	0
负'(n0,move,n0)'	'(n0,n0)'	0
负'(n0,n0)'	'(n0,move,n0)'	0
负'(n0,move,ng)'	'(n0,ng)'	0
负'(n0,ng)'	'(n0,move,ng)'	0
负'(ng,move,n0)'	'(ng,n0)'	0
负'(ng,n0)'	'(ng,move,n0)'	0
负'(ng,move,ng)'	'(ng,ng)'	0
负'(ng,ng)'	'(ng,move,ng)'	0
'reachableI(n0)'	0
负'(n0,n0)'	负'reachableI(n0)'	'reachableI(n0)'	0
负'(n0,ng)'	负'reachableI(n0)'	'reachableI(ng)'	0
负'(ng,n0)'	负'reachableI(ng)'	'reachableI(n0)'	0
负'(ng,ng)'	负'reachableI(ng)'	'reachableI(ng)'	0
负'reachableI(n0)'	'reachableG(n0,1)'	0
负'reachableI(ng)'	'reachableG(ng,1)'	0
'reachableG(ng,0)'	0
'reachableG(ng,1)'	0
负'reachableG(n0,0)'	0
负'reachableG(n0,0)'	'reachableG(n0,1)'	0
负'reachableG(ng,0)'	'reachableG(ng,1)'	0
负'YR1-n0-n0-0'	负'(n0,n0)'	'reachableG(n0,0)'	0
负'reachableG(n0,0)'	'YR1-n0-n0-0'	0
'(n0,n0)'	'YR1-n0-n0-0'	0
负'YR1-n0-ng-0'	负'(n0,ng)'	'reachableG(ng,0)'	0
负'reachableG(ng,0)'	'YR1-n0-ng-0'	0
'(n0,ng)'	'YR1-n0-ng-0'	0
负'reachableG(n0,1)'	'YR1-n0-n0-0'	0
负'reachableG(n0,1)'	'YR1-n0-ng-0'	0
'reachableG(n0,1)'	负'YR1-n0-n0-0'	负'YR1-n0-ng-0'	0
负'(var0=0)(n0)'	'(var0=1)(n0)'	0
负'(var0=0)(ng)'	负'(var0=1)(ng)'	0
```


cnf.py

```
	###########################################
	############## GENERATION #################
	###########################################

	#def generate_clauses(self, task, initialCState, goalCState, controllerStates, k, parser = None, debug = False):
	def generate_clauses(self, task, initialCState, goalCState, controllerStates, k, parser = None, debug = True):
		self.generateInitial(task, initialCState, debug)
		self.generateGoal(task, goalCState, debug)
		self.generatePreconditions(task, controllerStates, debug)
		self.generatePossibleNonDet(task, controllerStates, debug)
		self.generateOneSuccessor(task, controllerStates, debug)
		self.generateTripletForcesBin(task, controllerStates, debug)
		self.generateAtLeastOneAction(task, controllerStates, debug)
		self.generateNegativeForwardPropagation(task, controllerStates, debug)
		self.generateGeneralizeConnection(task, controllerStates, debug)
		self.generateReachableIClauses(task, initialCState, controllerStates, k, debug)
		self.generateReachableGClauses(task, controllerStates, goalCState, k, debug)
		self.generateSymmetryBreaking(task, controllerStates, initialCState, goalCState, debug)
		self.generateMutexGroupsClauses(task, controllerStates, debug)
```

 
 ###  cnf.26Variables --> 70Clauses
 
对应的子句生成如下所示：

```
>>> cnf.reset()
p cnf 1 1
>>> start_g = timer()
>>> task=my_task
>>> initialCState='n0'
>>> goalCState='ng'
>>> debug=True
>>> k=len(controllerStates)
```

```
self.generateInitial(task, initialCState, debug)
# -p(n0) for all p not in initial state
```

结果

```
>>> cnf.generateInitial(task, initialCState, debug)
-1	0
负'(var0=1)(n0)'	0
Generation: Initial              v 1             c : 1           0.000241
```


```
self.generateGoal(task, goalCState, debug)
# p(ng) for all p in goal state
```

结果

```
>>> cnf.generateGoal(task, goalCState, debug)
2	0
'(var0=1)(ng)'  0
Generation: Goal                 v 1             c : 1           0.000200
```


```
self.generatePreconditions(task, controllerStates, debug)
# p(ng) for all p in goal state
```

结果

```
>>> cnf.generatePreconditions(task, controllerStates, debug)
-3	4	0
-5	1	0
-6	7	0
-8	2	0
负'(n0,move(l1,l2))' 	'(var0=0)(n0)'	0
负'(n0,move(l2,l1))' 	1	0
负'(ng,move(l1,l2))'	'(var0=0)(ng)'	0
负'(ng,move(l2,l1))'	'(var0=1)(ng)' 	0
```


```
self.generatePossibleNonDet(task, controllerStates, debug)
# 1. (n, act) --> (n, act') // act, act' are non det act of equal det action (action names)
# 2. (n, act) --> -(n, act'') //
# 3. (n, b) --> (n, b') // b, b' are siblings
# 4. (n, b) --> -(n, b'') // b, b'' belong to same act
```
结果

```
>>> cnf.generatePossibleNonDet(task, controllerStates, debug)
Generation: Non Det              v 2             c : 0           0.000035

```



```
self.generateOneSuccessor(task, controllerStates, debug)
# 1. (n, act) --> \OR_{b} (n, b) // for b with name act
# 2. (n, act) --> \OR_{n'} (n, act, n')
# 3. -(n, act, n') \lor -(n, act, n'')
# 4. (n, b) --> (n, act)
```


结果

```
>>> cnf.generateOneSuccessor(task, controllerStates, debug)
-11	-12	0
-12	-11	0
-3	9	0
-5	9	0
-9	11	12	0
-9	3	5	0
-13	-14	0
-14	-13	0
-6	10	0
-8	10	0
-10	13	14	0
-10	6	8	0
负'(n0,move,n0)' 	负'(n0,move,ng)' 	0
负'(n0,move,ng)' 	负'(n0,move,n0)' 	0
负'(n0,move(l1,l2))' 	'(n0,move)'	0
负'(n0,move(l2,l1))' 	'(n0,move)'	0
负'(n0,move)'	'(n0,move,n0)' 	'(n0,move,ng)' 	0
负'(n0,move)'	'(n0,move(l1,l2))' 	'(n0,move(l2,l1))' 	0
负'(ng,move,n0)'	负'(ng,move,ng)'	0
负'(ng,move,ng)'	负'(ng,move,n0)'	0
负'(ng,move(l1,l2))'	'(ng,move)' 	0
负'(ng,move(l2,l1))'	'(ng,move)' 	0
负'(ng,move)' 	'(ng,move,n0)'	'(ng,move,ng)'	0
负'(ng,move)' 	'(ng,move(l1,l2))'	'(ng,move(l2,l1))'	0
Generation: One succ             v 4             c : 12                  0.085124

```

```
self.generateTripletForcesBin(task, controllerStates, debug)
# (n, act, n') --> (n, act)
```

结果

```
>>> cnf.generateTripletForcesBin(task, controllerStates, debug)
-11	9	0
-12	9	0
-13	10	0
-14	10	0
负'(n0,move,n0)' 	'(n0,move)'	0
负'(n0,move,ng)' 	'(n0,move)'	0
负'(ng,move,n0)'	'(ng,move)' 	0
负'(ng,move,ng)'	'(ng,move)' 	0
Generation: Trip bin             v 0             c : 4           0.030731

```


```
self.generateAtLeastOneAction(task, controllerStates, debug)
# \OR_{act_name} (n, act) for all n except goal, ng
```

结果

```
>>> cnf.generateAtLeastOneAction(task, controllerStates, debug)
9	0
'(n0,move)'	0
Generation: One act              v 0             c : 1           0.005008

```



```
self.generateNegativeForwardPropagation(task, controllerStates, debug)
# 1. (n, act, n') \land (n, b) --> -p(n') // if p in delete list
# 2. (n, n') \land -p(n) --> -p(n') \lor \OR_{b: p \in add(b)} (n, b)
# 3. (n, act, n') \land (n, b) \land -p(n) --> -p(n') // if p \not \in add(b) 
# and some sibling of b adds p
# for a in actions:
#	print(a, task.get_del_list(a))
#	print(a, task.get_add_list(a))
```

2.(n, n') $\land$  -p(n)  -->  -p(n') $\lor$ $\lor_{b: p \in add(b)}$ （n,b）
结果

```
>>> cnf.generateNegativeForwardPropagation(task, controllerStates, debug)
-11	-5	-1	0
-15	1	-1	3	0
-11	-3	-4	0
-15	4	-4	5	0
-12	-5	-2	0
-16	1	-2	3	0
-12	-3	-7	0
-16	4	-7	5	0
-13	-8	-1	0
-17	2	-1	6	0
-13	-6	-4	0
-17	7	-4	8	0
-14	-8	-2	0
-18	2	-2	6	0
-14	-6	-7	0
-18	7	-7	8	0
负'(n0,move,n0)' 	负'(n0,move(l2,l1))' 	负'(var0=1)(n0)'	0
负'(n0,n0)'	'(var0=1)(n0)'	负'(var0=1)(n0)'	'(n0,move(l1,l2))' 	0
负'(n0,move,n0)' 	负'(n0,move(l1,l2))' 	负'(var0=0)(n0)'	0
负'(n0,n0)'	'(var0=0)(n0)'	负'(var0=0)(n0)'	'(n0,move(l2,l1))' 	0
负'(n0,move,ng)' 	负'(n0,move(l2,l1))' 	负'(var0=1)(ng)' 	0
负'(n0,ng)'	'(var0=1)(n0)'	负'(var0=1)(ng)' 	'(n0,move(l1,l2))' 	0
负'(n0,move,ng)' 	负'(n0,move(l1,l2))' 	负'(var0=0)(ng)'	0
负'(n0,ng)'	'(var0=0)(n0)'	负'(var0=0)(ng)'	'(n0,move(l2,l1))' 	0
负'(ng,move,n0)'	负'(ng,move(l2,l1))'	负'(var0=1)(n0)'	0
负'(ng,n0)'	'(var0=1)(ng)' 	负'(var0=1)(n0)'	'(ng,move(l1,l2))'	0
负'(ng,move,n0)'	负'(ng,move(l1,l2))'	负'(var0=0)(n0)'	0
负'(ng,n0)'	'(var0=0)(ng)'	负'(var0=0)(n0)'	'(ng,move(l2,l1))'	0
负'(ng,move,ng)'	负'(ng,move(l2,l1))'	负'(var0=1)(ng)' 	0
负'(ng,ng)'	'(var0=1)(ng)' 	负'(var0=1)(ng)' 	'(ng,move(l1,l2))'	0
负'(ng,move,ng)'	负'(ng,move(l1,l2))'	负'(var0=0)(ng)'	0
负'(ng,ng)'	'(var0=0)(ng)'	负'(var0=0)(ng)'	'(ng,move(l2,l1))'	0
Generation: Neg Prop             v 4             c : 16                  0.135173

```


```
self.generateGeneralizeConnection(task, controllerStates, debug)
# (n, n') <--> \OR_{act} (n, act, n')
```

结果

```
>>> cnf.generateGeneralizeConnection(task, controllerStates, debug)
-11	15	0
-15	11	0
-12	16	0
-16	12	0
-13	17	0
-17	13	0
-14	18	0
-18	14	0
负'(n0,move,n0)' 	'(n0,n0)'	0
负'(n0,n0)'	'(n0,move,n0)' 	0
负'(n0,move,ng)' 	'(n0,ng)'	0
负'(n0,ng)'	'(n0,move,ng)' 	0
负'(ng,move,n0)'	'(ng,n0)'	0
负'(ng,n0)'	'(ng,move,n0)'	0
负'(ng,move,ng)'	'(ng,ng)'	0
负'(ng,ng)'	'(ng,move,ng)'	0
Generation: Gen conn             v 0             c : 8           0.048381

```


```
self.generateReachableIClauses(task, initialCState, controllerStates, k, debug)
```
结果

```
>>> cnf.generateReachableIClauses(task, initialCState, controllerStates, k, debug)
19	0
'reachableI(n0)'	0
Generation: RI init              v 1             c : 1           0.005257
-15	-19	19	0
-16	-19	20	0
-17	-20	19	0
-18	-20	20	0
负'(n0,n0)'	负'reachableI(n0)'	'reachableI(n0)'	0
负'(n0,ng)'	负'reachableI(n0)'	'reachableI(ng)'	0
负'(ng,n0)'	负'reachableI(ng)'	'reachableI(n0)'	0
负'(ng,ng)'	负'reachableI(ng)'	'reachableI(ng)'	0
Generation: RI prop              v 1             c : 4           0.030447
-19	21	0
-20	22	0
负'reachableI(n0)'	'reachableG(n0,1)'	0
负'reachableI(ng)'	'reachableG(ng,1)' 	0
Generation: IG prop              v 2             c : 2           0.007711

```



```

self.generateReachableGClauses(task, controllerStates, goalCState, k, debug)
		def generateReachableGClauses(self, task, controllerStates, goalCState, k, debug = True):
    		self.generateReachableGInitial(task, goalCState, controllerStates, k - 1, debug)
    		# ReachG(ng,0), ReachG(ng,1), ...
            # -ReachG(n, 0) for n != ng
            # set the initial values for goal state
            # set the negation for non goal states
    		self.generateCompletionReachabilityG(task, controllerStates, k - 1, debug)
    		# ReachG(n,j) --> ReachG(n, j+1)
    		if self.strong:
    			self.generatePropagationReachableGStrong(task, controllerStates, k - 1, debug)
    			# ReachG(n, j+1) <--> \AND_{n'} [(n,n') --> ReachG(n', j)]
    			# Force the equivalences
    			# Right arrow
    			# Left arrow
    		else:
    			if not self.fair:
    				self.generatePropagationReachableGUnfair(task, controllerStates, k - 1, debug)
    				# ReachG(n, j+1) <--> [1] 
        		# [1] = [2] \lor [3]
        		# [2] = (n, unfair) \land \AND_{n'} [(n,n') --> RG(n',j)]
        		# [3] = \OR_{n'} [(n, fair) \land (n,n') \land RG(n',j)]
        		c1, v1 = self.get_num_cl_vars()
        		start = timer()
        		# Set variables (n, fair) and (n, unfair)
        		self.setFairUnfairActions(task, controllerStates)
        		# Force the equivalences for [2]
        		# [(n,n') --> RG(n',j)] <-> Repl(n,n',j)
        		# Force the equivalences for [3]
                # [(n, fair) \land (n,n') \land RG(n',j)] <-> Repl3(n,n',j)
                # Right arrow
                # Left arrow
    			else:
    				self.generatePropagationReachableGCyclic(task, controllerStates, k - 1, debug)
    				# ReachG(n, j+1) <--> \OR_{n'} [(n,n') \land ReachG(n', j)]
        		c1, v1 = self.get_num_cl_vars()
        		start = timer()
        		# Force the equivalences
        		# Right arrow
        		# Left arrow
```


结果

```
>>> cnf.generateReachableGClauses(task, controllerStates, goalCState, k, debug)
23	0
22	0
-24	0
'reachableG(ng,0)'	0
'reachableG(ng,1)' 	0
负'reachableG(n0,0)' 	0
Generation: RG init              v 2             c : 3           0.009479
-24	21	0
-23	22	0
负'reachableG(n0,0)' 	'reachableG(n0,1)'	0
负'reachableG(ng,0)'	'reachableG(ng,1)' 	0
Generation: RG compl             v 0             c : 2           0.012321
-25	-15	24	0
-24	25	0
15	25	0
-26	-16	23	0
-23	26	0
16	26	0
-21	25	0
-21	26	0
21	-25	-26	0
负'YR1-n0-n0-0'	负'(n0,n0)'	'reachableG(n0,0)' 	0
负'reachableG(n0,0)' 	'YR1-n0-n0-0'	0
'(n0,n0)'	'YR1-n0-n0-0'	0
负'YR1-n0-ng-0'	负'(n0,ng)'	'reachableG(ng,0)'	0
负'reachableG(ng,0)'	'YR1-n0-ng-0'	0
'(n0,ng)'	'YR1-n0-ng-0'	0
负'reachableG(n0,1)'	'YR1-n0-n0-0'	0
负'reachableG(n0,1)'	'YR1-n0-ng-0'	0
'reachableG(n0,1)'	负'YR1-n0-n0-0'	负'YR1-n0-ng-0'	0
Generation: RG prop              v 2             c : 9           0.059131

```



```
self.generateSymmetryBreaking(task, controllerStates, initialCState, goalCState, debug)
# (na, nb) --> \OR_{i<=a} (n_i, n_{b-1})
```

结果

```
>>> cnf.generateSymmetryBreaking(task, controllerStates, initialCState, goalCState, debug)
Generation: Sym brk              v 0             c : 0           0.000004

```


```
self.generateMutexGroupsClauses(task, controllerStates, debug)
```

结果

```
>>> cnf.generateMutexGroupsClauses(task, controllerStates, debug)
-4	-1	0
-7	-2	0
负'(var0=0)(n0)'	负'(var0=1)(n0)'	0
负'(var0=0)(ng)'	负'(var0=1)(ng)' 	0
Generation: Mutex                v 0             c : 2           0.010046
```



## 通过调用minisat根据上cnf文件生成的outsat-temp.tx

land :$\land$

lor: $lor$

也就是说在命令行输入：

```
>./minisat formula-temp.txt outsat-temp.txt
[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |      21       69 |       7       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 0              (-nan /sec)
decisions             : 3              (inf /sec)
propagations          : 26             (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0 s

SATISFIABLE
```

根据上cnf文件生成的outsat-temp.txt

```
SAT
-1 2 3 4 -5 -6 -7 -8 9 -10 -11 12 -13 -14 -15 16 -17 -18 19 20 21 22 23 -24 25 26 0
```

也就是sat对应的公式结论
然后python读取这个满足cnf合取范式问题的可满足sat解，找到对应编号的公式翻译出来变成方案。



根据下面的


### 公式映射

```
>>> print(cnf.mapNumberVariable)
{1: '(var0=1)(n0)', 
2: '(var0=1)(ng)', 
3: '(n0,move(l1,l2))', 
4: '(var0=0)(n0)', 
5: '(n0,move(l2,l1))', 
6: '(ng,move(l1,l2))', 
7: '(var0=0)(ng)', 
8: '(ng,move(l2,l1))', 
9: '(n0,move)', 
10: '(ng,move)', 
11: '(n0,move,n0)', 
12: '(n0,move,ng)', 
13: '(ng,move,n0)', 
14: '(ng,move,ng)', 
15: '(n0,n0)', 
16: '(n0,ng)', 
17: '(ng,n0)', 
18: '(ng,ng)', 
19: 'reachableI(n0)', 
20: 'reachableI(ng)', 
21: 'reachableG(n0,1)', 
22: 'reachableG(ng,1)', 
23: 'reachableG(ng,0)', 
24: 'reachableG(n0,0)', 
25: 'YR1-n0-n0-0', 
26: 'YR1-n0-ng-0'}

>>> print(cnf.mapVariableType)
{'reachableG(ng,0)': 
5, '(ng,move,n0)': 
3, '(ng,move(l1,l2))': 
2, 'reachableI(n0)': 
4, '(n0,move)': 
2, '(ng,move(l2,l1))': 
2, '(n0,move,ng)': 
3, '(ng,move,ng)': 
3, 'reachableI(ng)': 
4, 'reachableG(n0,0)': 
5, '(var0=0)(n0)': 
1, '(ng,move)': 
2, '(n0,n0)': 
7, 'reachableG(ng,1)': 
5, 'YR1-n0-n0-0': 
6, '(ng,n0)': 
7, '(var0=0)(ng)': 
1, 'YR1-n0-ng-0': 
6, '(var0=1)(n0)': 
1, '(n0,move(l2,l1))': 
2, '(ng,ng)': 
7, '(n0,ng)': 
7, '(n0,move,n0)': 
3, '(var0=1)(ng)': 
1, '(n0,move(l1,l2))': 
2, 'reachableG(n0,1)': 5}

>>> print(cnf.mapVariableNumber)
{'reachableG(ng,0)': 
23, '(ng,move,n0)': 
13, '(ng,move(l1,l2))': 
6, 'reachableI(n0)': 
19, '(n0,move)': 
9, '(ng,move(l2,l1))': 
8, '(n0,move,ng)': 
12, '(ng,move,ng)': 
14, 'reachableI(ng)': 
20, 'reachableG(n0,0)': 
24, '(var0=0)(n0)': 
4, '(ng,move)': 
10, '(n0,n0)': 
15, 'reachableG(ng,1)': 
22, 'YR1-n0-n0-0': 
25, '(ng,n0)': 
17, '(var0=0)(ng)': 
7, 'YR1-n0-ng-0': 
26, '(var0=1)(n0)': 
1, '(n0,move(l2,l1))': 
5, '(ng,ng)': 
18, '(n0,ng)': 
16, '(n0,move,n0)': 
11, '(var0=1)(ng)': 
2, '(n0,move(l1,l2))': 
3, 'reachableG(n0,1)': 21}
```

```
SAT
-1 2 3 4 -5 -6 -7 -8 9 -10 -11 12 -13 -14 -15 16 -17 -18 19 20 21 22 23 -24 25 26 0
```

是这些cnf合取范式起来得到的结果

```
2: '(var0=1)(ng)', 
3: '(n0,move(l1,l2))', 
4: '(var0=0)(n0)', 
9: '(n0,move)', 
12: '(n0,move,ng)', 
16: '(n0,ng)', 
19: 'reachableI(n0)', 
20: 'reachableI(ng)', 
21: 'reachableG(n0,1)', 
22: 'reachableG(ng,1)', 
23: 'reachableG(ng,0)', 
25: 'YR1-n0-n0-0', 
26: 'YR1-n0-ng-0'}
```



```
===================
===================
Controller -- CS = Controller State
===================
===================
Atom (CS)
___________________
----------
Atom person-at(l1) (n0)
----------
Atom person-at(l2) (ng)
===================
===================
(CS, Action with arguments)
___________________
(n0,move(l1,l2))
(n0,move)
===================
===================
(CS, Action name, CS)
___________________
(n0,move,ng)
===================
(CS, CS)
___________________
(n0,ng)
===================
```








## 最终结果：

```
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |      21       69 |       7       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 0              (-nan /sec)
decisions             : 3              (inf /sec)
propagations          : 26             (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0 s

SATISFIABLE
Setting atoms
# Atoms: 2
Setting initial
Setting goal
Setting actions
# Actions: 2
	Setting other actions
(0, '/', 2)
	Setting action card
Setting mutexes
Setting relevant actions
Setting splitting
Setting compatible actions
(0, '/', 2)
2.88486480713e-05
=================================================
Trying with 2 states
Looking for strong plans: True
Fair actions: True
# Atoms: 2
# Actions: 2
SAT formula generation time = 0.000351
# Clauses = 70
# Variables = 26
Creating formula...
Done creating formula. Calling solver...
SAT solver called with 4096 MB and 3599 seconds
Done solver. Round time: 0.015620
Cumulated solver time: 0.015620

...

Solved with 2 states
Elapsed total time (s): 0.115060
Elapsed solver time (s): 0.015620
Elapsed solver time (s): [0.015619993209838867]
Looking for strong plans: True
Fair actions: True

```


# 我的stupid road demo run in Ipython/Jupyter

## main.py

```
from CNF import CNF
import os
import sys
from myTask import MyTask
from timeit import default_timer as timer
import time
import argparse
from parser import Parser 

def clean_and_exit(n1, n2, n3, n4, n5, msg):
	print(msg)
	os.system('rm %s %s %s %s %s' % (n1, n2, n3, n4, n5))
	exit()
	
def generateControllerStates(i):
	controllerStates = ['n0']
	for j in range(i):
		controllerStates.append('n' + str(j + 1))
	controllerStates.append('ng')
	return controllerStates
 
```

## 替换args输入参数字典，直接输入我想要的字典，包括传进去的数值参数

```
# my stuppid example:
params={'time_limit': 3600, 'inc': 1, 'path_domain': '../mystupidroad/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 1, 'path_instance': '../mystupidroad/stupid.pddl', 'name_temp': 'temp'}

#print params dictionary
#print(params)
#raw_input()
# Run code  below in ipython
# params={'time_limit': 3600, 'inc': 1, 'path_domain': '../F-domains/islands/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 0, 'path_instance': '../F-domains/islands/p03.pddl', 'name_temp': 'temp'}

# my stuppid example:
#params={'time_limit': 3600, 'inc': 1, 'path_domain': '../mystupidroad/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 1, 'path_instance': '../mystupidroad/stupid.pddl', 'name_temp': 'temp'}
```


```
time_start = timer()
time_limit = params['time_limit'] #3600 default 
time_buffer = 2
mem_limit = params['mem_limit'] #4096 default 
p = Parser()
p.set_domain(params['path_domain']) #path_domain 
p.set_problem(params['path_instance']) #path_instance 
name_formula_file = 'formula-' + params['name_temp'] + '.txt' 

#name_formula_file formula-temp.txt   formula-temp.txtheader       cnf diff In  --->   p cnf 656 7458 --- > p cnf 1 1

name_formula_file_extra = 'formula-extra-' + params['name_temp'] + '.txt' #name_formula_file_extra :formula-extra-temp.txt      blank
name_output_satsolver = 'outsat-' + params['name_temp'] + '.txt' #name_output_satsolver : outsat-temp.txt
name_sas_file = 'outputtrans-' + params['name_temp'] + '.sas' #name_sas_file   outputtrans-temp.sas

#time_limit 3600 default 
#mem_limit 4096 default 
#path_domain 
#path_instance 

# params={'time_limit': 3600, 'inc': 1, 'path_domain': '../F-domains/islands/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 0, 'path_instance': '../F-domains/islands/p03.pddl', 'name_temp': 'temp'}

# my stuppid example:
#params={'time_limit': 3600, 'inc': 1, 'path_domain': '../mystupidroad/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 0, 'path_instance': '../mystupidroad/stupid.pddl', 'name_temp': 'temp'}


# middle Files to be clean and exit
#name_formula_file :formula-temp.txt   formula-temp.txtheader       cnf  diff in ---> p cnf 656 7458 --- > p cnf 1 1
#name_formula_file_extra :formula-extra-temp.txt      blank
#name_output_satsolver : outsat-temp.txt
#name_sas_file ;outputtrans-temp.sas


p.generate_file(name_sas_file)
```

相当于命令行执行：

```
command = 'python translate/translate.py ' + str(time_limit) + ' ' + self.domain + ' ' + self.problem + ' ' + sas_file_name + ' | grep "noprint"'
```
## 使用domain文件和问题描述文件pddl通过translate.py生成翻译后的sas文件


```
begin_version
3
end_version
begin_metric
0
end_metric
1
begin_variable
var0
-1
2
Atom person-at(l1)
Atom person-at(l2)
end_variable
1
begin_mutex_group
2
0 0
0 1
end_mutex_group
begin_state
0
end_state
begin_goal
1
0 1
end_goal
2
begin_operator有多少个操作全部都写在这里，比如L3有4个操作
move l1 l2
0
1
0 0 0 1
0
end_operator
begin_operator
move l2 l1
0
1
0 0 1 0
0
end_operator
0这行固定的

```

接着

```
p.generate_task(name_sas_file) #读取sas文件，保存数据
>>> my_task = p.translate_to_atomic() #存进my_task类的实例对象my_task中
Setting atoms
# Atoms: 3
Setting initial
Setting goal
Setting actions
# Actions: 4
        Setting other actions
(0, '/', 4)
        Setting action card
Setting mutexes
Setting relevant actions
Setting splitting
Setting compatible actions
(0, '/', 4)
0.00387597084045
```

## 在Parser类的方法中翻译成，保存成mytask类的数据：
parser.py中p.translate_to_atomic

```
    task = MyTask()
    debug = False#这个应该是开发的时候方便调试可以设置True
    print('Setting atoms')#原子命题
    task.set_atoms(self.get_atoms(), debug)
    print('Setting initial')#初态
    task.set_initial(self.get_initial_atomic(), debug)
    print('Setting goal')#终态
    task.set_goal(self.get_goal_atomic(), debug)
    print('Setting actions')#设定动作
    task.set_actions_atomic(self.get_actions_atomic(), debug)
    print('Setting mutexes')#设定互斥量？
    task.set_mutex_groups(self.get_mutex_groups_atomic(), debug)
    print('Setting relevant actions')#设置相关动作
    task.set_relevant_actions(debug)
    print('Setting splitting')#分裂
    task.initialize_splitting(debug)
    start = timer()
    print('Setting compatible actions')#设置相容可以并存的动作
    task.create_compatible_actions(debug)
    print(timer() - start)
    return task
```

而查看my_task类中的局部变量

```
class MyTask():
	def __init__(self):
		self.atoms = None # Set
		self.initial = None # Set of atoms
		self.goal = None # Set of atoms
		self.actions = None # Dictionary, name --> [precs, adds, dels]
		self.action_nondet = {} # name --> list other actions
		self.action_cardinality = {} # name --> number
		self.mutex_groups = None # list of list; each sub-list has atoms belonging to the same mutex group
		self.compatible_actions = {} # action name --> set of compatible actions
		self.mutex_groups_set = [] # list of sets of mutex groups
		self.relevant_actions_atom = {} # dictionary: atom --> relevant actions
		self.relevant_actions_atom_aname = {} # dictionary: (atom, a_name) --> relevant actions
		self.action_names = None # set
		self.other_actions_name = {} # Dictionary name --> list of other actions
		self.action_name_to_actions = {} # action_name --> list of actions
		......
	def is_fair(self):
		for a in self.actions:
			if '_unfair_' in a:
				return False
		return True
		......
```

回到main.py

```
fair = my_task.is_fair()#判断True/False,demo p03 is True,本题设置为True

print_policy = True
if params['policy'] == 0:
	print_policy = False

strong = True
if params['strong'] == 0:
	strong = False

show_gen_info = True
if params['gen_info'] == 0:
	show_gen_info = False
#根据输入参数决定显示结果

cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)
#重点，根据公式文件formula-temp.txt这时候是空白的，formula-extra-temp此时空白，使用fair，strong取值决定策略
```

## 接下来这个大循环就是高潮部分：注意留意重点：

```
solver_time = []
for i in range(1000):
    cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)#文件formula-temp.txt这时候是空白的，formula-extra-temp此时空白，仅仅是传入地址方便最终结果存入数据
    ......
    cnf.reset()
	  start_g = timer()
    cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)#生成子句Clauses和写入cnf文件合取范式的核心代码!!!每次循环k追加nk,比如例子中controllerStates = ['n0', 'ng']
    ......
    command = './minisat %s %s' % (name_formula_file, name_output_satsolver)#调用minisat
    ......
    result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)#读取文件name_output_satsolver : outsat-temp.txt输出结果
    ......
```

因为大循环对打断，所以我在大循环区域上下加分割线

-------------------------------------------------------------

```
solver_time = []
for i in range(1000):
	if timer() - time_start > time_limit - time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')
	controllerStates = generateControllerStates(i * params['inc'])
	print('=================================================')
	print('Trying with %i states' % len(controllerStates))
	print('Looking for strong plans: %s' % str(strong))
	print('Fair actions: %s' % str(fair))
	print('# Atoms: %i' % len(my_task.get_atoms()))
	print('# Actions: %i' % len(my_task.get_actions()))
'''输出
第一遍
=================================================
Trying with 2 states
Looking for strong plans: True
Fair actions: True
# Atoms: 3
# Actions: 4
第二遍3 states有答案
=================================================
Trying with 3 states
Looking for strong plans: True
Fair actions: True
# Atoms: 3
# Actions: 4
'''
	cnf.reset()
	start_g = timer()
	cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
	print('SAT formula generation time = %f' % (timer() - start_g))
	print('# Clauses = %i' % cnf.getNumberClauses())
	print('# Variables = %i' % cnf.getNumberVariables())
'''输出
第一遍
SAT formula generation time = 0.000691
# Clauses = 99
# Variables = 32
第二遍
SAT formula generation time = 0.001249
# Clauses = 234
# Variables = 66
'''
	if timer() - time_start > time_limit - time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')
	print('Creating formula...')
	name_final = cnf.generateInputSat(name_formula_file)
	print('Done creating formula. Calling solver...')
'''输出
第一遍
Creating formula...
Done creating formula. Calling solver...
第二遍
Creating formula...
Done creating formula. Calling solver...
'''
	start_solv = timer()
	time_for_sat = int(time_limit - (timer() - time_start))
	if time_for_sat < time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')
	command = './minisat %s %s' % (name_formula_file, name_output_satsolver)
	# command = '/path/to/SATsolver/minisat -mem-lim=%i -cpu-lim=%i %s %s' % (mem_limit, time_for_sat, name_formula_file, name_output_satsolver)
	print('SAT solver called with %i MB and %i seconds' % (mem_limit, time_for_sat))
'''输出
第一遍
SAT solver called with 4096 MB and 1287 seconds
第二遍
SAT solver called with 4096 MB and 1286 seconds
'''
	os.system(command)
'''调用minisat求解得到输出：
第一遍
restarts              : 0
conflicts             : 0              (0 /sec)
decisions             : 0              (0 /sec)
propagations          : 19             (1216 /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0.015625 s

UNSATISFIABLE第一遍2 states没找到答案
第二遍找到答案
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |      52      240 |      17       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 0              (-nan /sec)
decisions             : 3              (inf /sec)
propagations          : 66             (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.79 MB
CPU time              : 0 s

SATISFIABLE第二遍3 states满足
'''
	end_solv = timer()
	solver_time.append(end_solv - start_solv)
	print('Done solver. Round time: %f' % (end_solv - start_solv))
	print('Cumulated solver time: %f' % sum(solver_time))
'''输出
第一遍
5120
Done solver. Round time: 0.164243
Cumulated solver time: 0.164243
第二遍

'''
	result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)
	if result is None:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME/MEM')#超出限定的内存和时间也找不到答案，不知道有没有解
	if result:
		break
	print('UNSATISFIABLE')#无解
'''输出
第一遍2 states没结果UNSATISFIABLE
第二遍
2560
Done solver. Round time: 0.208893
Cumulated solver time: 0.373136
和第一次不同的是这次有解，输出答案策略轨迹序列。
这部分是根据CNF.py中的def parseOutput(self, nameFile, controllerStates, parser, print_policy = False):的输出结果 
===================
===================
Controller -- CS = Controller State
===================
===================
Atom (CS)
___________________
----------
Atom person-at(l1) (n0)
----------
Atom person-at(l2) (n1)
----------
Atom person-at(l3) (ng)
===================
===================
(CS, Action with arguments)
___________________
(n0,move)
(n0,move(l1,l2))
(n1,move(l2,l3))
(n1,move)
===================
===================
(CS, Action name, CS)
___________________
(n0,move,n1)
(n1,move,ng)
===================
(CS, CS)
___________________
(n1,ng)
(n0,n1)
===================
Solved with 3 states
'''

```

核心循环到此结束

-------------------------------------------------------------------------------

main.py快结束了

```
print('Elapsed total time (s): %f' % (timer() - time_start))
print('Elapsed solver time (s): %f' % sum(solver_time))
print('Elapsed solver time (s): %s' % str(solver_time))
print('Looking for strong plans: %s' % str(strong))
print('Fair actions: %s' % str(fair))
clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, 'Done')#清理中间文件
```
















