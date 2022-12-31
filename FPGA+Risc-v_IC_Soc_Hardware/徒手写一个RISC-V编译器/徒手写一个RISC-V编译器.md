# env
https://gist.github.com/sunshaoce/90216c19591581f8997df0109b65c154 这个是RISC-V环境的构建脚本，需要先下载有相应的代码仓库。
脚本运行命令：./riscv.sh ALLv


一个除了代码以外的课程仓库，提问也欢迎用这个仓库的issues

https://github.com/sunshaoce/rvcc-course


docker构建方式（等1小时，bugfix中）

https://github.com/ksco/rvcc-env-docker
 

打包了RISC-V实验环境用到的各种可执行文件，包括riscv-gnu-toolchain、spike和pk、qemu、llvm等程序。

https://mirror.iscas.ac.cn/plct/rvcc-course-sysroot-20220721.tar.bz2


【RISC-V 编译及QEMU、Spike模拟器配置 [永恒天平]  - 孙少策 - 20200813 - PLCT实验室-哔哩哔哩】 https://b23.tv/IwLPq2N















 

# 徒手写一个RISC-V编译器
课程简介：

本课程基于 chibicc，将其由原来的X86架构改写为 RISC-V 架构，同时加入了大量的中文注释，并且配有316节对应于每一个 commit 的课程，帮助读者可以层层推进、逐步深入的学习编译器的构造。

RISC-V 是一个开源的精简指令集，相较于常见的 X86、ARM 架构，其简单易学，并且发展迅猛。现在已经出现了支持 RISC-V 的各类设备，未来还将出现RISC-V架构的笔记本电脑，可谓是前景一片光明。

chibicc（https://github.com/rui314/chibicc）是 Rui 大师开发的一个X86架构的迷你编译器。Rui 同时也是 8cc、9cc、mold、lld 等著名项目的主要开发者，chibicc 是他最新的编译器项目。chibicc 项目以 commit 为阶段，借助于316个 commits 实现了一个能够编译 Git 等开源项目的C编译器。

课程资源

课程对应的代码仓库将会上传到：https://github.com/sunshaoce/rvcc

课程对应的视频将会在B站lazyparser账号更新，请留意后续公众号推送。

我适合学习么？

学习 chibicc 不要求事先掌握编译原理知识（边做边学），但是需要一定的C编程能力。需要有一个 Linux 实验环境，同时安装了 RISC-V 模拟器等工具。

RISC-V 实验环境配置可以参考下面的视频：

https://www.bilibili.com/video/BV1D54y1m78G

我想加入学习小组！

目前还没有开始，预期本周末开始。请留意后续的课程内容推送，视频和代码仓库中都将会提供进入学习群的方法。

徒手写一个RISC-V编译器 - 第000课

https://www.bilibili.com/video/BV1gY4y1E7Ue

徒手写一个RISC-V编译器 - 第001课




https://www.bilibili.com/video/BV1ga411u7X9


----------------------------------------------------------------------------


# Notes



Risc -v 常用指令集 GC:

- I 整形基础指令集
- M乘除指令集
- A原子指令集 
- F单精度浮点
- D双精度浮点
- C精简指令集











# chibicc
一文讲透 Git 底层数据结构和原理 - 阿里开发者的文章 - 知乎
https://zhuanlan.zhihu.com/p/142289703

一、git checkout 用法总结

1.切换与创建分支
git checkout <branch_name > 切换分支
#git switch <branch_name> 切换分支

git checkout -b <branch_name> 创建并切换至分支
#git switch -c <branch_name> 创建并切换至分支

git checkout -b <branch_name>origin/<branch_name> 在本地创建和远程分支对应的分支，本地和远程分支的名称最好一致

2.还原工作区（文件内容）
git checkout – <file_name> 丢弃工作区的修改，并用最近一次的commit内容还原到当前工作区（对文件中内容的操作，无法对添加文件、删除文件起作用）

git checkout HEAD^ – <file_name> 将指定commit提交的内容(HEAD^表示上一个版本)还原到当前工作区

git checkout <branch_name> – <file_name> 将指定分支的指定提交内容还原到当前分支工作区

二、git restore 用法总结
git restore --staged <file_name> 将暂存区的修改重新放回工作区（包括对文件自身的操作，如添加文件、删除文件）

git restore <file_name> 丢弃工作区的修改（不包括对文件自身的操作，如添加文件、删除文件）

