
[TOC]


# Q&A

群友问：

>如何理解语义和语法呢
语义是语言的特性吗



zz 回答：



>一个语言只有语义而没有语法，你就无法进行证明，而一个语言只有语法而没有语义，你就无法判断对错。  
从语法的可推出，到语义的有效，是谓可靠性。从语义的有效到到语法的可推出，是谓完全性也。





第一个strong cyclic planning,

挑出来一些算strong planning.



嗯呐，这个k好像是步长为1，从1开始，前向为负（回溯步长-1），后向为正


k =|S|

```
CNF不是a1 Λ a2 Λ ...... Λ an这种格式吗，它的算法不是要从S里面选若干个状态去填充这个CNF表达式，然后调用minisat去看是不是satisfiable吗？对于一个FOND问题，它的状态最多只有|S|个，所以当C(P，k)里面的k等于|S|+1的时候，意味着该问题不能解
```




how each high-level fluent can be translated into a low-level formula，论文中也出现过几次fluent是啥意思？

Let Q = <F, V, I, O, G> be a QNP. The number of boolean states for Q is exponential in the number of fluents and variables


```
《knowledge in action》作者Raymond Reiter ，书里应该有这个概念
记起来了，fluent你就当成是对一个原子变量的赋值。
在状态s下，变量F为真，那你就认为F是一个fluent叭
```

石头世界：

$Q_{clear} =$ <**F**,V,I,O,G>


F,{H}

V,{n(x)}

I,{$\neg H$,n(x)>0}

O,{a,b},
a=< $\neg H$,n(x)>0;H,n(x)$\downarrow$>,
b=<H;$\neg H$>

G={n(x)=0}









# minisat

```
USAGE: ./minisat <input-file> <result-output-file>
  where the input may be either in plain/gzipped DIMACS format or in BCNF.
```







# FOND-SAT

**核心代码**：

```
cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)
......
cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
......
command = './minisat %s %s' % (name_formula_file, name_output_satsolver)
......
result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)
......
```

这个cnf类，输入“`formula-temp.txt写有cnf的文件`、`formula-extra-temp.txt空可能要有打开条件`， fair, strong”可以实现转换成为`CNF`


```
cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)

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

	cnf.reset()
	start_g = timer()
	cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
	
	print('SAT formula generation time = %f' % (timer() - start_g))
	print('# Clauses = %i' % cnf.getNumberClauses())
	print('# Variables = %i' % cnf.getNumberVariables())

	if timer() - time_start > time_limit - time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')

	print('Creating formula...')
	name_final = cnf.generateInputSat(name_formula_file)
	
	print('Done creating formula. Calling solver...')
	start_solv = timer()

	time_for_sat = int(time_limit - (timer() - time_start))
	if time_for_sat < time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')
```

然后就是调用求解了。


```
python main.py ../F-domains/islands/domain.pddl ../F-domains/islands/p03.pddl -policy 1
```
参数字典：

```
# params字典
{'time_limit': 3600, 
'inc': 1, 
'path_domain': '../F-domains/islands/domain.pddl', 
'gen_info': 0, 'policy': 1, 
'mem_limit': 4096, 
'strong': 0, 
'path_instance': '../F-domains/islands/p03.pddl', 
'name_temp': 'temp'
}
```
所以取代命令行去参数的运行方法是：
```
params={'time_limit': 3600, 'inc': 1, 'path_domain': '../F-domains/islands/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 0, 'path_instance': '../F-domains/islands/p03.pddl', 'name_temp': 'temp'}
```


```
python main.py ../F-domains/islands/domain.pddl ../F-domains/islands/p03.pddl -strong 1 -inc 2 -policy 1
```
最后成功运行的例程：

```
restarts              : 0
conflicts             : 0              (-nan /sec)
decisions             : 0              (-nan /sec)
propagations          : 191            (inf /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 13.92 MB
CPU time              : 0 s

UNSATISFIABLE
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |    2958     7243 |     986       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 8              (512 /sec)
decisions             : 10             (640 /sec)
propagations          : 749            (47936 /sec)
conflict literals     : 15             (21.05 % deleted)
Memory used           : 13.92 MB
CPU time              : 0.015625 s

UNSATISFIABLE
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |    5128    12958 |    1709       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 27             (inf /sec)
decisions             : 59             (inf /sec)
propagations          : 3126           (inf /sec)
conflict literals     : 111            (24.49 % deleted)
Memory used           : 14.05 MB
CPU time              : 0 s

SATISFIABLE
('WARNING: variable not Atom nor NegatedAtom;', '<none of those>')
```

