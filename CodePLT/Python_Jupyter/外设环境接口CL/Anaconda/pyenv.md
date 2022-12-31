# pyenv




## pyenv

pyenv是一个管理各个python版本的管理器。可以在系统里同时保留多个python版本，等需要时定义需要的版本。

[项目地址](https://github.com/pyenv/pyenv)

#### 安装

看项目地址中的readme

#### 使用

```cpp
pyenv install --list

```

查看pyenv可安装的版本列表

```css
pyenv install anaconda2-4.2.0
pyenv uninstall x.x.x

```

安装和卸载指定版本，会将python版本安装在`$(pyenv root)/versions/`中

```undefined
pyenv versions

```

查看当前已经安装了的python版本。输出内容中，system关键字是系统python版本。 *表示当前环境所处的版本。

```csharp
pyenv global anaconda2

```

全局切换为anaconda科学计算环境(不建议这么做)，做了如果要恢复，则将最后一个参数改为--unset

```css
pyenv local python3.4.1

```

当前环境接环。在当前目录以下。如果要恢复，则将最后一个参数改为--unset
