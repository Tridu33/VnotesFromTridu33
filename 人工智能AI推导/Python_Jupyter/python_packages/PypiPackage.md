

一个文件极简版本

https://blog.csdn.net/Fendaki/article/details/85158438



```bash

>python setup.py install
running install
running build
running build_py
creating build
creating build\lib
copying mymodule.py -> build\lib
running install_lib
copying build\lib\mymodule.py -> D:\ProgramData\Anaconda3\Lib\site-packages
byte-compiling D:\ProgramData\Anaconda3\Lib\site-packages\mymodule.py to mymodule.cpython-38.pyc
running install_egg_info
Writing D:\ProgramData\Anaconda3\Lib\site-packages\mymodule-1.0-py3.8.egg-info


```
实际只有一个文件的话，会直接安装在D:\ProgramData\Anaconda3\Lib\site-packages\mymodule.py连个文件夹都没有这么没牌面。
D:\ProgramData\Anaconda3\Lib\site-packages\mymodule-1.0-py3.8.egg-info这里存储元信息，其实没啥用不需要关心
D:\ProgramData\Anaconda3\Lib\site-packages\__pycache__\mymodule.py to mymodule.cpython-38.pyc这放置预编译版本加快执行速度，这样就不需要每次py文件拿来
```python
>ipython

In [*]: from mymodule import add

In [*]: add(2,3)
Out[*]: 5


```


这样不能通过pip卸载，因为：

```
Cannot uninstall 'mymodule'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```


解决此错误的唯一方法是从中手动删除有问题的目录site-packages。

完成此操作后，您可能需要使用重新安装软件包--force-reinstall。


# 1. dir findpackage namespace


https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html cfg配置方法看manimgl当作模板学习

`package_dir={'': 'src'}`什么？为什么我们有一个空字符串作为键？ https://stackoverflow.com/questions/57208736/what-does-an-empty-string-key-for-package-dir-do-in-setup-py 

当您在根级别有多个目录并且模块位于一个目录下时，您可以将该目录定义为根软件包，然后packages将在该目录中查找提供给named参数的所有软件包。Python的官方文档对此进行了很好的描述：
https://docs.python.org/2/distutils/setupscript.html#listing-whole-packages
在这里，如果代码位于下lib目录，然后定义package_dir = {'': 'lib'}＆packages = ['foo']将意味着你是在告诉系统 look for foo module under lib，即`lib/foo/__init__.py`存在。


https://stackoverflow.com/questions/50863045/how-do-tell-setuptools-to-get-my-package-from-src-mypackage


```python
Python 2.7.13 (default, Nov 24 2017, 17:33:09) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from setuptools import find_packages
>>> find_packages()
[]
>>> find_packages(include=['src'])
[]
>>> find_packages(where='src')
['mypackage']
```




https://github.com/pypa/setuptools/issues/1571 find_packages（）和package_dir（）


个人建议src使用setup.cfg而不是布局setup.py

find_namespace_packages其用途。它用于在Python 3隐式命名空间中添加软件包，因此namespace.mypackage。的文件中不应包含任何文件namespace，而只能是软件包。例如：

```
mypackage/__init__.py
mypackage/a/__init__.py
mypackage/b/__init__.py
不需要这样写：
packages = ['mypackage', 'mypackage.a', 'mypackage.b']
```

改成 https://stackoverflow.com/questions/12966216/make-distutils-in-python-automatically-find-packages


```
from distutils.core import setup
from pkgutil import walk_packages

import mypackage

def find_packages(path=__path__, prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name

setup(
    # ... snip ...
    packages = list(find_packages(mypackage.__path__, mypackage.__name__)),
    # ... snip ...
)
```
或者
```
from setuptools import setup, find_packages
packages=find_packages()
```


# 2. 标准版本
short:

