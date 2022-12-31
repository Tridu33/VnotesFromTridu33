





# c++位运算bitset





https://labuladong.github.io/algo/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BD%8D%E6%93%8D%E4%BD%9C.html 常用位运算操作




```n&(n-1)``` 这个操作是算法中常见的，作用是消除数字 n 的二进制表示中的最后一个 1。同时把其后的 0 都变成 1，这样再和 n 做一次 & 运算，就可以仅仅把最后一个 1 变成 0 了。














利用或操作 | 和空格将英文字符转换为小写
```
('a' | ' ') = 'a'
('A' | ' ') = 'a'
```
利用与操作 & 和下划线将英文字符转换为大写
```
('b' & '_') = 'B'
('B' & '_') = 'B'
```
利用异或操作 ^ 和空格进行英文字符大小写互换
```
('d' ^ ' ') = 'D'
('D' ^ ' ') = 'd'
```
以上操作能够产生奇特效果的原因在于 ASCII 编码。字符其实就是数字，恰巧这些字符对应的数字通过位运算就能得到正确的结果，有兴趣的读者可以查 ASCII 码表自己算算，本文就不展开讲了。

判断两个数是否异号
```
int x = -1, y = 2;
bool f = ((x ^ y) < 0); // true

int x = 3, y = 2;
bool f = ((x ^ y) < 0); // false
```
这个技巧还是很实用的，利用的是补码编码的符号位。如果不用位运算来判断是否异号，需要使用 if else 分支，还挺麻烦的。读者可能想利用乘积或者商来判断两个数是否异号，但是这种处理方式可能造成溢出，从而出现错误。

不用临时变量交换两个数
```
int a = 1, b = 2;
a ^= b;
b ^= a;
a ^= b;
// 现在 a = 2, b = 1
```
加一
```
int n = 1;
n = -~n;
// 现在 n = 2
```
减一
```
int n = 2;
n = ~-n;
// 现在 n = 1
```
PS：上面这三个操作就纯属装逼用的，没啥实际用处，大家了解了解乐呵一下就行。












GlassHour
C/C++位运算技巧
位运算加速技巧
1. 如果乘上一个2的倍数数值，可以改用左移运算(Left Shift) 加速 300%

```
x = x * 2;
x = x * 64;
//改为:
x = x << 1; // 2 = 21
x = x << 6; // 64 = 26
```

2. 如果除上一个 2 的倍数数值，可以改用右移运算加速 350%

```
x = x / 2;
x = x / 64;
//改为:

x = x >> 1;// 2 = 21
x = x >> 6;// 64 = 26
```

3. 数值转整数加速 10%

```
x = int(1.232)
//改为:

x = 1.232 >> 0;
```

4. 交换两个数值(swap)，使用 XOR 可以加速20%

```
var t:int = a;
a = b;
b = t;
//equals:
a = a^b;
b = a^b;
a = a^b;
```

5. 正负号转换，可以加入 300%

```
i = -i;
//改为
i = ~i + 1; // NOT 写法
//或
i = (i ^ -1) + 1; // XOR 写法
```

6. 取余数，如果除数为 2 的倍数，可利用 AND 运算加速 600%

```
x = 131 % 4;
//equals:
x = 131 & (4 - 1);
```

7. 利用 AND 运算检查整数是否为 2 的倍数，可以加速 600%

```
isEven = (i % 2) == 0;
//equals:
isEven = (i & 1) == 0;
```

8. 加速 Math.abs 600% 的写法1，写法2 又比写法1加速 20%

```
//写法1
i = x < 0 ? -x : x;

//写法2

i = (x ^ (x >> 31)) - (x >> 31);

//写法3

i=x^(~(x>>31)+1)+(x>>31);
```

9. 比较两数值相乘之后是否拥有相同的符号，加速 35%

```
eqSign = a * b > 0;
//equals:
eqSign = a ^ b > 0;
```

其它位运算技巧
1. RGB 色彩分离

```
var 24bitColor:uint = 0xff00cc;
var r:uint = 24bitColor >> 16;
var g:uint = 24bitColor >> 8 & 0xFF;
var b:uint = 24bitColor & 0xFF;
```

2. RGB 色彩合并

```
var r:uint = 0xff;
var g:uint = 0x00;
var b:uint = 0xcc;
var 24bitColor:uint = r << 16 | g << 8 | b;

```







位运算有什么奇技淫巧？ - 力扣（LeetCode）的回答 - 知乎
https://www.zhihu.com/question/38206659/answer/736472332


1 位逻辑运算符：

```
      & （位   “与”）  and
      ^  （位   “异或”）
      |   （位    “或”）   or
      ~  （位   “取反”）
```
2 移位运算符：
```
      <<（左移）
      >>（右移）
```

优先级
位“与”、位“或”和位“异或”运算符都是双目运算符，其结合性都是从左向右的，优先级高于逻辑运算符，低于比较运算符，且从高到低依次为&、^、| 

c++位运算符 | & ^ ~ && ||,补码，反码 


bitset 有许多成员函数，有些成员函数执行的就是类似于位运算的操作。





bitset 成员函数列表如下：

```
bitset <N> & operator &= (const bitset <N> & rhs);  //和另一个 bitset 对象进行与操作
bitset <N> & operator |= (const bitset <N> & rhs);  //和另一个 bitset 对象进行或操作
bitset <N> & operator ^= (const bitset <N> & rhs);  //和另一个 bitset 对象进行异或操作
bitset <N> & operator <<= (size_t num);  //左移 num 位
bitset <N> & operator >>= (size_t num);  //右移 num 位
bitset <N> & set();  //将所有位全部设成 1
bitset <N> & set(size_t pos, bool val = true);  //将第 pos 位设为 val
bitset <N> & reset();  //将所有位全部设成0
bitset <N> & reset (size_t pos);  //将第 pos 位设成 0
bitset <N> & flip();  //将所有位翻转（0变成1，1变成0）
bitset <N> & flip(size_t pos);  //翻转第 pos 位
reference operator[] (size_t pos);  //返回对第 pos 位的引用
bool operator[] (size_t pos) const;  //返回第 pos 位的值
reference at(size_t pos);  //返回对第 pos 位的引用
bool at (size_t pos) const;  //返回第 pos 位的值
unsigned long to_ulong() const;  //将对象中的0、1串转换成整数
string to_string () const;  //将对象中的0、1串转换成字符串（Visual Studio 支持，Dev C++ 不支持）
size_t count() const;  //计算 1 的个数
size_t size () const;  //返回总位数
bool operator == (const bitset <N> & rhs) const;
bool operator != (const bitset <N> & rhs) const;
bool test(size_t pos) const;  //测试第 pos 位是否为 1
bool any() const;  //判断是否有某位为1
bool none() const;  //判断是否全部为0
bitset <N> operator << (size_t pos) const;  //返回左移 pos 位后的结果
bitset <N> operator >> (size_t pos) const;  //返回右移 pos 位后的结果
bitset <N> operator ~ ();  //返回取反后的结果
bitset <N> operator & (const bitset <N> & rhs) const;  //返回和另一个 bitset 对象 rhs 进行与运算的结果
bitset <N> operator | (const bitset <N> & rhs) const;  //返回和另一个 bitset 对象 rhs 进行或运算的结果
bitset <N> operator ^ (const bitset <N> & rhs) const;  //返回和另一个 bitset 对象 rhs 进行异或运算的结果
```



