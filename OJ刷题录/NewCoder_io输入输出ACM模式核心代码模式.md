[TOC]


## 重定向debug.bat


OJ的输入输出基本都是使用标准输入输出(也称标准I/O，即直接读键盘、写屏幕)。

OJ的判题方式则是使用输入输出重定向到文件一个问题(十分常见！！！！)，如果测试数据是多组的，但是恰巧你代码里面需要些标记数组，map，set等，在循环内一定记得清空

```cpp
vec.clear();set.clear();

while (!Queue.empty()) Queue.pop();

while(!stack.empty()) stack.pop();// stack操作的是堆内存，所以要一个一个弹出。

stack<int> s; stack<int>().swap(s); // swap相当于交换了s和一个空临时stack的内容，然后临时stack再结束生命周期，但由于操作的是堆空间，其实还是一个一个释放空间。

map<string,vector<int> > empty_map1;
map1.swap(empty_map1);
map1.clear();//map.clear()只是把map清空了，但是内存没有释放，如果要释放内存不止是要clear()掉，还要和一个空的map来进行swap，将内存释放。注意map中如果元素不是基本类型，也要进行内存释放，如指针，vector要尤其注意，否则map占的内存太大，会造成程序崩溃。

```

，不然可能会产生前面的测试样例影响了后续数据的答案。

关于cin，cout和scanf，printf。做题的时候尽量使用scanf  printf。下面告诉一个小常识，不要惊讶：cin cout比scanf printf慢20倍左右。在测试自己的程序时，可以在代码里加入重定向语句来方便测试，但是必须注意：自我测试完毕之后删除重定向语句，再提交代码。

代码里重定向方法：

compiler.bat

```bat
del debug.exe
g++ debug.cpp -o debug -std=c++14
debug.exe
type .\debug\out.txt
pause
```

debug.cpp

```cpp
#include <stdio.h>
#include <iostream>
using namespace std;
//C++语法
int main(){
    int a,b;
    freopen("debug\\in.txt","r",stdin); //输入重定向，输入数据将从in.txt文件中读取
    freopen("debug\\out.txt","w",stdout); //输出重定向，输出数据将保存在out.txt文件中
    while(cin>>a>>b)
    cout<<a+b<<endl; // 注意使用endl
    fclose(stdin);//关闭文件
    fclose(stdout);//关闭文件
    return 0;
}
```

也可讲究点多写些预编译信息：

```cpp
#define LOCAL //在提交代码时注释掉

#include<stdio.h>
// 实际使用中发现freopen也包含在iostream.h中，C++代码#include <iostream.h>即可。
int main(){
#ifdef LOCAL
    freopen("data.in", "r", stdin);//将data.in改为输入文件路径
    freopen("data.out", "w", stdout);//将data.out改为输出文件路径
#endif
             
     //fclose(stdin);//最后关闭
     //fclose(stdout);
    
    return 0;
}
```

随后，正常使用C/C++的标准输入，都会定向到上述两个文件中，以便于自测代码。

**核心代码模式**就像Leecode中，一般需要的文件会写成Solution类型，然后Solution sol对象，调用sol.解题自定义方法，可以直接在main中处理IO,而后传进去```vector<int>,vector<char>,vector<string>,vector<vector<int>> matrix```等等数据给Solution继续处理。

```cpp
class Solution{
public:
    int test(int a,int b){
        return a+b;
    }
};

//万能头文件#include<bits/stdc++.h>
//要使用标准的跨平台的库函数。 各个语言一般平台都会告诉你每种语言给的编译器版本，这个环境信息也是很重要的。
#include<iostream>
using namespace std;


int main(){
    Solution sol;
    //只有一组数据
    cin>>a>>b;
    Solution sol;
    cout<<sol.test(a,b)<<endl;

    //预先不输入数据的组数
    while(cin>>a>>b){
        cout<<a+b<<endl;
    }

    return 0;

}

```



```cpp
//input single group of Int Number只有一组数据
    int a,b;
    scanf("%d%d",&a,&d);
    printf("%d\n", sol(a,b));//
    cout<<test(a,b);
```

