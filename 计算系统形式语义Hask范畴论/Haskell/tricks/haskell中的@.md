












# 1. haskell中的@

https://stackoverflow.com/questions/30326249/what-does-mean-in-haskell 这个相关链接很详细

```
reconstruct node@(Node a b c l r) parent@(Node b d le ri)
```

http://learnyouahaskell.com/syntax-in-functions#pattern-matching



还有一种叫做patterns的东西。这些是根据模式分解某些内容并将其绑定到名称同时仍然保留对整个事物的引用的一种方便的方法。您可以通过在模式前放置名称和@来实现。例如，模式xs@(x:y:ys)。此模式将与x:y:ys完全匹配，但您可以通过xs轻松获取整个列表，而不是通过再次在函数体中键入x:y:ys来重复自己。这是一个快速而肮脏的例子：

```
capital :: String -> String  
capital "" = "Empty string, whoops!"  
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]  
```


```
ghci> capital "Dracula"  
"The first letter of Dracula is D"  
```

除了@Sibi 的答案中描述的参数模式匹配用法之外，在 Haskell 中，“at”字符（'@'，也称为arobase字符）可以在某些上下文中用于强制输入决定。@Josh.F 在评论中提到了这一点。

这不是默认语言功能的一部分，被称为Type Application Haskell 语言扩展。总之，扩展允许您为多态函数提供显式类型参数，例如read. 在经典的 .hs 源文件中，必须包含相关的编译指示






















