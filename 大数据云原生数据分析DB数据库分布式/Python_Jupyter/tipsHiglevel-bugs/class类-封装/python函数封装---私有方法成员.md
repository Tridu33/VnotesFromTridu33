[TOC]

# 1. python私有方法成员





默认情况下，Python中的成员变量和方法都是public的，而Python中没有类似public、private等访问修饰符控制访问权限。

如果要使用私有变量需要在变量名或者方法名前加上“\_\_”双划线。

这是一种name mangling技术，将\_membername替换成\_classname\_membername，是一种伪私有化方式。为了保证class之外访问私有变量，Python会在类的内部自动将我们定义的\_\_spam私有变量的名字替换为\_classname\_\_spam，所以在外部访问\_\_any的时候回提示找不到该变量。

不过Python中的私有变量和私有方法仍然是可以访问的，例如：

```
私有变量：实例._类名__变量名
私有方法：实例._类名__方法名()

_xxx 单下划线修饰的成员变量，表示只有类实例或者子类实例可以访问，类似于protect
__xxx 双下划线修饰的成员变量，表示只有类对象自己能访问，类似于private
__xxx__ 系统定义名字，表示特殊方法专用的标识，如__init__()，代表类的构造方法
```

----------------------------------------------------------------------------------------------------------




Python函数之封装【private】https://blog.csdn.net/qq_41395729/article/details/111665601

非常全面

### 1.1.1. 一、封装【private】

#### 1.1.1.1. 1.概念

> 广义的封装：函数和类的定义本身，就是封装的体现
>
> 狭义的封装：一个类的某些属性，在使用的过程 中，不希望被外界直接访问，而是把这个属性给作为私有的【只有当前类持有】，然后暴露给外界一个访问的方法即可【间接访问属性】
>
> 封装的本质：就是属性私有化的过程
>
> 封装的好处：提高了数据的安全性，提高了数据的复用性

#### 1.1.1.2. 2.属性私有化

> 如果想让成员变量不被外界直接访问，则可以在属性名称的前面添加两个下划线__,成员变量则被称为私有成员变量
>
> 私有属性的特点：只能在类的内部直接被访问，在外界不能直接访问
>
> 代码演示：

```python
#1.属性不私有化的时候
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myPrint(self):
        print(self.name,self.age)

#通过构造函数给属性赋值
per = Person("张三",10)
per.myPrint()   #张三 10
#通过对象直接访问属性，并且给属性赋值
per.name = "李四"
per.age = 22
per.myPrint()   #李四 22

#2.属性私有化
#写法：在属性的前面添加两个下划线
#用法：只能在类的内部被访问，外界不能直接访问
class Person1():
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def myPrint(self):
        print(self.name,self.__age)

p1 = Person1("abc",10)
p1.myPrint()   #abc 10
p1.name = "hello"
#其实动态绑定属性，age和__age其实是两个不同的变量
p1.age = 222
p1.myPrint()
print(p1.age)

#AttributeError: 'Person1' object has no attribute '__age',私有化了，在外界不能直接访问
#print(p1.__age)

```

#### 1.1.1.3. 3.get函数和set函数

