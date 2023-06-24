


https://github.com/go-spring/go-spring


https://go-spring.com/en-us/docs/user/quick-start.html

# Spring-Go




golang小快灵的特征，你可以用gin的路由，可以用beego的缓存，也可以用其它框架的日志。但感觉golang的框架都在追求性能的极致，而不是生态的广阔，这也是golang并没有出现超级框架的原因。





gin

可以手动简易分成深度为1的Model层和Controller层。

目前应用最广泛的golang框架，甚至已经变成了golang的官方框架，但它主要是一个RESTFul的框架。封装比较优雅，API友好，源码注释比较明确。

beego

国内最早的golang框架，也是最全的MVC框架之一，中途停更了，现在已经开启了V2。beego可以用来快速开发API、Web、后端服务等各种应用，个人感觉有点参考PHP的超级框架Laravel。

Iris

号称全宇宙最快的 Go 语言 Web 框架。是一个快速、简单但功能齐全且非常高效的 Go 网络框架，完备 MVC 支持，未来尽在掌握。

Revel

也是一个优秀的高生产力、全栈 Web 框架。

echo

高性能、极简的 Go web 框架。

chi

用于构建 Go HTTP 服务的轻量级、惯用和可组合的路由器，是一个轻量级的、惯用的、可组合的路由器，用于构建 Go HTTP 服务。它特别擅长帮助您编写大型 REST API 服务，这些服务随着项目的增长和变化而保持可维护性。





Hertz http

Kitex rpc

---



如果以java程序员的角度看目前的golang生态，会给你一种还在远古时期的错觉。硬说的话也有很多框架试图支持mvc模型，试图支持ioc、aop，试图支持orm

基于k8s+istio的微服务体系，只要用gin做个frontend服务对外提供一套rest api，对内使用grpc client调用各个业务微服务就可以了。你每个微服务是个grpc server，那么从思想上看已经与mvc相去甚远了。


当前的微服务架构下，很多开发方式都变了，以前service层一个主要功能是利用aop来配置事务，现在这种东西不太重要，手写事务也没关系，但你更多需要考虑的是分布式事务。

以前你想跑定时任务还得用quartz，后来springboot简化了这个东西了只需要一个注解就搞定了，后来为了方便管理还有很多公司用xxl-job，但现在你只需要配置一个k8s的cronjob就可以了，至于管理是靠外围服务治理方案提供的。

以前做什么功能是想抽象出来一个jar包，再写个springboot的starter方便程序调用，现在做啥功能是想提供一套api再写一套k8s的yaml加到服务网格里供其他服务调用。





























