# python路径










临时添加python搜索包路径的方法：

方法1：（先进入python）

import sys  
sys.path.append(‘路径’)  

（这种方式仅对当前python有效）

  

方法2：  
export PYTHONPATH=路径  
(这种方式对所有的python有效)

永久写入sys.path的方法：

方法1：

在已有的sys.path搜索路径下添加 .pth文件，文件内容格式为：
import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")

方法2：

在home文件夹下的.bash_profile文件中添加下面一行：

export PYTHONPATH=路径








方式一：

导入系统自带的sys模块，然后将文件的路径进行追加或者插入，如下：

import sys
sys.path.append(r'E:\\syz\\day5')
sys.path.insert(0,r'E:\\syz\\day5')

说明：

sys.path返回模块的搜索路径，append和insert方法，把一个python文件加入到python的环境变量中，这样我们就可以在其他python文件中调用这些加入到环境变量中python文件了






## 常用命令

自动重新加载更改的模块

```
%load_ext autoreload
%autoreload 2
```

启动和当前笔记本相同内核的 qtconsole：

```
%qtconsole
```

当前笔记本链接信息：

```
%connect_info
```

## Line magics

| 命令 | 详情 |
| --- | --- |
| `%alias` | 定义别名 |
| `%alias_magic` | 为现有的魔术命令创建别名 |
| `%autocall` |
| `%automagic` | 设置输入魔术命令时是否键入`%`前缀，`on(1)/off(0)` |
| `%bookmark` | 管理IPython的书签系统 |
| `%cd` | 更改当前工作目录 |
| `%colors` |
| `%config` |
| `%debug` |
| `%dhist` | 打印历史访问目录 |
| `%dirs` | 返回当前目录堆栈 |
| `%doctest_mode` |
| `%edit` |
| `%env` | 设置环境变量(无需重启) |
| `%gui` |
| `%history` |
| `%killbgscripts` |
| `%load` | 导入python文件 |
| `%load_ext` |
| `%loadpy` | `%load`别名 |
| `%logoff` | 临时停止logging |
| `%logon` | 重新开始logging |
| `%logstart` |
| `%logstate` |
| `%lsmagic` | 列出当前可用的魔术命令。 |
| `%macro` | 定义用来重复执行的宏 |
| `%magic` | 显示魔术命令的帮助 |
| `%matplotlib` | 设置matplotlib的工作方式 |
| `%notebook` |
| `%page` |
| `%pastebin` |
| `%pdb` | 控制pdb交互式调试器的自动调用 |

### 打印相关

| 命令 | 详情 |
| --- | --- |
| `%pdef` | 打印任何可调用对象信息 |
| `%pdoc` | 打印对象的`docstring` |
| `%pfile` |
| `%pinfo` |
| `%pinfo2` |
| `%pip` | 运行`pip`命令 |
| `%popd` |
| `%pprint` | 美化打印 |
| `%precision` | 设置美化打印时的浮点数精度 |
| `%profile` | 打印您当前活动的IPython配置文件 |
| `%prun` | 告诉你程序中每个函数消耗的时间 |
| `%psearch` |
| `%psource` | 打印对象源代码 |
| `%pushd` |
| `%pwd` | 返回当前工作路径 |
| `%pycat` |
| `%pylab` | 加载numpy、matplotlib |
| `%quickref` |
| `%recall` |
| `%rehashx` |

### 运行相关

| 命令 | 详情 |
| --- | --- |
| `%reload_ext` | 通过其模块名称重新加载IPython扩展 |
| `%rerun` |
| `%reset` |
| `%reset_selective` |
| `%run` |
| `%save` |
| `%sc` |
| `%set_env` | 设置环境变量 |
| `%sx` |
| `%system` |
| `%tb` |
| `%time` | 执行Python语句或表达式的时间 |
| `%timeit` |
| `%unalias` | 移别名 |
| `%unload_ext` | 通过其模块名称卸载IPython扩展 |
| `%who` | 列出全局变量 |
| `%who_ls` | 以排序列表的方式列出变量 |
| `%whos` | 类似`who`，但给出的信息更详细 |
| `%xdel` |
| `%xmode` |

### 详情

#### `%autocall`

#### `%automagic`

#### `%bookmark`

#### `%cd`

#### `%colors`

#### `%env`

#### `%history`

#### `%load`

```
%load myscript.py
%load 7-27
%load myMacro
%load http://www.example.com/myscript.py
%load -r 5-10 myscript.py
%load -r 10-20,30,40: foo.py
%load -s MyClass,wonder_function myscript.py
%load -n MyClass
```

#### `%alias`

```
In [2]: alias bracket echo "Input in brackets: <%l>"
In [3]: bracket hello world
Input in brackets: <hello world>
```

```
In [1]: alias parts echo first %s second %s
In [2]: %parts A B
first A second B
In [3]: %parts A
Incorrect number of arguments: 2 expected.
parts is an alias to: 'echo first %s second %s'
```

```
In [6]: alias show echo
In [7]: PATH='A Python string'
In [8]: show $PATH
A Python string
In [9]: show $$PATH
/usr/local/lf9560/bin:/usr/local/intel/compiler70/ia32/bin:...
```

#### `%who`、`%who_ls`、`%whos`

限制返回的变量类型为函数和字符串：

```
%who function str
```

```
In [1]: alpha = 123

In [2]: beta = 'test'

In [3]: %who
alpha   beta

In [4]: %who int
alpha

In [5]: %who str
beta
```

```
In [1]: alpha = 123

In [2]: beta = 'test'

In [3]: %who_ls
Out[3]: ['alpha', 'beta']

In [4]: %who_ls int
Out[4]: ['alpha']

In [5]: %who_ls str
Out[5]: ['beta']
```

```
In [1]: alpha = 123

In [2]: beta = 'test'

In [3]: %whos
Variable   Type        Data/Info

alpha      int         123
beta       str         test
```

## Cell magics

在 notebook 内用不同的内核运行代码

| 命令 | 详情 |
| --- | --- |
| `%%bash` |
| `%%capture` |
| `%%html` |
| `%%javascript` |
| `%%js` |
| `%%latex` |
| `%%markdown` |
| `%%perl` |
| `%%pypy` |
| `%%python` |
| `%%python2` |
| `%%python3` |
| `%%ruby` |
| `%%sh` |
| `%%svg` |
| `%%writefile` |


























