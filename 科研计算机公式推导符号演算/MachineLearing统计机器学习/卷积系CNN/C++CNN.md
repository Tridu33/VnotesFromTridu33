C:\\\Users\\\dell\\\Desktop\\\mall_dataset\\\frames\\\1 (%d).jpg  
  
蒟蒻 8/15/2020 9:31:23 PM  
  
这些是什么图？  
  
蒟蒻 8/15/2020 9:32:17 PM  
  
装上opencv就能复现了吗  
9:34:59 PM  
蒟蒻 8/15/2020 9:34:59 PM  
  
w1\_001\_00001.bin  
w2\_001\_00001.bin  
......  
"loc.bin"这些后缀的文件是用来干什么的？没了他们就不能运行吗  
9:37:43 PM  
蒟蒻 8/15/2020 9:37:43 PM  
  
这个程序的输入输出目标是干什么？时间有点久远，我有点不记得你的ppt说这个手动cpp所实现的CNN卷积神经网络是想用来干什么的了  
  
蒟蒻 8/15/2020 9:38:14 PM  
  
我唯一记得的是你说这个程序跑了半个月  
9:41:11 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:41:11 PM  
  
让我想想  
9:41:29 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:41:29 PM  
  
首先opencv是要的  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:41:52 PM  
  
还有mall dataset数据集  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:42:52 PM  
  
哪些jpg就是测试图片  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:43:12 PM  
  
图片路径  
9:44:12 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:44:12 PM  
  
loc我把每个图片分为80份,每份的位置信息  
  
蒟蒻 8/15/2020 9:44:21 PM  
  
输出是什么？  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:44:36 PM  
  
输入是图片,输出人数  
  
蒟蒻 8/15/2020 9:44:38 PM  
  
bin文件是你自己写的吗  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:44:45 PM  
  
对  
  
蒟蒻 8/15/2020 9:44:58 PM  
  
![](file:///C:\Users\admin\Documents\Tencent Files\2055969978\Image\C2C\B74B01BA400C530F9AE5D967908C99C1.gif)  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:45:03 PM  
  
要不把工程文件都传给你吧  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:45:19 PM  
  
bin文件是训练的参数  
  
蒟蒻 8/15/2020 9:45:28 PM  
  
最后存成的是什么格式的模型？  
9:45:54 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:45:54 PM  
  
就是bin  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:46:03 PM  
  
二进制格式  
  
蒟蒻 8/15/2020 9:46:34 PM  
  
希望最好发给我琢磨下，发现你这个cpp我直接猜，有点看不懂…  
  
蒟蒻 8/15/2020 9:46:49 PM  
  
我觉得你太强了  
  
蒟蒻 8/15/2020 9:47:26 PM  
  
徒手cnn，tensorflow做的cnn和你这个有什么不一样的吗？  
9:49:13 PM  
蒟蒻 8/15/2020 9:49:13 PM  
  
tf存的h5或者其他格式的模型可以看作你的bin文件  
  
蒟蒻 8/15/2020 9:49:22 PM  
  
你的标签是什么？  
  
蒟蒻 8/15/2020 9:49:54 PM  
  
你怎么给图片对应人数标识？是有监督学习吗  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:50:36 PM  
  
每个视窗设置4个标签,分别是1到4人  
9:50:58 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:50:58 PM  
  
数据集里有每个人的位置信息  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:51:08 PM  
  
就是监督  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:51:44 PM  
  
我想不管啥编的,原理都差不多  
  
蒟蒻 8/15/2020 9:52:19 PM  
  
它存成什么文件格式？  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:52:54 PM  
  
.mat  
9:53:06 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:53:06 PM  
  
matlab文件  
  
蒟蒻 8/15/2020 9:53:58 PM  
  
![](file:///C:\Users\admin\AppData\Local\Temp\%W@GJ$ACOF(TYDYECOKVDYB.png)http://personal.ie.cuhk.edu.hk/~ccloy/downloads\_mall\_dataset.html  
  
蒟蒻 8/15/2020 9:54:04 PM  
  
是这个吗？  
  
蒟蒻 8/15/2020 9:54:32 PM  
  
商场数据集看着不止4个人呀  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:55:01 PM  
  
每个图片分为80份  
9:55:19 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:55:19 PM  
  
视窗依次移动  
  
蒟蒻 8/15/2020 9:55:39 PM  
  
![](file:///C:\Users\admin\Documents\Tencent Files\2055969978\Image\C2C\E699BA82F285259D79B3B676CCA45548.jpg)  
  
你已下载文件“test.zip”(418.98MB)。  
9:56:24 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:56:24 PM  
  
本来想直接程序和matlab建立端口  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:56:54 PM  
  
可是不是说我缺文件就是打开失败  
  
王大佬opencv徒手c++神经网络 8/15/2020 9:57:13 PM  
  
只好手动复制位置  
9:57:24 PM  
王大佬opencv徒手c++神经网络 8/15/2020 9:57:24 PM  
  
就有了loc.bin  
  

  
王大佬opencv徒手c++神经网络 8/15/2020 9:57:43 PM  
  
就是这个数据集







