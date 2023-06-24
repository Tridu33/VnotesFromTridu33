

https://dkalemis.wordpress.com/2014/01/23/trees-in-haskell/
```haskell
module Main where
 
data MyTree a = MyEmptyNode
              | MyFilledNode a (MyTree a) (MyTree a)
              deriving (Eq,Ord,Show,Read)
 
main :: IO ()
main  =
   do
      putStrLn "Begin program"
 
      let aMyTree = MyFilledNode 5 (MyFilledNode 3 MyEmptyNode MyEmptyNode) (MyFilledNode 2 MyEmptyNode MyEmptyNode)
      print aMyTree
      print (sumMyTree aMyTree)
 
      let bMyTree = MyFilledNode "r" (MyFilledNode "s" MyEmptyNode MyEmptyNode) (MyFilledNode "a" MyEmptyNode MyEmptyNode)
      print bMyTree
 
      putStrLn "End program"
 
sumMyTree                       :: Num a => MyTree a -> a
sumMyTree MyEmptyNode            = 0
sumMyTree (MyFilledNode n t1 t2) = n + sumMyTree t1 + sumMyTree t2
```


## 1.1. 多叉树


```haskell
data BinaryTree a  = BTNil 
                   | BTNode a (BinaryTree a) (BinaryTree a)

data TernaryTree a = TTNil
                   | TTNode a (TernaryTree a) (TernaryTree a) (TernaryTree a)

data QuadTree a    = QTNil
                   | QTNode a (QuadTree a) (QuadTree a) (QuadTree a) (QuadTree a)
```


## 1.2. rose tree


https://stackoverflow.com/questions/41408922/data-type-for-tree-in-haskell


```haskell
data RoseTree a = RTNil | RTNode a [RoseTree a]
```



There is some duplication here, as `RTNil` is only needed to store an explicit empty tree. 

Leaf nodes are just `RTNode a []`. 

(Consider what difference, if any, you would assign to the values `RTNode 3 [], RTNode 3 [RTNil], RTNode 3 [RTNil, RTNil]`, etc.)







# 2. haskell红黑树













手把手教你43行代码写红黑树（包括删除操作） - 鸭嘎嘎的文章 - 知乎
https://zhuanlan.zhihu.com/p/77616103


















