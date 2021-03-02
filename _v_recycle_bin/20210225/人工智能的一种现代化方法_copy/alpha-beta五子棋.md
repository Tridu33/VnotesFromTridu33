# alpha-beta五子棋






[CS312习题21大学伪代码](https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm)


github.com/colingogogo/gobang_AI#gobang_ai


cnblogs.com/qiaozhoulin/p/4546884.html

alpha-beta-pruning Topic github.com/topics/alpha-beta-pruning

在Python中使用Alpha-Beta修剪的Minimax  
https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

现在已经有了普通的minimax的伪代码, 由于下文中需要用到α, β所以对应地将其转换成a（alpha）、b（beta）的形式
```
function minimax(node, depth)
    if node is a terminal node or depth = 0
        return the heuristic value of node
    if the adversary is to play at node
        let b := +∞
        foreach child of node
            b := min(a, minimax(child, depth-1))
        return b
    else {we are to play at node}
        let a := -∞
        foreach child of node
            a := max(b, minimax(child, depth-1))
        return a
```
我们在此伪代码的基础上添加alpha-beta剪枝
```
function minimax(node, depth, a, b)
    if node is a terminal node or depth = 0
        return the heuristic value of node
    if the adversary is to play at node
        //let b := +∞
        foreach child of node
            b := min(a, minimax(child, depth-1, a, b))
            if b <= a 
                  return b
        return b
    else {we are to play at node}
        //let a := -∞
        foreach child of node
            a := max(b, minimax(child, depth-1, a, b))
            if a >= b 
                  return a
        return a
```
其实上述添加的两个if语句的条件判断是完全一样的，因为根据原理在min节点只能修改beta，而在max节点只能修改alpha，这样写只是为了让结构更为清晰。



```
(* the minimax value of n, searched to depth d.
 * If the value is less than min, returns min.
 * If greater than max, returns max. *)
 fun minimax(n: node, d: int, min: int, max: int): int =
   if leaf(n) or depth=0 return evaluate(n)
   if n is a max node
      v := min
      for each child of n
         v' := minimax (child,d-1,v,max)
         if v' > v, v:= v'
         if v > max return max
      return v
   if n is a min node
      v := max
      for each child of n
         v' := minimax (child,d-1,min,v)
         if v' < v, v:= v'
         if v < min return min
      return v
```