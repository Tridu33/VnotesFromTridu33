[TOC]
# CNF_py



# L3

domain.pddl

```
(define (problem line-0)
(:domain line)
(:objects 
	L1 - location
	L2 - location
	L3 - location
)
(:init
	(person-at L1)

	(road L1 L2)
	(road L2 L1)
	(road L3 L2)
	(road L2 L3)
)
(:goal (person-at L3))
)
```

problem 3 grid move right

```
; Stupid Examples for me to understand this programe 

(define (domain line)
  (:requirements :typing)
  (:types location)
  (:predicates (person-at ?loc - location)
               (road ?from - location ?to - location)
  )            
  (:action move-right
    :parameters (?from - location ?to - location)
    :precondition (and (person-at ?from) (road ?from ?to))
    :effect (and (person-at ?to) (not (person-at ?from)))
  )
)
```

```
/src$ python  main.py ../mystupidroad/domain.pddl  ../mystupidroad/stupid.pddl -strong 1 -policy 1
```






观察传入my_task的数据结构都有什么输入：

```
p.generate_task(name_sas_file) #读取sas文件，保存数据
>>> my_task = p.translate_to_atomic() #存进my_task类的实例对象my_task中，自动输出界面的内容
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

查看my_task类中的局部变量

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


在Parser类的方法中翻译成，保存成mytask类的数据，可以根据myTask.py定义的方法

```
	def print_task(self):
		print('ATOMS ================================================')
		for a in self.atoms:
			print(a)
		print('INITIAL ==============================================')
		for a in self.initial:
			print(a)
		print('GOAL =================================================')
		for a in self.goal:
			print(a)
		print('ACTIONS ==============================================')
		for a in self.actions:
			print(a, self.get_other_actions(a))
			print(a, self.actions[a])
```

打印出来看

```
>>> my_task.print_task()
ATOMS ================================================
(var0=1)
(var0=2)
(var0=0)
INITIAL ==============================================
(var0=0)
GOAL =================================================
(var0=2)
ACTIONS ==============================================
('move-right(l2,l3)', [])
('move-right(l2,l3)', [['(var0=1)'], ['(var0=2)'], ['(var0=1)']])
('move-right(l2,l1)', [])
('move-right(l2,l1)', [['(var0=1)'], ['(var0=0)'], ['(var0=1)']])
('move-right(l1,l2)', [])
('move-right(l1,l2)', [['(var0=0)'], ['(var0=1)'], ['(var0=0)']])
('move-right(l3,l2)', [])
('move-right(l3,l2)', [['(var0=2)'], ['(var0=1)'], ['(var0=2)']])
```

```
>>> print(my_task.action_nondet)
{'move-right(l1,l2)': [], 'move-right(l3,l2)': [], 'move-right(l2,l3)': [], 'move-right(l2,l1)': []}
>>> print(my_task.action_cardinality)
{'move-right(l1,l2)': 1, 'move-right(l3,l2)': 1, 'move-right': 1, 'move-right(l2,l3)': 1, 'move-right(l2,l1)': 1}
>>> print(my_task.mutex_groups)
[['(var0=0)', '(var0=1)', '(var0=2)']]
>>> print(my_task.compatible_actions)
{'move-right(l1,l2)': set([]), 'move-right(l3,l2)': set([]), 'move-right(l2,l3)': set(['move-right(l2,l1)']), 'move-right(l2,l1)': set(['move-right(l2,l3)'])}
>>> print(my_task.mutex_groups_set)
[set(['(var0=1)', '(var0=2)', '(var0=0)'])]
>>> print(my_task.relevant_actions_atom)
{'(var0=1)': set(['move-right(l1,l2)', 'move-right(l3,l2)', 'move-right(l2,l3)', 'move-right(l2,l1)']), '(var0=2)': set(['move-right(l2,l3)', 'move-right(l3,l2)']), '(var0=0)': set(['move-right(l1,l2)', 'move-right(l2,l1)'])}
>>> print(my_task.relevant_actions_atom_aname)
{}
>>> print(my_task.action_names)
set(['move-right'])
>>> print(my_task.other_actions_name)
{'move-right': []}
>>> print(my_task.action_name_to_actions)
{'move-right': ['move-right(l2,l3)', 'move-right(l2,l1)', 'move-right(l1,l2)', 'move-right(l3,l2)']}
```
parser.py中p.translate_to_atomic函数就是生成上述my_task数据结构对象的元凶

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


然后就是main.py大循环就是高潮部分：留意重点：

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


# CNF


重要的是再来一遍，main.py大循环就是高潮部分：留意重点：

```
solver_time = []
for i in range(1000):
    cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)#文件formula-temp.txt这时候是空白的，formula-extra-temp此时空白，仅仅是传入地址方便最终结果存入数据
    ......
    cnf.reset()
    start_g = timer()
    #唯一重点，一行代码
    cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
    #生成子句Clauses和写入cnf文件合取范式的核心代码!!!
    ......
    command = './minisat %s %s' % (name_formula_file, name_output_satsolver)#调用minisat
    ......
    result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)#读取文件name_output_satsolver : outsat-temp.txt输出结果
    ......
```

运行结果是`>>> print(result)
True`

然后是cnf对象的数据结构和变量，函数，类和方法

```
class CNF:
	type1 = 'Atom-Controller'
	type2 = 'Action-Controller'
	type3 = 'Triplet'
	type4 = 'Reachable-I'
	type5 = 'Reachable-G'
	type6 = 'Replacement-Goal'
	type7 = 'Controller-Controller'
	type8 = 'Replacement-Equality'
	type9 = 'Inequality-CSCS'
	type10 = 'Replacement-Goal'
	num_types = 18#这些静态变量定义完了
	print_types = [1, 2, 3, 7]#？代表参数选项，想打印出来什么结果吗

	def __init__(self, n_file, n_file_extra, fair, strong):
		self.disjunctions = [] # list of disjunctions
		self.maxKey = 1
		self.mapVariableNumber = {}
		self.mapNumberVariable = {}
		self.mapVariableType = {}
		self.clauseSizeCounter = {}
		self.name_file_formula = n_file
		self.name_file_formula_extra = n_file_extra
		self.file_formula = open(n_file, 'w')
		self.file_formula_extra = open(n_file_extra, 'w')
		self.file_formula.close()
		self.file_formula_extra.close()
		self.number_clauses = 0
		self.fair   = fair
		self.strong = strong

	def reset(self):
		self.disjunctions = [] # list of disjunctions
		self.maxKey = 1
		self.mapVariableNumber = {}
		self.mapNumberVariable = {}
		self.mapVariableType = {}
		self.clauseSizeCounter = {}
		self.file_formula = open(self.name_file_formula, 'w')
		self.file_formula.write('p cnf 1 1\n')
		self.file_formula_extra = open(self.name_file_formula_extra, 'a')
		# File formula extra is not used, can be ignored
		self.number_clauses = 0
	......
