[TOC]


# 1. 备忘必备snippet  




生成文件
pip freeze > requirements.txt
依赖库会导到于requirements.txt

从requirements.txt安装依赖库
pip install -r requirements
当提示权限不够时，前面加上sudo








如果您的代码包仅供内部使用，又不想直接发送源码，则可以将代码打包成whl文件
打包成whl命令

```
# --wheel-dir: 为打包存储的路径 
# 空格后为需要打包的工程路径
pip wheel --wheel-dir=D:\\work\\base_package\\dist D:\\work\\base_package
```



打包完成后就可以看到smart-0.0.1-py3-none-any.whl文件了，将此文件发送给有需要的同事后，对方就可以使用

```
pip install smart-0.0.1-py3-none-any.whl
```


来安装当前库了

作者：East_wu
链接：https://www.jianshu.com/p/19f1e564a29d

## 1.1. __init__.py功能

cnblogs.com/BlueSkyyj/p/9415087.html

```
package
  |- subpackage1
      |- __init__.py
      |- a.py
  |- subpackage2
      |- __init__.py
      |- b.py
```

有：

```
import subpackage1.a 
# 将模块subpackage.a导入全局命名空间，例如访问a中属性时用subpackage1.a.attr
from subpackage1 import a 
#　将模块a导入全局命名空间，例如访问a中属性时用a.attr_a
from subpackage.a import attr_a 
# 将模块a的属性直接导入到命名空间中，例如访问a中属性时直接用attr_a
```



## 1.2. **程序打包**

通过执行下列语句来进行打包：

```text
python setup.py xxx 
```

其中xxx可以是下列几种方式中其中一个：

```text
sdist             create a source distribution (tarball, zip file, etc.) 
bdist             create a built (binary) distribution 
bdist_dumb        create a "dumb" built distribution 
bdist_rpm         create an RPM distribution 
bdist_wininst     create an executable installer for MS Windows 
bdist_egg         create an "egg" distribution
 bdist_wheel      生成wheel包
```

举个例子：

```text
python setup.py sdist　#生成的文件支持 pip 
```

此时在根目录出现了dist文件夹，里面有name-version.tar.gz这个文件，这就是我们要发布到PyPI的压缩包了。





制作压缩包tar

```
\packages\3> python setup.py sdist                                         running sdist
running egg_info
creating pagtest.egg-info
writing pagtest.egg-info\PKG-INFO
writing dependency_links to pagtest.egg-info\dependency_links.txt
writing requirements to pagtest.egg-info\requires.txt
writing top-level names to pagtest.egg-info\top_level.txt
writing manifest file 'pagtest.egg-info\SOURCES.txt'
reading manifest file 'pagtest.egg-info\SOURCES.txt'
writing manifest file 'pagtest.egg-info\SOURCES.txt'
running check
creating pagtest-1.0.0
creating pagtest-1.0.0\pagtest
creating pagtest-1.0.0\pagtest.egg-info
copying files to pagtest-1.0.0...
copying README.txt -> pagtest-1.0.0
copying setup.py -> pagtest-1.0.0
copying pagtest\__init__.py -> pagtest-1.0.0\pagtest
copying pagtest\printtest1.py -> pagtest-1.0.0\pagtest
copying pagtest\printtest2.py -> pagtest-1.0.0\pagtest
copying pagtest.egg-info\PKG-INFO -> pagtest-1.0.0\pagtest.egg-info
copying pagtest.egg-info\SOURCES.txt -> pagtest-1.0.0\pagtest.egg-info
copying pagtest.egg-info\dependency_links.txt -> pagtest-1.0.0\pagtest.egg-info
copying pagtest.egg-info\requires.txt -> pagtest-1.0.0\pagtest.egg-info
copying pagtest.egg-info\top_level.txt -> pagtest-1.0.0\pagtest.egg-info
Writing pagtest-1.0.0\setup.cfg
creating dist
Creating tar archive
removing 'pagtest-1.0.0' (and everything under it)
```

制作whl安装包

