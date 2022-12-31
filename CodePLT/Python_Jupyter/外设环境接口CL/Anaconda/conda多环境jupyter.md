# conda多环境jupyter




https://zhuanlan.zhihu.com/p/64100305










```
pip install ipykernel
```


```
python -m ipykernel install --user --name py27 --display-name "Python (py27)"
```



>The--namevalue is used by Jupyter internally. These commands will overwrite any existing kernel with the same name.--display-nameis what you see in the notebook menus.[2]

```
import sys
print (sys.executable)
```




删除

```
conda remove --name py27 --all
```

^https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
^https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments



新环境pip版本有要求吗？



```
You are using pip version 9.0.1, however version 20.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(py27) PS C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\BasePythonNotesBooks\Books-py\notebooks> python -m pip install --upgrade pip
Cache entry deserialization failed, entry ignored
Collecting pip
  Downloading https://pypi.doubanio.com/packages/5a/4a/39400ff9b36e719bdf8f31c99fe1fa7842a42fa77432e584f707a5080063/pip-20.2.2-py2.py3-none-any.whl (1.5MB)
    100% |¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€¨€| 1.5MB 298kB/s
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Uninstalling pip-9.0.1:
      Successfully uninstalled pip-9.0.1
Successfully installed pip-20.2.2
```


会不会pip 20的安装包变成python3的包？




