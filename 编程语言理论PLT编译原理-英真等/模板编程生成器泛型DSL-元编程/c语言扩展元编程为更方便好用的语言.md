








# 1. c语言扩展元编程为更方便好用的语言






扩展C语言。



这里推荐一个我觉得非常神奇的一个C语言库：Cello • High Level C

这个库将C语言的宏玩出了花，结合库中提供的运行时，给C语言增加了如下的特性：

List、Set、Map等通用数据结构；
多态函数；
接口、类；
构造函数、析构函数；
可选的垃圾回收；
异常；
反射、RTTI；
等等。
举个例子，如果不提醒的话，我觉得很多人可能不会觉得以下代码是C语言：


```cpp
#include "Cello.h"

int main(int argc, char** argv) {

  /* Stack objects are created using "$" */
  var i0 = $(Int, 5);
  var i1 = $(Int, 3);
  var i2 = $(Int, 4);

  /* Heap objects are created using "new" */
  var items = new(Array, Int, i0, i1, i2);

  /* Collections can be looped over */
  foreach (item in items) {
    print("Object %$ is of type %$\n", item, type_of(item));
  }

  /* Heap objects destructed via Garbage Collection */
  return 0;
}


```



作者：年轻人啊不要熬夜
链接：https://www.zhihu.com/question/449508165/answer/1786904261
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 2. 宏不是图灵完备的




**C++模板元编程是Turing-complete**



https://qa.1r1g.com/sf/ask/525593281/

预处理器可以充当图灵完整语言,但不是局限于计算机的有限内存,而是受限于应用的有限数量的扫描.

C++预处理器不允许无限状态.您只有有限数量的开/关状态,加上包含堆栈.这使它成为一个下推式自动机,而不是图灵机(这也忽略了预处理器递归受限的事实 - 但模板递归也是如此).

但是,如果稍微改变定义,可以通过多次调用预处理器来实现 - 通过允许预处理器生成重新调用预处理器的程序,并在外部循环,确实可以使用预处理器.链接的示例使用C,但它应该足够容易适应C++.








