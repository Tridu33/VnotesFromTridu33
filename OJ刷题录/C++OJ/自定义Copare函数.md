









# 自定义Copare函数


## sort中


435区间调度三元组leecode题解官方有匿名函数写法例子


```
```





neewcoder官方题解有整理好的：

https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11184&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey

数组排列成最小的数字字符拼接串

```
class Solution {
private:
        bool static comstatic(string a, string b) {
            return a + b < b + a;
        }
        //加static的原因：类成员函数有隐藏的this指针,static 可以去this指针
        struct Com {
            bool operator() (string a, string b) {
             return a + b < b + a;
            }
        };

public:
    string PrintMinNumber(vector<int> nums) {
        vector<string> res;
        for(auto x:nums){
            res.push_back(to_string(x));
        }
        
        // 1. 匿名lambda表达式
//         sort(res.begin(),res.end(),[](string a,string b){
//             return a+b < b+a;
//         });
        
        // 2.具名lambda表达式
//         auto lam = [](string a, string b) {
//              return a + b < b + a;
//          };
//         sort(res.begin(), res.end(), lam);
        
        // 函数指针
        //sort(res.begin(), res.end(), comstatic);
        string  ret;
        
        // 仿函数
        sort(res.begin(), res.end(), Com()); // Com()为临时对象
        for(auto s: res){
            ret+= s;
        }
        return ret;
    }
};
```













## priority_queue中

```cpp
// 优先队列
private:
    struct cmp{
        bool operator()(const int &a,const int &b){
            return a<b;
        };
    };
public:
    int main(){
        priority_queue<int,vector<int> ,cmp > q;
    }
```





































