# pandas



tf.data.Dataset总结 - 张晓辉的文章 - 知乎 https://zhuanlan.zhihu.com/p/59052680


比较好的是[Dataset API入门教程](https://zhuanlan.zhihu.com/p/30751039)， [TensorFlow学习笔记(4): Tensorflow tf.data.Dataset](https://zhuanlan.zhihu.com/p/37106443)等等。这些介绍都非常详细，我就不从头解释了，再看看tf的tutorials就能学个七七八八，剩下的就是实际中的应用。主要是理解下面几个函数的应用

-   tf.data.Dataset的from\_tensor\_slice， TFRecordDataset, TextLineDataset等
-   对Dataset进行transformation: map, batch, shuffle, repeat等
-   Iterator： initializable, reinitializable, feedable iterator等

直接上代码吧:























































