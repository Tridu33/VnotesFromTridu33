# Spark




blog.csdn.net/u011513853/article/details/52865076




>提醒后来人 从spark2.0开始SQL context available as sqlContext.被替换成了Spark session available as 'spark'.所以只要有后面这句话就正确了。另外官网目前只提供spark2.4.5对应scala版本2.12.0，hadoop版本应该都可以，我采用的2.6.0可以正常运行







## 2


### windows 运行spark或者hadoop程序报winutils.exe错误

1.下载 winutils.exe：http://download.csdn.net/download/ypsong2011/9109143或者https://github.com/srccodes/hadoop-common-2.2.0-bin

2.将此文件放置在某个目录下，比如C:\winutils\bin\中。

3.在程序的一开始声明：System.setProperty("hadoop.home.dir", "c:\\winutil\\")


















