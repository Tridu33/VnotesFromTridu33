





[TOC]
chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://nusmv.fbk.eu/NuSMV/userman/v26/nusmv.pdf

The NuSMV home page:

http://nusmv.fbk.eu/

The NuSMV mailing list page:

http://nusmv.fbk.eu/mail.html

The most recent versions of NuSMV:

http://nusmv.fbk.eu/download.html

The home page of nuXmv, the extension over NuSMV to allow for
synchronous infinite-state systems:

http://nuxmv.fbk.eu

The CUDD home page:

http://vlsi.colorado.edu/~fabio/CUDD/

The MiniSat page:

http://MiniSat.se/

The ZCHAFF home page:

http://www.princeton.edu/~chaff/zChaff.html

The OpenSource site:

http://www.opensource.org/

The GNU General Public License home page:

http://www.gnu.org/copyleft/


# 1. NuSMV
[examples本地文件链接](file:///D:/tridu33/postgraduate/ModelChecking/NuSMV-2.6.0-win64/share/nusmv/examples)

https://nusmv.fbk.eu/examples/examples.html  案例


https://download.csdn.net/download/xh971801361/10155337
电梯例子 


https://blog.csdn.net/weixin_40388441/article/details/100068637
NuSMV实例




基于Ocaml语言实现Ocaml定义的语义模型到nuSMV程序的转换,实现nuSMV的自动化建模。
https://wap.cnki.net/lunwen-1017278874.nh.html
从Murphi到Ocaml语言的编译器及其在模型检测中的应用


精简运行
```
nusmv .smv
```


交互运行

```
nusmv -int .smv
```

```NuSMV -int,

set verbose_level 5

read_model -i counter.smv
flatten_hierarchy

encode_variables

build_model

pick_state -i

simulate -i 1

check_ctlspec -p "AG (!bit2.carry_out)"

```


```nusmv
Usage:  NuSMV [-h | -help] [options]* [input_file]
   -h | -help
      prints out current message
   -AG
      enables AG only search
   -bdd_soh heuristics
      sets the static variable ordering heuristics to "heuristics"
   -bmc
      enables BMC instead of BDD model checking
   -bmc_length k
      sets bmc_length variable, used by BMC
      NOTE: Requires option "-bmc"
   -coi
      enables cone of influence reduction
   -cp cp_t
      conjunctive partitioning with threshold of each partition set to "cp_t" (DEFAULT,
      with cp_t=1000). Use -thresh instead of this.
      NOTE: Incompatible with options -iwls95 -mono -thresh
      WARNING: option "-cp" is deprecated
   -cpp
      runs preprocessor on SMV files before any specified with -pre. Environment
      variable 'CPP' can be used to specify a different preprocessor.
      WARNING: option "-cpp" is deprecated
   -ctt
      enables checking for the totality of the transition relation
   -dcx
      disables computation of counter-examples
   -df
      disables the computation of reachable states
      NOTE: Incompatible with option -f
   -disable_daggifier
      disables the SMV model dumper daggifier
   -disable_sexp2bdd_caching
      disables caching of expressionsevaluation to BDD
   -disable_syntactic_checks
      Skips some correctness checks over the input model. Warning: when using this
      option, the input model MUST be correct, otherwise the tool may crash
   -dynamic
      enables dynamic reordering of variables
   -f
      computes the reachable states (forward search) (default)
      NOTE: Incompatible with option -df
      WARNING: option "-f" is deprecated
   -flt
      computes the reachable states also for the LTL Tableau
   -i iv_file
      reads order of variables from file "iv_file"
   -ic
      does not check COMPUTE
   -ii
      does not check INVARSPEC
   -ils
      does not check LTLSPEC
   -int
      enables interactive mode交互模式
   -ips
      does not check PSLSPEC
   -is
      does not check SPEC
   -iwl95preorder
      enables iwls95 preordering
   -iwls95 cp_t
      enables Iwls95 conjunctive partitioning and sets
      NOTE: Incompatible with options -thresh -mono -cp
   -keep_single_value_vars
      Does not convert variables that have only one single possible value into constant
      DEFINEs
   -load sc_file
      executes NuSMV commands from file
      NOTE: Incompatible with option -source
      WARNING: option "-load" is deprecated
   -lp
      lists all properties in SMV model
   -m method
      sets the variable ordering method to "method". Reordering will be activated
   -mono
      enables monolithic transition relation
      NOTE: Incompatible with options -thresh -iwls95 -cp
   -n idx
      specifies which property of SMV model should be checked
   -noaffinity
      disables affinity clustering
   -o ov_file
      prints order of variables to file "ov_file"
   -obm bn_file
      prints boolean model to file "bn_file"
   -ofm fn_file
      prints flattened model to file "fn_file"
   -ojeba str
      sets the algorthim used for BDD-based language emptiness of Buchi fair transition
      systems (default is EL_bwd). The available algorthims are: EL_fwd, EL_bwd
   -old
      keeps backward compatibility with older versions of NuSMV
   -old_div_op
      enables the old semantics of "/" and "mod" operations instead of ANSI C semantics
   -pre pp_list
      defines a space-separated list of pre-processors to run (in the order given)
      on the input file. The list must be in double quotes if there is more than one pre-processor
      named.
      The available preprocessors are: cpp m4
   -r
      enables printing of reachable states
   -reorder
      enables reordering of variables before exiting
   -rin on|off
      enables (on) or disables rbc inlining (default is on)
   -s
      does not read any initialization file (C:\Users\HUMAN\nusmv/master.nusmvrc,
      ~/.nusmvrc) (default in batch mode)
   -sat_solver str
      sets the sat_solver variable, used by BMC. The available SAT solvers are: MiniSat
   -sin on|off
      enables (on) or disables sexp inlining (default is off)
   -source sc_file
      executes NuSMV commands from file
      NOTE: Incompatible with option -load
   -t tv_file
      reads order of vars for clustering from file "tv_file"
   -thresh cp_t
      conjunctive partitioning with threshold of each partition set to "cp_t" (DEFAULT,
      with cp_t=1000)
      NOTE: Incompatible with options -iwls95 -mono -cp
   -v vl
      sets verbose level to "vl"
   input-file
      the file both the model and the spec were read from

```




















以下实验使用NuSMV https://nusmv.fbk.eu/

| &        | \|     | **$\rightarrow$** | !      |
| -------- | ------ | ----------------- | ------ |
| $\wedge$ | $\vee$ | $\rightarrow$     | $\neg$ |

-->l1<-->l2

```nusmv
MODULE main
VAR
	location: {l1,l2};
ASSIGN
	init(location) := l1;
	next(location) := case
				(location = l1):l2;
				(location = l2):l1;
					esac;
```

保存为```intro.smv``` 交互式运行：


```
reset; read_model -i t.smv ; go
```



```
./>nusmv -int 

read_model -i intro.smv
flatten_hierarchy
encode_variables
build_model
pick_state -i
```

输出初始状态：

```

***************  AVAILABLE STATES  *************

  ================= State =================
  0) -------------------------
  location = l1
  
There's only one available state. Press Return to Proceed.

Chosen state is: 0
```

输入：

```
NuSMV > print_reachable_states -v
```

打印状态转移图，对应的状态及其下一个状态，输出：

```
######################################################################
system diameter: 2
reachable states: 2 (2^1) out of 2 (2^1)
  ------- State    1 ------
  location = l2
  ------- State    2 ------
  location = l1
  -------------------------
######################################################################
```

输入：

```
NuSMV > simulate -i -k 3
```

动态“迁移系统仿真3步，输出仿真结果：

```
********  Simulation Starting From State 1.11   ********

***************  AVAILABLE STATES  *************

  ================= State =================
  0) -------------------------
  location = l2


There's only one available state. Press Return to Proceed.

Chosen state is: 0

***************  AVAILABLE STATES  *************

  ================= State =================
  0) -------------------------
  location = l1


There's only one available state. Press Return to Proceed.

Chosen state is: 0

***************  AVAILABLE STATES  *************

  ================= State =================
  0) -------------------------
  location = l2


There's only one available state. Press Return to Proceed.

Chosen state is: 0
NuSMV >quit
```