```


然后看看运行完结果，其实加断点可以看第一次循环的结果，

结果就是第二遍循环之后的这些量是多少：

```
>>> print(cnf.disjunctions)
[]
>>> print(cnf.maxKey)
67
>>> print(cnf.mapVariableNumber)
{'reachableG(ng,0)': 49, '(var0=2)(ng)': 3, 'YR1-n1-ng-1': 66, '(n1,move-right(l1,l2))': 12, 'reachableG(ng,1)': 50, '(ng,move-right,n0)': 31, '(n1,move-right,ng)': 30, '(ng,move-right(l1,l2))': 19, 'YR1-n0-n0-0': 55, '(n1,move-right,n1)': 29, '(ng,ng)': 42, 'reachableG(n1,1)': 54, '(n0,move-right)': 22, '(n0,move-right(l2,l3))': 4, '(var0=1)(n1)': 10, '(ng,move-right(l2,l1))': 18, 'YR1-n0-n0-1': 61, '(ng,move-right(l2,l3))': 16, '(n1,move-right,n0)': 28, 'YR1-n1-n0-0': 58, '(n0,move-right,n1)': 26, '(n1,move-right(l3,l2))': 14, 'reachableI(ng)': 45, '(n1,n1)': 38, '(n1,ng)': 39, '(var0=0)(n1)': 13, '(ng,move-right(l3,l2))': 21, 'YR1-n1-n1-1': 65, 'reachableI(n0)': 43, '(var0=2)(n1)': 15, '(var0=0)(n0)': 7, '(ng,move-right)': 24, '(n0,n0)': 34, '(n0,move-right,ng)': 27, 'YR1-n1-n0-1': 64, 'YR1-n0-ng-0': 57, 'reachableG(n1,0)': 52, 'YR1-n1-n1-0': 59, '(n1,n0)': 37, '(var0=0)(ng)': 20, 'YR1-n0-ng-1': 63, '(ng,move-right,n1)': 32, 'reachableI(n1)': 44, '(ng,n1)': 41, 'reachableG(n1,2)': 47, 'YR1-n0-n1-1': 62, '(var0=1)(n0)': 1, '(n0,move-right(l2,l1))': 5, '(n1,move-right(l2,l1))': 11, '(n0,ng)': 36, '(n0,move-right,n0)': 25, '(ng,n0)': 40, 'YR1-n1-ng-0': 60, 'reachableG(n0,0)': 51, '(var0=1)(ng)': 17, '(n0,move-right(l1,l2))': 6, '(n1,move-right)': 23, 'reachableG(n0,2)': 46, '(n0,move-right(l3,l2))': 8, 'reachableG(n0,1)': 53, 'YR1-n0-n1-0': 56, '(n1,move-right(l2,l3))': 9, '(ng,move-right,ng)': 33, 'reachableG(ng,2)': 48, '(var0=2)(n0)': 2, '(n0,n1)': 35}
>>> print(cnf.mapNumberVariable)
{1: '(var0=1)(n0)', 2: '(var0=2)(n0)', 3: '(var0=2)(ng)', 4: '(n0,move-right(l2,l3))', 5: '(n0,move-right(l2,l1))', 6: '(n0,move-right(l1,l2))', 7: '(var0=0)(n0)', 8: '(n0,move-right(l3,l2))', 9: '(n1,move-right(l2,l3))', 10: '(var0=1)(n1)', 11: '(n1,move-right(l2,l1))', 12: '(n1,move-right(l1,l2))', 13: '(var0=0)(n1)', 14: '(n1,move-right(l3,l2))', 15: '(var0=2)(n1)', 16: '(ng,move-right(l2,l3))', 17: '(var0=1)(ng)', 18: '(ng,move-right(l2,l1))', 19: '(ng,move-right(l1,l2))', 20: '(var0=0)(ng)', 21: '(ng,move-right(l3,l2))', 22: '(n0,move-right)', 23: '(n1,move-right)', 24: '(ng,move-right)', 25: '(n0,move-right,n0)', 26: '(n0,move-right,n1)', 27: '(n0,move-right,ng)', 28: '(n1,move-right,n0)', 29: '(n1,move-right,n1)', 30: '(n1,move-right,ng)', 31: '(ng,move-right,n0)', 32: '(ng,move-right,n1)', 33: '(ng,move-right,ng)', 34: '(n0,n0)', 35: '(n0,n1)', 36: '(n0,ng)', 37: '(n1,n0)', 38: '(n1,n1)', 39: '(n1,ng)', 40: '(ng,n0)', 41: '(ng,n1)', 42: '(ng,ng)', 43: 'reachableI(n0)', 44: 'reachableI(n1)', 45: 'reachableI(ng)', 46: 'reachableG(n0,2)', 47: 'reachableG(n1,2)', 48: 'reachableG(ng,2)', 49: 'reachableG(ng,0)', 50: 'reachableG(ng,1)', 51: 'reachableG(n0,0)', 52: 'reachableG(n1,0)', 53: 'reachableG(n0,1)', 54: 'reachableG(n1,1)', 55: 'YR1-n0-n0-0', 56: 'YR1-n0-n1-0', 57: 'YR1-n0-ng-0', 58: 'YR1-n1-n0-0', 59: 'YR1-n1-n1-0', 60: 'YR1-n1-ng-0', 61: 'YR1-n0-n0-1', 62: 'YR1-n0-n1-1', 63: 'YR1-n0-ng-1', 64: 'YR1-n1-n0-1', 65: 'YR1-n1-n1-1', 66: 'YR1-n1-ng-1'}
>>> print(cnf.mapVariableType)
{'reachableG(ng,0)': 5, '(var0=2)(ng)': 1, 'YR1-n1-ng-1': 6, '(n1,move-right(l1,l2))': 2, 'reachableG(ng,1)': 5, '(ng,move-right,n0)': 3, '(n1,move-right,ng)': 3, '(ng,move-right(l1,l2))': 2, 'YR1-n0-n0-0': 6, '(n1,move-right,n1)': 3, '(ng,ng)': 7, 'reachableG(n1,1)': 5, '(n0,move-right)': 2, '(n0,move-right(l2,l3))': 2, '(var0=1)(n1)': 1, '(ng,move-right(l2,l1))': 2, 'YR1-n0-n0-1': 6, '(ng,move-right(l2,l3))': 2, '(n1,move-right,n0)': 3, 'YR1-n1-n0-0': 6, '(n0,move-right,n1)': 3, '(n1,move-right(l3,l2))': 2, 'reachableI(ng)': 4, '(n1,n1)': 7, '(n1,ng)': 7, '(var0=0)(n1)': 1, '(ng,move-right(l3,l2))': 2, 'YR1-n1-n1-1': 6, 'reachableI(n0)': 4, '(var0=2)(n1)': 1, '(var0=0)(n0)': 1, '(ng,move-right)': 2, '(n0,n0)': 7, '(n0,move-right,ng)': 3, 'YR1-n1-n0-1': 6, 'YR1-n0-ng-0': 6, 'reachableG(n1,0)': 5, 'YR1-n1-n1-0': 6, '(n1,n0)': 7, '(var0=0)(ng)': 1, 'YR1-n0-ng-1': 6, '(ng,move-right,n1)': 3, 'reachableI(n1)': 4, '(ng,n1)': 7, 'reachableG(n1,2)': 5, 'YR1-n0-n1-1': 6, '(var0=1)(n0)': 1, '(n0,move-right(l2,l1))': 2, '(n1,move-right(l2,l1))': 2, '(n0,ng)': 7, '(n0,move-right,n0)': 3, '(ng,n0)': 7, 'YR1-n1-ng-0': 6, 'reachableG(n0,0)': 5, '(var0=1)(ng)': 1, '(n0,move-right(l1,l2))': 2, '(n1,move-right)': 2, 'reachableG(n0,2)': 5, '(n0,move-right(l3,l2))': 2, 'reachableG(n0,1)': 5, 'YR1-n0-n1-0': 6, '(n1,move-right(l2,l3))': 2, '(ng,move-right,ng)': 3, 'reachableG(ng,2)': 5, '(var0=2)(n0)': 1, '(n0,n1)': 7}
>>> print(cnf.clauseSizeCounter)
{}
>>> print(cnf.name_file_formula)
formula-temp.txt
>>> print(cnf.name_file_formula_extra)
formula-extra-temp.txt
>>> print(cnf.number_clauses)
234
>>> print(cnf.fair)
True
>>> print(cnf.strong)
True
```

上面这个数据整理一下格式：

```
>>> print(cnf.mapVariableNumber)
{'reachableG(ng,0)': 49,
 '(var0=2)(ng)': 3,
 'YR1-n1-ng-1': 66,
 '(n1,move-right(l1,l2))': 12,
 'reachableG(ng,1)': 50,
 '(ng,move-right,n0)': 31,
 '(n1,move-right,ng)': 30,
 '(ng,move-right(l1,l2))': 19,
 'YR1-n0-n0-0': 55,
 '(n1,move-right,n1)': 29,
 '(ng,ng)': 42,
 'reachableG(n1,1)': 54,
 '(n0,move-right)': 22,
 '(n0,move-right(l2,l3))': 4,
 '(var0=1)(n1)': 10,
 '(ng,move-right(l2,l1))': 18,
 'YR1-n0-n0-1': 61,
 '(ng,move-right(l2,l3))': 16,
 '(n1,move-right,n0)': 28,
 'YR1-n1-n0-0': 58,
 '(n0,move-right,n1)': 26,
 '(n1,move-right(l3,l2))': 14,
 'reachableI(ng)': 45,
 '(n1,n1)': 38,
 '(n1,ng)': 39,
 '(var0=0)(n1)': 13,
 '(ng,move-right(l3,l2))': 21,
 'YR1-n1-n1-1': 65,
 'reachableI(n0)': 43,
 '(var0=2)(n1)': 15,
 '(var0=0)(n0)': 7,
 '(ng,move-right)': 24,
 '(n0,n0)': 34,
 '(n0,move-right,ng)': 27,
 'YR1-n1-n0-1': 64,
 'YR1-n0-ng-0': 57,
 'reachableG(n1,0)': 52,
 'YR1-n1-n1-0': 59,
 '(n1,n0)': 37,
 '(var0=0)(ng)': 20,
 'YR1-n0-ng-1': 63,
 '(ng,move-right,n1)': 32,
 'reachableI(n1)': 44,
 '(ng,n1)': 41,
 'reachableG(n1,2)': 47,
 'YR1-n0-n1-1': 62,
 '(var0=1)(n0)': 1,
 '(n0,move-right(l2,l1))': 5,
 '(n1,move-right(l2,l1))': 11,
 '(n0,ng)': 36,
 '(n0,move-right,n0)': 25,
 '(ng,n0)': 40,
 'YR1-n1-ng-0': 60,
 'reachableG(n0,0)': 51,
 '(var0=1)(ng)': 17,
 '(n0,move-right(l1,l2))': 6,
 '(n1,move-right)': 23,
 'reachableG(n0,2)': 46,
 '(n0,move-right(l3,l2))': 8,
 'reachableG(n0,1)': 53,
 'YR1-n0-n1-0': 56,
 '(n1,move-right(l2,l3))': 9,
 '(ng,move-right,ng)': 33,
 'reachableG(ng,2)': 48,
 '(var0=2)(n0)': 2,
 '(n0,n1)': 35}


