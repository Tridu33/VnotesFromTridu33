[TOC]



```
python3 ~/downward-projects/downward/fast-downward.py domain.pddl task.pddl --search "astar(lmcut())"
```

```
python3 ~/downward-projects/downward/fast-downward.py blocks_clear_d.pddl blocks_clear_p.pddl --search "astar(lmcut())"
```


缩写

```
alias py3fd="python3 ~/downward-projects/downward/fast-downward.py"
```

```
py3fd blocks_clear_d.pddl blocks_clear_p.pddl --search "astar(lmcut())"
```

# 1. fast download

```
tridu33@tridu33:~/downward-projects/downward$ 
```
```
python3 fast-downward.py ../benchmarks/grid/prob01.pddl --search "astar(lmcut())"
```
http://www.fast-downward.org/PlannerUsage

```
# Clone Fast Downward and let it solve an example task.
git clone https://github.com/aibasel/downward.git
cd downward
./build.py
./fast-downward.py ../benchmarks/grid/prob01.pddl --search "astar(lmcut())"


# landmark-cut heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(lmcut())"

# iPDB heuristic with default settings
 ./fast-downward.py domain.pddl task.pddl --search "astar(ipdb())"

# blind heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(blind())"
```


https://github.com/aibasel/downward


http://www.fast-downward.org/LPBuildInstructions


http://www.fast-downward.org/ObtainingAndRunningFastDownward



https://stackoverflow.com/questions/18945035/fast-forward-and-pddl-is-the-computed-solution-the-best fd优于ff

http://www.fast-downward.org/


https://github.com/aibasel/downward

https://hackage.haskell.org/package/fast-downward 比如这里有个gripper例子



https://planning.wiki/ref/planners/fd


Jendrik Seipp  7:54 PM
Shameless plug: I'll be giving an ICAPS tutorial about "Evaluating Planners with Downward Lab" on October 20 at 19:00 UTC (https://icaps20subpages.icaps-conference.org/tutorials/evaluating-planners-with-downward-lab/). We'll talk about best practices for Downward Lab experiments and there'll be a Q&A session, so bring your questions!



https://icaps20subpages.icaps-conference.org/tutorials/evaluating-planners-with-downward-lab/ 




# 2. Lab and Downward Lab






Lab是一个Python软件包，用于评估基准集上的求解器。实验可以在单台计算机或计算机集群上运行。该软件包还包含用于解析结果和创建报告的代码。

该向下实验室Python包方便的运行实验快速向下规划体系。它使用通用实验软件包Lab。当前，实验室和向下实验室一起分发。

代码：https://github.com/aibasel/lab

文档：https://lab.readthedocs.io/en/latest/downward.tutorial.html

引用：请使用引用向下实验室



Examples:

```python
py3fd

#Translate and find a plan with A* + LM-Cut:
fast-downward.py misc/tests/benchmarks/gripper/prob01.pddl --search "astar(lmcut())"

#Translate and run no search:
fast-downward.py --translate misc/tests/benchmarks/gripper/prob01.pddl

#Run predefined configuration (LAMA-2011) on translated task:
fast-downward.py --alias seq-sat-lama-2011 output.sas

#Run a portfolio on a translated task:
fast-downward.py --portfolio driver/portfolios/seq_opt_fdss_1.py --search-time-limit 30m output.sas

#Run the search component in debug mode (with assertions enabled) and validate the resulting plan:
fast-downward.py --debug output.sas --search "astar(ipdb())"

#Pass options to translator and search components:
fast-downward.py misc/tests/benchmarks/gripper/prob01.pddl --translate-options --full-encoding --search-options --search "astar(lmcut())"

#Find a plan and validate it:
fast-downward.py --validate misc/tests/benchmarks/gripper/prob01.pddl --search "astar(cegar())"
#--------------------===========官网用法====================---------------------------
# landmark-cut heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(lmcut())"

# iPDB heuristic with default settings
 ./fast-downward.py domain.pddl task.pddl --search "astar(ipdb())"

# blind heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(blind())"

## using FF heuristic and context-enhanced additive heuristic (previously: "fFyY")
 ./fast-downward.py domain.pddl task.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])" 

## using FF heuristic (previously: "fF")
 ./fast-downward.py domain.pddl task.pddl  --evaluator "hff=ff()"  --search "lazy_greedy([hff], preferred=[hff])"  

## using context-enhanced additive heuristic (previously: "yY")
 ./fast-downward.py domain.pddl task.pddl   --evaluator "hcea=cea()"   --search "lazy_greedy([hcea], preferred=[hcea])"  


## LAMA2011
./fast-downward.py --alias seq-sat-lama-2011 domain.pddl task.pddl
```


help



