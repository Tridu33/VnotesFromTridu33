https://www.w3schools.com/python/python_regex.asp


[https://blog.csdn.net/qq_32113189/article/details/80969179](https://blog.csdn.net/qq_32113189/article/details/80969179)






莫烦正则表达式
[https://morvanzhou.github.io/tutorials/python-basic/basic/13-10-regular-expression/](https://morvanzhou.github.io/tutorials/python-basic/basic/13-10-regular-expression/)






# 1. 字符串处理和regex正则表达式

整理笔记和网页uri必须用到的regex


[https://www.cnblogs.com/songqingbo/p/5126957.html](https://www.cnblogs.com/songqingbo/p/5126957.html)





字符串的常用操作包括但不限于以下操作：

```
字符串的替换、删除、截取、复制、连接、比较、查找、分割等
```

这里将对字符串的内置操作方法进行总结归纳，重点是以示例的方式进行展示。

```
使用type获取创建对象的类 type(name)
使用dir获取类的成员dir(name)
使用vars获取类的成员和各个成员的值
```

**capitalize**

```
	功能：字符串首字母大写
	name = 'swhthaitun'
	name.capitalize()
	返回结果：'Swht'
```

**casefold()首字母小写**

```
	name = 'HelloWord'
	reault = name.casefold()
	print(reault)
	返回结果：helloword
```

**casefold**

```
    功能：将字符串中所有的大写字母转换成小写字母
    s1 = "['bsondump', 'mongo', 'mongod', 'mongodump', 'mongoexport', 'mongofiles', 'mongoimport', 'mongooplog', 'mongoperf', 'mongoLLKJKKore', 'mongos', 'UUUngostat', 'monGGtop']"
    s1.casefold()
    返回结果："['bsondump', 'mongo', 'mongod', 'mongodump', 'mongoexport', 'mongofiles', 'mongoimport', 'mongooplog', 'mongoperf', 'mongollkjkkore', 'mongos', 'uuungostat', 'monggtop']"
```

**center**

```
	功能：字符串宽度填充，使用原有字符串+填充字符构成指定长度的新的字符串
	name = 'swhthaitun'
	name.center(15)
	返回结果：'   swhthaitun  ' #默认以空格进行填充
	name.center(16,'*')
	返回结果：'***swhthaitun***'

	功能：字符串居中，以‘*’分割(20为新产生字符串的总的宽度)
	name = 'HelloWord'
	reault = name.center(20,'*')
	print(reault)
	返回结果：*****HelloWord******
```

**count**

```
	功能：统计某个字符在字符串中出现的次数，或在字符串指定区间内完成上述操作
	name = 'swhthaitun'
	name.count('h')
	返回结果：2
	name.count('h',0,3)  #从索引值0-3范围的字符中统计'h'出现的次数
	返回结果：1

	功能：统计子序列出现的次数
	name = 'HelloWord'
	reault = name.count('W') #如果换成'w'，返回结果为0，python对大小写敏感
	print(reault)
	返回结果：1

	name = 'HelloWord'
	reault = name.count('l',0,3) #统计单个字符出现的次数,可以指定起始范围,另外在python中起始范围讲究顾头不顾尾的原则，即[0,3)
	print(reault)
```

**encode**

```
	功能：对字符串进行编码操作
	name = 'swhthaitun'
	name.encode()
	返回结果：b'swhthaitun'

	功能：转变字符串的编码
	name = '南非波波'
	reault = name.encode('gbk')
	print(reault)
	返回结果：b'\xc4\xcf\xb7\xc7\xb2\xa8\xb2\xa8'
```

**endswith**

```
	功能：判断字符串是否以某个字符串结尾的，返回值为bool型
	name = 'swhthaitun'
	name.endswith('s')
	返回结果：False
	name.endswith('n')
	返回结果：True
	name.endswith('tun')
	返回结果：True

	name = 'Iamalatterboy'
	reault = name.endswith('y')
	print(reault)
	返回结果：True
```

**expandtabs**

```
	功能：将制表符'\t'转换成指定宽度的tab键分割，默认tabsize=8
	li = 'sw\tht'
	li.expandtabs(4)
	返回结果：'sw  ht'
	li.expandtabs()
	返回结果：'sw      ht'
```

**find**

```
	功能：在字符串中查找指定字符串，找不到时返回-1
	name = 'swht'
	name.find('s')
	返回结果：0
	name.find('h')
	返回结果：2
```

**format**

```
	功能：格式化输出字符串
	li = 'I\'m {},{}' #两个'{}'是占位符
	li.format('swht','欢迎来中国')
	返回结果："I'm swht,欢迎来中国"
	参考：http://blog.chinaunix.net/uid-23802873-id-4477364.html
```

_*contains*_

```
	功能：包含 -->'eal' in name
	name = 'swhtkkskjj'
	reault = name.__contains__('swht')
	print(reault)
	返回结果：True
```

**index**

```
	功能：在字符串中查找指定的字符串,找不到时直接报错
	name = 'swhthaitun'
	name.index('w')
	返回结果：1	
```

**join()**

```
	功能：字符串连接
	name = 'swhthaitun'
	'*'.join(name)
	返回结果：'s*w*h*t*h*a*i*t*u*n'
```

**isalnum**

```
	功能：检查判断字符串是否包含字母数字字符（http://www.yiibai.com/python/string_isalnum.html）
	name = 'swhthaitun'
	name.isalnum()
	返回结果：True
```

**isalpha**

```
	功能：检测字符串是否只由字母组成（http://www.runoob.com/python/att-string-isalpha.html）
	name = 'swhthaitun'
	name.isalpha()
	返回结果：True
```

**isdecimal**

```
	功能：检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。（参考：http://www.runoob.com/python/att-string-isdecimal.html）
	name = 'swhthaitun'
	name.isdecimal()
	返回结果：False
```

**isdigit**

```
	功能：检测字符串是否只由数字组成。(参考:http://www.runoob.com/python/att-string-isdigit.html)
	name = 'swhthaitun'
	name.isdigit()
	返回结果：False
```

**isidentifier**

```
	功能：检测字符串是否是字母开头
	name = 'swhthaitun'
	name.isidentifier()
	返回结果：True
	name = '1swhthaitun'
	name.isidentifier()
	返回结果：False
```

**isnumeric**

```
	功能：检测字符串是否只由数字组成。这种方法是只针对unicode对象。
	name = 'swhthaitun'
	name.isnumeric()
	返回结果：False
	Li = '5523'
	Li.isnumeric()
	返回结果：True
```

**isprintable**

```
	功能：判断字符串中所有字符是否都属于可见字符
	a = "\tPuppy"
	a.isprintable()
	返回结果：False
	name = 'swhthaitun'
	name.isprintable()
	返回结果：True
```

**isspace**

```
	功能：检测字符串是否为空格
	name = 'swhthaitun'
	name.isspace()
	返回结果：False
	Li = ' '
	Li.isspace()
	返回结果：True
```

**istitle**

```
	功能：判断字符串是否适合当作标题（其实就是每个单词首字母大写）
	a = "a puppy"
	b = "Puppy"
	a.istitle()
	返回结果：False
	b.istitle()
	返回结果：True
```

**isupper**

```
	功能：判断字符串中所有字母字符是否都是大写字母
	a = "puppy"
	b = "PUPPY"
	a.isupper()
	返回结果：False
	b.isupper()
	返回结果：True
```

**ljust**

```
	功能：返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。（参考：http://www.runoob.com/python/att-string-ljust.html）
	语法：str.ljust(width[, fillchar])
		 width -- 指定字符串长度。
		 fillchar -- 填充字符，默认为空格。
	name = 'swhthaitun'
	name.ljust(50,'*')
	返回结果：'swhthaitun****************************************'
```

**lower**

```
	功能：将所有的字母转换成小写字母
	name = 'SWHT'
	name.lower()
	返回结果：'swht'
```

**lstrip**

```
	功能：去除字符串左边开头的空格
	name = '  swht   '
	name.lstrip()
	返回结果：'swht   '
```

**rstrip**

```
	功能：去除字符串右边结尾的空格
	name = '  swht   '
	name.rstrip()
	返回结果：'   swht'
```

**strip**

```
	功能：去除字符串两边的空格
	name = '  swht   '
	name.rstrip()
	返回结果：'swht'
```

**maketrans**

```
	功能：用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
	注：两个字符串的长度必须相同，为一一对应的关系。
	语法：str.maketrans(intab, outtab)
	参数：intab -- 字符串中要替代的字符组成的字符串。
		  outtab -- 相应的映射字符的字符串。
	intab = "swhtr"
	outtab = "12345"
	name = "hjjksknsnjmk"
	name.maketrans(intab, outtab)
	返回结果：{104: 51, 114: 53, 115: 49, 116: 52, 119: 50}
```

**partition**

```
	功能：根据指定的分隔符将字符串进行分割。
		如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
	name = 'swht'
	li = 'hhsslswhtolljm'
	li.partition(name)
	返回结果：('hhssl', 'swht', 'olljm')
```

**replace**

```
	功能：把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
	语法：str.replace(old, new[, max])
	参数：old -- 将被替换的子字符串。
		 new -- 新字符串，用于替换old子字符串。
		 max -- 可选字符串, 替换不超过 max 次
	str = "this is string example....wow!!! this is really string"
	str.replace("is", "was")
	返回结果：'thwas was string example....wow!!! thwas was really string'
	str.replace("is", "was", 3)
	返回结果：'thwas was string example....wow!!! thwas is really string'
```

**split**

```
	功能：字符串分割，默认是空格
	name.split()
	返回结果：['swht']
	name.split('s') #以's'字符进行分割
	返回结果：['', 'wht']
```

**_\*add\*_**

```
	功能：在字符串后面增加指定的字符或字符串
	name = 'swht'
	name.__add__('e')
	返回结果：'swhte'
	li = 'hjh'
	name.__add__(li)
	返回结果：'swhthjh'
```

**contains**

```
	功能：判断指定字符串是否包含在字符串中,返回值为True和False
	name = 'swht'
	name.__contains__('s')
	返回结果：True
```

**eq**

```
	功能：判断字符串是否相等，返回值为True和False
	name = 'swht'
	li = 'test'
	name.__eq__(li)
	返回结果：False
```



























