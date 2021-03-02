# yield和yield from的用法





cnblogs.com/cnkai/p/7514828.html

### yield

python中yield的用法很像return，都是提供一个返回值，但是yield和return的最大区别在于，return一旦返回，则代码段执行结束，但是yield在返回值以后，会交出CUP的使用权，代码段并没有直接结束，而是在此处中断，当调用send()或者next()方法之后，yield可以从之前中断的地方继续执行。

在一个函数中，使用yield关键字，则当前的函数会变成生成器。

下面生成一个斐波那契数列。

```
def fib(n):
    index = 0
    a = 0
    b = 1

    while index < n:
        yield b
        a,b = b, a+b
        index += 1

```

1.  生成器对象

```
fib = fib(100)
print(fib)

```

打印出来的结果是一个生成器对象，并没有直接把我们想要的值打印出来。

2.  next()方法

```
fib = fib(100)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

```






它的执行顺序是这样的，每次yield返回之后，程序将会中断，当出现next(fib)之后，程序将会从之前中断的地方继续执行。 python新版本中，不再提供`fib.next()`方法。

3.  send()方法

使用send()方法允许我们向生成器中传值。

```
import time

def fib(n):
    index = 0
    a = 0
    b = 1

    while index < n:
        sleep = yield b
        print('等待%s秒' %sleep)
        time.sleep(sleep)
        a,b = b, a+b
        index += 1

fib = fib(20)
print(fib.send(None))   # 效果等同于print(next(fib))
print(fib.send(2))
print(fib.send(2))
print(fib.send(2))
print(fib.send(2))

```





执行顺序如下：  
首先，创建生成器对象  
调用fib.send(None)方法，此处作用与next(fib)相同，程序返回当前b的值1， 程序中断。  
调用fib.send(2)方法，程序被唤醒，将2传递给yield之前的变量sleep，程序继续运行，直到遇到yield将新的b返回，程序再次中断。  
如此继续下去，直到程序结束。




### yield from

前面的都是单一层次的生成器，并没有嵌套，如果是多个生成器嵌套会怎么样呢，下面是一个例子。

```
def fun_inner():
    i = 0
    while True:
        i = yield i

def fun_outer():
    a = 0
    b = 1
    inner = fun_inner()
    inner.send(None)
    while True:
        a = inner.send(b)
        b = yield a

if __name__ == '__main__':
    outer = fun_outer()
    outer.send(None)
    for i in range(5):
        print(outer.send(i))

```

![](https://images2017.cnblogs.com/blog/1203446/201709/1203446-20170913142714610-694085302.png)

在两层嵌套的情况下，值的传递方式是，先把值传递给外层生成器，外层生成器再将值传递给外层生成器，内层生成器在将值反向传递给外层生成器，最终yield出结果。如果嵌套的层次更多，传递将会越麻烦。

下面是yield from的实现方式：

```
def fun_inner():
    i = 0
    while True:
        i = yield i

def fun_outer():
    yield from fun_inner()

if __name__ == '__main__':
    outer = fun_outer()
    outer.send(None)
    for i in range(5):
        print(outer.send(i))

```


效果是一样的，但是明显的代码量减少了，嵌套传值的时候，并不需要我们手动实现。



yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁，结构更加清晰。  

来源地址：https://www.php.cn/python-tutorials-458439.html  









