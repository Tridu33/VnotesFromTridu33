>Ada, GNU awk, Bash 4, BASIC (C64 & QBasic) , C, C++, C#, ChucK, Common Lisp, Clojure (Clojure & ClojureScript) , CoffeeScript, Crystal, D, Dart, Elixir, Elm, Emacs Lisp, Erlang, ES6 (ECMAScript 2015) , F#, Factor, Fantom, Forth, Go, Groovy, GNU Guile, GNU Smalltalk, Haskell, Haxe (Neko, Python, C++, & JS) , Hy, Io, Java, JavaScript (Demo) , Julia, Kotlin, LiveScript, Logo, Lua, GNU Make, mal itself, Matlab (GNU Octave & MATLAB) , miniMAL (Repo, Demo) , NASM, Nim, Object Pascal, Objective C, OCaml, Perl, Perl 6, PHP, Picolisp, PL/pgSQL (Postgres) , PL/SQL (Oracle) , Postscript, PowerShell, Python (2.X & 3.X) , RPython, R, Racket, Rexx, Ruby, Rust, Scala, Scheme (R7RS), Skew, Swift, Swift 3, Swift 4, Tcl, TypeScript, VHDL, Vimscript, Visual Basic.NET, WebAssembly (wasm) , Yorick,

 




# mal - Make a Lisp









https://github.com/kanaka/mal


Mal 是受 Clojure 启发的 Lisp 解释器


Mal 用 87 种语言实现（93 种不同的实现方式和 115 种运行时模式）








mal 把使用任何语言写一个 mal 解释器的工作流程分解成11步，每一步中包含独立的目标、指导和测试。通过拆分任务，降低了整体难度。（如果这些还不够，mal 甚至还为每个步骤提供了伪代码，帮你"打小抄"。）

>Step 0: The REPL 为整个项目搭建一个空的骨架。
Step 1: Read and Print 实现输入和输出。
Step 2: Eval 实现求值。
Step 3: Environments 实现环境。
Step 4: If Fn Do 实现定义函数的功能和控制流。
Step 5: Tail call optimization 尾调用优化。
Step 6: Files, Mutation, and Evil 文件读取功能、变量和求值函数。
Step 7: Quoting 实现 Lisp 引用。
Step 8: Macros 实现 Lisp 宏。
Step 9: Try 实现异常处理 （try，catch，throw）
Step A: Metadata, Self-hosting and Interop 实现了解释器的自举以及一些琐碎的功能





