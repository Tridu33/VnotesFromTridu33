# 1. TensorFlow-js

粗暴教程有介绍


TensorFlow.js 提供了一系列预训练好的模型，方便大家快速地给自己的程序引入人工智能能力。

模型库 GitHub 地址：[https://github.com/tensorflow/tfjs-models](https://github.com/tensorflow/tfjs-models)，其中模型分类包括图像识别、语音识别、人体姿态识别、物体识别、文字分类等。

由于这些 API 默认模型文件都存储在谷歌云上，直接使用会导致中国用户无法直接读取。在程序内使用模型 API 时要提供 modelUrl 的参数，可以指向谷歌中国的镜像服务器。

谷歌云的 base url 是 [https://storage.googleapis.com](https://storage.googleapis.com)， 中国镜像的 base url 是 [https://www.gstaticcnapps.cn](https://www.gstaticcnapps.cn) 模型的 url path 是一致的。以 posenet 模型为例：

-   谷歌云地址是：**https://storage.googleapis.com**/tfjs-models/savedmodel/posenet/mobilenet/float/050/model-stride16.json
    
-   中国镜像地址是：**https://www.gstaticcnapps.cn**/tfjs-models/savedmodel/posenet/mobilenet/float/050/model-stride16.json

















