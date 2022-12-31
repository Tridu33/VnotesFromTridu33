# python22c

一条命令自动把 Python 翻译成等价 C++ - 腾讯技术工程的文章 - 知乎
https://zhuanlan.zhihu.com/p/95349005


那其实 “翻译器 Transpiler ” ，和编译器解释器类似，也是个古老的热门话题了，比如 https://link.zhihu.com/?target=https%3A//webassembly.org/  WebAssembly, https://link.zhihu.com/?target=https%3A//coffeescript.org/ CoffeeScript ，Babel https://link.zhihu.com/?target=https%3A//www.babeljs.cn/docs/ ,
Google Closure Compiler https://link.zhihu.com/?target=https%3A//github.com/google/closure-compiler，f2c https://link.zhihu.com/?target=https%3A//www.netlib.org/f2c/f2c.1


一番搜索，发现 python 到 C++ 的翻译器也不少，其中 Pythran 是新兴比较热门的开源项目。
https://link.zhihu.com/?target=https%3A//github.com/serge-sans-paille/pythran


于是一番尝试后，借助 pythran，我们实现了：

- 一条命令 全自动把 **Python 翻译成等价 C++**
- 严格等价保证改写，彻底消除不一致
- 完全去掉重新实现 这块工作量，后台开发成本降到 0 ，彻底解放生产力
- 算法同学继续使用纯 python，开发效率无影响，**无学习成本**
- 并能推广到其他需要 python 改写成后台 C++ 代码 的业务场景，解放生产力


```python
import math
import numpy as np

def zero(n, m):
    return [[0]*n for col in range(m)]

#pythran export matrix_multiply(float list list, float list list)
def matrix_multiply(m0, m1):
    new_matrix = zero(len(m0),len(m1[0]))
    for i in range(len(m0)):
        for j in range(len(m1[0])):
            for k in range(len(m1)):
                new_matrix[i][j] += m0[i][k]*m1[k][j]
    return new_matrix

#pythran export arc_distance(float[], float[], float[], float[])
def arc_distance(theta_1, phi_1, theta_2, phi_2):
    """
    Calculates the pairwise arc distance
    between all points in vector a and b.
    """
    temp = (np.sin((theta_2-theta_1)/2)**2
           + np.cos(theta_1)*np.cos(theta_2) * np.sin((phi_2-phi_1)/2)**2)
    distance_matrix = 2 * np.arctan2(np.sqrt(temp), np.sqrt(1-temp))
    return distance_matrix


#pythran export dprod(int list, int list)
def dprod(l0,l1):
    """WoW, generator expression, zip and sum."""
    return sum(x * y for x, y in zip(l0, l1))


#pythran export get_age(int )
def get_age(age):
    if age <= 20:
        age_x = '0_20'
    elif age <= 25:
        age_x = '21_25'
    elif age <= 30:
        age_x = '26_30'
    elif age <= 35:
        age_x = '31_35'
    elif age <= 40:
        age_x = '36_40'
    elif age <= 45:
        age_x = '41_45'
    elif age <= 50:
        age_x = '46_50'
    else:
        age_x = '50+'
    return age_x


```















