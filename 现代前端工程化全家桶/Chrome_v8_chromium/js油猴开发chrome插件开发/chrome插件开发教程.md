https://github.com/bingoogolapple/bga-chrome-plugin-note
从项目demo开始是最快的开发方法






# 1. chrome插件开发教程

如何从零开始写一个 Chrome 扩展？ - 动感小前端悄悄地的回答 - 知乎
https://www.zhihu.com/question/20179805/answer/101984352



文档
[https://support.google.com/chrome/a/answer/2714278?hl=zh-Hans](https://support.google.com/chrome/a/answer/2714278?hl=zh-Hans)



chrome 插件文档翻译[https://github.com/ccforward/chrome](https://github.com/ccforward/chrome)











[教程https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html](https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html)

配套源码：

《Chrome插件开发全攻略》配套完整Demo，欢迎clone体验 [http://blog.haoji.me/chrome-plugin-de…](http://blog.haoji.me/chrome-plugin-develop.html)






作者：岑武斌  
链接：https://www.zhihu.com/question/20179805/answer/48191009  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

直接看谷歌的官方文档，写的非常赞。  
一开始有一个例子 [https://developer.chrome.com/extensions/getstarted](https://link.zhihu.com/?target=https%3A//developer.chrome.com/extensions/getstarted)，他帮你都写好了，你按着他说的，把一个个文件都搞下来，就能弄出一个extension，然后他会指引你了解一下chrome extension的架构，搞清楚各个文件的功能 [https://developer.chrome.com/extensions/overview](https://link.zhihu.com/?target=https%3A//developer.chrome.com/extensions/overview)。我觉得这部分看了不一定能知道怎么做，但是了解一下还是很有帮助的，当你遇到一个需求的时候，你至少大概能知道要用哪种类型的技术，比如说应该用content.js还是event.js之类的，他讲的很清楚。  
从上面提到的两个文档，根据他的提示，把一些该看的都看了，一些暂时用不上的功能，我觉得可以先不看，还是以任务驱动吧，想想自己想做什么，然后实践出一个demo来，干看的话可能记不住，也理解不深。  
他还提供了好多例子，[https://developer.chrome.com/extensions/samples](https://link.zhihu.com/?target=https%3A//developer.chrome.com/extensions/samples)，各种功能都有，下载下来看看人怎么写的就好，当然主要是看配置文件，一些权限管理什么的。API的使用文档里说的很清楚也有例子，实在不行就网上搜就好了，用一回就明白了。  
实际开发中遇到困难，求助stackoverflow就好了，各种答案。  
说到底，除了要借助一点点的chrome API以外，其余的就是普通的js html 和 css，没什么东西，很容易学。  
边看文档边实践边Google就能做出东西了，先把东西做出来，然后再把东西优化做精。  
我也是最近才开始学的，某课程大作业需要用，做了一个模仿evernote剪藏的插件，关于chrome extension的经验还有待整理，等整理完了再来补充下答案~




360把Chrome的开发文档翻译了[http://open.chrome.360.cn/html/dev_doc.html](https://link.zhihu.com/?target=http%3A//open.chrome.360.cn/html/dev_doc.html)

**一个 Chrome 扩展其实就是一个配置（入口）文件 manifest.json 和一系列 html、css、js、图片文件的集合**，所以只要有前端基础，写一个简单的 Chrome 扩展是分分钟的事情。
## 1.1. debug
右键Chrome工具栏的小图标会弹出一个窗口，选择**审查弹出内容**即可调试。  
但是这种方法极度低效，直接chrome://extensions/找到你插件的ID：

然后浏览器访问：

```text
chrome-extension://<插件ID>/插件入口html文件
```

比如我的是：

```text
chrome-extension://fnfchnalfnjbjbfeccpophocngdgapad/index.html
```

然后就可以愉快的调试了。



```js
location.reload()
```



调试，如果是覆盖新标签页的应用，直接右键审查元素，加断点，刷新即可。

2.如何查看其他插件的源码

访问chrome://version 找到Chrome插件安装的本机目录:


然后找到extension目录，所有插件和数据都在这里，可以随便参考其他插件源码。

3.不要把JS代码写在html文件里

出于安全考虑，入口html文件中的JS代码只能通过script标签引用外部脚本文件，内嵌的JS代码会失效的。

4.注意国际化

webstore面向的是全球用户，你辛辛苦苦写的小工具肯定不想只限于国内用户吧，所以在你的项目里面加上_locales文件夹，写代码的时候时刻考虑到如何才能更好地支持国际化。

5.用好Google

开发遇到的问题Google一下一般能找到，StackOverflow 和Google网上论坛这两个站点要尤其留意，大部分问题这上面都有解决方案。

更多小技巧就不一一列举了，多看官方文档，有更详细的介绍。

应用发布

应用写好之后打包上传就好了，上传时Google会让你提供几张宣传图片（自己随便ps了一下）每一个需要填写的选项后面都有详细说明，需要认真阅读一下。

发布之后大概过上几个小时就能在webstore搜索到你的应用了：

  
  
作者：动感小前端悄悄地  
链接：https://www.zhihu.com/question/20179805/answer/101984352  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。








# 2. 发布到chrome


推荐用收费的VPN，以便于后续的一系列工作。不要把精力都花在了弄免费的翻墙工具上，毕竟收费的也不贵。

万里长城第一步，不必去办VISA卡

要想在Chrome网上应用店（下文简称webstore）发布应用，需要在webstore[的开发者信息中心](https://link.zhihu.com/?target=https%3A//chrome.google.com/webstore/developer/dashboard/)注册一下，填信息的时候你会发现没有中国大陆地区，所以Google在暗示天朝人民要用假的地址注册，于是我机智的选择了宝岛台湾。

然后Google还要你提供一个VISA/MasterCard账号，用来缴纳5美元注册费。我差点就真去办VISA卡了，后来网上一查，国内的VISA卡可能会认证失败，去淘宝上买虚拟卡又不放心，奋战一小时后我发现一个神奇的网站：[全球付](https://link.zhihu.com/?target=https%3A//www.globalcash.hk/).

mastercard

这网站专门用来搞全球购物的，冲100块钱，自动给你生成MasterCard账号，然后你就可以拿这个卡号信息去注册webstore开发者了，分分钟验证通过，并没有网友说的那么麻烦。

至于剩下的钱，你可以买点儿别的，或者转到其他银行卡里,机智如我。

应用开发 基础入门

webstore有四种程序类别：应用、游戏、扩展程序、主题背景。  
放心，都是用JS来写的，对于前端来说只有一星门槛。本文不会讲具体基础开发知识，因为这里已经有非常好的教学资料了：

-   [Chrome 扩展及应用开发](https://link.zhihu.com/?target=http%3A//www.ituring.com.cn/book/1421).来自图灵社区的免费电子书，适合入门。
-   [Chrome扩展开发文档](https://link.zhihu.com/?target=http%3A//open.chrome.360.cn/extension_dev/overview.html).来自360极速浏览器翻译的官方文档。
-   [Chrome 插件开发官方文档(英文)](https://link.zhihu.com/?target=https%3A//developer.chrome.com/extensions).前两个适合入门，实际开发的时候还是推荐官方的，查API啥的都很方便。

  
  
作者：动感小前端悄悄地  
链接：https://www.zhihu.com/question/20179805/answer/101984352  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。








































