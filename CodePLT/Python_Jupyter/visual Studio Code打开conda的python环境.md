# 1. visual Studio Code打开conda的python环境




然后在File---->Preferences---->Settings里面，  
选择Extensions----->Python Configuration，如图：

然后点Edit in settings.json
把原本的python路径修改为你需要的子环境python路径即可。
原来是：
```
"python.pythonPath": "C:\\ProgramData\\Miniconda3\\python.exe",
```
更改为：


```
"python.pythonPath": "C:\\ProgramData\\Miniconda3\\python.exe"
```


https://blog.csdn.net/weixin_40040107/article/details/102650433

```
"code-runner.executorMap": {
        "python":"$pythonPath $fullFileName",
    }



```






































































































