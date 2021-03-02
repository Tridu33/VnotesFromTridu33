




# Hugo+gitee+vnote

Hugo+Gitee 搭建个人博客 - 哈哈的文章 - 知乎
https://zhuanlan.zhihu.com/p/184625753


https://blog.csdn.net/qq_34688164/article/details/104615706 



进入Hugo  https://themes.gohugo.io/ 主题页面，找到需要的主题。 将主题克隆到 themes 目录。


```
git clone https://github.com/dillonzq/LoveIt.git themes/LoveIt

```



在配置完成后，若想在本地访问搭建的站点，只需要运行：```hugo server ```命令，接着在浏览器访问 ```http://localhost:1313 ```即可。后续在自定义样式，或者编写博客时，可以通过访问该地址，进行实时预览。


5. 编写博客
在网站框架根目录内，使用 hugo new posts/blog_name.md 命令创建博客。使用MarkDown语法编辑博客内容。

6. 打包构建
在网站框架根目录下，使用 hugo 命令打包构建。运行该命令后，会生成一个 public 目录, 目录内包含了网站的所有静态内容和资源。






7. 在Gitee上建立仓库，上传资源包
7.1 申请Gitee账号。
7.2 在Gitee上建立仓库。
根据在Gitee里的Gitee Pages 静态页面托管说明,仓库名最好与个人空间地址一致，例如我个人空间地址为JihahaCabin，我建立的仓库名也为JihahaCabin。

如果你想你的 pages 首页访问地址不带二级目录，如http://ipvb.gitee.io，你需要建立一个与自己个性地址同名的仓库，如 https://gitee.com/ipvb 这个用户，想要创建一个自己的站点，但不想以子目录的方式访问，想以ipvb.gitee.io直接访问，那么他就可以创建一个名字为ipvb的仓库 https://gitee.com/ipvb/ipvb 部署完成后，就可以以 https://ipvb.gitee.io 进行访问了。

7.3 在public目录下，运行以下命令，将public目录下所有文件，上传到Gitee仓库。${git_address} 表示在上一步建立的仓库地址。

```
git init 
git add . 
git commit -m "init" 
git remote add origin ${git_address}  
git push -f origin master
```
8. 配置Gitee Pages
8.1 登录Gitee，找到上传的仓库，点击"服务"下拉框，点击"Gitee Pages"选项。



8.2 选择部署分支，点击"启动"按钮。















































