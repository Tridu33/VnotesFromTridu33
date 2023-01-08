# Taro（react） vs uni-app(Vue) 选型对比


  
作者：jianfly  
链接：https://zhuanlan.zhihu.com/p/55903320  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。







总结：taro在性能优化上做的更细致，使用uni-app需要自己注意代码优化。


综合比较，uni-app跨端质量更好，真实跨端案例也更多。

两个框架都在官网放上了众多案例，只是taro案例清一色是微信小程序，没看到其他端，难道大家使用taro，只是为了用react开发微信小程序，不需要跨端？

uni-app的案例什么平台都有，很多App做了多个平台。说起来我们领导还问过跨iOS、Android App的事情，不过目前另有原生团队，我们也只是做个备份调研。最终还是决定先把前端的技术统一了，稳定后再考虑App是否也迁移到这类框架下。

  

taro的安装及使用：

```text
# 全局安装 @tarojs/cli
$ npm install -g @tarojs/cli
# 创建 taro 项目
$ taro init myApp
# 进入项目目录
$ cd myApp
# 运行到微信小程序，调试模式
$ npm run dev:weapp
# 发行到微信小程序
$ npm run build:weapp
```

uni-app的安装及使用：

```text
# 全局安装 vue-cli
$ npm install -g @vue/cli
# 创建uni-app项目
$ vue create -p dcloudio/uni-preset-vue my-project
# 进入项目目录
$ cd my-project
# 运行到微信小程序，调试模式
$ npm run dev:mp-weixin
# 发行到微信小程序
$ npm run build:mp-weixin
```

开发流程方面，taro和uni-app均是以微信小程序为基础，也都针对小程序的开发弊端，提供了更优秀的体验，比如：

-   均支持使用 npm/yarn 安装管理第三方依赖
-   均支持使用 ES6 甚至更新的ES规范
-   均支持使用 less/scss/ts 等预编译器
-   均支持进行应用状态管理，taro 支持 Redux/Mobx，uni-app 支持 vuex


开发工具方面，taro官方未特别推荐IDE，但提供了vscode支持的d.ts； uni-app推荐的开发工具是他自家的HBuilderX，用它可以不配环境，开箱即用； hbuilder以前接触过，当时没深研究，新版还挺让我意外，真没想到国人的开发工具可以做到这样，尤其是他家的markdown支持真心不错，于是本文就是在hbuilder里写的（已经有情感分了哈哈）。

总结：两个框架都支持现代前端开发流程。hbuilder对uni-app提供了优化定制，但对不熟悉的开发者有一定适应成本。另外hbuilder自带一个编译器，和cli装在项目下的编译器是2个，这个坑不少新人要注意别踩。

 Taro通过Github Issues+微信群方式交流，微信群活跃，贡献代码的人也多。

uni-app有专门的论坛，还有视频教程，QQ群微信群都活跃。

另外文档角度，uni-app的文档比taro要完善，数了数交流群的数量，也是uni-app多不少。







为什么uniapp不能完全兼容h5，而要自建生态并且走向小程序规范？ - an wang的回答 - 知乎 https://www.zhihu.com/question/344661200/answer/815553706

评论区亮点

































