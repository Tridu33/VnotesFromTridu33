
程序或算法可以被形式化地证明是正确的吗，如果可以，应该如何证明？ - Jason Hu的回答 - 知乎
https://www.zhihu.com/question/21578571/answer/700799496


Z3 https://github.com/Z3Prover/z3
Vampire https://vprover.github.io/
Matryoshka http://matryoshka.gforge.inria.fr/
Dafny https://rise4fun.com/Dafny
Ivy https://github.com/microsoft/ivy
Isabelle https://isabelle.in.tum.de/
HOL https://hol-theorem-prover.org/
Coq https://coq.inria.fr/
Agda https://agda.readthedocs.io/en/v2.6.0.1/
Lean https://leanprover.github.io/about/
VST https://github.com/PrincetonUniversity/VST



可以。你所说的领域叫做software verification，横跨了数学、理论计算机和软件工程的很大的应用方向。做software verification有整一个谱系的方法。

全自动化。

model checking。

model checking需要你把specification用temporal logic来表达。典型的temporal logic有CTL, LTL和CTL*。model checking有个好处就是提到的三个temporal logic都有完备的检查算法，因此是全自动的。在状态空间有限的情况下model checking的应用很普遍，比方说电子硬件又或者是分布式协议。

SAT。

有完备的NP-complete算法。DPLL算法是历史上的突破点。


SMT和automatic theorem prover。

现有成熟的都是基于first order logic，内部用到了SAT。SMT专注于arithematic而automatic theorem prover专注于quantifiers。有名的有MSR的z3[1] 和Vampire[2]。荷兰有个项目在开发基于AI和higher order logic的SMT，非常有前途。[3] 但是注意first order logic是undecidable theory所以这个自动工具的能力有限。要利用这些工具进行定理证明需要你对实现有很深的理解。

半自动。

半自动的往往是基于SMT的。比方说Dafny[4]和Ivy[5]。他们本身是编程语言，可以编写specification验证写的程序。Dafny和Ivy都是基于z3的。这个方向在纯软件工程很常见，这些工具往往都是软工的人开发的。

（基本上）全手动。

这一类型的工具更加偏向于数学性的。常见的有Isabelle[6], HOL[7], Coq[8], Agda[9]和Lean[10]。他们有的是基于formal logic，比方说Isabelle和HOL，有的基于type theory比方说剩下三个。但是本质上他们本身也是编程语言。我对type theory比较了解。在type theory，你可以表达很多的程序，包括很多高阶的程序，你用Dafny是没办法验证的。虽然这些语言都是函数式语言，你也可以用他们来验证其他程序。比方说VST[11]用Coq里的separation logic模型来验证C程序。

基本上，这个方向的工具太多了。一般来讲，自动化越强的可证明的命题就越弱；自动化越弱的需要的专业知识就越多。你对这个方向感兴趣的话可以先从比方说Dafny入手，感受一下。这个方向基本跟CS一样老。





https://dafny-lang.github.io/dafny/ 文档

github
 https://github.com/dafny-lang/dafny




https://rise4fun.com/Dafny/tutorial/Guide
官方教程

Bug 为什么不能彻底消除？ - 圆角骑士魔理沙的回答 - 知乎
https://www.zhihu.com/question/38378942/answer/84744046

online 

https://rise4fun.com/dafny



实际工作中怎么验证程序写对了？ - Mike He的回答 - 知乎
https://www.zhihu.com/question/20275593/answer/1070445082

  
科普 - 程序验证（5）- 验证案例 - FRONTIERS的文章 - 知乎
https://zhuanlan.zhihu.com/p/312501103

file - 读取(写入)Dafny中的文件 https://www.coder.work/article/6656593


# 1. Dafny



Dafny的一个重要定位是High-level的、program verification的intermediate language(IL)。比如在实现C/Java/JavaScript等语言等program verifier时，可以比较方便、直接地把VC(verification condition)  生成为Dafny，而不用关心Dafny具体使用的验证算法。 MSR出的类似语言还有F*, Boogie等，Boogie更low-level一点，实际上Dafny正是建立在Boogie之上。前面同学也提到了Z3 SMT Solver, 它又是Boogie的主要引擎，所以类比编译流程，大概有这个关系Dafny -> Boogie -> Z3.  说是"主要引擎“，是因为在Boogie之上可以实现其它验证算法如abstract interpretation，并不依赖于SMT solver.题外话，“程序验证“是很广的话题，不止“Coq、Idris”，各人做的维度、风格不尽相同。 祝有兴趣的同学基于Dafny玩出verification相关的有趣应用～

