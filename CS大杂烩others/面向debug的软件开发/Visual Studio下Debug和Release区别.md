# Visual Studio下Debug和Release区别
 debug程序通常比release程序要慢，尤其是处理视频方便release要比debug快很多。在release模式对程序进行调试的时候经常会遇到变量虽然初始化了，但是在查看其值的时候却发现是一个随机的数并不是初始化的值，有时候在对变量进行监视的时候了，会出现找不到变量的情况，原因大致如下：

> debug跟release在初始化变量时所做的操作是不同的，debug是将每个字节位都赋成0xcc， 而release的赋值近似于随机。如果你的程序中的某个变量没被初始化就被引用，就很有可能出现异常：用作控制变量将导致流程导向不一致；用作数组下标将会使程序崩溃；更加可能是造成其他变量的不准确而引起其他的错误。所以在声明变量后马上对其初始化一个默认的值是最简单有效的办法，否则项目大了你找都没地方找。代码存在错误在debug方式下可能会忽略而不被察觉到。debug方式下数组越界也大多不会出错，在release中就暴露出来了，这个找起来就比较难了。

   只有DEBUG版的程序才能设置断点、单步执行、使用 TRACE/ASSERT等调试输出语句。REALEASE不包含任何调试信息，所以体积小、运行速度快。
   



 Debug 和 Release 的真正区别，在于一组编译选项。 
Debug 版本   
>参数       含义   
/MDd /MLd 或 /MTd 使用 Debug runtime library(调试版本的运行时刻函数库)   
/Od 关闭优化开关   
/D "_DEBUG" 相当于 #define _DEBUG,打开编译调试代码开关(主要针对assert函数)   
/ZI   
创建 Edit and continue(编辑继续)数据库，这样在调试过程中如果修改了源代码不需重新编译   
GZ 可以帮助捕获内存错误  

   
Release 版本 参数含义   
>/MD /ML 或 /MT 使用发布版本的运行时刻函数库   
/O1 或 /O2 优化开关，使程序最小或最快   
/D "NDEBUG" 关闭条件编译调试代码开关(即不编译assert函数)   
/GF 合并重复的字符串，并将字符串常量放到只读内存，防止被修改  


Debug 和 Release 并没有本质的界限，他们只是一组编译选项的集合，编译器只是按照预定的选项行动。 




https://blog.csdn.net/pkueecser/article/details/8653213
这些修改意见很重要


Debug模式和Release模式有什么区别？ - 程序喵大人的回答 - 知乎
https://www.zhihu.com/question/443340911/answer/1720297063






添加调试信息生成debug版本，debug版本可使用gdb进行调试（若不携带该选项则默认生成release版本，release不可调试）
gcc -g
Debug版本通常称为调试版本，它包含调试信息，并且不作任何优化，便于程序员调试程序。Release 版本称为发布版本，它往往是进行了各种优化，使得程序在代码大小和运行速度上都是最优的，以便用户很好地使用。



https://blog.csdn.net/bestgonghuibin/article/details/6092143
有时优化会出错

《Debug 和 Release 模式下程序测试时间不同》, https://blog.csdn.net/qq_39367684/article/details/112298045





































