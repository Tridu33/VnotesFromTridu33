[TOC]

# NuSMV

官网 

文档 nusmv.fbk.eu

预发行二进制文件:

https://github.com/felipeblassioli/nusmv

编译安装方法:
https://wenku.baidu.com/view/6467fb48852458fb770b56bc.html



别人的笔记教程
https://blog.csdn.net/jmh1996/article/details/85871304

官方教程

## On-line documentation

-   [NuSMV User Manual PDF](http://nusmv.fbk.eu/NuSMV/userman/index-v2.html)
-   [NuSMV Tutorial-PDF](http://nusmv.fbk.eu/NuSMV/tutorial/index.html)
-   [NuSMV Programmer Manual在线版本](http://nusmv.fbk.eu/NuSMV/progman/progmanual-v2.html)，主要是[数据结构](http://nusmv.fbk.eu/NuSMV/progman/v26/html/annotated.html)
-   [NuSMV FAQ](http://nusmv.fbk.eu/faq.html)

## NuSMV Papers

[Here](http://nusmv.fbk.eu/NuSMV/papers.html) is the collection of papers related to NuSMV.

## NuSMV Examples

[Here](http://nusmv.fbk.eu/examples/examples.html) is the collection of NuSMV examples included in the distribution package.

官方文档

```
>NuSMV.exe -h
*** This is NuSMV 2.6.0 (compiled on Wed Oct 14 15:37:51 2015)
*** Enabled addons are: compass
*** For more information on NuSMV see <http://nusmv.fbk.eu>
*** or email to <nusmv-users@list.fbk.eu>.
*** Please report bugs to <Please report bugs to <nusmv-users@fbk.eu>>

*** Copyright (c) 2010-2014, Fondazione Bruno Kessler

*** This version of NuSMV is linked to the CUDD library version 2.4.1
*** Copyright (c) 1995-2004, Regents of the University of Colorado

*** This version of NuSMV is linked to the MiniSat SAT solver.
*** See http://minisat.se/MiniSat.html
*** Copyright (c) 2003-2006, Niklas Een, Niklas Sorensson
*** Copyright (c) 2007-2010, Niklas Sorensson

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
      enables interactive mode
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
      prints order of variablesto file "ov_file"
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
      does not read any initialization file (C:\Users\admin\nusmv/master.nusmvrc,
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




## 书中渡河问题




```
MODULE main

 VAR 
 ferryman : boolean;
 goat     : boolean;
 cabbage  : boolean;
 wolf     : boolean;

 carry: {g,c,w,0};

 ASSIGN

 init(ferryman):= 0; init(goat):=0;
 init(cabbage) :=0;  init(wolf):=0;
 init(carry)   :=0;

 next(ferryman) := 0,1;

 next(carry):= case
                 ferryman=goat: g;
                 1:0;
                 esac union
                 case
                     ferryman=cabbage:c;
                     1:0;
                 esac union
                 case
                 ferryman=wolf:w;
                 1:0;
                 esac union 0;
                 
next(goat):=case
    ferryman=goat & next(carry)=g:next(ferryman);
    1 : goat;
 esac;
 next(cabbage):=case
     ferryman=cabbage & next(carry)=c : next(ferryman);
     1: cabbage;
 esac;
 next(wolf):= case
     ferryman=wolf & next(carry)=w : next(ferryman);
     1:wolf;
 esac;
 
 LTLSPEC !((  (goat=cabbage | goat=wolf) -> goat=ferryman)
            U (cabbage & goat & wolf & ferryman))
```






























