# matplotlib-seaborn中文画图



Matplotlib 数据绘图基础课程

https://www.shiyanlou.com/courses/1093




















使用matplotlib及seaborn时，中文无法正常显示，显示结果为一个方框，解决方法:

Matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题-设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(10, 7))
plt.plot(x, y1, label='$sinx$')
plt.plot(x, y2, label='$cosx$')
plt.legend(loc='upper right')
plt.xlim(-2*np.pi-1, 2*np.pi+3)
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], ['$-2\pi$', '$-\pi$', '$0$', '$\pi$', '$2\pi$'])
plt.title('三角-函数')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.axhline(y=0, c='black')

plt.show()

```

Seaborn
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei')  # 解决Seaborn中文显示问题

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(10, 7))
plt.plot(x, y1, label='$sinx$')
plt.plot(x, y2, label='$cosx$')
plt.legend(loc='upper right')
plt.xlim(-2*np.pi-1, 2*np.pi+3)
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], ['$-2\pi$', '$-\pi$', '$0$', '$\pi$', '$2\pi$'])
plt.title('三角-函数')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.axhline(y=0, c='black')

plt.show()

```

————————————————
版权声明：本文为CSDN博主「风浅安然」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_31816741/article/details/79339898