```python
#3.get函数和set函数
class Person2():
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        #特殊情况一
        self.__weight__ = 20.0
        #特殊情况二
        self._height = 155.0

    def myPrint(self):
        print(self.name,self.__age)

    # 书写私有属性age的get函数和set函数【通过自定义的函数进行私有属性的赋值和获取值，暴露给外界】
    """
    get函数和set函数并不是系统的函数，而是自定义的，为了和封装的概念相吻合，起名为getXxx和setXxx
    get函数：获取值
    set函数：赋值【传值】
    """
    #set函数:给成员变量赋值
    #命名方式：setXxx
    #特点：需要设置参数，参数和私有成员变量有关
    def setAge(self,age):
        #数据的过滤
        if age < 0:
            age = 0
        self.__age = age
    #get函数：获取成员变量的值
    #命名方式：getXxx
    #特点：需要设置返回值，将成员变量的值返回
    def getAge(self):
        return self.__age

    #注意：有几个私有属性，则书写几对get函数和set函数

p2 = Person2("abc",10)
p2.myPrint()   #abc 10
#print(p2.__age)
#间接的访问了私有的成员变量
print(p2.getAge())
p2.setAge(22)
print(p2.getAge())

p2.setAge(-20)
print(p2.getAge())

#总结：通过将属性私有化之后，然后提供get函数和set函数，外部代码就不能随意更改成员变量的值，这样在一定程度上保证了数据的安全性

#4.工作原理【了解】
#当编译器加载了程序之后，不能直接访问p2.__age,Python解释器把__age解释成_Person2__age
#p2.__age = 100
p2._Person2__age = 100
print(p2.getAge())

#5.特殊情况：尽量不要直接访问
#a.在一个变量的前后各加两个下划线，在Python中被认为特殊成员变量，将不再属于私有变量
#print(p2.__weight__)
#b.特殊变量
#print(p2._height)

#面试题：下面变量的含义
"""
xxx:普通的变量
_xxx:受保护的变量，不建议使用这种形式
__xxx:表示私有的，外界无法直接访问，只能通过暴露给外界的函数访问
__xxxx__：一般是系统的内置变量，比如：__name__,__solts__,自定义标识符的时候尽量不要使用这种形式
"""

```



#### 1.1.1.4. 4.@property装饰器


```python
class Person1():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def myPrint(self):
        print(self.__name,self.__age)

    """
   def setAge(self,age):
        #数据的过滤
        if age < 0:
            age = 0
        self.__age = age

    def getAge(self):
        return self.__age
    """

    #注意：函数的命名方式：变量的名称
    #作用：相当于get函数，设置返回值，将成员变量的值返回
    @property
    def age(self):
        return  self.__age

    #注意：函数的命名方式：需要和@property中函数的命名保持一致
    #作用：相当于set函数,设置参数，给成员变量赋值
    @age.setter
    def age(self,age):
        if age < 0:
            age = 0
        self.__age = age

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self,name):
        self.__name = name


p1 = Person1("abc",10)
p1.myPrint()   #abc 10
#p1.setAge(20)
#print(p1.getAge())

print(p1.age)  #10
p1.age = 18   #相当于调用了set函数，将18传值，实质调用的是@age.setter修饰的函数
print(p1.age) #相当于调用了get函数，将成员变量的值获取出来，实质调用的是@peoperty修饰的函数

p1.name = "zhangsan"
print(p1.name)

```



#### 1.1.1.5. 5.私有方法


```python
class Site():
    def __init__(self,name):
        self.name = name

    def who(self):
        print(self.name)
        self.__foo()

    #私有成员方法，只能在当前类的内部内调用
    def __foo(self):    #私有函数
        print("foo")

    def foo(self):    #公开函数
        print("foo~~~~")

    #注意：以上两个函数是两个不同的函数，不存在覆盖的问题

s = Site("千锋")
s.who()
#s.__foo()  #AttributeError: 'Site' object has no attribute 'foo'
s.foo()

```

#### 1.1.1.6. 2.单继承

##### 1.1.1.6.1. 2.1使用

简单来说，一个子类只能有一个父类，被称为单继承

语法：

父类：

class 父类类名(object):

 类体【所有子类公共的部分】

子类：

class 子类类名（父类类名）:

 类体【子类特有的属性和成员方法】

说明：一般情况下，如果一个类没有显式的指明父类，则统统书写为object

代码演示：

person.py文件【父类】


```python
#1.定义父类
class Person(object):
    #构造函数【成员变量】
    def __init__(self,name,age):
        self.name = name
        self.age = age


    #成员方法
    def show(self):
        print("show")

    def __fun(self):
        print("fun")

```

worker.py文件【子类1】


