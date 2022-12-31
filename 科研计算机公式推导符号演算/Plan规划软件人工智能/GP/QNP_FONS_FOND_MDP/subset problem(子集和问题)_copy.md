# subset problem(子集和问题)




blog.csdn.net/a130737/article/details/44242047

子集和问题是一个NP的问题（没有已知的polynomial time的算法）。

但是我们可以使用动态规划的办法在pseudo polynomial的时间内解决这个问题。 我们的做法是：

创建一个2D的boolean table subset[i][j]。 然后自底向上的方式（所以没有递归）填充这个二维布尔数组。  如果存在一个子集合set[0..j-1],, 使得这个子集合的和等与i, 我们就记录subset[i][j]为true， 否则填充为false。 最后我们只需要返回subset[sum][n]即可。


https://www.cnblogs.com/jclian91/p/9132663.html
python求解







