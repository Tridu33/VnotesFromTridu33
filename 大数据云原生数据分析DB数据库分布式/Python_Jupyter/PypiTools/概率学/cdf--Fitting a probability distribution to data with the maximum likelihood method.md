# cdf--Fitting a probability distribution to data with the maximum likelihood method
https://ipython-books.github.io/75-fitting-a-probability-distribution-to-data-with-the-maximum-likelihood-method/











gama And erlang 讲的很好
[http://nicta.github.io/dora/generated/generated/scipy.stats.gamma.html](http://nicta.github.io/dora/generated/generated/scipy.stats.gamma.html)


[http://nicta.github.io/dora/generated/generated/scipy.stats.erlang.html#scipy.stats.erlang](http://nicta.github.io/dora/generated/generated/scipy.stats.erlang.html#scipy.stats.erlang)














画图得到

```
impot seaborn as sns
from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=10000)
ax = sns.distplot(data_gamma,
                  kde=False,
                  bins=100,
                  color='skyblue',
                )
ax.set(xlabel='Gamma', ylabel='Frequency')

```

[https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv\_histogram.html#scipy.stats.rv\_histogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_histogram.html#scipy.stats.rv_histogram)







```
import seaborn as sns
from scipy.stats import erlang
data_erlang = erlang.rvs(a=1,scale=1,loc=0,size=1,random_state=None)
ax = sns.distplot(data_erlang,
                  kde=False,
                  color='skyblue',
                 )
ax.set(xlabel='Negative Binomial', ylabel='Frequency')

```



埃尔朗分布的比例scale参数，尺寸size参数，
$\alpha$形状参数必须整数，Gama可以是小数
















[用Scipy拟合伽马分布https://stackoverflow.com/questions/2896179/fitting-a-gamma-distribution-with-python-scipy](https://stackoverflow.com/questions/2896179/fitting-a-gamma-distribution-with-python-scipy)


```python




In [7]: import scipy.stats as stats
   ...: alpha = 5
   ...: loc = 100.5
   ...: beta = 22
   ...: data = stats.gamma.rvs(alpha, loc=loc, scale=beta, size=10000)
   ...: print(data)

#[223.21704399 208.3047519  160.56111625 ... #204.78542849 140.76147946
# 194.69357773]

In [8]: fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
   ...: print(fit_alpha, fit_loc, fit_beta)
   ...: print(alpha, loc, beta)

```


我对ss.gamma.rvs函数感到不满意，因为它可以生成负数，而伽马分布本来应该没有。因此，我通过期望值= mean（data）和方差= var（data）拟合了样本（有关详细信息，请参见Wikipedia），并编写了一个函数，该函数可以生成随机分布的伽马分布样本而不会产生毛刺（我发现很难正确安装，在旁注）：








```python
import random
import numpy

data = [6176, 11046, 670, 6146, 7945, 6864, 767, 7623, 7212, 9040, 3213, 6302, 10044, 10195, 9386, 7230, 4602, 6282, 8619, 7903, 6318, 13294, 6990, 5515, 9157]

# Fit gamma distribution through mean and average
mean_of_distribution = numpy.mean(data)
variance_of_distribution = numpy.var(data)

def gamma_random_sample(mean, variance, size):
    """Yields a list of random numbers following a gamma distribution defined by mean and variance"""
    g_alpha = mean*mean/variance
    g_beta = mean/variance
    for i in range(size):
        yield random.gammavariate(g_alpha,1/g_beta)

# force integer values to get integer sample
grs = [int(i) for i in gamma_random_sample(mean_of_distribution,variance_of_distribution,len(data))]

print("Original data: ", sorted(data))
print("Random sample: ", sorted(grs))

# Original data: [670, 767, 3213, 4602, 5515, 6146, 6176, 6282, 6302, 6318, 6864, 6990, 7212, 7230, 7623, 7903, 7945, 8619, 9040, 9157, 9386, 10044, 10195, 11046, 13294]
# Random sample:  [1646, 2237, 3178, 3227, 3649, 4049, 4171, 5071, 5118, 5139, 5456, 6139, 6468, 6726, 6944, 7050, 7135, 7588, 7597, 7971, 10269, 10563, 12283, 12339, 13066]


```

这是尝试模仿用scipy的自带fit一下埃尔朗分布



```python

import scipy.stats import erlang
alpha=
data_erlang = erlang.rvs(a=1,scale=1,loc=0,size=1)


# ?



```

因为gama直接令alpha=integer就是erlang分布，所以E2的话就直接令


```python 

In [7]: import scipy.stats as stats
   ...: alpha = 2
   ...: loc = 100.5
   ...: beta = 22
   ...: data = stats.gamma.rvs(alpha, loc=loc, scale=beta, size=10000)
   ...: print(data)

#lambda = 1/scale = 1/22
# alpha =2
# loc=100.5位置参数
#[223.21704399 208.3047519  160.56111625 ... #204.78542849 140.76147946
# 194.69357773]

In [8]: fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
   ...: print(fit_alpha, fit_loc, fit_beta)
   ...: print(alpha, loc, beta)


```








不用默认scipy包也行，可以用statsmodels来拟合

```python








```




















```python








```























