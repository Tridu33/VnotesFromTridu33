# 1. SDK




[科大讯飞https://www.iflyrec.com/?from=mzpzhihu](https://www.iflyrec.com/?from=mzpzhihu)











百度语音支持英语实时识别，需要部署SDK（安卓／iOS／Linux），语言选择可以参考右边链接中PID 参数设置部分 [文档中心--百度AI-百度AI-AI开放平台](https://link.zhihu.com/?target=http%3A//ai.baidu.com/docs/%23/ASR-Android-SDK/top)






# 2. **开源语音识别库**
5 款不错的开源语音识别/语音文字转换系统 - Linux中国的文章 - 知乎 https://zhuanlan.zhihu.com/p/70246657

 ## `DeepSpeech 项目`


该项目由 Firefox 浏览器的开发组织 Mozilla 团队开发。它是 100% 的自由开源软件，其名字暗示使用了 TensorFlow 机器学习框架实现去功能。

换句话说，你可以用它训练自己的模型获得更好的效果，甚至可以用它来转换其它的语言。你也可以轻松的将它集成到自己的 Tensorflow 机器学习项目中。可惜的是项目当前默认仅支持英语。

它也支持许多编程语言，例如 Python（3.6）。可以让你在数秒之内完成工作：


## 2.1. Kaldi 
是一个用 C++ 编写的开源语音识别软件，并且在 Apache 公共许可证下发布。它可以运行在 Windows、macOS 和 Linux 上。它的开发始于 2009。

Kaldi 超过其他语音识别软件的主要特点是可扩展和模块化。社区提供了大量的可以用来完成你的任务的第三方模块。Kaldi 也支持深度神经网络，并且在它的网站上提供了[出色的文档](https://link.zhihu.com/?target=http%3A//kaldi-asr.org/doc/index.html)。

虽然代码主要由 C++ 完成，但它通过 Bash 和 Python 脚本进行了封装。因此，如果你仅仅想使用基本的语音到文字转换功能，你就会发现通过 Python 或 Bash 能够轻易的实现。

-   [项目主页](https://link.zhihu.com/?target=http%3A//kaldi-asr.org/)


Kaldi是一个用C ++编写的语音识别工具包，项目其宗旨就是为了给语音识别研究人员使用，因为kaldi拥有大多数标准技术的代码和脚本，包括所有标准线性变换，MMI，增强MMI和MCE判别训练，以及特征空间判别训练（如fMPE，但基于提升的MMI），使得国内大部分语音识别领域的专家学者其语音研究结果都是基于kaldi来进行的。

  

>作者：知乎  希尔贝壳  :
>
>还有一个就是数据开源：这里不得不提我们**aishell-2**，其数据规模达到了1000个小时。这是迄今为止全球最大的中文开源测试集，当然这是我们免费开源的，说实话当初提出这个想法的时候我们自己都吓一跳，花费大量人力物力做出来的数据，最终是免费在kaldi进行开源。虽说很肉疼，但是看到语音人对我们的认可，我们觉得还是很值得。

  
  




## 2.2. `Julius`


它可能是有史以来最古老的语音识别软件之一。它的开发始于 1991 年的京都大学，之后在 2005 年将所有权转移到了一个独立的项目组。

Julius 的主要特点包括了执行实时 STT 的能力，低内存占用（20000 单词少于 64 MB），能够输出 *最优词(N-best word)*和 *词图(Word-graph)*，能够作为服务器单元运行等等。这款软件主要为学术和研究所设计。由 C 语言写成，并且可以运行在 Linux、Windows、macOS 甚至 Android（在智能手机上）。

它当前仅支持英语和日语。软件应该能够从 Linux 发行版的仓库中轻松安装。只要在软件包管理器中搜索 julius 即可。最新的版本[发布](https://link.zhihu.com/?target=https%3A//github.com/julius-speech/julius/releases)于本文发布前大约一个半月之前。

-   [项目主页](https://link.zhihu.com/?target=https%3A//github.com/julius-speech/julius)







## 2.3. `Wav2Letter++`


如果你在寻找一个更加时髦的，那么这款一定适合。Wav2Letter++ 是一款由 Facebook 的 AI 研究团队于 2 个月之前发布的开源语言识别软件。代码在 BSD 许可证下发布。

Facebook 描述它的库是“最快、 *最先进(state-of-the-art)*的语音识别系统”。构建它时的理念使其默认针对性能进行了优化。Facebook 最新的机器学习库 [FlashLight](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/flashlight) 也被用作 Wav2Letter++ 的底层核心。

Wav2Letter++ 需要你先为所描述的语言建立一个模型来训练算法。没有任何一种语言（包括英语）的预训练模型，它仅仅是个机器学习驱动的文本语音转换工具，它用 C++ 写成，因此被命名为 Wav2Letter++。

-   [项目主页](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/wav2letter)

## 2.4. `DeepSpeech2`



中国软件巨头百度的研究人员也在开发他们自己的语音文字转换引擎，叫做“DeepSpeech2”。它是一个端对端的开源引擎，使用“PaddlePaddle”深度学习框架进行英语或汉语的文字转换。代码在 BSD 许可证下发布。

该引擎可以在你想用的任何模型和任何语言上训练。模型并未随代码一同发布。你要像其他软件那样自己建立模型。DeepSpeech2 的源代码由 Python 写成，如果你使用过就会非常容易上手。

-   [项目主页](https://link.zhihu.com/?target=https%3A//github.com/PaddlePaddle/DeepSpeech)
- 





## 2.5. ASRT语音识别中文


开源的语音识别首先推荐的当然就是**ASRT语音识别项目**

这是一个基于中文的语音识别开源项目，GitHub地址为：

https%3A//github.com/nl8590687/ASRT_SpeechRecognition

项目主页：https://asrt.ailemon.me

ASRT是一套基于深度学习实现的语音识别系统，全称为Auto Speech Recognition Tool，由AI柠檬博主开发并在GitHub上开源(GPL 3.0协议)。本项目声学模型通过采用卷积神经网络（CNN）和连接性时序分类（CTC）方法，使用大量中文语音数据集进行训练，将声音转录为中文拼音，并通过语言模型，将拼音序列转换为中文文本。算法模型在测试集上已经获得了80%的正确率。基于该模型，在Windows平台上实现了一个基于ASRT的语音识别应用软件，取得了较好应用效果。这个应用软件包含Windows 10 UWP商店应用和Windows 版.Net平台桌面应用，也一起开源在GitHub上了。

ASRT语音识别系统的声学模型采用了深度全卷积神经网络，直接将语谱图作为输入。模型结构上，借鉴了图像识别中效果最好的网络配置VGG，这种网络模型有着很强的表达能力，可以看到非常长的历史和未来信息，相比RNN在鲁棒性上更出色。在输出端，这种模型可以和CTC方案可以完美结合，以实现整个模型的端到端训练，将声音波形信号直接转录为中文普通话拼音序列。在语言模型上，通过最大熵隐含马尔可夫模型，将拼音序列转换为中文文本。并且，为了通过网络提供服务给所有的用户，本项目还使用了Python的HTTP协议基础服务器包，提供基于网络HTTP协议的语音识别API，客户端软件通过网络，调用该API实现语音识别功能。


现在有什么开源的语音识别吗？ \- zahet的回答 - 知乎 https://www.zhihu.com/question/23473262/answer/812989806


# 3. 教程


语音识别有哪些好的资料（基础点）？ \- 杨超的回答 \- 知乎 https://www.zhihu.com/question/355153863/answer/903999833






































































