>>> print(cnf.mapNumberVariable)
{
1: '(var0=1)(n0)', 
2: '(var0=2)(n0)', 
3: '(var0=2)(ng)', 
4: '(n0,move-right(l2,l3))', 
5: '(n0,move-right(l2,l1))', 
6: '(n0,move-right(l1,l2))', 
7: '(var0=0)(n0)', 
8: '(n0,move-right(l3,l2))', 
9: '(n1,move-right(l2,l3))', 
10: '(var0=1)(n1)', 
11: '(n1,move-right(l2,l1))', 
12: '(n1,move-right(l1,l2))', 
13: '(var0=0)(n1)', 
14: '(n1,move-right(l3,l2))', 
15: '(var0=2)(n1)', 
16: '(ng,move-right(l2,l3))', 
17: '(var0=1)(ng)', 
18: '(ng,move-right(l2,l1))', 
19: '(ng,move-right(l1,l2))', 
20: '(var0=0)(ng)', 
21: '(ng,move-right(l3,l2))', 
22: '(n0,move-right)', 
23: '(n1,move-right)', 
24: '(ng,move-right)', 
25: '(n0,move-right,n0)', 
26: '(n0,move-right,n1)', 
27: '(n0,move-right,ng)', 
28: '(n1,move-right,n0)', 
29: '(n1,move-right,n1)', 
30: '(n1,move-right,ng)', 
31: '(ng,move-right,n0)', 
32: '(ng,move-right,n1)', 
33: '(ng,move-right,ng)', 
34: '(n0,n0)', 
35: '(n0,n1)', 
36: '(n0,ng)', 
37: '(n1,n0)', 
38: '(n1,n1)', 
39: '(n1,ng)', 
40: '(ng,n0)', 
41: '(ng,n1)', 
42: '(ng,ng)', 
43: 'reachableI(n0)', 
44: 'reachableI(n1)', 
45: 'reachableI(ng)', 
46: 'reachableG(n0,2)', 
47: 'reachableG(n1,2)', 
48: 'reachableG(ng,2)', 
49: 'reachableG(ng,0)', 
50: 'reachableG(ng,1)', 
51: 'reachableG(n0,0)', 
52: 'reachableG(n1,0)', 
53: 'reachableG(n0,1)', 
54: 'reachableG(n1,1)', 
55: 'YR1-n0-n0-0', 
56: 'YR1-n0-n1-0', 
57: 'YR1-n0-ng-0', 
58: 'YR1-n1-n0-0', 
59: 'YR1-n1-n1-0', 
60: 'YR1-n1-ng-0', 
61: 'YR1-n0-n0-1', 
62: 'YR1-n0-n1-1', 
63: 'YR1-n0-ng-1', 
64: 'YR1-n1-n0-1', 
65: 'YR1-n1-n1-1', 
66: 'YR1-n1-ng-1'}


>>> print(cnf.mapVariableType)
{'reachableG(ng,0)': 5,
 '(var0=2)(ng)': 1,
 'YR1-n1-ng-1': 6,
 '(n1,move-right(l1,l2))': 2,
 'reachableG(ng,1)': 5,
 '(ng,move-right,n0)': 3,
 '(n1,move-right,ng)': 3,
 '(ng,move-right(l1,l2))': 2,
 'YR1-n0-n0-0': 6,
 '(n1,move-right,n1)': 3,
 '(ng,ng)': 7,
 'reachableG(n1,1)': 5,
 '(n0,move-right)': 2,
 '(n0,move-right(l2,l3))': 2,
 '(var0=1)(n1)': 1,
 '(ng,move-right(l2,l1))': 2,
 'YR1-n0-n0-1': 6,
 '(ng,move-right(l2,l3))': 2,
 '(n1,move-right,n0)': 3,
 'YR1-n1-n0-0': 6,
 '(n0,move-right,n1)': 3,
 '(n1,move-right(l3,l2))': 2,
 'reachableI(ng)': 4,
 '(n1,n1)': 7,
 '(n1,ng)': 7,
 '(var0=0)(n1)': 1,
 '(ng,move-right(l3,l2))': 2,
 'YR1-n1-n1-1': 6,
 'reachableI(n0)': 4,
 '(var0=2)(n1)': 1,
 '(var0=0)(n0)': 1,
 '(ng,move-right)': 2,
 '(n0,n0)': 7,
 '(n0,move-right,ng)': 3,
 'YR1-n1-n0-1': 6,
 'YR1-n0-ng-0': 6,
 'reachableG(n1,0)': 5,
 'YR1-n1-n1-0': 6,
 '(n1,n0)': 7,
 '(var0=0)(ng)': 1,
 'YR1-n0-ng-1': 6,
 '(ng,move-right,n1)': 3,
 'reachableI(n1)': 4,
 '(ng,n1)': 7,
 'reachableG(n1,2)': 5,
 'YR1-n0-n1-1': 6,
 '(var0=1)(n0)': 1,
 '(n0,move-right(l2,l1))': 2,
 '(n1,move-right(l2,l1))': 2,
 '(n0,ng)': 7,
 '(n0,move-right,n0)': 3,
 '(ng,n0)': 7,
 'YR1-n1-ng-0': 6,
 'reachableG(n0,0)': 5,
 '(var0=1)(ng)': 1,
 '(n0,move-right(l1,l2))': 2,
 '(n1,move-right)': 2,
 'reachableG(n0,2)': 5,
 '(n0,move-right(l3,l2))': 2,
 'reachableG(n0,1)': 5,
 'YR1-n0-n1-0': 6,
 '(n1,move-right(l2,l3))': 2,
 '(ng,move-right,ng)': 3,
 'reachableG(ng,2)': 5,
 '(var0=2)(n0)': 1,
 '(n0,n1)': 7}
```


最终找到的SAT解答

```
SAT
SAT
-1 -2 3 4 5 -6 -7 -8 -9 -10 -11 12 13 -14 -15 -16 -17 -18 -19 -20 -21 22 23 -24 -25 26 -27 -28 -29 30 -31 -32 -33 -34 35 -36 -37 -38 39 -40 -41 -42 43 44 45 46 47 48 49 50 -51 -52 -53 54 55 -56 57 58 59 60 61 62 63 64 65 66 0
```

对应的命题：

```