main.py这行：

```
>>> my_task = p.translate_to_atomic()
```

输出

```
Setting atoms
# Atoms: 31
Setting initial
Setting goal
Setting actions
# Actions: 80
	Setting other actions
(0, '/', 80)
	Setting action card
Setting mutexes
Setting relevant actions
Setting splitting
Setting compatible actions
(0, '/', 80)
0.00220704078674

```

main.py 92 

```
cnf = CNF(name_formula_file, name_formula_file_extra, fair, strong)

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

	cnf.reset()
	start_g = timer()
	cnf.generate_clauses(my_task, 'n0', 'ng', controllerStates, len(controllerStates), p, show_gen_info)
	
	print('SAT formula generation time = %f' % (timer() - start_g))
	print('# Clauses = %i' % cnf.getNumberClauses())
	print('# Variables = %i' % cnf.getNumberVariables())

	if timer() - time_start > time_limit - time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')

	print('Creating formula...')
	name_final = cnf.generateInputSat(name_formula_file)
	
	print('Done creating formula. Calling solver...')
	start_solv = timer()

	time_for_sat = int(time_limit - (timer() - time_start))
	if time_for_sat < time_buffer:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME')

	command = './minisat %s %s' % (name_formula_file, name_output_satsolver)
	# command = '/path/to/SATsolver/minisat -mem-lim=%i -cpu-lim=%i %s %s' % (mem_limit, time_for_sat, name_formula_file, name_output_satsolver)
	print('SAT solver called with %i MB and %i seconds' % (mem_limit, time_for_sat))
	os.system(command)
	end_solv = timer()
	solver_time.append(end_solv - start_solv)
	print('Done solver. Round time: %f' % (end_solv - start_solv))
	print('Cumulated solver time: %f' % sum(solver_time))
	
	result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)
	if result is None:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME/MEM')
	if result:
		break
	print('UNSATISFIABLE')
	
```

**./minisat %s %s' % (name_formula_file, name_output_satsolver）**

根据minisat用法：

```
USAGE: ./minisat <input-file> <result-output-file>
  where the input may be either in plain/gzipped DIMACS format or in BCNF.
```
也就是说在命令行输入：

```
./minisat formula-temp.txt outsat-temp.txt
```

如果在命令行输入单独运行cnf生成sat求解的过程是：

```
$ ./minisat test-formula-temp.txt test-outsat-temp.txt
==================================[MINISAT]===================================
| Conflicts |     ORIGINAL     |              LEARNT              | Progress |
|           | Clauses Literals |   Limit Clauses Literals  Lit/Cl |          |
==============================================================================
|         0 |    5128    12958 |    1709       0        0    -nan |  0.000 % |
==============================================================================
restarts              : 1
conflicts             : 32             (2048 /sec)
decisions             : 64             (4096 /sec)
propagations          : 3495           (223680 /sec)
conflict literals     : 136            (21.84 % deleted)
Memory used           : 14.05 MB
CPU time              : 0.015625 s

SATISFIABLE
```

对应的是main.py运行过程中最最最开始的运行结果，先运行minisat再出现结果，因为Demo需要找4过程才能出结果，所以调用3次minisat开头出现3次这段使用情况，以及前两次test-outsat-temp.txt用python读取为result==None为空说明./minisat找不到可满足的，于是UNSATISFIABLE，知道第三次找到之后就是SATISFIABLE可满足有解。

对应整体命令行的输出下面的：

```
=================================================
Trying with 2 states
Looking for strong plans: False
Fair actions: True
# Atoms: 31
# Actions: 80
SAT formula generation time = 0.008767
# Clauses = 2877
# Variables = 276
Creating formula...
Done creating formula. Calling solver...
SAT solver called with 4096 MB and 3599 seconds
Done solver. Round time: 0.050868
Cumulated solver time: 0.050868
UNSATISFIABLE
=================================================
Trying with 3 states
Looking for strong plans: False
Fair actions: True
# Atoms: 31
# Actions: 80
SAT formula generation time = 0.020353
# Clauses = 4917
# Variables = 450
Creating formula...
Done creating formula. Calling solver...
SAT solver called with 4096 MB and 3599 seconds
Done solver. Round time: 0.022791
Cumulated solver time: 0.073659
UNSATISFIABLE
=================================================
Trying with 4 states
Looking for strong plans: False
Fair actions: True
# Atoms: 31
# Actions: 80
SAT formula generation time = 0.030047
# Clauses = 7458
# Variables = 656
Creating formula...
Done creating formula. Calling solver...
SAT solver called with 4096 MB and 3599 seconds
Done solver. Round time: 0.022768
Cumulated solver time: 0.096427

```

