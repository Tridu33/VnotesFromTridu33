

# NLTK-DATA


离线安装路径看这个博客：blog.csdn.net/qq_43140627/article/details/103895811

```
import nltk
nltk.find('.')
```


>  For more information see: https://www.nltk.org/data.html
  Attempted to load ./
  Searched in:
    - 'C:\\Users\\admin/nltk_data'
    - 'C:\\ProgramData\\Miniconda3\\nltk_data'
    - 'C:\\ProgramData\\Miniconda3\\share\\nltk_data'
    - 'C:\\ProgramData\\Miniconda3\\lib\\nltk_data'
    - 'C:\\Users\\admin\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


```
from nltk.book import *
```

临时使用可以每次添加


```
data.path.append(r"G:\nltk_data")
```





blog.csdn.net/ling620/article/details/98940539


```
nltk.download()
```

网络问题无法获得

当打开NLTK下载器时，弹出 [Error 11004]getaddrinfo failed的提示窗口。

在    C:\Windows\System32\drivers\etc   路径下找到hosts文件，并在最后添加  199.232.68.133 raw.githubusercontent.com  IP地址，并保存。这时再打开NLTK下载器，便可以正常打开。


**打包下载**（推荐）：  
http://yunpan.cn/cgGUPFzF3spir （提取码：504e）

下载后放在python/nltk_data目录下即可.
来自这个博客 cnblogs.com/ToDoToTry/archive/2013/01/18/2865941.html

***这里才是正确的下载方式***：最好的方法是用使用@V_can打包好的的包网盘下载[下载地址1：云盘密码znx7](http://pan.baidu.com/s/1slP4wfr)，下来的包nltk_data.zip ***解压到C盘根目录下***，这样是最保险的，防止找不到包。[下载地址2：云盘密码4cp3](http://pan.baidu.com/s/1qYwA240)

  
  
作者：mrlevo520  
链接：https://www.jianshu.com/p/9c48e8edc7aa  










>https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml

这里有个解决方法  jianshu.com/p/9c48e8edc7aa







```
In[4]:from nltk.book import *
# 只输入import nltk 会出错的，但却有很多博客上都这么写，我也母鸡
```








然后我通过，nltk.download()下载，一直出现错误，只好到  
官方下载http://nltk.org/nltk_data/  
另外，也可以到nltk.code.google.com 下载，

  

cnblogs.com/webRobot/p/6065831.html

但是又遇到了下载后，直接放在nltk_data目录，却发现还是不行，程序找不到数据集。  
因此我就用nltk.download()试着下载了一个，观察他的文件位置，这才发现原来有好几个文档目录。  
用tree命令的到其目录结构如下：  
文件夹 PATH 列表  
卷序列号为 00000200 B2F8:ED9D

```

├─chunkers #这一级为nltk_data下的文件夹  
│ └─maxent\_ne\_chunker #这一级为相对应文件夹下的数据文件  
├─corpora      #这一级为nltk_data下的文件夹  
│ ├─abc        #这一级为相对应文件夹下的数据文件  


```








## [这里详细教导如何解决问题](https://blog.csdn.net/weixin_44633882/article/details/104494276)


我们可以看到，尝试加载了`tokenizers/punkt/english.pickle`文件，但没有找到。系统会从`'C:\\Users\\11244/nltk_data'`这几个路径下进行搜索。

OK，我们知道了需要什么文件，应该将这个文件放到哪里。从哪里下载呢？

访问[nltk_data](https://github.com/nltk/nltk_data)，可以选择直接download下来需要的包，再按刚才的路径放好。大概14分钟才能下好吧。



