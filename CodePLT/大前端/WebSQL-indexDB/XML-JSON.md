[TOC]

# 1. JSON 工具

 [格式化工具](http://tool.oschina.net/codeformat/json/)


 [JSON-XML互转](http://www.bejson.com/xml2json/)








# 2. XML
XML规范：

https://www.w3.org/TR/REC-xml/


扩展标记语言 (Extensible Markup Language, XML) ，用于标记电子文件使其具有结构性的标记语言，可以用来标记数据、定义数据类型，是一种允许用户对自己的标记语言进行定义的源语言。 XML使用DTD(document type definition)文档类型定义来组织数据;格式统一，跨平台和语言，早已成为业界公认的标准。





Xml 格式数据的生成和解析[https://blog.csdn.net/axi295309066/article/details/52760959](https://blog.csdn.net/axi295309066/article/details/52760959)

教程
[https://www.runoob.com/xml/xml-usage.html](https://www.runoob.com/xml/xml-usage.html)


[https://www.w3school.com.cn/xml/xml_intro.asp](https://www.w3school.com.cn/xml/xml_intro.asp)


如果是读取本地xml，chrome默认是禁止访问本地文件，需要增加启动参数 --allow-file-access-from-files。


不同的浏览器对xml的解析方式不同，根据目前主流浏览器大致分三类：

第一类，ie： js 提供用于创建 Automation对象的方法，new ActiveXObject("Microsoft.XMLDOM") ；

第二类：firefox，opera：用构造函数 DOMParser()实例化DOMParser对象，解析xml文本，并返回xml Document对象；

第三类：chrome，safari：由于chrome不支持load方法，故用http协议，XMLHttpRequest对象。

代码：

funct













# 3. JSON
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。

JSON规范：

http://json.org/


关于流行度，XML已经被业界广泛的使用，而JSON才刚刚开始，但是在Ajax这个特定的领域，未来的发展一定是XML让位于JSON。到时Ajax应该变成Ajaj(Asynchronous Javascript and JSON)[https://www.cnblogs.com/lightsong/p/6230280.html](https://www.cnblogs.com/lightsong/p/6230280.html)


[ Json入门基础、Json常用数据类型、Json语法](https://blog.csdn.net)King_weng/article/details/88263717?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task）










 教程
 [https://www.w3cschool.cn/json/9l4f1h7u.html](https://www.w3cschool.cn/json/9l4f1h7u.html)





-   对象表示为键值对
-   数据由逗号分隔
-   花括号保存对象
-   方括号保存数组

· 并列的数据之间用逗号“**，**”分割；  
· 映射用冒号“**：**”表示；  
· 映射的集合用大括号“**{ }**”表示，其中在一个大括号内部的部分为一个完整的**对象**；  
· 中括号“**\[ \]**”用来描述，在中括号中的部分为**JSON数组**，可以包含多个对象。












































































































































