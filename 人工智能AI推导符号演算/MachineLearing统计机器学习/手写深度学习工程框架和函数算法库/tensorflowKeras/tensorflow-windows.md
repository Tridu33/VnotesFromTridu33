# 1. tensorflow-windows


C:\ProgramData\Miniconda3\Lib\site-packages\tensorflow


[https://github.com/fo40225/tensorflow-windows-wheel/tree/master/2.0.0/py37/CPU/avx2](https://github.com/fo40225/tensorflow-windows-wheel/tree/master/2.0.0/py37/CPU/avx2)


```
pip install https://github.com/fo40225/tensorflow-windows-wheel/blob/master/2.0.0/py37/CPU/avx2/tensorflow-2.0.0-cp37-cp37m-win_amd64.whl
```

pip install https://pypi.doubanio.com/simple/mkl-2019.0-py2.py3-none-win_amd64.whl

（1）[下载](https://blog.csdn.net/beyond9305/article/details/95896135?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

（2）在刚安装的Anaconda3\Lib\site-packages\文件下新建文件夹tensorflow；

（3）将下载的tensorflow安装包复制到Anaconda\Lib\site-packages\tensorflow文件夹中；

（4）通过cmd命令进入到Anaconda\Lib\site-packages\tensorflow目录下，执行安装命令


[https://pypi.doubanio.com/simple/tensorflow](https://pypi.doubanio.com/simple/tensorflow)




[https://pypi.doubanio.com/simple/tensorboard](https://pypi.doubanio.com/simple/tensorboard)







[Tensorflow2.0版本高效实用指南快速上手3个建议——Tensor2.0版本与1.0版本有哪些改动之处tf1.x和tf2.X](https://blog.csdn.net/weixin_37479258/article/details/100108368?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)


AttributeError: module 'tensorflow' has no attribute 'Session'
因为是tensorflow 2.0版本


```
import tensorflow as tf

sess=tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))

```