三、git reset 用法总结
git reset HEAD <file_name> 丢弃暂存区的修改，重新放回工作区，会将暂存区的内容和本地已提交的内容全部恢复到未暂存的状态，不影响原来本地文件(相当于撤销git add 操作，不影响上一次commit后对本地文件的修改) （包括对文件的操作，如添加文件、删除文件）

git reset –hard HEAD 清空暂存区，将已提交的内容的版本恢复到本地，本地的文件也将被恢复的版本替换（恢复到上一次commit后的状态，上一次commit后的修改也丢弃）


- 转到特定的提交版本并编译，企图修改make查看源码的改进步骤
 一次搞清 git checkout，git restore 和 git reset
reset和revert都可以用来回滚代码。但他们是有区别的，准确来说，reset是用来"回退"版本，而revert是用来"还原"某次或者某几次提交。

使用reset命令，Git会把要回退版本之后提交的修改都删除掉。要从第四次修改回退到第一次修改，那么会删除第二、三、四次的修改。
>【注：这里并不是真正的物理删除】上面提的并不是真正的物理删除，是因为Git会把分支的每次修改记录都会保留下来，比如有某次的commit,某次的reset等。而使用`git reflog show`命令,可以查看完整的提交历史，只要有commit_id，我们就能恢复任意版本的代码，在各版本之间来回穿梭。

`git reset --hard 97ea0f9`

 
如果发现第三次修改有错误，想要恢复第三次修改，却要保留第四次修改呢？

这个时候就可以用revert命令：

`git revert -n 97ea0f9`
`git commit -m "恢复第三次修改"`


314次commit都是精心设计的，分别代表不同的任务进度
- git 到特定的历史的情况下，快捷跳到下一个历史

回退上个版本：git reset --hard HEAD^ 
【注： 
HEAD表示当前最新版本
HEAD^表示当前最新版本的前一个版本
HEAD^^表示当前最新版本的前两个版本，以此类推
HEAD~1表示当前最新版本的前一个版本
HEAD~8表示当前最新版本的前8个版本，以此类推
git reset --hard 版本号】

查看特定某次比如d56dd2f的提交内容
`$ git show d56dd2f`

查看当前分支id `git rev-parse HEAD`

