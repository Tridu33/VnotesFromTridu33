# 1. google文本翻译api




https://cloud.google.com/translate/docs/?hl=zh-cn




使用Cloud Translation，可以将任意的字符串翻译为API支持的语言。由于语言检测功能的存在，即使在源语言未知的情况下，也能使用该API。

将要学习的东西

创建Cloud Translation API请求，使用curl调用API
翻译文本的方法
高级版（Premium Edition）的使用方法
检测语言




https://segmentfault.com/a/1190000014205232 使用谷歌Cloud Translation API翻译文本


free-google-translate
Free Google Translator API 免费的Google翻译，其中的破解思路主要来源于将 https://translate.google.cn 的web访问方式模拟成全部代码的形式来控制api的访问


大量的相同IP请求会导致Google翻译接口返回 429 Too many requests
建议处理方案：每一个app客户端自己去请求此接口，就可以避免只有一个IP的服务器去请求


大量的请求也会使此接口的服务不可用

免费的Google Translate是适用于Google的免费翻译API的工具，回购协议的主要思想来自网络https://translate.google.cn翻译，我们使用黑客手段访问网络翻译api来翻译文本。

https://github.com/VictorZhang2014/free-google-translate


Python使用
```
text = "Hello world"
GoogleTrans().query(text, lang_to='zh-CN') 
```
最初一段待翻译的文本，和目标翻译语言代码，然后你就会得到翻译结果，该接口会自动识别输入的语言代码

输出结果是：

翻译前：Hello world，翻译前code：en
翻译后：你好，世界, 翻译后code：zh-CN








# 2. baidu翻译api



https://api.fanyi.baidu.com/api/trans/product/apidoc

通用翻译API HTTP地址：

http://api.fanyi.baidu.com/api/trans/vip/translate

通用翻译API HTTPS地址：

https://fanyi-api.baidu.com/api/trans/vip/translate


# 3. parser读取识别html,ass字幕文件等等需要翻译的文本信息，然后api翻译之后自动插入需要填充地方，就能得到markdown，html,ass,等文件批量自动翻译软件




 如果我需要翻译整个网页，尖括号内的标签无法原样输出，怎么办？

翻译API会将传入的所有字符串当做可翻译字符，目前暂时无法区分哪些部分需原样保留，因此API不适合直接处理html文件。您可将html文件进行译前处理，抽取出待翻译文本，传入API翻译后再回填。




















