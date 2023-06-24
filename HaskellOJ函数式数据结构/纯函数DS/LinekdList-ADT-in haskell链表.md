[TOC]

# 1. LinekdList-ADT-in haskell 抽象List是如何定义的 haskell链表 链表形式化 链表抽象代数类型 抽象类型理论中的链表


《B方法》等好像没有这样的链表数学化抽象机：



## 1.1. 链表形式化抽象数据类型--集合论，类型论出发的链表数学定义

mutable sequences

https://wiki.haskell.org/Tying_the_Knot
扭结类型 haskell实现双链表




https://medium.com/@lucasmagnum/sidenotes-linked-list-abstract-data-type-and-data-structure-fd2f8276ab53

linked list abstract data type

Maths - Monads and Algebras
https://www.euclideanspace.com/maths/discrete/category/higher/monad/algebra/index.htm

linked list abstract data type
mutable 
《编程原本》的描述
**《编程原本》**Coordinates withMutable Successors 第67八章




https://en.wikipedia.org/wiki/Cons 在Lisp行话中，“将x限制在y上”表示用(cons x y)。结果对具有左半部分（称为car（寄存器的地址的第一个元素或内容）和右半部分（称为寄存器的减量的第二个元素或内容）

尽管cons单元格可用于保存有序的数据对，但它们更常用于构建更复杂的复合数据结构，尤其是**列表和二叉树**。


在Lisp中，列表是在cons对之上实现的。更具体地说，Lisp中的任何列表结构是：

一个空列表()，通常是一个特殊的对象nil。
一个cons单元格，它car是列表的第一个元素，并且cdr是包含其余元素的列表。
这形成了一个简单的基础上，单链表结构，其内容可以被操纵cons，car和cdr。





您如何特别定义抽象类型理论中的链表？还是你会那样做？

我有点理解抽象List是如何定义的。但仍不是100％。类型理论文学还不是那么伟大。


提示：将链接列表简化为缺点列表，然后类型理论可能更容易思考。 –凯文（Kevin）

我想知道如何构建基本数据类型。这是我学习更多类型理论的最接近的垫脚石。

类型理论是否继续定义列表的不同实现，例如基于指针的基本链接列表？

https://math.stackexchange.com/questions/2858752/how-do-you-define-in-particular-a-linked-list-in-abstract-type-theory-or-would




