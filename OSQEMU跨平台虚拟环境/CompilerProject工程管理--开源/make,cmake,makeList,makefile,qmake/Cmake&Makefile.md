```
 # 利用cmake生成makefile
 cmake .
 # 执行make命令，利用gcc/g++编译生成最终的二进制文件
 make
./configure
make
make install
```

















# Cmake


https://zhuanlan.zhihu.com/p/396719316 cmake

第一步，学会写简单的CMakeLists.txt，这个很容易找到例子，比如vtk，osg都有示例。

第二步，从使用了CMake的项目中寻找示例用法。比如require(xxx)时，cmake会执行findxxx.cmake，你看看这个脚本怎么写的。cmake也自带了不少这样的脚本。

第三步，尝试自己写一个findxxx.cmake，让自己的工程能自动找到你的库。

第四步，查看cmake文档，一个很长的网页，里面有各个命令的说明。

cmake的书籍有一本：[https://github.com/Akagi201/learning-cmake/blob/master/docs/mastering-cmake.pdf](https://link.zhihu.com/?target=https%3A//github.com/Akagi201/learning-cmake/blob/master/docs/mastering-cmake.pdf)。 但我没看过。

优点在于：抽象，跨平台。抽象的意思是，编译软件的步骤都类似，只不过各个平台名称不一样，于是cmake抽象出相关的规则，把你把编译逻辑映射为具体的工程。比如同一个cmake工程可在linux下生成makefile，在Windows下生成vs project。

## 利用vs2017 CMake开发跨平台C++项目实战

https://blog.csdn.net/qingcaichongchong/article/details/86493146

Visual studio 如何导入CMake项目？ - Jingle的文章 - 知乎
https://zhuanlan.zhihu.com/p/58353524


https://docs.microsoft.com/zh-cn/cpp/build/cmake-projects-in-visual-studio?view=msvc-160




##  cmake参数



















## makefile  



makefile https://zhuanlan.zhihu.com/p/393316878







https://blog.csdn.net/haoel/article/details/2886


https://blog.csdn.net/xiaoshuai537/article/details/79340153


示例

https://blog.csdn.net/sfuncc/article/details/80185007

资料


https://download.csdn.net/download/heming6666/10132083

书本









比较权威的文档是[GUN make手册](https://link.zhihu.com/?target=https%3A//www.gnu.org/software/make/manual/make.html)。

浅谈 GNU Make 构建项目实践 - 七阶子的文章 - 知乎 https://zhuanlan.zhihu.com/p/72616078












make makefile cmake qmake都是什么，有什么区别？ - 辉常哥的回答 - 知乎 https://www.zhihu.com/question/27455963/answer/89770919



Makefile新手入门 - CRongbx的文章 - 知乎 https://zhuanlan.zhihu.com/p/97463313


图解嵌入式系统开发之Makefile - 公子小白的文章 - 知乎 https://zhuanlan.zhihu.com/p/71204704







CMAKE综述&学习&常用指令 - 路明的文章 - 知乎 https://zhuanlan.zhihu.com/p/97142420






【译】一个简单的 make & makefile 教程 - JustSong的文章 - 知乎 https://zhuanlan.zhihu.com/p/92010728


























