1、行末空格：比如我输出需要打印多个数需要使用空格分隔的时候，我们循环使用printf("%d  ",x);这种会很方便，但是这样会导致行末多一个空格，后台系统会严格比对你的输出和.out文件，这样也会被判错误

2、换行问题，对于每个样例，建议输出完全之后都换行一下。对于一些题目，可能就是不换行就导致了后面输入数据错位，那就肯定不可能过了。



```cpp
//有很多组数据，然后告诉了数据个数
//预先知道数据组数
cin>>n;
for(int i=0; i<n; i++){
    int a,b;
    cin>>a>>b;
    cout<<a+b<<endl;
}
```
//读取N行字符串

**cin.ignore**

```cpp
#include<iostream>
using namespace std;
int main(){
    int N;
    cin >> N ;  //希望读取N行，并输出
    while(N--){
        string s;
        getline(cin, s);
        cout << s << endl;
    }
}//上面的程序只能读取有效的两行，而第一行是一个空行，这不是我们想要的效果，这个看起来不起眼的错误，会导致笔试题0AC，不要问我怎么知道的。
```

*/
```cpp
//“可恶”的字符串——带空白
    int N;
    cin >> N ;  
    cin.ignore(); // 加上这一句即可解决。可去除缓冲区中残留的'\n'.
    while(N--){
        string s;
        getline(cin,s);
        cout << s << endl;;
    }
```
//output输出    //----------------------------------------------------------------

```cpp
//不需要输出case数
cin>>n;
for(int i=0; i<n; i++){
    int a, b;
    cin>>a>>b;
    cout<<a+b<<endl;
}
```

```cpp
//需要输出case数
cin>>n;
for(int i=0; i<n; i++){
    int a, b;
    cin>>a>>b;
    cout<<"Case"<<i+1<<a+b<<endl;
}
```

```cpp
//每个case之后有空行
for(int i=0; i<n; i++){
    int a, b;
    cin>>a>>b;
    cout<<"Case"<<i+1<<a+b<<endl<<endl;
}
```

```cpp
//两个Case之间有空行
cin>>n;
for(int i=0; i<n; i++){
    int a, b;
    cin>>a>>b;
    if(i>0){
        cout<<endl;
    }
    cout<<"Case"<<i+1<<a+b<<endl;
}
```




## 输入格式处理细节和技巧

| 输入格式                                                     | 输出格式                                                     |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 一个case输入                                                 | 一个输出结果                                                 |
| 有多个case输入，直到文件结束                                 | 一行一个结果                                                 |
| 先输入case个数，再依次输入每个case                           | 一行一个结果                                                 |
| 每行输入一组case，当case中的数据满足某种情况时退出           | 一行一个结果                                                 |
| 输入直到文件结束                                             | 一行一个结果，结果输完后还有一个blank line                   |
| 一开始输入总的case数，每组case一开始有控制该组输入个数的东西 | 一行一个结果，两个结果之间有一个回车，注意最后一个case后没有回车。 |



>
> 等待：服务器正忙，请稍后查看运行并评判您的程序
>
> 正在评测中编译中：您的程序正在被编译
>
> 正确：恭喜您！完全正确！
>
> 格式错误：结果正确，但格式不正确，比如多或少了换行或空格
>
> 答案错误：经过比对，您的程序错误运行错误程序运行后发生错误，可能包括：
>
> 指针/数组违规访问
> 除数为0
> 函数调用错误，或栈溢出
> 捕捉到违背处理的STL或自定义异常等
> …
>
> 时间超限：程序运行时间超过了时间限制，请检查程序的算法效率
>
> 内存超限：程序使用的内存超过了内存限制，请检查程序是否栈/堆开辟空间过大 或内存泄露
>
> 输出超限：输出了与答案无关的信息，比如“please input”等提示
>
> 编译错误：程序语法错误，编译不通过。可能您在本地可以编译通过，但可能使用了非标准C的函数 ，请使用符合标准的语法。
>




输入

> 不用保存所有组的输入，读一组算一组
> “可恶”的字符串——带空白
>
> scanf, cin之类都读到空白结束
> gets, cin.getline。再自己parse
> 用scanf, gets代替cin。

输出注意格式

