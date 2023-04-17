# 1. 教程

https://zhuanlan.zhihu.com/p/58073454
这份开源的 JavaScript 教程是真的走心






```<script>```里写的不是 ```type=”text/javascript”```，而是```language=”Javascript”```


目前这两种方法都可以表示<script> </script>里的代码是Javascript。然而，language这个属性在W3C的HTML标准中，已不再推荐使用。


js代码写在body，head和body后面的区别
计算机读代码的顺序是从上往下读的,html文件中的顺序是<head>→<body>→body后方

javascript代码写在```<head>```里面：

由于这时候网页主体（body）还未加载，所以这里适合放一些不是立即执行的自定义函数，立即执行的语句则很可能会出错（视浏览器而定）

javascript代码写在```<body>```里面：

这里可以放函数也可以放立即执行的语句，但是如果需要和网页元素互动的（比如获取某个标签的值或者给某个标签赋值），Javascript代码务必在标签的后面

javascript代码写在```<body>```下面，不规范。为什么把 Script 标签放在 body 结束标签之后 html 结束标签之前？ - 贺师俊的回答 - 知乎
https://www.zhihu.com/question/20027966/answer/13727164








[JS在HTML代码中的执行顺序https://blog.csdn.net/wjiaoling136/article/details/84627688?depth\_1-utm\_source=distribute.pc\_relevant.none-task&utm\_source=distribute.pc_relevant.none-task](https://blog.csdn.net/wjiaoling136/article/details/84627688?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)


```html



```


```html



```

JS 一定要放在 Body 的最底部么？聊聊浏览器的渲染机制
[https://blog.csdn.net/weixin\_33950035/article/details/89428273?depth\_1-utm\_source=distribute.pc\_relevant.none-task&utm\_source=distribute.pc\_relevant.none-task](https://blog.csdn.net/weixin_33950035/article/details/89428273?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)




在HTML body部分中的JavaScripts会在页面加载的时候被执行。
在HTML head部分中的JavaScripts会在被调用的时候才执行。

一、区别
浏览器解析html是从上到下的。
如果把javascript放在head里的话，则先被解析,但这时候body还没有解析，所以会返回空值。一般都会绑定一个监听，当全部的html文档解析完之后，再执行代码：
   windows.οnlοad=function(){
       //这里放入执行代码
   }
说明:
放在head中的JS代码会在页面加载完成之前就读取，而放在body中的JS代码，会在整个页面加载完成之后读取。

这就说明了，如果我们想定义一个全局对象，而这个对象是页面中的某个按钮时，我们必须将其放入body中，道理很明显：如果放入head，那当你定义的时候，那个按钮都没有被加载，可能获得的是一个undefind。










先，前端工程师必须得熟练掌握HTML、CSS和JavaScript。只懂其中一个或两个不行，必须对这三个都很熟悉，尤其是JS。

很多前端工程师还把对JS的认识停留在用jQuery做网页动画的时代，这个认识早就落后了，现在JS不仅负责前端的所有页面逻辑，还能利用Node开发后端服务。

而JS并没有看上去那么简单，它入门容易精通难，尤其是自己摸索，或者在网上随便搜索一些代码片断，很容易被带进沟里。学JavaScript应该学到精髓，还应该知道JS不好的设计，并且有意识地只用JS优秀的设计。

由于JS最近随着HTML5的兴起有了很大的更新，网上很多教程或者资料都过时了，现在应该用ES 6标准来写代码。即使不做后端，也要对Node非常熟悉，因为前端的自动化也是基于Node和npm实现的


https://wangdoc.com/javascript/

JavaScript 教程





































































