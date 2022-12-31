# Vector




[Vector详解](https://www.cnblogs.com/zsq1993/p/5929806.html)

Vector数组快速声明与初始化
一维
以int类型为例子

设置数组长度的默认初始
```
vector<int> data(N);
```

N为默认数组长度，默认初始值为0
设置数组长度的给定值初始
```
vector<int> data(N,value);

```
N为默认数组长度value为初始值
直接给定数据
```
vector<int> data = {1,2,3,4,5};

```
动态改变长度(主要调用vector 中的resize()函数)
二维
设置数组长度的默认初始
```
vector<vector<int>> data(N1, vector<int>(N2));

```
N1为行，N2为列，默认值为0
设置数组长度的给定初始值
```
vector<vector<int>> data(N1, vector<int>(N2,value));

```

N1为行，N2为列，默认值为value
直接给定数据(以初始一个2X5的数组为例)
```
vector<int> data = {{1,2,3,4,5},{6,7,8,9,10}};

```
动态改变长度(主要调用vector 中的resize()函数)
三维
设置数组长度的默认初始
```
vector<vector<vector<int>>> dp(N1, vector<vector<int>>(N2, vector<int>(N3)));

```
默认值为0
设置数组长度的给定初始值
```
vector<vector<vector<int>>> dp(N1, vector<vector<int>>(N2, vector<int>(N3, value)));

```
默认值为value

1 vector二维数组的创建和初始化

std::vector <int> vec(10,90); //将10个一维动态数组初始为90
std::vector<std::vector<int> > vec(row,vector<int>(col,0)); //初始化row * col二维动态数组，初始化值为0

2 获取一维数组的长度

int size = vec.size();

3 获取二维数组的长度

int size_row = vec.size(); //获取行数
int size_col = vec[0].size(); //获取列数

 

4 给vector二维数组赋值

简单的就直接赋值

ans[0][0]=1;

ans[0][1]=2;

ans[1][0]=3;

ans[1][1]=4;

（1） vector<int> a(10); //定义了10个整型元素的向量（尖括号中为元素类型名，它可以是任何合法的数据类型），但没有给出初值，其值是不确定的。
（2）vector<int> a(10,1); //定义了10个整型元素的向量,且给出每个元素的初值为1
（3）vector<int> a(b); //用b向量来创建a向量，整体复制性赋值
（4）vector<int> a(b.begin(),b.begin+3); //定义了a值为b中第0个到第2个（共3个）元素
（5）int b[7]={1,2,3,4,5,9,8};vector<int> a(b,b+7); //从数组中获得初值





1.构造函数
vector():创建一个空vector
vector(int nSize):创建一个vector,元素个数为nSize
vector(int nSize,const t& t):创建一个vector，元素个数为nSize,且值均为t
vector(const vector&):复制构造函数
vector(begin,end):复制[begin,end)区间内另一个数组的元素到vector中
    2.增加函数
 

 

void push_back(const T& x):向量尾部增加一个元素X
iterator insert(iterator it,const T& x):向量中迭代器指向元素前增加一个元素x
iterator insert(iterator it,int n,const T& x):向量中迭代器指向元素前增加n个相同的元素x
iterator insert(iterator it,const_iterator first,const_iterator last):向量中迭代器指向元素前插入另一个相同类型向量的[first,last)间的数据
   3.删除函数
 

 

iterator erase(iterator it):删除向量中迭代器指向元素
iterator erase(iterator first,iterator last):删除向量中[first,last)中元素
void pop_back():删除向量中最后一个元素
void clear():清空向量中所有元素
  4.遍历函数
 

 

reference at(int pos):返回pos位置元素的引用
reference front():返回首元素的引用
reference back():返回尾元素的引用
iterator begin():返回向量头指针，指向第一个元素
iterator end():返回向量尾指针，指向向量最后一个元素的下一个位置
reverse_iterator rbegin():反向迭代器，指向最后一个元素
reverse_iterator rend():反向迭代器，指向第一个元素之前的位置
  5.判断函数
 

 

bool empty() const:判断向量是否为空，若为空，则向量中无元素
  6.大小函数
 

 

int size() const:返回向量中元素的个数
int capacity() const:返回当前向量张红所能容纳的最大元素值
int max_size() const:返回最大可允许的vector元素数量值
  7.其他函数
 

 

void swap(vector&):交换两个同类型向量的数据
void assign(int n,const T& x):设置向量中第n个元素的值为x
void assign(const_iterator first,const_iterator last):向量中[first,last)中元素设置成当前向量元素



关于C++中vector<vector<int> >的使用 https://www.cnblogs.com/tyty-Somnuspoppy/p/9361821.html







## 二维数组

```cpp
vector<vector<int> > array(m); //这个m一定不能少
//vector<int> array[m];
//初始化一个m*n的二维数组
for(int i=0;i<m;i++) {
    array[i].resize(n);
}
//遍历赋值
for(i = 0; i < array.size(); i++) 
{ 
　　for (j = 0; j < array[0].size();j++)
 { 
　　array[i][j] = (i+1)*(j+1); 
} 
```


























