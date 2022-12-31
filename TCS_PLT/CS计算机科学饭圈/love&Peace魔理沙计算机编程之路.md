








# 1. 向强者学习的计算机编程之路



计算机科学已经有六七十年历史了，这段时间内书写历史的人不在小数：图灵，冯洛伊曼，Dijkstra，John Reynold，Tony Hoare，John McCarthy，Alan Kay。。。有的人生怕你不知道谁做出了杰出奉献，专门弄了个奖出来呢:)！

你如果真想向更强的人学习，图灵老冯哥德尔都有传记，尽管我没看过，也不知道年代久远的天才有什么借鉴之处；ACM每年都会请图灵奖得主来做freestyle演讲，有展示自己领域的一个漂亮的idea的（[Reflections on Trusting Trust](https://link.zhihu.com/?target=https%3A//www.archive.ece.cmu.edu/~ganger/712.fall02/papers/p761-thompson.pdf)），有总结自己所在领域的（[Principles for Computer System Design](https://link.zhihu.com/?target=http%3A//www.bwlampson.site/Slides/TuringLectureAbstract.htm)），有当场开创新领域的（[Can programming be liberated from the von Neumann style?](https://link.zhihu.com/?target=https%3A//www.thocp.net/biographies/papers/backus_turingaward_lecture.pdf)），有对编程跟设计做出foundational comment的（[The humble programmer](https://link.zhihu.com/?target=https%3A//www.cs.utexas.edu/users/EWD/ewd03xx/EWD340.PDF), [The Emperor’s Old Clothes](https://link.zhihu.com/?target=http%3A//zoo.cs.yale.edu/classes/cs422/2014/bib/hoare81emperor.pdf)），还有让我们rethink computer的（[The Computer Revolution Hasnt Happened Yet](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DoKg1hTOQXoY)）。

如果嫌一年一次的演讲太短，学不到太多，上面所述的很多人都把自己的人生经验整理下来了：Richard Hamming写了本教你如何规划学术生涯的书（The Art of doing science and engineering），Dijkstra的一生所著被整理进了EWD Archive，里面的精品除了The Humble Programmer，还有[A case against the GO TO statement](https://link.zhihu.com/?target=https%3A//www.cs.utexas.edu/users/EWD/ewd02xx/EWD215.PDF)，[Programming considered as a human activity](https://link.zhihu.com/?target=https%3A//www.cs.utexas.edu/users/EWD/ewd01xx/EWD117.PDF)，[On the cruelty of really teaching computing science](https://link.zhihu.com/?target=https%3A//www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html)。Alan Kay则每过一段时间发个视频上youtube（[Power of Simplicity](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DNdSD07U5uBs)）

领域相关的也有很多：在编程语言领域，[History of Programming Languages](https://link.zhihu.com/?target=http%3A//research.ihost.com/hopl/HOPL.html) 把这半世纪的杰出的编程语言设计者的见解汇集在一起， [Dealers of Lightning](https://link.zhihu.com/?target=https%3A//www.amazon.com/Dealers-Lightning-Xerox-PARC-Computer/dp/0887309895) 跟[The Dream Machine](https://link.zhihu.com/?target=https%3A//www.amazon.com/Dream-Machine-Licklider-Revolution-Computing/dp/014200135X) 则描述了改变了世界的Xerox Parc的文化。如果你看的paper足够多，你可以从里面倒推出一个researcher的taste：比如John Reynold就很软，能把多种风格混合在一起（https://zhuanlan.zhihu.com/p/42907876），同时能在很脏的领域做出严谨的工作（Seprational Logic），我就很喜欢。

如果嫌这些人都是上世纪的，很多成功人士也有blog，教你如何做research，如何申请大学，如何规划career，还有自己领域的见解：[http://www.pgbovine.net/](https://link.zhihu.com/?target=http%3A//www.pgbovine.net/)，[https://programanalysis.blogspot.com/](https://link.zhihu.com/?target=https%3A//programanalysis.blogspot.com/)，[https://existentialtype.wordpress.com/](https://link.zhihu.com/?target=https%3A//existentialtype.wordpress.com/)，[http://worrydream.com/](https://link.zhihu.com/?target=http%3A//worrydream.com/)，[http://matt.might.net/](https://link.zhihu.com/?target=http%3A//matt.might.net/)

我一个小本科生，拿啥跟上面的人比，也就比普通人更努力点更早学编程而已，没什么好讨教的。

等我拿到图灵奖再说吧。











# 2. love&Peace





为什么国外大学计算机系本科生培养如此强调函数式编程？ - 圆角骑士魔理沙的回答 - 知乎
https://www.zhihu.com/question/450773131/answer/1807321110





有一群人，就抱着这样的理念，聚集在一起，对程序的复杂性发起了进击。

这群士兵，就是研究编程语言的人。

对于debugging，他们发现了[design by contract](https://en.wikipedia.org/wiki/Design_by_contract)。当你程序出bug的时候，你可以检查出错时具体执行的函数。如果你觉得这个函数没错，你可以给这个函数自身，以及他调用的函数更强的contract（更强的输入输出检查），然后你再跑一次这个程序。只要你这样做，你程序下一次出错的时候，就会更接近真正有问题的代码，而且，你写下的contract以后依然可以继续用。所以，你的代码出一次bug，你代码的健壮性，就会提高一点！这叫[blame shifting](https://scholar.cnki.net/en/Detail/index/GARJ2019/SJCM8020E75BAD6EF6AF48AA0F8F0CCD6C11 )。同时，也有人研究把这些工作扩展到高阶函数，对象，以及指针上，使得无论你用什么feature，都能用如此手段debug。

对于testing，则有[property based testing, fuzzing, model checking, symbolic execution](https://github.com/trailofbits/deepstate)等手段：你可以通过快速的穷举程序输入输出，而抓大量程序的bug。这是普通的unit testing做不到的。

如果你要极致的正确性也可以：你可以用[program analysis/formal verification](https://en.wikipedia.org/wiki/Formal_verification )验证程序不可能有某种错误，或者程序必须符合某种性质。

对于软件架构，这些人整出了operator overloading/typeclass/module等dispatch手段：如果你的程序更通用了，这也更可扩展。

事实上，pytorch的核心正是这样设计的：一个通用的dispatcher，再加上多个不同的Object。普通的Dense Tensor走一个dispatch，Sparse Tensor走另一个dispatch。。。这听上去很正常，反向传播（AD），其实也是dispatch！而且，AD是通过调用更多的dispatch来实现的。（至于高阶导呢？就是AD dispatch上AD）Checkpoint, Quantization, Dynamic Batching, Tracing等等也是通过dispatch组合的。而如果你要多个feature，你只需要一个dispatch调另一个，则可实现。这样，你就可以达到功能的可组合性：大家各写各的，但是到最后，可以无缝贴贴到一起。

如何写API？make illegal state unrepresentable。通过类型系统，特别是sum type，你可以让函数的输入输出，永远满足你想要的形状。你可以通过[refinement type](https://en.wikipedia.org/wiki/Refinement_type )（某种意义上就是contract）进一步对程序需求进行限制。只要你的类型系统够健壮，当你用类型系统表达了你想要的东西的时候，你就会得到它，no if, and, or but。当你要a list of string的时候，不可能得到null，不可能得到string，不可能得到a list with string and number。其他人不可能调错你的API。

至于如何做编程语言？做编程语言并不需要加多少feature。相反，feature越小越好，你只要有几个很强的feature就够了。什么意思呢？[first class function](https://en.wikipedia.org/wiki/Refinement_type )足矣表达大部分design pattern（lambda the ultimate） https://github.com/thma/LtuPatternFactory ，而[continuation](https://en.wikipedia.org/wiki/Continuation )，[algebraic effect](https://stackoverflow.com/questions/49626714/what-does-algebraic-effects-mean-in-fp )/[monad](https://en.wikipedia.org/wiki/Monad_(functional_programming) )
则可以表示各种各样的控制流跟effect。[ADT](https://en.wikipedia.org/wiki/Algebraic_data_type )可以组合出各种各样的类型，然后pattern matching可以很简单的traverse一个ADT。所以，你看专家整的编程语言，都很简单，给你一种‘就这？这就完了？’的感觉。但是，你再定睛一看，普通编程语言能做的，这能做。这能做的，其他的编程语言不能做。

所以，为什么要这么重视函数式编程呢？因为这些课是编程语言的第0课。你可以学到用高阶函数去取代设计模式，用adt消除illegal state。用抽象提高程序组合性，用invariant跟数学手段证明程序的正确性。这些东西本身已经够重要了，但是还给你打开了进修编程语言的大门。

而为什么编程语言又如此重要呢？因为各个领域都在提高硬件效率，但这是人类唯一对抗程序复杂性的方法。如果你没学，你只能自己在错误中慢慢领悟如何写程序。或者更糟糕的，整天去追寻工业界提出的新的编程语言，最新的方法论，但是到最后，发现这些都浮于表面，最后一无所获。[The Pendulum Swings Eternal ]( https://link.zhihu.com/?target=https%3A//buttondown.email/hillelwayne/archive/the-pendulum-swings-eternal/ )

想明白程序的意义吗？想真正的。。。活着吗？

[Automated Software Test Generation: Some Challenges, Solutions, and Recent Advances](https://link.springer.com/chapter/10.1007/978-3-319-91908-9_24)







