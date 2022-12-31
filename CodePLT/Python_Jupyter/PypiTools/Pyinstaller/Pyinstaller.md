


# Pyinstaller
[document](https://pyinstaller.readthedocs.io/en/stable/usage.html#running-pyinstaller-from-python-code)




github.com/pyinstaller/pyinstaller

pypi.org/project/pyinstaller/



```
pyinstaller --onefile --nowindowed --icon='./tridu33.ico' tmp.py
```

把要打包的python文件，想用的图标icon格式的放一个文件夹，然后
```python
 pyinstaller -F --icon="name.ico" name.py
```

，-F表示打包成一个文件，不想显示窗口的话加个-w

```python
pyinstaller -F -w --icon='E:\workspace-eclipse\day1\mydat\favicon.ico' b.py
```



```python
pyinstaller -F .py -w
```


超详细Pyinstaller打包exe+反编译Pyinstaller打包的exe教程+防止反编译教程 - 会飞的瓶盖的文章 - 知乎
https://zhuanlan.zhihu.com/p/59442292
















































































