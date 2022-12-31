# COM
LoadLibrary  一般是动态加载DLL时（你并不需要对应的头文件，和LIB） 

#pragma comment 一般是静态加载DLL时（对应的头文件、DLL，和LIB缺一不可，并且生产的EXE没有找到DLL文件就会导致“应用程序初始化失败”） 

#import指令用于从一个类型库中结合信息。该类型库的内容被转换为C++类,主要用于描述COM界面。







[《COM本质论》读书笔记https://www.cnblogs.com/rhzhang/p/5184262.html](https://www.cnblogs.com/rhzhang/p/5184262.html)





















COM 过时了吗？它的应用前景究竟如何？ - vczh的回答 - 知乎 https://www.zhihu.com/question/19998748/answer/20234998











虽然现在已经很少使用com了，但没觉得com技术过时了，反而进化成了winrt组件。


怎么通俗的解释COM组件？ - 灵剑的回答 - 知乎 https://www.zhihu.com/question/49433640/answer/115952604

COM，OLE，ActiveX，OCX，VBScript，历史不会忘记你们的，如果历史忘了，我替历史记住你们。安息吧。

到今天，其实COM都是C++的二进制本机代码的动态链接的最佳的选择（Windows上的）。但是，C++，二进制本机代码，动态链接，这三件事现在没有一件是重要的……

怎么通俗的解释COM组件？ - Froser的回答 - 知乎 https://www.zhihu.com/question/49433640/answer/116028598



怎么通俗的解释COM组件？ - Xiaoyu Ma的回答 - 知乎 https://www.zhihu.com/question/49433640/answer/116142887


















































