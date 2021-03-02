[TOC]


现在的MVP模式越来越流行。就默认采用了。  
如果项目比较小的话：

-   app——Application Activity Fragment Presenter等的顶级父类
-   config——API,常量表等
-   model——数据层
    -   entities——数据模型
-   presenter——MVP的P
-   service——服务
-   ui——MVP的V
-   utils——工具类集合
-   widget——各个可复用View集合

如果项目比较大，上面的方式一定会造成presenter和view里近百个文件。看瞎眼系列。推荐下列方式：

-   app
-   config
-   model
    -   entities
-   module——将界面层以功能模块分配包。
    -   launch
    -   main
    -   account
    -   news
    -   music
    -   ……
-   utils
-   widget

## 1.1. 2.配置主题

对于不遵守Material Design的项目无视这一步。

**1.先在color.xml中写好需要的颜色：**

```xml
<resources>
    <color name="Orange">#ff5722</color>
    <color name="DeepPurple">#673AB7</color>
    <color name="DeepPurple900">#311B92</color>
    <color name="White">#fff</color>
    <color name="Gray">#888888</color>
    <color name="Gray100">#dddddd</color>
    <color name="Gray600">#999999</color>
</resources>

```

注意color.xml是配色表。应该是描述颜色而不是对字体颜色，背景颜色等的定义。这样能防止相近的颜色重复定义。而导致界面颜色不统一。

**2.在style.xml里定义主题：**

```xml
<style name="AppTheme.Base" parent="Theme.AppCompat.Light.NoActionBar">
    <!-- Customize your theme here. -->
    <item name="colorPrimary">@color/DeepPurple</item>
    <item name="colorPrimaryDark">@color/DeepPurple900</item>
    <item name="colorAccent">@color/Orange</item>
</style>

<style name="AppTheme" parent="AppTheme.Base"></style>

```

在res目录下，创建一个values-v21目录，再创建一个style.xml:

```xml
<style name="AppTheme" parent="AppTheme.Base">
    <item name="android:windowDrawsSystemBarBackgrounds">true</item>
    <item name="android:statusBarColor">?colorPrimaryDark</item>
</style>

```

然后在AndroidManifest.xml文件中修改application的theme属性为上面定义的AppTheme.即可实现沉浸式状态栏。

