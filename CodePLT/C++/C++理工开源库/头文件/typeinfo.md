# typeinfo
请问这个意思是不是把头文件typeinfo.h改为typeinfo就行了？我最近在学清华邓俊辉老师的数据结构，用VS2019打开老师的工程文件就出现了这个错误。
是的


已删除非标准标头<stdexcpt.h>和<typeinfo.h>。包含它们的代码应改为分别包括标准标头  **\<exception\>**    和 **\<typeinfo\>**




















#include <typeinfo.h>




函数typeid()返回值类型class type_info。
其中type_info重载了操作符==, !=, =分别用来比较是否相等、不等、赋值。
函数name()返回类型名称。




当类型是类和类指针时需要注意：
正常类基类指针base*指向继承类deived，则typeid(deived) != typeid(*base) 前者类型是继承类的type_info类型，而后者是父类的type_info类型。
虚类基类指针base*指向继承类deived，则typeid(deived) == typeid(*base) 两者都是父类的type_info类型。
// type_info example