```
packages\3> python setup.py bdist_wheel                                   running bdist_wheel
running build
running build_py
creating build
creating build\lib
creating build\lib\pagtest
copying pagtest\printtest1.py -> build\lib\pagtest
copying pagtest\printtest2.py -> build\lib\pagtest
copying pagtest\__init__.py -> build\lib\pagtest
installing to build\bdist.win-amd64\wheel
running install
running install_lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\wheel
creating build\bdist.win-amd64\wheel\pagtest
copying build\lib\pagtest\printtest1.py -> build\bdist.win-amd64\wheel\.\pagtest
copying build\lib\pagtest\printtest2.py -> build\bdist.win-amd64\wheel\.\pagtest
copying build\lib\pagtest\__init__.py -> build\bdist.win-amd64\wheel\.\pagtest
running install_egg_info
running egg_info
writing pagtest.egg-info\PKG-INFO
writing dependency_links to pagtest.egg-info\dependency_links.txt
writing requirements to pagtest.egg-info\requires.txt
writing top-level names to pagtest.egg-info\top_level.txt
reading manifest file 'pagtest.egg-info\SOURCES.txt'
writing manifest file 'pagtest.egg-info\SOURCES.txt'
Copying pagtest.egg-info to build\bdist.win-amd64\wheel\.\pagtest-1.0.0-py3.7.egg-info
running install_scripts
creating build\bdist.win-amd64\wheel\pagtest-1.0.0.dist-info\WHEEL
creating 'dist\pagtest-1.0.0-py3-none-any.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'pagtest/__init__.py'
adding 'pagtest/printtest1.py'
adding 'pagtest/printtest2.py'
adding 'pagtest-1.0.0.dist-info/METADATA'
adding 'pagtest-1.0.0.dist-info/WHEEL'
adding 'pagtest-1.0.0.dist-info/top_level.txt'
adding 'pagtest-1.0.0.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
```


```
python setup.py sdist bdist_wheel
```



4.上传到PyPI上。上传时，可以建立一个账户验证文件~/.pypirc（Windows不可以，因为文件命名中含有非法字符），也可以在上传时输入账户和密码。

```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <username>
password = <password>

```
5.将命令行定位到此文件夹下，输入命令对dist目录下的pagtest-1.0.0.tar.gzt包进行上传，twine为Python包需要安装：

```
twine upload dist/*

```




如果你想阅读更多关于包装的Python库，你可以做以下事情：

