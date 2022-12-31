# 1. haskell-CFG

https://github.com/alexandrustoica/dataflow.analysis







analysis-dataflow
```
BNF
program := statement

statement :=
	| statement; statement
	| print(expression)
	| id = expression
	| if expression then statement else statement
	| while expression do statement

expression :=
	| number
	| id
	| expression + expression
	| expression - expression
	| expression * expression
	| expression / expression

number := [0-9] | [1-9][0-9]+
id := string                    // variable name

```






