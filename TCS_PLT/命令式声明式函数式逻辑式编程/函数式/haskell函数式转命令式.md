







# 1. haskell函数式转命令式



https://bartoszmilewski.com/2016/11/21/monads-programmers-definition/




有趣的是，这种do表示法的等效项已在命令式语言（尤其是C ++）中找到了应用。我说的是可恢复的功能或协程。C ++期货组成monad并不是秘密。这是延续单子的示例，我们将在稍后讨论。延续的问题在于它们很难组成。在Haskell中，我们使用do表示法将“我的处理程序将调用您的处理程序”的意大利细面条变成类似于顺序代码的形式。可恢复的函数使C ++中的相同转换成为可能。并且可以应用相同的机制将**嵌套循环的意大利面条转换为列表推导或“生成器”**，它们实质上是do单子列表的符号。如果没有统一的monad抽象，通常会通过为语言提供自定义扩展来解决这些问题中的每一个。在Haskell中，所有这些都通过库处理。

















