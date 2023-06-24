
SPOJ, https://www.spoj.com/ranks/users/  
Timus Online Judge, https://acm.timus.ru/ https://acm.timus.ru/problemset.aspx
CodeChef, https://www.codechef.com/
Codeforces, https://codeforces.com/  https://codeforces.com/catalog
 HackerRank https://www.hackerrank.com/

都能用Haskell

**CodeWars**最好


CMU 15210 用 sml实现了图论的算法，动态规划，等 用sml写实验题

印象中实验内容涉及有最短路(Dijkstra),割边割点(Tarjan),分治,素性测试,高精度,撸ST表解决RMQ.
 
https://github.com/Misaka9468/sml-experiment 实验代码传送门，





# Haskell的OJ平台

如何使用 haskell 写出高效代码刷算法比赛题目？ - 肥猪千里冰封的回答 - 知乎
https://www.zhihu.com/question/27208859/answer/758590101


Google Code Jam https://buildyourfuture.withgoogle.com/events/code-jam/ 、Project Euler https://projecteuler.net/ 、Rosalind https://rosalind.info/about/  这样提交答案的可以本地用

金斌的 fancy-walks https://github.com/chaoxu/fancy-walks/tree/master/haskell.org/99_Problems

MaskRay/OJHaskell · GitHub https://github.com/MaskRay/OJHaskell


Haskell OJ https://wiki.haskell.org/SPOJ https://wiki.haskell.org/Online_judges



https://github.com/EveryTian/Haskell-Codewars



code wars题库
https://www.codewars.com/kata/latest/my-languages?beta=false

入门指导 https://acm.timus.ru/help.aspx?topic=haskell





# 本地搭建Haskell OJ代码管理仓库
## 单文件编译执行vscode脚本


https://zhuanlan.zhihu.com/p/399605960 
评论可以配置任何bash和cmd命令："

```json
command": "cd ${fileDirname} && stack runghc ${fileDirname}/${fileBasename}",
"args": [],
```

然后只要此项目你需要敲命令行的，都可以变成F5快捷键自动调用执行

## 多文件类库项目管理
stack一站式写lib多项目管理
https://blog.csdn.net/myRealization/article/details/118967134 ，就是Stackage镜像太慢




https://zhuanlan.zhihu.com/p/455688955?utm_id=0
2022 cabal又不是不能用，目前国内只有上海交大和中科大有 Haskell 工具链的完整镜像（GHCup、Hackage、Stackage）。


Window原生环境下ghci国内镜像还是一堆问题，投降了。最后还是用了2011过时的Haskell platform。主要图他exe离线安装，不会出现那些国内镜像源安装失败的问题。我是为了编程才下的环境，不是为了成为“环境配置大师”。

```cmd

(base) C:\FPds\LeetCodeWars>cabal --version
cabal-install version 2.4.1.0
compiled using version 2.4.1.0 of the Cabal library 

(base) C:\FPds\LeetCodeWars>ghci --version
The Glorious Glasgow Haskell Compilation System, version 8.6.5

(base) C:\FPds\LeetCodeWars>stack --version
Version 1.9.3, Git revision 40cf7b37526b86d1676da82167ea8758a854953b (6211 commits) x86_64 hpack-0.31.1

(base) C:\FPds\LeetCodeWars>where stack 
C:\Users\AppData\Roaming\local\bin\stack.exe

(base) C:\FPds\LeetCodeWars>where cabal
C:\Program Files\Haskell Platform\8.6.5\lib\extralibs\bin\cabal.exe

(base) C:\FPds\LeetCodeWars>where ghci
C:\Program Files\Haskell Platform\8.6.5\bin\ghci.exe

```

WSL2当然可以追新

# IO
https://www.cnblogs.com/youxin/p/3765432.html
Haskell 输入和输出

codewars那样写好io最好

https://www.jianshu.com/p/2bfeceb3f569 Haskell命令行软件希望读取参数，最好用模板，用包



