>>> print(cnf.mapNumberVariable)
{
3: '(var0=2)(ng)', 
4: '(n0,move-right(l2,l3))', 
5: '(n0,move-right(l2,l1))', 
12: '(n1,move-right(l1,l2))', 
13: '(var0=0)(n1)', 
22: '(n0,move-right)', 
23: '(n1,move-right)', 
26: '(n0,move-right,n1)', 
30: '(n1,move-right,ng)', 
35: '(n0,n1)', 
39: '(n1,ng)', 
43: 'reachableI(n0)', 
44: 'reachableI(n1)', 
45: 'reachableI(ng)', 
46: 'reachableG(n0,2)', 
47: 'reachableG(n1,2)', 
48: 'reachableG(ng,2)', 
49: 'reachableG(ng,0)', 
50: 'reachableG(ng,1)', 
54: 'reachableG(n1,1)', 
55: 'YR1-n0-n0-0', 
57: 'YR1-n0-ng-0', 
58: 'YR1-n1-n0-0', 
59: 'YR1-n1-n1-0', 
60: 'YR1-n1-ng-0', 
61: 'YR1-n0-n0-1', 
62: 'YR1-n0-n1-1', 
63: 'YR1-n0-ng-1', 
64: 'YR1-n1-n0-1', 
65: 'YR1-n1-n1-1', 
66: 'YR1-n1-ng-1'}

```



# cnf.py

<table width="100%" border="0" cellspacing="0" cellpadding="2" summary="section"><tbody><tr><td width="100%"><p><table width="100%" border="0" cellspacing="0" cellpadding="2" summary="section"><tbody><tr bgcolor="#ffc8d8"><td valign="bottom" colspan="3"><font color="#000000" face="helvetica, arial"><a name="CNF">class <strong>CNF</strong></a>(<a href="http://localhost:8080/builtins.html#object">builtins.object</a>)</font></td></tr><tr bgcolor="#ffc8d8"><td rowspan="2"><tt>&nbsp;&nbsp;&nbsp;</tt></td><td colspan="2"><tt><a href="http://localhost:8080/CNF.html#CNF">CNF</a>(n_file,&nbsp;n_file_extra,&nbsp;fair,&nbsp;strong)<br>&nbsp;<br><br>&nbsp;</tt></td></tr><tr><td>&nbsp;</td><td width="100%">Methods defined here:<br><dl><dt><a name="CNF-__init__"><strong>__init__</strong></a>(self, n_file, n_file_extra, fair, strong)</dt><dd><tt>Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</tt></dd></dl><dl><dt><a name="CNF-addClause"><strong>addClause</strong></a>(self, clause)</dt></dl><dl><dt><a name="CNF-addClauseExtra"><strong>addClauseExtra</strong></a>(self, clause)</dt></dl><dl><dt><a name="CNF-alreadyUsed"><strong>alreadyUsed</strong></a>(self, var)</dt></dl><dl><dt><a name="CNF-assignKey"><strong>assignKey</strong></a>(self, var, typeVar=-1)</dt></dl><dl><dt><a name="CNF-generateAfterG"><strong>generateAfterG</strong></a>(self, n)</dt></dl><dl><dt><a name="CNF-generateAtLeastOneAction"><strong>generateAtLeastOneAction</strong></a>(self, task, controllerStates, debug)</dt></dl><dl><dt><a name="CNF-generateAtomControllerState"><strong>generateAtomControllerState</strong></a>(self, atom, controllerState)</dt></dl><dl><dt><a name="CNF-generateCompletionReachabilityG"><strong>generateCompletionReachabilityG</strong></a>(self, task, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generateConn"><strong>generateConn</strong></a>(self, CStates)</dt></dl><dl><dt><a name="CNF-generateFirstG"><strong>generateFirstG</strong></a>(self, n)</dt></dl><dl><dt><a name="CNF-generateGeneralizeConnection"><strong>generateGeneralizeConnection</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generateGoal"><strong>generateGoal</strong></a>(self, task, goalCState, debug=False)</dt></dl><dl><dt><a name="CNF-generateInequalityN"><strong>generateInequalityN</strong></a>(self, n1, n2)</dt></dl><dl><dt><a name="CNF-generateInitial"><strong>generateInitial</strong></a>(self, task, initialCState, debug=False)</dt></dl><dl><dt><a name="CNF-generateInputSat"><strong>generateInputSat</strong></a>(self, nameFile)</dt></dl><dl><dt><a name="CNF-generateLowerPredecessor"><strong>generateLowerPredecessor</strong></a>(self, n1, n2)</dt></dl><dl><dt><a name="CNF-generateMutexGroupsClauses"><strong>generateMutexGroupsClauses</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generateNegativeForwardPropagation"><strong>generateNegativeForwardPropagation</strong></a>(self, task, controllerStates, debug)</dt></dl><dl><dt><a name="CNF-generateOneSuccessor"><strong>generateOneSuccessor</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generatePairActionControllerState"><strong>generatePairActionControllerState</strong></a>(self, action, controllerState)</dt></dl><dl><dt><a name="CNF-generatePairCSCS"><strong>generatePairCSCS</strong></a>(self, n1, n2)</dt></dl><dl><dt><a name="CNF-generatePairFairCS"><strong>generatePairFairCS</strong></a>(self, n)</dt></dl><dl><dt><a name="CNF-generatePairUnfairCS"><strong>generatePairUnfairCS</strong></a>(self, n)</dt></dl><dl><dt><a name="CNF-generatePossibleNonDet"><strong>generatePossibleNonDet</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generatePreconditions"><strong>generatePreconditions</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generatePropagationIG"><strong>generatePropagationIG</strong></a>(self, task, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generatePropagationReachableGCyclic"><strong>generatePropagationReachableGCyclic</strong></a>(self, task, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generatePropagationReachableGStrong"><strong>generatePropagationReachableGStrong</strong></a>(self, task, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generatePropagationReachableGUnfair"><strong>generatePropagationReachableGUnfair</strong></a>(self, task, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generatePropagationReachableI"><strong>generatePropagationReachableI</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generateReachableG"><strong>generateReachableG</strong></a>(self, controllerState, j)</dt></dl><dl><dt><a name="CNF-generateReachableGClauses"><strong>generateReachableGClauses</strong></a>(self, task, controllerStates, goalCState, k, debug=False)</dt></dl><dl><dt><a name="CNF-generateReachableGInitial"><strong>generateReachableGInitial</strong></a>(self, task, goalCState, controllerStates, numberControllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generateReachableI"><strong>generateReachableI</strong></a>(self, controllerState)</dt></dl><dl><dt><a name="CNF-generateReachableI2"><strong>generateReachableI2</strong></a>(self, controllerState, j)</dt></dl><dl><dt><a name="CNF-generateReachableIClauses"><strong>generateReachableIClauses</strong></a>(self, task, initialCState, controllerStates, k, debug=False)</dt></dl><dl><dt><a name="CNF-generateReachableIinitial"><strong>generateReachableIinitial</strong></a>(self, initialCState, debug=False)</dt></dl><dl><dt><a name="CNF-generateReplacementEquality"><strong>generateReplacementEquality</strong></a>(self, n1, n2, atom)</dt></dl><dl><dt><a name="CNF-generateReplacementGoalPropagation"><strong>generateReplacementGoalPropagation</strong></a>(self, controllerState1, controllerState2, i)</dt></dl><dl><dt><a name="CNF-generateReplacementGoalPropagation3"><strong>generateReplacementGoalPropagation3</strong></a>(self, controllerState1, controllerState2, i)</dt></dl><dl><dt><a name="CNF-generateReplacementIPropagation"><strong>generateReplacementIPropagation</strong></a>(self, controllerState1, controllerState2, i)</dt></dl><dl><dt><a name="CNF-generateSymmetryBreaking"><strong>generateSymmetryBreaking</strong></a>(self, task, controllerStates, initialCState, goalCState, debug=False)</dt></dl><dl><dt><a name="CNF-generateTripletCSACS"><strong>generateTripletCSACS</strong></a>(self, initialState, action, finalState)</dt></dl><dl><dt><a name="CNF-generateTripletForcesBin"><strong>generateTripletForcesBin</strong></a>(self, task, controllerStates, debug=False)</dt></dl><dl><dt><a name="CNF-generate_clauses"><strong>generate_clauses</strong></a>(self, task, initialCState, goalCState, controllerStates, k, parser=None, debug=False)</dt></dl><dl><dt><a name="CNF-getNumberClauses"><strong>getNumberClauses</strong></a>(self)</dt></dl><dl><dt><a name="CNF-getNumberVariables"><strong>getNumberVariables</strong></a>(self)</dt></dl><dl><dt><a name="CNF-get_num_cl_vars"><strong>get_num_cl_vars</strong></a>(self)</dt></dl><dl><dt><a name="CNF-parseOutput"><strong>parseOutput</strong></a>(self, nameFile, controllerStates, parser, print_policy=False)</dt></dl><dl><dt><a name="CNF-printClausesSizes"><strong>printClausesSizes</strong></a>(self, n)</dt></dl><dl><dt><a name="CNF-printMapVarNumber"><strong>printMapVarNumber</strong></a>(self)</dt></dl><dl><dt><a name="CNF-printVariables"><strong>printVariables</strong></a>(self)</dt></dl><dl><dt><a name="CNF-reset"><strong>reset</strong></a>(self)</dt></dl><dl><dt><a name="CNF-setFairUnfairActions"><strong>setFairUnfairActions</strong></a>(self, task, controllerStates)</dt></dl><dl><dt><a name="CNF-writeDisjunctions"><strong>writeDisjunctions</strong></a>(self, file)</dt></dl><hr>Data descriptors defined here:<br><dl><dt><strong>__dict__</strong></dt><dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd></dl><dl><dt><strong>__weakref__</strong></dt><dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd></dl><hr>Data and other attributes defined here:<br><dl><dt><strong>num_types</strong> = 18</dt></dl><dl><dt><strong>print_types</strong> = [1, 2, 3, 7]</dt></dl><dl><dt><strong>type1</strong> = 'Atom-Controller'</dt></dl><dl><dt><strong>type10</strong> = 'Replacement-Goal'</dt></dl><dl><dt><strong>type2</strong> = 'Action-Controller'</dt></dl><dl><dt><strong>type3</strong> = 'Triplet'</dt></dl><dl><dt><strong>type4</strong> = 'Reachable-I'</dt></dl><dl><dt><strong>type5</strong> = 'Reachable-G'</dt></dl><dl><dt><strong>type6</strong> = 'Replacement-Goal'</dt></dl><dl><dt><strong>type7</strong> = 'Controller-Controller'</dt></dl><dl><dt><strong>type8</strong> = 'Replacement-Equality'</dt></dl><dl><dt><strong>type9</strong> = 'Inequality-CSCS'</dt></dl></td></tr></tbody></table></p></td></tr></tbody></table>

入口函数

```
    #唯一重点，一行代码
    cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
    #生成子句Clauses和写入cnf文件合取范式的核心代码!!!
