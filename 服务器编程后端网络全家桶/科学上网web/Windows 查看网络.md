# Windows 查看网络


windows+R执行`perfmon -res` 看端口占用

1.查看某个端口是否被占用

打开命令行，输入：netstat -ano |findstr "20880"

2.查看端口被哪个服务占用

tasklist | findstr 1180




有什么比较好的Windows流量监控软件？ - 深信服产教中心的回答 - 知乎
https://www.zhihu.com/question/60345119/answer/2314116703 


后者实时抓包看
winshark

TrafficMonitor
Traffic Monitor 是一款开源免费的 Windows 平台系统信息监控软件。功能全面，界面也十分美观。

可以显示实时网速、CPU 和内存利用率，支持桌面悬浮窗和任务栏两种显示模式，和自定义皮肤、历史流量统计等功能。






 Wise System Monitor
非常简洁的一款系统性能监测工具，支持网速、内存、CPU 和核心部件温度显示。

在桌面悬浮窗实时显示软件的系统占用率，点击进程旁边的 “叉号” 可以快速关闭进程。




Open Hardware Monitor
一款免费开源的电脑信息检测工具，绿色软件无需安装。

可以监控电脑的温度、风扇转速、电压、负载和功耗等。既可以显示在独立的窗口，也支持桌面小工具和系统托盘。



软媒系统雷达
软媒魔方中的独立小工具，绿色软件，小巧美观。支持显示 CPU、内存使用率，流量、硬盘读写和温度监控。



游戏加加
游戏加加是一款专门为游戏爱好者制作的系统信息监控软件，可以在桌面和游戏中显示系统监测信息。

提供了 CPU 和 GPU 的温度、频率、占用，风扇转速，显存、内存占用，FPS、网络速度等，可以根据自己的需求选择显示项目。

# 查看网络端口占用



利用 netstat 查看网络状态命令：


netstat -an|grep 端口号









