# SVG CSS3动画
贝塞尔曲线：SVG以及canvas都有基情Canvas之前也介绍过，HTML 画布元素，脚本化客户端绘图。https://www.zhangxinxu.com/wordpress/2013/08/贝塞尔曲线-cubic-bezier-css3动画-svg-canvas/

Canvas API（画布）是在HTML5中新增的标签用于在网页实时生成图像，并且可以操作图像内容，基本上它是一个可以用JavaScript操作的位图（bitmap）  
<canvas> 标记和 SVG以及 VML 之间的一个重要的不同是，<canvas> 有一个基于 JavaScript 的绘图 API，而 SVG 和 VML 使用一个 XML 文档来描述绘图。

```
<!DOCTYPE HTML>
<html>
<body>
<canvas id="myCanvas">your browser does not support the canvas tag </canvas>
<script type="text/javascript">
var canvas=document.getElementById('myCanvas');
var ctx=canvas.getContext('2d');
ctx.fillStyle='#FF0000';
ctx.fillRect(0,0,80,100);
</script>
</body>
</html>

```
https://www.runoob.com/html/html5-canvas.html
canvas 元素本身是没有绘图能力的。所有的绘制工作必须在 JavaScript 内部完成：https://www.runoob.com/html/html5-canvas.html
这两种方式在功能上是等同的，任何一种都可以用另一种来模拟。从表面上看，它们很不相同，可是，每一种都有强项和弱点。例如，矢量图SVG 绘图很容易编辑，只要从其描述中移除元素就行。

Canvas API 提供了一个通过JavaScript 和 HTML的<canvas>元素来绘制图形的方式。它可以用于动画、游戏画面、数据可视化、图片编辑以及实时视频处理等方面。

Canvas API主要聚焦于2D图形。而同样使用<canvas>元素的 WebGL API 则用于绘制硬件加速的2D和3D图形。

贝塞尔曲线  https://cubic-bezier.com/#.86,.22,.2,.93


要从同一图形的一个 <canvas> 标记中移除元素，往往需要擦掉绘图重新绘制它。







SVG只是一个用类似Canvas的感觉，通过有点像CSS的方法去实现矢量图绘制的XML文件。
https://segmentfault.com/a/1190000014620252







基础教程


贝塞尔曲线
https://www.jasondavies.com/animated-bezier/

画图

https://blog.csdn.net/cuixiping/article/details/6871666

核心Javscript代码：m

canvas

https://blog.csdn.net/jslang/article/details/37991517
贝塞尔曲线









基本形状








# SVG总结教程

https://segmentfault.com/a/1190000004393817




# CSS3
https://www.zhangxinxu.com/wordpress/2014/06/deep-understand-svg-path-bezier-curves-command/



https://browser.qq.com/mac/en/index.html







https://www.zhangxinxu.com/wordpress/2014/06/deep-understand-svg-path-bezier-curves-command/








```



<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
<style> 
div
{
	width:100px;
	height:100px;
	background:red;
	animation:myfirst 5s;
	-webkit-animation:myfirst 5s; /* Safari and Chrome */
}

@keyframes myfirst
{
	from {background:red;}
	to {background:yellow;}
}

@-webkit-keyframes myfirst /* Safari and Chrome */
{
	from {background:red;}
	to {background:yellow;}
}
</style>
</head>
<body>

<p><b>注意:</b> 该实例在 Internet Explorer 9 及更早 IE 版本是无效的。</p>

<div></div>

</body>
</html>



```
https://www.runoob.com/css3/css3-animations.html


https://c.runoob.com/codedemo/5528?

行星动画CSSC3















# 在线编辑SVG,WEB



https://c.runoob.com/more/svgeditor/


https://c.runoob.com/front-end/61


























