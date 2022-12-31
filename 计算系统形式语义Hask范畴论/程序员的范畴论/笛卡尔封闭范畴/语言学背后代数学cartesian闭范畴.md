
# cartesian 闭范畴






语言背后的代数学（九）：笛卡尔闭范畴 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/35281476



--------------------------------------------------





语言背后的代数学（一）：语义解释 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/34977830



语言背后的代数学（二）：初等代数 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/35017879





语言背后的代数学（五）：Σ代数 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/35142819
可以用来解释带有类型签名的项。




语言背后的代数学（六）：Henkin模型 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/35170799



递归函数（九）：最小不动点定理 - 何幻的文章 - 知乎
https://zhuanlan.zhihu.com/p/34604220







**完全偏序集上的连续函数具有最小不动点**，这称之为最小不动点定理




如果$D,\neq$是一个完全偏序集，且 $f:D\rightarrow D$ 是连续的，
则 f 有最小不动点，$f_ix_Df= \bigwedge\{f^n(\bottom)|n>0\}$ 。



fact = fix g


阶乘函数fact是以下函数的不动点



```haskell
g :: (Int -> Int) -> Int -> Int
g f n = case n of
  1 -> 1
  _ -> n * f (n-1)


```








