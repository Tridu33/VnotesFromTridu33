# linux minisat 安装指南




https://blog.csdn.net/baoli1008/article/details/47030409



首先到http://www.minisat.se/MiniSat.html下载minisat-2.2.0.tar.gz这个安装包，并解压缩，可以看到压缩包中有一个README，其中就包含了安装方法：

1.进入解压缩后的文件夹

2.export MROOT=文件夹所在路径    //这句的意义是声明一个环境变量保存文件夹路径，下面的make命令会调用这个环境变量以完成安装

3.cd core 或 cd simp   //两个版本的minisat，通常用第一个，即执行cd core

4.make rs         //开始编译程序，按照文件夹中makefile的规定。makefile已写好无需改动。

5.cp minisat_static /usr/bin/minisat    //上一步make之后生成了一个名为minisat_static的可执行程序，将其拷入/usr/bin/minisat 中，使该程序在任意路径下都可执行。



minisat所需实验数据可以从http://www.cs.ubc.ca/~hoos/SATLIB/benchm.html下载，下载的数据文件需要将最后一行那个0删去才能正常调用。



如果要修改程序，可以直接在core或 simp中修改main文件，然后仍然按照那五步进行编译。








