# bayes贝叶斯参数估计


# 贝叶斯思想和贝叶斯参数估计







https://wenku.baidu.com/view/420461e4102de2bd9605883c.html

from random import randrange
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


# 绘制时序图
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
data.plot()
plt.legend(prop=myfont)  
plt.show()
# 绘制自相关图
plot_acf(data).show()
# 绘制偏自相关图
plot_pacf(data).show()


文为CSDN博主「Python_小屋」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/oh5W6HinUg43JvRhhB/article/details/78360686













