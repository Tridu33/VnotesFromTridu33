# WebGL



简介

https://www.jianshu.com/p/fd4bbf7d09b6

甩一个 WebGL 支持检查的网站 [WebGL Report](https://link.zhihu.com/?target=http%3A//webglreport.com/%3Fv%3D1)，每一步之后都可以通过这个网站来查看操作是否成功。

https://zhuanlan.zhihu.com/p/24794967


H5 WebGL Demo 例子

https://blog.csdn.net/firedragon7031/article/details/51771792








教程
https://learnopengl-cn.github.io

好棒


hewebgl.com



https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API/Tutorial




源码例程
hewebgl.com


https://github.com/lesliebeijing/webgl-tutorial



现状看这儿










































作者：wonder-yyc  
链接：https://www.zhihu.com/question/41280881/answer/619784360  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  
  

我们[Wonder](https://link.zhihu.com/?target=https%3A//www.wonder-3d.com/)在WebGL领域耕耘了4年了，基于WebGL做了[3D引擎](https://link.zhihu.com/?target=https%3A//github.com/Wonder-Technology/Wonder.js)（支持多线程）和[编辑器](https://link.zhihu.com/?target=https%3A//github.com/Wonder-Technology/Wonder-Editor)，实际证明了Web 3D领域大有可为：

![](https://pic1.zhimg.com/v2-184f3af6f892ed23e7daca9913524580_b.gif)

![](https://pic1.zhimg.com/v2-184f3af6f892ed23e7daca9913524580_b.jpg)

现在Chrome浏览器已经比较成熟了，具备了开发大型网页3D应用和游戏的基础。[Wonder](https://link.zhihu.com/?target=https%3A//www.wonder-3d.com/)充分利用了Chrome的特性，具备了以下特性：

支持多线程，使得网页3D游戏成为可能；

支持流加载，能够边加载超大场景边显示；

支持PWA，获得原生app体验；

  

而且现在各种编译到javascript的语言也层出不穷，比如[Wonder](https://link.zhihu.com/?target=https%3A//www.wonder-3d.com/)就使用了[ReasonML语言](https://link.zhihu.com/?target=https%3A//reasonml.github.io/)，采用了函数式编程范式，证明了：

1、函数式编程范式比起面向对象，更适合3D应用。

因为3D应用中需要操作大量的数据，因此需要使用[Data Oriented](https://link.zhihu.com/?target=https%3A//www.wonder-3d.com/docs/docs/doc3-3/)来使用Buffer和Type Array来组织和操作数据，而函数式编程天然适合操作数据。

  

2、函数式编程也能有很好的性能。

感谢[Bucklescript](https://link.zhihu.com/?target=https%3A//bucklescript.github.io/)的编译优化～ReasonML编译的javascript性能非常好。

  

## 总结

1.Chrome浏览器已经能够支持大型网页3D应用。

2.[ReasonML语言](https://link.zhihu.com/?target=https%3A//reasonml.github.io/)提供了编写大型应用的语言保障。

3.WebGL2现在已经成熟，而且也即将 Metal，D3D12 和 Vulkan 等带到web端（如[WebGPU](https://zhuanlan.zhihu.com/p/45682197)）。

4.我们[Wonder](https://link.zhihu.com/?target=https%3A//www.wonder-3d.com/)进行了实践和应用，验证了可行性。

  

经过上面几点，我们可以看到，WebGL前途大好，网页3D必会发展起来。



































































