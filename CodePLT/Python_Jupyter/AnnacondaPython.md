http://www.cnblogs.com/harvey888/p/5465452.html


conda info –envs
conda info -e
显示环境
https://blog.csdn.net/u011797832/article/details/82997386

```
# To activate this environment, use:
# > activate py3
#
# To deactivate an active environment, use:
# > deactivate
#
# * for power-users using bash, you must source

```



https://stackoverflow.com/questions/36000263/importerror-no-module-named-jupyter-client

给我的py3环境安装了


```
D:\JAVA_JupyterNotebook>activate py3

(py3) D:\JAVA_JupyterNotebook>python install.py
Installed java kernel into "C:\ProgramData\jupyter\kernels\java"

```

www.cnplugins.com/tool/howtosolvechromeblankpage.html

接着，使用 python3 install.py（也可以根据自己需要写参数），然后使用命令：

jupyter kernelspec list

获取已配置的kernel列表。

可以看到java已经在其中。


版本不支持

KernelRestarter: restarting kernel (4/5)
WARNING:root:kernel 3d7d4ba6-2eda-4b06-8d08-1d72edab8c39 restarted
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.UnsupportedClassVersionError: io/github/spencerpark/ijava/IJava has been compiled by a more recent version of the Java Runtime (class file version 53.0), this version of the Java Runtime only recognizes class file versions up to 52.0
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClass(Unknown Source)
        at java.security.SecureClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.access$100(Unknown Source)
        at java.net.URLClassLoader$1.run(Unknown Source)
        at java.net.URLClassLoader$1.run(Unknown Source)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
        at sun.misc.Launcher$AppClassLoader.loadClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
        at sun.launcher.LauncherHelper.checkAndLoadMain(Unknown Source)





