```python
from  extends01.person import Person

#2.定义子类
class Worker(Person):
    #构造函数【成员变量】
    def __init__(self,name,age,job):
        """
        self.name = name
        self.age = age
        """
        self.job = job

        #6.在子类的构造函数中调用父类的构造函数【从父类中继承父类中的成员变量】
        #方式一：super(当前子类，self).__init__(属性列表)
        #super(Worker, self).__init__(name,age)
        #方式二：父类名.__init__(self,属性列表)
        Person.__init__(self,name,age)
        #方式三：super().__init__(属性列表)
        #super().__init__(name,age)


    #成员方法
    def work(self):
        print("work")

```

student.py文件【子类2】


```python
from extends01.person import  Person

class Student(Person):
    # 构造函数【成员变量】
    def __init__(self, name, age, score):

        Person.__init__(self,name,age)
        self.score = score

    # 成员方法
    def study(self):
        print("study")

```

extendsDemo01.py文件【测试模块】


```python
#测试模块
from extends01.person import Person
from extends01.worker import Worker
from extends01.student import Student

#3.创建父类的对象
p = Person("zhangsan",10)
p.show()
#p.__fun()

#4.创建子类的对象
w = Worker("aaa",20,"工人")
w.work()

#5.子类对象访问父类中的内容
#结论一：子类对象可以调用父类中的公开的成员方法【因为继承，私有方法除外】
w.show()
#w.__fun()
#结论二：通过在子类的构造函数中调用父类的构造函数，子类对象可以直接访问父类中的成员变量【私有变量除外】
print(w.name,w.age,w.job)

s = Student("小明",9,90)
s.study()
s.show()

```

---------------------------------------


```python
#6.子类中出现一个和父类同名的成员函数,则优先调用子类中的成员函数
#子类的成员函数覆盖了父类中的同名的成员函数
s = Student("小明",9,90)
s.study()
s.show()

#7.父类对象能不能访问子类中特有的成员函数和成员变量？----->不能
per = Person("gs",10)
#per.work()

```

总结：

继承的特点：

 a.子类对象可以直接访问父类中非私有化的属性

 b.子类对象可以调用父类中非私有化的成员方法

 c.父类对象不能访问或者调用子类 中任意的内容

继承的优缺点：

优点：

 a.简化代码，减少代码的冗余

 b.提高代码的复用性

 c.提高了代码的可维护性

 d.继承是多态的前提

缺点：

 通常使用耦合性来描述类与类之间的关系，耦合性越低，则说明代码的质量越高

 但是，在继承关系中，耦合性相对较高【如果修改父类，则子类也会随着发生改变】



#### 1.1.1.7. 多继承

> 一个子类可以有多个父类
>
> 语法：
>
> class 子类类名(父类1，父类2，父类3.。。。)：
>
>  类体
>
> 代码演示：
>
> father.py文件【父类1】


```python
class Father(object):
    def __init__(self,money):
        self.money = money

    def play(self):
        print("playing")

    def fun(self):
        print("father中的fun")

```

mother.py文件【父类2】




```python
class Mother(object):
    def __init__(self,faceValue):
        self.faceValue = faceValue

    def eat(self):
        print("eating")

    def fun(self):
        print("mother中的fun")

```

child.py文件【子类】


```python
from extends02.father import Father
from extends02.mother import Mother

#定义子类，有多个父类
class Child(Mother,Father):
    def __init__(self,money,faceValue,hobby):
        #调用父类中的构造函数
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)
        self.hobby = hobby

    def study(self):
        print("study")

```

extendsDemo03.py文件【测试模块】


```python
from extends02.father import Father
from extends02.mother import Mother
from extends02.child import Child


f = Father(100000)
m = Mother(3.0)

#创建子类对象
c = Child(1000,3.0,"打游戏")
#子类对象调用父类中的成员方法
c.play()
c.eat()

#结论;如果多个父类中有相同的函数，通过子类的对象调用，调用的是哪个父类中的函数取决于在父类列表中出现的先后顺序
c.fun()

```

#### 1.1.1.8. 函数重写【override】

> 在子类中出现和父类同名的函数，则认为该函数是对父类中函数的重写