CNF.py中的parserOutput方法

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
Atom person-at(l22-1) (n0)
Atom person-alive() (n0)
Atom bridge-clear() (n0)
----------
Atom person-at(l21-1) (n1)
Atom person-alive() (n1)
Atom bridge-clear() (n1)
----------
Atom person-at(l22-2) (n2)
Atom person-alive() (n2)
----------
Atom person-at(l21-2) (ng)
===================
===================
(CS, Action with arguments)
___________________
(n0,move-person(l22-1,l21-1))
(n0,move-person)
(n1,walk-on-bridge(l21-1,l22-2))
(n1,walk-on-bridge)
(n2,move-person)
(n2,move-person(l22-2,l21-2))
===================
===================
(CS, Action name, CS)
___________________
(n0,move-person,n1)
(n1,walk-on-bridge,n2)
(n2,move-person,ng)
===================
(CS, CS)
___________________
(n2,ng)
(n0,n1)
(n1,n2)
===================
Solved with 4 states
```


main.py 137


```
print('Elapsed total time (s): %f' % (timer() - time_start))
print('Elapsed solver time (s): %f' % sum(solver_time))
print('Elapsed solver time (s): %s' % str(solver_time))
print('Looking for strong plans: %s' % str(strong))
print('Fair actions: %s' % str(fair))
clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, 'Done')
```

```
Elapsed total time (s): 0.354544
Elapsed solver time (s): 0.096427
Elapsed solver time (s): [0.05086803436279297, 0.022791147232055664, 0.022768020629882812]
Looking for strong plans: False
Fair actions: True
Done

