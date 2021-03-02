# 《 Velocity用户指南》






[《 Velocity用户指南》](https://velocity.apache.org/engine/1.7/user-guide.html)

[上述官方文档翻译](http://ifeve.com/apache-velocity-dev/)









[简书入门code教程](https://www.jianshu.com/p/5913903324ff)

[教程详解](http://codingdict.com/article/23731)

[教程详解w3c](http://www.51gjie.com/javaweb/126)




Apache Velocity于2001年4月首次发布，它是一个基于Java的模板引擎，提供了一种**模板语言**来引用用Java代码定义的对象。它旨在确保Web应用程序中表示层和业务层之间的清晰分隔（模型-视图-控制器设计模式）。

Velocity是由Apache Software Foundation托管的一个开源软件项目。它根据Apache许可证发行。乔恩·史蒂文斯（Jon Scott Stevens）的名字来自PowerPC G4芯片中的AltiVec Velocity Engine 。


Velocity是一个基于java的模板引擎（template engine）。它允许任何人仅仅简单的使用模板语言（template language）来引用由java代码定义的对象。 当Velocity应用于web开发时，界面设计人员可以和java程序开发人员同步开发一个遵循MVC架构的web站点，也就是说，页面设计人员可以只 关注页面的显示效果，而由java程序开发人员关注业务逻辑编码。Velocity将java代码从web页面中分离出来，这样为web站点的长期维护提 供了便利，同时也为我们在JSP和PHP之外又提供了一种可选的方案。


使用Velocity的一些常见类型的应用程序是：

AWS API Gateway主体映射模板
AWS API Gateway主体映射模板。
Web应用程序：Web开发人员呈现HTML页面结构。内容填充有动态信息。该页面使用VelocityViewServlet或任何支持Velocity的框架中的任何一个处理。
源代码生成：Velocity可用于基于模板生成Java，SQL或PostScript源代码。许多开源和商业开发软件包都以这种方式使用Velocity。[1]
自动电子邮件：许多应用程序会为帐户注册，密码提示或自动发送的报告生成自动电子邮件。使用Velocity，电子邮件模板可以存储在文本文件中，而不是直接嵌入Java代码中。
XML转换：Velocity提供了一个称为Anakia的Ant任务，该任务读取XML文件并将其提供给Velocity模板。常见的应用程序是将以通用“ xdoc”格式存储的软件文档转换为样式化的HTML文档。
AWS API Gateway将Apache Velocity引擎用于主体映射模板-输出JSON。
Velocity是一个基于Java的模板引擎，其提供了一个Context容器，在java代码里面我们可以往容器中存值，然后在vm文件中使用特定的语法获取，这是velocity基本的用法，其与jsp、freemarker并称为三大视图展现技术，相对于jsp而言，velocity对前后端的分离更加彻底：在vm文件中不允许出现java代码，而jsp文件中却可以.

作为一个模块引擎，除了作为前后端分离的MVC展现层，Velocity还有一些其他用途，比如源代码生成、自动email和转换xml等，具体的用法可以参考这篇文章.









