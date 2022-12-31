

https://github.com/JourWon/test-lombok

教程

https://gitee.com/cauchy6317/lombok
注解系列文章




java类加载顺序：（静态变量、静态初始化块）–>（变量、初始化块）–> 构造器。如果有父类，加载顺序是：父类static方法 –> 子类static方法 –> 父类构造方法- -> 子类构造方法 。


        @Builder 关于Builder较为复杂一些，Builder的作用之一是为了解决在某个类有很多构造函数的情况，也省去写很多构造函数的麻烦
        ，Builder在设计模式中的思想是：用一个内部类去实例化一个对象，避免一个类出现过多构造函数，
        
        @Setter ： 注在属性上，提供 set 方法
        
        @Getter ： 注在属性上，提供 get 方法
        
        @EqualsAndHashCode ： 注在类上，提供对应的 equals 和 hashCode 方法
        
        @Log4j/@Slf4j ： 注在类上，提供对应的 Logger 对象，变量名为 log

        @Data   ：注解在类上；提供类所有属性的 getting 和 setting 方法，此外还提供了equals、canEqual、hashCode、toString 方法。
        Lombok给出了一个注解用来表示这个四个注解@Getter/@Setter，@ToString，@EqualsAndHashCode，@RequiredArgsConstructor等注解，这个几个注解通常都是一个实体类所需要的。如果为每一个类都去加上这四个注解会有点麻烦

        @Setter：注解在属性上；为属性提供 setting 方法

        @Getter：注解在属性上；为属性提供 getting 方法

        @Log4j ：注解在类上；为类提供一个 属性名为log 的 log4j 日志对象

        @NoArgsConstructor：注解在类上；为类提供一个无参的构造方法

        @AllArgsConstructor：注解在类上；为类提供一个全参的构造方法

# 1. Lombok for Java启发的Python简化模板库


```




```







https://github.com/IgniparousTempest/puffadder https://www.cnpython.com/pypi/puffadder


https://github.com/rayanht/paprika 更新更好用
https://pypi.org/project/paprika/

```
pip install paprika
```

and

```python
from paprika import *
```



```
import paprika
@paprika.data
```




