# 1. CS人工智能数学哲学






人工智能能够研究发展数学和哲学吗？ - 赵泠的回答 - 知乎
https://www.zhihu.com/question/413552492/answer/1420732821






大部分计算机辅助证明有着庞大的计算量，尽管人是看得懂的，但是字实在太多了，无法在短时间内以人手验证。所以这样的证明的检验工作也可以交给自动定理检验来执行。

一些数学家出于美学上的理由而不接受计算机辅助证明。

典型案例：

1998年，托马斯·黑尔斯宣称证明了开普勒猜想，他提交的证明包含3GB的计算机数据和250页的注释，数据包括证明所用的程序、资料和结果。由20名裁判员组成的小组接受了这个证明，《数学年报》由此同意发表该论文。

2003年，裁判员小组报告他们“99%确定”此证明的正确性，但不能完全确定所有电脑计算的正确性。同年，黑尔斯宣布开始执行以“完成开普勒猜想的形式证明”为目标的协作计划，通过产生可由自动定理检验软件HOL等来确认其正确性的证明，来移除残存的和证明有效性相关的不确定性。

黑尔斯认为此计划需要约20年时间，而实际上整个工作在2014年8月10日就完成了。2015年，黑尔斯和21位协作者共同发表了“开普勒猜想的形式化证明[\[3\]](https://www.zhihu.com/question/413552492/answer/1420732821?utm_source=wechat_session&utm_medium=social&utm_oi=749297898931384320#ref_3)”。

  

让人工智能直接去搞哲学的情况较少，不过自动推理本身就和哲学有很深的联系，自动常识推理还含有一些民俗学、民间物理学内容。近年来，自动常识推理在分类推理、动作和变化推理、时间推理等领域都有重大进展。GPT系列也是在自然语言方面进行自动常识推理的尝试，其原本设计目的是预测在人给出的一段文字后面出现概率较高的单词。

用人工智能研究哲学的一个办法是，程序员将他们对世界的理解进行编码抑或写一个程序来从按照他们的世界观组织起来的数据集里提取统计数据，然后让程序运行来产生在这个世界模型下必然做出的推理和结论。虽然目前还没看到谁用这种研究去灌水论文，但使用人工智能分析图像的时候已经有这样的趋势：人工智能从人们选择的数据集里发现了种族优越论、非人化等东西。至于GPT系列，你可以通过给它简单的文字让它输出看起来很有哲学味道的文本。例如Janelle Shane利用GPT-3的预览API产生的“测测你是哪种人工智能”




1988年证明屏风式四子棋是先手必胜 [https://tromp.github.io/c4/c4.html](https://tromp.github.io/c4/c4.html)
006年证明n=6时的幸福结局问题 [https://doi.org/10.1017%2FS144618110000300X](https://doi.org/10.1017%2FS144618110000300X)
开普勒猜想的形式化证明[http://arxiv.org/pdf/1501.02155.pdf](http://arxiv.org/pdf/1501.02155.pdf)
对自动推理有兴趣的话，可以参加自动推理协会。 http://aarinc.org/#](http://aarinc.org/#






计算机辅助证明简介 - 彭柯尧的文章 - 知乎
https://zhuanlan.zhihu.com/p/181671237







我们先说结论，计算机辅助证明能干什么：**计算机辅助证明可以对人写的证明进行检查，换句话说，我们可以用计算机语言把证明输入计算机，然后计算机验证证明。**



> 计算机可以根据命题自动给出证明吗？

大部分情况不行，对于一些线性不等式或者平面几何问题似乎有自动证明。再次强调计算机辅助证明**不是自动证明**，只是帮助验证人写的证明。

> 计算机辅助证明会受到哥德尔不完备定理的影响而受限吗？

受到的影响和人书写证明是一样的。哥德尔不完备定理是指蕴涵皮亚诺算术公理的体系里面会**有不能证明真命题**，类型论的公理体系当然也不例外。但证明辅助做的事情是**验证给出了的证明**，而**不是通过计算判断命题是否可以被证明**，所以某种意义上是不相干的。

> 计算机可以告诉我们我们不知道的事情或者新的结论吗？

不能，目前来说还不能。如同上一个问题说的一样，它能做的是验证人写下来的证明，还不能像人一样智能得自己去推导新结论，也许遥远的未来可能会有有办法实现。

> 计算机验证证明需要现在流行的人工智能吗？

不需要，这两者基本上完全是独立的两个东西。我们之后会讲到辅助证明是基于各种依赖类型论(dependent type theory)，完全只是运行普通的程序。人工智能能否对辅助证明起到帮助我目前还不清楚是否有相关的研究，包括解决上一个问题的提出的设想。

> 计算机验证可靠吗？会出错/bug吗？

可靠，至少比人可靠。还是像上一个回答一样，计算机辅助证明不是靠深度学习一样通过输入大量数据炼丹然后来判断证明，而是依照严格的类型论逻辑计算得到的结果。辅助证明总是基于一门计算机语言的(如后文会提到的Lean)，我们会了解到这种验证是基于该语言的**类型检查器**，而类型检查器是程序语言设计的**元理论**的部分，应该是不会轻易出现问题的(我对这方面不是完全了解，期待有懂行的大佬来解释)，或者说这些功能本来就是用来抓bug的。这就如同问计算器算加法或者用C语言可靠吗一样，当然你完全可以担心用来使用他们的前端软件出现bug，不过这就不是我们要谈论的问题了。





> 计算机辅助证明只能处理一些初等的问题？比如说组合问题？

并非如此，事实上我们人能处理的理论基本上计算机都可以处理，当然使用的公理不同在某些特定的细节有所差别。举例来说，Kevin Buzzard 等人已经使用Lean这一语言定义出了Scholze荣获菲尔兹奖的成果Perfectoid Space，也就是已经让电脑理解了这个东西[https://leanprover-community.github.io/lean-perfectoid-spaces/](https://leanprover-community.github.io/lean-perfectoid-spaces/) 。另外Lean也有社区在建立大规模数学定理库，目前对于本科生级别的数学已经建立了不少了[https://leanprover-community.github.io](https://leanprover-community.github.io/mathlib_docs/)













看到这里可能你会有疑问，连基于人工智能的聊天机器人经常都理解不了日常人说的话，完全不靠人工智能的电脑却可以理解“更难”的数学证明。然而事实上我们将会发现，利用类型论，比自然语言更形式化的数学其实是更简单的东西，计算机更容易理解。这也印证了冯诺依曼的名言

> 如果有人不相信数学是简单的，那是因为他们没有意识到人生有多复杂。

为了解释这些事情，我将参考Buzzard博客文章里的一些观点[https://xenaproject.wordpress.com/2020/06/20/mathematics-in-type-theory/](https://xenaproject.wordpress.com/2020/06/20/mathematics-in-type-theory/)

当我们在讨论数学时我们在讨论什么？实际上大体可以归结为这四种东西：**定义，(真/假)论断，证明，想法**。

**定义**，如自然数，实数，拓扑空间等概念；**论断**，如费马大定理，1+1=2，1+1=3等命题，他们是谈论数学基石，所有定义和论断，在一个公理体系下都有明确而清晰的含义。我们通过一些基本的概念来不断拓展新的命题，数学也得以发展。

而**证明**则是一种数学“正确性”的保障：尽管1+1=3是有明确含义的命题，但是我们却没法给出它的证明，甚至会给出对其否定的证明。而拥有证明的1+1=2则是得以验证的真命题。所以数学不仅是要给出新的命题，也需要给出相应的证明。

> 构造证明是一门艺术，而验证它是科学

有一定数学经验的朋友都会有这种经历：一道题自己笑不出来证明做，但翻看答案却能看懂。这也恰恰说明前者是包含一些更复杂的东西，后者只是一些按部就班的工作。

所以**想法**则是数学里最玄妙的一部分，它体现了我们对数学的理解，而人的理解不仅仅是读懂记忆了定义，命题，证明，还有更多的诸如建立联系和直觉等等难以言说的东西。想法不仅引导我们构造证明，还会引导数学家提出新的命题，发展新的理解，解决新的问题。这一部分是我们所知甚少的，也是目前科学所无法处理的。

但所幸，为了达到我们的目标，验证证明的正确性，我们只需要处理前三者。或许在集合论的框架下他们可能不尽相同，但在类型论中，他们几乎都是同一种东西：他们都是某个类型的**项**(term)。更准确地说，定义和论断我们都将其看做某个**类型**(type)(如同集合论中集合可以作为元素一样，一个类型也可以作为一个更大类型的项)，而一个证明我们视为它所对应的命题的类型的项。

为了更确切地描述这些，我们需要简要的介绍一下类型论，更详细的学习可以参看视频[https://www.bilibili.com/video/BV1bk4y1B7uy](https://www.bilibili.com/video/BV1bk4y1B7uy)。另外你同样也可以选择先进行实操，来体会一下如何证明一些自然数的基本命题[Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)。

首先如同集合论中的集合一样，类型论中的类型是先验而无法定义的。但事实上，在我们的直觉中，完全可以按照我们原来对集合的想象去想象类型，一个类型的项也可以想成集合的元素一样。事实上我们很多时候用集合，就已经是在像类型一样使用它了，只是我们不知道而已。另一方面运用范畴论去想象类型论也是一个不错的理解方式。

实际上集合论中 ![[公式]](https://www.zhihu.com/equation?tex=a%5Cin+A) 是一个命题，它存在着被否定的可能，并且其实随便给出两个 ![[公式]](https://www.zhihu.com/equation?tex=a%2CA) 都能组成命题，即便是 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmathbb%7BR%7D%5Cin+%5Cpi) 这种看起来毫无意义的东西，也是一个命题。然而事实上我们使用属于符号一般是两种情况：首先有时我们想要明确讨论的范围，强调元素是从哪来的，我们写 ![[公式]](https://www.zhihu.com/equation?tex=a%5Cin+%5Cmathbb%7BR%7D) 是想说 ![[公式]](https://www.zhihu.com/equation?tex=a) 是从实数集中取出来的，而非想要去论证 ![[公式]](https://www.zhihu.com/equation?tex=a) 是是不是实数；齐次正好相反，当我们在明确讨论范围在实数后，当我们用 ![[公式]](https://www.zhihu.com/equation?tex=a%5E2%5Cin+%5Cmathbb%7BR%7D_%2B) 来设问 ![[公式]](https://www.zhihu.com/equation?tex=a%5E2) 是否大于0，也就是说这个时候我们是要关心 ![[公式]](https://www.zhihu.com/equation?tex=a%5E2%5Cgt+0) 这样的命题是否能被证明的。这也就说明我们运用属于的时候并非所有时候都期望它是命题的，而类型论的最大的特点就是将前者从命题变成一种无须证明的**断言**(judgement)。于是我们可以把实数看做是类型，类型的项的表述 ![[公式]](https://www.zhihu.com/equation?tex=a%3A%5Cmathbb%7BR%7D) 就来代表前者这样的情况，而后者在类型论中如何表现，就要涉及到类型论如何处理命题了。

“Propositions As Types, Proofs As Terms”这句口号可以说是涵盖了类型论中对命题处理的核心Curry-Howard 同构。关于如何看待命题，从亚里士多德时带就有的将其真值看法，然而这种把命题单纯归为真和假的做法，隐含了任何命题我们经过论证都可以归为真或假这样超验的论断(并且在后来的数学发展也可以知道这是不正确的)，并且丧失了命题与证明的联系，损失了不少信息。到了弗雷格的分析哲学时，提出了一种“命题的含义就是使它为真时的情况”的说法，开启了对命题内涵的探讨。这个时候我们可以用韦恩图来表达命题，这实质上是一种“命题当做集合”的观点。





当然为了证明更具体的命题诸如 0+a=a，我们就必须要定义具体的数学结构，比如说自然数的皮亚诺算数结构等等。更具体的证明，欢迎来[Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)中体验。作为思考，大家也可以想想如何证明两个f g: monoidmorphism的复合还是 f∘g: monoidmorphism。(提示：我们只需要证明f∘g.fun=f.fun∘g.fun 满足后面两条性质，如何使用rw实现？)
















为了更确切地描述这些，我们需要简要的介绍一下类型论，更详细的学习可以参看视频[https://www.bilibili.com/video/BV1bk4y1B7uy](https://www.bilibili.com/video/BV1bk4y1B7uy)。另外你同样也可以选择先进行实操，来体会一下如何证明一些自然数的基本命题[Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)。








实际上，目前大部分本科阶段的数学内容的定理库已经被建立了[Mathlib Overview](https://leanprover-community.github.io/mathlib-overview.html) 。本科数学是大家相对比较熟悉的同时也是现代数学的基石，对其进行代码形式化是很不错的工作，并且也是一种使用证明辅助的训练。


所以Buzzard把眼光转向了下一代，通过在本科生教育阶段使用Lean等工具，不仅可以起到教学的帮助，也可以让学生对辅助证明打下基础，还更可以在过程中给定理库添砖加瓦。实际上他的[Xena Project](https://xenaproject.wordpress.com/what-is-the-xena-project/)正是如此，一边进行教学，一边进行完善定理库。而效果也是喜人的，本科生不仅表现出了惊人的学习效率，甚至还可以在此帮助下理解本科之上的数学内容。









单纯靠我这样一篇文章学习当然是不够，但若这激起了你的兴趣的话，我们可以提供一些指引。首先市面上其实有不少具有能进行证明辅助功能的计算机语言，但大部分都是计算机方向的人研究使用。目前一个受到很多数学人关注并且有希望能真正在数学上使用的语言是[LEAN](https://leanprover.github.io/)，我们也推荐使用LEAN来进行相关的学习。评论区里 

[@药罐子千里冰封](https://www.zhihu.com/people/67ebe1bd8e4a63f17a42572e40afaac7)

 提到的[Arend](http://arend-lang.github.io/)也是一个有潜力的语言，它甚至是基于一种类似于HoTT的CuTT类型论，在我看来其实会更方便，不过目前还没有足够多的积淀，期待其未来会成为一种更好的工具。

要学习Lean，毫无疑问我们首先再次推荐Buzzard编写的在线交互式教程[Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/) 无须任何麻烦配置，使用一款现代浏览器打开就能玩(另外还有功能更全的在线编辑器[lean-web-editor](https://leanprover-community.github.io/lean-web-editor/))。这个教程将会手把手引导你完成自然数相关的基本定理证明，而完成这个游戏后你将开始逐渐理解这一切，也有助于更深入的学习。视反响我们可能会对考虑其进行翻译和搬运。

而后续的学习可以参考[https://leanprover-community.github.io/learn.html](https://leanprover-community.github.io/learn.html)里的各种资料。其中比较适合数学相关背景的进一步学习的是[Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/)。关于Lean在本地安装配置请参考[https://leanprover-community.github.io/get_started.html](https://leanprover-community.github.io/get_started.html)

Lean有一个由社区构建中的数学定理库Mathlib，里面已经构建起了很多本科程度的数学[Mathlib Overview](https://leanprover-community.github.io/mathlib-overview.html)，更详细的文档可以查看[mathlib documentation](https://leanprover-community.github.io/mathlib_docs/)。我们鼓励本科生通过Lean的方式来学习数学，同时也鼓励大家试着去构建还没补全的定理。

同时将Lean应用在教育中也是提倡的，Buzzard发起的[Xena Project](https://xenaproject.wordpress.com/what-is-the-xena-project/) 就是通过Lean进行本科生数学教学

当然我们也鼓励大家与人交流学习，有条件的话可以加入[Lean Zulip chat](https://leanprover.zulipchat.com/)，这是Lean最活跃的一个社区，里面不管问什么都会有人很快来回复。




另外如果对一些类型论基本理论感兴趣，我们也有推荐的一些相关视频

[https://www.bilibili.com/video/BV1bk4y1B7uy](https://www.bilibili.com/video/BV1bk4y1B7uy) 本视频讲解了类型论，并且比较了类型论与集合论的异同，适合入门看。

[https://www.bilibili.com/video/BV1cb411z79V](https://www.bilibili.com/video/BV1cb411z79V) 本视频讲述了类型论中存在的同伦(模型范畴)结构，由此也引出了同伦类型论(HoTT)。另外此up主[https://space.bilibili.com/6897517](https://space.bilibili.com/6897517) 还有搬运很多其他的相关视频。

如果希望了解更多HoTT和泛等基础(Univalent Foundation)相关的内容，可以参看Voevodsky本人的介绍[https://www.bilibili.com/video/BV1454y1S7Kf](https://www.bilibili.com/video/BV1454y1S7Kf)

以及这个在有一定经验和直观感受后，比较详细的HoTT相关的Univalent的一些例子和构造[https://www.bilibili.com/video/BV1Yp4y1i7ri](https://www.bilibili.com/video/BV1Yp4y1i7ri)

## 1.1. 结语

我从学习证明辅助之初，就在自己的社交圈范围内极力推广它，虽然收获了一定反响，但基数相对就较少。但经过 

[@陆zz](https://www.zhihu.com/people/6dd067bf5573f2a38d487ab6f67b0431)

 的提醒，我才想起来我还有知乎账号可以用作宣传(太久没用知乎了)。于是便写了这篇，以及未来可能会有的一系列文章和答案。之前给朋友讲解的经验也成为了我的成文的基石。

我们现在已经习以为常使用的TeX排版，起初也离不开王垠等先驱的在国内的宣传(虽然后来他又开始黑)。虽然我无法自比王垠，但我也希望能通过我的文章能让大家对[数学的未来](https://www.bilibili.com/video/BV1YE411r7Qw)有所了解，也希望更多数学领域相关的朋友能




















