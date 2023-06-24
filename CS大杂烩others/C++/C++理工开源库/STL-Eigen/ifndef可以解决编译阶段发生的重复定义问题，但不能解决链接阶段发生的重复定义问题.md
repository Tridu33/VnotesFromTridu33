# ifndef可以解决编译阶段发生的重复定义问题，但不能解决链接阶段发生的重复定义问题
































所以不要在头文件中作具体定义！

########给新人科普##########

头文件中#ifndef的用法如下：

#ifndenf \_\_XXXXX\_H  

#define \_\_XXXXX\_H

函数声明

#endif

其中ifndef(if not define)用来判断这个宏有没有定义过，如果没有定义过，说明这个头文件是第一次引用，那么就继续往下执行；如果这个宏定义过了，说明这个头文件已经被包含过了，直接跳到endif，也就是什么都不执行，就可以防止重复包含头文件了。

########################






[h和c文件的区分，很全面](https://blog.csdn.net/21aspnet/article/details/149810)












https://blog.csdn.net/a445849497/article/details/80512814