然后关于Theme与Toolbar的详细设置参考我另两篇博客：  
[http://www.cnblogs.com/Jude95/p/4369816.html](https://link.jianshu.com?t=http://www.cnblogs.com/Jude95/p/4369816.html)  
[http://www.cnblogs.com/Jude95/p/4370176.html](https://link.jianshu.com?t=http://www.cnblogs.com/Jude95/p/4370176.html)

## 1.2. 开发库，依赖库与SDK

必选的库:  
[gradle-retrolambda](https://link.jianshu.com?t=https://github.com/evant/gradle-retrolambda)——Android的lambda表达式插件  
[fresco](https://link.jianshu.com?t=https://github.com/facebook/fresco)——Android最屌图片加载库  
[material-dialogs](https://link.jianshu.com?t=https://github.com/afollestad/material-dialogs) ——Material Dialog向下兼容库  
[material-ripple](https://link.jianshu.com?t=https://github.com/balysv/material-ripple)——Ripple向下兼容库  
[fastjson](https://link.jianshu.com?t=https://github.com/alibaba/fastjson)——最快JSON解析  
[butterknife](https://link.jianshu.com?t=https://github.com/JakeWharton/butterknife)——View注解库和配套插件[android-butterknife-zelezny](https://link.jianshu.com?t=https://github.com/avast/android-butterknife-zelezny)  
[ActiveAndroid](https://link.jianshu.com?t=https://github.com/pardom/ActiveAndroid)——数据库注解库。  
[RxAndroid](https://link.jianshu.com?t=https://github.com/ReactiveX/RxAndroid)——Rx函数响应式编程[中文文档](https://link.jianshu.com?t=https://mcxiaoke.gitbooks.io/rxdocs/content/)  
[retrofit](https://link.jianshu.com?t=https://github.com/square/retrofit),[okhttp](https://link.jianshu.com?t=https://github.com/square/okhttp),[sqlbrite](https://link.jianshu.com?t=https://github.com/square/sqlbrite),[okio](https://link.jianshu.com?t=https://github.com/square/okio)——Square家的精品多啊  
`compile 'com.android.support:design:23.0.1'`——谷歌Material Design控件库

下面安利几个自己写的库，如果有什么建议欢迎交流：  
[Utils](https://link.jianshu.com?t=https://github.com/Jude95/Utils)——Android各种小功能集合  
[RollViewPager](https://link.jianshu.com?t=https://github.com/Jude95/RollViewPager)——自动轮播使用方便的ViewPager  
[EasyRecyclerView](https://link.jianshu.com?t=https://github.com/Jude95/EasyRecyclerView)——支持下拉上拉刷新等功能全面的RecyclerView  
[SwipeBackHelper](https://link.jianshu.com?t=https://github.com/Jude95/SwipeBackHelper)——Activity滑动关闭支持库，能达到微信效果

尝试了很多，这几个是现在常用的。  
[融云](https://link.jianshu.com?t=http://www.rongcloud.cn/)——即时通讯  
[友盟](https://link.jianshu.com?t=http://www.umeng.com/)——数据统计,推送，意见反馈，自动更新，第三方分享及登录,社区  
[七牛](https://link.jianshu.com?t=https://portal.qiniu.com/)——云存储  
[Mob](https://link.jianshu.com?t=http://www.rongcloud.cn/)——短信验证  
[Bmob](https://link.jianshu.com?t=http://www.bmob.cn/)——做后台不求人

依赖这一大堆库和SDK以后。建议在合适的时机初始化他们，而不是全堆在Application的onCreate()里面。这样会导致启动时间过长。启动后也会较卡。虽然是不会影响功能正常使用。

## 1.3. 4.配置Gradle

某些SDK运行时需要检查签名是否正确。所以在debug模式时也必须用正式KEY签名。而把签名放进版本控制不是明智的做法。所以推荐下面的做法：  
在app的gradle加入下面代码

```csharp
Properties props = new Properties()
props.load(new FileInputStream(file("signing.properties")))
android {
    signingConfigs {
        release{
            keyAlias props['KEY_ALIAS']
            keyPassword props['KEY_PASSWORD']
            storeFile file(props['KEYSTORE_FILE'])
            storePassword props['KEYSTORE_PASSWORD']
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
        debug {
            signingConfig signingConfigs.release
        }
    }
}

```

在app的gradle文件同级目录新建signing.properties文件，里面填入你的key的相应信息

```undefined
KEYSTORE_FILE = C:\\Users\\Mr.Jude\\Documents\\Android\\HelloWorld.jks
KEYSTORE_PASSWORD = xxxxxx
KEY_ALIAS = xxxxxx
KEY_PASSWORD = xxxxxx

```

将signing.properties添加进忽略目录。  
其他人pull下来代码后。自己新建signing.properties填入相应信息后即可编译成功。

## 1.4. 5.制定开发规范

为了避免合作开发写的代码风格迥异。或做出了多套开发模式。下面是个例子。毕竟是为了高效开发而制定的。适合自己项目的才是最好。  
所有Activity继承BaseActivity  
所有Fragment继承BaseFragment  
所有Presenter继承BasePresenter  
这样利于生命周期管理。也可以方便的全局修改。  
命名，例  
`AccountFragment`  
`UserDetailActivity`

layout命名，例  
`activity_collection`  
`fragment_account`  
`item_person`  
`include_toolbar`  
`view_progress`  
不过对于庞大项目的开发。近百个activity开头的layout列表还是会眼瞎。所以那种情况会在前面加上模块名。

id命名，例  
`btn_send`  
`tv_name`  
`list_persons`  
`et_password`  
然后用butterknife的插件生成变量会自动将下划线变成驼峰命名

变量命名:以m开头。例`mAdapter`使用时按一个m全都出来了  
方法命名:与其写好名字不如写好注释。= =。

**TextView使用官方标准字体**

  
  
作者：Jude95  
链接：https://www.jianshu.com/p/d9e4ddd1c530  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。













































# 2. 如何开发一个App


正常的互联网开发app的流程大致如下： 
- 产品规划，定产品方向 
- 需求调研，产出需求文档 
- 需求评审，修订需求文档 
- 产品狗画app线框图提供给射鸡师 
- 射鸡师根据线框图设计视觉稿 
- 程序猿根据视觉稿搭建UI框架 
- 程序猿根据需求文档开发功能 
- 测试媛编写测试用例，根据排期进行测试 
- 程序猿修复回归测试反馈的bug，提交beta版 
- 测试通过，提交给运营喵发布到渠道上线

上面是笔者的经验总结，可能有不太准确的地方，但大致整个流程是这样，我们开发者要清楚自己在整个产品中充当的角色，明白自己的工作职责即可。



快速搭建项目
Android比没有想象那么难，只是刚开始要学习的东西多，一下子消化不了才会比较茫然，笔者写这篇博客就是想帮助大家整理一下开发思路。

快速搭建项目也算是一项技能，而这项技能只能由你自己来完善，刚开始做开发的时候一定会有很多重复性的工作，如果没有意识去提高自己的开发效率的话，可能你的十年工作经验代表的只是一年的经验用了十年而已。

那要怎么做，笔者提供一个自己总结的，仅供参考： 
- 定开发规范 
- 搭建UI框架 
- 选用开发库集成（或自造轮子） 
- 第三方服务集成（视情况而定）

定开发规范
一个项目一般不会只有一个人独立开发，就算是独立开发，我们也应该定一下开发规范，一般会有什么样的规范？ 
- 命名规范 
- 代码规范 
- 代码管理规范

命名规范
命名规范包括： 
- 项目命名 
- 包命名 
- 类命名、成员变量命名 
- 资源文件命名 
我们做每一个产品都会有相应的命名，不要用中文来命名，最好用能表达中文意思的英文来表示，例如CSDN客户端，可以用CSDNClient作为命名，我们创建项目的时候可以以它作为Application name。 
可以看看以前写的这篇文章： 
http://blog.csdn.net/wwj_748/article/details/42347283

代码规范
代码规范视语言而定，开发android使用的是Java，自然要按照Java的编码规范进行编码，比如命名采用驼峰命名法，编码的时候也要符合Android的开发规范，比如UI线程不做任何耗时的操作，像网络请求、数据库操作都需要放到子线程中去做，只有UI的刷新才在UI线程中做，像这些规范，可以根据自身在项目遇到的问题来定，定规范的好处就是减少踩坑的几率，提高开发的质量。

代码管理
对于一个经常更新迭代的产品，不可能由头到尾不变，这个时候我们需要对代码进行分支管理，最好使用git代码仓库对代码进行管理，作为一个合格的开发者连git都不用实在说不过去，还用svn的童鞋赶紧放弃它投入git的怀抱，它的好处是不言而喻的，自己去体会。

搭建UI框架
搭建UI框架需要我们根据产品的导航模式来设计，市场上常用的导航模式有如下图几种：







我们的app如果不出意外一定是其中的一种导航模式，一般线框图出来我们就应该知道即将要开发的app长什么样子，开发者不必等视觉稿和素材出来才开始动工，我们先大致搭个架子，等视觉稿出来之后我们再做调整。

选用开发库
一般我们app涉及到的库会有： 
- UI框架（比如下拉刷新PullToRefresh、侧滑菜单Slidingmenu） 
- 网络请求库（比如okhtttp、AndroidAsyncHttp、Volley） 
- 数据操作库（比如GreenDao、Ormlite） 
- 图片缓存框架（比如Universal-Imageloader） 
- 数据解析库（比如Gson）

之所以要选用这些库，肯定是为了避免重复造轮子，在开发效率的角度来说，选用优秀的开源库能大大缩短开发周期和提高开发效率，但从个人提升角度来看的话，我们可能就成了一个只会用API的程序猿了，如果想提升的话，造轮子或者分析这些优秀的源代码是一个不错的途径。

第三方服务集成
我们开发app的时候，肯定会遇到一些需求，比如推送的需求、自动升级、数据统计、社会化分享、用户反馈等等，然而对于一个刚起步的企业或者个人开发者的话，全都要自己去开发的话，那岂不是累死，像推送这种有一定的技术门槛，能做好都能成立一家公司了，所以选用一些第三方服务是一个可选之举。如果说你以后做大了，用第三方怕不好控制，那就自己做呗，有钱任性招兵买马就自己做，谁叫咱有钱呢。

前面这些东西开发一个app够了，开发出来能不能用还得有靠谱的测试，有没有crash，操作流不流畅，体验好不好才会有用户去用。这里不从产品的角度去评判一个app的好与坏，程序员要考虑的是从代码层面、性能层面去让我们的app变得更好。

云测
我们开发完毕之后，需要给测试工程师进行基本的功能需求测试，他们传统的做法就是根据事先写好的测试用例来做回归测试，再把测试出来的bug反馈给工程师，工程师再去修bug，但这样实在是太不靠谱了，有时候我们太在意功能而忽略了一些更重要的东西，那就是体验，给用户最直接的感受就是你这个app够不够惊艳，够不够流畅，用户可能根本就不在乎你这个功能做的有多牛逼。所以我们更应该从非功能性方向去做测试，我们的目的是让用户用的爽，而不是加一些乱七八糟的功能。那怎么测非功能性的一些因素，这里就要提到『云测』这个东西，因为现在设备太多了，如果公司要买一堆设备来做测试，那得多少成本，况且设备更新得太快，你根本就跟不上，所以就有了云测这个东西，它是一个云测试平台服务，提供了一大批主流机型，我们就直接省去购买设备的成本，还能得到完善的测试报告。

再来说一下它的好处： 
- 终端云，省去测试设备购买租赁成本 
- 高效率 节省测试人员成本及时间 
- 包含兼容性测试、性能测试、功能测试 
- 操作简单、详细测试报告生成

这么多好处，你在缺少测试工程师的时候，不去尝试那实在说不过去。

打包上线
前面的开发环节、测试环节都没问题之后，你离实现一个app的完整开发就不远了，正常的互联网公司，会把签名打包的apk给到运营，交给他们去写文案，上传到应用渠道，让渠道给我们去首发和推广。如果是个人开发者，这些工作就得我们自己做了。

总结
本篇博客从整个app开发流程上去给大家梳理了一遍，没有讲太多技术上的东西，但理解app流程对自己把握产品很有益处，虽然我们只是一个小小的开发者，但如果你有追求，哪天轮到你去负责一个产品的时候，你就应该对开发的每一个环节都了如指掌，因为出了问题，你也知道怎么针对性的去解决。笔者虽然只是一个小小的开发者，但也乐于思考，很多时候不太愿意被别人牵着鼻子走，因为我们的人生就应该把握在自己手里。
————————————————
版权声明：本文为CSDN博主「IT_xiao小巫」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wwj_748/java/article/details/50088959








































































































































