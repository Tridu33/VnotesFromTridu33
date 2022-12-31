# 1. Android未来


2020年Android开发的前景如何？ - 奶盖的文章 - 知乎
https://zhuanlan.zhihu.com/p/105091568

- 音视频开发

 GitHub 开源的 [CarGuo/GSYVideoPlayer](https://link.zhihu.com/?target=https%3A//github.com/CarGuo/GSYVideoPlayer) 用户还不少，所以被逼着成了半桶水的音视频开发。
**未来 5G 时代音视频方向肯定会继续红火。**
**然而事实上一旦做了音视频开发，你就会发现音视频方向其实和 Android 没有太大的必然联系，因为音视频开发是服务于 Android ，而非用 Android 去开发音视频。**
音视频开发首要的是需要学习 `C++` ，学习 `FFMpeg` 开源项目，了解音视频的编码协议、容器封装和网络协议，最后对于 Android 来说就是 NDK 开发，然后还需要给 iOS 等其他平台音视频服务，因为如果音视频项目只服务于 Android 是不现实的，感兴趣的可以看看下面我写过的相关基础概念。
**[《移动开发者的音视频基础知识》](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/HjSdmAsHuvixCH_EWdvk3Q)**
**所以选择音视频开发就要让自己不局限于 Android ，并且这个方向会是偏低层的学习，所以会比较累但是技术会相对稳定。**

- 大前端

**大前端是 Android 开发不可逃避的方向**，因为随着 Android 开发和 iOS 开发红利的消失，整个市场招聘开始趋向稳定，如今 Android 和 iOS 的基础门槛已经不高，所以和前端融合是不可避免的节奏。
都是做 UI 和动画的，跨平台自然成了企业期望的选择：**跨平台使得代码逻辑可以复用，减少各平台同一逻辑因人而异的开发成本。对于企业而言，一套业务逻辑可以在多处使用是最理想也是最保险的，同时也可以一定程度的优化做界面开发的人员。**
**[《做Android开发的，想转行，如何选择呢？》](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/fV0WTujkpNM1tFUCwsM_vw)**
**所以跨平台不算是一个方向，而是正常前端和客户端开发人员的能力拓展**，如果继续从事做大前端的，就必须有心理准备：**拥抱技术红利，拥抱技术更新，说人话就是“学不动也要学”，要保证自己的知识迁移能力与架构能力**。（*Cordova、uni-app、React-Native、Weex、Flutter、Kotlin-Compose、Swift 这些都只是开始*）
**[《谁告诉你 Flutter 会干掉原生开发？》](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/1bp2gtoYRIIvxgGP2UCHig)**
但是事实上看着技术框架和技术路线很多，但是本质上思维方式是通用的。

- Android安全方向（逆向，渗透）

刚好我有一个 360 做安全方向的朋友，从他日常发的招聘信息比较少看到这个方面，从我理解上更多是招牌 **安全方向（逆向，渗透） 的相关人员，然后他可能对 Android 攻防比较了解，而不是从 Android 开发转过去，毕竟安全领域除了“社会攻防”外，更多的还是网络协议、计算机原理、linux 安全等方面的运用。**
因为关于这个我涉猎不多，没办法给出比较好的建议。
4、Android应用架构开发（框架开发，应用架构）
**事实上这个方向除了大厂的超级 App，基本上在以后的中小型团队不会有**，毕竟一个普通应用的搭建现状基本很成熟，比如 ***ViewModel + DataBinding + Realm + Dagger2 + Retrofit + Glide\*** 就可以搭建出一套不错的应用开发，谷歌的 Jetpack 项目也相对成熟。
**而对于大厂的超级 App ，因为涉及多部门开发，所以一般才会有基础架构搭建的**，比如：*做一些通用的组件池，通用的技术架构支撑，搭配各种监控产品和数据上报等功能*，但这时候的 Andriod 开发也不只是普通的 Android 应用架构开发，比如：

- *美团的 MRN 、Mach 等项目就需要跨平台大前端开发的能力；*
- *闲鱼的项目从 RN 到 Flutter 的搭建再到**[Flutter+Serverless 研发实践](https://link.zhihu.com/?target=https%3A//www.jianshu.com/p/d7694913102e)*

这些都离不开大前端的路线支持，**所以未来 Android 应用的架构开发和大前端是一起发展的路线。**
**反而是面向 Android Framework 和 HAL 层的开发人员会有不一样的选择，这类相关的从业者可能会参与到各种物联网智能设备上开发上。**
Android 平台和 iOS 平台最不同的就是它的开源和影响力，多年后的今天，Android 已经不仅仅代表着手机平台，在电视、机顶盒、楼宇安防、自动售卖、广告展牌、智能家电、车载等领域都已渗透并精进，**现在还从事单纯 App 的 Android 开发的反而不多，但是在以上领域继续耕耘 Android 的反而很多。**
5G 时代下物联网领域很有可能具备新的机会，华为的鸿蒙智慧屏、无人驾驶的车载平板、其他各类利用 Android 实现的无线智能平台，这都是 Android 开发者可以耕耘的机会。