implement a Haskell algebraic datatype linked list (or perhaps more accurately something linked list-like since I don't know of any way to do memory addressing using Haskell)




A typical example of a recursive ADT is a linked list. Here, the list is also made generic over a type `T`:

T = TypeVar('T')

@adt
class LinkedList(Generic\[T\]):
    NIL: Case
    CONS: Case\[T, "LinkedList\[T\]"\]

See the library's [tests](https://pypi.org/project/algebraic-data-types/tests/) for more examples of complete ADT definitions. https://pypi.org/project/algebraic-data-types/





Heterogenous collections Techniques for implementing heterogenous lists in Haskell 某种类型不同的对象的集合 https://wiki.haskell.org/Heterogenous_collections
Oleg Kiselyov，RalfLämmel和Keean Schupke撰写的论文《强类型异类集合》不仅包含Haskell中异构列表的实现，而且还提供了有关何时，为什么以及如何使用HLists的令人振奋的例子。特别是，他们正在使用它进行类型安全的编译时检查的数据库访问。（认为LINQ，事实上，它们被引用的纸张是由Erik Meijer等人，导致LINQ Haskell的纸。） https://softwareengineering.stackexchange.com/questions/132835/is-there-a-specific-purpose-for-heterogeneous-lists






# 2. implementation

https://github.com/cdepillabout/focuslist


http://hackage.haskell.org/package/ListZipper

http://hackage.haskell.org/package/pointedlist-0.6.1




历史上有三种实现：
- 双数组，第二个数组是第一个数组的index，第一个数组存真正的数字
- cpp之流的point结构体指针类型
- python之流的Class类和对象封装


https://rosettacode.org/wiki/Linked_list 


单链表
https://github.com/CindyLinz/Haskell-linked-list-with-iterator

https://github.com/mark-gerarts/haskell-learning/tree/master/Data%20Structures%20%26%20Algorithms

https://rosettacode.org/wiki/Singly-linked_list/Element_definition#Haskell
单链表

```haskell
module LinkedList
    ( LinkedList
    , datum
    , fromList
    , isNil
    , new
    , next
    , nil
    , reverseLinkedList
    , toList
    ) where

import Data.Maybe

data LinkedList a = LinkedList {
  getNext :: Maybe (LinkedList a),
  getValue :: Maybe a
  }

datum :: LinkedList a -> a
datum ll = fromJust $ getValue ll

fromList :: [a] -> LinkedList a
fromList = foldr new nil

isNil :: LinkedList a -> Bool
isNil ll = isNothing (getValue ll) && isNothing (getNext ll)

new :: a -> LinkedList a -> LinkedList a
new val next_list = LinkedList {getNext = Just next_list, getValue = Just val}

next :: LinkedList a -> LinkedList a
next ll = fromJust $ getNext ll  

nil :: LinkedList a
nil = LinkedList {getNext = Nothing, getValue = Nothing}

reverseLinkedList :: LinkedList a -> LinkedList a
reverseLinkedList ll
  | isNil ll = ll
  | otherwise = fromList $ reverse $ toList ll

toList :: LinkedList a -> [a]
toList ll 
  | isNil ll = []
  | otherwise = datum ll : toList (next ll)

```
双链表

https://github.com/mark-gerarts/haskell-learning/tree/master/Data%20Structures%20%26%20Algorithms

haskell双链表
https://rosettacode.org/wiki/Doubly-linked_list/Element_definition#Haskell


```haskell
data DList a = Leaf | Node (DList a) a (DList a)
 
updateLeft _ Leaf = Leaf
updateLeft Leaf (Node _ v r) = Node Leaf v r
updateLeft new@(Node nl _ _) (Node _ v r) = current
    where current = Node prev v r
          prev = updateLeft nl new
 
updateRight _ Leaf = Leaf
updateRight Leaf (Node l v _) = Node l v Leaf  
updateRight new@(Node _ _ nr) (Node l v _) = current
    where current = Node l v next
          next = updateRight nr new
```






## 2.1. lisp 用cons实现链表


https://en.wikipedia.org/wiki/Cons

















《编程珠玑》haskell函数式编程数据结构看看：

## 2.2. haskell功能，无突变，高效的双链表

chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://arxiv.org/pdf/1808.08329.pdf  When You Should Use Lists in Haskell(Mostly, You Should Not


A simple Haskell linked list implementation https://gist.github.com/akoskovacs/5074344#file-mylist-hs-L63

```haskell
module MyList where

data MyList a = Cons a (MyList a) 
                | MyNil deriving (Show, Eq)
{-
 A simple linked list module
  Some examples: 
	mylist = (Cons 10 (Cons 99 (Cons 11 (Cons 1 MyNil))))
	myHead myList                       # => 10
	myTail myList                       # => Cons 99 (Cons 11 (Cons 1 MyNil))
	myLength myList               # => 4
	myToList myList               # => [10,99,11,1]
	myFromList [10,99,11,1]       # => (Cons 10 (Cons 99 (Cons 11 (Cons 1 MyNil))))
	myIndex 2 myList              # => 11
	myMapList (\x -> x*x) myList  # => Cons 100 (Cons 9801 (Cons 121 (Cons 1 MyNil)))
	...etc..
-}

myHead :: MyList a -> a
myHead l = case l of
        Cons a _ -> a

myTail :: MyList a -> MyList a
myTail MyNil = MyNil
myTail l = case l of
        Cons _ a -> a

myIndex :: Int -> MyList a -> a
myIndex 0 xs = myHead xs
myIndex x xs = myHead (myIndexTail x xs)
    where 
        myIndexTail 0 xs = xs
        myIndexTail i xs = myIndexTail (i-1) (myTail xs)

myLength :: MyList a -> Int 
myLength MyNil = 0
myLength xs = 1 + (myLength (myTail xs))

myLast :: MyList a -> a
myLast (Cons a MyNil) = a
myLast l = myLast (myTail l)

myInsert :: a -> MyList a -> MyList a
myInsert x xs = Cons x xs

myConcat :: MyList a -> MyList a -> MyList a
myConcat (Cons a MyNil) bs = Cons a bs
myConcat as bs = myInsert (myHead as) (myConcat (myTail as) bs)

myAppend :: a -> MyList a -> MyList a
myAppend x (Cons a MyNil) = Cons a (Cons x MyNil)
myAppend x xs = myInsert (myHead xs) (myAppend x (myTail xs))

myToList :: MyList a -> [a]
myToList MyNil = []
myToList (Cons a l) = a:(myToList l)

myFromList :: [a] -> MyList a 
myFromList [] = MyNil
myFromList l = Cons (head l) (myFromList (tail l))

myMapList :: (t -> a) -> MyList t -> MyList a
myMapList f (Cons x MyNil) = Cons (f x) MyNil
myMapList f l = Cons (f (myHead l)) (myMapList f (myTail l))
```



https://hackage.haskell.org/package/stm-linkedlist-0.1.0.0/docs/Data-STM-LinkedList.html


视频教程 haskell实现双链表 https://www.reddit.com/r/haskell/comments/2nepr0/implementing_doubly_linked_lists_in_haskell/


为什么Haskell和Scheme使用单链接列表？https://qastack.cn/software/294983/why-do-haskell-and-scheme-use-singly-linked-lists









好吧，如果您看起来更深一点，实际上它们都还包括基本语言中的数组：

-   第五次修订的计划报告（R5RS）包括[*向量*类型](http://www.schemers.org/Documents/Standards/R5RS/HTML/r5rs-Z-H-9.html#%_sec_6.3.6)，它们是固定大小的整数索引集合，随机访问的时间要好于线性时间。
-   Haskell 98报告也具有[数组类型](https://www.haskell.org/onlinereport/array.html)。

但是，功能性编程指令长期以来一直强调数组而不是单链表或双链表。实际上，很可能过分强调了。但是，有几个原因。

第一个是单链接列表是最简单但也是最有用的递归数据类型之一。用户定义的等效于Haskell列表类型的定义如下：

```
data List a           -- A list with element type `a`...
  = Empty             -- is either the empty list...
  | Cell a (List a)   -- or a pair with an `a` and the rest of the list. 

```

列表是递归数据类型这一事实意味着，处理列表的函数通常使用[**结构递归**](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Structural_versus_generative_recursion)。用Haskell术语：在列表构造函数上进行模式匹配，然后在列表的*子部分*递归。在这两个基本函数定义中，我使用变量`as`来引用列表的末尾。因此请注意，递归调用在列表中“下降”：

```
map :: (a -> b) -> List a -> List b
map f Empty = Empty
map f (Cell a as) = Cell (f a) (map f as)

filter :: (a -> Bool) -> List a -> List a
filter p Empty = Empty
filter p (Cell a as)
    | p a = Cell a (filter p as)
    | otherwise = filter p as

```

这种技术保证您的函数将在所有有限列表中终止，并且是一种很好的解决问题的技术-它倾向于将问题自然地分解为更简单，更易处理的子部分。

因此，单链列表可能是向学生介绍这些技术的最佳数据类型，这在函数式编程中非常重要。

第二个原因不是“为什么是单链表”原因，而是“为什么不是双链表或数组”原因：后一种数据类型通常需要*突变*（可修改的变量），这在函数编程中非常常见。避开。碰巧的是：

-   在像Scheme这样的热切语言中，如果不使用mutation，就无法创建一个双向链接列表。
-   在像Haskell这样的惰性语言中，您可以创建一个双向链接列表，而无需使用突变。但是，每当您基于该列表创建一个新列表时，就必须复制大多数（如果不是全部）原始结构。使用单链接列表，您可以编写使用“结构共享”的函数，而新列表可以在适当时重用旧列表的单元格。
-   传统上，如果您以不变的方式使用数组，则意味着每次您想要修改数组时，都必须复制整个内容。（[`vector`](https://wiki.haskell.org/Numeric_Haskell:_A_Vector_Tutorial)但是，最近的Haskell库（例如）发现了可以大大改善此问题的技术）。

第三个也是最后一个原因主要适用于像Haskell这样的惰性语言：在实践中，惰性单链接列表实际上更类似于*迭代器，而*不是适用于内存中列表。如果您的代码按顺序使用列表元素并将其丢弃，那么当您逐步浏览列表时，目标代码将仅实现列表单元格及其内容。

这意味着整个列表不需要一次存在于内存中，只需当前单元即可。可以对当前单元格之前的单元格进行垃圾收集（使用双链表是不可能的）；直到当前单元格才需要计算比当前单元格晚的单元格。

它甚至远不止于此。在几种流行的Haskell库中使用了一种称为[**融合的技术**](https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/rewrite-rules.html#idp26293440)，在该库中，编译器分析您的列表处理代码，并发现依次生成和使用的中间列表，然后“丢弃”中间列表。有了这些知识，编译器就可以完全消除这些列表单元的内存分配。这意味着在编译后，Haskell源程序中的单链接列表实际上可能变成*循环*而不是数据结构。

融合也是上述`vector`库用来为不可变数组生成有效代码的技术。极为流行的`bytestring`（字节数组）和`text`（Unicode字符串）库也是如此，它们是用来代替Haskell的不是很好的本机`String`类型（`[Char]`与字符的单链接列表相同）的。因此，在现代的Haskell中，存在一种趋势，即带有融合支持的不可变数组类型变得非常普遍。

在单链接列表中，您可以*前进*但不能*向后退*，这有利于列表融合。这在函数式编程中提出了一个非常重要的主题：使用数据类型的“形状”派生计算的“形状”。如果要顺序处理元素，则单链接列表是一种数据类型，当您通过结构递归使用它时，它会非常自然地为您提供该访问模式。如果您想使用“分而治之”的策略来解决问题，那么树数据结构将很好地支持这一点。

很多人很早就退出了函数式编程旅行，因此他们接触了单链接列表，但没有接触更高级的基础思想。













https://softwareengineering.stackexchange.com/questions/294983/why-do-haskell-and-scheme-use-singly-linked-lists/294984








编写对数据结构具有破坏性作用的命令式算法的纯功能性和高效实现始终是一个有趣的挑战。该功能实现具有方程式推理和模块化的显着优势。我们可以在不考虑隐式全局状态的情况下理解算法。无突变的功能实现也具有实际好处：易于添加检查点，撤消和重做。突变的存在使代码具有多线程安全性，并有助于移植到分布式或非共享内存的并行体系结构。另一方面，命令式实现具有最优性的优点：至少在常规体系结构上，对复杂数据结构中的组件进行更改是恒定时间操作。命令式代码使共享变得明确，
我们展示了一个简单的示例，该示例在纯函数式程序中实现了命令式数据结构的所有优点-包括共享和更新效率。我们的数据结构是一个双链表，可能是循环表，具有添加，删除和更新元素的标准操作；双向遍历列表；遍历列表，并进行周期检测。代码：

统一处理循环列表和终止列表；
不会在更新时重建整个列表；
在一个小常数的时间范围内更新当前节点中的值；
不使用或提及任何单子；
不使用任何IORef，STRef，TVars或任何其他破坏性更新;
允许记录，撤消和重做更新，检查点；
容易地推广到二维网格。
该算法本质上是必不可少的-因此支持身份检查和就地“更新”-但仅在功能上实现。尽管代码依赖于许多本地类型的安全堆，但强调没有全局堆，也没有全局状态。
Haskell被称为最佳命令式语言并非没有。祈使算法可以按原样实施-真正具有功能性，无需诉诸于Monadic子语言，而是充分利用了从句定义，模式保护和惰性。

版本
当前版本是1.2，2009年1月7日
参考
FDList.hs  [8K]
完整的，已注释的Haskell98代码和许多测试
Haskell-Cafe讨论``更新双向链表''。2009年1月。

http://okmij.org/ftp/Haskell/AlgorithmsH1.html#pure-cyclic-list




```
-- Haskell98
-- Pure functional, mutation-free, constant-time-access double-linked
-- lists

module FDList where

-- Note that insertions, deletions, lookups have
-- a worst-case complexity of O(min(n,W)), where W is either 32 or 64
-- (depending on the paltform). That means the access time is bounded
-- by a small constant (32 or 64). 
import qualified Data.IntMap as IM

-- Representation of the double-linked list

type Ref = Int				-- positive, we shall treat 0 specially

data Node a = Node{node_val   :: a,
		   node_left  :: Ref,
		   node_right :: Ref}

data DList a = DList{dl_counter :: Ref,	    -- to generate new Refs
		     dl_current :: Ref,     -- current node
		     dl_mem :: IM.IntMap (Node a)} -- main `memory'

-- Because DList contains the `pointer' to the current element, DList
-- is also a Zipper

-- Operations on the DList a

empty :: DList a
empty = DList{dl_counter = 1, dl_current = 0, dl_mem = IM.empty}

-- In a well-formed list, dl_current must point to a valid node
-- All operations below preserve well-formedness
well_formed :: DList a -> Bool
well_formed dl | IM.null (dl_mem dl) = dl_current dl == 0
well_formed dl = IM.member (dl_current dl) (dl_mem dl) 

is_empty :: DList a -> Bool
is_empty dl = IM.null (dl_mem dl)


-- auxiliary function
get_curr_node :: DList a -> Node a
get_curr_node DList{dl_current=curr,dl_mem=mem} = 
  maybe (error "not well-formed") id $ IM.lookup curr mem

-- The insert operation below makes a cyclic list
-- The other operations don't care
-- Insert to the right of the current element, if any
-- Return the DL where the inserted node is the current one
insert_right :: a -> DList a -> DList a
insert_right x dl | is_empty dl =
   let ref = dl_counter dl
       -- the following makes the list cyclic
       node = Node{node_val = x, node_left = ref, node_right = ref}
   in DList{dl_counter = succ ref,
	    dl_current = ref,
	    dl_mem = IM.insert ref node (dl_mem dl)}

insert_right x dl@DList{dl_counter = ref, dl_current = curr, dl_mem = mem} =
  DList{dl_counter = succ ref, dl_current = ref, 
	dl_mem = IM.insert ref  new_node   $ 
                 IM.insert next next_node' $
	         (if next == curr then mem else IM.insert curr curr_node' mem)}
 where
 curr_node = get_curr_node dl
 curr_node'= curr_node{node_right = ref}
 next      = node_right curr_node
 next_node = if next == curr then curr_node'
                else maybe (error "ill-formed DList") id $ IM.lookup next mem
 new_node  = Node{node_val   = x, node_left = curr, node_right = next}
 next_node'= next_node{node_left = ref}
 

-- Delete the current element from a non-empty list
-- We can handle both cyclic and terminated lists
-- The right node becomes the current node.
-- If the right node does not exists, the left node becomes current
delete :: DList a -> DList a
delete dl@DList{dl_current = curr, dl_mem = mem_old} =
 case () of
   _ | notexist l && notexist r -> empty
   _ | r == 0 ->
       dl{dl_current = l, dl_mem = upd l (\x -> x{node_right=r}) mem}
   _ | r == curr ->			-- it was a cycle on the right
       dl{dl_current = l, dl_mem = upd l (\x -> x{node_right=l}) mem}
   _ | l == 0 ->
       dl{dl_current = r, dl_mem = upd r (\x -> x{node_left=l}) mem}
   _ | l == curr ->
       dl{dl_current = r, dl_mem = upd r (\x -> x{node_left=r}) mem}
   _ | l == r ->
       dl{dl_current = r, dl_mem = upd r (\x -> x{node_left=r, 
						     node_right=r}) mem}
   _ ->
       dl{dl_current = r, dl_mem = upd r (\x -> x{node_left=l}) .
	                           upd l (\x -> x{node_right=r}) $ mem}
 where
 (Just curr_node, mem) = IM.updateLookupWithKey (\_ _ -> Nothing) curr mem_old
 l = node_left curr_node
 r = node_right curr_node
 notexist x = x == 0 || x == curr
 upd ref f mem = IM.adjust f ref mem


get_curr :: DList a -> a
get_curr = node_val . get_curr_node

move_right :: DList a -> Maybe (DList a)
move_right dl = if next == 0 then Nothing else Just (dl{dl_current=next})
 where
 next = node_right $ get_curr_node dl

-- If no right, just stay inplace
move_right' :: DList a -> DList a
move_right' dl = maybe dl id $ move_right dl

move_left :: DList a -> Maybe (DList a)
move_left dl = if next == 0 then Nothing else Just (dl{dl_current=next})
 where
 next = node_left $ get_curr_node dl

-- If no left, just stay inplace
move_left' :: DList a -> DList a
move_left' dl = maybe dl id $ move_left dl

fromList :: [a] -> DList a
fromList = foldl (flip insert_right) empty

-- The following does not anticipate cycles (deliberately)
takeDL :: Int -> DList a -> [a]
takeDL 0 _ = []
takeDL n dl | is_empty dl = []
takeDL n dl = get_curr dl : (maybe [] (takeDL (pred n)) $ move_right dl)

-- Reverse taking: we move left
takeDLrev :: Int -> DList a -> [a]
takeDLrev 0 _ = []
takeDLrev n dl | is_empty dl = []
takeDLrev n dl = get_curr dl : (maybe [] (takeDLrev (pred n)) $ move_left dl)

-- Update the current node `inplace'
update :: a -> DList a -> DList a
update x dl@(DList{dl_current = curr, dl_mem = mem}) = 
   dl{dl_mem = IM.insert curr (curr_node{node_val = x}) mem}
  where
  curr_node = get_curr_node dl


-- This one watches for a cycle and terminates when it detects one
toList :: DList a -> [a]
toList dl | is_empty dl = []
toList dl = get_curr dl : collect (dl_current dl) (move_right dl)
 where
 collect ref0 Nothing = []
 collect ref0 (Just DList{dl_current = curr}) | curr == ref0 = []
 collect ref0 (Just dl) = get_curr dl : collect ref0 (move_right dl)



-- Tests

test1l = insert_right 1 $ empty
test1l_r = takeDL 5 test1l		-- [1,1,1,1,1]
test1l_l = takeDLrev 5 test1l		-- [1,1,1,1,1]
test1l_c = toList test1l		-- [1]

test2l = insert_right 2 $ test1l
test2l_r = takeDL 5 test2l		-- [2,1,2,1,2]
test2l_l = takeDLrev 5 test2l		-- [2,1,2,1,2]
test2l_l'= takeDLrev 5 (move_left' test2l) -- [1,2,1,2,1]
test2l_c = toList test2l		-- [2,1]

test3l = insert_right 3 $ test2l
test3l_r = takeDL 7 test3l		-- [3,1,2,3,1,2,3]
test3l_l = takeDLrev 7 test3l		-- [3,2,1,3,2,1,3]
test3l_l'= takeDLrev 7 (move_left' test3l) -- [2,1,3,2,1,3,2]
test3l_c = toList (move_right' test3l)	-- [1,2,3]


test31l = delete test3l
test31l_r = takeDL 7 test31l		-- [1,2,1,2,1,2,1]
test31l_l = takeDLrev 7 test31l		-- [1,2,1,2,1,2,1]
test31l_c = toList test31l		-- [1,2]

test32l = delete test31l
test32l_r = takeDL 5 test32l		-- [2,2,2,2,2]
test32l_l = takeDLrev 5 test32l		-- [2,2,2,2,2]
test32l_c = toList test32l		-- [2]


test33l = delete test32l
test33l_r = takeDL 5 test33l		-- []


testl = fromList [1..5]
testl_r = takeDL 11 testl		-- [5,1,2,3,4,5,1,2,3,4,5]
testl_l = takeDLrev 11 testl		-- [5,4,3,2,1,5,4,3,2,1,5]
testl_c = toList testl			-- [5,1,2,3,4]

testl1 = update (-1) testl
testl1_r = takeDL 11 testl1		-- [-1,1,2,3,4,-1,1,2,3,4,-1]
testl1_c = toList testl1		-- [-1,1,2,3,4]

testl2 = update (-2) . move_right' . move_right' $ testl1
testl2_r = takeDL 11 testl2		-- [-2,3,4,-1,1,-2,3,4,-1,1,-2]
testl2_l = takeDLrev 11 testl2		-- [-2,1,-1,4,3,-2,1,-1,4,3,-2]
testl2_c = toList testl2		-- [-2,3,4,-1,1]

-- Old testl is still available: there are no destructive updates
testl3 = update (-2) . move_right' . move_right' $ testl
testl3_r = takeDL 11 testl3		-- [-2,3,4,5,1,-2,3,4,5,1,-2]
testl3_c = toList testl3		-- [-2,3,4,5,1]
```



## 2.3. 函数式编程语言中最常用的一种数据结构：不可变的链表ImmutableList

  [趣味编程：函数式链表的快速排序](http://blog.zhaojie.me/2009/08/functinal-list-quick-sort.html)














## 2.4. 关于Haskell：如何实现双向链表

純函數式編程語言中的雙重鏈接列表 https://zh.stackoom.com/question/7jl5/%E7%B4%94%E5%87%BD%E6%95%B8%E5%BC%8F%E7%B7%A8%E7%A8%8B%E8%AA%9E%E8%A8%80%E4%B8%AD%E7%9A%84%E9%9B%99%E9%87%8D%E9%8F%88%E6%8E%A5%E5%88%97%E8%A1%A8


haskell实现双链表视频教程：https://www.youtube.com/watch?v=-HZ4bo_USvE









https://www.codenong.com/10386616/

双链表不是数据类型，而是实现细节。我想您想要的是一个类似列表的数据结构，您可以在其中高效地左右移动。此数据结构是列表的**zipper**拉链，只是一对列表。前缀以相反的顺序表示。要左右移动，您只需将后缀列表的开头移到前缀上，反之亦然。





在Haskell中有一个双向链表实际上是不实际的，因为您必须立即构造所有链表。

例如，假设您有一个要双重链接的列表\[1, 2, 3, 4, 5\]。现在，让我们想象一下列表的表示方式：

<table cellspacing="0" cellpadding="0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; border-collapse: separate; border-spacing: 0px; text-size-adjust: 100%; width: 745.6px; direction: ltr;"><tbody style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><tr style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><td class="line-numbers" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border-top: 0px; border-right: 3px solid rgb(108, 226, 108) !important; border-bottom: 0px; border-left: 0px; border-image: initial; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: right; text-size-adjust: 100%; width: 36px; direction: ltr; color: rgb(136, 136, 136); background-color: rgb(238, 238, 238);"><div style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; min-width: 23px;">1<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">2<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">3<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">4<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"></div></td><td style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; width: auto;"><div class="haskell codecolorer" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; color: rgb(8, 8, 8); background-color: rgb(249, 249, 249);"><span class="kw1" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(121, 73, 56);">data</span><span>&nbsp;</span>DoubleList a<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp;<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>LeftEnd &nbsp;a<span>&nbsp;</span><span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">(</span>DoubleList a<span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">)</span><br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp;<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">|</span><span>&nbsp;</span>Middle &nbsp; a<span>&nbsp;</span><span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">(</span>DoubleList a<span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">)</span><span>&nbsp;</span><span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">(</span>DoubleList a<span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">)</span><br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp;<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">|</span><span>&nbsp;</span>RightEnd a<span>&nbsp;</span><span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">(</span>DoubleList a<span class="br0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">)</span></div></td></tr></tbody></table>

(为简单起见，我在两端使用了两个不同的构造函数)

要构建上面的列表，您必须首先构建第一个元素：

<table cellspacing="0" cellpadding="0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; border-collapse: separate; border-spacing: 0px; text-size-adjust: 100%; width: 745.6px; direction: ltr;"><tbody style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><tr style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><td class="line-numbers" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border-top: 0px; border-right: 3px solid rgb(108, 226, 108) !important; border-bottom: 0px; border-left: 0px; border-image: initial; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: right; text-size-adjust: 100%; width: 36px; direction: ltr; color: rgb(136, 136, 136); background-color: rgb(238, 238, 238);"><div style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; min-width: 23px;">1<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"></div></td><td style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; width: auto;"><div class="haskell codecolorer" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; color: rgb(8, 8, 8); background-color: rgb(249, 249, 249);"><span class="kw1" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(121, 73, 56);">let</span><span>&nbsp;</span>e1<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>LeftEnd &nbsp;<span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">1</span><span>&nbsp;</span>...</div></td></tr></tbody></table>

但是要构造第一个元素，您已经需要有第二个元素：

<table cellspacing="0" cellpadding="0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; border-collapse: separate; border-spacing: 0px; text-size-adjust: 100%; width: 745.6px; direction: ltr;"><tbody style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><tr style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><td class="line-numbers" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border-top: 0px; border-right: 3px solid rgb(108, 226, 108) !important; border-bottom: 0px; border-left: 0px; border-image: initial; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: right; text-size-adjust: 100%; width: 36px; direction: ltr; color: rgb(136, 136, 136); background-color: rgb(238, 238, 238);"><div style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; min-width: 23px;">1<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">2<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"></div></td><td style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; width: auto;"><div class="haskell codecolorer" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; color: rgb(8, 8, 8); background-color: rgb(249, 249, 249);"><span class="kw1" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(121, 73, 56);">let</span><span>&nbsp;</span>e1<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>LeftEnd &nbsp;<span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">1</span><span>&nbsp;</span>e2<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp; &nbsp; e2<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>Middle &nbsp;<span>&nbsp;</span><span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">2</span><span>&nbsp;</span>e1 ...</div></td></tr></tbody></table>

对于第二个元素，您需要第三个，依此类推：

<table cellspacing="0" cellpadding="0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; border-collapse: separate; border-spacing: 0px; text-size-adjust: 100%; width: 745.6px; direction: ltr;"><tbody style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><tr style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"><td class="line-numbers" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border-top: 0px; border-right: 3px solid rgb(108, 226, 108) !important; border-bottom: 0px; border-left: 0px; border-image: initial; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: right; text-size-adjust: 100%; width: 36px; direction: ltr; color: rgb(136, 136, 136); background-color: rgb(238, 238, 238);"><div style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; min-width: 23px;">1<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">2<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">3<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">4<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">5<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;"></div></td><td style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; width: auto;"><div class="haskell codecolorer" style="box-sizing: border-box; margin: 0px; padding: 5px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-align: left; text-size-adjust: 100%; color: rgb(8, 8, 8); background-color: rgb(249, 249, 249);"><span class="kw1" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(121, 73, 56);">let</span><span>&nbsp;</span>e1<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>LeftEnd &nbsp;<span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">1</span><span>&nbsp;</span>e2<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp; &nbsp; e2<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>Middle &nbsp;<span>&nbsp;</span><span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">2</span><span>&nbsp;</span>e1 e3<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp; &nbsp; e3<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>Middle &nbsp;<span>&nbsp;</span><span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">3</span><span>&nbsp;</span>e2 e4<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp; &nbsp; e4<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>Middle &nbsp;<span>&nbsp;</span><span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">4</span><span>&nbsp;</span>e3 e5<br style="box-sizing: border-box; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%;">&nbsp; &nbsp; e5<span>&nbsp;</span><span class="sy0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(8, 8, 8);">=</span><span>&nbsp;</span>RightEnd<span>&nbsp;</span><span class="nu0" style="box-sizing: border-box; margin: 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline; font: 1.4rem / 1.9rem Monaco, &quot;Lucida Console&quot;, monospace; text-size-adjust: 100%; color: rgb(129, 31, 36);">5</span><span>&nbsp;</span>e4</div></td></tr></tbody></table>

由于懒惰的评估，这可能在Haskell中完成。这种策略称为"打结"(您不必从字面上将其全部放在一个let块中；您可以将构造分为功能)

但是，换句话说，要制作一个双向链接的列表，您需要立即构建所有列表，如果您想更改其中的任何部分，则需要使用Zipper或仅对其进行完整复制每次。

我建议改用Data.Sequence，这是基于手指树的优化顺序存储实现。它支持非常快速的插入，删除和迭代，同时仍然是纯粹的功能数据结构。

否则，您可能只想使用拉链，而将它们用于树而不是列表。有关拉链的更多信息，请参见Haskell Wiki。在这种情况下，拉链非常适合，因为它们提供了您所追求的确切功能：如果您使用拉链参观一棵树，则可以访问所访问树的"父级"，但树本身不必包含父引用。







由于您(通常)在Haskell中没有OO样式的对象，因此认为数据具有自我意识是很奇怪的。重要的是要注意，您通常不使用Haskell数据类型中的聚合，而倾向于组合。

您可能需要研究XMonad，以查看其设计是否符合您的需求(代码可读性出奇)。

您可能还需要重新设计，以使您无需再看上方(例如，通过将子级"回调"传递给您)。

您可能还想看看是否可以为整个图形编写一个拉链。







## 2.5. haskell用zipper，手指树




