```
python setup.py sdist bdist_wheel
python setup.py register
python -m twine upload dist/*
```
在目录中生成dist文件夹，文件夹中有testpg-1.0.tar.gz文件，用户安装的话只需要testpg-1.0.tar.gz文件即可。将此文件解压得到testpg-1.0文件夹，会发现该文件夹有我们刚刚书写的3个py文件，还有一个PKG-INFO，打开该文件，会显示该模块的具体信息：由于我们没有设置，所以为UNKOWN


```
sdist             create a source distribution (tarball, zip file, etc.) 
bdist             create a built (binary) distribution 
bdist_dumb        create a "dumb" built distribution 
bdist_rpm         create an RPM distribution 
bdist_wininst     create an executable installer for MS Windows 
bdist_egg         create an "egg" distribution
bdist_wheel       create *.whl
```
终端定位到此文件夹下，输入以下命令，模块将会被安装到解释器对应的Lib/site-packages目录下： python setup.py install 安装后，会发现Lib/site-packages目录下存在printtest.py文件和printtest-1.0-py3.6.egg-info
应用测试安装是否成功：

```python
import printtest

printtest.test()


In [1]: import pagtest

In [2]: from pagtest.printtest1 import test

In [3]: test()
print test 1

In [4]: from pagtest.printtest2 import test

In [5]: test()
print test 2

```



more

