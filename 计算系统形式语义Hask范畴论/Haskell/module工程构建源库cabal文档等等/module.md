


默认源码位置


```
D:\Program Files\Haskell Platform\8.6.5\lib

C:\ProgramData\chocolatey\lib\ghc\tools\ghc-8.10.2\lib
```

*.hi


*.o

# module






如果ghci要从与包含该文件的文件夹不同的文件夹运行，请执行以下操作：

ghci -iC:\Test\Haskell\
-i 设置导入搜索路径，然后执行以下操作：

:load C:\Test\Haskell\MyApp.hs
或从ghci控制台内部执行：

:set -iC:\Test\Haskell\
如果要查看haskell在哪个文件夹中查找模块，请致电：

:show paths
它应该在下面打印路径列表 module import search paths:

如果ghci从包含文件的文件夹中运行，则所有这些都是不必要的，因为默认情况下，Haskell始终会在当前文件夹中查找导入。

不要-i在路径与路径之间留出空间



haskell.org/hugs/pages/users_guide/module-commands.html


