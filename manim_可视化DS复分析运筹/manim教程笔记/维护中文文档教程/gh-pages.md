




[TOC]



# 1. 提交
master

```
git add .
git commit -m "my comments"
git push
```

gh pages

```
git add .
git commit -m "comments"
第一次 git branch --set-upstream origin gh-pages
第二次直接 git push
```


# 2. gh-pages




```
git subtree push --prefix=dist origin gh-pages
```

https://gist.github.com/cobyism/4730490
dist文件夹作为子目录发布文档










我看的是这个，使用的也是这个方法：

[纯代码 巧用gh-pages分支发布自己的静态项目 https://yq.aliyun.com/articles/694995](https://yq.aliyun.com/articles/694995)


这是其中一部分


[git点选 https://www.cnblogs.com/MuYunyun/p/6082359.html](https://www.cnblogs.com/MuYunyun/p/6082359.html)



这个没看过 [使用Github的gh-pages分支展示一个页面](https://www.cnblogs.com/dear_diary/p/6555011.html)









































# 3. git理论相关

[master分支与其他分支https://www.jianshu.com/p/5140bd5979f8](https://www.jianshu.com/p/5140bd5979f8)


[HEAD、master 与 branchhttps://www.jianshu.com/p/4219b6f62ce3](https://www.jianshu.com/p/4219b6f62ce3)









































































































































