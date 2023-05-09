# PyTorch学习：动态图和静态图




blog.csdn.net/qq_35447659/article/details/83898172



>目前神经网络框架分为静态图框架和动态图框架，PyTorch 和 TensorFlow、Caffe 等框架最大的区别就是他们拥有不同的计算图表现形式。 TensorFlow 使用静态图，这意味着我们先定义计算图，然后不断使用它，而在 PyTorch 中，每次都会重新构建一个新的计算图。通过这次课程，我们会了解静态图和动态图之间的优缺点。



其实tensorflow1.x使用静态图session，但是tensorflow2.x直接起飞，即时计算方便调试，还招安了keras内嵌，框架互相学习趋同的大势所趋，都在变得简单易行
