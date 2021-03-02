# python环境变量



# 环境变量

[windows安装包添加自己的路经的位置file:///C:/ProgramData/Miniconda3/Lib/site-packages/.py](file:///C:/ProgramData/Miniconda3/Lib/site-packages/.py)


linux下目录：anaconda/lib/pythonx.x/site-packages

python环境变量
https://www.cnblogs.com/hujq1029/p/7133237.html


加入当前目录
```
import os,sys
sys.path.append(os.getcwd())
```

加入上一层目录和绝对路径

```
import sys
sys.path.append('..') #表示导入当前文件的上层目录到搜索路径中
sys.path.append('/home/model') # 绝对路径
from folderA.folderB.fileA import functionA
```

python临时环境变量

```
import os

# 设置环境变量
os.environ['WORKON_HOME']="value"
# 获取环境变量方法1
os.environ.get('WORKON_HOME')
#获取环境变量方法2(推荐使用这个方法)
os.getenv('path')
# 删除环境变量
del os.environ['WORKON_HOME']
其他key值：
os.environ['HOMEPATH']:当前用户主目录。
os.environ['TEMP']:临时目录路径。
os.environ['PATHEXT']:可执行文件。
os.environ['SYSTEMROOT']:系统主目录。
os.environ['LOGONSERVER']:机器名。
os.environ['PROMPT']:设置提示符。
```


Python 永久变量






```
import os
path=r"E:\env"
command =r"setx WORK1 %s /m"%path
os.system(command)
```















