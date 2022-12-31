# Vector









随着C++11标准的出现，C++标准添加了许多有用的特性，C++代码的写法也有比较多的变化。
 
vector是经常要使用到的std组件，对于vector的遍历，本文罗列了若干种写法。
 
（注：本文中代码为C++11的代码，需要在较新的编译器中编译运行）
 
假设有这样的一个vector：
 
vector<int> valList = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
需要输出这个vector中的每个元素，原型如下：
 
void ShowVec(const vector<int>& valList)
{
}
int main(int argc, char* argv[])
{
    vector<int> valList = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    ShowVec(valList);
    return 0;
}
 
 
 
 
 
方法零，对C念念不舍的童鞋们习惯的写法：(c++ 98/03 ,c++ 11 通用)
 ```

void ShowVec(const vector<int>& valList)
{
    int count = valList.size();
    for (int i = 0; i < count;i++)
    {
        cout << valList[i] << endl;
    }
}
 ```
 
 
方法一，大家喜闻乐见的for循环迭代器输出：(c++ 98/03 ,c++ 11 通用)
 
```
void ShowVec(const vector<int>& valList)
{
    for (vector<int>::const_iterator iter = valList.cbegin(); iter != valList.cend(); iter++)
    {
        cout << (*iter) << endl;
    }
}
```
 
 
方法二，与方法一差不多，不过能少打几个字：(仅c++ 11 可用)
 
```
void ShowVec(const vector<int>& valList)
{
    for (auto iter = valList.cbegin(); iter != valList.cend(); iter++)
    {
        cout << (*iter) << endl;
    }
}
```
 
 
方法三，for_each加函数：(c++ 98/03 ,c++ 11 通用)
 
```
template<typename T>
void printer(const T& val)
{
    cout << val << endl;
}
void ShowVec(const vector<int>& valList)
{
    for_each(valList.cbegin(), valList.cend(), printer<int>);
}
```
 
 
方法四，for_each加仿函数：(c++ 98/03 ,c++ 11 通用)
 ```
 
template<typename T>
struct functor
{
    void operator()(const T& obj)
    {
        cout << obj << endl;
    }
};
void ShowVec(const vector<int>& valList)
{
    for_each(valList.cbegin(), valList.cend(), functor<int>());
}
 
 ```
 
方法五，for_each加Lambda函数：(仅c++ 11 可用)
 
```
void ShowVec(const vector<int>& valList)
{
    for_each(valList.cbegin(), valList.cend(), [](const int& val)->void{cout << val << endl; });
}
 
```

方法六，for区间遍历：(仅c++ 11 可用)
 
`for (auto val : valList)
{
    cout << val << endl;
}`

C++11相比C++98/03还是更新了挺多东西的，目前g++最新版已完全支持C++11标准，这意味着开源社区的新的project必然将迁移到最新的C++11标准上，平时参与/阅读/参考开源代码的童鞋们需要学习了。



