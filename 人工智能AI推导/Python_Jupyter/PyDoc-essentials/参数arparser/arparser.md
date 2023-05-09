# arparser



[https://docs.python.org/3/howto/argparse.html](https://docs.python.org/3/howto/argparse.html)


[https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html)
































```
import argparse

# PARSE ARGUMENTS
args_parser = argparse.ArgumentParser(description = 'Process arguments to SAT FOND planner')
args_parser.add_argument('path_domain', help = 'Path to domain file (pddl) -- NOT OPTIONAL')
args_parser.add_argument('path_instance', help = 'Path to instance file (pddl) -- NOT OPTIONAL')
args_parser.add_argument('-time_limit', type = int, default = 3600, help = 'Time limit (int) for solver in seconds (default 3600 s)')
args_parser.add_argument('-mem_limit',  type = int, default = 4096, help = 'Memory limit (int) for solver in MB (default 4096 MB)')
args_parser.add_argument('-name_temp', default = 'temp', help = 'Name for temp files (erased after solver is done)')
args_parser.add_argument('-strong', type = int, default = 0, help = '1: strong planning mode; 0: default, strong cyclic planning mode')
args_parser.add_argument('-inc', type = int, default = 1, help = 'Increments in controller size per step (> 0, default 1)')
args_parser.add_argument('-gen_info', type = int, default = 0, help = '1: shows info about SAT formula generation; 0: default, does not show info')
args_parser.add_argument('-policy', type = int, default = 0, help = '1: shows final policy (if found); 0: default, does not show policy')

params = vars(args_parser.parse_args())#保存为params字典
if params['strong'] not in [0, 1]:
	print('Argument strong has to be 0 or 1')
	exit()
if params['policy'] not in [0, 1]:
	print('Argument policy has to be 0 or 1')
	exit()
if params['inc'] <= 0:
	print('Argument inc has to be > 0')
	exit()
########读取参数和默认值出来的结果保存为params字典#########
#print params dictionary
#print(params)
#raw_input()暂停
# Run code  below in ipython
# demo's params={'time_limit': 3600, 'inc': 1, 'path_domain': '../F-domains/islands/domain.pddl', 'gen_info': 0, 'policy': 1, 'mem_limit': 4096, 'strong': 0, 'path_instance': '../F-domains/islands/p03.pddl', 'name_temp': 'temp'}
```

后续 数据直接用，比如：

```
time_limit = params['time_limit']#3600 default 
```
























































