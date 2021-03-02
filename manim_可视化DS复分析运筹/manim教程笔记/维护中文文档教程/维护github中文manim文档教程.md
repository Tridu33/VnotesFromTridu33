# 维护中文文档教程

[https://github.com/manim-kindergarten](https://github.com/manim-kindergarten)



[https://github.com/manim-kindergarten/manim\_document\_zh](https://github.com/manim-kindergarten/manim_document_zh)



gh-pages分支推送博客网页。



看的是这个教程：
https://yq.aliyun.com/articles/694995






```bash

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (master)
$ git init
Initialized empty Git repository in C:/Users/admin/Documents/manim/Manim-Document-zh/build/html/.git/

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (master)
$ git checkout --orphan gh-pages
Switched to a new branch 'gh-pages'

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (gh-pages)
$ git add .
warning: LF will be replaced by CRLF in _sources/1.installation安装/index.rst.txt.


The file will have its original line endings in your working directory

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (gh-pages)
$ git commit -m "init project"
[gh-pages (root-commit) d76ea8b] init project
 671 files changed, 170495 insertions(+)
 create mode 100644 .buildinfo
 create mode 100644 .nojekyll

 ......
 create mode 100644 searchindex.js

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (gh-pages)
$ git remote add origin git@github.com:manim-kindergarten/manim_document_zh.git

admin@Tridu MINGW64 ~/Documents/manim/Manim-Document-zh/build/html (gh-pages)
$ git push origin gh-pages
Enumerating objects: 601, done.
Counting objects: 100% (601/601), done.
Delta compression using up to 4 threads
Compressing objects: 100% (593/593), done.
Writing objects: 100% (601/601), 19.24 MiB | 162.00 KiB/s, done.
Total 601 (delta 168), reused 0 (delta 0)
remote: Resolving deltas: 100% (168/168), done.
remote:
remote: Create a pull request for 'gh-pages' on GitHub by visiting:
remote:      https://github.com/manim-kindergarten/manim_document_zh/pull/new/gh-pages
remote:
To github.com:manim-kindergarten/manim_document_zh.git
 * [new branch]      gh-pages -> gh-pages

```





















































































