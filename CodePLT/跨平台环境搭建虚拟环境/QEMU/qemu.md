# qemu
https://www.qemu.org  官网

https://qemu.weilnetz.de/doc/qemu-doc.html  帮助文档



https://qemu.weilnetz.de/w64/ 2019-08-15 21:55  158   SHA-512 for installer





QEMU是一套由[法布里斯·贝拉](https://baike.baidu.com/item/%E6%B3%95%E5%B8%83%E9%87%8C%E6%96%AF%C2%B7%E8%B4%9D%E6%8B%89/9358492)(Fabrice Bellard)所编写的以[GPL](https://baike.baidu.com/item/GPL)许可证分发源码的模拟处理器，在[GNU/Linux](https://baike.baidu.com/item/GNU%2FLinux)平台上使用广泛。[Bochs](https://baike.baidu.com/item/Bochs)，[PearPC](https://baike.baidu.com/item/PearPC)等与其类似，但不具备其许多特性，比如高速度及跨平台的特性，通过[KQEMU](https://baike.baidu.com/item/KQEMU)这个闭源的加速器，QEMU能模拟至接近真实电脑的速度。













https://github.com/qemu




1.命令参数: 

 -L dir :指向 BIOS 和 VGA BIOS 所在目录(一般我们使用”-L .”) 

 -hda/-hdb/-hdd/-hdc “文件名” :虚拟机系统安装文件 

 -cdrom “文件名” :使用“文件名”作为光盘景象（文件应该是 ISO 类型） 

*Windows 下，可以通过下列命令使用实体光盘: -cdrom //./x: -> x 代表光盘名称/位置

例如:-cdrom //./e: -> 使用 E:\ 为光盘* 

 -fda/-fdb “文件名” :使用“文件名”作为磁盘 0/1 镜像. 

 -boot \[a|b|c\] :使用磁盘 a，光盘 d，或者硬盘 c 启动. 

 -m 容量 :指定内存的大小，单位是 MB. 

 -soundhw c1,„: 使用声卡设备. 

 -soundhw ? :列出所有可使用的声卡 -soundhw all 使用全部声卡 

 -usb :允许使用 usb 设备. 

 -usbdevice :名字 添加一个 usb 设备“名字”. 

 -net nic :创建一块新的网卡. 

上面就是常用的命令参数.如果对各种操作系统下的应用有迷惑,可以到这里查找相关资料











