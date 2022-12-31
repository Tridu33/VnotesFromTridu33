[TOC]

# 立志而无恒，终身事难成。——曾国藩

https://zhuanlan.zhihu.com/p/456545784
npm打包
发布npm包




# npm命令学习

https://www.jianshu.com/p/30ef3c874c1e








# npm 模块安装机制简介


www.ruanyifeng.com/blog/2016/01/npm-install.html






























































`npm`有两层含义。一层含义是Node的开放式模块登记和管理系统，网址为[npmjs.org](http%3A%2F%2Fnpmjs.org%2F)。另一层含义是Node默认的模块管理器，是一个命令行下的软件，用来安装和管理Node模块。

 Node学习(1)--NPM

https://www.jianshu.com/p/30ef3c874c1e


何区分项目的依赖中，哪些应该放在 dependencies，而哪些应该放在 devDependencies 呢？

https://zhuanlan.zhihu.com/p/56002037


其实 nodejs 中总共有 5 种依赖：

dependencies (常用)
devDependencies （常用），在线上状态不需要使用的依赖，就是开发依赖。
peerDependencies （不太常用）
bundledDependencies (我之前没用过)
optionalDependencies (我之前没用过)


从 5.x 开始就已经和 yarn 不分伯仲了，因此如何选择多数看是否有历史包袱。如果是新项目的话，就看程序员个人的喜好了。
## 参考文章

-   [npm 官网的 dependencies 文档](https://link.zhihu.com/?target=https%3A//docs.npmjs.com/files/package.json%23dependencies)
-   [npm 官方微博的 peerDependencies 介绍](https://link.zhihu.com/?target=https%3A//nodejs.org/en/blog/npm/peer-dependencies/) \- 这篇有点老了，npm 依赖还是嵌套关系
-   [Why use peerDependencies in npm for plugins](https://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/26737819/why-use-peer-dependencies-in-npm-for-plugins) \- 比较简略，不过说的在点上
-   [Types of dependencies](https://link.zhihu.com/?target=https%3A//yarnpkg.com/lang/en/docs/dependency-types/) \- 虽然是 yarn 的介绍，但概念和 npm 一致，且很精炼。
-   [semver](https://link.zhihu.com/?target=https%3A//docs.npmjs.com/misc/semver) \- npm 官方用来比较版本号的包
-   ["npm install --save" No Longer Using Tildes](https://link.zhihu.com/?target=http%3A//fredkschott.com/post/2014/02/npm-no-longer-defaults-to-tildes/) \- 早期的一篇博客，npm 对依赖版本号默认处理的变更
-   [npm 官网的 package-lock.json 文档](https://link.zhihu.com/?target=https%3A//docs.npmjs.com/files/package-lock.json)
-   [Workspaces in Yarn](https://link.zhihu.com/?target=https%3A//yarnpkg.com/blog/2017/08/02/introducing-workspaces/) \- yarn 官网介绍的 workspace 功能
-   [Here’s what you need to know about npm 5](https://link.zhihu.com/?target=https%3A//blog.pusher.com/what-you-need-know-npm-5/) \- 介绍 npm 5.x 的重要改进点








# 包管理nodejs

为什么 npm 要为每个项目单独安装一遍 node_modules？ - 贺师俊的回答 - 知乎 https://www.zhihu.com/question/41409670/answer/90869108

2019年nodejs凉了吗？凉到什么程度了？ - 小爝的回答 - 知乎 https://www.zhihu.com/question/313414600/answer/631267373 就业











npm package manager(npm包管理)

这是Nodejs默认的包管理工具








yarn

cnpm


yrm








```
>where node
C:\Program Files\nodejs\node.exe
```




































express框架很好的封装了nodejs的http模块，使我们用起来非常的简单。 引入express ：

通过命令行指令：

-   $ npm install express –save






































































C:\Users\admin\node_modules











```text
npm install express          # 本地安装
npm install express -g   # 全局安装
```

```text
$ npm list -g
```

```text
$ npm uninstall express
```



```text
$ npm ls
```

```text
$ npm update express
```





## 创建模块

创建模块，package.json 文件是必不可少的。我们可以使用 NPM 生成 package.json 文件，生成的文件包含了基本的结果：

```text
$ npm init
```

接下来我们就用以下命令来发布模块：

```text
$ npm publish
```

如果你以上的步骤都操作正确，你就可以跟其他模块一样使用 npm 来安装。





### Package.json 属性说明

-   **name** \- 包名。
-   **version** \- 包的版本号。
-   **description** \- 包的描述。
-   **homepage** \- 包的官网 url 。
-   **author** \- 包的作者姓名。
-   **contributors** \- 包的其他贡献者姓名。
-   **dependencies** \- 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。
-   **repository** \- 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。
-   **main** \- main 字段指定了程序的主入口文件，require('moduleName') 就会加载这个文件。这个字段的默认值是模块根目录下面的 index.js。
-   **keywords** \- 关键字


































