```
usage: fast-downward.py [-h] [-v] [--show-aliases] [--run-all] [--translate]
                        [--search]
                        [--translate-time-limit TRANSLATE_TIME_LIMIT]
                        [--translate-memory-limit TRANSLATE_MEMORY_LIMIT]
                        [--search-time-limit SEARCH_TIME_LIMIT]
                        [--search-memory-limit SEARCH_MEMORY_LIMIT]
                        [--validate-time-limit VALIDATE_TIME_LIMIT]
                        [--validate-memory-limit VALIDATE_MEMORY_LIMIT]
                        [--overall-time-limit OVERALL_TIME_LIMIT]
                        [--overall-memory-limit OVERALL_MEMORY_LIMIT]
                        [--alias ALIAS] [--build BUILD] [--debug] [--validate]
                        [--log-level {debug,info,warning}] [--plan-file FILE]
                        [--sas-file FILE] [--keep-sas-file] [--portfolio FILE]
                        [--portfolio-bound VALUE] [--portfolio-single-plan]
                        [--cleanup]
                        INPUT_FILE1 [INPUT_FILE2] [COMPONENT_OPTION ...]

Fast Downward driver script.

Input files can be either a PDDL problem file (with an optional PDDL domain
file), in which case the driver runs both planner components (translate and
search), or a SAS+ translator output file, in which case the driver runs just
the search component. You can override this default behaviour by selecting
components manually with the flags below. The first component to be run
determines the required input files:

--translate: [DOMAIN] PROBLEM
--search: TRANSLATE_OUTPUT

Arguments given before the specified input files are interpreted by the driver
script ("driver options"). Arguments given after the input files are passed on
to the planner components ("component options"). In exceptional cases where no
input files are needed, use "--" to separate driver from component options. In
even more exceptional cases where input files begin with "--", use "--" to
separate driver options from input files and also to separate input files from
component options.

By default, component options are passed to the search component. Use
"--translate-options" or "--search-options" within the component options to
override the default for the following options, until overridden again. (See
below for examples.)

positional arguments:
  planner_args          file names and options passed on to planner components

driver options that show information and exit (don't run planner):
  -h, --help            show this help message and exit
  -v, --version         print version number and exit
  --show-aliases        show the known aliases (see --alias) and exit

driver options selecting the planner components to be run
(may select several; default: auto-select based on input file(s)):
  --run-all             run all components of the planner
  --translate           run translator component
  --search              run search component

time and memory limits:
  You can limit the time or memory for individual components
  or the whole planner. The effective limit for each component is the minimum
  of the component, overall, external soft, and external hard limits.

  Limits are given in seconds or MiB. You can change the unit by using the
  suffixes s, m, h and K, M, G.

  By default, all limits are inactive. Only external limits (e.g. set with
  ulimit) are respected.

  Portfolios require that a time limit is in effect. Portfolio configurations
  that exceed their time or memory limit are aborted, and the next
  configuration is run.

  --translate-time-limit TRANSLATE_TIME_LIMIT
  --translate-memory-limit TRANSLATE_MEMORY_LIMIT
  --search-time-limit SEARCH_TIME_LIMIT
  --search-memory-limit SEARCH_MEMORY_LIMIT
  --validate-time-limit VALIDATE_TIME_LIMIT
  --validate-memory-limit VALIDATE_MEMORY_LIMIT
  --overall-time-limit OVERALL_TIME_LIMIT
  --overall-memory-limit OVERALL_MEMORY_LIMIT

other driver options:
  --alias ALIAS         run a config with an alias (e.g. seq-sat-lama-2011)
  --build BUILD         BUILD can be a predefined build name like release
                        (default) and debug, a custom build name, or the path
                        to a directory holding the planner binaries. The
                        driver first looks for the planner binaries under
                        'BUILD'. If this path does not exist, it tries the
                        directory '<repo>/builds/BUILD/bin', where the build
                        script creates them by default.
  --debug               alias for --build=debug --validate
  --validate            validate plans (implied by --debug); needs "validate"
                        (VAL) on PATH
  --log-level {debug,info,warning}
                        set log level (most verbose: debug; least verbose:
                        warning; default: info)
  --plan-file FILE      write plan(s) to FILE (default: sas_plan; anytime
                        configurations append .1, .2, ...)
  --sas-file FILE       intermediate file for storing the translator output
                        (implies --keep-sas-file, default: output.sas)
  --keep-sas-file       keep translator output file (implied by --sas-file,
                        default: delete file if translator and search
                        component are active)
  --portfolio FILE      run a portfolio specified in FILE
  --portfolio-bound VALUE
                        exclusive bound on plan costs (only supported for
                        satisficing portfolios)
  --portfolio-single-plan
                        abort satisficing portfolio after finding the first
                        plan
  --cleanup             clean up temporary files (translator output and plan
                        files) and exit

component options:
  --translate-options OPTION1 OPTION2 ...
  --search-options OPTION1 OPTION2 ...
                        pass OPTION1 OPTION2 ... to specified planner component
                        (default: pass component options to search)


```

https://hackage.haskell.org/package/fast-downward 
居然还有haskell版本




