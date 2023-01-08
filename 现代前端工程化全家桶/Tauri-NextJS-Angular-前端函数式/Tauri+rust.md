[TOC]






------------

https://tauri.app/zh-cn/



https://nextjs.org/docs/getting-started

https://docs.rs/tauri/1.2.0/tauri/

# Tauri总览
https://jspang.com/article/51
技术胖12集nextjs系列课程 https://www.bilibili.com/video/BV13441117KK/ 


学习笔记和心得体会：https://lijing-2008.gitlab.io/coderli-vitepress/backend/nestjs/


- springboot后端+nextjs纯静态前端。
https://zhuanlan.zhihu.com/p/576234428
nextjs不单可以在这里当静态前端写，还有ssr服务器渲染优势没有被发挥出来。甚至可以直接是nextjs作为后端，js自给自足。

- NextJS作为SSR的后端，NestJS把整个价格和生态都优化：
    - 控制层，数据层，业务逻辑层和视图层 。 基于Angular思想确实很强大，DTO，typeORM，Swagger等


NestJS 是最好的后端框架 https://zhuanlan.zhihu.com/p/481063126
抛弃javaweb和spring/go/rust/cpp后端那些RESTful接口提供方。
NestJS 在处理多个请求时具有性能优势，而在服务器端执行计算量大的任务时表现不佳。

NodeJS优点：异步IO/IO密集 事件驱动 虽然解决了堵塞问题，但是对CPU占用还是有的。NestJS是nodejs最优秀的后端框架，之前的express koa（1/2）太辣鸡了。

nextjs是为了**SEO效果**。前后端同构是指在前后端维护同一份代码。它是在SPA的基础上，利用服务端渲染（SSR）直出首屏，解除单页面应用（SPA）在首屏渲染上面临的窘境

- 但是Tauri+原生js Api+rust Api+wasm能够弥补速度优势？

    - 原生Go后端的Goroutines帮助多个线程同时执行，可以实现的原始性能。

    - Java Spring全家桶磅礴的CRUD生态圈











# Tauri后端实践=SSR+TypeORM

动态路由@controller，javaweb后端那套工具搬家到前端来使用

https://jspang.com/article/87
controller react

nextjs的路由里像 pages/posts/[id] 这样的路由被称为动态路由，这种路由有一个致命缺点，就是即便你使用了next/link它还是不会走前端路由，它总是会让页面重载，严重影响页面性能。替代方案是改成 pages/posts?id={id}。


新版的nextjs没有这个坑，

```js
<Link href="/post/[pid]" as="/post/abc">
<a>First Post</ a>
</Link>

```
写法和原来csr的react-router不同，所以官方文档很重要


http://b23.tv/Hyif8pi
 ORM前端http://b23.tv/EGlhitP  controlle动态路由可以“/url/{id}”隐含在路径上去查询，静态路由需要?id=参数，

get post  
http://b23.tv/TV3BsCw


# Tauri作为前端的一些实践

+Vue博客

花十天时间重构了一下之前的Vue博客。
全部项目仓库:
1. 服务端Node项目Repo：https://github.com/Acmenlei/node-admin-backend

2. 前端Nextjs项目Repo：https://github.com/Acmenlei/next-ssr-blog

3. Vue博客后台管理系统Repo：https://github.com/Acmenlei/vue-admin-top


本博客项目已在 Github 开源，地址：https://github.com/Chocolate1999/nextjs-tailwind-blog
博客样式参考了 antfu 的博客页面，自己也用 React 写了他的梅开二度效果。
这是第一个版本，已经上线了，地址在：https://blog.yangchaoyi.vip/


## Tauri+antd
https://www.zhihu.com/answer/675443366
nextjs+antd


nextjs+graphql
https://jczhang.com/2022/09/11/startup-mvp-recipes-14-jwt-authentication-with-nest-js-passport-mikroorm


nextjs **mock**
https://juejin.cn/post/6850418109540073480
新建文件夹 `pages/api` （名字不能改）, 所有mock文件都放在这个目录中，打包时该目录的文件不会被写入页面路由列表

## Next.js + TailwindCSS + Firebase实现CRUD网页应用
 Next.js 速成课程将教您使用 Next.js + TailwindCSS + Firebase（身份验证和数据库）进行全栈开发的所有要点。http://b23.tv/Zqo9uED

我们涵盖了 React 钩子、React auth 上下文、身份验证、路由、模式、状态、样式、响应式 Web 应用程序开发的所有最佳实践，并了解我们如何使用 Firestore 和 Firebase Auth 实现所有 CRUD 操作。https://www.youtube.com/watch?v=UzMr7-0FgA0&t=699s
code: https://github.com/jamezmca/nextjs-todo

## Nextjs、Chakra UI、 Framer Motion 和 threejs 构建个人项目展示网站
https://www.youtube.com/watch?v=bSMZgXzC9AA&ab_channel=devaslife 
(搬运的简介)
你好我是来自日本大阪的松山拓哉，一位独立开发者，正在开发一款名为Inkdrop的降价笔记应用程序。
在这段视频中，我分享了我是如何使用 Nextjs、Chakra UI、 Framer Motion 和 threejs 构建投资组合网站
 我的录音设备
* 视频编辑: Final Cut Pro X
* 摄像机: Fujifilm X-T4
* 麦克风: Zoom H1n
* Slider: SliderONE v2
* Terminal: Hacked Hyper - https://dev.to/craftzdog/getting-side-by-side-preview-in-a-terminal-app-hyper-20ii

Credits:
 BGM: Epidemic Sound ---->     https://www.epidemicsound.com/campaign/invite-a-creator/ 


# Tauri + Rust + Wasm实践Native应用
Tauri + Rust + Wasm 开发了一个图片压缩应用
https://juejin.cn/post/7100105373767434247

【04】Tauri 入门篇 - 集成 WebAssembly - 知乎
https://zhuanlan.zhihu.com/p/533025312


How to show a WASM GUI in tauri (with **Next.js**)
https://github.com/tauri-apps/tauri/discussions/5231



Tauri + **Svelte** = cross-platform native GUI apps compiled to WASM
https://forum.safedev.org/t/tauri-svelte-cross-platform...





