```

查看定义：

```
	def generate_clauses(self, task, initialCState, goalCState, controllerStates, k, parser = None, debug = False):
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




## cnf源码加解析各自的类



```
import sys
from myTask import MyTask
from timeit import default_timer as timer
import os

class MyCNFError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class CNF:
	type1 = 'Atom-Controller'
	type2 = 'Action-Controller'
	type3 = 'Triplet'
	type4 = 'Reachable-I'
	type5 = 'Reachable-G'
	type6 = 'Replacement-Goal'
	type7 = 'Controller-Controller'
	type8 = 'Replacement-Equality'
	type9 = 'Inequality-CSCS'
	type10 = 'Replacement-Goal'
	num_types = 18
	print_types = [1, 2, 3, 7]

	def __init__(self, n_file, n_file_extra, fair, strong):
		self.disjunctions = [] # list of disjunctions
		self.maxKey = 1
		self.mapVariableNumber = {}
		self.mapNumberVariable = {}
		self.mapVariableType = {}
		self.clauseSizeCounter = {}
		self.name_file_formula = n_file
		self.name_file_formula_extra = n_file_extra
		self.file_formula = open(n_file, 'w')
		self.file_formula_extra = open(n_file_extra, 'w')
		self.file_formula.close()
		self.file_formula_extra.close()
		self.number_clauses = 0
		self.fair   = fair
		self.strong = strong

	def reset(self):
		self.disjunctions = [] # list of disjunctions
		self.maxKey = 1
		self.mapVariableNumber = {}
		self.mapNumberVariable = {}
		self.mapVariableType = {}
		self.clauseSizeCounter = {}
		self.file_formula = open(self.name_file_formula, 'w')
		self.file_formula.write('p cnf 1 1\n')
		self.file_formula_extra = open(self.name_file_formula_extra, 'a')
		# File formula extra is not used, can be ignored
		self.number_clauses = 0

```

代码接上，标记方便跳转查看

## GENERAl通用功能性函数

```
	###########################################
	################# GENERAL #################
	###########################################

	def generateAtomControllerState(self, atom, controllerState):
		var = atom + '(' + controllerState + ')'
		self.assignKey(var, 1)
		return var

	def generatePairActionControllerState(self, action, controllerState):
		var = '(' + controllerState + ',' + action + ')'
		self.assignKey(var, 2)
		return var

	def generateTripletCSACS(self, initialState, action, finalState):
		var = '(' + initialState + ',' + action + ',' + finalState + ')'
		self.assignKey(var, 3)
		return var

	def generateReachableI(self, controllerState):
		var = 'reachableI(' + controllerState + ')'
		self.assignKey(var, 4)
		return var

	def generateReachableI2(self, controllerState, j):
		var = 'reachableI(' + controllerState + ',' + str(j) + ')'
		self.assignKey(var, 4)
		return var

	def generateReachableG(self, controllerState, j):
		var = 'reachableG(' + controllerState + ',' + str(j) + ')'
		self.assignKey(var, 5)
		return var

	def generateReplacementGoalPropagation(self, controllerState1, controllerState2, i):
		var = 'YR1-' + controllerState1 + '-' + controllerState2 + '-' + str(i)
		self.assignKey(var, 6)
		return var

	def generateReplacementGoalPropagation3(self, controllerState1, controllerState2, i):
		var = 'YR1-FAIR-' + controllerState1 + '-' + controllerState2 + '-' + str(i)
		self.assignKey(var, 6)
		return var

	def generatePairCSCS(self, n1, n2):
		var = '(' + n1 + ',' + n2 + ')'
		self.assignKey(var, 7)
		return var

	def generateReplacementEquality(self, n1, n2, atom):
		var = 'YR2-' + n1 + '-' + n2 + '-' + atom
		self.assignKey(var, 8)
		return var

	def generateInequalityN(self, n1, n2): # n1 < n2
		var = n1 + '<' + n2
		self.assignKey(var, 9)
		return var	

	def generateReplacementIPropagation(self, controllerState1, controllerState2, i):
		var = 'YR3-' + controllerState1 + '-' + controllerState2 + '-' + str(i)
		self.assignKey(var, 10)
		return var

	def generateFirstG(self, n):
		var = 'FirstG(' + str(n) + ')'
		self.assignKey(var, 13)
		return var

	def generateAfterG(self, n):
		var = 'AfterG(' + str(n) + ')'
		self.assignKey(var, 14)
		return var

	def generateConn(self, CStates):
		var = 'conn('
		for n in CStates:
			var += str(n) + ','
		var += ')'
		self.assignKey(var, 15)
		return var

	def generatePairFairCS(self, n):
		var = 'F(' + n + ',fair)'
		self.assignKey(var, 16)
		return var

	def generatePairUnfairCS(self, n):
		var = 'U(' + n + ',unfair)'
		self.assignKey(var, 17)
		return var

	def generateLowerPredecessor(self, n1, n2):
		var = 'Lower(' + n1 + ', ' + n2 + ')'
		self.assignKey(var, 18)
		return var

	def generateInputSat(self, nameFile):
		self.file_formula.close()
		with open(nameFile, 'r') as formula:
			name_final = nameFile + 'header'
			with open(name_final, 'w') as final_formula:
				final_formula.write('p cnf %i %i\n' % (len(self.mapNumberVariable), self.number_clauses))
				first_line = True
				for line in formula:
					if first_line:
						first_line = False
						continue
					final_formula.write(line)
		# name_final is the name of the file that contains the formula with header and everything
		return name_final

	def writeDisjunctions(self, file):
		for i in self.disjunctions:
			for j in i:
				if j[0] == '-':
					file.write('-' + str(self.mapVariableNumber[j[1:]]) + '\t')
				else:
					file.write(str(self.mapVariableNumber[j]) + '\t')
			file.write('0\n')

	# def printDisjunctions(self):
	# 	for i in self.disjunctions:
	# 		for j in i:
	# 			print j + ' ',
	# 		print '\n',

	# def printDisjunctionsNumbers(self, printExpanded):
	# 	for i in self.disjunctions:
	# 		if printExpanded:
	# 			for j in i:
	# 				print j + '\t',
	# 			print ''
	# 		for j in i:
	# 			if j[0] == '-':
	# 				print '-' + str(self.mapVariableNumber[j[1:]]), '\t',
	# 			else:
	# 				print self.mapVariableNumber[j], '\t',
	# 		print ' 0'

	def printVariables(self):
		for i in self.mapVariableNumber:
			print(i)
```

