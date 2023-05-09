[TOC]

# qnp2fond
```
./qnp2fond [--force-direct] [--disable-optimizations] <qnp-file> <num-bits-per-counter> <max-stack-depth> <prefix>
```


例子

```
$ ./qnp2fond ./blocks04.qnp 2 2  blocks04_output
call: ./qnp2fond ./blocks04.qnp 2 2 blocks04_output
qnp: #features=5, #numeric=2, #boolean=3, #actions=8
using full translation...
translation: time=0
translation: stats.extra=[ 9 8 4 2 2 ]
fond: #features=22, #actions=16
```

有理由相信，pddl2cnf翻译是现成的轮子代码，输入输出已经很明确了。

```
/hush$ diff ./FOND-SAT/src/translate/translate.py ./PRP/planner-for-relevant-policies/src/translate/translate.py
651,652d650
<         "sas_name", help="sas file name")
<     argparser.add_argument(
659d656
<     print('HOLAAAAAAAAAAAAAAAAAAAAAAA')
686c683
<         with open(args.sas_name, "w") as output_file:
---
>         with open("output.sas", "w") as output_file:
```



命令行执行：

```
command = 'python translate/translate.py ' + str(time_limit) + ' ' + self.domain + ' ' + self.problem + ' ' + sas_file_name + ' | grep "noprint"'
```
使用domain文件和问题描述文件pddl通过translate.py生成翻译后的sas文件


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
move-right l1 l2
0
1
0 0 0 1
0
end_operator
begin_operator
move-right l2 l1
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
```












