> 字母大小写
> 什么时候换行
> 输出“case”后面有没有“#”或者“：”之类。
> 每行末尾有\n，但一般没有空白
> 用printf代替cout。


OJ常见状态

> 内存超限——使用内存过多
> 返回非零——main函数返回了非零值
> 浮点错误——除以零
> 运行错误——指针乱指
> 段错误——指针越界



## newcoder实战

## cin,cout版本vector类IO

8-9-10是实战中经常用到的方式，比如输入数组，有多组，以逗号/空格分隔，不同场景下的处理方式。主要是对 sstringstream 以及 getline main


https://ac.nowcoder.com/acm/contest/5647
//-------------------------------cin ==> vector<char>------------------
8 ACM模式调用核心代码模式

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
	void test(vector<string>& vec){
        sort(vec.begin(),vec.end());
        return;
    }
};

int main (){
    int n ;
    cin>>n;
    vector<string> vec;
    while(n--){
        string cur;
        cin>>cur;
        vec.push_back(cur);
    }
    //-------------------------processing
    Solution sol;
    sol.test(vec);
    //--------------------------processed
    int len = vec.size();
    for(int j =0;j<len - 1;j++){
        cout<<vec[j]<<" ";
    }
    cout<<vec[len - 1]<<endl;;
    return 0;
}
```

9
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
	void test(vector<string>& vec){
        sort(vec.begin(),vec.end());
        return;
    }
};

int main (){
    string input;
    vector<string> vec;
    while(getline(cin,input)){
        stringstream ss(input);
        string cur;
        while(ss>>cur){
            vec.push_back(cur);
        }
        //--------processing
        Solution sol;
        sol.test(vec);
        //--------processed
        int len = vec.size();
        for(int i =0;i<len - 1;i++){
            cout<<vec[i]<<' ';
        }
        cout<<vec[len- 1] <<endl;
        vec.clear();
    };
    return 0;
}
```


10

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
	void test(vector<string>& vec){
        sort(vec.begin(),vec.end());
        return;
    }
};

