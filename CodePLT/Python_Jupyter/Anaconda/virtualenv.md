# virtualenv










本来这是一个单独的软件用来虚拟一个python版本环境，让每个工作环境都有一套独立的python各自的第三方插件互不影响。然而在 pyenv 下有一个插件 pyenv-virtualenv 他可以在 pyenv 的环境下担负起 virtualenv 的事情。（如果使用的是原生python可以用这个工具，如果用的是anaconda则不用这个，用下一章说的conda工具来完成虚拟环境）

[项目地址](https://github.com/pyenv/pyenv-virtualenv)

#### 安装

看项目地址中的readme

#### 使用

```css
pyenv virtualenv 2.7.1 env271

```

在当前目录下创建一个 python 版本为2.7.1的环境，环境名字为 env271。 这个环境的真实目录位于`~/.pyenv/versions/`

```undefined
pyenv activate env271

```

（创建时并不激活）激活当前环境。此时已经进入虚拟环境，在当前环境下所有pip等操作都不会影响系统环境和系统路径。

```undefined
pyenv deactivate

```

离开已激活的环境，切换回系统环境。但并没有被删除，下次依旧可以启动。

```undefined
pyenv uninstall env271

```

删除一个环境，当然也可以到真实目录下删除文件夹。






