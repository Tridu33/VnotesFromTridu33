[2020 https://zhuanlan.zhihu.com/p/103794964](https://zhuanlan.zhihu.com/p/103794964)




# 1. Google Summer of Code 2019







[申请之前的准备https://zhuanlan.zhihu.com/p/27823910](https://zhuanlan.zhihu.com/p/27823910)


至于贡献的时间，窃以为比较理想的时间是前一年的 12 月份或者同年的 1 月份开始，就要尝试着去给社区做一些微小的工作。这些工作包括但不限于：

-   贡献代码，无论什么社区，都喜欢高质量的 PR
-   Review PR，给别人的 Review 点赞
-   提交 Bug
-   添补更新文档
-   在 IRC 里解决别人的问题



申请真正开始于谷歌公布的 Mentoring organizations 列表，这里大致介绍下其内容。

以 2017 年 GSoC 其中的一个开源组织 [The Processing Foundation](https://link.zhihu.com/?target=https%3A//summerofcode.withgoogle.com/organizations/4962961559912448/) 为例，介绍一下 GSoC 主页上 organization 的页面布局。每个 organization 都会有一段介绍性的文字，这个不是很关键。右边的一栏是比较重要的，其中 Technologies 是方便大家在搜索 organization 的。上面的 VIEW IDEAS LIST 比较重要，一般来说每个社区会事先提出一些他们期望的 idea，学生可以就这些 idea 进行申请。当然社区也鼓励学生提出自己的 idea。其下的 Chat 和 Email 一般来说会写明该社区常用的交流工具，在申请的过程中往往需要频繁地与社区相关人员交流。





## 1.1. 正式申请

Proposal，是一个申请时很关键的材料。它是学生在申请时需要提交的一个设计文件，在其中，学生往往需要写明自己的背景（学术背景，开源贡献经历等），对 idea 的了解与认识，以及大致的实现思路和方法。Proposal 的书写是没有定式的，只要可以突出你的长处就好，这是社区对你了解的唯一途径，所以需要你把自己所有的优势都要写在其中。

[Proposal for Processing.R](https://link.zhihu.com/?target=https%3A//docs.google.com/document/d/1b0HhRVKtCJkDaxP9dfSwzthzX0FRv6Y_0Yk58r634TA/edit%3Fusp%3Dsharing) 是我在申请时的一份 Proposal，可以列为参考，介绍下常规的写法。

首先是 Project Description，这个部分就是让社区知道你对 idea 没有理解错，你深刻地了解这个 idea 想做的是什么。三言两语就好了。

然后是 Implementation，我个人觉得是比较重要的部分。要向社区证明你已经有了完整的实现思路，现在差的就是写代码实现而已了。

其次，是 Development Process，社区肯定更喜欢那些风险低，feature 吸引人的申请。一个好的 schedule 可以让社区相信你是真的已经做好了准备。精确到天自然最好，但是基本来说比较难，周和月都是不错的选择。不过有一点需要注意，不要把所有时间都安排的满满的，还是需要有一些 buffer 的。不然看起来太假了 =。=

最后是 About Me，因为我对于申请的项目而言，没有什么积累，而且没有相关领域的贡献，所以把这一项放在了最后。如果你是申请 Kubernetes，而日常是 Docker 的 contributor，那把 About Me 放在最前面是更好的选择，完全看申请而定。

一般来说这些是都要有的，还有一些其他的，社区特定的要求，这个也是要注意的。这里还有一些我认为写的比较好的 proposal：

-   [Integrate Unikernel Runtime](https://link.zhihu.com/?target=https%3A//docs.google.com/document/d/1Vld4j0B-wk1A1827gIc5fzWHJlzQVqcYQnCAKJwe_ZM/edit%3Fusp%3Dsharing)
-   [Optimization of Distance Between Methods in Single Java Class](https://link.zhihu.com/?target=https%3A//docs.google.com/document/d/1lWXpWhUN6cE06sjQANjWxamc_X3ddbSphTRSofChLyk/edit%3Fusp%3Dsharing)

感兴趣也可以看下。

## 1.2. Community Bonding Period

走到这一步，离拿钱就不远了，因为 GSoC 申请比完成更难。在 Community Bonding Period，你需要跟自己的 mentor 建立联系，积极融入社区等等，但是没有量化的标准，这个就不再多说了。

## 1.3. 开始写码

写码这个，不同的项目有不同的要求。有一部分项目是给开源的 repo 贡献代码，因此要走整个 review 的流程，这想必大家都比较熟悉，不再多说。但是还有一部分项目，是 standalone 的，就是自己开了个 repo，自己写，比如我申请到的 [Processing.R](https://link.zhihu.com/?target=https%3A//github.com/gaocegege/Processing.R)。这就会有很多问题，这里也着重说一下对于这一类项目的建议。

首先，要明确之前 proposal 里写的 schedule 只是为了给社区信心的，事实上在开始写码之前，mentor 会跟你重新制定计划。所以如果你在 Community Bonding Period 写了很多 feature，很可能没有用，因为 mentor 说不定会给你重新制定要求。

关于 standalone 的项目，跟 mentor 以及社区其他成员的交流是很关键的。因为你的 repo 别人都是没有 watch 的，所有的变动，可能只有你和你的 mentor 知道。如何让社区里的其他人看到你的贡献，非常重要。所以尽可能多在 IRC 里跟大家分享你遇到的问题，或者你的项目中的新 feature，可能会让你感觉到自己不是玩单机游戏。

其次就是要尽早引入 CI，并且所有变动都以 PR merge 的方式进行，以保证代码质量。一个人的项目，质量很容易滑坡，CI 和 PR 可以让 mentor 对你的代码有一个很好的 review 体验，他也会更加积极一点。

最后是不要太肝。因为自己的项目，每个 PR 的生命周期都是由自己负责的，很容易就会进入疯狂开发的状态，但是记住上面说的，在开始写码之前，mentor 会跟你重新制定计划 :)

## 1.4. Evaluation 与奖金发放

Evaluation 是一个双向的评估，mentor 会评估学生的工作完成度如何，学生会评估社区和 mentor 对自己的帮助是否到位，学生对社区的评估可能会影响社区明年能够参加 GSoC 以及 slots 的数量，mentor 的评估决定学生能否拿到奖金。

如果通过了 evaluation，奖金会在几天内到账。

## 1.5. **注意事项与 Tips**

1.  **只有**学生才可以申请 GSoC。
2.  一般来说 GSoC 主页需要科学上网才能访问。
3.  时差问题是申请的时候需要注意的问题，这个需要格外注意，每年都有人错过申请。
4.  奖金的发放是通过 [Payoneer](https://link.zhihu.com/?target=https%3A//www.payoneer.com/home/) 发放的，如果是非美元账户，需要支付 4% 左右的换汇费用。
5.  第一次入选 Mentoring organizations 的组织原则上只有 1 个或者 2 个 slots。


## 1.6. **结语**

  

这是一篇摸鱼作，希望能够对各位有所帮助。其实大家在选择开源社区的时候可以多问问有经验的人，尽可能选择一个友好的社区作为开始，这样会在开源的路上走的远一点。另外如果你在申请 GSoC 的过程中有什么疑惑，欢迎加入 [GSoC CN](https://link.zhihu.com/?target=https%3A//github.com/gsoc-cn/gsoc-cn) 的在线聊天频道 [Gsoc-cn/Lobby](https://link.zhihu.com/?target=https%3A//gitter.im/Gsoc-cn/Lobby)。GSoC CN 是一个由国内的参加过 GSoC 的同学们创建的社区。














































[Google Summer of Code 2019](https://summerofcode.withgoogle.com/archive/2019/projects/5460192307707904/)


粗暴Tensorflow2教程是优秀的例子













