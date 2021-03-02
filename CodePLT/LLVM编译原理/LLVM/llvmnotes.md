

[不深不淺，帶你認識 LLVM (20191218@系統貓)](https://www.youtube.com/watch?v=RzrHuP2aVEg)


[COSCUP 2016 - LLVM 由淺入淺](https://www2.slideshare.net/zongfanyang/coscup-2016-llvm)



```
//min.c
int  min(int a,int b){
    if(a<b)
        return a;
    return b;
}
```

then:


```
>clang -cc1 -dump-tokens min.c
int 'int'        [StartOfLine]  Loc=<min.c:2:1>        
identifier 'min'         [LeadingSpace] Loc=<min.c:2:6>
l_paren '('             Loc=<min.c:2:9>
int 'int'               Loc=<min.c:2:10>
identifier 'a'   [LeadingSpace] Loc=<min.c:2:14>       
comma ','               Loc=<min.c:2:15>
int 'int'               Loc=<min.c:2:16>
identifier 'b'   [LeadingSpace] Loc=<min.c:2:20>       
r_paren ')'             Loc=<min.c:2:21>
l_brace '{'             Loc=<min.c:2:22>
if 'if'  [StartOfLine] [LeadingSpace]   Loc=<min.c:3:5>
l_paren '('             Loc=<min.c:3:7>
identifier 'a'          Loc=<min.c:3:8>
less '<'                Loc=<min.c:3:9>
identifier 'b'          Loc=<min.c:3:10>
r_paren ')'             Loc=<min.c:3:11>
return 'return'  [StartOfLine] [LeadingSpace]   Loc=<min.c:4:9>
identifier 'a'   [LeadingSpace] Loc=<min.c:4:16>
semi ';'                Loc=<min.c:4:17>
return 'return'  [StartOfLine] [LeadingSpace]   Loc=<min.c:5:5>
identifier 'b'   [LeadingSpace] Loc=<min.c:5:12>
semi ';'                Loc=<min.c:5:13>
r_brace '}'      [StartOfLine]  Loc=<min.c:6:1>
eof ''          Loc=<min.c:19:1>
```

ast

```
>clang -cc1 -ast-dump min.c
TranslationUnitDecl 0x14593632d18 <<invalid sloc>> <invalid sloc>
|-TypedefDecl 0x145936335d8 <<invalid sloc>> <invalid sloc> implicit __int128_t '__int128'
| `-BuiltinType 0x145936332b0 '__int128'
|-TypedefDecl 0x14593633648 <<invalid sloc>> <invalid sloc> implicit __uint128_t 'unsigned __int128'
| `-BuiltinType 0x145936332d0 'unsigned __int128'
|-TypedefDecl 0x14593633980 <<invalid sloc>> <invalid sloc> implicit __NSConstantString 'struct __NSConstantString_tag'
| `-RecordType 0x14593633720 'struct __NSConstantString_tag'
|   `-Record 0x145936336a0 '__NSConstantString_tag'
|-TypedefDecl 0x14593633a28 <<invalid sloc>> <invalid sloc> implicit __builtin_ms_va_list 'char *'
| `-PointerType 0x145936339e0 'char *'
|   `-BuiltinType 0x14593632db0 'char'
|-TypedefDecl 0x14593633a98 <<invalid sloc>> <invalid sloc> implicit __builtin_va_list 'char *'
| `-PointerType 0x145936339e0 'char *'
|   `-BuiltinType 0x14593632db0 'char'
`-FunctionDecl 0x14593633c68 <min.c:2:1, line:6:1> line:2:6 min 'int (int, int)'
  |-ParmVarDecl 0x14593633b08 <col:10, col:14> col:14 used a 'int'
  |-ParmVarDecl 0x14593633b88 <col:16, col:20> col:20 used b 'int'
  `-CompoundStmt 0x1459373ed10 <col:22, line:6:1>
    |-IfStmt 0x1459373ecb0 <line:3:5, line:4:16>
    | |-BinaryOperator 0x1459373ec48 <line:3:8, col:10> 'int' '<'
    | | |-ImplicitCastExpr 0x1459373ec18 <col:8> 'int' <LValueToRValue>
    | | | `-DeclRefExpr 0x1459373ebd8 <col:8> 'int' lvalue ParmVar 0x14593633b08 'a' 'int'
    | | `-ImplicitCastExpr 0x1459373ec30 <col:10> 'int' <LValueToRValue>
    | |   `-DeclRefExpr 0x1459373ebf8 <col:10> 'int' lvalue ParmVar 0x14593633b88 'b' 'int'
    | `-ReturnStmt 0x1459373eca0 <line:4:9, col:16>
    |   `-ImplicitCastExpr 0x1459373ec88 <col:16> 'int' <LValueToRValue>
    |     `-DeclRefExpr 0x1459373ec68 <col:16> 'int' lvalue ParmVar 0x14593633b08 'a' 'int'
    `-ReturnStmt 0x1459373ed00 <line:5:5, col:12>
      `-ImplicitCastExpr 0x1459373ece8 <col:12> 'int' <LValueToRValue>
        `-DeclRefExpr 0x1459373ecc8 <col:12> 'int' lvalue ParmVar 0x14593633b88 'b' 'int'
```

诊断

https://clang.llvm.org/docs/UsersManual.html

```
clang -fsyntax-only -fdiagnostics-show-category=name在诊断行中启用打印类别信息。
```

https://techdecoded.intel.io/resources/understanding-the-instruction-pipeline/#gs.qeskep 指令流水线

![compiler](.\images\compiler.png)

![JIT](.\images\JIT.png)

![llvm-ir](.\images\llvm-ir.png)

![MLIR](.\images\MLIR.png)

![v8-LLVM-IR-WebAssembly](.\images\v8-LLVM-IR-WebAssembly.png)

JIT WebAssembly 系列（二）JavaScript Just-in-time (JIT) 工作原理 - 胡子大哈的文章 - 知乎 https://zhuanlan.zhihu.com/p/25669120





![HLS](.\images\HLS.png)

![wasm-good](.\images\wasm-good.png)

![wasm-all](.\images\wasm-all.png)

![JSLinux](.\images\JSLinux.png)

![QEMU-2](.\images\QEMU-2.png)

![QEMU-1](.\images\QEMU-1.png)

![QEMU](.\images\QEMU.png)

![GraalVM](.\images\GraalVM.png)

![JVM](.\images\JVM.png)

![JIT](.\images\JIT.png)

![LLVM-world](.\images\LLVM-world.png)





https://www2.slideshare.net/zongfanyang/coscup-2016-llvm