作者：rainoftime
链接：https://www.zhihu.com/question/59465221/answer/248361757


Dafny是一种命令式编译语言，它针对C＃，并通过前置条件，后置条件，循环不变式和循环变体支持形式规范。该语言主要结合了功能和命令式范式的思想，并且对面向对象的编程提供了有限的支持。功能包括通用类，动态分配，归纳数据类型以及称为隐式动态框架的分离逻辑的变体[1]关于副作用的推理。[2] Dafny由Microsoft Research的Rustan Leino创建，此前他从事开发ESC / Modula-3， ESC / Java和Spec＃的工作。Dafny被广泛用于教学中，并定期在软件验证竞赛中使用（例如VSTTE'08， [3] VSCOMP'10， [4] COST'11， [5]和VerifyThis'12 [6]）。

Dafny旨在提供对形式规范和验证的简单介绍，并已在教学中广泛使用。Dafny建立在Boogie中间语言的基础上，该中间语言使用Z3自动定理证明器来履行证明义务。[7] [8]

> Dafny==>Boogie==>SMT solver Z3==>sat

如何评价微软研究院的 Dafny 语言？ - 知乎
https://www.zhihu.com/question/59465221/answer/247746999

从程序语言的角度来看，Dafny的设计还是比较Modern，比较优秀的。它结合了OOP和FP，ADT是Haskell的写法，比Scala更简便。有命令式的method也有函数式的function，总之就是怎么爽怎么写，还可以编译到C#。MS家的PL组合拳C#+F#+Dafny简直可以让你上天。但是，它的缺点也有不少，比如ADT不能深层匹配，只能一层一层地匹配（可能是为了Verify更方便）；对OOP的支持不如Scala好；库和语言不分（可能也是为Verify方便Orz）；以及，最致命的伤，没有标准库。编译器有很多Bug我就不说了，不属于评价编译语言好坏的范畴。。。

从程序验证的角度来看，Dafny应该算中等偏上。我目前玩过Boogie，Z3，Dafny和Scala家的stainless(以前叫leon)，有的问题在这个语言好证，有的问题那个语言好证。不过Dafny有一点很强，它可以验证Dirty的代码，这一点Scala选手表示已经跪了。但是，Scala的stainless在验证不通过时可以构造反例，leon(目前正在逐步迁移到stainless)还可以给出正确的代码实现，这确实是很吸引人的地方。不过stainless启动太慢了（这个赖scala╮(╯▽╰)╭

还有，Dafny的IDE支持比stainless好，stainless居然想让我们用eclipse写代码，天呐，没有idea怎么活！以及，dafny有language server，可以一边写代码一边看验证结果，stainless那边开了个sbt插件的branch都开了几年了，还没有推出正式的sbt插件，我都看不下去了，自己撸了一个从外部调用stainless的插件，牺牲了一(hen)点(duo)速度。

另外，程序验证真的是玄学，你根本不知道要给Verifier写些什么hint，它才能证明出结论。这一点上述verifier一个都没跑。


https://github.com/dafny-lang/dafny







































































 

