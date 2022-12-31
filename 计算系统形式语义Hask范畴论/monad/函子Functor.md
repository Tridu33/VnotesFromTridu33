|          | 函数                               | 功能                       | 类型                     |
| -------- | ---------------------------------- | -------------------------- | ------------------------ |
| 函子     | `fmap`                             | 将函数应用到带有上下文的值 | `(a -> b) -> f a -> f b` |
| 应用函子 | `pure`                             | 添加最小上下文             | `a -> f a`               |
| `<$>`    | 中缀版`fmap`                       | `(a -> b) -> f a -> f b`   |                          |
| `<*>`    | 将上下文中的函数应用到上下文中的值 | `f (a -> b) -> f a -> f b` |                          |
| 单子     | `return`                           | 添加最小上下文             | `a -> m a`               |
| `>>=`    | 连接单子运算                       | `m a -> (a -> m b) -> m b` |                          |
| `>>`     | 连接单子                           | `m a -> m b -> m b`        |                          |
| `fail`   | 失败函数                           | `String -> m a`            |                          |

https://www.w3cschool.cn/hsriti/hsriti-rzg43l3l.html



# 函子Functor


函子(representative functor)是范畴论里的概念，指从任意范畴到集合范畴的一种特殊函子。（yoneda lemma）




函子（Functor、Pointed、Maybe、Either、Monad、IO、Ap） - amanisky的文章 - 知乎
https://zhuanlan.zhihu.com/p/269513973


# 函子->应用函子->单子

群里讨论：
https://stackoverflow.com/questions/7460809/can-someone-explain-the-traverse-function-in-haskell

```haskell
Prelude> :t traverse pure [1,2,3,4,5]
traverse pure [1,2,3,4,5] :: (Applicative f, Num b) => f [b]
```

```haskell


Prelude> :t traverse
traverse
  :: (Traversable t, Applicative f) => (a -> f b) -> t a -> f (t b)
Prelude> :t putStrLn
putStrLn :: String -> IO ()

Prelude>  :t traverse (:[]) [1,2,3]
traverse (:[]) [1,2,3] :: Num b => [[b]]


```
群友讨论到：

> :t 不会跑 所以是f 
去掉:t就是在ghci下就会是IO
去掉:t 从结果看是看不出区别的。
默认有个转IO的操作


```haskell
Prelude> :t pure
pure :: Applicative f => a -> f a
Prelude> :t pure "hello" >>= putStrLn
pure "hello" >>= putStrLn :: IO ()

Prelude> :t traverse (pure:: Int -> IO Int) [1,2,3,4,5]
traverse (pure:: Int -> IO Int) [1,2,3,4,5] :: IO [Int]
Prelude> :t traverse (pure:: Int -> Maybe Int) [1,2,3,4,5]
traverse (pure:: Int -> Maybe Int) [1,2,3,4,5] :: Maybe [Int]

Prelude> :t traverse (pure) [1,2,3,4,5]
traverse (pure) [1,2,3,4,5] :: (Applicative f, Num b) => f [b]
Prelude> traverse (pure:: Int -> IO Int) [1,2,3,4,5]
[1,2,3,4,5]
Prelude> traverse (pure) [1,2,3,4,5]
[1,2,3,4,5]
```













-------------


https://blog.tonycrane.cc/p/290ecb74.html 翻译

韩冬的书和github例章

Haskell中的范畴之函子和自然变换 - parker liu的文章 - 知乎
https://zhuanlan.zhihu.com/p/25565309





函子才是Haskell的精髓 - 脚趾头的文章 - 知乎
https://zhuanlan.zhihu.com/p/353764293











函数式编程进阶：JS应用函子 - 云音乐前端技术团队的文章 - 知乎 https://zhuanlan.zhihu.com/p/275686659





























