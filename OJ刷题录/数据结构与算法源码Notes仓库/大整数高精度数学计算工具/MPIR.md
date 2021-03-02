# MPIR





blog.csdn.net/caorui_nk/article/details/83245607






MPIR 是一个用于高精度计算的数值计算库，提供了对大整数和高精度有理数的支持。

MPIR 是从 GMP 派生出来的项目，GMP 相比大家都听说过，是一套高度优化的任意精度数值计算库。许多很著名的软件在内部都用到了 GMP，比如 gcc。 但是 GMP 有一个问题，就是它里面有大量的汇编代码，这些代码无法在 MSVC 平台下编译。为此，就衍生出了 MPIR 和 MPFR 项目。这两个项目做的工作基本上就是把 GMP 移植到了 MSVC 平台上，其他的改动不多。

当然，MPIR 的目标是跨平台的，linux、Mac OS X 上也可以编译运行。
