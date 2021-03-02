# gitClone分支

git branch -a


如果 已经 clone了 master分支  


方法 1：  
那么 本地 git pull  
然后执行 git checkout -t origin/2.0.0  
这样就能下载 到远程分支



```
git branch -r #查看远程分支
或

git branch -a #查看所有分支
```

``` 
git branch -r
  origin/HEAD -> origin/master
  origin/gh-pages
  origin/master
```

然后

```
git checkout origin/gh-pages
```

如果尚未克隆，那么  
git clone -b gh-pages [https://github.xxxx.git](https://github.xxxx.git/)  
test 是分支名






---------------------------

git clone只能clone远程库的master分支，无法clone所有分支，解决办法如下：

1. 找一个干净目录，假设是git_work
2. cd git_work
3. git clone http://myrepo.xxx.com/project/.git ,这样在git_work目录下得到一个project子目录
4. cd project
5. git branch -a，列出所有分支名称如下：
remotes/origin/dev
remotes/origin/release
6. git checkout -b dev origin/dev，作用是checkout远程的dev分支，在本地起名为dev分支，并切换到本地的dev分支
7. git checkout -b release origin/release，作用参见上一步解释
8. git checkout dev，切换回dev分支，并开始开发。


[基本类似的经历 https://gaohaoyang.github.io/2016/07/07/git-clone-not-master-branch/](https://gaohaoyang.github.io/2016/07/07/git-clone-not-master-branch/)




[用gh-pages发博自己的静态项目 https://yq.aliyun.com/articles/694995](https://yq.aliyun.com/articles/694995)



















