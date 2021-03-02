
https://www.zhihu.com/question/311415552/answer/600063213


dev.stephendiehl.com/hask/#monads

https://www.zhihu.com/question/22291305/answer/21333050


https://www.zhihu.com/question/24972880/answer/134078723



Monad是一种数学结构，haskell中的Monad意义和数学上的意义是一样的。简单的说单子(Monad)就是自函子范畴上的一个幺半群。这个幺半群的态射是作用在自函子上的自然变换，其单位态射是haskell中class Monad 的return函数(这个实际上是个自然变换)。而这个幺半群的态射的组合操作(composition)则是haskell中class Monad的join函数，也是一个自然变换。  
从几何直观的概念来说，Monad是一个自相似的几何结构，通过自函子的作用和两个自然变换的约束得到一层层嵌套的自相似结构。

  
  
作者：parker liu  
链接：https://www.zhihu.com/question/22291305/answer/21333050  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。






















