# svg格式含义数据


















M20,11H7.83l5.59,-5.59L12,4l-8,8 8,8 1.41,-1.41L7.83,13H20v-2Z




简单介绍一下<path>标签，大家粗略地看一下就好：
M = moveto(M X,Y) ：将画笔移动到指定的坐标位置
L = lineto(L X,Y) ：画直线到指定的坐标位置
H = horizontal lineto(H X)：画水平线到指定的X坐标位置
V = vertical lineto(V Y)：画垂直线到指定的Y坐标位置
C = curveto(C X1,Y1,X2,Y2,ENDX,ENDY)：三次贝赛曲线
S = smooth curveto(S X2,Y2,ENDX,ENDY)：三次贝赛曲线
Q = quadratic Belzier curve(Q X,Y,ENDX,ENDY)：二次贝赛曲线
T = smooth quadratic Belzier curveto(T ENDX,ENDY)：映射前面路径后的终点
A = elliptical Arc(A RX,RY,XROTATION,FLAG1,FLAG2,X,Y)：弧线
Z = closepath()：关闭路径

作者：四会歌神陈子豪
链接：https://www.jianshu.com/p/5c81970ddf33
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

有几点要注意：

坐标轴为以(0,0)为中心，X轴水平向右，Y轴水平向下。
所有指令大小写均可。大写绝对定位，参照全局坐标系；小写相对定位，参照父容器坐标系
指令和数据间的空格可以省略
同一指令出现多次可以只用一个

M = moveto
L = lineto
H = horizontal lineto
V = vertical lineto
C = curveto
S = smooth curveto
Q = quadratic Bézier curve
T = smooth quadratic Bézier curveto
A = elliptical Arc
Z = closepath

作者：ywyan
链接：https://www.jianshu.com/p/c819ae16d29b
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。











#####  PATH命令

在下面列出了SVG `<path>`元素的虚拟画笔可以使用的命令。大小的指令通常将参数坐标解析为绝对坐标。小写的指令通常将参数坐标解析为相对坐标。

| 指令 | 参数 | 名称 | 描述 |
| --- | --- | --- | --- |
| M | x,y | moveto | 移动虚拟画笔到指定的（x,y）坐标，仅移动不绘制 |
| m | x,y | moveto | 移动虚拟画笔到指定的（x,y）坐标，这个坐标是相对于当前画笔的坐标，仅移动不绘制 |
| L | x,y | lineto | 从当前画笔所在位置绘制一条直线到指定的（x,y）坐标 |
| l | x,y | lineto | 从当前画笔所在位置绘制一条直线到指定的（x,y）坐标，(x,y)坐标是相对于花瓣位置的点 |
| H | x | horizontal lineto | 绘制一条水平直线到参数指定的x坐标点，y坐标为画笔的y坐标 |
| h | x | horizontal lineto | 绘制一条水平直线到参数指定的x坐标点（当前x + 指定的x），x坐标相对于当前画笔x坐标 |
| V | y | vertical lineto | 从当前位置绘制一条垂直直线到参数指定的y坐标 |
| v | y | horizontal lineto | 从当前位置绘制一条垂直直线到参数指定的y坐标，y坐标相对于当前画笔的y坐标 |
| C | x1,y1 x2,y2 x,y | curveto | 从当前画笔位置绘制一条三次贝兹曲线到参数（x,y）指定的坐标。x1，y1和x2,y2是曲线的开始和结束控制点，用于控制曲线的弧度 |
| c | x1,y1 x2,y2 x,y | curveto | 于大小C指令相同，但是坐标是相对于画笔的坐标 |
| S | x2,y2 x,y | shorthand / smooth curveto | 从当前画笔位置绘制一条三次贝兹曲线到参数（x,y）指定的坐标。x2,y2是结束控制点。开始控制点和前一条曲线的结束控制点相同 |
| s | x2,y2 x,y | shorthand / smooth curveto | 和大小的S指令相同，但是坐标是相对于当前画笔的坐标点 |
| Q | x1,y1 x,y | 二次贝兹曲线 | 从当前画笔位置绘制一条二次贝兹曲线到参数（x,y）指定的坐标。x1,y1是控制点，用于控制曲线的弧度 |
| q | x1,y1 x,y | 二次贝兹曲线 | 和大小的Q指令相同，但是坐标是相对于当前画笔的坐标点 |
| T | x,y | 平滑的二次贝兹曲线 | 从当前画笔位置绘制一条二次贝兹曲线到参数（x,y）指定的坐标。控制点被假定为最后一次使用的控制点 |
| t | x,y | 平滑的二次贝兹曲线 | 和大小的T指令相同，但是坐标是相对于当前画笔的坐标点 |
| A | rx,ry x-axis-rotation large-arc-flag,sweepflag x,y | 椭圆弧线 | 从当前画笔位置开始绘制一条椭圆弧线到（x,y）指定的坐标。rx和ry分别为椭圆弧线水平和垂直方向上的半径。x-axis-rotation指定弧线绕x轴旋转的度数。它只在rx和ry的值不相同是有效果。large-arc-flag是大弧标志位，取值0或1，用于决定绘制大弧还是小弧。sweep-flag用于决定弧线绘制的方向 |
| a | rx,ry x-axis-rotation large-arc-flag,sweepflag x,y | 椭圆弧线 | 和大写的A指令相同，但是坐标是相对于当前画笔的坐标点 |
| Z | 无 | 闭合路径 | 从结束点绘制一条直线到开始点，闭合路径 |
| z | 无 | 闭合路径 | 从结束点绘制一条直线到开始点，闭合路径 |

