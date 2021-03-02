# 主析取范式和主合取范式的c++求解程序







blog.csdn.net/cfc_andy/article/details/102770417




这是我们老师刚刚布置的作业，自己百度了一下，发现没有比较简单完善的程序代码，于是自己写成功后，与大家分享一下。有些地方描述的不好，可能比较难理解，请见谅。如果有啥不懂的，可以在下面评论，我会尽力解答
一、算法思想
主要思想是：先求真值表，再根据真值表输出主析取范式和主合取范式。

用！来表示非，用小写v表示析取，用^来表示合取，用~来表示双条件，用-来表示条件，用大写字母来表示命题变元。

真值表的求解
① 根据命题的个数n，得出所有命题变元赋值的情况个数sum，例如n=4个命题变元，则有sum=2^4种情况，并将所有情况存入二维数组a[i][j]中,a[i]代表第i种情况。
② 创建两个栈，一个用来存放操作符Operator，先自己在栈里面存放字符‘#’（输入命题公式时要最后应该加一个字符‘#’）；一个存放操作数Operand。
③ 根据表达式求值的思想，读取表达式，若是操作符，则与之前的操作符相比优先级，若大于前者，则读取下一个；若相等，则说明两者为（）则弹出前者，读取下一个；若小于前者，则可以进行运算；
④ 若读取的是操作数，则在数组a中读取操作数所对应的数，存入栈中；
⑤ 将最后的运算结果存入数组result中，再次循环步骤③，循环sum次即可
⑥ 根据result的结果，当输出主析取范式时，当result[i]==1时，则输出相应的命题变元（当命题变元为1则输出P，为0则输出！P），把result都遍历一遍，将结果为1的都连在一起即可；求取主合取范式就将result=0的输出连在一起即可；
二、源代码

第一个头文件const.h//预定义常量头文件
#pragma once

#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 1
#define INFEASIBLE -1
#define OVERFLOW -2

typedef int Status;

第二个头文件prefunction.h//变量类型的定义与函数的声明
#pragma once

#include"const.h"

#define STACK_INIT_SIZE 100
#define STACKINCREMENT 10

typedef char SElemType;

typedef int SElemType_1;

typedef struct {
SElemType *base;
SElemType *top;
int stacksize;
}SqStack;//操作符栈

typedef struct {
SElemType_1 *INTbase;
SElemType_1 *INTtop;
int INTstacksize;
}INTStack;//操作数栈
Status InitStack(SqStack &S);//初始化
Status GetTop(SqStack S, SElemType &e);//读栈顶
Status Push(SqStack &S, SElemType e);//入栈
Status Pop(SqStack &S, SElemType &e);//出栈
Status initStack(INTStack &S);// 初始化
Status pop(INTStack &S, SElemType_1 &e);// 出栈
Status push(INTStack &S, SElemType_1 e);// 入栈
char precede(SElemType e1, SElemType e2);//判断操作数的优先级
Status bothway(int &a, SElemType b, int c);//双向运算符操作
Status TruthTable(int a[65][6], int count,char ch[6]);//真值表
Status Proposition(char a[50], char ch[6]);//求命题的个数

第二个头文件function.h
#pragma once
#include
#include
#include

#include"prefunction.h"