int main (){
    string input;
    vector<string> vec;
    while(getline(cin,input)){
        stringstream ss(input);
        string cur;
        while(getline(ss,cur,',')){//--------------------------------
            vec.push_back(cur);
        }
        //--------processing
        Solution sol;
        sol.test(vec);
        //--------processed
        int len = vec.size();
        for(int i =0;i<len - 1;i++){
            cout<<vec[i]<<',';//-------------------------------------
        }
        cout<<vec[len- 1] <<endl;
        vec.clear();
    };
    return 0;
}
```
script


```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    ;
    return 0;
}
/*
```

1 ACM模式调用核心代码模式

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int test(int a,int b){
        return a+b;
    }
};

int main(){
    int a,b;
    Solution sol;
    while(cin>>a>>b){
        cout<<sol.test(a,b)<<endl;
    }
    return 0;
}
```

2
```cpp
#include<bits/stdc++.h>
using namespace std;

int main (){
    int t;
    cin >> t;
    for(int i = 1;i<= t;i++){
        int a,b;
        cin>>a>>b;
        cout<<a+b<<endl;
    }
    return 0;
}
```

3
```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    int a,b;
    while(cin>>a>>b){
        if(a == 0 && b == 0) break;
        cout<<a+b<<endl;
        ;
    }
    return 0;
}

```

4
```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    int n;
    while(cin>>n){
        if(n == 0) break;
        int sum = 0;
        for(int i =1;i<=n;i++){
            int val;
            cin>>val;
            sum+=val;;
        };
        cout<<sum<<endl;;
    }
    return 0;
}
```


5
```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    int t;cin>>t;
    while(t--){
        int sum =0;
        int n;
        cin>>n;
        for(int i =0;i<n;i++){
            int val;
            cin>>val;
            sum += val;
        }
        cout<<sum<<endl;
    }
    return 0;
}
```

6
```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    int n ;
    while(cin>>n){
        int sum =0;
        for(int i =0;i<n;i++){
            int val;cin >>val;
            sum += val;
        };
        cout<<sum<<endl;
    };
    return 0;
}
```
//-------------------------------`cin ==> vector<int>`------------------
7
```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    string input;
    vector<int> vec;
    while(getline(cin,input)){
        stringstream ss(input);
        int val;
        while(ss>>val){
            vec.push_back(val);
        };
        int len = vec.size();
        int sum = 0;
        for(int j =0;j<len;j++){
            sum += vec[j];
        }
        cout<<sum<<endl;
        vec.clear();
    };
    return 0;
}
```

11
//---------------------------------------------

int型数据存储的数值范围是-231～231-1，即-2 147 483 648～ 2 147 483 647：

1byte = 8 bit;

int: 4byte =  32 bit 有符号signed范围：2^31-1 ~ -2^31即：2147483647 ~ -2147483648无符号unsigned范围：2^32-1 ~ 0即：4294967295 ~ 0

long: 4 byte = 32 bit 同int型

double: 8 byte = 64 bit 范围：1.79769e+308 ~ 2.22507e-308

long double: 12 byte = 96 bit 范围： 1.18973e+4932 ~ 3.3621e-4932

float: 4 byte = 32 bit 范围： 3.40282e+038 ~ 1.17549e-038

long long的最大值：9223372036854775807（>10^18）
long long的最小值：-9223372036854775808
unsigned long long的最大值：18446744073709551615

\__int64的最大值：9223372036854775807
\__int64的最小值：-9223372036854775808
unsigned \__int64的最大值：18446744073709551615


```cpp
#include <bits/stdc++.h>
using namespace std;

int main (){
    long long a,b;
    while(cin>>a>>b){
        cout<<a+b<<endl;
    };
    return 0;
}

```

### 到二维矩阵就只需要核心模式,反正newcoder调试方便

https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e


旋转矩阵之类的。


###  链表类，二叉树IO


如果在main中处理IO,输入输出一般传递到Solution类的核心代码模式的时候，会是`vector<int>,vector<string>,vector<char>,matrix`矩阵就是二维`vector<vector<int>>`。

而如果是链表类二叉树类，ListNode* head的话，一般就是新建链表类，二叉树相关数据结构，这就要写很多题目以外的代码了，一般这时候都是使用核心代码模式。

单链表模板类 https://blog.csdn.net/Zhoujy1996/article/details/80720300

```cpp
#include <iostream>
#include <string>

using namespace std;

//链表节点
template<typename T>
struct ListNode
{
    T data;
    ListNode<T> *next;
};

//单向链表 -- 采用类模板
//单链表操作类模板
template <typename T>
class LinkList
{
public:
    LinkList();
    LinkList(T elem);
    LinkList(int n, T elem);
    ~LinkList();
    void ClearList() const;
    bool Empty() const;
    int Length() const;
    T GetElem(int n) const;
    int LocateElem(T elem) const;
    bool Insert(int n, T elem);
    bool Delete(int n);
    void Displasy();
    void Remove(T elem);
private:
    ListNode<T> *m_head;
};

template <typename T>
LinkList<T>::LinkList() 
{
    //创建头节点
    m_head = new ListNode<T>;
    if (nullptr == m_head)
    {
        cout << "动态申请头节点内存失败" << endl;
        return;
    }

    m_head->next = nullptr;
}

template <typename T>
LinkList<T>::LinkList(T elem) :LinkList()
{
    Insert(1, elem);
}

template <typename T>
LinkList<T>::LinkList(int n, T elem) :LinkList()
{
    for (int i = 0; i < n; ++i)
    {
        Insert(i, elem);
    }
}

template <typename T>
LinkList<T>::~LinkList()
{
    ClearList();    //置为空白
    delete m_head;  //释放头节点
}

template <typename T>
void LinkList<T>::ClearList() const     //常成员函数 不改变对象的值
{
    ListNode<T> *temp, *p = m_head->next;

    while (p != nullptr)        //删除头节点以后的所有节点
    {
        temp = p->next;
        delete p;           //要释放动态内存
        p = temp;
    }

    m_head->next = nullptr;
}

template <typename T>
bool LinkList<T>::Empty() const
{
    //如果头节点的下一个节点为空，则该链表为空
    return nullptr == m_head->next;
}

template <typename T>
int LinkList<T>::Length() const
{
    int count = 0;
    ListNode<T> *ptemp = m_head->next;

    while (ptemp != nullptr)
    {
        count++;
        ptemp = ptemp->next;
    }

    return count;
}

template <typename T>
T LinkList<T>::GetElem(int n) const
{
    ListNode<T> *ptemp = m_head->next;

    if (n <= Length())
    {
        for (int i = 1; i < n; ++i)
        {
            ptemp = ptemp->next;
        }
    }
    else
    {
        cout << "out of ranger" << endl;
        return false;
    }

    return ptemp->data;
}

template <typename T>
int LinkList<T>::LocateElem(T data) const
{
    size_t location = 0;
    ListNode<T> *ptemp = m_head->next;

    while (ptemp != nullptr)
    {
        ++location;
        if (ptemp->data == data)            //注意 该类型必须支持 == 操作符，如果不支持需要进行运算符重载
        {
            return location;
        }

        ptemp = ptemp->next;
    }

    return 0;       //返回0表示未找到
}

template <typename T>
bool LinkList<T>::Insert(int n, T elem)
{
    ListNode<T> *ptemp = m_head;

    if (n-1 <= Length())
    {
        for (int i = 0; i < n - 1; ++i)
        {
            ptemp = ptemp->next;
        }

        //先生成一个新的节点
        ListNode<T> *newnode = new ListNode < T >;
        if (nullptr == newnode)
        {
            cout << "申请空间失败" << endl;
            return false;
        }

        newnode->data = elem;       //如果数据类型不是基本数据类型，即不支持 = 操作符，需要重载 = 操作符
        newnode->next = ptemp->next;
        ptemp->next = newnode;

        return true;
    }
    else
    {
        cout << "out of range" << endl;
        return false;
    }
}

template <typename T>
bool LinkList<T>::Delete(int n)
{
    ListNode<T> *ptemp = m_head;

    if (n <= Length())
    {
        for (int i = 0; i < n - 1; ++i)
        {
            ptemp = ptemp->next;
        }

        ListNode<T> *t = ptemp->next;       //指向待删除的节点

        ptemp->next = ptemp->next->next;        //将待删除节点的上一节点指向待删除节点的下一节点
        delete t;       //释放删除节点的内存

        return true;
    }
    else
    {
        cout << "out of range" << endl;
        return false;
    }
}

template <typename T>
void LinkList<T>::Displasy()
{
    ListNode<T> *ptemp = m_head->next;

    while (ptemp != nullptr)
    {
        cout << ptemp->data << endl;
        ptemp = ptemp->next;
    }
}

template <typename T>
void LinkList<T>::Remove(T elem)
{
    ListNode<T> *ptemp = m_head;

    while (ptemp->next != nullptr)
    {
        if (ptemp->next->data == elem)          //找到与要删除的节点相同
        {
            ListNode<T> *t = ptemp->next;       //指向待删除的节点
            ptemp->next = ptemp->next->next;        //将待删除节点的上一节点指向待删除节点的下一节点
            delete t;       //释放删除节点的内存
        }
        else        //这里需要注意一下：如果删除了那么它的下一节点是新的节点需要重现判断，所以不需要移动
        {
            ptemp = ptemp->next;
        }

    }
}

struct Data
{
    int id;
    string name;
};
//由于使用的是结构体，所以对于一些运算符需要进行重载
ostream &operator << (ostream &os, const Data &data)
{
    os << data.id << "  " << data.name;
    return os;
}

bool operator==(const Data &data1, const Data &data2)
{
    //按照ID进行比较
    return data1.id == data2.id;
}
```



如果需要本地执行像leecode之类的测例的话，一般需要写一个`vector<int> vec`转linked list的方法就可以直接从[1,2,3,4]转换等效对应单链表 双链表之类的；


```cpp
//vec转linked list
int len = vec.size();
for(int i =0;i<len;i++){
    int temp = vec[i];
    ...;//尾插法，遍历vec[i]不断添加尾插到链表head中即可。
}
```

**数组转vector**：使用vector的初始化构造函数
a. 定义vector时直接赋值，如：

```cpp
vector<char> v(array, array + sizeof(array))  
//其用法是：vector<char> v(a, a+N)  (其中：N代表数组长度.)
```
b. 先定义vector，其元素数目为N，再使用memcpy将array的值拷贝到vector中，如：

```cpp
vector<int> v(N)
memcpy(&V[0], array, sizeof(array))
```


**vector转数组**: 使用memcpy将vector中的数据拷贝到数组中
注意: memcpy的第三个参数，拷贝长度必须乘以sizeof(vec[0])

```cpp
#include <vector>
#include <iostream>
 
using std::vector;
 
int main(void){
    //初始化为10个c字符
    vector<unsigned char> vec(10, 'c');
    unsigned char charray[vec.size()];
 
    //vector全部转到数组
    memcpy(charray, &vec[0], vec.size() * sizeof(vec[0]));
 
    for(int i = 0; i != sizeof(charray); ++i){
        std::cout << charray[i] ; //打印出来观察一下
    }
    std::cout << std::endl;
    //转部分vector数据到数组，最后4个
    unsigned char ary1[4];
    memcpy(ary1, &vec[6], 4);
 
    for(int i = 0; i != sizeof(ary1); ++i){
        std::cout << ary1[i] ;
    }
    std::cout << std::endl;
 
    return 0;
}
```
将数组线性表转换为链表

```cpp
//将数组线性表转换为链表
template<typename T>
void chain<T>::fromList(arrayList<T>&theList)
{
	int i = 0;
	T temp= theList.get(0);
	firstNode = new chainNode<T>(temp, firstNode);
	do
	{
		chainNode<T>*p = firstNode;
		int k = 0;
		while(k<i)
		{
			p = p->next;
			k++;
		}
		temp = theList.get(i+1);
		p->next = new chainNode<T>(temp, p->next);
		listSize++;
		i++;
	} while (i<theList.size()-1);
	listSize++;
}
```

如果需要本地执行像leecode二叉树之类的话，IO一般为：

```cpp
输入
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出
[null, 3, 7, true, 9, true, 15, true, 20, false]
```
则需要写一个vector<string>指令符号列表生成-->对应代码模板元编程的替换操作，也可以无脑一点实现“符号匹配对应的指令序列”case str == "BSTIterator" 执行对应指令,case str == "next"执行对应位置指令

```cpp
//符号匹配对应的指令序列

```

注意：**有参指令** 指令符号vector的index，一般和下一个vector的对应位置index相对应。这玩意儿因题而异，如非必要，反正leecode核心代码模式能直接用，多数时候就懒得写。

比较常用的方法，还需要写一个 [[7, 3, 15, null, null, 9, 20]] vector<vector<string>>完全二叉树层次遍历序列-->二叉树反序列化构造二叉树，返回对应root。

https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

```cpp
//完全二叉树层次遍历序列-->二叉树反序列化构造二叉树，返回对应root
public class Codec {
    public String rserialize(TreeNode root, String str) {
        if (root == null) {
            str += "None,";
        } else {
            str += str.valueOf(root.val) + ",";
            str = rserialize(root.left, str);
            str = rserialize(root.right, str);
        }
        return str;
    }
  
    public String serialize(TreeNode root) {
        return rserialize(root, "");
    }
  
    public TreeNode rdeserialize(List<String> l) {
        if (l.get(0).equals("None")) {
            l.remove(0);
            return null;
        }
  
        TreeNode root = new TreeNode(Integer.valueOf(l.get(0)));
        l.remove(0);
        root.left = rdeserialize(l);
        root.right = rdeserialize(l);
    
        return root;
    }
  
    public TreeNode deserialize(String data) {
        String[] data_array = data.split(",");
        List<String> data_list = new LinkedList<String>(Arrays.asList(data_array));
        return rdeserialize(data_list);
    }
}

//作者：LeetCode-Solution
//链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/
```
LL文法的读取指令序列，来实现

```cpp
class Codec {
public:
    string serialize(TreeNode* root) {
        if (!root) return "X";
        auto l = "(" + serialize(root->left) + ")";
        auto r = "(" + serialize(root->right) + ")";
        return  l + to_string(root->val) + r;
    }

    inline TreeNode* parseSubtree(const string &data, int &ptr) {
        ++ptr; // 跳过左括号
        auto subtree = parse(data, ptr);
        ++ptr; // 跳过右括号
        return subtree;
    }

    inline int parseInt(const string &data, int &ptr) {
        int x = 0, sgn = 1;
        if (!isdigit(data[ptr])) {
            sgn = -1;
            ++ptr;
        }
        while (isdigit(data[ptr])) {
            x = x * 10 + data[ptr++] - '0';
        }
        return x * sgn;
    }

    TreeNode* parse(const string &data, int &ptr) {
        if (data[ptr] == 'X') {
            ++ptr;
            return nullptr;
        }
        auto cur = new TreeNode(0);
        cur->left = parseSubtree(data, ptr);
        cur->val = parseInt(data, ptr);
        cur->right = parseSubtree(data, ptr);
        return cur;
    }

    TreeNode* deserialize(string data) {
        int ptr = 0;
        return parse(data, ptr);
    }
};

```
这样就能使用leecode的测例本地自动调试，甚至可以加断点检查到底什么地方出问题，步进debug。

输入一颗二叉搜索树, 将该二叉搜索树转换成一个排序的**双向链表**. https://www.cnblogs.com/clnchanpin/p/6740431.html



https://blog.nowcoder.net/n/954373f213e14eeab0a69ed0e9ef1b6e
牛客网树结构

```cpp
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
using namespace std;

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};

void PrintTree(TreeNode* root) {
	if (root == NULL) {
		printf("%s", "{}");
		return;
	}
	printf("%s", "{");
	vector<TreeNode*> v;
	if (root != NULL) {
		v.push_back(root);
	}
	size_t c = 0;
	string none;
	while (c < v.size()) {
		if (c == 0) {
			printf("%d", v[c]->val);
			v.push_back(v[c]->left);
			v.push_back(v[c]->right);
		} else {
			if (v[c] == NULL) {
				none.append(",#");
			} else {
				printf("%s,%d", none.c_str(), v[c]->val);
				none.clear();
				v.push_back(v[c]->left);
				v.push_back(v[c]->right);
			}
		}
		++c;
	}
	printf("%s", "}");
}


struct TreeLinkNode {
	int val;
	struct TreeLinkNode *left;
	struct TreeLinkNode *right;
	struct TreeLinkNode *next;
	TreeLinkNode(int x) :
			val(x), left(NULL), right(NULL), next(NULL) {
	}
};
void PrintTreeLinkNode(TreeLinkNode* root) {
	if (root == NULL) {
		printf("%s", "{}");
		return;
	}
	printf("%s", "{[");
	vector<TreeLinkNode*> v;
	vector<TreeLinkNode*> label_node_v;
	if (root != NULL) {
		v.push_back(root);
		label_node_v.push_back(root);
	}
	size_t c = 0;
	string none;
	while (c < v.size()) {
		if (c == 0) {
			printf("%d", v[c]->val);
			v.push_back(v[c]->left);
			v.push_back(v[c]->right);
		} else {
			if (v[c] == NULL) {
				none.append(",#");
			} else {
				label_node_v.push_back(v[c]);
				printf("%s,%d", none.c_str(), v[c]->val);
				none.clear();
				v.push_back(v[c]->left);
				v.push_back(v[c]->right);
			}
		}
		++c;
	}
	v.clear();
	printf("%s", "],[");
	for (size_t i = 0; i < label_node_v.size(); ++i) {
		if (i != 0) {
			printf("%s", ",");
		}
		if (label_node_v[i]->next != NULL) {
			// 注意：这里的link是根据节点的指来索引的，所以这种数据结构每个节点的val要唯一
			printf("%d", label_node_v[i]->next->val);
		} else {
			printf("%s", "#");
		}
	}
	printf("%s", "]}");
}


struct RandomListNode {
	int label;
	struct RandomListNode *next, *random;
	RandomListNode(int x) :
			label(x), next(NULL), random(NULL) {
	}
};

void PrintRandomListNode(RandomListNode* head) {
	if (head == NULL) {
		printf("%s", "{}");
		return;
	}
	RandomListNode* current = head;
	printf("%s", "{");
	while (current != NULL) {
		if (current == head) {
			printf("%d", current->label);
		} else {
			printf(",%d", current->label);
		}
		current = current->next;
	}
	current = head;
	while (current != NULL) {
		if (current->random != NULL) {
			printf(",%d", current->random->label);
		} else {
			printf("%s", ",#");
		}
		current = current->next;
	}
	printf("%s", "}");
}


struct UndirectedGraphNode {
	int label;
	vector<struct UndirectedGraphNode *> neighbors;
	UndirectedGraphNode(int x) :
			label(x) {
	}
};

void PrintUndirectedGraphNode(UndirectedGraphNode* root) {
	if (root == NULL) {
		printf("%s", "{}");
		return;
	}
	printf("%s", "{");
	if (root != NULL) {
		set<UndirectedGraphNode*> nodes_set;
		map<int, UndirectedGraphNode*> nodes_map;
		vector<UndirectedGraphNode*> nodes;
		nodes.push_back(root);
		nodes_set.insert(root);
		nodes_map[root->label] = root;
		for (size_t i = 0; i < nodes.size(); ++i) {
			for (size_t j = 0; j < nodes[i]->neighbors.size(); ++j) {
				UndirectedGraphNode* n_node = nodes[i]->neighbors[j];
				if (nodes_set.find(n_node) == nodes_set.end()) {
					nodes_set.insert(n_node);
					nodes.push_back(n_node);
					nodes_map[n_node->label] = n_node;
				}
			}
		}

		// map的key从小到大，逐个输出节点
		for (map<int, UndirectedGraphNode*>::iterator it = nodes_map.begin();
				it != nodes_map.end(); ++it) {
			UndirectedGraphNode* node = it->second;
			if (it != nodes_map.begin()) {
				printf(",[%d", node->label);
			} else {
				printf("[%d", node->label);
			}
			for (size_t j = 0; j < node->neighbors.size(); ++j) {
				printf(",%d", node->neighbors[j]->label);
			}
			printf("%s", "]");
		}
	}
	printf("%s", "}");
}

int main()
{
	// {1,2,3,#,#,4,#,#,5}
    TreeNode* node1 = new TreeNode(1);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node3 = new TreeNode(3);
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node5 = new TreeNode(5);
    node1->left = node2;
    node1->right = node3;
    node3->left = node4;
    node4->right = node5;
    PrintTree(node1);
	printf("\n");

	// {[1,2,3,#,#,4,#,#,5],[#,3,#,#,#]}
    TreeLinkNode* tlnode1 = new TreeLinkNode(1);
    TreeLinkNode* tlnode2 = new TreeLinkNode(2);
    TreeLinkNode* tlnode3 = new TreeLinkNode(3);
    TreeLinkNode* tlnode4 = new TreeLinkNode(4);
    TreeLinkNode* tlnode5 = new TreeLinkNode(5);
    tlnode1->left = tlnode2;
    tlnode1->right = tlnode3;
    tlnode3->left = tlnode4;
    tlnode4->right = tlnode5;
	tlnode2->next = tlnode3;
	PrintTreeLinkNode(tlnode1);
	printf("\n");

	// { -1, 8, 7, -3,4, 4,-3,#,#,8}
	RandomListNode* rlnode1 = new RandomListNode(-1);
	RandomListNode* rlnode2 = new RandomListNode(8);
	RandomListNode* rlnode3 = new RandomListNode(7);
	RandomListNode* rlnode4 = new RandomListNode(-3);
	RandomListNode* rlnode5 = new RandomListNode(4);
	rlnode1->next = rlnode2;
	rlnode2->next = rlnode3;
	rlnode3->next = rlnode4;
	rlnode4->next = rlnode5;
	rlnode1->random = rlnode5;
	rlnode2->random = rlnode4;
	rlnode5->random = rlnode2;
	PrintRandomListNode(rlnode1);
	printf("\n");

	//{[0,1],[1,2],[2,2]}
	UndirectedGraphNode* ugn1 = new UndirectedGraphNode(0);
	UndirectedGraphNode* ugn2 = new UndirectedGraphNode(1);
	UndirectedGraphNode* ugn3 = new UndirectedGraphNode(2);
	ugn1->neighbors.push_back(ugn2);
	ugn2->neighbors.push_back(ugn3);
	ugn3->neighbors.push_back(ugn3);
	PrintUndirectedGraphNode(ugn1);
    return 0;
}

```











