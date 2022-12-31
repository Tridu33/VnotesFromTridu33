[TOC]

#  Python内核下magic code曲线救国jupyter-haskell
第一选择：IHaskell插件kernel
https://github.com/gibiansky/IHaskell

[IHaskell笔记](https://nbviewer.jupyter.org/github/gibiansky/IHaskell/blob/master/notebooks/IHaskell.ipynb)

在线浏览Haskell的api函数库

http://www.haskell.org/ghc/docs/latest/html/libraries

 [Haskell Report](http://www.haskell.org/onlinereport/literate.html)
 


推荐的方法是 [WSl](https://docs.microsoft.com/en-us/windows/wsl/install-win10)下的linux运行jupyter服务器，安装这个



但是真的网络又卡，又想一边用python3临时用一下haskell还想写markdown，觉得wsl路径切换麻烦啦,wsl不想装太多python环境，想省点空间大部分装在windows主系统下的conda环境......各种千奇百怪的理由，不妨试试**曲线救国**，选择用下面这种low招儿？

## 命令行
前提是ghci能在cmd运行：

```
C:\Users\admin>ghci
GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
Prelude> :q
Leaving GHCi.

```


```python
%%script ghci
putStrLn "Hello world!"
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> Hello world!
    Prelude> Leaving GHCi.


## 写入文本文件或者更新编辑文件


```python
%%writefile tmp.hs
module Tmp where
main = putStr "Hello World!"
```

    Writing tmp.hs
    

## 加载hs在ghci运行文件


```python
%%script ghci
:load tmp.hs
main
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Tmp              ( tmp.hs, interpreted )
    Ok, one module loaded.
    *Tmp> Hello World!*Tmp> Leaving GHCi.


## 查看文件内容


```python
!more tmp.hs
```

    module Tmp where
    main = putStr "Hello World!"
    

## compiler文件exe


```python
%%cmd
ghc -main-is Tmp tmp.hs -o tmp-executive.exe
```

    Microsoft Windows [Version 10.0.18362.1016]
    (c) 2019 Microsoft Corporation. All rights reserved.
    
    C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\Advanced-Data-Analysis-with-Haskell\tmp>ghc -main-is Tmp tmp.hs -o tmp-executive.exe
    [1 of 1] Compiling Tmp              ( tmp.hs, tmp.o )
    Linking tmp-executive.exe ...
    
    C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\Advanced-Data-Analysis-with-Haskell\tmp>


```python
%ls
```

     Volume in drive C has no label.
     Volume Serial Number is 32C5-E3BF
    
     Directory of C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\Advanced-Data-Analysis-with-Haskell\tmp
    
    08/23/2020  06:59 PM    <DIR>          .
    08/23/2020  06:59 PM    <DIR>          ..
    08/23/2020  06:58 PM    <DIR>          .ipynb_checkpoints
    08/23/2020  06:59 PM            23,688 IPythonMagicHaskellGHCi.ipynb
    08/23/2020  05:50 PM               193 lhs1.lhs
    08/23/2020  05:50 PM               189 lhs2.lhs
    08/23/2020  06:40 PM               401 lhs3.lhs
    08/23/2020  06:41 PM               401 lhs3-5.lhs
    08/23/2020  05:50 PM               436 lhs4.lhs
    08/23/2020  05:50 PM               288 lhs5.lhs
    08/23/2020  05:56 PM               249 lhs6.lhs
    08/23/2020  06:59 PM               835 tmp.hi
    08/23/2020  06:59 PM                48 tmp.hs
    08/23/2020  06:59 PM             2,321 tmp.o
    08/23/2020  06:59 PM        14,278,565 tmp-executive.exe
                  12 File(s)     14,307,614 bytes
                   3 Dir(s)   1,454,374,912 bytes free
    

## 执行exe文件


```python
%%cmd
tmp-executive.exe
```

    Microsoft Windows [Version 10.0.18362.1016]
    (c) 2019 Microsoft Corporation. All rights reserved.
    
    C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\Advanced-Data-Analysis-with-Haskell\tmp>tmp-executive.exe
    Hello World!
    C:\Users\admin\Documents\Tridu33\Py\jupyternotebook\Advanced-Data-Analysis-with-Haskell\tmp>

## 删除文本文件和中间辅助文件


```python
!rm tmp.hs 
```


```python
!rm tmp.o 
!rm tmp.hi
!rm tmp-executive.exe
```

# LHS literate programming

Haskell是提供本地功能以支持识字编程的少数语言之一。
在haskell中，一个识字程序是后缀.lhs而不是.hs的程序。
在具有读写能力的Haskell程序中，有两种方法可以区分代码部分和非代码部分。
您可以在所有代码前面加上>（bird 样式），也可以在代码行之间用\ begin {code}和\ end {code}对（latex样式）括起来。
对于那些了解，使用和喜爱latex的人，建议使用后者。
请注意，Happy也通过.ly文件中的bird样式（>标记）支持识字编程。
可悲的是，Alex不再这样做。
您可能会考虑将noweb与它一起使用。


## 写入文本

这风格是由Richard **Bird**（因此得名）和Philip Wadler提出的。

所有以“>”开头的行均被解释为代码，其他所有内容均视为注释。

另一个要求是，您必须始终在代码块之前和之后保留空白行：在Bird样式中，您必须在代码之前保留空白。


```python
%%writefile lhs1.lhs
In Bird-style you have to leave a blank before the code.

> fact :: Integer -> Integer
> fact 0 = 1
> fact n = n * fact (n-1)

And you have to leave a blank line after the code as well.
```

    Overwriting lhs1.lhs
    

而且您还必须在代码后留空行。
该限制背后的想法是捕获未在行首插入'>`标记的错误。

通常，这不仅是一种好习惯，而且还是一种使代码更具可读性的格式。
但是，在某些情况下，您可能想绕开此限制。

也许您是在非Latex的标记语言中编写Haskell代码的，并且可能必须用等效于\\ begin {code}和\ end {code}的内容来包围代码。

在这种情况下，GHC提供了可用于lift（消散）空白行要求的标志：

```
$ ghc -optL -q
```


```python
%%script ghci
:load lhs1.lhs
fact 3
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs1.lhs, interpreted )
    Ok, one module loaded.
    *Main> 6
    *Main> Leaving GHCi.



```python
%%writefile lhs2.lhs
In Bird-style you have to leave a blank before the code.
> fact :: Integer -> Integer
> fact 0 = 1
> fact n = n * fact (n-1)
And you have to leave a blank line after the code as well.
```

    Overwriting lhs2.lhs
    


```python
%%script ghci -optL -q
:load lhs2.lhs
fact 3
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs2.lhs, interpreted )
    Ok, one module loaded.
    *Main> 6
    *Main> Leaving GHCi.


不加标志会报错：


```python
%%script ghci
:load lhs2.lhs
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> > Leaving GHCi.


    lhs2.lhs line 2: unlit: Program line next to comment
    lhs2.lhs line 4: unlit: Program line next to comment
    `unlit.exe' failed in phase `Literate pre-processor'. (Exit code: 1)


## Latex suggestions for literate programming


```python
%%writefile lhs3.lhs
In LaTex-style you have to leave a blank before the code.

\begin{code}
tsort []     = []
tsort (x:xs) = tsort [y | y<-xs, y>x] ++ [x] ++ tsort [y | y<-xs, y<=x]
\end{code}

The advantage: Source code and documentation are consistent!
    
The code environment is understood by Haskell compilers, so you can run your documentation files directly.
```

    Overwriting lhs3.lhs
    


```python
%%script ghci
:load lhs3.lhs
tsort [1,4,3,6]
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs3.lhs, interpreted )
    Ok, one module loaded.
    *Main> [6,4,3,1]
    *Main> Leaving GHCi.



```python
%%writefile lhs3-5.lhs
In LaTex-style you have to leave a blank before the code.

\begin{code}
tsort []     = []
\end{code}

试试分开

\begin{code}
tsort (x:xs) = tsort [y | y<-xs, y>x] ++ [x] ++ tsort [y | y<-xs, y<=x]
\end{code}

The advantage: Source code and documentation are consistent!
    
The code environment is understood by Haskell compilers, so you can run your documentation files directly.
```

    Overwriting lhs3-5.lhs
    


```python
%%script ghci
:load lhs3-5.lhs
tsort [1,4,3,6]
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs3-5.lhs, interpreted )
    Ok, one module loaded.
    *Main> [6,4,3,1]
    *Main> Leaving GHCi.


## Hiding code from Haskell


```python
%%writefile lhs4.lhs
And the definition of the following function would totally screw up my program, so I'm not definining it:

\begin{code} % this is not really code
main :: IO ()
main = print "this is not really code"
\end{code}

尽管这代码在vanilla  LaTeX运行效果很好，如果您使用的是lhs2TeX，那么您将在输出中得到打印“％this is not实际上code”的信息。

我不是安装的vanilla  LaTeX，会报错。
```

    Overwriting lhs4.lhs
    


```python
%%script ghci
:load lhs4.lhs
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> > Leaving GHCi.


    lhs4.lhs line 6: unlit: spurious \end{code}
    
    lhs4.lhs line 11: unlit: No definitions in file (perhaps you forgot the '>'s?)
    `unlit.exe' failed in phase `Literate pre-processor'. (Exit code: 1)



```python
%%writefile lhs5.lhs
第一个是main代码:

\begin{code}
main :: IO ()
main = print "this is really code"
\end{code}

Neither of the following definitions are really code:

\begin{spec}
main :: IO ()
main = print "another example"
\end{spec}

< main :: IO ()
< main = print "...and another"
```

    Overwriting lhs5.lhs
    


```python
%%script ghci
:load lhs5.lhs
main
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs5.lhs, interpreted )
    Ok, one module loaded.
    *Main> "this is really code"
    *Main> Leaving GHCi.


## 反正不识别latex,标签粘过来也无所谓


```python
%%writefile lhs6.lhs
\documentstyle{article}

\begin{document}

\section{Introduction}

This is a trivial program that prints the first 5 factorials.

\begin{code}
main :: IO ()
main =  print [ (n, product [1..n]) | n <- [1..5]]
\end{code}

\end{document}
```

    Overwriting lhs6.lhs
    


```python
%%script ghci
:load lhs6.lhs
main
```

    GHCi, version 8.6.3: http://www.haskell.org/ghc/  :? for help
    Prelude> [1 of 1] Compiling Main             ( lhs6.lhs, interpreted )
    Ok, one module loaded.
    *Main> [(1,1),(2,2),(3,6),(4,24),(5,120)]
    *Main> Leaving GHCi.




# 两个工具

- [lhs2tex](https://github.com/kosmikus/lhs2tex)工具，

看这里：http://www.andresloeh.de/lhs2tex

literate programming部分翻译这里的:https://wiki.haskell.org/Literate_programming

张淞说：

>使用.lhs文件书写代码的优点很明显。函数式编程的代码往往蕴含了编写者很大的思考量，需要用大段的注释进行解释说明，而代码又不是特别长，这个时候用.lhs最好不过了—哪部分是代码、哪部分是注释一目了然，还能生成.pdf文件方便阅读与传播。
但是，当不需要多行注释还有生成文档的时候就可以用扩展名为.hs的文件。

>.hs文件里全局的函数要起头写，不可以有其他字符；
单行的注释用两个减号（--）开头，多行注释用“{-”开头，以“-}”结尾。

- [pandoc](https://pandoc.org/MANUAL.html?source=post_page---------------------------#literate-haskell-support)


```
pandoc -f markdown+lhs -t html+lhs
```

```
pandoc -f markdown+lhs -t html
```

