# c++面试









你遇到过哪些高质量的 C++ 面试？ - 知乎
https://www.zhihu.com/question/60911582/answer/596537278




















比如面试官问智能指针。

首先说三个智能指针的实现以及内存模型（建议使用make shared因为make shared的内存模型可能是control block和对象连在一起的、control block为什么要有weak ref count），unique的T[]偏特化，shared from this的设计思路crtp，智能指针的设计指导思想raii，智能指针的线程安全性，等等。

然后由智能指针的内存模型说到堆栈的分配，虚拟地址，exec加载，动态链接库，mmap，堆的实现（freelist、分配一块大的33页（好像是、记不住了）、直接mmap），再展开可以说页表、tlb、tlb刷新，进程切换（switch mm、switch to、系统调用int 80过程、调用约定，fork把子进程tss的rax设置为0所以子进程fork返回0），带进程id的tlb，ipc，等等。

T[]偏特化说到C++模板的偏序原则，说到msvc、gcc、clang的array decay的偏序规则不一致，说到C++模板实例化原理（名称查找、参数推导、参数替换、重载决议），SFINAE，模板元编程。

crtp说到多态和system F。爬一遍lambda cube，说到dependent type以及C++阉割版的非类型模板参数。再说到递归，为什么system F里的递归就比stlc里的和谐，强在哪。





所以我觉得面试官问什么一点也不重要。主要是面试官想和你以什么方式聊。如果面试官要是敞开心扉放飞自我，总有面试官熟悉的领域，开开心心聊俩小时完事。如果面试官要是拿个小本本记你答题答的对不对，那面试官的引导是最重要的。













