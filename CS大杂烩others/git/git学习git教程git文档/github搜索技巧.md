[TOC]



这个技能超级恐怖有用，github是一款软件发展最好的温床。

commit跟踪，issues追溯，生态还原，code学习，github搜索LaggedStartMap等等manim来学习旧的3b1b中的例子来学习。


https://learngitbranching.js.org/




# github搜索技巧


[Sox在Windows下的安装以及Sox在python中的安装https://blog.csdn.net/weixin_43216017/article/details/88531363](https://blog.csdn.net/weixin_43216017/article/details/88531363)





(1). 基本搜索(Basic search)：

A．查找stars数超过100的”cat”仓库：cat stars:>100

B．搜索用户名为fengbingchun的所有仓库：user:fengbingchun

搜索结果如下图所示，左上侧显示fengbingchun有多少个仓库(Repositories)、Issues数等信息，想查看特定信息可以进一步点击；左下侧显示仓库中包含哪些开发语言，如C++、C、Python等，也可点击对应的只查看指定语言的仓库；右上侧显示这些仓库按哪种方式进行排序，包括最多stars数、最多fork数、按最近更新日期等。









C. 搜索地址在” San Francisco, CA”的用户名包含tom的所有仓库：tom location:"San Francisco, CA"

D. 搜索不包含”cat”的所有仓库：NOT cat

(2). 仓库搜索(Repository search)：

A. 查找stars数超过100的”cat”仓库：cat stars:>100

B. 搜索用户名为fengbingchun的所有仓库：user:fengbingchun

C. 搜索名为”node.js”并fork数少于200的所有仓库：node.js forks:<200

D. 搜索名为”jquery”并库大小在1024至4089KB之间的所有仓库：jquery size:1024..4089

E. 搜索用户名为fengbingchun并且开发语言为C++的所有仓库：language:c++ user:fengbingchun

F. 搜索用户名为fengbingchun并且stars数大于等于10的所有仓库：user:fengbingchun followers:>=10

G. 搜索开发语言为C++且stars数大于10000的所有仓库：language:c++ stars:>10000

H. 搜索用户名为fengbingchun并且仓库在2019年1月1日后有更新的所有仓库：user:fengbingchun pushed:>2019-01-01

(3). 代码搜索(Code search)：

A. 搜索用户名为fengbingchun并且文件中含有”cv::Mat”的所有文件：cv::Mat user:fengbingchun

B. 搜索文件大小大于1000KB并文件中包含”system”的所有文件：system size:>1000

C. 搜索在/docs/路径下文件中含有”examples”的所有文件：examples path:/docs/

(4). (问题搜索)Issue search：

A. 搜索用户名为fengbingchun并issue中含有”opencv”字段的所有issues：opencv user:fengbingchun

B. 搜索issue是open状态并且issue中含有”fengbingchun”字段的所有issues：fengbingchun is:open

C. 搜素issue中comments数大于4次且含有”fengbingchun”字段的所有issues：fengbingchun comments:>4

D. 搜索issue创建者是fengbingchun的所有issues：author:fengbingchun

E. 搜索issue在2019年2月15日后创建的且含有”opencv”字段的所有issues：opencv created:>2019-03-15

(5). 用户名搜索(User search)：

A. 搜索用户全名为”Bingchun Feng”的用户：fullname:"Bingchun Feng"

B. 搜索地址在” San Francisco, CA”的用户名包含tom的所有仓库：tom location:"San Francisco, CA"

(6). 高级搜索(Advanced search)：说明见https://github.com/search/advanced

注意：

(1). 冒号两侧不能有空格；

(2). 不区分大小写；

(3). 不能将以下通配符用作搜索查询的一部分，搜索将忽略这些符号：. , : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } [ ]；

(4). 搜索默认为master分支。

2. 进入到某个项目的主页后，你会发现有Watch、Star、 Fork、Issues、Pull requests等按钮选项，如下图所示


Watch：默认是处于Not watching的状态即未关注，当选择Watching后，表示你以后会关注这个项目的所有状态，以后只要这个项目发生变动，如被别人提交了Pull requests、别人发起了新的Issue、或Issue中有新的讨论等等情况，你都会在自己的个人通知中心，收到一条通知，如果你设置了个人邮箱，那么你的邮箱也可能收到响应的邮件。你也可以选择Release only，只有当此项目有新的发布版本或参与某个Issue讨论，或被别人@时你才会收到通知；选择Ignoring，则不会收到任何通知；选择Not watching，只有当参与此项目时，如参与某个Issue，Pull requests或commit的讨论，或被别人@后，才会收到相关通知。

Star：点击Star表示你喜欢这个项目。你可以通过点击个人GitHub主页上的Stars按钮来查看自己star过哪些项目。

Fork：如果你点击了Fork，相当于你自己有了一份原项目的拷贝，即复制原项目到自己的GitHub仓库中，你可以基于此做调整、修改，但是如果后续原项目发生了改变，你必须通过其它的方式去同步。

Issues：如果你对此项目有任何疑问或问题，都可以通过创建新issue方式提出。

Pull requests：如果你对原项目进行了bug fix或增加了新功能，都可以通过创建新pull request方式提交。

3. GitHub Trending页面：https://github.com/trending ，此页面可查看每天或每周或每月最热门的开发项目(Repositories)或开发者(Developers)，也可按开发语言过滤选择，如下图所示：

4. GitHub Topics页面：https://github.com/topics ，此页面显示最新和最流行的讨论主题，如下图所示：



5. GitHub插件：如Octotree、OctoLinker、Sourcegraph

 
















