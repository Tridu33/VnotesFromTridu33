# 1. tomcat中文编码
浏览器页面	GBK
(可在浏览器页面右键切换)
request（get）	ISO-8859-1
request（post）	GBK(同浏览器)，但是如果是服务器来的页面一般已经设置了UTF-8(例如JSP提交的页面)
Servlet（response）	ISO-8859-1
————————————————
版权声明：本文为CSDN博主「荣磊」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kevinr1990/java/article/details/78655407



```
System.out.println("中文");
 
        System.out.println("中文".getBytes());
 
        System.out.println("中文".getBytes("GB2312"));
 
        System.out.println("中文".getBytes("ISO8859_1"));
 
        System.out.println(new String("中文".getBytes()));
 
        System.out.println(new String("中文".getBytes(), "GB2312"));
 
        System.out.println(new String("中文".getBytes(), "ISO8859_1"));
 
        System.out.println(new String("中文".getBytes("GB2312")));
 
        System.out.println(new String("中文".getBytes("GB2312"), "GB2312"));
 
        System.out.println(new String("中文".getBytes("GB2312"), "ISO8859_1"));
 
        System.out.println(new String("中文".getBytes("ISO8859_1")));
 
        System.out.println(new String("中文".getBytes("ISO8859_1"), "GB2312"));
 
        System.out.println(new String("中文".getBytes("ISO8859_1"), "ISO8859_1"));
```



[TomCat的编码https://blog.csdn.net/shendeguang/article/details/8231673](https://blog.csdn.net/shendeguang/article/details/8231673)
















