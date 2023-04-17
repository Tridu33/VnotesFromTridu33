# 1. 文档








[https://www.jianshu.com/p/454f63169bff](https://www.jianshu.com/p/454f63169bff)HTML中为什么CSS要写在上面JS要写在下面



总结：JS的执行顺序，由HTML的加载顺序决定，谁先被引用谁就优先执行（无论是写在页面上的JS代码还是引入的JS文件），最后执行onload()方法。如果有Jquery的$(function)或者$(document).ready(function(){})，其原则跟上面的原则一致，有出入的是：她优先onload()方法执行
原文链接：https://blog.csdn.net/wjiaoling136/article/details/84627688



JS 一定要放在 Body 的最底部么？聊聊浏览器的渲染机制
https://blog.csdn.net/weixin_33950035/article/details/89428273?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

[Google Web Fundamentals](https://developers.google.com/web/fundamentals/?hl=en) 是一个非常优秀的文档，里面讲到了跟web、浏览器、前端的方方面面。




















