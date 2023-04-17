[TOC]


[加速度传感器的感性理解://blog.csdn.net/asdjy123/article/details/51250653](https://blog.csdn.net/asdjy123/article/details/51250653)




# 1. 传感器Sensor

https://www.jianshu.com/p/8440a5897944  Android Sensor 传感器总结

Android 传感器开发详解
https://blog.csdn.net/Airsaid/article/details/52902299

摇一摇:https://www.jianshu.com/p/4c141d851346


## 1.1. 官方传感器教程

IBM文档源码：
https://www.ibm.com/developerworks/cn/opensource/os-android-sensor/index.html


官方传感器文档：
https://developer.android.google.cn/guide/topics/sensors/sensors_overview.html?hl=zh-cn

[https://developer.androi d.google.cn/guide/topics/sensors](https://developer.android.google.cn/guide/topics/sensors)

## 1.2. B乎大学online课程

Android从入门到精通（项目案例版）[https://www.bilibili.com/video/BV1jW411375J?p=178](https://www.bilibili.com/video/BV1jW411375J?p=178)

加速度传感器 https://www.bilibili.com/video/BV1jW411375J/?p=178




天哥】Android开发视频教程最新版 Android Studio开发 https://www.bilibili.com/video/BV1Rt411e76H







# 2. andriod连接获取手机加速度传感器实时数据

 android传感器

  

官方文档说的很清楚，Android平台支持三大类的传感器，它们分别是：  

a. Motion sensors

b. Environmental sensors

c. Position sensors

从另一个角度划分，安卓的传感器又可以分为基于硬件的和基于软件的。基于硬件的传感器往往是通过物理组件去实现的，他们通常是通过去测量特殊环境的属性获取数据，比如：重力加速度、地磁场强度或方位角度的变化。而基于软件的传感器并不依赖物理设备，尽管它们是模仿基于硬件的传感器的。基于软件的传感器通常是通过一个或更多的硬件传感器获取数据，并且有时会调用虚拟传感器或人工传感器等等，线性加速度传感器和重力传感器就是基于软件传感器的例子。下面通过官方的一张图看看安卓平台支持的所有传感器类型  

在Android中传感器类是通过Sensor类来表示的，它属于android.hardware包下的类，顾名思义，和硬件相关的类。传感器的API不复杂，包含3个类和一个接口，分别是：  

SensorManager

Sensor

SensorEvent

SensorEventListener

根据官方文档的概述分别简单解释一下这4个API的用处：  

SensorManager：可以通过这个类去创建一个传感器服务的实例，这个类提供的各种方法可以访问传感器列表、注册或解除注册传感器事件监听、获取方位信息等。

Sensor：用于创建一个特定的传感器实例，这个类提供的方法可以让你决定一个传感器的功能。

SensorEvent：系统会通过这个类创建一个传感器事件对象，提供了一个传感器的事件信息，包含一下内容，原生的传感器数据、触发传感器的事件类型、精确的数据以及事件发生的时间。

SensorEventListener：可以通过这个接口创建两个回调用法来接收传感器的事件通知，比如当传感器的值发生变化时。
















原理Three-axis/Tri-Axial Accelerometers三轴加速度传感器原理_三轴加速度传感器应用性能参数应用andriod开源项目算法三轴加速度传感器角度值转换原理基于三轴加速度传感器的计步算法【翻译】利用加速度求解位置的算法——三轴传感器如何利用加速度传感器测量物体的倾斜角度？芯片DocsBMA250三轴加速度传感器（部分翻译）很多公司的商用型号和文档算法识别

# 3. 原理Three-axis/Tri-Axial Accelerometers



> Tri-Axial Accelerometers. Tri-Axial Accelerometers are **high level output transducers** that provide three outputs, simultaneously measuring acceleration along the X-, Y- and Z-axes. The transducers can be used on any part of the body or attached to external equipment. The pliable and unobtrusive design conforms readily to body contours.


三轴加速度传感器原理



***Analog vs digital*** \- First and foremost, you must choose between an accelerometer with analog outputs or digital outputs. This will be determined by the hardware that you are interfacing the accelerometer with. Analog style accelerometers output a continuous voltage that is proportional to acceleration. E.g. 2.5V for 0g, 2.6V for 0.5g, 2.7V for 1g. Digital accelerometers usually use pulse width modulation (PWM) for their output. This means there will be a square wave of a certain frequency, and the amount of time the voltage is high will be proportional to the amount of acceleration.
.....

## 3.1. 三轴加速度传感器原理_三轴加速度传感器应用

[http://www.elecfans.com/yuanqijian/sensor/201910171093891.html](http://www.elecfans.com/yuanqijian/sensor/201910171093891.html)

## 3.2. 性能参数

[https://www.dimensionengineering.com/info/accelerometers](https://www.dimensionengineering.com/info/accelerometers)

模拟与数字-首先，您必须在具有模拟输出或数字输出的加速度计之间进行选择。  这将由与加速度计接口的硬件决定。  模拟式加速度计可输出与加速度成比例的连续电压。  例如。 0g为2.5V，0.5g为2.6V，1g为2.7V。  数字加速度计通常将脉冲宽度调制（PWM）用于其输出。  这意味着将有一个特定频率的方波，并且高电压的时间将与加速度成正比。

如果您使用的是BASIC Stamp或任何其他具有纯数字输入的微控制器，则很可能需要使用数字输出加速度计。  这里的缺点是，它需要您使用微控制器的定时资源来测量占空比，以及执行计算量大的除法运算。

如果您将PIC / AVR / OOPIC /标枪用于模拟输入或完全基于模拟的电路，则模拟几乎总是最好的选择。  根据编译器的不同，测量模拟加速度的过程可能非常简单：acceleration = read_adc（）;。  并且可以在几微秒内完成。

轴数-对于大多数项目，两个就足够了。  但是，如果要尝试3D定位，则需要一个3轴加速度计，或者两个以直角安装的2轴加速度计。

最大摆幅-如果您仅关心使用地球重力来测量倾斜度，则±1.5g加速度计将绰绰有余。  如果要使用加速度计来测量汽车，飞机或机器人的运动，±2g应该给您足够的工作空间。  对于启动或停止非常突然的项目，您将需要一个能够处理±5g或更大的项目。

灵敏度-一般来说，灵敏度越高越好。  这意味着对于给定的加速度变化，信号的变化将更大。  由于较大的信号变化更易于测量，因此您将获得更准确的读数。

带宽-这表示每秒可以获取可靠的加速度读数的时间。  对于缓慢移动的倾斜感应应用，50Hz的带宽可能就足够了。  如果打算进行振动测量或控制快速移动的机器，则需要几百Hz的带宽。

阻抗/缓冲问题-到目前为止，这是涉及模拟加速度计的项目中最常见的问题的唯一根源，因为很少有人彻底阅读所需的文档。 PIC和AVR数据手册均指定为使A-D转换正常工作，所连接的器件的输出阻抗必须低于10kΩ。  不幸的是，ADI公司的模拟加速度计的输出阻抗为32kΩ。  解决方案是使用低输入失调轨到轨运算放大器作为缓冲器来降低输出阻抗。  据我们所知，DE-ACCM是唯一为您解决此问题的加速度计解决方案。

# 4. 应用

三轴加速度传感器应用[http://baike.cntronics.com/abc/10174](http://baike.cntronics.com/abc/10174)

1、车身安全、控制及导航系统中的应用

加速度传感器已被广泛应用于汽车电子领域，主要集中在车身操控、安全系统和导航，典型的应用如汽车安全气囊（Airbag）、ABS防抱死刹车系统、电子稳定程序（ESP）、电控悬挂系统等。

目前车身安全越来越得到人们的重视，汽车中安全气囊的数量越来越多，相应对传感器的要求也越来越严格。整个气囊控制系统包括车身外的冲击传感器（Satellite Sensor）、安置于车门、车顶，和前后座等位置的加速度传感器（G-Sensor）、电子控制器，以及安全气囊等。电子控制器通常为16位或32位MCU，当车身受到撞击时，冲击传感器会在几微秒内将信号发送至该电子控制器。

随后电子控制器会立即根据碰撞的强度、乘客数量及座椅/安全带的位置等参数，配合分布在整个车厢的传感器传回的数据进行计算和做出相应评估，并在最短的时间内通过电爆驱动器（Squib Driver）启动安全气囊保证乘客的生命安全。

通常仅靠ABS和牵引控制系统无法满足车辆在弯曲路段上的行车安全要求。该场合下电子稳定性控制系统 （ESC） 就能够通过修正驾驶员操作中的转向不足或过度转向，来控制车辆使其不偏离道路。该系统通过使用一个陀螺仪来测量车辆的偏航角，同时用一个低重力加速度传感器来测量横向加速度。将所得测量数据与通过行驶速度和车轮倾斜角两项数据计算得到的结果进行比对，从而调整车辆转向以防止发生侧滑。

除了车身安全系统这类重要应用以外，目前加速度传感器在导航系统中的也在扮演重要角色。 其主要利于GPS卫星信号实现定位。而当进入卫星信号接收不良的区域或环境中，如遂道、高楼林立、丛林地带，就会因失去信号而丧失导航功能。基于MEMS技术的3轴加速度传感器配合陀螺仪或电子罗盘等元件一起可创建方位推算系统（DR， Dead Reckoning），对GPS系统实现互补性应用。

2、硬盘抗冲击防护

目前由于海量数据对存储方面的需求，硬盘和光驱等元器件被广泛应用到笔记本电脑、手机、数码相机/摄相机、便携式DVD机、PMP等设备中。便携式设备由于其应用场合的原因，经常会意外跌落或受到碰撞，而造成对内部元器件的巨大冲击。

为了使设备以及其中数据免受损伤，越来越多的用户对便携式设备的抗冲击能力提出要求。

一般便携式产品的跌落高度为1.2~1.3米，其在撞击大理石质地面时会受到约50KG的冲击力，硬盘等高速旋转的器件却在此类冲击下显得十分脆弱。

如果在硬盘中内置3轴加速度传感器，当跌落发生时，系统会检测到加速的突然变化，并执行相应的自我保护操作，如关闭抗震性能差的电子或机械器件，让磁头复位，以减少硬盘的受损程度。

3、消费产品中的创新应用

3轴加速度传感器为传统消费及手持电子设备实现了革命性的创新空间。其可被安装在游戏机手柄上，作为用户动作采集器来感知其手臂前后、左右，和上下等的移动动作，并在游戏中转化为虚拟的场景动作如挥拳、挥球拍、跳跃、甩鱼竿等，把过去单纯的手指运动变成真正的肢体和身体的运动，实现比以往按键操作所不能实现的临场游戏感和参与感。

此外，3轴加速度传感器还可用于电子计步器，人在走动的时候会产生一定规律性的振动，而加速度传感器可以检测振动的过零点，从而计算出人所走的步或跑步所走的步数，从而计算出人所移动的位移。并且利用一定的公式可以计算出卡路里的消耗。

为电子罗盘（3D Compass）提供补偿功能，如果不带倾斜校正的电子指南针，需要用户水平放置。而利用加速度传感器可以测量倾角的这一原理，可以对电子指南针的倾斜进行补偿。

也可用于数码相机的防抖，检测手持设备的振动/晃动幅度，当振动/晃动幅度过大时锁住照相快门，使所拍摄的图像永远是清晰的。

3轴加速度传感器的应用范围很广， 还能用于手持设备的姿态识别和UI操作。例如借助3轴加速度传感器，手持设备可实现画面自动转向。

设备显示的画面和信息会根据用户的动作而自动旋转。其通过内部传感器对重力向量的方向检测来确定设备处于水平或垂直状态，并自动调整显示状态，给用户带来方便。

4、趣味性扩展功能

3轴加速度传感器对用户操控动作的转变还可转化为许多趣味性的扩展功能上，如虚拟乐器、虚拟骰子游戏，以及“闪讯”（Wave Message）等。

虚拟乐器内置的加速度传感器可检测用户对手持设备的挥动来控制乐器的节奏和音量等；骰子游戏也采用类似的原理，通过对挥动等动作的感知来控制虚拟骰子的旋转速度，并借助内部数学模型抽象的物理定律决定其停止的时间。

“闪讯”是一个更富有想象力的应用，用户可利用此功能在空中进行文字编辑。“闪讯”即让手持设备通过加速度传感器捕捉用户在空中模拟写字的快速动作，主要适合较暗的环境下使用。手持设备上会安装发光的LED，由于人眼视网膜的视觉暂留现象，其在空中挥动的动作会在其眼中留下短暂的连续画面，完成写字的所有动作笔顺。

随着MEMS微电子机械系统技术在传感器领域中的广泛应用，使得加速度传感器的体积变得更加轻便、性能得到明显提升。

## 4.1. andriod开源项目

[https://blog.csdn.net/lacker159/article/details/86561919](https://blog.csdn.net/lacker159/article/details/86561919) andriod开发之获取加速度传感器信息

Android 手机获取加速度传感器加速度数据并自定义采样频率[https://blog.csdn.net/llp1992/article/details/41786865](https://blog.csdn.net/llp1992/article/details/41786865)

1 加速度传感器  加速度传感器又叫G-sensor，返回x、y、z三轴的加速度数值。  该数值包含地心引力的影响，单位是m/s^2。 

将手机平放在桌面上，x轴默认为0，y轴默认0，z轴默认9.81。  

将手机朝下放在桌面上，z轴为-9.81。  将手机向左倾斜，x轴为正值。  

将手机向右倾斜，x轴为负值。  将手机向上倾斜，y轴为负值。  

将手机向下倾斜，y轴为正值。

2.在sensormanager的调用中为

#define SENSOR\_TYPE\_ACCELEROMETER //加速度

Android 中传感器的功能

SensorManager 是所有传感器的一个综合管理类，包括了传感器的种类、采样率、精准度等。

// 得到一个SensorManager对象

SensorManager mSensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);

// 得到传感器列表

List<Sensor> sensors = mSensorManager.getSensorList(Sensor.TYPE_ORIENTATION);

// 注册传感器

boolean result = mSensorManager.registerListener(this, sensors, SensorManager.SENSOR\_DELAY\_FASTEST);

// 卸载传感器

mSensorManager.unregisterListener(this);

// SensorEventListener有两个接口方法

// 在传感器值更改时调用

onSensorChanged(SensorEvent event);

// SensorEvent 对象包括一组浮点数

float x = event.values\[SensorManager.DATA_X\];

float y = event.values\[SensorManager.DATA_Y\];

float z = event.values\[SensorManager.DATA_Z\];

// 在传感器的精准度发生改变时调用

// 参数accuracy表示传感器新的准确值

onAccuracyChanged(Sensor sensor, int accuracy);

原文链接：[https://blog.csdn.net/u014675538/article/details/50363797](https://blog.csdn.net/u014675538/article/details/50363797)

曲线救国，不想安装Andriod Studio

有什么能记录（安卓）手机加速度传感器数据的APP吗？ - 巫毅的回答 - 知乎  [https://www.zhihu.com/question/29923733/answer/165284791](https://www.zhihu.com/question/29923733/answer/165284791)

# 5. 算法

# 6. 三轴加速度传感器角度值转换原理

[https://blog.csdn.net/ylzmm/article/details/78453347](https://blog.csdn.net/ylzmm/article/details/78453347)

## 6.1. 基于三轴加速度传感器的计步算法

[https://blog.csdn.net/Dancer__Sky/article/details/81504778](https://blog.csdn.net/Dancer__Sky/article/details/81504778)

## 6.2. 【翻译】利用加速度求解位置的算法——三轴传感器

[https://www.cnblogs.com/cposture/p/4378922.html](https://www.cnblogs.com/cposture/p/4378922.html)

## 6.3. 如何利用加速度传感器测量物体的倾斜角度？

[http://www.elecfans.com/d/542602.html](http://www.elecfans.com/d/542602.html)

# 7. 芯片Docs

[齐了，什么资料都在这儿搜就行](https://www.arrow.com/en/categories/sensors/accelerometers)

## 7.1. BMA250三轴加速度传感器（部分翻译）

[https://blog.csdn.net/lissettecarlr/article/details/78910273](https://blog.csdn.net/lissettecarlr/article/details/78910273)

Tri-Axial Accelerometers are high level output transducers that provide three outputs, simultaneously measuring acceleration along the X-, Y- and Z-axes. The transducers can be used on any part of the body or attached to external equipment. The pliable and unobtrusive design conforms readily to body contours.

-   TSD109C2 (±5 G) is optimal for measuring accelerations when performing slow movements, such as walking and hand tremor.
    
-   TSD109J (±200 G) is more suitable for quick movements, such as swinging a tennis racket.
    

BIOPAC offers tri-axial accelerometers available in ±5 G and ±200 G ranges. These accelerometers are used with the BIOPAC HLT100C module, which makes a high-level transducer connection and provides power to the transducer when making a connection. When used in conjunction with Acq*Knowledge* software, an MP data analysis and acquisition hardware platform, and the HLT100C module, these transducers permit detailed, three axis, accelerometry measures over a wide range of test conditions.

## 7.2. 很多公司的商用型号和文档

[https://www.ctconline.com/biaxial\_triaxial\_accelerometers.aspx](https://www.ctconline.com/biaxial_triaxial_accelerometers.aspx) 商用很多型号  [https://www.kasensors.com/us/products/triaxial-accelerometers](https://www.kasensors.com/us/products/triaxial-accelerometers) 商用型号

[https://www.stiweb.com/Triaxial\_Accelerometers\_s/88.htm](https://www.stiweb.com/Triaxial_Accelerometers_s/88.htm) 商用型号和文档

# 8. 算法识别

行为识别常用哪种特征提取？ \- 王晋东不在家的回答 \- 知乎 [https://www.zhihu.com/question/41068341/answer/89926233](https://www.zhihu.com/question/41068341/answer/89926233)






## 8.1. 参考文献      


\[1\]张敏,姜秀柱,陈伟,周军娜.基于三轴加速度传感器的速度测量方法研究与实现\[J\].传感器与微系统,2018,37(06):122-125+128.

\[2\]潘大伟,于云华.基于三轴加速度传感器的抽油机悬点位移测量装置设计\[J\].传感器与微系统,2019,38(12):93-95+99.

\[3\]钟君. 基于加速度传感器的日常行为识别的特征提取方法研究\[D\].兰州大学,2016.

\[4\]李晨. 基于手机加速度传感器的人体监控系统研制\[D\].广西大学,2015.

\[5\]罗初发.基于三轴加速度传感器的人体动作识别研究\[J\].工业控制计算机,2015,28(11):31-32.


\[6\]舒潇.三轴加速度传感器测量体力活动研究进展\[J\].当代体育科技,2018,8(14):230-231.



\[7\]庄姝颖,皮德常.基于手机传感器的用户行为识别\[J\].盐城工学院学报(自然科学版),2017,30(03):58-63.

\[8\]杨峰,赵曙光,许方成,黄佳佳.基于安卓平台的老人摔倒报警系统\[J\].信息通信,2018(01):244-246.

\[9\]李飞龙. 基于三轴加速度传感器跌倒检测方法的研究\[D\].电子科技大学,2015.

\[10\]程一风,李达,张翔晨.基于Android手机多传感器的老人跌倒检测技术研究与实现\[J\].电子设计工程,2016,24(14):181-183.

\[11\]丁红,饶万贤.基于深度学习的人体行为检测系统设计\[J\].电子技术与软件工程,2019(09):79-80.





\[12\]刘雷,慕艳艳,刘睿鑫.基于三轴加速度传感器的步长估算模型研究\[J\].传感器与微系统,2017,36(08):22-24+28.



\[13\]陈蔚.基于三轴加速度传感器的计步器的设计\[J\].数字技术与应用,2018,36(09):181-183.

\[14\]赵月民,陈培友.基于加速度传感器的大学生自行车运动能耗预测模型研究\[J\].山东体育学院学报,2019,35(01):80-85.

\[15\]吴廉卿,刘丹松,屈萍.基于三轴加速度传感器的大学生体力活动能量消耗模型研究\[J\].武汉体育学院学报,2018,52(04):87-91.

\[16\]商用芯片Docs检索\[EB/OL\] . https://www.arrow.com/en/categories/sensors/accelerometers





\[17\]谷歌文档\[EB/OL\] .https://developer.android.google.cn/guide/topics/sensors/sensors_overview

\[18\]Android开发从入门到精通（项目案例版）\[EB/OL\] . https://www.bilibili.com/video/BV1jW411375J

\[19\] \[天哥\]Android开发视频教程最新版 Android Studio开发\[EB/OL\] . https://www.bilibili.com/video/BV1Rt411e76H?p=27

\[20\] Android Sensor 传感器总结 \[EB/OL\] . https://www.jianshu.com/p/8440a5897944

\[21\] 深入探讨 Android 传感器\[EB/OL\] . https://www.ibm.com/developerworks/cn/opensource/os-android-sensor/index.html

\[22\] Android 传感器开发详解 \[EB/OL\] . https://blog.csdn.net/Airsaid/article/details/52902299

\[23\] A beginner’s guide to accelerometers \[EB/OL\] . https://www.dimensionengineering.com/info/accelerometers

\[24\] 三轴加速度传感器的原理和应用\[EB/OL\] . https://blog.csdn.net/weixin_34186931/article/details/85826506.

\[25\] 三轴加速度传感器原理\[EB/OL\] . http://www.elecfans.com/yuanqijian/sensor/201910171093891.html

\[26\]\[EB/OL\] .

\[27\]\[EB/OL\] .

\[28\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .

\[\]\[EB/OL\] .












