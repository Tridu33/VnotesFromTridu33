


# 1. python交互模式中怎么运行py文件





python交互模式中怎么运行py文件
https://www.zhihu.com/answer/135304134



python2交互模式下键入execfile(' 文件名.py')
python3 变成 `exec(open("./filename").read())`

```
exec( (open("D:\\tridu33\z3solverBlockWorld.py").read() ) )
```


import文件import sys;
sys.path.append("E:\python\学习demo");
import chapter1_1.py


ipython下，%run python_file.py

利用cmd，在开始搜索那里输入cmd,点开命令提示符，然后把.py文件拖到cmd窗口，按回车就可以了。






