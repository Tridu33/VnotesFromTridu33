

# Yield解决回溯模板问题参考subset.py代码

https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html

回溯算法框架：


```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
C(6,4)问题，除了上面列出的十个步骤，我们换个思路：

　　　　
**求组合**问题

https://www.cnblogs.com/vipchenwei/p/7147488.html 
如果在6个数中选定一个数，那么确定剩下的3个数是不是变为了“从5个数中选3个数的组合问题”了呢？以此类推，这似乎变成了一个“递归”问题了，确实，我们可以用递归的思路来解决这个问题。

```
def combNumber(m, n, b):
    global totalNumberR
    for i in range(m, n-1, -1):   
        b[n-1] = i
        if n-1>0:
            combNumber(i-1,n-1,b)
        else:
            print b
            totalNumberR += 1
    return totalNumberR

 

group=[99,99,99,99,99]
totalNumberR = 0
print "\nUsing Recursive: %d\n" % combNumber(7,5,group)　
```

python提供的内置组合函数


```
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
```










**求子集**算法-循环、递归、回溯、位运算 - 翩翩少年的文章 - 知乎
https://zhuanlan.zhihu.com/p/347663905

```
nums = [1,2,3]
def subset(nums):
    def backtrack(first=0, curr=[]):
        ## 递归函数的出口
        if len(curr) == k:
            res.append(curr[:])
        ## 设计递归函数结构
        for i in range(first, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    res = []
    for k in range(len(nums) + 1):
        # 计算每一类的子集
        backtrack()
    return res
```


```
def PowerSetsBinary(items):
    N = len(items)
    # generate all combination of N items
    # enumerate the 2**N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):  # jth bit of Integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

```

 yield_subset https://stackoverflow.com/questions/8711596/python-3-s-for-s-in-subsetss-and-yield



# 各种语言组件趋同


语法特性互相抄袭，coroutine已广为推行。


底层全是class的OOP设计思路的java坦白说没有模仿scheme的javascript灵活，特别是纯函数方面，比如把CPS的fib函数翻译为java代码很头痛，js则不会，直接等效写法。



```scheme
(define fib-cps
  (lambda (n k)
    (cond
     ((< n 0) (k #f))
     ((= n 0) (k 0))
     ((= n 1) (k 1))
     (else
      (fib-cps (- n 1)
           (lambda (n1)
              (fib-cps (- n 2) (lambda (n2) (k (+ n1 n2))))))))))
```


但是也不是没有挽救余地，毕竟c生万物，计算等价性总是可以模拟出来的，实在不行java包一层上层支持该语法特性的DSL，编译到java即可。正如ES6是web时代的汇编语言。
python yield equivalent in java https://juejin.cn/s/python%20yield%20equivalent%20in%20java















------------


Scheme 的 call/cc - include-yy的文章 - 知乎
https://zhuanlan.zhihu.com/p/180473795
说到回溯，有一个运算符与它有着紧密的联系，那就是 amb 。amb 是 ambiguous 的一个缩写，它用于非确定性计算。
参考资料【7】对 amb 进行了描述：amb 接收一个或多个表达式，并在它们中进行一次非确定选择，这个选择使得程序趋向于有意义。不带参数调用 amb 不会有返回值并会出错。





























