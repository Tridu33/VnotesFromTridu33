# JLU_PrimaryOR_JLU_operational research


已经做到什么程度了呢？



https://github.com/tanmoyie/Operations-Research

About
Some lecture notes of Operations Research (usually taught in Junior year of BS) can be found in this repository along with some Python programming codes to solve numerous problems of Optimization including Travelling Salesman, Minimum Spanning Tree and so on.

[www.youtube.com/playlist?lis](https://www.youtube.com/playlist?list=PLHyZ7Tamw-fevmrx2V3U13hPDDlUSBbi7)


```
setup(name='src',
      version='1.0.0',
      description='Primary Operational Research',
      author='tridu33',
      author_email='tridu33@qq.com',
      url='https://github.com/Tridu33/Primary_OR',
      license='GPL-3.0',
      project_urls={
            'Documentation': 'https://github.com/Tridu33/Primary_OR/wiki',
            'Source': 'https://github.com/Tridu33/Primary_OR',
            'Tracker': 'https://github.com/Tridu33/Primary_OR/issues',
      },
      packages=['src'],
      install_requires=['numpy>=1.14',''],
      python_requires='>=3'
     )
```









那我就接着整起来吧，毕竟本来就是想写面向教程的Package,已经有人先整了些，太好了，接力棒

```
pip install *.whl
```

then 


```
pip unintall PrimaryOR
```

```
    c:\programdata\miniconda3\lib\site-packages\dualplanning\*
    c:\programdata\miniconda3\lib\site-packages\dynamicprogramming\*
    c:\programdata\miniconda3\lib\site-packages\graphandnetwork\*
    c:\programdata\miniconda3\lib\site-packages\integerprogramming\*
    c:\programdata\miniconda3\lib\site-packages\linearplanning\*
    c:\programdata\miniconda3\lib\site-packages\primaryor-1.0.0.dist-info\*
    c:\programdata\miniconda3\lib\site-packages\primaryor\*
    c:\programdata\miniconda3\lib\site-packages\transportationproblem\*
    c:\programdata\miniconda3\my_data\data_file
    c:\programdata\miniconda3\scripts\primaryorconsole.exe
```



测试一下：

```
In [1]: import  primaryOR.addone as tmp
In [2]: tmp.add_one(5)
Out[2]: 6
```

```
In [1]: from primaryOR.cutting_plane_algorithm import cutting_plane_algorithm
In [2]: cutting_plane_algorithm(9)
BranchAndBoundAlgorithm
Out[2]: 1
```

```
In [3]: import primaryOR.cutting_plane_algorithm as tmp
In [4]: tmp.cutting_plane_algorithm(2)
BranchAndBoundAlgorithm
Out[4]: 1
```




```
python setup.py sdist bdist_wheel
cd dist
pip install primaryOR-1.0.0-py3-none-any.whl
pip uninstall primaryOR

```

