查看所有提交版本历史
```bash
$ git log --graph --oneline
* 90d1f7f (HEAD -> main, origin/main, origin/HEAD) Make struct member access to work with `=` and `?:`
* 982041f Update README
* b35d148 Add __attribute__((aligned(N)) for struct declaration
* 44bea4c Add __attribute__((packed))
* 395308c redefinition
* 2ed3fda Add test/thirdparty/cpython.sh
* 0a5d08c Complete stdatomic.h
* d69a11d Add _Atomic and atomic ++, -- and op= operators
* 80ea9d4 Add atomic_exchange
* ca27455 Add atomic_compare_exchange
* fb49370 Add scripts to test third-party apps
* 469f159 Add -Xlinker option
* d1bc9a4 Add -Wl, option
* c8df787 Add -L option
* 4e5de36 Add -shared option
* 1e9b6dd Add -static option
* f10bceb [GNU] Add #include_next
* a6c6622 [GNU] Add "#pragma once"
* d48d9e5 Add include guard optimization
* c0f0614 Cache file search results
* 86785fc Add -fpic and -fPIC options
* c3edffb Add -MMD option
* 7aa72e4 Add -MQ option
* fb5cfe5 Add -MD option
* db850f3 Add -MT option
* 57c1d4e Add -MP option
* 95d5a46 Add -MF option
* d0c4667 Add -M option
* f694413 Use hashmap for keyword lookup
* 655954e Use hashmap for block-scope lookup
* 30520e5 Use hashmap for macro name lookup
* 0aad326 Add string hashmap
* f0c98e0 [GNU] Treat labels-as-values as compile-time constant
* 4f165ec [GNU] Support labels-as-values
* 3d5550e [GNU] Support array range designator
* d90c73b [GNU] Support case ranges
* e0bf168 Add long double
* d56dd2f Recognize .a and .so files
* 8d130ab Emit size and type for symbols
* c32f0e2 Add -s option
* bc25279 Add -l option
* b0109a3 Do not define __STDC_NO_VLA__
* 2fa8f48 Support sizeof(typename) where typename is a VLA
* 07f9010 Add pointer arithmetic for VLA
* e8667af Add sizeof() for VLA
* 77275c5 Add alloca()
* 4064871 Make -E to imply -xc
* ee0a951 Add -x option
* 8f5ff07 Add -include option
* b377284 Add thread-local variable
* 6d344ed Add -fcommon and -fno-common flags
* 85e46b1 Add tentative definition
* 1b99bad Add offsetof
* 11fc259 Add -idirafter option
* 6a2dc5a Use __attribute__((format(print, ...))) to find programming errors
* e5f4ca9 Do not emit static inline functions if referenced by no one
* 31087f8 Handle inline functions as static functions
* a253516 Add basic "asm" statement
* e28a612 [GNU] Add ?: operator with omitted operand
* aee7891 [GNU] Allow sizeof(<function type>)
* 1faab48 Add _Generic
* 1433b40 [GNU] Add __builtin_types_compatible_p
* 7d80a51 Add typeof
* 007e526 [GNU] Support GCC-style variadic macro
* 74ec9f6 Ignore #pragma
* 083c275 [GNU] Handle ,##__VA_ARG__
* 3381448 Add __VA_OPT__
* 3a10c8a [GNU] Add __BASE_FILE__ macro
* 922604a [GNU] Add __TIMESTAMP__ macro
* aaf20fb [GNU] Add line marker directive
* c61c0d0 Add #line
* 37998be Improve error message for multibyte characters
* 95eb5b0 Handle struct designator for anonymous struct member
* 31dc1df Add union designated initializer
* 67f5834 Add struct designated initializer
* 691c4fa [GNU] Allow to omit "=" in designated initializers
* 835cd24 Allow array designators to initialize incomplete arrays
* c618c3b Add array designated initializer
* 2b2fa25 Skip UTF-8 BOM markers
* 2382777 Allow to concatenate regular string literals with L/u/U string literals
* adb8b98 [GNU] Accept $ as an identifier character
* 0e5d250 Allow multibyte UTF-8 character in identifier
* e4491b8 Define __STDC_UTF_{16,32}__ macros
* 6adba75 Add UTF-32 string literal initializer
* 36230e0 Add UTF-16 string literal initializer
* cae061a Add wide string literal
* c467ee6 Add UTF-32 string literal
* 9cabe1f Add UTF-16 string literal
* 57b21fe Add UTF-8 string literal
* 2dac3af Add UTF-32 character literal
* 454618c Add UTF-16 character literal
* a57c661 Accept multibyte character as wide character literal
* c31886a Add \u and \U escape sequences
* 74bcec5 Canonicalize newline character
* 0e77f3d [GNU] Add __COUNTER__ macro
* e27417f Add __DATE__ and __TIME__ macros
* c3075b3 Add anonymous struct and union
* 9c36dd7 Make "main" to implicitly return 0
* 5257ee0 Make an array of at least 16 bytes long to have alignment of at least 16 bytes
* 2c91da5 Turn on -Wall compiler flag and fix compiler warnings
* b1fdddf Ignore -O, -W and -g and other flags
* 2bdc6b8 Write to an in-memory buffer before writing to an actual output file
* c302a96 Do not allow to obtain an address of a bitfield
* 17ea802 Handle zero-width bitfield member
* 54c2b3b Handle op=-style assignments to bitfields
* 441a89b Support global struct bitfield initializer
* cc852fe Add bitfield
* be8b6f6 Add -U option
* fc69f5c Add -D option
* 3f2c2d5 Tokenize numeric tokens as pp-numbers
* e0b5da3 Dereferencing a function shouldn't do anything
* 603de50 Add va_copy()
* b6d3cd0 Allow variadic function to take more than 6 parameters
* d7bad96 Allow to define a function returning a struct
* c72df1c Allow to call a fucntion returning a struct
* d63b1f4 Allow struct argument
* 5e0f8c4 Allow struct parameter
* 9021f7f Support passed-on-stack parameters
* b29f052 Support passed-on-stack arguments
* 12a9e75 Self-host: including preprocessor, chibicc can compile itself
* 5322ea8 Add va_arg()
* 7cbfd11 Add stdarg.h, stdbool.h, stddef.h, stdalign.h and float.h
* 7746e4e Recognize wide character literal
* ab4f1e1 Concatenate adjacent string literals
* 82ba010 [GNU] Add __FUNCTION__
* ba6b4b6 Add __func__
* dc01f94 Add __VA_ARGS__
* 6f17071 Add __FILE__ and __LINE__
* 5f5a850 Add predefine macros such as __STDC__
* e7fdc2e Add #error
* a939a7a Add default include paths
* a1dd621 Add -I<dir> option
* d85fc4f Add #include <...>
* b33fe0e Support line continuation
* 8075582 Preserve newline and space during macro expansion
* a8d76ad Replace remaining identifiers with 0 in macro constexpr
* 5cb2f89 Add defined() macro operator
* 769b5a0 Use chibicc's preprocessor for all tests
* 8f561ae Add macro token-pasting operator (##)
* 8f6f792 Add macro stringizing operator (#)
* 1313fc6 Do not expand a token more than once for the same funclike macro
* c7d7ce0 Allow parenthesized expressions as macro arguments
* dd4306c Allow empty macro arguments
* b9ad3e4 Add multi-arity funclike #define
* dec3b3f Add zero-arity funclike #define
* 1f80f58 Add #ifdef and #ifndef
* acce002 Do not expand a token more than once for the same objlike macro
* 2651448 Expand macros in the #if and #elif argument context
* 9ad60e4 Add #undef
* 97d33ad Add objlike #define
* e7a1857 Add #elif
* c6e81d2 Add #else
* aa570f3 Skip nested #if in a skipped #if-clause
* bf6ff92 Add #if and #endif
* d138864 Add -E option
* ec149f6 Skip extra tokens after `#include "..."`
* d367510 Add #include "..."
* 146c7b3 Add the null directive
* 1e1ea39 Add a do-nothing preprocessor
* 8b726b5 Run "ld" unless -c is given
* b833cd0 Accept multiple input files
* 140b433 Run "as" command unless -S is given
* f3d9613 Split cc1 from compiler driver
* 53e8103 Add usual arithmetic conversion for function pointer
* c5953ba Decay a function to a pointer in the func param context
* d06a8ac Add function pointer
* 5d15431 Add stage2 build
* 9bf9612 Add "long double" as an alias for "double"
* ffea421 Add flonum constant expression
* e452cf7 Support variadic function with floating-point parameters
* 8b14859 Implement default argument promotion for float
* c6b3056 Allow to define a function that takes/returns flonums
* 8ec1ebf Allow to call a function that takes/returns flonums
* 0ce1093 Handle flonum for if, while, do, !, ?:, || and &&
* 83f76eb Add flonum +, -, * and /
* cf9ceec Add flonum ==, !=, < and <=
* 29de46a Add "float" and "double" local variables and casts
* 1e57f72 Add floating-point constant
* 1fad259 Allow to omit parameter name in function declaration
* 93d1277 Ignore "static" and "const" in array-dimensions
* b773554 Ignore const, volatile, auto, register, restrict or _Noreturn.
* 7ba6fe8 Handle unsigned types in the constant expression
* 6880a39 When comparing two pointers, treat them as unsigned
* 8b8f3de Use long or ulong instead of int for some expressions
* aaf1045 Add U, L and LL suffixes
* 34ab83b Add unsigned integral types
* 3f59ce7 Add `signed` keyword
* 197689a Check the number of function arguments
* 754a24f Add va_start to support variadic functions
* 58fc861 Allow to call a variadic function
* dcd4579 Handle a function returning bool, char or short
* 6a0ed71 Align stack frame to 16 byte boundaries
* ee252e6 Add do ... while
* eb85527 Add static global variables
* 30b3e21 Add return that doesn't take any value
* 127056d Add compound literals
* 319772b Add static local variables
* 310a87e [GNU] Allow a variable as an operand of _Alignof
* 9df5178 Add _Alignof and _Alignas
* 2764745 Handle extern declarations in a block
* 006a45c Add extern
* 157356c Align global variables
* 7a1f816 Accept `void` as a parameter list
* cd688a8 Allow to initialize struct flexible array member
* 824543b Add flexible array member
* 3d216e3 Emit uninitialized global data to .bss instead of .data
* fde464c Allow extraneous comma at the end of enum or initializer list
* a58958c Allow extraneous braces for scalar initializer
* efa0f33 Allow parentheses in initializers to be omitted
* 1eae5ae Handle union initializers for global variable
* eeb62b6 Add struct initializer for global variable
* bbfe3f4 Add global initializer for scalar and string
* 483b194 Handle union initializers for local variables
* aca19dd Allow to initialize a struct with other struct
* e9d2c46 Handle struct initializers for local variables
* 5b95533 Allow to omit array length if an initializer is given
* 0d71737 Add string literal initializer
* a754732 Skip excess initializer elements
* ae0a37d Initialize excess array elements with zero
* 22dd560 Support local variable initializers
* 79f5de2 Add constant expression
* 447ee09 Add ?: operator
* d0c0cb7 Add <<, >>, <<= and >>=
* 044d9ae Add switch-case
* 3c83dfd Add continue statement
* b3047f2 Add break statement
* a4be55b Resolve conflict between labels and typedefs
* 6116cae Add goto and labeled statement
* 61a1055 Add a notion of an incomplete struct type
* 7963221 Decay an array to a pointer in the func param context
* 29ed294 Add a notion of an incomplete array type
* f30f781 Add && and ||
* 8644006 Add &, |, ^, &=, |= and ^=
* daa7398 Add % and %=
* 46a96d6 Add ~ operator
* 6b88bcb Add ! operator
* 7df934d Add hexadecimal, octal and binary number literals
* e8ca48c Add post ++ and --
* 47f1937 Add pre ++ and --
* 01a94c0 Add +=, -=, *= and /=
* a4fea2b Allow for-loops to define local variables
* 736232f Support file-scope functions
* 48ba265 Add enum
* aa0accc Add character literal
* 44bba96 Add _Bool type
* fdc80bc Handle function argument type conversion
* 818352a Handle return type conversion
* 9e211cb Report an error on undefined/undeclared functions
* 8b430a6 Implement usual arithmetic conversion
* cfc4fa9 Add type cast
* cb81a37 Use 32 bit registers for char, short and int
* 67543ea Make sizeof to accept not only an expression but also a typename
* a6b82da Add typedef
* f46370e Add `long long` as an alias for `long`
* 287906a Handle complex type declarations correctly
* 8c3503b Add void type
* 74e3acc Add function declaration
* a817b23 Add nested type declarators
* 9d48eef Add short type
* 43c2f08 Add long type
* 5831eda Change size of int from 8 to 4
* bef0543 Add struct assignment
* 11e3841 Add union
* f0a018a Add -> operator
* e1e831e Support struct tags
* dfec115 Align local variables
* 9443e4b Align struct members
* f814033 Add struct
* e6307ad Add comma operator
* 1c91d19 Emit .file and .loc assembler directives
* 6647ad9 Precompute line number for each token
* cd832a3 Rewrite tests in shell script in C
* ca8b243 Handle block scope
* 6c0a429 Add line and block comments
* a0388ba Add -o and --help options
* 7b8528f Refactor -- no functionality change
* d9ea597 Read code from a file instead of argv[1]
* 9dae234 [GNU] Add statement expression
* c2cc1d3 Add \x<hexadecimal-sequence>
* 699d2b7 Add \<octal-sequence>
* ad7749f Add \a, \b, \t, \n \v, \f, \r and \e
* 35a0bcd Refactoring: Add a utility function
* 4cedda2 Add string literal
* be38d63 Add char type
* a4d3223 Add global variables
* 0b76634 Merge Function with Var
* 3e55caf Add sizeof
* 648646b Add [] operator
* 3ce1b2d Add arrays of arrays
* 8b6395d Add one dimensional arrays
* aacc0cf Support function definition up to 6 parameters
* 6cb4220 Support zero-arity function definition
* 964b1d2 Support function call with up to 6 arguments
* 30a3992 Support zero-arity function calls
* b4e82cf Add keyword "int" and make variable definition mandatory
* a6bc4ab Make pointer arithmetic work
* 863e2b8 Add unary & and *
* 3d86277 Add a representative node to each Node to improve error messages
* 5b142b1 Add LICENSE and README.md
* 1f3eb34 Add "while" statement
* f5d480f Add "for" statement
* 72b8415 Add "if" statement
* ff8912c Add null statement
* 18ac283 Add { ... }
* 6cc1c1f Add "return" statement
* 482c26b Support multi-letter local variables
* 1f9f3ad Support single-letter local variables
* 76cae0a Accept multiple statements separated by semicolons
* 725badf Split main.c into multiple small files
* 25b4b85 Add ==, !=, <= and >= operators
* bf9ab52 Add unary plus and minus
* 84cfcaf Add *, / and ()
* cc5a6d9 Improve error message
* a1ab0ff Add a tokenizer to allow space characters between tokens
* bf7081f Add + and - operators
* 0522e2d Compile an integer to an exectuable that exits with the given number


```

