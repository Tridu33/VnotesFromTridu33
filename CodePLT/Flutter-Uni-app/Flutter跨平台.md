#  Flutter是谷歌推出的一个全新的跨平台的开发框架。


## 首先你要搞清楚什么才是跨平台的真正目的。任何跨平台无非就是以下几种方式去解决问题：

-   语言层面编译转换一下，编译成C语言或者字节码之类的，能够运行在不同的设备上面，但是这个语言转换过程很复杂，而且还需要做移植的工作。比如著名的：swiftUI，kotlin-native就是这类型的跨平台框架。
-   自带渲染引擎，不依赖于任何平台，一套代码就可以自动编译成多个平台的应用程序。比如：Flutter
-   中转类型的框架，使用JS衔接原生平台的一些功能，要么由社区开发者自己维护一套扩展兼容库，要么本身带有一系列的兼容库，但是还是摆脱不了Web的环境和编程思想，全部依赖于JS，如果不熟悉JS的朋友，去用这种类型的框架开发跨平台应用程序，简直是灾难。这类型的框架有：React Native，Weex，当然也包括楼主提出的5+app以及uni-app。

  
  
作者：AWeiLoveAndroid  
链接：https://www.zhihu.com/question/330607558/answer/962409108  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。











为什么国内的uniapp一直没人讨论呢？ - AWeiLoveAndroid的回答 - 知乎 https://www.zhihu.com/question/330607558/answer/962409108






1.你只需要使用Dart语言写一套代码，即可自动编译到各个平台，目前支持Android,iOS,Web(Beta)，Desktop(Alpha)，当然也有Windows PC和linux平台的兼容支持官方正在研发中。所以你完全不用担心框架内部是如何帮你实现的。你只需要一个命令行就可以在对应平台运行你的代码了，比如：flutter run xxx，这里的xxx指的是你的平台设备名称，比如“flutter run chrome"表示将程序运行在浏览器上面。  
2.高性能高一致性。你的代码编译出来的程序可以达到60bps的高性能。  
3.丰富的组件支持，你完全可以按照你的想法去做，扩展性非常强大，MD风格的，以及ios风格的组件都有，足够满足平时开发需求。而且Flutter基于react以及flex的思想进行布局，Dart语法很像JS+Java+Swift+Kotlin+C#+TypeScript+JavaScript+PHP，虽然表面上没有使用web开发，但是你完全不用担心，你仍然可以进行开发，只是语言写法不一样，但是这里面很多都是熟悉的东西，基本上上手成本也是很低的。  
4.丰富的社区支持。目前常用的组件以及一些第三方包都有大佬开源出来了，足够应对平时的开发了。如果你不清楚的话，也没干系，我特意收集了Flutter工具集合，这里面啥都有，足够让你可以快速找到你要的东西，你可以点进来看看：[https://github.com/AweiLoveAndroid/Flutter-learning/](https://link.zhihu.com/?target=https%3A//github.com/AweiLoveAndroid/Flutter-learning/)  
5.开源免费的。你可以随意修改内核引擎代码，以及组件代码，定制化的开发，比如闲鱼，腾讯，字节跳动等大厂都基于Flutter进行针对他们的App开发做了定制化的整合方案，当然你要是感兴趣的话，你也可以这么做。
