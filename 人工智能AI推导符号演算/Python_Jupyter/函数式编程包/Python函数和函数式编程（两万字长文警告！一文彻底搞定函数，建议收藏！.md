# Python函数和函数式编程（两万字长文警告！一文彻底搞定函数，建议收藏！





### 文章目录

-   [Python函数和函数式编程](https://blog.csdn.net/qq_44721831/article/details/102883028#Python_1)

-   [1、函数概述](https://blog.csdn.net/qq_44721831/article/details/102883028#1_3)

-   [1.1函数的基本概念](https://blog.csdn.net/qq_44721831/article/details/102883028#11_4)
-   [1.2函数的功能](https://blog.csdn.net/qq_44721831/article/details/102883028#12_10)
-   [1.3Python中函数的分类](https://blog.csdn.net/qq_44721831/article/details/102883028#13Python_18)

-   [2、函数的声明和调用](https://blog.csdn.net/qq_44721831/article/details/102883028#2_28)

-   [2.1函 数对象的创建](https://blog.csdn.net/qq_44721831/article/details/102883028#21__29)
-   [2.2函数的调用](https://blog.csdn.net/qq_44721831/article/details/102883028#22_72)
-   [2.3函数的副作用](https://blog.csdn.net/qq_44721831/article/details/102883028#23_108)

-   [3、参数的传递](https://blog.csdn.net/qq_44721831/article/details/102883028#3_114)

-   [3.1形式参数和实际参数](https://blog.csdn.net/qq_44721831/article/details/102883028#31_115)
-   [3.2形式参数变量和对象引用传递](https://blog.csdn.net/qq_44721831/article/details/102883028#32_132)
-   [3.3传递不可变对象的引用](https://blog.csdn.net/qq_44721831/article/details/102883028#33_138)
-   [3.4传递可变对象的引用](https://blog.csdn.net/qq_44721831/article/details/102883028#34_164)
-   [3.5可选参数](https://blog.csdn.net/qq_44721831/article/details/102883028#35_186)
-   [3.6位置参数和命名参数](https://blog.csdn.net/qq_44721831/article/details/102883028#36_202)
-   [3.7可变参数](https://blog.csdn.net/qq_44721831/article/details/102883028#37_230)
-   [3.8 强制命名参数](https://blog.csdn.net/qq_44721831/article/details/102883028#38__265)
-   [3.9参数类型检查](https://blog.csdn.net/qq_44721831/article/details/102883028#39_286)

-   [4、函数的返回值](https://blog.csdn.net/qq_44721831/article/details/102883028#4_293)

-   [4.1return语句和函数返回值](https://blog.csdn.net/qq_44721831/article/details/102883028#41return_294)
-   [4.2多条return语句](https://blog.csdn.net/qq_44721831/article/details/102883028#42return_319)
-   [4.3 返回多个值](https://blog.csdn.net/qq_44721831/article/details/102883028#43__340)

-   [5、变量的作用域](https://blog.csdn.net/qq_44721831/article/details/102883028#5_357)

-   [5.1全局变量](https://blog.csdn.net/qq_44721831/article/details/102883028#51_359)
-   [5.2 局部变量](https://blog.csdn.net/qq_44721831/article/details/102883028#52__391)
-   [5.3全 局语句global](https://blog.csdn.net/qq_44721831/article/details/102883028#53_global_409)
-   [5.4非局部语句nonlocal](https://blog.csdn.net/qq_44721831/article/details/102883028#54nonlocal_444)
-   [5.5 类成员变量](https://blog.csdn.net/qq_44721831/article/details/102883028#55__463)
-   [5.6 输出局部变量和全局变量](https://blog.csdn.net/qq_44721831/article/details/102883028#56__467)

-   [6、递归函数](https://blog.csdn.net/qq_44721831/article/details/102883028#6_486)

-   [6.1递归函 数的定义](https://blog.csdn.net/qq_44721831/article/details/102883028#61__487)
-   [6.2递归函数的原理](https://blog.csdn.net/qq_44721831/article/details/102883028#62_501)
-   [6.3编写递归函数时需要注意的问题](https://blog.csdn.net/qq_44721831/article/details/102883028#63_527)
-   [6.4 递归函数的应用:最大公约数](https://blog.csdn.net/qq_44721831/article/details/102883028#64__544)
-   [6.5 递归函数的应用:汉诺塔](https://blog.csdn.net/qq_44721831/article/details/102883028#65__564)

-   [7、内置函数的使用](https://blog.csdn.net/qq_44721831/article/details/102883028#7_590)

-   [7.1 内置函数一览表](https://blog.csdn.net/qq_44721831/article/details/102883028#71__592)

-   [8、Python函数式编程基础](https://blog.csdn.net/qq_44721831/article/details/102883028#8Python_614)

-   [8.1作为对象的函数](https://blog.csdn.net/qq_44721831/article/details/102883028#81_617)
-   [8.2 高阶函数](https://blog.csdn.net/qq_44721831/article/details/102883028#82__627)
-   [8.3map()函数](https://blog.csdn.net/qq_44721831/article/details/102883028#83map_636)
-   [8.4filter()函数](https://blog.csdn.net/qq_44721831/article/details/102883028#84filter_673)
-   [8.5reduce()函数](https://blog.csdn.net/qq_44721831/article/details/102883028#85reduce_707)
-   [8.6 lambda表达式（匿名函数）及用法](https://blog.csdn.net/qq_44721831/article/details/102883028#86_lambda_735)
-   [8.7@函数装饰器及用法（超级详细）](https://blog.csdn.net/qq_44721831/article/details/102883028#87_852)

-   [8.7.1 引入](https://blog.csdn.net/qq_44721831/article/details/102883028#871__853)
-   [8.7.2带参数的函数装饰器](https://blog.csdn.net/qq_44721831/article/details/102883028#872_908)
-   [8.7.3带自定义参数的函数装饰器](https://blog.csdn.net/qq_44721831/article/details/102883028#873_976)
-   [8.7.4函数装饰器也可以嵌套](https://blog.csdn.net/qq_44721831/article/details/102883028#874_1009)