```


# bugs

```
from parser import Parser
```

无法导入自己定义的类，观察__pycache__没有对应.pyc导入不成功也发现

暂时low炸天的解决方法是复制parser.py代码到main.py文件,成功。






##  bug2

```
Traceback (most recent call last):
  File "main.py", line 432, in <module>
    result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)
  File "C:\Users\admin\Desktop\hush\FOND-SAT\src\CNF.py", line 202, in parseOutput
    fres = open(nameFile, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'outsat-temp.txt'
```
观察源码
暂时g 430

```
	print('Cumulated solver time: %f' % sum(solver_time))

	result = cnf.parseOutput(name_output_satsolver, controllerStates, p, print_policy)
	if result is None:
		clean_and_exit(name_formula_file, name_output_satsolver, name_sas_file, name_formula_file_extra, name_final, '-> OUT OF TIME/MEM')
	if result:
		break
	print('UNSATISFIABLE')
```

回调

```
	def parseOutput(self, nameFile, controllerStates, parser, print_policy = False):
		sets = [set([]) for i in range(self.num_types)]
		fres = open(nameFile, 'r')
		res = fres.readlines()
		
```

FileNotFoundError: [Errno 2] No such file or directory: 'outsat-temp.txt'


## debug







```
Traceback (most recent call last):
  File "translate/translate.py", line 692, in <module>
    main()
  File "translate/translate.py", line 678, in main
    sas_task = pddl_to_sas(task)
  File "translate/translate.py", line 518, in pddl_to_sas
    groups, mutex_groups, translation_key = fact_groups.compute_groups(
  File "/home/tridu33/document/FOND-SAT/src/translate/fact_groups.py", line 110, in compute_groups
    groups = invariant_finder.get_groups(task, reachable_action_params)
  File "/home/tridu33/document/FOND-SAT/src/translate/invariant_finder.py", line 134, in get_groups
    invariants = sorted(find_invariants(task, reachable_action_params))
  File "/home/tridu33/document/FOND-SAT/src/translate/invariant_finder.py", line 102, in find_invariants
    start_time = time.clock()
AttributeError: module 'time' has no attribute 'clock'
Traceback (most recent call last):
  File "main.py", line 92, in generate_task
    f_task = open(sas_file_name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'outputtrans-temp.sas'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 370, in <module>
    p.generate_task(name_sas_file)
  File "main.py", line 94, in generate_task
    raise MyError('Error opening sas file!')
__main__.MyError: 'Error opening sas file!'

```



The error occurs because in python 2, there is `time.clock()`, but in python 3, it has been replaced with `time.perf_counter()`.

```
➜  src grep -r time.clock ./
./translate/invariant_finder.py:    start_time = time.clock()
./translate/invariant_finder.py:        if time.clock() - start_time > task.INVARIANT_TIME_LIMIT:

```


Linux下

```
 ./minisat:cannot execute binary file: Exec format error
```
























## from parser import Parser 



```

#-------------------------------------
#from parser import Parser
#'''
from objs import Variable, Operator

def generate_atom(name, val):
  return '(' + name + '=' + str(val) + ')'

class MyError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class Parser:
  def __init__(self):
    self.domain = None
    self.problem = None
    self.task = None
    self.variables = {} # map, int (vars number) --> Variable object
    self.initial = {}
    self.goal = {}
    self.operators = set([])
    self.mutex_groups = [] # list containing mutex groups; each is a list of tuples, each tuple has 2 elements, (var, val)

  def print_task(self):
    self.print_variables()
    print('==============================')
    self.print_initial()
    print('==============================')
    self.print_goal()
    print('==============================')
    self.print_operators()

  def print_operators(self):
    for o in self.operators:
      print(o.name)
      print('PRE')
      for p in o.prec:
        var = p[0]
        val = p[1]
        print(self.variables[var].get_str(val))
      print('EFFECTS')
      for p in o.effects:
        var = p[0]
        val1 = p[1]
        val2 = p[2]
        if val1 == -1:
          print('---------', self.variables[var].get_str(val2))
        else:
          print(self.variables[var].get_str(val1), self.variables[var].get_str(val2))
      print('-----------------------')

  def print_variables(self):
    for v in self.variables:
      print(v)
      self.variables[v].print_me()
      print('-----------------------')

  def print_initial(self):
    for i in self.initial:
      print(self.variables[i].get_str(self.initial[i]))

  def print_goal(self):
    for i in self.goal:
      print(self.variables[i].get_str(self.goal[i]))  

  def set_domain(self, path_domain):
    self.domain = path_domain

  def set_problem(self, path_problem):
    self.problem = path_problem

  def generate_file(self, sas_file_name):
    if self.domain == None or self.problem == None:
      raise MyError('Domain and/or problem not set!')
    time_limit = 1000
    command = 'python translate/translate.py ' + str(time_limit) + ' ' + self.domain + ' ' + self.problem + ' ' + sas_file_name + ' | grep "noprint"'
    os.system(command)

  def generate_task(self, sas_file_name):
    try:
      f_task = open(sas_file_name, 'r')
    except:
      raise MyError('Error opening sas file!')
    lines = f_task.readlines()
    lines = self.__process_lines(lines)
    limits = self.__get_limits(lines)
    for (init, end) in limits:
      self.process(lines[init + 1: end], lines[init])

  def process(self, lines, title):
    if 'version' in title:
      self.process_version(lines)
    if 'metric' in title:
      self.process_metric(lines)
    if 'variable' in title:
      self.process_variable(lines)
    if 'mutex_group' in title:
      self.process_mutex_group(lines)
    if 'state' in title:
      self.process_initial_state(lines)
    if 'goal' in title:
      self.process_goal(lines)
    if 'operator' in title:
      self.process_operator(lines)
    if 'rule' in title:
      self.process_rule(lines)

  def process_version(self, lines):
    # TODO
    return None

  def process_metric(self, lines):
    # TODO
    return None

  def process_variable(self, lines):
    v = Variable()
    value = int(v.set_name(lines[0]))
    rg = int(lines[2])
    for i in range(rg):
      v.add_value(i, lines[2 + i + 1])
    self.variables[value] = v

  def process_mutex_group(self, lines):
    mutex_g = []
    for line in lines[1:]:
      var = int(line.split(' ')[0])
      val = int(line.split(' ')[1])
      mutex_g.append((var, val))
    self.mutex_groups.append(mutex_g)

  def process_initial_state(self, lines):
    for i, line in enumerate(lines):
      self.initial[i] = int(line) # var, value

  def process_goal(self, lines):
    first = True
    for line in lines:
      if first:
        first = False
        continue
      var = int(line.split(' ')[0])
      value = int(line.split(' ')[1])
      self.goal[var] = value

  def process_operator(self, lines):
    o = Operator(self.variables)
    o.set_name(lines[0])
    num_prev_cond = int(lines[1])
    if num_prev_cond != 0:
      self.__process_prevail_conditions(lines[2:2 + num_prev_cond], o)
    line_num_effects = 2 + num_prev_cond
    num_effects = int(lines[line_num_effects])
    if num_effects != 0:
      self.__process_effects(lines[line_num_effects + 1:line_num_effects + num_effects + 1], o)
    self.operators.add(o)
    # o.print_me()

  def process_rule(self, lines):
    # TODO
    return None

  def __process_effects(self, lines, operator):
    for line in lines:
      l_split = line.split(' ')
      if len(l_split) != 4:
        raise MyError('Incorrect number of components in effects of an operator!')
      if l_split[0] != '0':
        raise MyError('First component of effects != 0!')
      var = int(l_split[1])
      pre = int(l_split[2])
      eff = int(l_split[3])
      operator.add_prec_eff(var, pre, eff)

  def __process_prevail_conditions(self, lines, operator):
    for line in lines:
      try:
        var, value = line.split(' ')
      except:
        raise MyError('Error processing prevail conditions!')
      operator.add_precondition(int(var), int(value))

  def __get_limits(self, lines):
    initis = []
    ends = []
    for i, line in enumerate(lines):
      if 'begin_' in line:
        initis.append(i)
      if 'end_' in line:
        ends.append(i)
    if len(initis) != len(ends):
      raise MyError('Inits and ends of different size!')
    return zip(initis, ends)

  def __process_lines(self, lines):
    p_lines = []
    for line in lines:
      p_lines.append(line.split('\n')[0])
    return p_lines

  def translate_to_atomic(self):
    task = MyTask()
    debug = False
    print('Setting atoms')
    task.set_atoms(self.get_atoms(), debug)
    print('Setting initial')
    task.set_initial(self.get_initial_atomic(), debug)
    print('Setting goal')
    task.set_goal(self.get_goal_atomic(), debug)
    print('Setting actions')
    task.set_actions_atomic(self.get_actions_atomic(), debug)
    print('Setting mutexes')
    task.set_mutex_groups(self.get_mutex_groups_atomic(), debug)
    print('Setting relevant actions')
    task.set_relevant_actions(debug)
    print('Setting splitting')
    task.initialize_splitting(debug)
    start = timer()
    print('Setting compatible actions')
    task.create_compatible_actions(debug)
    print(timer() - start)
    return task

  def get_atoms(self):
    atoms = set([])
    for v in self.variables:
      var = self.variables[v]
      for val in var.possible_values:
        atoms.add(generate_atom(var.name, val))
    return atoms

  def get_initial_atomic(self):
    initial = set([])
    for var in self.initial:
      value = self.initial[var]
      initial.add(generate_atom(self.variables[var].name, value))
    # print initial
    return initial

  def get_goal_atomic(self):
    goal = set([])
    for var in self.goal:
      value = self.goal[var]
      goal.add(generate_atom(self.variables[var].name, value))
    # print goal
    return goal

  def get_actions_atomic(self):
   actions = {}
   for action in self.operators:
     act_name = action.name
     preconditions = set([])
     add_list = set([])
     del_list = set([])
     for var, val in action.prec:
       preconditions.add(generate_atom(self.variables[var].name, val))
     for var, pre, post in action.effects:
       name = self.variables[var].name
       if pre != -1:
         # -1 is for value not important
         atom_pre = generate_atom(name, pre)
         preconditions.add(atom_pre)
         if pre != post:
           # the var changed --> old value to del list
           del_list.add(atom_pre)
       if post != -1:
         add_list.add(generate_atom(name, post))
         # also, delete all other possible values! (if not in prec)
         if pre == -1:
           var_values = self.variables[var].possible_values
           for v in var_values:
             if v == post:
               continue
             atom_del = generate_atom(name, v)
             del_list.add(atom_del)
     actions[act_name] = [list(preconditions), list(add_list), list(del_list)]
   return actions

  def get_mutex_groups_atomic(self):
    mutex_groups_atomic = []
    for mutex_group in self.mutex_groups:
      # mutex_group is a list of tuples
      mg = []
      for var, val in mutex_group:
        name = self.variables[var].name
        mg.append(generate_atom(name, val))
      mutex_groups_atomic.append(mg)
    return mutex_groups_atomic

  def get_var_string(self, name):
    # name = (varX=Y)
    s = name[1:len(name) - 1]
    # s = varX=Y
    var = int(s.split('=')[0].split('var')[1])
    val = int(s.split('=')[1])
    return self.variables[var].get_str(val)

#'''
#from parser import Parser 
# End
#------------------------------------


```