```bash
Microsoft Windows [Version 10.0.18363.1500]
(c) 2019 Microsoft Corporation. All rights reserved.
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame>python -m pip install --user --upgrade setuptools wheel
Looking in indexes: https://pypi.douban.com/simple/
Collecting setuptools
  Downloading https://pypi.doubanio.com/packages/ae/42/2876a3a136f8bfa9bd703518441c8db78ff1eeaddf174baa85c083c1fd15/setuptools-56.0.0-py3-none-any.whl (784
kB)
     |████████████████████████████████| 784 kB ...
Collecting wheel
  Downloading https://pypi.doubanio.com/packages/65/63/39d04c74222770ed1589c0eaba06c05891801219272420b40311cd60c880/wheel-0.36.2-py2.py3-none-any.whl (35 kB
)
Installing collected packages: setuptools, wheel
  WARNING: The script wheel.exe is installed in 'C:\Users\HUMAN\AppData\Roaming\Python\Python38\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed setuptools-56.0.0 wheel-0.36.2
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>python setup.py sdist bdist_wheel
running sdist
running egg_info
creating tridu33LearnWriteMLFrame.egg-info
writing tridu33LearnWriteMLFrame.egg-info\PKG-INFO
writing dependency_links to tridu33LearnWriteMLFrame.egg-info\dependency_links.txt
writing top-level names to tridu33LearnWriteMLFrame.egg-info\top_level.txt
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
reading manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
running check
warning: check: missing required meta-data: url

creating tridu33LearnWriteMLFrame-0.0.1
creating tridu33LearnWriteMLFrame-0.0.1\nn
creating tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
creating tridu33LearnWriteMLFrame-0.0.1\utils
copying files to tridu33LearnWriteMLFrame-0.0.1...
copying LICENSE -> tridu33LearnWriteMLFrame-0.0.1
copying README.md -> tridu33LearnWriteMLFrame-0.0.1
copying setup.py -> tridu33LearnWriteMLFrame-0.0.1
copying nn\__init__.py -> tridu33LearnWriteMLFrame-0.0.1\nn
copying nn\core.py -> tridu33LearnWriteMLFrame-0.0.1\nn
copying tridu33LearnWriteMLFrame.egg-info\PKG-INFO -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\SOURCES.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\dependency_links.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\top_level.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying utils\__init__.py -> tridu33LearnWriteMLFrame-0.0.1\utils
copying utils\utilities.py -> tridu33LearnWriteMLFrame-0.0.1\utils
Writing tridu33LearnWriteMLFrame-0.0.1\setup.cfg
creating dist
Creating tar archive
removing 'tridu33LearnWriteMLFrame-0.0.1' (and everything under it)
running bdist_wheel
running build
running build_py
creating build
creating build\lib
creating build\lib\nn
copying nn\core.py -> build\lib\nn
copying nn\__init__.py -> build\lib\nn
creating build\lib\utils
copying utils\utilities.py -> build\lib\utils
copying utils\__init__.py -> build\lib\utils
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\nn
copying build\lib\nn\core.py -> build\bdist.win-amd64\wheel\.\nn
copying build\lib\nn\__init__.py -> build\bdist.win-amd64\wheel\.\nn
creating build\bdist.win-amd64\wheel\utils
copying build\lib\utils\utilities.py -> build\bdist.win-amd64\wheel\.\utils
copying build\lib\utils\__init__.py -> build\bdist.win-amd64\wheel\.\utils
running install_egg_info
Copying tridu33LearnWriteMLFrame.egg-info to build\bdist.win-amd64\wheel\.\tridu33LearnWriteMLFrame-0.0.1-py3.8.egg-info
running install_scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build\bdist.win-amd64\wheel\tridu33LearnWriteMLFrame-0.0.1.dist-info\WHEEL
creating 'dist\tridu33LearnWriteMLFrame-0.0.1-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'nn/__init__.py'
adding 'nn/core.py'
adding 'utils/__init__.py'
adding 'utils/utilities.py'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/LICENSE'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/METADATA'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/WHEEL'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/top_level.txt'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>pip install --upgrade build
Looking in indexes: https://pypi.douban.com/simple/
Collecting build
  Downloading https://pypi.doubanio.com/packages/74/5e/d8ddec55f619557a828bb0a4036eac991de018418e76262e603d03e443ef/build-0.3.1.post1-py2.py3-none-any.whl (
13 kB)
Requirement already satisfied, skipping upgrade: toml in c:\users\human\appdata\roaming\python\python38\site-packages (from build) (0.10.1)
Requirement already satisfied, skipping upgrade: packaging in d:\programdata\anaconda3\lib\site-packages (from build) (20.4)
Collecting pep517>=0.9
  Downloading https://pypi.doubanio.com/packages/2f/5b/9afe177c8cc801ad9342488f8509c3e237f7c9ec161b7fccb1d61d6d0716/pep517-0.10.0-py2.py3-none-any.whl (19 k
B)
Requirement already satisfied, skipping upgrade: six in c:\users\human\appdata\roaming\python\python38\site-packages (from packaging->build) (1.15.0)
Requirement already satisfied, skipping upgrade: pyparsing>=2.0.2 in d:\programdata\anaconda3\lib\site-packages (from packaging->build) (2.4.7)
Installing collected packages: pep517, build
Successfully installed build-0.3.1.post1 pep517-0.10.0
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>python -m build
Found existing installation: setuptools 47.1.0
Uninstalling setuptools-47.1.0:
  Successfully uninstalled setuptools-47.1.0
Looking in indexes: https://pypi.douban.com/simple/
Collecting wheel
  Using cached https://pypi.doubanio.com/packages/65/63/39d04c74222770ed1589c0eaba06c05891801219272420b40311cd60c880/wheel-0.36.2-py2.py3-none-any.whl (35 k
B)
Collecting setuptools>=40.8.0
  Using cached https://pypi.doubanio.com/packages/ae/42/2876a3a136f8bfa9bd703518441c8db78ff1eeaddf174baa85c083c1fd15/setuptools-56.0.0-py3-none-any.whl (784
 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-56.0.0 wheel-0.36.2
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'C:\Users\HUMAN\AppData\Local\Temp\build-env-rpn4oim1\Scripts\python.exe -m pip install --upgrade pip' command.
running egg_info
writing tridu33LearnWriteMLFrame.egg-info\PKG-INFO
writing dependency_links to tridu33LearnWriteMLFrame.egg-info\dependency_links.txt
writing top-level names to tridu33LearnWriteMLFrame.egg-info\top_level.txt
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
reading manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
running sdist
running egg_info
writing tridu33LearnWriteMLFrame.egg-info\PKG-INFO
writing dependency_links to tridu33LearnWriteMLFrame.egg-info\dependency_links.txt
writing top-level names to tridu33LearnWriteMLFrame.egg-info\top_level.txt
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
reading manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
running check
warning: check: missing required meta-data: url

creating tridu33LearnWriteMLFrame-0.0.1
creating tridu33LearnWriteMLFrame-0.0.1\nn
creating tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
creating tridu33LearnWriteMLFrame-0.0.1\utils
copying files to tridu33LearnWriteMLFrame-0.0.1...
copying LICENSE -> tridu33LearnWriteMLFrame-0.0.1
copying README.md -> tridu33LearnWriteMLFrame-0.0.1
copying setup.py -> tridu33LearnWriteMLFrame-0.0.1
copying nn\__init__.py -> tridu33LearnWriteMLFrame-0.0.1\nn
copying nn\core.py -> tridu33LearnWriteMLFrame-0.0.1\nn
copying tridu33LearnWriteMLFrame.egg-info\PKG-INFO -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\SOURCES.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\dependency_links.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying tridu33LearnWriteMLFrame.egg-info\top_level.txt -> tridu33LearnWriteMLFrame-0.0.1\tridu33LearnWriteMLFrame.egg-info
copying utils\__init__.py -> tridu33LearnWriteMLFrame-0.0.1\utils
copying utils\utilities.py -> tridu33LearnWriteMLFrame-0.0.1\utils
Writing tridu33LearnWriteMLFrame-0.0.1\setup.cfg
Creating tar archive
removing 'tridu33LearnWriteMLFrame-0.0.1' (and everything under it)
Found existing installation: setuptools 47.1.0
Uninstalling setuptools-47.1.0:
  Successfully uninstalled setuptools-47.1.0
Looking in indexes: https://pypi.douban.com/simple/
Collecting wheel
  Using cached https://pypi.doubanio.com/packages/65/63/39d04c74222770ed1589c0eaba06c05891801219272420b40311cd60c880/wheel-0.36.2-py2.py3-none-any.whl (35 k
B)
Collecting setuptools>=40.8.0
  Using cached https://pypi.doubanio.com/packages/ae/42/2876a3a136f8bfa9bd703518441c8db78ff1eeaddf174baa85c083c1fd15/setuptools-56.0.0-py3-none-any.whl (784
 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-56.0.0 wheel-0.36.2
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'C:\Users\HUMAN\AppData\Local\Temp\build-env-jumxzn8_\Scripts\python.exe -m pip install --upgrade pip' command.
running egg_info
writing tridu33LearnWriteMLFrame.egg-info\PKG-INFO
writing dependency_links to tridu33LearnWriteMLFrame.egg-info\dependency_links.txt
writing top-level names to tridu33LearnWriteMLFrame.egg-info\top_level.txt
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
reading manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
Looking in indexes: https://pypi.douban.com/simple/
Requirement already satisfied: wheel in c:\users\human\appdata\local\temp\build-env-jumxzn8_\lib\site-packages (from -r C:\Users\HUMAN\AppData\Local\Temp\bu
ild-reqs-e3ja7cbs.txt (line 1)) (0.36.2)
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.
You should consider upgrading via the 'C:\Users\HUMAN\AppData\Local\Temp\build-env-jumxzn8_\Scripts\python.exe -m pip install --upgrade pip' command.
running bdist_wheel
running build
running build_py
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\nn
copying build\lib\nn\core.py -> build\bdist.win-amd64\wheel\.\nn
copying build\lib\nn\__init__.py -> build\bdist.win-amd64\wheel\.\nn
creating build\bdist.win-amd64\wheel\utils
copying build\lib\utils\utilities.py -> build\bdist.win-amd64\wheel\.\utils
copying build\lib\utils\__init__.py -> build\bdist.win-amd64\wheel\.\utils
running install_egg_info
running egg_info
writing tridu33LearnWriteMLFrame.egg-info\PKG-INFO
writing dependency_links to tridu33LearnWriteMLFrame.egg-info\dependency_links.txt
writing top-level names to tridu33LearnWriteMLFrame.egg-info\top_level.txt
adding license file 'LICENSE' (matched pattern 'LICEN[CS]E*')
reading manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
writing manifest file 'tridu33LearnWriteMLFrame.egg-info\SOURCES.txt'
Copying tridu33LearnWriteMLFrame.egg-info to build\bdist.win-amd64\wheel\.\tridu33LearnWriteMLFrame-0.0.1-py3.8.egg-info
running install_scripts
adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
creating build\bdist.win-amd64\wheel\tridu33LearnWriteMLFrame-0.0.1.dist-info\WHEEL
creating 'D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame\dist\tmp3inh8dcs\tridu33LearnWriteMLFrame-0.0.1-py3
-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'nn/__init__.py'
adding 'nn/core.py'
adding 'utils/__init__.py'
adding 'utils/utilities.py'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/LICENSE'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/METADATA'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/WHEEL'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/top_level.txt'
adding 'tridu33LearnWriteMLFrame-0.0.1.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>python -m pip install --user --upgrade twine
Looking in indexes: https://pypi.douban.com/simple/
Collecting twine
  Downloading https://pypi.doubanio.com/packages/42/ad/713372978a8de58a43c507bf62b9c30c3d7b5cda4e972d563b881620a511/twine-3.4.1-py3-none-any.whl (34 kB)
Requirement already satisfied, skipping upgrade: tqdm>=4.14 in d:\programdata\anaconda3\lib\site-packages (from twine) (4.50.2)
Collecting importlib-metadata>=3.6
  Downloading https://pypi.doubanio.com/packages/52/d0/bdb31463f2d9ca111e39b268518e9baa3542ef73ca449b711a7b4da69764/importlib_metadata-3.10.1-py3-none-any.w
hl (14 kB)
Requirement already satisfied, skipping upgrade: pkginfo>=1.4.2 in d:\programdata\anaconda3\lib\site-packages (from twine) (1.6.1)
Collecting readme-renderer>=21.0
  Downloading https://pypi.doubanio.com/packages/39/a5/459adfa22ea237f6e8d0fa95ad29d7369579a5eec26f016ab34bb7f8359c/readme_renderer-29.0-py2.py3-none-any.wh
l (15 kB)
Collecting rfc3986>=1.4.0
  Downloading https://pypi.doubanio.com/packages/78/be/7b8b99fd74ff5684225f50dd0e865393d2265656ef3b4ba9eaaaffe622b8/rfc3986-1.4.0-py2.py3-none-any.whl (31 k
B)
Requirement already satisfied, skipping upgrade: colorama>=0.4.3 in c:\users\human\appdata\roaming\python\python38\site-packages (from twine) (0.4.3)
Collecting requests-toolbelt!=0.9.0,>=0.8.0
  Downloading https://pypi.doubanio.com/packages/60/ef/7681134338fc097acef8d9b2f8abe0458e4d87559c689a8c306d0957ece5/requests_toolbelt-0.9.1-py2.py3-none-any
.whl (54 kB)
     |████████████████████████████████| 54 kB 240 kB/s
Requirement already satisfied, skipping upgrade: requests>=2.20 in d:\programdata\anaconda3\lib\site-packages (from twine) (2.24.0)
Requirement already satisfied, skipping upgrade: keyring>=15.1 in d:\programdata\anaconda3\lib\site-packages (from twine) (21.4.0)
Requirement already satisfied, skipping upgrade: zipp>=0.5 in d:\programdata\anaconda3\lib\site-packages (from importlib-metadata>=3.6->twine) (3.4.0)
Requirement already satisfied, skipping upgrade: bleach>=2.1.0 in d:\programdata\anaconda3\lib\site-packages (from readme-renderer>=21.0->twine) (3.2.1)
Requirement already satisfied, skipping upgrade: docutils>=0.13.1 in d:\programdata\anaconda3\lib\site-packages (from readme-renderer>=21.0->twine) (0.16)
Requirement already satisfied, skipping upgrade: Pygments>=2.5.1 in d:\programdata\anaconda3\lib\site-packages (from readme-renderer>=21.0->twine) (2.7.2)
Requirement already satisfied, skipping upgrade: six in c:\users\human\appdata\roaming\python\python38\site-packages (from readme-renderer>=21.0->twine) (1.
15.0)
Requirement already satisfied, skipping upgrade: chardet<4,>=3.0.2 in d:\programdata\anaconda3\lib\site-packages (from requests>=2.20->twine) (3.0.4)
Requirement already satisfied, skipping upgrade: idna<3,>=2.5 in d:\programdata\anaconda3\lib\site-packages (from requests>=2.20->twine) (2.10)
Requirement already satisfied, skipping upgrade: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in d:\programdata\anaconda3\lib\site-packages (from requests>=2.20-
>twine) (1.25.11)
Requirement already satisfied, skipping upgrade: certifi>=2017.4.17 in d:\programdata\anaconda3\lib\site-packages (from requests>=2.20->twine) (2020.6.20)
Requirement already satisfied, skipping upgrade: pywin32-ctypes!=0.1.0,!=0.1.1; sys_platform == "win32" in d:\programdata\anaconda3\lib\site-packages (from
keyring>=15.1->twine) (0.2.0)
Requirement already satisfied, skipping upgrade: webencodings in d:\programdata\anaconda3\lib\site-packages (from bleach>=2.1.0->readme-renderer>=21.0->twin
e) (0.5.1)
Requirement already satisfied, skipping upgrade: packaging in d:\programdata\anaconda3\lib\site-packages (from bleach>=2.1.0->readme-renderer>=21.0->twine)
(20.4)
Requirement already satisfied, skipping upgrade: pyparsing>=2.0.2 in d:\programdata\anaconda3\lib\site-packages (from packaging->bleach>=2.1.0->readme-rende
rer>=21.0->twine) (2.4.7)
Installing collected packages: importlib-metadata, readme-renderer, rfc3986, requests-toolbelt, twine
  WARNING: The script twine.exe is installed in 'C:\Users\HUMAN\AppData\Roaming\Python\Python38\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed importlib-metadata-3.10.1 readme-renderer-29.0 requests-toolbelt-0.9.1 rfc3986-1.4.0 twine-3.4.1
--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>python setup.py register
running register
running check
warning: Check: missing required meta-data: url

warning: Check: This command has been deprecated. Use `twine check` instead: https://packaging.python.org/guides/making-a-pypi-friendly-readme#validating-re
structuredtext-markup

warning: Check: Not checking long description content type 'text/markdown', this command only checks 'text/x-rst'.

We need to know who you are, so please choose either:
 1. use your existing login,
 2. register as a new user,
 3. have the server generate a new password for you (and email it to you), or
 4. quit
Your selection [default 1]:
1
Username: tridu33
Password:
Registering tridu33LearnWriteMLFrame to https://upload.pypi.org/legacy/
Server response (410): Project pre-registration is no longer required or supported, upload your files instead.

--------------------------------------------------------------------------------------------------------------------------
(base) D:\tridu33\Py\tridu33LearnWriteMLFrame\tridu33LearnWriteMLFrame>python -m twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: tridu33
Enter your password:
Uploading tridu33LearnWriteMLFrame-0.0.1-py3-none-any.whl
100%|███████████████████████████████████████████████████████████████████████████
100%|███████████████████████████████████████████████████████████████████████████
██████████████████████████████████████| 7.92k/7.92k [00:02<00:00, 3.11kB/s]
Uploading tridu33LearnWriteMLFrame-0.0.1.tar.gz
100%|███████████████████████████████████████████████████████████████████████████
██████████████████████████████████████| 7.35k/7.35k [00:01<00:00, 5.62kB/s]

View at:
https://pypi.org/project/tridu33LearnWriteMLFrame/0.0.1/


```








