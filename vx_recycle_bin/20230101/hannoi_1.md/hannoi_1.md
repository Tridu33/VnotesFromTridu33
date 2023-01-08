Hanoi汉诺塔，魔方4色图数独。。。。。。
hanoi(N):- ove(N,left,center,right)
move(0,_,_,_):-!.
move(N,A,B,C)
    N is N-1,
    move(M,A,C,B),
    inform(A,B)
    move(M,C,B,A)
inform(x,y):-write('move from'),write(X),write('to'),write(Y),write('.'),nl.



递归是循环的超集

循环对应尾递归 这样？


你对一颗节点带一个int的二叉树求和就不能普通的用循环接口










离散数学设未知量证明求解，数列递推公式


matlab 可视化
C,
JAVA
，haskell
prolog



























































































