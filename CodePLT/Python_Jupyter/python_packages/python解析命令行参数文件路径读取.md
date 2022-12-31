# 1. path


```
import sys
print sys.argv[0]#获得的是当前执行脚本的位置（若在命令行执行的该命令，则为空）

```



```
import os
print os.getcwd()#获得当前工作目录
print os.path.abspath('.')#获得当前工作目录
print os.path.abspath('..')#获得当前工作目录的父目录
print os.path.abspath(os.curdir)#获得当前工作目录
```

```
print os.path.relpath("d:/MyProj/MyFile.txt")
#..\MyProj\MyFile.txt
```
 注意用os.chdir(dir)改变当前比较路径
```
path = "..\MyProj\MyFile.txt"
print os.path.abspath(path)
#D:\MyProj\MyFile.txt
```



[TensorFlow』从磁盘读取数据](https://www.cnblogs.com/hellcat/p/8568064.html)


tensorflow read model files:

```
    path ="/data0/user/data/fenlei/datadir"
    image_options = {'resize': True, 'resize_size': IMAGE_SIZE}
    aa=BatchDatset(image_options, path)# config package dict,then the relpath

```


具体使用：
```
# 读取图片，并进行解码
    image = tf.read_file(imagepath)
    image = tf.image.decode_jpeg(image, channels=IMAGE_CHANNELS)
```













# 2. python解析命令行参数




https://www.cnblogs.com/qi-yuan-008/p/11953518.html