-   阅读有关使用[setuptools](https://link.zhihu.com/?target=https%3A//packaging.python.org/key_projects/%23setuptools)在[打包和分发项目中](https://link.zhihu.com/?target=https%3A//packaging.python.org/guides/distributing-packages-using-setuptools/)打包库的 更多信息。
-   阅读[包装二进制扩展](https://link.zhihu.com/?target=https%3A//packaging.python.org/guides/packaging-binary-extensions/)。
-   考虑诸如[flit](https://link.zhihu.com/?target=https%3A//packaging.python.org/key_projects/%23flit)，[hatch](https://link.zhihu.com/?target=https%3A//github.com/ofek/hatch)和[poetry之类的](https://link.zhihu.com/?target=https%3A//github.com/sdispater/poetry)[setuptools的](https://link.zhihu.com/?target=https%3A//packaging.python.org/key_projects/%23setuptools)替代方案。














## 1.3. **发布到PyPI**

首先我们需要在PyPI上注册一个帐号，并在本地用户根目录下创建文件~/.pypirc，这样以后就不需要输入帐号密码了。

```text
[distutils]
index-servers=pypi

[pypi]
repository = https://pypi.python.org/pypi
username = <username>
password = <password> 
```

接下来，需要在PyPI网站上注册一个项目，网站提供三种方式注册，选择一种即可，最简单的是通过上传打包时生成的PKG-INFO文件，生成项目信息。此步骤只需在第一次发布时操作。

接下来就是最后一步，上传打包好的库。我们这里是用twine，如果环境中没有安装，需要先采用pip install twine安装即可。

```text
twine upload dist/* 
```

此时在网页上就可以看到自己的源代码包啦，并且可以通过使用pip install packagename,就可以使用我们自己写的Python库了。














# 2. python制作自己的whl安装包



[在Python中安装包的三种方法](https://www.jianshu.com/p/c6055e8873ee)

![](https://upload-images.jianshu.io/upload_images/234392-59937eefa274b70b.png?imageMogr2/auto-orient/strip|imageView2/2/w/527/format/webp)

-   Distutils：Python 标准的包管理工具，扩展性不够。
-   Setuptools：比 Distutils 提供了更多的功能，虽然不是官方的，但却是事实上的标准。
- 如何编写setup.py来对一个简单的python模块进行打包。

开发者可以基于 Distutils 或 Setuptools 生成这三种类型的包。

3 file type of install 

- tar.gz
- egg# replae by wheel 
- wheel

easy_install 只能安装包，不能卸载包。

easy_install 不能安装 wheel 格式的包（pip 可以，但 pip 不能安装 egg 格式的包）

# 3. 利用distutils

[利用distutils制作自己的工具包小例子](https://blog.csdn.net/Fendaki/article/details/85158438)

```
> python setup.py install                                   running install
running build
running build_py
creating build
creating build\lib
copying mymodule.py -> build\lib
running install_lib
copying build\lib\mymodule.py -> C:\ProgramData\Miniconda3\Lib\site-packages
byte-compiling C:\ProgramData\Miniconda3\Lib\site-packages\mymodule.py to mymodule.cpython-37.pyc
  File "C:\ProgramData\Miniconda3\Lib\site-packages\mymodule.py", line 7
    if __name__='__main__':
               ^
SyntaxError: invalid syntax

running install_egg_info
Writing C:\ProgramData\Miniconda3\Lib\site-packages\mymodule-1.0-py3.7.egg-info
```
把=变成==就行，意思看这里：
if \_\_name\_\_ == '\_\_main\_\_' 如何正确理解? - 留德华叫兽的回答 - 知乎 https://www.zhihu.com/question/49136398/answer/517623249

[https://blog.konghy.cn/2017/04/24/python-entry-program/](https://blog.konghy.cn/2017/04/24/python-entry-program/) 解释了python -m和__name__












# 4. 详例将python包发布到PyPI和制作whl文件




[详例将python包发布到PyPI和制作whl文件](https://blog.csdn.net/winycg/article/details/80025432)

[官网教程https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)




[https://github.com/pypa/sampleproject/](https://github.com/pypa/sampleproject/)
















```
|--smart
|  |--static
|  |  |--icon.svg
|  |  |--confg.json
|  |--engine
|  |  |--__init__.py
|  |  |--core.py
|  |--__init__.py
|  |--__version__.py
|  |--api.py
|  |--utils.py
|--tests
|  |--__init__.py
|--LICENSE
|--README.rst
|--setup.py
```



主要有`MANIFEST.in`和`setup.py`两个文件。`MANIFEST.in`表示打包时不会被自动包含进去的附加文件清单。`setup.py`是打包程序配置文件，需要设置一些选项。此外，`setup.cfg`是包含setup.py额外配置信息的文件

 







## 4.1. setuptools重点在于setup.py文件编写：


可以参考一下：

-   [PyPA sample project](https://link.jianshu.com/?t=https://github.com/pypa/sampleproject)这是一个官方示例库结构。
-   [Python Packaging User Guide](https://link.jianshu.com/?t=http://python-packaging-user-guide.readthedocs.io/en/latest/)这是Python打包的官方英文文档。


https://www.dashen.tech/2019/06/07/%E5%88%B6%E4%BD%9Cpython%E5%8C%85%E5%B9%B6%E4%B8%8A%E4%BC%A0pypi/ 一个教程blog

```python
import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    # 包的分发名称，使用字母、数字、_、-
    name="dashen",
     # 版本号, 版本号规范：https://www.python.org/dev/peps/pep-0440/
    version="0.0.1",
    # 作者名
    author="fliter",
     # 作者邮箱
    author_email="i@dashen.tech",  
    # 包的简介描述
    description="我的第二个python包",
    # 包的详细介绍(一般通过加载README.md)
    long_description=long_description, 
    # 和上条命令配合使用，声明加载的是markdown文件
    long_description_content_type="text/markdown",
    # 项目开源地址
    url="http://www.dashen.tech",
     # 如果项目由多个文件组成，我们可以使用find_packages()自动发现所有包和子包，而不是手动列出每个包，在这种情况下，包列表将是example_pkg
    packages=setuptools.find_packages(),
    # 关于包的其他元数据(metadata)
    classifiers=[
         # 该软件包仅与Python3兼容
        "Programming Language :: Python :: 3",
        # 根据MIT许可证开源
        "License :: OSI Approved :: MIT License",
        # 与操作系统无关
        "Operating System :: OS Independent",
    ],
)
```







```
d> python setup.py sdist                                    running sdist
running egg_info
creating printtest.egg-info
writing printtest.egg-info\PKG-INFO
writing dependency_links to printtest.egg-info\dependency_links.txt
writing top-level names to printtest.egg-info\top_level.txt
writing manifest file 'printtest.egg-info\SOURCES.txt'
reading manifest file 'printtest.egg-info\SOURCES.txt'
writing manifest file 'printtest.egg-info\SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md

running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) must be supplied

creating printtest-1.0
creating printtest-1.0\printtest.egg-info
copying files to printtest-1.0...
copying printtest.py -> printtest-1.0
copying setup.py -> printtest-1.0
copying printtest.egg-info\PKG-INFO -> printtest-1.0\printtest.egg-info
copying printtest.egg-info\SOURCES.txt -> printtest-1.0\printtest.egg-info
copying printtest.egg-info\dependency_links.txt -> printtest-1.0\printtest.egg-info
copying printtest.egg-info\top_level.txt -> printtest-1.0\printtest.egg-info
Writing printtest-1.0\setup.cfg
creating dist
Creating tar archive
removing 'printtest-1.0' (and everything under it)
```






```
\dist\printtest-1.0> python setup.py install               running install
running bdist_egg
running egg_info
writing printtest.egg-info\PKG-INFO
writing dependency_links to printtest.egg-info\dependency_links.txt
writing top-level names to printtest.egg-info\top_level.txt
reading manifest file 'printtest.egg-info\SOURCES.txt'
writing manifest file 'printtest.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_py
creating build
creating build\lib
copying printtest.py -> build\lib
creating build\bdist.win-amd64
creating build\bdist.win-amd64\egg
copying build\lib\printtest.py -> build\bdist.win-amd64\egg
byte-compiling build\bdist.win-amd64\egg\printtest.py to printtest.cpython-37.pyc
creating build\bdist.win-amd64\egg\EGG-INFO
copying printtest.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
copying printtest.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying printtest.egg-info\dependency_links.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying printtest.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist\printtest-1.0-py3.7.egg' and adding 'build\bdist.win-amd64\egg' to it
removing 'build\bdist.win-amd64\egg' (and everything under it)
Processing printtest-1.0-py3.7.egg
Copying printtest-1.0-py3.7.egg to c:\programdata\miniconda3\lib\site-packages
Adding printtest 1.0 to easy-install.pth file

Installed c:\programdata\miniconda3\lib\site-packages\printtest-1.0-py3.7.egg
Processing dependencies for printtest==1.0
Finished processing dependencies for printtest==1.0
```


安装后，会发现Lib/site-packages目录下存在printtest.py文件和printtest-1.0-py3.6.egg-info



```
import printtest
printtest.test()

```


## 4.2. 参考例子

### 4.2.1. setup.py 安装配置介绍

setup.py 主要使用setuptools的setup模块，提供打包所需要的基本信息。python依赖此脚本中的配置信息，将相关模块、静态文件，打包成一个完整的模块安装到site-packages文件。

基本示例：


```
|--smart
|  |--static
|  |  |--icon.svg
|  |  |--confg.json
|  |--engine
|  |  |--__init__.py
|  |  |--core.py
|  |--__init__.py
|  |--__version__.py
|  |--api.py
|  |--utils.py
|--tests
|  |--__init__.py
|--LICENSE
|--README.rst
|--setup.py
```

**zip_safe=False,  # 此项需要，否则卸载时报windows error**


```python
# 需要将那些包导入
packages = ["smart", "smart.engine"]

# 导入静态文件
file_data = [
    ("smart/static", ["smart/static/icon.svg", "smart/static/config.json"]),
]

# 第三方依赖
requires = [
    "pandas>=0.23.4"
]

# 自动读取version信息
about = {}
with open(os.path.join(here, 'smart', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

# 自动读取readme
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about["__title__"],  # 包名称
    version=about["__version__"],  # 包版本
    description=about["__description__"],  # 包详细描述
    long_description=readme,   # 长描述，通常是readme，打包到PiPy需要
    author=about["__author__"],  # 作者名称
    author_email=about["__author_email__"],  # 作者邮箱
    url=about["__url__"],   # 项目官网
    packages=packages,    # 项目需要的包
    data_files=file_data,   # 打包时需要打包的数据文件，如图片，配置文件等
    include_package_data=True,  # 是否需要导入静态数据文件
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3*",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[    # 程序的所属分类列表
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)

```

上面这个代码来自这个链接：https://www.jianshu.com/p/19f1e564a29d  


`setup()`需要几个参数。此示例包使用相对最小的集合：

-   `name`是软件包的*发行名称*。该名称可以是任何名称，只要仅包含字母，数字`_`和即可`-`。也一定不能在pypi.org上使用它。**请务必使用您的用户名进行更新，**因为这样可以确保您不会尝试上传与上载软件包时已经存在的相同名称的软件包。
    
-   `version` 软件包的版本见 [](https://www.python.org/dev/peps/pep-0440)有关版本的更多详细信息，请参见[ **PEP 440**](https://www.python.org/dev/peps/pep-0440)。
    
-   `author`并`author_email`用于标识软件包的作者。
    
-   `description` 是该软件包的简短，一句话摘要。
    
-   `long_description`是包装的详细说明。这在Python Package Index的package detail包中显示。在这种情况下，将载入详细描述，`README.md`这是常见的模式。
    
-   `long_description_content_type`告诉索引用于长描述的标记类型。在这种情况下，就是降价促销。
    
-   `url`是项目主页的URL。对于许多项目，这仅是指向GitHub，GitLab，Bitbucket或类似代码托管服务的链接。
    
-   `packages`是应该包含在[分发包](https://packaging.python.org/glossary/#term-distribution-package)中的所有Python [导入包](https://packaging.python.org/glossary/#term-import-package)的列表。无需手动列出每个软件包，我们可以 用来自动发现所有软件包和子软件包。在这种情况下，软件包列表将为example_pkg，因为这是唯一的软件包。[](https://packaging.python.org/glossary/#term-distribution-package)`find_packages()`
    
-   `classifiers`给出了指数和[点子](https://packaging.python.org/key_projects/#pip)你的包一些额外的元数据。在这种情况下，该软件包仅与Python 3兼容，已获得MIT许可证的许可，并且与操作系统无关。您应始终至少包括您的软件包所使用的Python版本，软件包所使用的许可证以及软件包所使用的操作系统。有关分类器的完整列表，请参见 [https://pypi.org/classifiers/](https://pypi.org/classifiers/)。
    

除了这里提到的以外，还有更多。有关更多详细信息，请参见 [打包和分发项目](https://packaging.python.org/guides/distributing-packages-using-setuptools/)。











这个例子是极简化后的setup.py

```
from setuptools import setup

setup(name='pagtest',
      version='1.0.0',
      description='A print test for PyPI',
      author='winycg',
      author_email='win@163.com',
      url='https://www.python.org/',
      license='MIT',
      keywords='ga nn',
      project_urls={
            'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
            'Funding': 'https://donate.pypi.org',
            'Source': 'https://github.com/pypa/sampleproject/',
            'Tracker': 'https://github.com/pypa/sampleproject/issues',
      },
      packages=['pagtest'],
      zip_safe=False,  # 此项需要，否则卸载时报windows error
      install_requires=['numpy>=1.14', 'tensorflow>=1.7'],
      python_requires='>=3'
     )
```


```
# name : 打包起来的包的文件名
# version : 版本号,添加为打包文件的后缀名
#author : 作者
#author_email : 作者的邮箱
#py_modules : 打包的.py文件
#packages: 打包的python文件夹
#include_package_data : 项目里会有一些非py文件,比如html和js等,这时候就要靠include_package_data 和 package_data 来指定了。package_data:一般写成{‘your_package_name’: [“files”]}, #include_package_data还没完,还需要修改MANIFEST.in文件.MANIFEST.in文件的语法为: include xxx/xxx/xxx/.ini/(所有以.ini结尾的文件,也可以直接指定文件名)
#license : 支持的开源协议
#description : 对项目简短的一个形容
#ext_modules : 是一个包含Extension实例的列表,Extension的定义也有一些参数。
#ext_package : 定义extension的相对路径
#requires : 定义依赖哪些模块
#provides : 定义可以为哪些模块提供依赖
#data_files :指定其他的一些文件(如配置文件),规定了哪些文件被安装到哪些目录中。如果目录名是相对路径,则是相对于sys.prefix或sys.exec_prefix的路径。如果没有提供模板,会被添加到MANIFEST文件中。
```

setup.py参数介绍




# 5. 更新Python包

修改setup.py中的版本号，然后直接上传即可

```
python3 setup.py sdist bdist_wheel
```




































































