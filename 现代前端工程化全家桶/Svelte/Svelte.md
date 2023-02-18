https://www.sveltejs.cn/










# Svelte









Svelte作者是前端轮子哥 Rich Harris，同时也是 Rollup 的作者。Rich Harris 作者本人在介绍 Svelte 时，有一个非常精彩的演讲《Rethinking reactivity》，油管连接https://www.youtube.com/watch?v=AdNJ3fydeao&t=1900s，感兴趣的同学不要错过。



新兴前端框架 Svelte 从入门到原理 - 字节前端的文章 - 知乎
https://zhuanlan.zhihu.com/p/350507037

他设计 Svelte 的核心思想在于『通过静态编译减少框架运行时的代码量』，也就是说，vue 和 react 这类传统的框架，都必须引入运行时 (runtime) 代码，用于虚拟dom、diff 算法。Svelted完全溶入JavaScript，应用所有需要的运行时代码都包含在bundle.js里面了，除了引入这个组件本身，你不需要再额外引入一个运行代码。





