```python
class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #重写__str__函数,重写之后一般return一个字符串，有关于成员变量
    def __str__(self):
        return "name=%s age=%d"%(self.name,self.age)

    #重写__repr__,作用和str是相同的，优先使用str
    def __repr__(self):
        return "name=%s age=%d"%(self.name,self.age)

a = Animal("大黄",10)
print(a)   #<__main__.Animal object at 0x00000226A87AC240>
print(a.__str__())

#当一个类继承自object的时候，打印对象获取的是对象的地址，等同于通过子类对象调用父类中__str__
#当打印对象的时候，默认调用了__str__函数
#重写__str__的作用：为了调试程序

"""
总结：【面试题】
a.__str__和__repr__都未被重写的时候，使用对象调用的是__str__,此时__str__返回的是对象的地址
b.__str__和__repr__都被重写之后，使用对象调用的是__str__，此时__str__返回的是自定义的字符串
c.重写了__str__，但是没有重写__repr__，则使用对象调用的是__str__，此时__str__返回的是自定义的字符串
d.未重写__str__，但是重写了__repr__，则使用对象调用的是__repr__,此时，__repr__返回的是自定义的字符串
"""

#使用时机：当一个对象的属性有很多的时候，并且都需要打印，则可以重写__str__，可以简化代码，调试程序

```

##### 1.1.1.8.1. 自定义函数重写


```python
#函数重写的时机：在继承关系中，如果父类中函数的功能满足不了子类的需求，则在子类中需要重写
#父类
class People(object):
    def __init__(self,name):
        self.name = name

    def fun(self):
        print("fun")

#子类
class Student(People):
    def __init__(self,name,score):
        self.score = score
        super(Student,self).__init__(name)

    #重写;将函数的声明和实现重新写一遍
    def fun(self):
        #在子类函数中调用父类中的函数【1.想使用父类中的功能，2.需要添加新的功能】
        #根据具体的需求决定需不需要调用父类中的函数
        super(Student,self).fun()
        print("fajfhak")


s = Student("fhafh",10)
s.fun()

```

### 1.1.2. 多态【了解】重载重写



    重载：函数名相同，函数的参数个数、参数类型或参数顺序三者中必须至少有一种不同。函数返回值的类型可以相同，也可以不相同。发生在一个类内部，不能跨作用域。

    重定义：也叫做隐藏，子类重新定义父类中有相同名称的非虚函数 ( 参数列表可以不同 ) ，指派生类的函数屏蔽了与其同名的基类函数。可以理解成发生在继承中的重载。

    重写：也叫做覆盖，一般发生在子类和父类继承关系之间。子类重新定义父类中有相同名称和参数的虚函数。(override)

https://www.artima.com/weblogs/viewpost.jsp?thread=101605

用classmethod实现类似构造函数重载 https://www.zhihu.com/question/20053359/answer/231134480
```python
class Overloading(object):
    def __init__(self, x):
        self.x = x

    @classmethod
    def NewInit(cls, x, y):
        b = cls(x*y)
        b.z = x - y
        return b

a = Overloading(4)
b = Overloading.NewInit(4,5)

```



@staticmethod和@classmethod的作用与区别
http://www.python-china.com/html/140.html





一种事物的多种体现形式，函数的重写其实就是多态的一种体现

在Python中，多态指的是父类的引用指向子类的对象




```python
#父类
class Animal(object):
 	pass

#子类
class Dog(Animal):
 	pass

class Cat(Animal):
 	pass

#定义变量
a = []   #a是list类型
b = Animal()  #b是Animal类型
c = Cat()  #c是Cat类型

#isinstance():判断一个对象是否属于某种类型【系统还是自定义的类型】
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Cat))

print(isinstance(c,Animal))  #True
print(isinstance(b,Dog))   #False

#结论：子类对象可以是父类类型，但是，父类的对象不能是子类类型

```

类方法：使用@classmethod装饰器修饰的方法，被称为类方法，可以通过类名调用，也可以通过对象调用，但是一般情况下使用类名调用

静态方法：使用@staticmethod装饰器修饰的方法，被称为静态方法，可以通过类名调用，也可以通过对象调用，但是一般情况下使用类名调用


