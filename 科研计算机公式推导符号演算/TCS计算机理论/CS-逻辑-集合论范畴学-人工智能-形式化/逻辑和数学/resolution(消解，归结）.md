# resolution(消解，归结）


















国科大高级人工智能8-归结原理和horn子句

blog.csdn.net/weixin_40485502/article/details/103874579



消解原理程序：
cnblogs.com/dadamrx/p/7294648.html




```c++
#include <cstdio>
#include <cstring>
#define N 1010
int s[N][30]; 
//每行存储一个简单析取式，第二维下标0~25代表命题变项a~z
//取值 0: 该变项没有出现，1: 该变项出现，2: 该变项出现且为否定
int sum0, sum1, sum2; //实现对S1，S2，S3三个集合的指向
void store(char str[]) //将输入字符串存到s数组，标记到S2
{
	memset(s, 0, sizeof(s));
	sum0 = sum1 = -1; sum2 = 0;
	int len = strlen(str);
	int i = 0; 
	while (i <= len)
	{
		if (str[i] >= 'a' && str[i] <= 'z') s[sum2][str[i] - 'a'] = 1;
		else if (str[i] == '&') sum2++;
		else if (str[i] == '!') s[sum2][str[++i] - 'a'] = 2;
		i++;
	}
}
bool same(int a[], int b[]) //判断两简单析取式是否相同
{
	for (int i = 0; i < 26; i++)
		if (a[i] != b[i]) return false;
	return true;
}
bool check(int c[]) //检查S1，S2，S3中是否有重复
{
	for (int i = 0; i <= sum2; i++)
		if (same(s[i], c)) return false;
	return true;
}
bool res(int a[], int b[]) //消解函数，若得到空子句，返回false，否则返回true
{
	int single = 0; //不能消解的变项个数
	int couple = 0; //可消解的变项个数
	for (int i = 0; i < 26; i++)
	{
		if (!a[i] && !b[i]) continue;
		if ((a[i] == 1 && b[i] == 2) || (a[i] == 2 && b[i] == 1)) couple++;
		else single++;
	}

	if (couple != 1) return true; //不能消解或有多对可以消解
	if (!single) return false; //只有一对可消解且没有不能消解的变项，得到空子句

	int c[30]; //消解结果
	for (int i = 0; i < 26; i++)
	{
		if ((!a[i] && !b[i]) || (a[i] + b[i] == 3)) c[i] = 0;
		else if (a[i] == 1 || b[i] == 1) c[i] = 1;
		else c[i] = 2;
	}

	if (check(c)) //检查c在S0，S1，S2中是否出现过
	{
		sum2++; //将c加入S2
		for (int i = 0; i < 26; i++) s[sum2][i] = c[i];
	}
	return true;
}
int main()
{
	char str[N];
	scanf("%s", str);
	store(str);
	do
	{
		sum0 = sum1; sum1 = sum2; //将S1并到S0中，令S1等于S2，清空S2
		for (int i = 0; i <= sum0; i++)
			for (int j = sum0 + 1; j <= sum1; j++)
				if (!res(s[i], s[j]))
				{
					printf("NO\n");
					return 0;
				}
		for (int i = sum0 + 1; i <= sum1; i++)
			for (int j = i + 1; j <= sum1; j++)
				if (!res(s[i], s[j]))
				{
					printf("NO\n");
					return 0;
				}
	} while (sum2 > sum1); //若S2为空，结束
	printf("YES\n");
	return 0;
}
```
































