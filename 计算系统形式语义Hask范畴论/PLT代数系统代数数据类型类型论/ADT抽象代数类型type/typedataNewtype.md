# 1. typedataNewtype



https://segmentfault.com/a/1190000004646702

type 用来为一个已有类型声明别名。
data 用来定义新的数据类型，可以有任意个值构造器。
newtype 用来封装已有的数据类型，只能有一个值构造器，速度比 data 快。


type


```haskell
type BookId = Int
type BookSummary = String
type BookRecord = (BookId, BookSummary)
```

data

data 关键字用来创建新的数据类型，有「类型构造器」 和 「值构造器」，它们的名字可以是相同的，也可以是不同的。
其中，有一个以上「值构造器」的数据类型称为 「代数数据类型（algebraic data type）」。
```haskell
-- BookInfo 是类型构造器
-- Book 是值构造器data constructor 
-- ghci> Book 1 "Hello" :: BookInfo
data BookInfo = Book Int String deriving (Show)

-- 左边的 Book 是类型构造器
-- 右边的 Book 是值构造器
-- ghci> Book 1 "World" :: Book
data Book = Book Int String deriving (Show)

-- Tree a 是代数数据类型
-- a 是类型参数，表示任意类型
-- Empty 和 Node 都是值构造器
-- ghci> Empty :: Tree a
-- ghci> Node 1 (Empty) (Empty) :: Num a => Tree a
-- ghci> Node "Hello" Empty (Node "World" (Empty) (Empty)) :: Tree [Char]
data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show)
```

data 支持用 Record Syntax 来创建数据类型，用 Record Syntax 生成数据类型的同时会生成一些 getter 函数。

```haskell
data Person = Person {
    name :: String,
    age :: Int,
    height :: Float
} deriving (Show)

-- 自动生成下面这些 getter 函数
-- name :: Person -> String
-- age :: Person -> Int
-- height :: Person -> Float

-- 通过如下方式来创建数据
-- let p = Person { name="John", age=30, height=1.8 }

-- 使用 getter 函数
-- name p -> "John"
-- age p -> 30
-- height p -> 1.8
```

newtype


newtype 关键字和 data 类似，都是用来创建新的数据类型，但 newtype 的值构造器限制在一个，而 data 没有限制值构造器的数量。
另外，newtype 速度比 data 要快。

为什么既然有了 data 还要有 newtype ？ 先看下面这个例子：

```
[(+2), (*3)] <*> [2, 3]
```
-- 结果是 [4, 5, 6, 9]
-- 但我希望的结果是 [4, 9]，该怎样做 ？
在上面的例子中，因为 [] 已经是 Applicative 的实例了，也就是说它已经实现了自己的 <*> 方法了。
如果不重新实现 <\*> 方法，我们是没有办法得到 [4, 9] 这个结果的。

但怎样才能既不改动原有的 []，又可以重新实现 <\*> 方法呢 ？
答案就是用 newtype 把 [] 封装成一个新的类型，然后让这个新的类型成为 Applicative 的实例啦~
我们来试试：
```haskell
newtype ZipList a = ZipList { getZipList :: [a] } deriving (Show)

-- 要让 ZipList 成为 Applicative 的实例，
-- 必须先让 ZipList 成为 Functor 的实例
instance Functor ZipList where
    fmap f xs = undefined

instance Applicative ZipList where
    pure x = undefined
    ZipList fs <*> ZipList xs = ZipList (zipWith id fs xs)

-- ghci> getZipList $ ZipList [(+2), (*3)] <*> ZipList [2,3]
-- ghci> [4, 9]
```








