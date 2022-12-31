[TOC]

# 1. cookie

cookie的缺陷是非常明显的

1. 数据大小：作为存储容器，cookie的大小限制在4KB左右这是非常坑爹的，尤其对于现在复杂的业务逻辑需求，4KB的容量除了存储一些配置字段还简单单值信息，对于绝大部分开发者来说真的不知指望什么了。

2. 安全性问题：由于在HTTP请求中的cookie是明文传递的（HTTPS不是），带来的安全性问题还是很大的。

3. 网络负担：我们知道cookie会被附加在每个HTTP请求中，在HttpRequest 和HttpResponse的header中都是要被传输的，所以无形中增加了一些不必要的流量损失

cookie作为HTTP协议的一部分用来处理客户端和服务器通信是不可或缺的，session正是依赖于实现的客户端状态保持。WebStorage的意图在于解决本来不应该cookie做，却不得不用cookie的本地存储。






# 2. H5存储WebStorage

为什么WebStorage比cookies好?

1. 从容量上讲WebStorage一般浏览器提供5M的存储空间，用来存储视频、图片神马的不够，但对于绝大部分操作足矣

2.安全性上WebStorage并不作为HTTP header发送的浏览器，所以相对安全

3.从流量上讲，因为WebStorage不传送到服务器，所以不必要的流量可以节省，这样对于高频次访问或者针对手机移动设备的网页还是很不错的。

这并不意味着WebStorage可以取代cookie，而是有了WebStorage后cookie能只做它应该做的事情了——作为客户端与服务器交互的通道，保持客户端状态。所以仅仅作为本地存储解决方案WebStorage是优于cookie的。




 [HTML5 WebStorage](https://www.cnblogs.com/dolphinX/p/3348469.html)








[Web Storage](http://www.cnblogs.com/dolphinX/p/3348469.html)（Local Storage和Session Storage）与IndexedDB。Web Storage使用简单字符串键值对在本地存储数据，方便灵活，但是对于大量结构化数据存储力不从心，IndexedDB是为了能够在客户端存储大量的结构化数据，并且使用索引高效检索的API。

# 3. H5存储（web Storage和web SQL）
[https://blog.csdn.net/gaomengwang/article/details/74628662](https://blog.csdn.net/gaomengwang/article/details/74628662)
对于Web Storage来说，实际上是Cookies存储的进化版。如果了解Cookie的人几乎一看Web Storage就会用，如果你从来没用过没了解过Cookie，没关系，看了这篇文章照样轻松玩转Web Storage。首先，学习Web Storage只需背熟这句口诀：“两个接口，四个函数”。

口诀：

（1）两个接口：分别是localStorage和sessonStorage

（2）四个函数：分别是setItem、getItem、removeItem和clear


**3、localStorage：**

（1）特性：

     域内安全、永久保存。即客户端或浏览器中来自同一域名的所有页面都可访问localStorage数据且数据除了删除否则永久保存，但客户端或浏览器之间的数据相互独立。

（2）四个函数：

     A. localStorage.setItem      存储数据信息到本地

     B. localStorage.getItem      读取本地存储的信息

     C. localStorage.removeItem   删除本地存储的信息

     D. localStorage.clear        清空所以存储的信息  

  

 **4、sessonStorage**：****

 （1）特性：

      会话控制、短期保存。会话概念与服务器端的session概念相似，短期保存指窗口或浏览器或客户端关闭后自动消除数据。

 （2）四个函数：

      A. sessionStorage.setItem       存储数据信息到本地

      B. sessionStorage.getItem       读取本地存储的信息

      C. sessionStorage.removeItem    删除本地存储的信息

      D. sessionStorage.clear         清空所以存储的信息










# 4. HTML5本地存储web storage（localStorage和sessionStorage）、WebSQL、indexedDB 



localStorage 用于持久化的本地存储，除非主动删除数据，否则数据是永远不会过期的。
sessionStorage 用于本地存储一个会话（session）中的数据，这些数据只有在同一个会话中的页面才能访问并且当会话结束后数据也随之销毁。因此sessionStorage不是一种持久化的本地存储，仅仅是会话级别的存储。

 web storage（localStorage和sessionStorage）和cookie的区别
Web Storage的概念和cookie相似，区别是它是为了更大容量存储设计的。Cookie的大小是受限的，并且每次你请求一个新的页面的时候Cookie都会被发送过去，这样无形中浪费了带宽，另外cookie还需要指定作用域，不可以跨域调用。除此之外，Web Storage拥有setItem,getItem,removeItem,clear等方法，不像cookie需要前端开发者自己封装setCookie，getCookie。但是Cookie也是不可以或缺的：Cookie的作用是与服务器进行交互，作为HTTP规范的一部分而存在 ，而Web Storage仅仅是为了在本地“存储”数据而生。


WebSQl差不多凉透了。

IndexedDB 是一种可以让你在用户的浏览器内持久化存储数据的方法。特点如下：

支持事务、游标、索引等数据库操作
一般浏览器会分配50M-250M不等的内存
持久化存储，清除浏览器缓存不会被删除（localStorage是会被删除的）
支持多种数据格式：arrayBuffer、String、Object、Array、File、Blob、ImageData都ok
不支持跨域，一个域可以有多个数据库
开发中需要谨记的一个特性：异步操作，换句话说，所有操作都需要在回调函数中完成
存储空间大，IndexedDB的存储空间比localStorage大得多，一般来说不少于250MB。IE的储存上限是250MB，Chrome和Opera是硬盘剩余空间的某个百分比，Firefox则没有上限。


IndexedDB在使用上需要调用HTML5提供的API，过程略有些麻烦。因此本文推荐一个工具类：localForage，这个工具类库是firefox公司开发和维护的开源类库。封装了WebSQL、IndexedDB以及localstorage三种存储模式的API，让使用者更好的来选择存储模式。然而它对外释放的API是统一的，简单的。

作者：白水螺丝
链接：https://www.jianshu.com/p/8cf47c755522

























# 5. localForage的使用 [API](https://link.jianshu.com/?t=https://localforage.github.io/localForage/) 地址





