```cmd
Usage: Dafny [ option ... ] [ filename ... ]

  ---- General options -------------------------------------------------------

  /version      print the Dafny version number
  /help         print this message
  /attrHelp     print a message about supported declaration attributes
  /env:<n>      print command line arguments
                  0 - never, 1 (default) - during BPL print and prover log,
                  2 - like 1 and also to standard output
  /printVerifiedProceduresCount:<n>
                0 - no
                1 (default) - yes
  /wait         await Enter from keyboard before terminating program
  /xml:<file>   also produce output in XML format to <file>

  ---- Boogie options --------------------------------------------------------

  Multiple .bpl files supplied on the command line are concatenated into one
  Boogie program.

  /lib           : Include library definitions
  /proc:<p>      : Only check procedures matched by pattern <p>. This option
                   may be specified multiple times to match multiple patterns.
                   The pattern <p> matches the whole procedure name and may
                   contain * wildcards which match any character zero or more
                   times.
  /noProc:<p>    : Do not check procedures matched by pattern <p>. Exclusions
                   with /noProc are applied after inclusions with /proc.
  /noResolve     : parse only
  /noTypecheck   : parse and resolve only

  /print:<file>  : print Boogie program after parsing it
                   (use - as <file> to print to console)
  /pretty:<n>
                0 - print each Boogie statement on one line (faster).
                1 (default) - pretty-print with some line breaks.
  /printWithUniqueIds : print augmented information that uniquely
                   identifies variables
  /printUnstructured : with /print option, desugars all structured statements
  /printDesugared : with /print option, desugars calls
  /printLambdaLifting : with /print option, desugars lambda lifting

  /freeVarLambdaLifting : Boogie's lambda lifting transforms the bodies of lambda
                         expressions into templates with holes. By default, holes
                         are maximally large subexpressions that do not contain
                         bound variables. This option performs a form of lambda
                         lifting in which holes are the lambda's free variables.

  /overlookTypeErrors : skip any implementation with resolution or type
                        checking errors

  /loopUnroll:<n>
                unroll loops, following up to n back edges (and then some)
  /soundLoopUnrolling
                sound loop unrolling
  /printModel:<n>
                0 (default) - do not print Z3's error model
                1 - print Z3's error model
  /printModelToFile:<file>
                print model to <file> instead of console
  /mv:<file>    Specify file to save the model with captured states 
                (see documentation for :captureState attribute)
  /enhancedErrorMessages:<n>
                0 (default) - no enhanced error messages
                1 - Z3 error model enhanced error messages

  /printCFG:<prefix> : print control flow graph of each implementation in
                       Graphviz format to files named:
                         <prefix>.<procedure name>.dot

  /useBaseNameForFileName : When parsing use basename of file for tokens instead
                            of the path supplied on the command line

  ---- Inference options -----------------------------------------------------

  /infer:<flags>
                use abstract interpretation to infer invariants
                <flags> must specify exactly one of the following domains:
                   t = trivial bottom/top lattice
                   j = stronger intervals
                together with any of the following options:
                   s = debug statistics
                0..9 = number of iterations before applying a widen (default=0)
  /checkInfer   instrument inferred invariants as asserts to be checked by
                theorem prover
  /contractInfer
                perform procedure contract inference
  /instrumentInfer
                h - instrument inferred invariants only at beginning of
                    loop headers (default)
                e - instrument inferred invariants at beginning and end
                    of every block (this mode is intended for use in
                    debugging of abstract domains)
  /printInstrumented
                print Boogie program after it has been instrumented with
                invariants

  ---- Debugging and general tracing options ---------------------------------

  /trace        blurt out various debug trace information
  /traceTimes   output timing information at certain points in the pipeline
  /tracePOs     output information about the number of proof obligations
                (also included in the /trace output)
  /break        launch and break into debugger

  ---- Civl options ----------------------------------------------------------

  /trustMoverTypes
                do not verify mover type annotations on atomic action declarations
  /trustNoninterference
                do not perform noninterference checks
  /trustLayersUpto:<n>
                do not verify layers <n> and below
  /trustLayersDownto:<n>
                do not verify layers <n> and above
  /civlDesugaredFile:<file>
                print plain Boogie program to <file>

  ---- Verification-condition generation options -----------------------------

  /liveVariableAnalysis:<c>
                0 = do not perform live variable analysis
                1 = perform live variable analysis (default)
                2 = perform interprocedural live variable analysis
  /noVerify     skip VC generation and invocation of the theorem prover
  /verifySnapshots:<n>
                verify several program snapshots (named <filename>.v0.bpl
                to <filename>.vN.bpl) using verification result caching:
                0 - do not use any verification result caching (default)
                1 - use the basic verification result caching
                2 - use the more advanced verification result caching
                3 - use the more advanced caching and report errors according
                    to the new source locations for errors and their
                    related locations (but not /errorTrace and CaptureState
                    locations)
  /traceCaching:<n>
                0 (default) - none
                1 - for testing
                2 - for benchmarking
                3 - for testing, benchmarking, and debugging
  /verifySeparately
                verify each input program separately
  /removeEmptyBlocks:<c>
                0 - do not remove empty blocks during VC generation
                1 - remove empty blocks (default)
  /coalesceBlocks:<c>
                0 = do not coalesce blocks
                1 = coalesce blocks (default)
  /traceverify  print debug output during verification condition generation
  /subsumption:<c>
                apply subsumption to asserted conditions:
                0 - never, 1 - not for quantifiers, 2 (default) - always
  /alwaysAssumeFreeLoopInvariants
                usually, a free loop invariant (or assume
                statement in that position) is ignored in checking contexts
                (like other free things); this option includes these free
                loop invariants as assumes in both contexts
  /inline:<i>   use inlining strategy <i> for procedures with the :inline
                attribute, see /attrHelp for details:
                  none
                  assume (default)
                  assert
                  spec
  /printInlined
                print the implementation after inlining calls to
                procedures with the :inline attribute (works with /inline)
  /recursionBound:<n>
                Set the recursion bound for stratified inlining to
                be n (default 500)
  /smoke        Soundness Smoke Test: try to stick assert false; in some
                places in the BPL and see if we can still prove it
  /smokeTimeout:<n>
                Timeout, in seconds, for a single theorem prover
                invocation during smoke test, defaults to 10.
  /causalImplies
                Translate Boogie's A ==> B into prover's A ==> A && B.
  /typeEncoding:<m>
                Encoding of types when generating VC of a polymorphic program:
                   p = predicates (default)
                   a = arguments
                Boogie automatically detects monomorphic programs and enables
                monomorphic VC generation, thereby overriding the above option.
  /monomorphize
                Try to monomorphize program. An error is reported if
                monomorphization is not possible. This feature is experimental!
  /useArrayTheory
                Use the SMT theory of arrays (as opposed to axioms). Supported
                only for monomorphic programs.
  /reflectAdd   In the VC, generate an auxiliary symbol, elsewhere defined
                to be +, instead of +.

  ---- Verification-condition splitting --------------------------------------

  /vcsMaxCost:<f>
                VC will not be split unless the cost of a VC exceeds this
                number, defaults to 2000.0. This does NOT apply in the
                keep-going mode after first round of splitting.
  /vcsMaxSplits:<n>
                Maximal number of VC generated per method. In keep
                going mode only applies to the first round.
                Defaults to 1.
  /vcsMaxKeepGoingSplits:<n>
                If set to more than 1, activates the keep
                going mode, where after the first round of splitting,
                VCs that timed out are split into <n> pieces and retried
                until we succeed proving them, or there is only one
                assertion on a single path and it timeouts (in which
                case error is reported for that assertion).
                Defaults to 1.
  /vcsKeepGoingTimeout:<n>
                Timeout in seconds for a single theorem prover
                invocation in keep going mode, except for the final
                single-assertion case. Defaults to 1s.
  /vcsFinalAssertTimeout:<n>
                Timeout in seconds for the single last
                assertion in the keep going mode. Defaults to 30s.
  /vcsPathJoinMult:<f>
                If more than one path join at a block, by how much
                multiply the number of paths in that block, to accomodate
                for the fact that the prover will learn something on one
                paths, before proceeding to another. Defaults to 0.8.
  /vcsPathCostMult:<f1>
  /vcsAssumeMult:<f2>
                The cost of a block is
                    (<assert-cost> + <f2>*<assume-cost>) *
                    (1.0 + <f1>*<entering-paths>)
                <f1> defaults to 1.0, <f2> defaults to 0.01.
                The cost of a single assertion or assumption is
                currently always 1.0.
  /vcsPathSplitMult:<f>
                If the best path split of a VC of cost A is into
                VCs of cost B and C, then the split is applied if
                A >= <f>*(B+C), otherwise assertion splitting will be
                applied. Defaults to 0.5 (always do path splitting if
                possible), set to more to do less path splitting
                and more assertion splitting.
  /vcsDumpSplits
                For split #n dump split.n.dot and split.n.bpl.
                Warning: Affects error reporting.
  /vcsCores:<n>
                Try to verify <n> VCs at once. Defaults to 1.
  /vcsLoad:<f>  Sets vcsCores to the machine's ProcessorCount * f,
                rounded to the nearest integer (where 0.0 <= f <= 3.0),
                but never to less than 1.

  ---- Prover options --------------------------------------------------------

  /errorLimit:<num>
                Limit the number of errors produced for each procedure
                (default is 5, some provers may support only 1)
  /timeLimit:<num>
                Limit the number of seconds spent trying to verify
                each procedure
  /rlimit:<num>
                Limit the Z3 resource spent trying to verify each procedure
  /errorTrace:<n>
                0 - no Trace labels in the error output,
                1 (default) - include useful Trace labels in error output,
                2 - include all Trace labels in the error output
  /vcBrackets:<b>
                bracket odd-charactered identifier names with |'s.  <b> is:
                   0 - no (default),
                   1 - yes
  /proverDll:<tp>
                use theorem prover <tp>, where <tp> is either the name of
                a DLL containing the prover interface located in the
                Boogie directory, or a full path to a DLL containing such
                an interface. The default interface shipped is:
                    SMTLib (uses the SMTLib2 format and calls an SMT solver)
  /proverOpt:KEY[=VALUE]
                Provide a prover-specific option (short form /p).
  /proverHelp   Print prover-specific options supported by /proverOpt.
  /proverLog:<file>
                Log input for the theorem prover.  Like filenames
                supplied as arguments to other options, <file> can use the
                following macros:
                    @TIME@    expands to the current time
                    @PREFIX@  expands to the concatenation of strings given
                              by /logPrefix options
                    @FILE@    expands to the last filename specified on the
                              command line
                In addition, /proverLog can also use the macro '@PROC@',
                which causes there to be one prover log file per
                verification condition, and the macro then expands to the
                name of the procedure that the verification condition is for.
  /logPrefix:<str>
                Defines the expansion of the macro '@PREFIX@', which can
                be used in various filenames specified by other options.
  /proverLogAppend
                Append (not overwrite) the specified prover log file
  /proverWarnings
                0 (default) - don't print, 1 - print to stdout,
                2 - print to stderr
  /restartProver
                Restart the prover after each query

  ---- Dafny options ---------------------------------------------------------

 All the .dfy files supplied on the command line along with files recursively
 included by 'include' directives are considered a single Dafny program;
 however only those files listed on the command line are verified.

 Exit code: 0 -- success; 1 -- invalid command-line; 2 -- parse or type errors;
            3 -- compilation errors; 4 -- verification errors

/dprelude:<file>
    choose Dafny prelude file
/dprint:<file>
    print Dafny program after parsing it
    (use - as <file> to print to console)
/printMode:<Everything|DllEmbed|NoIncludes|NoGhost>
    Everything is the default.
    DllEmbed prints the source that will be included in a compiled dll.
    NoIncludes disables printing of {:verify false} methods incorporated via the
    include mechanism, as well as datatypes and fields included from other files.
    NoGhost disables printing of functions, ghost methods, and proof statements in
    implementation methods.  It also disables anything NoIncludes disables.
/rprint:<file>
    print Dafny program after resolving it
    (use - as <file> to print to console)
/pmtrace      print pattern-match compiler debug info
/titrace      print type-inference debug info
/view:<view1, view2>
    print the filtered views of a module after it is resolved (/rprint).
    If print before the module is resolved (/dprint), then everything in the module
    is printed.
    If no view is specified, then everything in the module is printed.

/dafnyVerify:<n>
    0 - stop after typechecking
    1 - continue on to translation, verification, and compilation
/compile:<n>  0 - do not compile Dafny program
    1 (default) - upon successful verification of the Dafny
        program, compile it to the designated target language
        (/noVerify automatically counts as failed verification)
    2 - always attempt to compile Dafny program to the target
        language, regardless of verification outcome
    3 - if there is a Main method and there are no verification
        errors and /noVerify is not used, compiles program in
        memory (i.e., does not write an output file) and runs it
    4 - like (3), but attempts to compile and run regardless of
        verification outcome
/compileTarget:<lang>
    cs (default) - Compilation to .NET via C#
    go - Compilation to Go
    js - Compilation to JavaScript
    java - Compilation to Java
    cpp - Compilation to C++
    php - Compilation to PHP

    Note that the C++ backend has various limitations (see Docs/Compilation/Cpp.md).
    This includes lack of support for BigIntegers (aka int), most higher order
    functions, and advanced features like traits or co-inductive types.
/Main:<name>
    The (fully-qualified) name of the method to use as the executable entry point.
    Default is the method with the {:main} atrribute, or else the method named 'Main'.
/compileVerbose:<n>
    0 - don't print status of compilation to the console
    1 (default) - print information such as files being written by
        the compiler to the console
/spillTargetCode:<n>
    This option concerns the textual representation of the target program.
    This representation is of no interest when working with only Dafny code,
    but may be of interest in cross-language situations.
    0 (default) - Don't make any extra effort to write the textual target program
        (but still compile it, if /compile indicates to do so).
    1 - Write the textual target program, if it is being compiled.
    2 - Write the textual target program, provided it passes the verifier (and
        /noVerify is NOT used), regardless of /compile setting.
    3 - Write the textual target program, regardless of verification outcome
        and /compile setting.
    Note, some compiler targets may (always or in some situations) write out the
    textual target program as part of compilation, in which case /spillTargetCode:0
    behaves the same way as /spillTargetCode:1.
/out:<file>
    filename and location for the generated target language files
/coverage:<file>
    The compiler emits branch-coverage calls and outputs into
    <file> a legend that gives a description of each
    source-location identifier used in the branch-coverage calls.
    (use - as <file> to print to console)
/noCheating:<n>
    0 (default) - allow assume statements and free invariants
    1 - treat all assumptions as asserts, and drop free.
/induction:<n>
    0 - never do induction, not even when attributes request it
    1 - only apply induction when attributes request it
    2 - apply induction as requested (by attributes) and also
        for heuristically chosen quantifiers
    3 - apply induction as requested, and for
        heuristically chosen quantifiers and lemmas
    4 (default) - apply induction as requested, and for lemmas
/inductionHeuristic:<n>
    0 - least discriminating induction heuristic (that is, lean
        toward applying induction more often)
    1,2,3,4,5 - levels in between, ordered as follows as far as
        how discriminating they are:  0 < 1 < 2 < (3,4) < 5 < 6
    6 (default) - most discriminating
/noIncludes   Ignore include directives
/noExterns    Ignore extern and dllimport attributes
/noNLarith    Reduce Z3's knowledge of non-linear arithmetic (*,/,%).
    Results in more manual work, but also produces more predictable behavior.
    (This switch will perhaps be replaced by /arith in the future.
    For now, it takes precedence of /arith.)
/arith:<n>    (Experimental switch. Its options may change.)
    0 - Use Boogie/Z3 built-ins for all arithmetic operations.
    1 (default) - Like 0, but introduce symbolic synonyms for *,/,%, and
        allow these operators to be used in triggers.
    2 - Like 1, but introduce symbolic synonyms also for +,-.
    3 - Turn off non-linear arithmetic in the SMT solver. Still,
        use Boogie/Z3 built-in symbols for all arithmetic operations.
    4 - Like 3, but introduce symbolic synonyms for *,/,%, and allow these
        operators to be used in triggers.
    5 - Like 4, but introduce symbolic synonyms also for +,-.
    6 - Like 5, and introduce axioms that distribute + over *.
    7 - like 6, and introduce facts that associate literals arguments of *.
    8 - Like 7, and introduce axiom for the connection between *,/,%.
    9 - Like 8, and introduce axioms for sign of multiplication
    10 - Like 9, and introduce axioms for commutativity and
        associativity of *
/autoReqPrint:<file>
    Print out requirements that were automatically generated by autoReq.
/noAutoReq    Ignore autoReq attributes
/allowGlobals Allow the implicit class '_default' to contain fields, instance functions,
    and instance methods.  These class members are declared at the module scope,
    outside of explicit classes.  This command-line option is provided to simplify
    a transition from the behavior in the language prior to version 1.9.3, from
    which point onward all functions and methods declared at the module scope are
    implicitly static and fields declarations are not allowed at the module scope.
/countVerificationErrors:<n>
    [ deprecated ]
    0 - Set exit code to 0 regardless of the presence of any other errors.
    1 (default) - Emit usual exit code (cf. beginning of the help message).
/autoTriggers:<n>
    0 - Do not generate {:trigger} annotations for user-level quantifiers.
    1 (default) - Add a {:trigger} to each user-level quantifier. Existing
                  annotations are preserved.
/rewriteFocalPredicates:<n>
    0 - Don't rewrite predicates in the body of prefix lemmas.
    1 (default) - In the body of prefix lemmas, rewrite any use of a focal predicate
                  P to P#[_k-1].
/optimize     Produce optimized C# code, meaning:
      - passes /optimize flag to csc.exe.
/optimizeResolution:<n>
    0 - Resolve and translate all methods
    1 - Translate methods only in the call graph of current verification target
    2 (default) - As in 1, but only resolve method bodies in non-included Dafny sources
/stats        Print interesting statistics about the Dafny files supplied.
/funcCallGraph Print out the function call graph.  Format is: func,mod=callee*
/warnShadowing  Emits a warning if the name of a declared variable caused another variable
    to be shadowed
/definiteAssignment:<n>
    0 - ignores definite-assignment rules; this mode is for testing only--it is
        not sound
    1 (default) - enforces definite-assignment rules for variables and fields
        of types that do not support auto-initialization
    2 - enforces definite-assignment for all non-yield-parameter
        variables and fields, regardless of their types
    3 - like 2, but also performs checks in the compiler that no nondeterministic
        statements are used; thus, a program that passes at this level 3 is one
        that the language guarantees that values seen during execution will be
        the same in every run of the program
/deprecation:<n>
    0 - don't give any warnings about deprecated features
    1 (default) - show warnings about deprecated features
    2 - also point out where there's new simpler syntax
/verifyAllModules
    Verify modules that come from an include directive
/separateModuleOutput
    Output verification results for each module separately, rather than
    aggregating them after they are all finished.
/useRuntimeLib
    Refer to pre-built DafnyRuntime.dll in compiled assembly rather
    than including DafnyRuntime.cs verbatim.
/allocated:<n>
    Specify defaults for where Dafny should assert and assume
    allocated(x) for various parameters x, local variables x,
    bound variables x, etc.  Lower <n> may require more manual
    allocated(x) annotations and thus may be more difficult to use.
    Warning: this option should be chosen consistently across
    an entire project; it would be unsound to use different
    defaults for different files or modules within a project.
    And even so, modes /allocated:0 and /allocated:1 let functions
    depend on the allocation state, which is not sound in general.
    0 - Nowhere (never assume/assert allocated(x) by default).
    1 - Assume allocated(x) only for non-ghost variables and fields
        (these assumptions are free, since non-ghost variables
        always contain allocated values at run-time).  This option
        may speed up verification relative to /allocated:2.
    2 - Assert/assume allocated(x) on all variables,
        even bound variables in quantifiers.  This option is
        the easiest to use for heapful code.
    3 - (default) Frugal use of heap parameters.
    4 - mode 3 but with alloc antecedents when ranges don't imply
        allocatedness.
/printTooltips
    Dump additional positional information (displayed as mouse-over tooltips by
    the VS plugin) to stdout as 'Info' messages.
/printIncludes:<None|Immediate|Transitive>
    None is the default.
    Immediate prints files included by files listed on the command line
    Transitive recurses on the files printed by Immediate
    Immediate and Transitive will exit after printing.
/disableScopes
    Treat all export sets as 'export reveal *'. i.e. don't hide function bodies
    or type definitions during translation.
/stdin
    Read standard input and treat it as an input .dfy file.

Dafny generally accepts Boogie options and passes these on to Boogie. However,
some Boogie options, like /loopUnroll, may not be sound for Dafny or may not
have the same meaning for a Dafny program as it would for a similar Boogie
program.

```




