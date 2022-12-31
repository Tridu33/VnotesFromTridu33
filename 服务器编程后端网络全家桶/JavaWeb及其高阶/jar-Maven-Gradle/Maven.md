E:\CS_learning\Java\源码笔记教程Demo\JavaLearning高级





Maven是基于项目对象模型(POM project object model)，可以通过一小段描述信息（配置）来管理项目的构建，报告和文档的软件项目管理工具**\[百度百科\]**

　　　　这种又是大白话，如果没明白maven是什么，那么上面这句话跟没说一样，我自己觉得，Maven的核心功能便是合理叙述项目间的依赖关系，通俗点讲，就是通过pom.xml文件的配置获取jar包，而不用手动去添加jar包，而这里pom.xml文件对于学了一点maven的人来说，就有些熟悉了，怎么通过pom.xml的配置就可以获取到jar包呢？pom.xml配置文件从何而来？等等类似问题我们需要搞清楚，如果需要使用pom.xml来获取jar包，那么首先该项目就必须为maven项目，maven项目可以这样去想，就是在java项目和web项目的上面包裹了一层maven，本质上java项目还是java项目，web项目还是web项目，但是包裹了maven之后，就可以使用maven提供的一些功能了(通过pom.xml添加jar包)。



https://www.cnblogs.com/whgk/p/7112560.html


# Maveni教程 
类似ant build建立工程，也就是python的annaconda,sh的各种包管理器之类的存在，建立工程Docker

https://www.w3cschool.cn/maven/

maven能够解决你jar包依赖的问题，最简单的例子，你要开发S2SH项目。你是不是要去找struts2 hibernate spring的jar包 去官网下一堆 然后百度搜索哪些是必须的，在放到你的项目里；麻烦不？  
用了maven 在pom里把依赖一配置，说你要用struts2的xxx版本，xxx家出的，ok 你说一嘴就行，maven插件会从中央仓库拿的；至于struts2依赖了什么？你不用操心……

maven的学习你看看maven实战，百度搜一搜，它是个项目构建的工具，有依赖管理功能；

  
  
作者：顺陌先生  
链接：https://www.zhihu.com/question/20104186/answer/24029424  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。







maven是干嘛的？ - wuxinliulei的回答 - 知乎 https://www.zhihu.com/question/20104186/answer/73797359

# 教程2

https://www.yiibai.com/maven/ 教程




























