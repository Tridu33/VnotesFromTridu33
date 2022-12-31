








https://blog.csdn.net/ArrowYL/article/details/79333178

[链表添加函数中为什么要用指向链表指针的指针](https://blog.csdn.net/shen_jz2012/article/details/50631317)
#if  0  ...   #endfif的作用跟/*...*/的作用是一样的，就是注释，可是注释为什么不用注释符号/*就行了么？google了一下，大家都说是为了解决嵌套注释
一下优化，减少不必要的功能。


#if 1    需要编译器编译以下内容；

#if 0   编译器不要编译以下内容；

#if 0   #endif   这种用法还可以实现“注释嵌套！！！”//如果用的话，中间的代码不能加注释。这样不利于调试。

#define TSIZE      45
struct film
{
    char title[TSIZE];
    int rating;
};//定义第一个结构体

/* 类型重定义，Item 相当于 struct film */
typedef struct film Item; 

/* 定义第二个结构体，并将此结构体重命名为 Node */ 
typedef struct node 
{ 
Item item;           // struct film item；
struct node * next;  //此结构体指针
} Node;

/* 类型重定义，将Node* 相当于 List */
typedef Node * List; 





C与C++关于*与&（引用方式传参，传值方式传参https://blog.csdn.net/qq_34243930/article/details/81638852

**值传参，复制副本**
void AddToTail(Node** pHead, int value);值传参，结构体指向指针的指针，如果detype struct node{...}Node,Linklist的话也可以等价:void AddToTail(Linlist * pHead, int value);

因为a传进去的时候会被复制了一份copy，此后的修改都是在临时变量copy上，出了函数体copy被销毁，a还是原来的a，根本就没被修改过，所以才会值传参对变量的修改无效。要使得对a的修改有效，一方面是传入a的地址，也就是对指向a的指针作为值传参（反正修改的不是a的指针，修改了也无所谓，反正只是修改a的指针的copy），此时a的指针的copy指向的内容也是a，因此对copy指向的内容修改会导致a的内容也被修改，check！另外一种方式就是引用传参，引用传参往往要比值传参高效，因为它是直接将a作为参数传入进去，而少了对a进行复制这部分的开销，既然传入进去的是a，那么对a的修改肯定也生效。
**引用传参，直接改变原来的值**
void AddToTail(Node* &pHead, int value);引用传参更高效https://blog.csdn.net/shen_jz2012/article/details/50631317

--------------------- 
作者：mrshen007 
来源：CSDN 
原文：https://blog.csdn.net/shen_jz2012/article/details/50631317 
版权声明：本文为博主原创文章，转载请附上博文链接！
**因此链表建立删除传参需要指向指针的指针传入参数（值传参）**

















'''
/*************************************************************************************************
函数名称:fgets_wrapper
参数：buffer输入缓冲区指针;buflen最大输入字符数，实际最大输入buflen-1; fp输入流
功能：重新封装fgets函数;
      解决fgets输入时最大长度超过buflen-1个字符后输入缓冲区遗留问题及输入包含'\n'问题
区别: scanf("%s",buffer) 输入字符串不能有空格；
      gets(buffer)输入字符串超过buffer长度导致溢出错误；
	  fgets(buffer,buflen,fp)最大输入buflen-1个字符，'\n'会被输入；输入被截断后输入缓冲区有遗留
*****************************************************************************************************/
char *fgets_wrapper(char *buffer, size_t buflen, FILE *fp)
{
	if (fgets(buffer, buflen, fp) != 0)
	{
	size_t len = strlen(buffer);
	if (len > 0 && buffer[len-1] == '\n')
	{
		buffer[len-1] = '\0';
	}
	//清空剩余的数据
	else
	{
		int ch;
		while ((ch = getc(fp)) != EOF && ch != '\n');
	}
	return buffer;
	}
	return 0;
}
 
'''





