Status InitStack(SqStack &s) {
//构造一个空的栈
s.base = (SElemType*)malloc(STACK_INIT_SIZE * sizeof(SElemType));
if (!s.base)
exit(OVERFLOW);
s.top = s.base;
s.stacksize = STACK_INIT_SIZE;
return OK;
}
Status GetTop(SqStack s, SElemType &e) {
//获得栈顶元素
if (s.top == s.base)
return ERROR;
e = (s.top - 1);
return OK;
}
Status Push(SqStack &s, SElemType e) {
//插入元素e为新的栈顶
if (s.top - s.base >= s.stacksize) {
s.base = (SElemType)realloc(s.base, (s.stacksize + STACKINCREMENT) * sizeof(SElemType));
if (!s.base)
exit(OVERFLOW);
s.top = s.base + s.stacksize;
s.stacksize += STACKINCREMENT;
}
*s.top++ = e;
return OK;
}
Status Pop(SqStack &s, SElemType &e) {
//弹出栈顶元素
if (s.top == s.base)
return ERROR;
e = –s.top;
return OK;
}
Status initStack(INTStack &s)
{
//构造一个空的栈
s.INTbase = (SElemType_1)malloc(STACK_INIT_SIZE * sizeof(SElemType_1));
if (!s.INTbase)
exit(OVERFLOW);
s.INTtop = s.INTbase;
s.INTstacksize = STACK_INIT_SIZE;
return OK;
}
Status pop(INTStack &s, SElemType_1 &e)
{//弹出栈顶元素
if (s.INTtop == s.INTbase)
return ERROR;
e = –s.INTtop;
return OK;
}
Status push(INTStack &s, SElemType_1 e)
{
//插入元素e为新的栈顶
if (s.INTtop - s.INTbase >= s.INTstacksize) {
s.INTbase = (SElemType_1)realloc(s.INTbase, (s.INTstacksize + STACKINCREMENT) * sizeof(SElemType_1));
if (!s.INTbase)
exit(OVERFLOW);
s.INTtop = s.INTbase + s.INTstacksize;
s.INTstacksize += STACKINCREMENT;
}
*s.INTtop++ = e;
return OK;
}
char precede(SElemType e1, SElemType e2)//判断操作数的优先级
{
if (e1 == ‘v’&&e2 == ‘v’)
return ‘>’ ;
if (e1 == ‘v’&&e2 == ‘^’)
return ‘>’;
if (e1 == ‘v’&&e2 == ‘~’)
return ‘>’;
if (e1 == ‘v’&&e2 == ‘-’)
return ‘>’;
if (e1 == ‘v’&&e2 == ‘)’)
return ‘>’;
if (e1 == ‘v’&&e2 == ‘(’)
return ‘<’;
if (e1 == ‘v’&&e2 == ‘#’)
return ‘>’;

if (e1 == '^'&&e2 == 'v')
	return '>';
if (e1 == '^'&&e2 == '^')
	return '>';
if (e1 == '^'&&e2 == '~')
	return '>';
if (e1 == '^'&&e2 == '-')
	return '>';
if (e1 == '^'&&e2 == ')')
	return '>';
if (e1 == '^'&&e2 == '(')
	return '<';
if (e1 == '^'&&e2 == '#')
	return '>';

if (e1 == '-'&&e2 == 'v')
	return '>';
if (e1 == '-'&&e2 == '^')
	return '>';
if (e1 == '-'&&e2 == '~')
	return '>';
if (e1 == '-'&&e2 == '-')
	return '>';
if (e1 == '-'&&e2 == ')')
	return '>';
if (e1 == '-'&&e2 == '(')
	return '<';
if (e1 == '-'&&e2 == '#')
	return '>';

if (e1 == '~'&&e2 == 'v')
	return '>';
if (e1 == '~'&&e2 == '^')
	return '>';
if (e1 == '~'&&e2 == '~')
	return '>';
if (e1 == '~'&&e2 == '-')
	return '>';
if (e1 == '~'&&e2 == ')')
	return '>';
if (e1 == '~'&&e2 == '(')
	return '<';
if (e1 == '~'&&e2 == '#')
	return '>';

if (e1 == '('&&e2 == 'v')
	return '<';
if (e1 == '('&&e2 == '^')
	return '<';
if (e1 == '('&&e2 == '~')
	return '<';
if (e1 == '('&&e2 == '-')
	return '<';



if (e1 == '#'&&e2 == 'v')
	return '<';
if (e1 == '#'&&e2 == '^')
	return '<';
if (e1 == '#'&&e2 == '~')
	return '<';
if (e1 == '#'&&e2 == '-')
	return '<';
if (e1 == '#'&&e2 == '(')
	return '<';

if (e1 == '!'&&e2 == 'v')
	return '>';
if (e1 == '!'&&e2 == '^')
	return '>';
if (e1 == '!'&&e2 == '~')
	return '>';
if (e1 == '!'&&e2 == '-')
	return '>';
if (e1 == '!'&&e2 == ')')
	return '>';
if (e1 == '!'&&e2 == '(')
	return '<';
if (e1 == '!'&&e2 == '#')
	return '>';



if (e1 == 'v'&&e2 == '!')
	return '<';
if (e1 == '^'&&e2 == '!')
	return '<';
if (e1 == '~'&&e2 == '!')
	return '<';
if (e1 == '-'&&e2 == '!')
	return '<';
if (e1 == '#'&&e2 == '!')
	return '<';





if (e1 == '('&&e2 == '(')
	return '<';
if (e1 == '('&&e2 == ')')
	return '=';
return 'p';
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
}
//用小写的v来表示析取；用^来表示合取；用-来表示条件；用~来表示双条件;
Status bothway(int &a, SElemType b, int c)
{
if ( b ==‘v’) {
if (a == 0 && c == 0)
a = 0;
else
a = 1;
}
if (b ‘^’) {
if (a == 1 && c == 1)
a = 1;
else
a = 0;
}
if (b == ‘-’) {
if (a == 1 && c == 0)
a = 0;
else
a = 1;
}
if (b == ‘~’) {
if (a == c)
a = 1;
else
a = 0;
}
return OK;
}
Status TruthTable(int a[65][6], int count,char ch[6])//真值表
{
int i,sum=1,s,k,j;
for (i = 0; i < count; i++)
sum = sum * 2;
i = 1;
s = sum;
while (i <= count) {
s = s / 2;
k = 0;
j = 1;
while (j <= sum) {
if((j/s)%20)
for (k = 0; k < s; k++) {
a[j-1][i-1] = 0; j++;
}
else
for (k = 0; k < s; k++) {
a[j-1][i-1] = 1; j++;
}
}
i++;
}

return OK;
1
}
Status Proposition(char a[50], char ch[6])//求命题的个数
{
int i=0,j=0,k=0;
int flag = 0;
while (a[i]) {
if (a[i] >= 65 && a[i] <= 90) {
while (ch[j]) {
if (a[i] == ch[j])
flag = 1;
j++;
}
if (flag == 0) {
ch[k] = a[i];
k++;
}
flag = 0;
j = 0;
}
i++;
}
return OK;
}
第四个文件是cpp文件：xiquhequ.cpp
#include"function.h"

using namespace std;

int main() {
int n,a[65][6],sum=1,s;
char exqu[50], ch[6] = {0};
printf_s("请输入命题的个数:");
scanf("%d", &n);
printf_s("请输入命题表达式:");
scanf("%s", exqu);
for (s = 0; s < n; s++) {
	sum = sum * 2;
}//求所有的情况个数sum


Proposition(exqu,ch);//将n个变量变元提取出来存入字符数组ch

TruthTable(a, n, ch);//将所有情况存入数组a中


SqStack Operator;//操作符栈
INTStack Operand;//操作数栈
InitStack(Operator);//初始化
initStack(Operand);//初始化


SElemType e;
int k = 0,result[65];
int i = 0,j=0;
SElemType_1 p, q;
SElemType	E;

while (k < sum)
{
	*Operator.top = '#';
	Operator.top++;
	GetTop(Operator, e);
	i = 0;
	while (exqu[i] != '#' || e != '#') 
	{


		if (exqu[i] <= 90 && exqu[i] >= 65) {
			while (exqu[i] != ch[j]) {
				j++;
			}
			push(Operand, a[k][j]);
			//print(Operand);
			//*Operand.INTtop = a[k][j];// printf_s("%d", a[k][j]);
			//Operand.INTtop++;
			j = 0;
			i++;
		}
		else {
			GetTop(Operator, e);
			switch (precede(e, exqu[i])) {
			case '<':Push(Operator, exqu[i]); i++;
				break;
			case '=':Pop(Operator, e); i++;
				break;
			case '>':Pop(Operator, E); 
				if (E == '!')
				{
					pop(Operand, p);
					if (p == 0)
						p = 1;
					else
						p = 0;	
					push(Operand, p);

					//print(Operand);
					//printf("%d", p);
				}
				else
				{
					pop(Operand, p); pop(Operand, q);  bothway(q, E, p); push(Operand, q);//print(Operand);
				}
				break;
			default:printf_s("precede函数返回值错误\n");
			}
		}
		GetTop(Operator, e);
	}

	pop(Operand, q);
	//printf("%d\n", q);
	result[k] = q;
	k++;
	Pop(Operator, e);
	//Pop(Operator, e);


}


for (i = 0; i < n; i++) {
	printf_s("%c    ", ch[i]);
}
i = 0;
while (exqu[i]!='#') {
	printf_s("%c", exqu[i]);
	i++;
}
printf_s("\n");
for (k = 0; k < sum; k++) {

	for (i = 0; i < n; i++) {
		printf_s("%d    ", a[k][i]);
	}
	printf_s("%d", result[k]);
	printf_s("\n");
}

//输出主析取范式
printf_s("主析取范式\n");
for (k = 0; k < sum; k++)
{
	if (result[k] == 1)
	{
		printf_s("(");
		for (i = 0; i < n; i++)
		{
			if (a[k][i] == 1)
				printf_s("%c^", ch[i]);
			else
				printf_s("!%c^", ch[i]);
		}
		printf_s("\b)v");
	}		
}
printf_s("\b \n");

//输出主合取范式
printf_s("主合取范式\n");
for (k = 0; k < sum; k++)
{
	if (result[k] == 0)
	{
		printf_s("(");
		for (i = 0; i < n; i++)
		{
			if (a[k][i] == 1)
				printf_s("%c^", ch[i]);
			else
				printf_s("!%c^", ch[i]);
		}
		printf_s("\b)v");
	}
}
printf_s("\b ");
getchar();
getchar();
return 0;