## parseOutput输出解决policy

```
	def parseOutput(self, nameFile, controllerStates, parser, print_policy = False):
		sets = [set([]) for i in range(self.num_types)]
		fres = open(nameFile, 'r')
		res = fres.readlines()
		if 'UNSAT' in res[0]:
			return False
		if 'INDET' in res[0]:
			return None
		if not print_policy:
			return True
		res = res[1]
		res = res.split(' ')
		for r in res:
			if '\n' in res:
				continue
			var = int(r)
			if var > 0:
				varName = self.mapNumberVariable[var]
				t = self.mapVariableType[varName]
				sets[t - 1].add(varName)
		print('===================\n===================')
		print('Controller -- CS = Controller State')
		for i in range(len(sets)):
			if i + 1 in self.print_types:
				s = sets[i]
				if i == 0:
					# pair atom controller
					print('===================\n===================')
					print('Atom (CS)')
					print('___________________')
					for n in controllerStates:
						print('----------')
						for j in s:
							ind = '(' + n + ')'
							if ind in j:
								print('%s %s' % (str(parser.get_var_string(j.split(ind)[0])), str(ind)))
				elif i == 1:
					# pair cs action
					print('===================\n===================')
					print('(CS, Action with arguments)')
					print('___________________')
					for n in controllerStates:
						for j in s:
							if '(' + n + ',' in j:
								print(j)
				elif i == 2:
					# Triplet
					print('===================\n===================')
					print('(CS, Action name, CS)')
					print('___________________')
					for n in controllerStates:
						for j in s:
							if '(' + n + ',' in j:
								print(j)
				else:
					print('===================')
					print('(CS, CS)')
					print('___________________')
					for j in s:
						print(j)
		print('===================')
		print('Solved with %i states' % len(controllerStates))
		return True

	def getNumberVariables(self):
		return len(self.mapVariableNumber)

	def getNumberClauses(self):
		return self.number_clauses

	def printMapVarNumber(self):
		for i in self.mapVariableNumber:
			print(i, '-->', self.mapVariableNumber[i])

	def alreadyUsed(self, var):
		if var in self.mapVariableNumber:
			return True
		return False

	def assignKey(self, var, typeVar = -1):
		if not self.alreadyUsed(var):
			self.mapVariableNumber[var] = self.maxKey
			self.mapNumberVariable[self.maxKey] = var
			self.mapVariableType[var] = typeVar
			self.maxKey += 1

	def get_num_cl_vars(self):
		return self.getNumberClauses(), self.getNumberVariables()

	def addClause(self, clause):
		self.number_clauses += 1
		for j in clause:
			negated = (j[0] == '-')
			if negated:
				var = j[1:]
			else:
				var = j
			if negated:
				self.file_formula.write('-' + str(self.mapVariableNumber[var]) + '\t')
			else:
				self.file_formula.write(str(self.mapVariableNumber[var]) + '\t')
		self.file_formula.write('0\n')

	def addClauseExtra(self, clause):
		for j in clause:
			self.file_formula_extra.write(j + '|')
		self.file_formula_extra.write('\n')
		# j1|j2|...|jn|\n

	def printClausesSizes(self, n):
		print(self.clauseSizeCounter)
		sum_all = 0
		sum_greater = 0
		for i in self.clauseSizeCounter:
			sum_all += self.clauseSizeCounter[i]
			if i >= n:
				sum_greater += self.clauseSizeCounter[i]
			else:
				print(i, ':', self.clauseSizeCounter[i])
		print('>=', i, ':', sum_greater)
```

代码接上，标记方便跳转查看



## generate_clauses核心入口类


main.py
高潮部分：注意留意重点：

```
solver_time = []
for i in range(1000):
    cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)#文件formula-temp.txt这时候是空白的，formula-extra-temp此时空白，仅仅是传入地址方便最终结果存入数据
    ......
    cnf.reset()
	  start_g = timer()
    cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)#生成子句Clauses和写入cnf文件合取范式的核心代码!!!
    ......
    command = './minisat %s %s' % (name_formula_file, name_output_satsolver)#调用minisat
    ......
    result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)#读取文件name_output_satsolver : outsat-temp.txt输出结果
    ......
```



cnf.py

