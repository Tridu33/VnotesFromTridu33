







# 1. 题目
[Leetcode][动态规划]相关题目汇总/分析/总结 - 后端技术漫谈的文章 - 知乎
https://zhuanlan.zhihu.com/p/35707293


70


121



5





1143





 LeeCode动态规划

[https://www.bilibili.com/video/BV1SE41157mS](https://www.bilibili.com/video/BV1SE41157mS)


 动态规划专题班

[https://www.bilibili.com/video/BV1xb411e7ww](https://www.bilibili.com/video/BV1xb411e7ww)


 acm专题B站动态规划





[https://www.bilibili.com/video/BV1VW411Q7kw](https://www.bilibili.com/video/BV1VW411Q7kw)



https://blog.csdn.net/fjsd155/article/details/88833701 动态规划类型们：

[一、资源型](https://blog.csdn.net/fjsd155/article/details/88833701#t0)

[01背包](https://blog.csdn.net/fjsd155/article/details/88833701#t1)

[完全背包](https://blog.csdn.net/fjsd155/article/details/88833701#t2)

[多重背包](https://blog.csdn.net/fjsd155/article/details/88833701#t3)

[二维费用背包](https://blog.csdn.net/fjsd155/article/details/88833701#t4)

[分组背包](https://blog.csdn.net/fjsd155/article/details/88833701#t5)

[有依赖的背包](https://blog.csdn.net/fjsd155/article/details/88833701#t6)

[泛化物品](https://blog.csdn.net/fjsd155/article/details/88833701#t7)

[背包问题的经典变形](https://blog.csdn.net/fjsd155/article/details/88833701#t8)

[背包问题的搜索方法](https://blog.csdn.net/fjsd155/article/details/88833701#t9)

[崔天翼大牛推荐的相关题目（USACO）](https://blog.csdn.net/fjsd155/article/details/88833701#t10)

[其他](https://blog.csdn.net/fjsd155/article/details/88833701#t11)

[二、线性动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t12)

[三、区间动态规划（剖分问题）](https://blog.csdn.net/fjsd155/article/details/88833701#t13)

[四、坐标动态规划（平面、地图）](https://blog.csdn.net/fjsd155/article/details/88833701#t14)

[五、树型动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t15)

[六、字符串动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t16)

[七、贪心动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t17)

[八、多进程动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t18)

[九、状压动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t19)

[十、判定型动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t20)

[十一、目标型动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t21)

[十二、概率动态规划](https://blog.csdn.net/fjsd155/article/details/88833701#t22)

[十三、二次动态规划（双重动态规划）](https://blog.csdn.net/fjsd155/article/details/88833701#t23)

[十四、递推问题](https://blog.csdn.net/fjsd155/article/details/88833701#t24)

[十五、计数问题](https://blog.csdn.net/fjsd155/article/details/88833701#t25)


# 2. 解题模板


https://charon.me/posts/leetcode/dp/  Dynamic Programming

动态规划之初识动规：有了四步解题法模板，再也不害怕动态规划！ - 程序员吴师兄的文章 - 知乎
https://zhuanlan.zhihu.com/p/91680256

**动态规划**算法是通过拆分问题，定义问题状态和状态之间的关系，使得问题能够以递推（或者说分治）的方式去解决。它的几个重要概念如下所述。

**阶段：**对于一个完整的问题过程，适当的切分为若干个相互联系的子问题，每次在求解一个子问题，则对应一个阶段，整个问题的求解转化为按照阶段次序去求解。

**状态：**状态表示每个阶段开始时所处的客观条件，即在求解子问题时的已知条件。状态描述了研究的问题过程中的状况。

**决策：**决策表示当求解过程处于某一阶段的某一状态时，可以根据当前条件作出不同的选择，从而确定下一个阶段的状态，这种选择称为决策。

**策略：**由所有阶段的决策组成的决策序列称为全过程策略，简称策略。

**最优策略：**在所有的策略中，找到代价最小，性能最优的策略，此策略称为最优策略。

**状态转移方程：**状态转移方程是确定两个相邻阶段状态的演变过程，描述了状态之间是如何演变的。

## 2.1. 思考动态规划问题的四个步骤




动态规划模板 DP https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-mo-ban-dp-by-wohaiyo/



```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化数组为 amount + 1，便于取 min
        dp = [amount+1] * (amount+1)
        # 最基本case
        dp[0] = 0
        # 自底向上
        for i in range(amount+1):
            # 根据每个***，求解可能性
            for c in coins:
                if i - c < 0: continue
                dp[i] = min(dp[i], 1+dp[i-c])
        if dp[i] < amount + 1:
            return dp[amount]
        return -1


```



一般解决动态规划问题，分为四个步骤，分别是

- 问题拆解，找到问题之间的具体联系
- 状态定义
- 递推方程推导
- 实现




https://labuladong.github.io/algo/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.html




首先，动态规划问题的一般形式就是求最值。动态规划其实是运筹学的一种最优化方法，只不过在计算机问题上应用比较多，比如说让你求最长递增子序列呀，最小编辑距离呀等等。

既然是要求最值，核心问题是什么呢？求解动态规划的核心问题是穷举。因为要求最值，肯定要把所有可行的答案穷举出来，然后在其中找最值呗。



首先，动态规划的穷举有点特别，因为这类问题存在「重叠子问题」，如果暴力穷举的话效率会极其低下，所以需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算。

而且，动态规划问题一定会具备「**最优子结构**」，才能通过子问题的最值得到原问题的最值。

另外，虽然动态规划的核心思想就是穷举求最值，但是问题可以千变万化，穷举所有可行解其实并不是一件容易的事，只有列出正确的「状态转移方程」才能正确地穷举。


以上提到的重叠子问题、最优子结构、状态转移方程就是动态规划三要素。具体什么意思等会会举例详解，但是在实际的算法问题中，写出状态转移方程是最困难的，这也就是为什么很多朋友觉得动态规划问题困难的原因，我来提供我研究出来的一个思维框架，辅助你思考状态转移方程：

明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。



```
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
```


下面通过斐波那契数列问题和凑零钱问题来详解动态规划的基本原理。前者主要是让你明白什么是**重叠子问题**（斐波那契数列没有求最值，所以严格来说不是动态规划问题），后者主要举集中于如何列出**状态转移方程**。

```
int fib(int N) {
    if (N < 1) return 0;
    // 备忘录全初始化为 0
    vector<int> memo(N + 1, 0);
    // 进行带备忘录的递归
    return helper(memo, N);
}

int helper(vector<int>& memo, int n) {
    // base case
    if (n == 1 || n == 2) return 1;
    // 已经计算过
    if (memo[n] != 0) return memo[n];
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2);
    return memo[n];
}
```

找零钱


根据我们文章开头给出的动态规划代码框架可以写出如下解法：

```
int coinChange(vector<int>& coins, int amount) {
    // 数组大小为 amount + 1，初始值也为 amount + 1
    vector<int> dp(amount + 1, amount + 1);
    // base case
    dp[0] = 0;
    // 外层 for 循环在遍历所有状态的所有取值
    for (int i = 0; i < dp.size(); i++) {
        // 内层 for 循环在求所有选择的最小值
        for (int coin : coins) {
            // 子问题无解，跳过
            if (i - coin < 0) continue;
            dp[i] = min(dp[i], 1 + dp[i - coin]);
        }
    }
    return (dp[amount] == amount + 1) ? -1 : dp[amount];
}
```
你会发现，上面的几种解法中的所有操作，例如 return f(n - 1) + f(n - 2)，dp[i] = dp[i - 1] + dp[i - 2]，以及对备忘录或 DP table 的初始化操作，都是围绕这个方程式的不同表现形式。可见列出「状态转移方程」的重要性，它是解决问题的核心。而且很容易发现，其实状态转移方程直接代表着暴力解法。

千万不要看不起暴力解，动态规划问题最困难的就是写出这个暴力解，即状态转移方程。只要写出暴力解，优化方法无非是用备忘录或者 DP table，再无奥妙可言。


计算机解决问题其实没有任何奇技淫巧，它唯一的解决办法就是**穷举**，穷举所有可能性。算法设计无非就是先思考“如何穷举”，然后再追求“如何聪明地穷举”。




























































