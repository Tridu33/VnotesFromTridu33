# 1. how在github找项目

怎么在 GitHub 上找到自己喜欢的项目？ - GitHub Daily的回答 - 知乎
https://www.zhihu.com/question/20084458/answer/585375525




**代码搜索网站：**

1.  代码：  
    [GitHub](https://github.com/search)  
    [Codase](http://www.codase.com/)  
    [Ohloh](http://code.ohloh.net/)  
    [krugle](http://www.krugle.com/)  
    [Merobase Component Finder](http://www.merobase.com/)  
    [Google Code Archive](https://code.google.com/archive/)
2.  [SymbolHound](http://symbolhound.com/)  
    可以搜索特殊符号的搜索引擎，程序员的福音，遇到 Bash、正则之类的问题时候的利器！
3.  [Hoogle](http://www.haskell.org/hoogle/)  
    Haskell 的专用函数搜索引擎，妈妈再也不用担心我的 Functional Programming
4.  [RSeek.org R-project Search Engine](http://rseek.org/)  
    R 语言专用搜索。
5.  [findjar.com](http://www.findjar.com/)  
    JAR 搜索引擎，对 Java 编程有帮助。
6.  [Microsoft Research](http://research.microsoft.com/en-us/default.aspx)  
    微软内部搜索，好东西多多，经常会发现 Google 学术搜不到的技术文献
7.  针对 SEO 排名的知识搜索引擎：[SEO优化网](http://www.skyh.cn/)，完全在线学习 \+ 公式化结构化的 SEO 搜索算法
8.  [CA App Synthetic Monitor网站监控服务](https://asm.ca.com/zh_cn/ping.php)  
    从世界各地查询网站的 Ping 结果。

**Github代码搜索技巧：**

很多人搜索github，但是芸芸众生，要找到自己想要的项目犹如海底捞针一般，今天教大家几项神技，可以快速找到自己想要的内容。

1、按star数目搜索，比如[JavaScript](http://lib.csdn.net/base/18)，要求星数，这样就能获取star数目最多的项目

![](https://img-blog.csdn.net/20160518121352135?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

2、follow一些github上面的大牛

请登录：https://github-ranking.com/

国内大牛：http://outofmemory.cn/github/

这里是搜索名人的网址：https://github.com/search

高级搜索：https://github.com/search/advanced

3、Awesome + 你的关键字：搜索一些优秀的框架、教程、项目等

![](https://img-blog.csdn.net/20160518121402338?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

4、看一些搜索技巧，设定条件进行搜索

地址：https://help.github.com/articles/searching-repositories/

5、通过readme看看人家是否发出pull request

看看这篇文章：http://blog.csdn.net/qianlong4526888/article/details/11529981

6、看explore推荐

https://github.com/explore

7、看看其他

http://blog.sina.com.cn/s/blog_4e60b09d0102vcso.html

8、直接github上搜fackbook或者其他，可以看到他们的最新作品

github是一个非常丰富的资源，但是面对这丰富的资源很多人不知到怎么使用，更谈不上怎么贡献给他，我们需要使用github就要学习使用他的方法，学会了使用的方法，接受了他的这种观点我们才会慢慢的给他贡献自己的力量，这是我自己在学习的时候的一个笔记。现在分享给大家希望能够对一些人有帮助。

[Search](https://help.github.com/categories/search) / Searching code

github搜索之代码搜索

## 1.1. Searching code

代码搜索

To search for code, use the following search qualifiers in any combination.

**Tip:** There's a list of [search syntaxes](https://help.github.com/articles/search-syntax) you can add to any search qualifier to further improve your results.

### 1.1.1. Considerations for code search

Due to the complexity of searching code, there are a few restrictions on how searches are performed:

-   Only the default branch is considered. In most cases, this will be the `master` branch.
-   Only files smaller than 384 KB are searchable.
-   You must always include at least one search term when searching source code. For example, searching for [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language:go&type=Code) is not valid, while [`amazinglanguage:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language:go&type=Code) is.
-   At most, search results can show two fragments from the same file, but there may be more results within the file.
-   You can't use the following wildcard characters as part of your search query:``., : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } []``. The search will simply ignore these symbols.

以上是代码搜索中需要注意的一些问题

默认搜索是从master分支搜索代码

只有小于384k的代码才是可以搜索到的

搜索的时候必须包含至少一个搜索关键词 [`如amazing language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language:go&type=Code)

搜索语句不能有特殊字符如``., : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } []``.

### 1.1.2. Scope the search fields

指定搜索方式

[octocat in:file](https://github.com/search?q=octocat+in:file&type=Code)

Matches code where "octocat" appears in the file contents.

搜索文件中有octocat的代码

[octocat in:path](https://github.com/search?q=octocat+in:path&type=Code)

Matches code where "octocat" appears in the path name.

搜索路径中有octocat的代码

[octocat in:file,path](https://github.com/search?q=octocat+in:file,path&type=Code)

Matches code where "octocat" appears in the file contents or the path name.

搜索路径中有octocat的代码或者文件中有octocat的代码

[display language:scss](https://github.com/search?q=display+language:scss&type=Code)

Matches code with the word "display," that's marked as being SCSS.

搜索用scss写的包含display的代码

[Integer](https://github.com/search?q=Integer&type=Code)

Matches code with the word "Integer".

搜索包含Integer的字段

### 1.1.3. Search by language

通过语言搜索代码

You can search for code based on what language it's written in. For example:

[element language:xml size:100](https://github.com/search?q=element+language:xml+size:100&type=Code)

Matches code with the word "element" that's marked as being XML and has exactly 100 bytes.

搜索大小为100字节的xml代码

[user:mozilla language:markdown](https://github.com/search?q=user:mozilla+language:markdown&type=Code)

Matches code from all @mozilla's repositories that's marked as Markdown.

搜索mozilla用户下用markdown写的代码

### 1.1.4. Search by the number of forks the parent repository has

通过fork的数量或者是否有父节点的方式搜索

If you would like forked results to appear, add the **fork:true** qualifier. For example:

[android language:java fork:true](https://github.com/search?q=android+language:java+fork:true&type=Code)

Matches code in a forked repository with the word "android" that's written in Java.

搜索用java写的 android相关的代码并且被fork过

The **size** qualifier filters results based on the size of the file in which the code is found. For example:

[function size:>10000 language:python](https://github.com/search?q=function+size:%3E10000+language:python&type=Code)

Matches code with the word "function," written in Python, in files that are larger than 10 KB.

搜索与function相关的python代码，文件大小超过10kb

### 1.1.5. Search by the location of a file within the repository

按照目录结构搜索

By including the **path** qualifier, you specify that resulting source code must appear at a specific location in a repository. Subfolders are considered during the search, so be as specific as possible. For example:

[console path:app/public language:javascript](https://github.com/search?q=console+path:)

Finds JavaScript files with the word "console" in an app/public directory (even if they reside inapp/public/js/form-validators).

在app/public directory目录下搜索console关键字

[form path:cgi-bin language:perl](https://github.com/search?q=form+path:cgi-bin+language:perl&type=Code)

Finds Perl files under cgi-bin with the word "form" in them.

搜索cgi-bin目录下包含form的perl代码

### 1.1.6. Search by filename

通过文件名搜索

You can use the **filename** qualifier if there's a specific file you're looking for. For example:

[filename:.vimrc commands](https://github.com/search?q=filename:.vimrc+commands&type=Code)

Finds *.vimrc* files with the word "commands" in them.

搜索 文件名匹配*.vimrc* 并且包含commands的代码

[minitest filename:test_helper path:test language:ruby](https://github.com/search?q=minitest+filename:test_helper+path:test+language:ruby&type=Code)

Finds Ruby files containing the word "minitest" named \*test_helper\* within the \*test\* directory.

在test目录中搜索包含minitest且文件名匹配"\*test_helper\*"的代码

### 1.1.7. Search by the file extension

根据扩展名来搜索代码

The **extension** qualifier matches code files with a certain extension. For example:

[form path:cgi-bin extension:pm](https://github.com/search?q=form+path:cgi-bin+extension:pm&type=Code)

Matches code with the word "form," under cgi-bin, with the .pm extension.

搜索cgi-bin目录下以pm为扩展名的代码

[icon size:>200000 extension:css](https://github.com/search?q=icon+size:%3E200000+extension:css&type=Code)

Finds files larger than 200 KB that end in .css and have the word "icon" in them.

搜索超过200kb包含icon的css代码

### 1.1.8. Search within a user's or organization's repositories

通过用户或者组织来查找

To grab a list of code from all repositories owned by a certain user or organization, you can use the **user**syntax. For getting a list of code from a specific repository, you can use the **repo** syntax. For example:

[user:github extension:rb](https://github.com/search?q=user:github+extension:rb&type=Code)

推荐项目：

-   [free-programming-books](https://github.com/vhf/free-programming-books)

这个项目目前 star 数排名 GitHub 第三，总 star 数超过6w，这个项目整理了所有跟编程相关的免费书籍，而且全球多国语言版的都有，中文版的在这里：[free-programming-books-zh](https://github.com/vhf/free-programming-books/blob/master/free-programming-books-zh.md)，有了这个项目，理论上你可以获取任何编程相关的学习资料，强烈推荐给你们！

-   [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

俗话说，不会用 shell 的程序员不是真正的程序员，所以建议每个程序员都懂点 shell，有用不说，装逼利器啊！而 oh-my-zsh 毫无疑问就是目前最流行，最酷炫的 shell，不多说了，懂得自然懂，不懂的以后你们会懂的！

-   [awesome](https://github.com/sindresorhus/awesome)

GitHub 上有各种 awesome 系列，简单来说就是这个系列搜罗整理了 GitHub 上各领域的资源大汇总，比如有 awesome-android, awesome-ios, awesome-java, awesome-[Python](http://lib.csdn.net/base/11) 等等。

-   [github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet/)

GitHub 的使用有各种技巧，只不过基本的就够我们用了，但是如果你对 GitHub 超级感兴趣，想更多的了解 GitHub 的使用技巧，那么这个项目就刚好是你需要的，每个 GitHub 粉都应该知道这个项目。


**代码搜索网站：**

1.  代码：  
    [GitHub](https://github.com/search)  
    [Codase](http://www.codase.com/)  
    [Ohloh](http://code.ohloh.net/)  
    [krugle](http://www.krugle.com/)  
    [Merobase Component Finder](http://www.merobase.com/)  
    [Google Code Archive](https://code.google.com/archive/)
2.  [SymbolHound](http://symbolhound.com/)  
    可以搜索特殊符号的搜索引擎，程序员的福音，遇到 Bash、正则之类的问题时候的利器！
3.  [Hoogle](http://www.haskell.org/hoogle/)  
    Haskell 的专用函数搜索引擎，妈妈再也不用担心我的 Functional Programming
4.  [RSeek.org R-project Search Engine](http://rseek.org/)  
    R 语言专用搜索。
5.  [findjar.com](http://www.findjar.com/)  
    JAR 搜索引擎，对 Java 编程有帮助。
6.  [Microsoft Research](http://research.microsoft.com/en-us/default.aspx)  
    微软内部搜索，好东西多多，经常会发现 Google 学术搜不到的技术文献
7.  针对 SEO 排名的知识搜索引擎：[SEO优化网](http://www.skyh.cn/)，完全在线学习 \+ 公式化结构化的 SEO 搜索算法
8.  [CA App Synthetic Monitor网站监控服务](https://asm.ca.com/zh_cn/ping.php)  
    从世界各地查询网站的 Ping 结果。

**Github代码搜索技巧：**

很多人搜索github，但是芸芸众生，要找到自己想要的项目犹如海底捞针一般，今天教大家几项神技，可以快速找到自己想要的内容。

1、按star数目搜索，比如[JavaScript](http://lib.csdn.net/base/18)，要求星数，这样就能获取star数目最多的项目

![](https://img-blog.csdn.net/20160518121352135?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

2、follow一些github上面的大牛

请登录：https://github-ranking.com/

国内大牛：http://outofmemory.cn/github/

这里是搜索名人的网址：https://github.com/search

高级搜索：https://github.com/search/advanced

3、Awesome + 你的关键字：搜索一些优秀的框架、教程、项目等

![](https://img-blog.csdn.net/20160518121402338?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

4、看一些搜索技巧，设定条件进行搜索

地址：https://help.github.com/articles/searching-repositories/

5、通过readme看看人家是否发出pull request

看看这篇文章：http://blog.csdn.net/qianlong4526888/article/details/11529981

6、看explore推荐

https://github.com/explore

7、看看其他

http://blog.sina.com.cn/s/blog_4e60b09d0102vcso.html

8、直接github上搜fackbook或者其他，可以看到他们的最新作品

github是一个非常丰富的资源，但是面对这丰富的资源很多人不知到怎么使用，更谈不上怎么贡献给他，我们需要使用github就要学习使用他的方法，学会了使用的方法，接受了他的这种观点我们才会慢慢的给他贡献自己的力量，这是我自己在学习的时候的一个笔记。现在分享给大家希望能够对一些人有帮助。

[Search](https://help.github.com/categories/search) / Searching code

github搜索之代码搜索

## 1.2. Searching code

代码搜索

To search for code, use the following search qualifiers in any combination.

**Tip:** There's a list of [search syntaxes](https://help.github.com/articles/search-syntax) you can add to any search qualifier to further improve your results.

### 1.2.1. Considerations for code search

Due to the complexity of searching code, there are a few restrictions on how searches are performed:

-   Only the default branch is considered. In most cases, this will be the `master` branch.
-   Only files smaller than 384 KB are searchable.
-   You must always include at least one search term when searching source code. For example, searching for [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language:go&type=Code) is not valid, while [`amazinglanguage:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language:go&type=Code) is.
-   At most, search results can show two fragments from the same file, but there may be more results within the file.
-   You can't use the following wildcard characters as part of your search query:``., : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } []``. The search will simply ignore these symbols.

以上是代码搜索中需要注意的一些问题

默认搜索是从master分支搜索代码

只有小于384k的代码才是可以搜索到的

搜索的时候必须包含至少一个搜索关键词 [`如amazing language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language:go&type=Code)

搜索语句不能有特殊字符如``., : ; / \ ` ' " = * ! ? # $ & + ^ | ~ < > ( ) { } []``.

### 1.2.2. Scope the search fields

指定搜索方式

[octocat in:file](https://github.com/search?q=octocat+in:file&type=Code)

Matches code where "octocat" appears in the file contents.

搜索文件中有octocat的代码

[octocat in:path](https://github.com/search?q=octocat+in:path&type=Code)

Matches code where "octocat" appears in the path name.

搜索路径中有octocat的代码

[octocat in:file,path](https://github.com/search?q=octocat+in:file,path&type=Code)

Matches code where "octocat" appears in the file contents or the path name.

搜索路径中有octocat的代码或者文件中有octocat的代码

[display language:scss](https://github.com/search?q=display+language:scss&type=Code)

Matches code with the word "display," that's marked as being SCSS.

搜索用scss写的包含display的代码

[Integer](https://github.com/search?q=Integer&type=Code)

Matches code with the word "Integer".

搜索包含Integer的字段

### 1.2.3. Search by language

通过语言搜索代码

You can search for code based on what language it's written in. For example:

[element language:xml size:100](https://github.com/search?q=element+language:xml+size:100&type=Code)

Matches code with the word "element" that's marked as being XML and has exactly 100 bytes.

搜索大小为100字节的xml代码

[user:mozilla language:markdown](https://github.com/search?q=user:mozilla+language:markdown&type=Code)

Matches code from all @mozilla's repositories that's marked as Markdown.

搜索mozilla用户下用markdown写的代码

### 1.2.4. Search by the number of forks the parent repository has

通过fork的数量或者是否有父节点的方式搜索

If you would like forked results to appear, add the **fork:true** qualifier. For example:

[android language:java fork:true](https://github.com/search?q=android+language:java+fork:true&type=Code)

Matches code in a forked repository with the word "android" that's written in Java.

搜索用java写的 android相关的代码并且被fork过

The **size** qualifier filters results based on the size of the file in which the code is found. For example:

[function size:>10000 language:python](https://github.com/search?q=function+size:%3E10000+language:python&type=Code)

Matches code with the word "function," written in Python, in files that are larger than 10 KB.

搜索与function相关的python代码，文件大小超过10kb

### 1.2.5. Search by the location of a file within the repository

按照目录结构搜索

By including the **path** qualifier, you specify that resulting source code must appear at a specific location in a repository. Subfolders are considered during the search, so be as specific as possible. For example:

[console path:app/public language:javascript](https://github.com/search?q=console+path:)

Finds JavaScript files with the word "console" in an app/public directory (even if they reside inapp/public/js/form-validators).

在app/public directory目录下搜索console关键字

[form path:cgi-bin language:perl](https://github.com/search?q=form+path:cgi-bin+language:perl&type=Code)

Finds Perl files under cgi-bin with the word "form" in them.

搜索cgi-bin目录下包含form的perl代码

### 1.2.6. Search by filename

通过文件名搜索

You can use the **filename** qualifier if there's a specific file you're looking for. For example:

[filename:.vimrc commands](https://github.com/search?q=filename:.vimrc+commands&type=Code)

Finds *.vimrc* files with the word "commands" in them.

搜索 文件名匹配*.vimrc* 并且包含commands的代码

[minitest filename:test_helper path:test language:ruby](https://github.com/search?q=minitest+filename:test_helper+path:test+language:ruby&type=Code)

Finds Ruby files containing the word "minitest" named \*test_helper\* within the \*test\* directory.

在test目录中搜索包含minitest且文件名匹配"\*test_helper\*"的代码

### 1.2.7. Search by the file extension

根据扩展名来搜索代码

The **extension** qualifier matches code files with a certain extension. For example:

[form path:cgi-bin extension:pm](https://github.com/search?q=form+path:cgi-bin+extension:pm&type=Code)

Matches code with the word "form," under cgi-bin, with the .pm extension.

搜索cgi-bin目录下以pm为扩展名的代码

[icon size:>200000 extension:css](https://github.com/search?q=icon+size:%3E200000+extension:css&type=Code)

Finds files larger than 200 KB that end in .css and have the word "icon" in them.

搜索超过200kb包含icon的css代码

### 1.2.8. Search within a user's or organization's repositories

通过用户或者组织来查找

To grab a list of code from all repositories owned by a certain user or organization, you can use the **user**syntax. For getting a list of code from a specific repository, you can use the **repo** syntax. For example:

[user:github extension:rb](https://github.com/search?q=user:github+extension:rb&type=Code)

推荐项目：

-   [free-programming-books](https://github.com/vhf/free-programming-books)

这个项目目前 star 数排名 GitHub 第三，总 star 数超过6w，这个项目整理了所有跟编程相关的免费书籍，而且全球多国语言版的都有，中文版的在这里：[free-programming-books-zh](https://github.com/vhf/free-programming-books/blob/master/free-programming-books-zh.md)，有了这个项目，理论上你可以获取任何编程相关的学习资料，强烈推荐给你们！

-   [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

俗话说，不会用 shell 的程序员不是真正的程序员，所以建议每个程序员都懂点 shell，有用不说，装逼利器啊！而 oh-my-zsh 毫无疑问就是目前最流行，最酷炫的 shell，不多说了，懂得自然懂，不懂的以后你们会懂的！

-   [awesome](https://github.com/sindresorhus/awesome)

GitHub 上有各种 awesome 系列，简单来说就是这个系列搜罗整理了 GitHub 上各领域的资源大汇总，比如有 awesome-android, awesome-ios, awesome-java, awesome-[Python](http://lib.csdn.net/base/11) 等等。

-   [github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet/)

GitHub 的使用有各种技巧，只不过基本的就够我们用了，但是如果你对 GitHub 超级感兴趣，想更多的了解 GitHub 的使用技巧，那么这个项目就刚好是你需要的，每个 GitHub 粉都应该知道这个项目。


















