# 1. octave


[https://github.com/calysto/octave_kernel](https://github.com/calysto/octave_kernel)

Octave基本操作
https://www.cnblogs.com/zhxuxu/p/9473385.html#_label4


官网教程

https://octave.org/doc/interpreter/Functions-and-Scripts.html


[http://homepages.math.uic.edu/~hanson/Octave/OctaveLinearAlgebra.html](http://homepages.math.uic.edu/~hanson/Octave/OctaveLinearAlgebra.html)





不等号：~=

注释：%

抑或xor()

结尾不用；，如果用了效果是抑制输出。

赋值之后再次输入该变量，就会回馈你他上次赋值是什么。

复杂的打印用disp()

小数点后几位用disp(printf('其他字符串%0.2f',a))

format long标准输出long格式，这使得之后所有的都是long输出。

矩阵换行用；

表示矩阵用[]

v=1:0.1:2从1每次增加0.1直到2，并把它们作为行向量。

v=ones(2,3)声明2行三列全一矩阵、2*ones(2,3)

v=zeros(2,3)全零

rand(2,3)随机

不说赋值给谁默认给ans

randn正态分布h=randn(1,3)均值是1，方差是3，miu和theta

hist(h)绘制h的直方图hist(h,50)绘制50条直方图，精准度更高

size(a)返回a大小，会把a当作矩阵，反悔dimention，返回的是一个一行两列的矩阵。

size(A,1)返回A的一维大小，这就涉及到多维矩阵，一维行二维列。因为我测试了size(A,3/4/5这样)全等于1，所以我猜这是维度。

length(A)返回最大维度大小。

cd '路径'进入文件夹

ls列出现有的文件文件夹

进入文件夹，就可读其中的文件，直接打文件名就能打开该文件，通常是类似于.cpp一样的命令文本

加载别的格式的文件load('data.txt')=load data.txt

.dat格式是处理好的就能用的数据，有表头，数据这样的。who命令可以直接查看其中的features

whos可以更详细的查看features

输入feature名，可以点名他，然后size(feature)可以查询它的大小。

试用whos之后使用clear feature_name 可以删除那一特征。

v=feature_name(1:10)将该特征的前10个数值存入v，并且算入.dat文件。

save test.mat v;存成二进制文件

save test.txt v -ascii存成埃斯科码的txt文件

A(3,2)指引到矩阵A的三行两列

A(2,:)指到第二行所有的元素

A([1 3],:)1,3行逻辑或，列都要

A(:,2) = [10; 11; 12]给第二列赋值

A=[[1,2,3];A]与A=[A,[1,2,3]]是分别加行和列，关键在于符号

A(:)把a变成列向量

C=[A;B]如果在括号里面，；以及，是被看做一种运算，‘  ’空格也被看作一种运算。表示加行加列加行.如果不加[]，对于；那就直接结束了C=A;B.C=A,B会显示B并且给C赋值A。



























