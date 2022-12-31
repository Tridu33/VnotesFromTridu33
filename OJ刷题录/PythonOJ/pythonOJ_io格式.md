

# pythonOJ格式


[入门](https://blog.csdn.net/weixin_41687289/article/details/79936020)



```

2016级程序设计基础一(2017春季上)(140)
实验1---顺序结构程序设计(17) 
全部用python写完。
实验2----选择结构程序设计(16)
全部用python写完。 
实验3----while 循环结构程序设计(10)
全部用python写完。更新时间(2018.4.17)




#print怎么输出后不换行？
print(待输出,end = '')
#python是允许这样赋值的
a,b,c = 1,2,3
print(a,b,c)
#python玩acm读取输入应该这么干
a,b,c = input().strip().split()#其实strip()可有可无
print(a,b,c)
#strip('可选字符，默认为空格')的用处：去掉字符串首位连续的某字符
#split('可选指定分隔符',可选分割次数)的用法：通过分隔符将字符串切片处理
#注意，python的格式控制是这样的。
print(a+b+c,a*b*c,"{:.2f}".format((a+b+c)/3))
#也是这样的
print("{}\n{}\n{:.6f}".format(100,'A',3.14))
print("{:02d}:{:02d}:{:02d}".format(timeA,timeB,timeC))
#d代表输出int，2代表输出宽度，0代表剩余位用0来填充。
01:08:31

#如果你想在字符串中表示\  请用"\\"  转义


像我这样的彩笔大概是这样搞数组的。。
s = input().split()
j = 0
for i in s:
	s[j] = int(i)
	j += 1
#########补充，像我这样的大彩笔是这样搞的。。
for i in s:
	sum += int(i)
####捂脸
for i in range(len(s)):
	s[i] = (int)s[i]

print(das,das,fds,gfd,sep='分隔子列',end = '结束子列',
file = '文件位置')


```

在python中,int非常的大,而float倒没有那么的大,因此在float转换成int的过
程中,会出现int too large to convert to float错误.
传送门:http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Index/problemdetail/pid/1194.html


```
ac代码:
while True:
    sum = 1
    x,n = input().split()
    x,n = float(x),int(n)
    for i in range(1,n+1):
        fenmu = 1.0#将之设置成1.0 从一开始就让他是float
        for j in range(2,2*i+1):
            fenmu *= j
        sum += ((-1)**i)*(x**(2.0*i))/fenmu#保证每个运算的量都是float
    print('%.4f' %sum)
在用python进行浮点运算时,一定要注意,避免int自动转换为float.
我们最好一开始就用float

# python多组输入应该这么干：
def solution():
    while True:
        try:
            n = int(input())
        except:
            break
solution()

```








# 输入输出







[ACM八大输入输出格式之Python版https://blog.csdn.net/u013595779/article/details/40860323](https://blog.csdn.net/u013595779/article/details/40860323)




```python
# encoding: utf-8
 
'''
Created on Nov 6th, 2014
@author: Speedcell
'''
 
'''
Python的输入是野生字符串，所以要自己转类型
strip去掉左右两端的空白符，返回str
slipt把字符串按空白符拆开，返回[str]
map把list里面的值映射到指定类型，返回[type]
EOF用抓异常
print后面加逗号就不会换行，否则反之，当然3.x君自行传参
题目细节没看太细，可能有的地方不对，不要在意这些细节啦
これは以上です
'''
 
# 有多组输入数据，但没有具体的告诉你有多少组，只是让你对应每组输入，应该怎样输出。
 
while True:
    try:
        a, b = map(int, raw_input().strip().split())
        print a + b,
    except EOFError:
        break
    
# 输入一个整数，告诉我们接下来有多少组数据，然后在输入每组数据的具体值。
 
tcase = int(raw_input().strip())
for case in range(tcase):
    a, b = map(int, raw_input().strip().split())
    print a + b,
    
# 有多组输入数据，没有具体的告诉你有多少组,但是题目却告诉你遇见什么结束
 
while True:
    a, b = map(int, raw_input().strip().split())
    if a == 0 and b == 0:
        break
    print a + b,
    
# 输入有多组，并却题目告诉你每组输入遇见什么结束，与第三种不同之处在于，每组输入都有相应的细化。
    
tcase = int(raw_input().strip())
for case in range(tcase):
    a, b = map(int, raw_input().strip().split())
    if a == 0 and b == 0:
        break
    print a + b,
    
# 这次的输入实现输入一个整数，告诉我们有多少行，在输入每一行。对于每一行的输入，有划分为第一个数和其他的数，第一个数代表那一组数据一共有多少输入。
 
tcase = int(raw_input().strip())
for case in range(tcase):
    data = map(int, raw_input().strip().split())
    n, array = data[0], data[1:]
    
    sum = 0
    for i in range(n):
        sum += array[i]
    print sum,
    
# 有多种输入数据，对于每组输入数据的第一个数代表该组数据接下来要输入数据量
 
while True:
    try:
        data = map(int, raw_input().strip().split())
        n, array = data[0], data[1:]
            
        sum = 0
        for i in range(n):
            sum += array[i]
        print sum,
    except EOFError:
        raise
    
# 这道题的输出只是简单的在每组输出后边多加一个换行而已！
 
while True:
    try:
        a, b = map(int, raw_input().strip().split())
        print a + b
    except EOFError:
        break
    
# 这种类型的输出注意的就是换行，这类题目说在输出样例中，每组样例之间有什么什么，所以我们在对应输出的同时要判断一下是否是最后一组输出，如果不是，就 将题目所说的东西输出（一般是换行或空格），如果是，就直接结束。
 
while True:
    data = raw_input().strip()
    if data.isspace():
        break
    else:
        data = map(int, data)
        n, array = data[0], data[1:]
                
        sum = 0
        for i in range(n):
            sum += array[i]
        print sum,
```




















[如何优雅地使用Python做OJ题https://www.zybuluo.com/diyer22/note/310572](https://www.zybuluo.com/diyer22/note/310572)


有哪些适合Python新手练习的OJ？ - Jasin Yip的回答 - 知乎 https://www.zhihu.com/question/25523815/answer/30998035












































