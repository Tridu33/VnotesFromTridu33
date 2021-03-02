# sty+cls文件

是什么？https://www.jianshu.com/p/12b4a4b3afce




https://www.ctan.org/pkg/


 [CTAN](https://ctan.org/)




https://www.cnblogs.com/sukai/articles/3921759.html










方案一
    这是很简单的方案：

在计算机程序中找到：MikTex Console
选择Packages
在搜索栏中输入自己缺少的包名
右键，Install Packages
    这样就可以解决了，但有的时候，MiKTex会卡顿出问题，Whatever什么原因，那就用方案二吧

 

方案二
    访问https://www.ctan.org/tex-archive/macros/latex/contrib/
搜索缺少的安装包名，如appendix，下载到本地
一般是zip文件，解压，里面有Ins文件
cmd进入解压后的文件，并执行命令：latex appendix.ins，会生成相对应的appendix.sty文件
将整个文件拷贝到latex安装目录下“\MiKTex2.9\tex\latex”
win+R召唤cmd，执行texhash刷新Tex文件数据库即可
 