```python
class Test(object):
 #1.类属性
 age = 100

 def __init__(self,name):
     #2.实例属性
     self.name = name

 #3.成员方法,通过对象调用
 #必须有一个参数，这个参数一般情况下为self，self代表是当前对象
 def func(self):
     print("func")

 #4.类方法
 """
 a.必须有一个参数，这个参数一般情况下为cls，cls代表的是当前类
 b.类方法是属于整个类的，并不是属于某个具体的对象，在类方法中禁止出现self
 c.在类方法的内部，可以直接通过cls调用当前类中的属性和方法
 d.在类方法的内部，可以通过cls创建对象
 """
 @classmethod
 def test(cls):
     print("类方法")
     print(cls)   #<class 'methodDemo01.Test'>
     print(cls.age)

     #6
     #注意：cls完全当做当前类使用
     c = cls("hello")
     c.func()

 #7.静态方法
 @staticmethod
 def show():
     print("静态方法")

t = Test("hjfsh")
t.func()

#5,.调用类方法
Test.test()   #类名.类方法的名称()
t.test()       #对象.类方法的名称()

#7。调用静态方法
Test.show()
t.show()

```

总结：实例方法【成员方法】、类方法以及静态方法之间的区别

a.语法上

 实例方法：第一个参数一般为self，在调用的时候不需要传参，代表的是当前对象【实例】

 静态方法：没有特殊要求

 类方法：第一个参数必须为cls，代表的是当前类

b.在调用上

 实例方法：只能对象

 静态方法：对象 或者 类

 类方法：对象 或者 类

c.在继承上【相同点】

 实例方法、静态方法、类方法：当子类中出现和父类中重名的函数的时候，子类对象调用的是子类中的方法【重写】


```python
class SuperClass(object):
 @staticmethod
 def show():
     print("父类中的静态方法")

 @classmethod
 def check(cls):
     print("父类中的类方法")

class SubClass(SuperClass):
 pass

s = SubClass()
s.show()
s.check()

```

注意：注意区分三种函数的书写形式，在使用，没有绝对的区分



### 1.1.3. 类中的常用属性


```python
__name__
	通过类名访问，获取类名字符串
	不能通过对象访问，否则报错
	
__dict__
	通过类名访问，获取指定类的信息【类方法，静态方法，成员方法】，返回的是一个字典
	通过对象访问，获取的该对象的信息【所有的属性和值】，，返回的是一个字典
	
__bases__
	通过类名访问，查看指定类的所有的父类【基类】

```



```python
class Animal(object):
 def __init__(self,arg):
     super(Animal, self).__init__()
     self.arg = arg


class Tiger(Animal):
 age = 100
 height = 200

 def __init__(self,name):
     #super(Tiger, self).__init__(name)
     self.name = name

 def haha(self):
     print("haha")

 @classmethod
 def test(cls):
     print("cls")

 @staticmethod
 def show():
     print("show")


if __name__ == "__main__":

 #1.__name__
 print(Tiger.__name__)  #Tiger

 t = Tiger("")
 #print(t.__name__)  #AttributeError: 'Tiger' object has no attribute '__name__'

 #2.__dict__
 print(Tiger.__dict__)  #类属性，所有的方法
 print(t.__dict__)   #实例属性

 #3.__bases__，获取指定类的所有的父类，返回的是一个元组
 print(Tiger.__bases__)

```

### 1.1.4. 单例设计模式【扩展】


实际应用：数据库连接池操作-----》应用程序中多处需要连接到数据库------》只需要创建一个连接池即可，避免资源的浪费


```python
class Singleton(object):
 #类属性
 instance = None

 #类方法
 @classmethod
 def __new__(cls, *args, **kwargs):
     #如果instance的值不为None，说明已经被实例化了，则直接返回；如果为NOne，则需要被实例化
     if not cls.instance:
         cls.instance = super().__new__(cls)

     return cls.instance

class MyClass(Singleton):
 pass

#当创建对象的时候自动被调用
one = MyClass()
two = MyClass()

print(id(one))
print(id(two))

print(one is two)

```

