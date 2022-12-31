







# 1. ghc-vis是在GHCi中可视化Haskell实时数据结构的工具

http://felsin9.de/nnis/ghc-vis/



ghc-vis是一种工具，用于可视化此类两个功能，即惰性评估和共享，其方式可用于Haskell的（自）教学以及Haskell软件的开发和调试。

惰性评估功能的一个常见示例是无限数据结构



```haskell
$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ> :vis
```


```haskell
λ> let a = [1..3]
λ> :view a
λ> let b = cycle a
λ> :view b
λ> :view "foo" ++ "bar"
```


```haskell
λ> :eval t2
λ> :switch
λ> a !! 2
3
λ> :update
λ> :clear
```



其他工具


另一方面，vacuum-cairo确实告诉我们如何在b中共享值：



```hasekll
λ> System.Vacuum.Cairo.view b
```
但是vacuum-cairo在显示数据结构之前会先对其进行全面评估。因此，我们无法使用它来查看在Haskell中如何对数据结构进行延迟评估。

另外，Vacuum-cairo无法可视化不同数据结构之间的共享，在这种情况下，例如a和b，因为在任何时候都只能查看一个数据结构。我们必须将数据结构组合为一个，以查看在两个结构中都引用了哪些值。

当我们直接使用vacuum（和vacuum-graphviz）时，我们可以检查数据结构而无需评估它们：

```haskell
λ> let a = "foo"
λ> let b = a ++ a
λ> head b
'f'
λ> GHC.Vacuum.GraphViz.graphToDotFile "vacuum2" Data.GraphViz.Commands.Png $
   GHC.Vacuum.nameGraph (GHC.Vacuum.vacuumLazy (a,b))
```






GHCi调试器具有集成的:print命令，可在运行时检查数据结构。评估不是强制性的，因此没有副作用。

```hasekll
$ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
λ> let a = [1..3]
λ> :print a
a = (_t1::[Integer])
λ> head a
1
λ> :print a
a = 1 : (_t2::[Integer])
λ> head $ tail a
2
λ> :print a
a = 1 : 2 : (_t3::[Integer])
λ> a
[1,2,3]
λ> :print a
a = [1,2,3]
λ> let b = a ++ a
λ> head b
1
λ> :print b
b = 1 : (_t3::[Integer])
λ> b
[1,2,3,1,2,3]
λ> :print b
b = [1,2,3,1,2,3]
```