| 指令 | 参数 | 名称 | 描述 |
| --- | --- | --- | --- |
| M | x,y | moveto  
移动到 | 移动虚拟画笔到指定的（x,y）坐标，仅移动不绘制 |
| m | x,y | moveto | 同M，但使用相对坐标 |
| L | x,y | lineto  
连直线到 | 从当前画笔所在位置绘制一条直线到指定的（x,y）坐标 |
| l | x,y | lineto | 同L，但使用相对坐标 |
| H | x | horizontal lineto  
水平连线到 | 绘制一条水平直线到参数指定的x坐标点，y坐标为画笔的y坐标 |
| h | x | horizontal lineto | 同H，但使用相对坐标 |
| V | y | vertical lineto  
垂直连线到 | 从当前位置绘制一条垂直直线到参数指定的y坐标 |
| v | y | vertical lineto | 同V，但使用相对坐标 |
| C | x1,y1 x2,y2 x,y | curveto  
三次方贝塞尔曲线 | 从当前画笔位置绘制一条三次贝兹曲线到参数（x,y）指定的坐标。x1，y1和x2,y2是曲线的开始和结束控制点，用于控制曲线的弧度 |
| c | x1,y1 x2,y2 x,y | curveto | 同C，但使用相对坐标 |
| S | x2,y2 x,y | shorthand / 平滑三次方贝塞尔曲线 | 从当前画笔位置绘制一条三次贝塞尔曲线到参数（x,y）指定的坐标。x2,y2是结束控制点。开始控制点和前一条曲线的结束控制点相同 |
| s | x2,y2 x,y | shorthand / 平滑三次方贝塞尔曲线 | 同S，但使用相对坐标 |
| Q | x1,y1 x,y | 二次方贝塞尔曲线 | 从当前画笔位置绘制一条二次方贝塞尔曲线到参数（x,y）指定的坐标。x1,y1是控制点，用于控制曲线的弧度 |
| q | x1,y1 x,y | 二次方贝塞尔曲线 | 同Q，但使用相对坐标 |
| T | x,y | 平滑的二次贝塞尔曲线 | 从当前画笔位置绘制一条二次贝塞尔曲线到参数（x,y）指定的坐标。控制点被假定为最后一次使用的控制点 |
| t | x,y | 平滑的二次贝塞尔曲线 | 同T，但使用相对坐标 |
| A | rx,ry x-axis-rotation large-arc-flag,sweepflag x,y | 椭圆弧线 | 从当前画笔位置开始绘制一条椭圆弧线到（x,y）指定的坐标。rx和ry分别为椭圆弧线水平和垂直方向上的半径。x-axis-rotation指定弧线绕x轴旋转的度数。它只在rx和ry的值不相同是有效果。large-arc-flag是大弧标志位，取值0或1，用于决定绘制大弧还是小弧。sweep-flag用于决定弧线绘制的方向 |
| a | rx,ry x-axis-rotation large-arc-flag,sweepflag x,y | 椭圆弧线 | 同A，但使用相对坐标 |
| Z | 无 | 闭合路径 | 从结束点绘制一条直线到开始点，闭合路径 |
| z | 无 | 闭合路径 | 同Z |

注意:所有的这些字符命令都可以用大小写两种形式。大小表示绝对位置，而小写表示相对位置。





























