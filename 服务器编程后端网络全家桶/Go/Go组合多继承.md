# Go组合多继承



go语言一个module里面，假设定义一个c struct多重继承a接口和b interface，其中
假如a,b存在一个相同返回值，参数，方法名的方法tempMethod()，

那么
func(xxx *c) tempMethod() String{balabala}

是不是就必须要求tempMethod() 在a,b的含义是一样的，即只有balabala写的一种实现来计算temMethod的值。
可以区分开a,b接口为两种不同的tempMethod() 方法吗？还是说不存在这种建模。

比如成绩计算系统中，有一个4.0满分a绩点体系，5.0满分b绩点体系，c学生结构体的getScore分数计算方法，要怎么多态继承。

>用 ca 实现 a，再用 cb 实现 b，在用 c 组合 ca cb.调用c.ca.tempMethod()和c.cb.tempMethod()就可以区分了。



**提倡组合不提倡继承**
继承隐藏一个虚指针多态去找方法名，go的组合c.ca.tempMethod一层层指明地址去找方法地址有点类似“js的原型链，自动从内往外找作用域的方法签名，然后调用最靠近里面的”














