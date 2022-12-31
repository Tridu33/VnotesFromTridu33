



# Haskell运算符全解






https://krantz-xrf.github.io/2020/10/09/haskell-operators.html

Haskell运算符全解 - Monad的文章 - 知乎
https://zhuanlan.zhihu.com/p/263797220



# 整理

Hoogle 在线查询也可以，`:k :t :f `也可以

双冒号`::` 可以用它来“投”function到你想要的版本; 例如，如果一个函数是“多态的”（有一个普通的types签名），而且实际上你想要一个Integer ，那么你可以对整个值进行:: Integer 



比如：
```haskell
Prelude> :t pure
pure :: Applicative f => a -> f a
Prelude> :t pure "hello" >>= putStrLn
pure "hello" >>= putStrLn :: IO ()
比如可以指定IO Int或者Maybe Int 不同实际类型，因为多态没，还没确定instance怎么用
Prelude> :t traverse (pure:: Int -> IO Int) [1,2,3,4,5]
traverse (pure:: Int -> IO Int) [1,2,3,4,5] :: IO [Int]
Prelude> :t traverse (pure:: Int -> Maybe Int) [1,2,3,4,5]
traverse (pure:: Int -> Maybe Int) [1,2,3,4,5] :: Maybe [Int]

Prelude> :t traverse (pure) [1,2,3,4,5]
traverse (pure) [1,2,3,4,5] :: (Applicative f, Num b) => f [b]
默认转换为IO Int所以打印出来没区别
Prelude> traverse (pure:: Int -> IO Int) [1,2,3,4,5]
[1,2,3,4,5]
Prelude> traverse (pure) [1,2,3,4,5]
[1,2,3,4,5]

```

