```
	###########################################
	############## GENERATION #################
	###########################################

	def generate_clauses(self, task, initialCState, goalCState, controllerStates, k, parser = None, debug = False):
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


代码接上，标记方便跳转查看

##  generate_clauses调用的生成子句的类

```
	###########################################
	################ INITIAL ##################
	###########################################

	def generateInitial(self, task, initialCState, debug = False):
		# -p(n0) for all p not in initial state
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		initial = task.get_initial()
		atoms = task.get_atoms()
		for a in atoms:
			if a not in initial:
				variable = self.generateAtomControllerState(a, initialCState)
				self.addClause(['-' + variable])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Initial\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## GOAL #######################
	###########################################

	def generateGoal(self, task, goalCState, debug = False):
		# p(ng) for all p in goal state
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		goal = task.get_goal()
		atoms = task.get_atoms()
		for a in atoms:
			if a in goal:
				variable = self.generateAtomControllerState(a, goalCState)
				self.addClause([variable])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Goal\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## PRECONDITIONS ##############
	###########################################

	def generatePreconditions(self, task, controllerStates, debug = False):
		# (n, b) --> p(n) // if p \in prec(b)
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		atoms = task.get_atoms()
		actions = task.get_actions()
		
		for n in controllerStates:
			for a in actions:
				pre = task.get_preconditions(a)
				var = self.generatePairActionControllerState(a, n)
				for p in pre:
					varPre = self.generateAtomControllerState(p, n)
					self.addClause(['-' + var, varPre])
		 			# print clause + [varPre] # DEBUG

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Precs\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))


	###########################################
	############## NON-DET ####################
	###########################################

	def generatePossibleNonDet(self, task, controllerStates, debug = False):
		# 1. (n, act) --> (n, act') // act, act' are non det act of equal det action (action names)
		# 2. (n, act) --> -(n, act'') //
		# 3. (n, b) --> (n, b') // b, b' are siblings
		# 4. (n, b) --> -(n, b'') // b, b'' belong to same act
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		acts = task.get_action_names()
		for n in controllerStates:
			for act in acts:
				var_pair = self.generatePairActionControllerState(act, n)
				other_acts = task.get_other_actions_name(act)
				for act2 in acts:
					if act2 == act:
						continue
					var_pair2 = self.generatePairActionControllerState(act2, n)
					if act2 in other_acts:
						self.addClause(['-' + var_pair, var_pair2]) # 1
					else:
						self.addClause(['-' + var_pair, '-' + var_pair2]) # 2

				for a1 in task.get_actions_with_name(act):
					var1 = self.generatePairActionControllerState(a1, n)
					for a2 in task.get_actions_with_name(act):
						if a2 == a1:
							continue
						if task.actions_are_compatible(a1, a2): # IMPORTANT!! ie. prec not mutex
							var2 = self.generatePairActionControllerState(a2, n)
							self.addClause(['-' + var1, '-' + var2]) # 4

			for a in task.get_actions():
				var1 = self.generatePairActionControllerState(a, n)
				other_actions = task.get_other_actions(a)
				for other in other_actions:
					if other == a:
						continue
					var2 = self.generatePairActionControllerState(other, n)
					self.addClause(['-' + var1, var2]) # 3

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Non Det\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## ONE SUCC ###################
	###########################################

	def generateOneSuccessor(self, task, controllerStates, debug = False):
		# 1. (n, act) --> \OR_{b} (n, b) // for b with name act
		# 2. (n, act) --> \OR_{n'} (n, act, n')
		# 3. -(n, act, n') \lor -(n, act, n'')
		# 4. (n, b) --> (n, act)
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		acts = task.get_action_names()

		for n1 in controllerStates:
			for a_name in acts:
				for n2 in controllerStates:
					for n3 in controllerStates:
						if n3 == n2:
							continue
						var1 = self.generateTripletCSACS(n1, a_name, n2)
						var2 = self.generateTripletCSACS(n1, a_name, n3)
						self.addClause(['-' + var1, '-' + var2]) # 3

				for a in task.get_actions_with_name(a_name):
					pair1 = self.generatePairActionControllerState(a, n1)
					pair2 = self.generatePairActionControllerState(a_name, n1)
					self.addClause(['-' + pair1, pair2]) # 4

				var1 = self.generatePairActionControllerState(a_name, n1)
				var_triplets = []
				for n2 in controllerStates:
					var_triplets.append(self.generateTripletCSACS(n1, a_name, n2))
				self.addClause(['-' + var1] + var_triplets) # 2

				var1 = self.generatePairActionControllerState(a_name, n1)
				var_bin = []
				for a in task.get_actions_with_name(a_name):
					var_bin.append(self.generatePairActionControllerState(a, n1))
				self.addClause(['-' + var1] + var_bin) # 1

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: One succ\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## TRIPLET-BIN ################
	###########################################

	def generateTripletForcesBin(self, task, controllerStates, debug = False):
		# (n, act, n') --> (n, act)
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		actions = task.get_action_names()
		for n1 in controllerStates:
			for a in actions:
				for n2 in controllerStates:
					var1 = self.generateTripletCSACS(n1, a, n2)
					var2 = self.generatePairActionControllerState(a, n1)
					# print ['-' + var1, var2] # DEBUG
					self.addClause(['-' + var1, var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Trip bin\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## ONE ACTION #################
	###########################################

	def generateAtLeastOneAction(self, task, controllerStates, debug):
		# \OR_{act_name} (n, act) for all n except goal, ng
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		actions = task.get_action_names()
		for n in controllerStates:
			if n == 'ng':
				continue
			disj = []
			for a in actions:
				pair = self.generatePairActionControllerState(a, n)
				disj.append(pair)
			self.addClause(disj)

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: One act\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## NEG-FORWARD PROP ###########
	###########################################

	def __sibling_action_adds_atom(self, task, action, atom):
		siblings = task.get_other_actions(action)
		for a in siblings:
			add_list = task.get_add_list(a)
			if atom in add_list:
				return True
		return False

	def generateNegativeForwardPropagation(self, task, controllerStates, debug):
		# 1. (n, act, n') \land (n, b) --> -p(n') // if p in delete list
		# 2. (n, n') \land -p(n) --> -p(n') \lor \OR_{b: p \in add(b)} (n, b)
		# 3. (n, act, n') \land (n, b) \land -p(n) --> -p(n') // if p \not \in add(b) 
		# and some sibling of b adds p
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		atoms = task.get_atoms()
		actions = task.get_actions()

		#for a in actions:
		#	print(a, task.get_del_list(a))
		#	print(a, task.get_add_list(a))

		for n1 in controllerStates:
			for n2 in controllerStates:
				for p in atoms:
					var_atom_n1 = self.generateAtomControllerState(p, n1)
					var_pair_n1n2 = self.generatePairCSCS(n1, n2)
					var_atom_n2 = self.generateAtomControllerState(p, n2)
					disj_add_clause = ['-' + var_pair_n1n2, var_atom_n1, '-' + var_atom_n2]
					for a in task.get_relevant_actions(p):
						a_name = task.get_action_name(a)
						del_list = task.get_del_list(a)
						add_list = task.get_add_list(a)
						var_triplet = self.generateTripletCSACS(n1, a_name, n2)
						var_bin = self.generatePairActionControllerState(a, n1)
						if p in del_list:
							self.addClause(['-' + var_triplet, '-' + var_bin,'-' + var_atom_n2]) # 1
						if p in add_list:
							disj_add_clause.append(var_bin)
						if p not in add_list and self.__sibling_action_adds_atom(task, a, p):
							self.addClause(['-' + var_triplet, '-' + var_bin, var_atom_n1, '-' + var_atom_n2]) # 3
					self.addClause(disj_add_clause) # 2

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Neg Prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## GEN-CONNS ##################
	###########################################

	def generateGeneralizeConnection(self, task, controllerStates, debug = False):
		# (n, n') <--> \OR_{act} (n, act, n')
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		actions = task.get_action_names()
		for n1 in controllerStates:
			for n2 in controllerStates:
				varBin = self.generatePairCSCS(n1, n2)
				triplets = ['-' + varBin]
				for a in actions:
					triplet = self.generateTripletCSACS(n1, a, n2)
					self.addClause(['-' + triplet, varBin])
					# print ['-' + triplet, varBin] # DEBUG
					triplets.append(triplet)
				# print triplets # DEBUG
				self.addClause(triplets)

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Gen conn\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## REACH-I ####################
	###########################################

	def generateReachableIClauses(self, task, initialCState, controllerStates, k, debug = False):
		self.generateReachableIinitial(initialCState, debug)
		self.generatePropagationReachableI(task, controllerStates, debug)
		self.generatePropagationIG(task, controllerStates, k - 1, debug)

	def generateReachableIinitial(self, initialCState, debug = False):
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		self.addClause([self.generateReachableI(initialCState)])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RI init\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def generatePropagationReachableI(self, task, controllerStates, debug = False):
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		for n1 in controllerStates:
			for n2 in controllerStates:
				var1 = self.generateReachableI(n1)
				var2 = self.generateReachableI(n2)
				var3 = self.generatePairCSCS(n1, n2)
				self.addClause(['-' + var3, '-' + var1, var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RI prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def generatePropagationIG(self, task, controllerStates, k, debug = False):
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		for n in controllerStates:
			var1 = self.generateReachableI(n)
			var2 = self.generateReachableG(n, k)
			self.addClause(['-' + var1, var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: IG prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## REACH-G ####################
	###########################################

	def generateReachableGClauses(self, task, controllerStates, goalCState, k, debug = False):
		self.generateReachableGInitial(task, goalCState, controllerStates, k - 1, debug)
		self.generateCompletionReachabilityG(task, controllerStates, k - 1, debug)
		if self.strong:
			self.generatePropagationReachableGStrong(task, controllerStates, k - 1, debug)
		else:
			if not self.fair:
				self.generatePropagationReachableGUnfair(task, controllerStates, k - 1, debug)
			else:
				self.generatePropagationReachableGCyclic(task, controllerStates, k - 1, debug)	

	def generateReachableGInitial(self, task, goalCState, controllerStates, numberControllerStates, debug = False):
		# ReachG(ng,0), ReachG(ng,1), ...
		# -ReachG(n, 0) for n != ng
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		# set the initial values for goal state
		for i in range(numberControllerStates + 1):
			self.addClause([self.generateReachableG(goalCState, i)])
		# set the negation for non goal states
		for n in controllerStates:
			if n == goalCState:
				continue
			self.addClause(['-' + self.generateReachableG(n, 0)])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RG init\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def generateCompletionReachabilityG(self, task, controllerStates, k, debug = False):
		# ReachG(n,j) --> ReachG(n, j+1)
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		for n in controllerStates:
			for i in range(k):
				var1 = self.generateReachableG(n, i)
				var2 = self.generateReachableG(n, i + 1)
				self.addClause(['-' + var1, var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RG compl\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def setFairUnfairActions(self, task, controllerStates):
		# 1: (n, unfair) <-> \OR_{b: unf} (n,b)
		# 2: (n, fair) <-> \OR_{b: unf} (n,b)
		# 3: -(n, fair) \lor -(n, unfair)
		actions = task.get_action_names()
		for n in controllerStates:
			varPairUnf = self.generatePairUnfairCS(n)
			disj = ['-' + varPairUnf]
			for a in actions:
				if '_unfair_' in a:
					varPair = self.generatePairActionControllerState(a, n)
					self.addClause(['-' + varPair, varPairUnf]) # 1
					# print(['-' + varPair, varPairUnf])
					disj.append(varPair)
			self.addClause(disj) # 1
			# print(disj)
		for n in controllerStates:
			varPairF = self.generatePairFairCS(n)
			disj = ['-' + varPairF]
			for a in actions:
				if '_unfair_' not in a:
					varPair = self.generatePairActionControllerState(a, n)
					self.addClause(['-' + varPair, varPairF]) # 2
					# print(['-' + varPair, varPairF])
					disj.append(varPair) 
			self.addClause(disj) # 2
			# print(disj)
		for n in controllerStates:
			varF = self.generatePairFairCS(n)
			varU = self.generatePairUnfairCS(n)
			self.addClause(['-' + varF, '-' + varU]) # 3
			# print(['-' + varF, '-' + varU])

	def generatePropagationReachableGUnfair(self, task, controllerStates, k, debug = False):
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
		for i in range(k):
			for n1 in controllerStates:
				if n1 == 'ng':
					continue
				for n2 in controllerStates:
					varRepl = self.generateReplacementGoalPropagation(n1, n2, i)
					varPair = self.generatePairCSCS(n1, n2)
					varRG   = self.generateReachableG(n2, i)
					self.addClause(['-' + varRepl, '-' + varPair, varRG])
					self.addClause(['-' + varRG, varRepl])
					self.addClause([varPair, varRepl])
		# Force the equivalences for [3]
		# [(n, fair) \land (n,n') \land RG(n',j)] <-> Repl3(n,n',j)
		for i in range(k):
			for n1 in controllerStates:
				if n1 == 'ng':
					continue
				for n2 in controllerStates:
					varRepl = self.generateReplacementGoalPropagation3(n1, n2, i)
					varPair = self.generatePairCSCS(n1, n2)
					varFair = self.generatePairFairCS(n1)
					varRG   = self.generateReachableG(n2, i)
					self.addClause(['-' + varRepl, varPair])
					self.addClause(['-' + varRepl, varFair])
					self.addClause(['-' + varRepl, varRG])
					self.addClause([varRepl, '-' + varPair, '-' + varFair, '-' + varRG])
		# Right arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				varRG = self.generateReachableG(n1, i + 1)
				listStrong = [self.generatePairUnfairCS(n1)]
				listCyclic = []
				for n in controllerStates:
					listStrong.append(self.generateReplacementGoalPropagation(n1, n, i))
					listCyclic.append(self.generateReplacementGoalPropagation3(n1, n, i))
				clause = ['-' + varRG] + listCyclic
				for e in listStrong:
					self.addClause(clause + [e])
					# print(clause + [e])
		# Left arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				varRG = self.generateReachableG(n1, i + 1)
				listStrong = [self.generatePairUnfairCS(n1)]
				listCyclic = []
				for n in controllerStates:
					listStrong.append(self.generateReplacementGoalPropagation(n1, n, i))
					listCyclic.append(self.generateReplacementGoalPropagation3(n1, n, i))
				self.addClause([varRG] + ['-' + e for e in listStrong])
				# print([varRG] + ['-' + e for e in listStrong])
				for e in listCyclic:
					self.addClause([varRG, '-' + e])
					# print([varRG, '-' + e])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RG prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def generatePropagationReachableGCyclic(self, task, controllerStates, k, debug = False):
		# ReachG(n, j+1) <--> \OR_{n'} [(n,n') \land ReachG(n', j)]
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		# Force the equivalences
		for i in range(k):
			for n1 in controllerStates:
				if n1 == 'ng':
					continue
				for n2 in controllerStates:
					var1 = self.generateReplacementGoalPropagation(n1, n2, i)
					var2 = self.generatePairCSCS(n1, n2)
					var3 = self.generateReachableG(n2, i)
					self.addClause(['-' + var1, var2])
					self.addClause(['-' + var1, var3])
					self.addClause([var1, '-' + var2, '-' + var3])
		# Right arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				var1 = self.generateReachableG(n1, i + 1)
				var2 = ['-' + var1]
				for n2 in controllerStates:
					var3 = self.generateReplacementGoalPropagation(n1, n2, i)
					var2.append(var3)
				self.addClause(var2)
		# Left arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				var1 = self.generateReachableG(n1, i + 1)
				for n2 in controllerStates:
					var2 = self.generateReplacementGoalPropagation(n1, n2, i)
					self.addClause([var1, '-' + var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RG prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def generatePropagationReachableGStrong(self, task, controllerStates, k, debug = False):
		# ReachG(n, j+1) <--> \AND_{n'} [(n,n') --> ReachG(n', j)]
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		# Force the equivalences
		for i in range(k):
			for n1 in controllerStates:
				if n1 == 'ng':
					continue
				for n2 in controllerStates:
					varRepl = self.generateReplacementGoalPropagation(n1, n2, i)
					varPair = self.generatePairCSCS(n1, n2)
					varRG   = self.generateReachableG(n2, i)
					self.addClause(['-' + varRepl, '-' + varPair, varRG])
					self.addClause(['-' + varRG, varRepl])
					self.addClause([varPair, varRepl])
		# Right arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				varRG = self.generateReachableG(n1, i + 1)
				for n2 in controllerStates:
					varRepl = self.generateReplacementGoalPropagation(n1, n2, i)
					self.addClause(['-' + varRG, varRepl])
		# Left arrow
		for n1 in controllerStates:
			if n1 == 'ng':
				continue
			for i in range(k):
				disj = [self.generateReachableG(n1, i + 1)]
				for n2 in controllerStates:
					varRepl = self.generateReplacementGoalPropagation(n1, n2, i)
					disj.append('-' + varRepl)
				self.addClause(disj)

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: RG prop\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	###########################################
	############## SYMM-BREAKING ##############
	###########################################

	def generateSymmetryBreaking(self, task, controllerStates, initialCState, goalCState, debug = False):
		c1, v1 = self.get_num_cl_vars()
		start = timer()

		if len(controllerStates) >= 4:
			# (na, nb) --> \OR_{i<=a} (n_i, n_{b-1})
			for ia, na in enumerate(controllerStates[:-1]):
				for ib, nb in enumerate(controllerStates[:-1]):
					if ib in [0, 1]:
						continue
					nb_1 = controllerStates[ib - 1]
					var_pair_ab = self.generatePairCSCS(na, nb)
					disj = ['-' + var_pair_ab]
					for i in range(ia + 1):
						ni = controllerStates[i]
						disj.append(self.generatePairCSCS(ni, nb_1))
					self.addClause(disj)

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Sym brk\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))


	###########################################
	############## MUTEX GROUPS ###############
	###########################################

	def generateMutexGroupsClauses(self, task, controllerStates, debug = False):
		c1, v1 = self.get_num_cl_vars()
		start = timer()
		mutex_groups = task.get_mutex_groups()
		for mg in mutex_groups:
			pairs = self.__get_all_pairs(mg)
			for (a1, a2) in pairs:
				for n in controllerStates:
					var1 = self.generateAtomControllerState(a1, n)
					var2 = self.generateAtomControllerState(a2, n)
					self.addClause(['-' + var1, '-' + var2])

		c2, v2 = self.get_num_cl_vars()
		if debug:
			print('Generation: Mutex\t\t v %i \t\t c : %i \t\t %f' % (v2 - v1, c2 - c1, timer() - start))

	def __get_all_pairs(self, els):
		return [(e1, e2) for (i1, e1) in enumerate(els) for (i2, e2) in enumerate(els) if i2 > i1]
```



























