




https://tikzit.github.io/


LaTeX—Tikz 宏包入门使用教程 - zdr0的文章 - 知乎 https://zhuanlan.zhihu.com/p/127155579
神经网络这种图有宏包 graph用，tikz还有wysiwyg编辑器 qtikz，ktikz挺不错，很多复杂的图 用inkscape或者geogebra 输出成tikz latex文件，再用tikzmark改改很舒服

# 1. tikz
如果你觉得还没看过瘾的话，可以到 [TikZ and PGF examples](https://link.zhihu.com/?target=http%3A//www.texample.net/tikz/examples/all/) 继续欣赏。

这么说吧，绝大多数**能够精确描述的矢量图**，理论上都可以用 TikZ 画出来。

（PS：我以前写过一篇（还没有写完的）文章，详细对比了不同作图工具的优劣，以及适用场景，见： [常见绘图工具的对比](https://link.zhihu.com/?target=https%3A//github.com/Hansimov/tikzpy/blob/master/doc/comparisons%2520of%2520tools.md)）

## 1.1. **TikZ 的名字由来**

TikZ 的德文原文是 TikZ ist kein Zeichenprogramm， 这是一个 "GNU's Not Unix!" 式的递归缩写。（是的，无聊的程序员们就是很喜欢这种文字游戏。）

翻译成英文就是 TikZ is not a drawing program，中文意思是“TikZ 不是一个绘图程序”。（程序员式冷幽默）

我在 [PGF/TikZ 中文手册](https://link.zhihu.com/?target=https%3A//github.com/Hansimov/pgfmanual-zh) 里将其译作“**绘何物为**”，用了拼音的递归：Huì hé wù wéi。意即“‘绘’是什么呢”，当然也可以将“绘”直接作为动词，理解成“绘制什么呢”。这样中文含义就和原文含义形成一问一答，无论是形式上还是内容上，都有了合理的对应。

当然，这里夹杂了我的私货，正文中依旧使用 TikZ 来指代这一绘图系统。

https://zhuanlan.zhihu.com/p/48300815

## 1.2. **PGF/TikZ 相关的学习资源**

PGF/TikZ 相关的学习资源很多，可以参考这个项目：[xiaohanyu/awesome-tikz](https://link.zhihu.com/?target=https%3A//github.com/xiaohanyu/awesome-tikz)。

基本列出了常见的高质资源，语言大多为英文。

中文资源相对零碎，社区用户也不够活跃，资源比较集中的地方有：

-   [Tikz&pgf - LaTeX 工作室](https://link.zhihu.com/?target=http%3A//www.latexstudio.net/archives/category/tex-graphics/tikz-example)：这里有不少基础教程、学习笔记和实用样例，质量也不错  
    
-   [CTEX 社区 - tikz/pgf 等 TeX 绘图宏包](https://link.zhihu.com/?target=http%3A//bbs.ctex.org/forum.php%3Fmod%3Dforumdisplay%26fid%3D51%26filter%3Dtypeid%26typeid%3D26)：如今已是死气沉沉，在质量上也明显不如上一个  
    

**如果你英文较好，或者对 PGF/TikZ 已经有了一定了解，建议还是参考英文资源，并且善用搜索引擎（Google Is Your Friend），选择合适的英文关键词。**

自然，我也在翻译 PGF/TikZ 的英文文档，项目地址在：[Hansimov/pgfmanual-zh](https://link.zhihu.com/?target=https%3A//github.com/Hansimov/pgfmanual-zh)。目前还在早期阶段。## **怎么用好这些学习资源**

虽然 [xiaohanyu/awesome-tikz](https://link.zhihu.com/?target=https%3A//github.com/xiaohanyu/awesome-tikz) 里面列出的链接非常详尽，不过我知道你们是懒得点进去看的。

资源在精不在多，所以我就提炼一下，选取比较重要的几个说一说：

-   英文文档：[pgfmanual](https://link.zhihu.com/?target=http%3A//mirrors.ctan.org/graphics/pgf/base/doc/pgfmanual.pdf)  
    
-   命令大全：[VisualTikZ](https://link.zhihu.com/?target=http%3A//mirrors.ctan.org/info/visualtikz/VisualTikZ.pdf)  
    
-   各种样例：[TikZ and PGF examples](https://link.zhihu.com/?target=http%3A//www.texample.net/tikz/examples/all/)  
    
-   TeX 社区：[Questions tagged \[tikz-pgf\]](https://link.zhihu.com/?target=https%3A//tex.stackexchange.com/questions/tagged/tikz-pgf)  
    

关于这些资源该怎么用，其实不同人需求不同，背景知识和学习能力也有差别，因此没有适用于所有人的方法。

**最重要的是兴趣。**比如我是手残党，画画写字都不行，所以非常依赖计算机帮我排版优美的文档和图表，因此在这方面的兴趣就非常浓厚，钻研得自然也就相对多一点。（我也想像那些大触一样，手绘各种好看的作品啊……）

**首先，如果能吃透近 1200 页的英文文档，我想你大概就神功大成（身败头秃）了。**Till Tantau 写的文档真的是深入浅出、巨细靡遗，我每次看都自叹弗如、望尘莫及。看文档当然不仅仅要看内容，还得看他是怎么组织的，而且有时候在文档的源代码里，也能学到各种眼前一亮的 LaTeX 技巧。当然，这个文档也可以当成字典来用，实用中碰到想不起来的，直接到文档的对应位置查阅即可。

除了 Till Tantau 写的文档之外，还有一个列在 CTAN 上的 PGF/TikZ 文档：[A very minimal introduction to TikZ](https://link.zhihu.com/?target=http%3A//cremeronline.com/LaTeX/minimaltikz.pdf)，能让你了解一下基本的命令，大概半小时就能读完。不过个人感觉这个文档并不出色，初学者看完发现自己顶多画个圆，可是教练我想画的明明是上面你列举的那些牛逼闪闪的图啊。然而既然 CTAN 上把这个文档列出来了，我也只好提一下以示尊重。

**其次，**[TeXample](https://zhuanlan.zhihu.com/p/48300815/(http://www.texample.net/tikz/examples/all/)) **上的各种样例值得反复观摩。**“凡操千曲而后晓声，观千剑而后识器；故圆照之象，务先博观”。一个是看 TikZ 能做到什么程度，二个是看那些大牛是怎么做到的。源码下载下来，先看看它画了啥，再跑一下看能不能跑通，然后再改一改，看看不同地方是做什么的，最后再试试能不能自己也画一个类似的。这跟书法和绘画中的临摹是一个道理。

**然后，是** [VisualTikZ](https://link.zhihu.com/?target=http%3A//mirrors.ctan.org/info/visualtikz/VisualTikZ.pdf)**。**它类似一个 cheatsheat，也就是命令清单，罗列了各种命令的各种用法和细节，比 Till Tantau 的文档更像一本字典。大概记得什么命令在文档的什么位置就好了。

**再者，是 TeX 社区上带有 tikz-pgf 标签的问题：**[Questions tagged \[tikz-pgf\]](https://link.zhihu.com/?target=https%3A//tex.stackexchange.com/questions/tagged/tikz-pgf)**。**目前这个 tag 下已经累计超过 2 万个问题了，也就是说，作为初学者，你碰到的绝大多数问题一定有人已经碰到过、并且解决掉了。如果你谷歌自己的问题，发现第一个弹出来的是 TeX - LaTeX Stack Exchange 或者简称 TeX.SX 里的链接，那么你的问题有九成的概率可以解决了。

顺便一提，没事可以浏览一些 Votes （投票）比较高的提问，因为这些是最常见的问题，也就意味着你碰见它们的概率也最高。然后 TeX.SX 里有好多大佬喜欢在问题的评论区回答，而不是直接写成答案，所以这些评论也是有必要都过一遍的。

**另外，就是善用搜索引擎。**真的，利人利己。这已经是老生常谈了。

当然，如果你确实没有搜到某个问题的答案，那么有两种可能：一是你没有搜索合适的关键词（九成概率），二是确实没人问过这个问题（一成概率）。这时不用顾虑和害羞，直接在 TeX.SX 上提问。一般情况下已经有类似问题了，这时会有大佬告诉你，你这个已经 duplicated （重复）了，然后甩给你一个连接，这时只要乖乖地点到对应连接学习就好了。如果真的没人碰到过这个问题，而且半天也没人回答，那么反思一下，这个问题是否是真实或合理的需求，对于这种非常边缘和比较个人的问题，要么把它扔在一旁，要么尝试自己动手解决。

关于如何提问，这里有一篇 [提问的智慧](https://link.zhihu.com/?target=https%3A//github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)，当然各种地方你都能搜到这篇贴子及其变种。

**最后，想要进阶的话，功夫就在 TikZ 之外了。**除了熟练使用各种绘图命令以外，还得清楚一些 TeX 的底层原理，要涉猎排版和设计领域的知识。这不但是个体力活，也是个技术活，更是个艺术活。我目前还没有修炼到这层境界，自然也就不敢给出建议，期待有大佬能够指点一二。

***

不知道多少人能看到这里，毕竟通篇都没有写这个宏包该怎么用。Talk is cheap, show me the code，教练，你整这么多虚的没用，最起码给个能跑的例子啊。

怎么说呢，“臣之所好者，道也，进乎技矣”。哈哈没有啦，我们下一篇就讲，别急。

我想，最终能用好并且喜欢上 TikZ 的人，应该也不会在乎这一两篇的工夫。

https://zhuanlan.zhihu.com/p/48300815编辑于 2019-02-08


# 2. 入门级notes


```
\documentclass{article} % say
\usepackage{tikz}
\begin{document}
We are working on
\begin{tikzpicture}
  \draw (-1.5,0) -- (1.5,0);
  \draw (0,-1.5) -- (0,1.5);
\end{tikzpicture}.
\end{document}
```



```
\documentclass{article}
\usepackage{tikz}

\begin{document}

\begin{tikzpicture}
\draw[black] (-3,0) -- (4,0);
\draw (-1.5, -0.1) -- (-1.5, 0.1) node[above] {FOOO};
\foreach \x in {-2,-1,0,1,2,3}
 \draw (\x,0) -- (\x,-0.1) node[below] {$\x$};  
\end{tikzpicture}

\end{document}
```


1.1 语法

1.1.1 点的表示 (坐标表示)

绝对位置

直角坐标表示 (x,y), 例如 (1cm,2pt), (1,2pt).
极坐标表示 (θ,ρ), 例如 (30:1cm), (120:1cm).

相对位置

```
++(dx,dy)
```

使用两个加号表示相对于最后使用的坐标点的位置 ++(dx,dy), 例如 ++(1cm,0).

```
+(dx,dy)
```

和 ++(dx,dy) 类似, 只是不改变后续相对位置坐标的基准点. 如 (1,0)+(1,0)+(0,1) 表示 (1,0), (2,0) 和 (1,1).

1.1.2 路径 (Path) 的表示以及对路径的操作 不要忘记表达式尾的分号。
	
```
\draw (-1.5,0) -- (1.5,0) -- (0,-1.5) -- (0,1.5);
```

线条的粗细有以下一些值

ultra thin, very thin, thin, semithick, thick, very thick, ultra thick

thin是正常粗细，它和TEX的\hrule的粗细相同。

线条的样式有以下一些值

loosely dashed, dashed, densely dashed

loosely dotted, dotted, densely dotted

若要为线条尾部增加箭头，可以为\draw添加->选项。若为线条头部增加箭头，改为<-。若首尾均增加箭头，则是<->。

路径是一系列的直线或曲线. TikZ 使用类似于 MetaPost 的语法表示路径. 我们可以 画(draw), 填充(fill), 阴影化(shade) 以及 剪切(clip)路径. 例如,

```
\path (0,0) rectangele (2ex,1ex);,
\path[draw] (0,0) rectangle (2ex,1ex)
\path[fill]
\path[clip]
```


```
\draw (-0.5,-0.5) rectangle (-1,-1);
```


增加点风格：

```
help lines/.style={color=blue!50,very thin}
```



如果help lines定义在全局，则在文档开头使用\tikzset

```
\tikzset{help lines/.style=very thin}
```

一个风格的定义可以引用另一个风格。如Karl's grid引用了上面的help lines


```
\tikzset{Karl’s grid/.style={help lines,color=blue!50}}
...
  \draw[Karl’s grid] (0,0) grid (5,5);
```
这也同时提示我们风格的用法类似```\draw[style]```。如果定义局部（在环境内部）的风格，则像下面这样


```
\begin{tikzpicture}
[Karl’s grid/.style ={help lines,color=#1!50},
Karl’s grid/.default=blue]
  \draw[Karl’s grid] (0,0) grid (1.5,2);
  \draw[Karl’s grid=red] (2,0) grid (3.5,2);
\end{tikzpicture}
```
定义在tikzpicture的可选参数中。上面也提示我们可以为风格设置默认值，想要替换默认值只需要给风格赋一个新值。







1.1.3 节点 (Nodes) 的表示

TikZ中的node可以插入文字标签，更重要的是可以方便地构造几何图形。转换图、流程图等等都可以用node实现

\node和at 

```
\begin{tikzpicture}
  \node at ( 0,2) [circle,draw] {};
  \node at ( 0,1) [circle,draw] {};
  \node at ( 0,0) [circle,draw] {};
  \node at ( 1,1) [rectangle,draw] {};
  \node at (-1,1) [rectangle,draw] {};
\end{tikzpicture}
```


这种写法使用了\node命令和at标记，简化了原始写法。行尾的{}用于插入文字，为空表示不插入任何文字。可选参数中，circle给出了环绕文字（尽管为空）的形状，draw选项引起绘制环绕形状的动作。

事实上，\node命令是\path node的简写。更原始的版本是这样



```
\begin{tikzpicture}
\path node at ( 0,2) [shape=circle,draw] {}
	  node at ( 0,1) [shape=circle,draw] {}
	  node at ( 0,0) [shape=circle,draw] {}
	  node at ( 1,1) [shape=rectangle,draw] {}
	  node at (-1,1) [shape=rectangle,draw] {};
\end{tikzpicture}
```

最原始的版本没有使用at标记，含义并不直观，所以不再列出。


上面绘制出的node尺寸非常小，因为我们没有设定尺寸参数。node默认使用inner sep的值自动为node中的文字增加环绕空白，而默认的inner sep是很小的。可以手动修改inner sep的值

```
\begin{tikzpicture}
[inner sep=2mm,
place/.style={circle,draw=blue!50,fill=blue!20,thick},
transition/.style={rectangle,draw=black!50,fill=black!20,thick}]
  \node at ( 0,2) [place] {};
  \node at ( 0,1) [place] {};
  \node at ( 0,0) [place] {};
  \node at ( 1,1) [transition] {};
  \node at (-1,1) [transition] {};
\end{tikzpicture}
```



但是更好的做法是使用minimum size选项。它指定了node的最小尺寸：无论内部文字多么小（甚至没有），node都能达到这一最小尺寸。同时将inner sep设为0pt，这样能在minimum size较小的时候不至于错误地包含inner sep增加的空间。

node命名

为了后续引用定义好的node（比如在node间绘制连接线），可以为node命名，以后用名字引用node。方便的做法是将名字放置在圆括号内部

```
% ... set up styles
\begin{tikzpicture}
  \node (waiting 1) at ( 0,2) [place] {};
  \node (critical 1) at ( 0,1) [place] {};
  \node (semaphore) at ( 0,0) [place] {};
  \node (leave critical) at ( 1,1) [transition] {};
  \node (enter critical) at (-1,1) [transition] {};
\end{tikzpicture}
```

node的语法很宽松，名字、at标识符、可选参数的顺序不做要求。

使用相对位置
fixed positioning弊端很大，不直观而且不灵活，relative positioning使用起来更方便。在TikZ中使用相对位置需要载入positioning库。于是使用相对位置改写上面的例子

```
\begin{tikzpicture}
  \node[place] (waiting) {};
  \node[place] (critical) [below=of waiting] {};
  \node[place] (semaphore) [below=of critical] {};
  \node[transition] (leave critical) [right=of critical] {};
  \node[transition] (enter critical) [left=of critical] {};
\end{tikzpicture}
```


当类似below的选项后面紧跟of，TikZ就会启用相对位置。相对距离则使用node distance选项。

为node增加文字标签
想要在node周围增加文字标签，有两种方法

直接使用node，利用node的anchor属性

```
\begin{tikzpicture}
  \node[place] (waiting) {};
  \node[place] (critical) [below=of waiting] {};
  \node[place] (semaphore) [below=of critical] {};
  \node[transition] (leave critical) [right=of critical] {};
  \node[transition] (enter critical) [left=of critical] {};
  \node [red,above] at (semaphore.north) {$s\le 3$};
\end{tikzpicture}
```

使用label选项


```
\tikz
  \node [circle,draw,label=60:$60^\circ$,label=below:$-90^\circ$] {my circle};
```

像上面这样，可以增加多个标签。

node连接线
连接node使用锚点anchor最为简便，每个node定义了一系列的锚点。最简单的情况是直线


	
```
\draw [->] (critical.west) -- (enter critical.east);
```


绘制曲线就复杂的多。我们不列出使用controls语法的方式，直接讲述to操作。如果to操作不带任何参数，它就绘制一条直线



```
\draw [->] (enter critical) to (critical);
```
需要注意的是，上面的node没有指定anchor。当TikZ遇到一个node需要解析为坐标时，它会根据后面的内容判断应该选取node的哪一个anchor作为坐标。如果TikZ判断错误，大可重新加上anchor给出准确位置。

to操作有很多参数，这里用到的是in和out对。in和out接受角度值，分别给出曲线离开初始坐标的角度和曲线到达目标坐标的角度。



```
\draw [->] (waiting) to [out=180,in=90] (enter critical);
```
绘制直线和曲线的代码得到
to syntax

更为简单的方式是使用bend left/bend right选项。



```
\draw [->] (waiting) to [bend right=45] (enter critical);
```
bend right可以想象为，本来有一条连接起始点和终点的直线，把直线的中点向右拉伸45∘。

有一个操作比to操作更好，就是edge操作。这个操作专门为node添加连接线，它和node一样，不是path的一部分，在path构造完后才会被加入进去。



```
\begin{tikzpicture}
  \node[place] (waiting) {};
  \node[place] (critical) [below=of waiting] {};
  \node[place] (semaphore) [below=of critical] {};
  \node[transition] (leave critical) [right=of critical] {};
  \node[transition] (enter critical) [left=of critical] {}
    edge [->] (critical)
    edge [<-,bend left=45] (waiting)
    edge [->,bend right=45] (semaphore);
\end{tikzpicture}
```
上面三条edge操作每一条都创建了一条新的path，每条path都是enter critical to在edge后面的node。

两个很实用的style


```

\begin{tikzpicture}
  [bend angle=45,
   pre/.style={<-,shorten <=1pt,>=stealth,semithick},
   post/.style={->,shorten >=1pt,>=stealth,semithick}]
   
```
bend angle一旦被设置，bend left和bend right的角度都是bend angle的值。

https://methor.github.io/writing/tikz/ 来自这里的笔记



该表示可用于向图片中添加文本. 节点插入在当前路径上的当前位置. 例如,

```
\draw (1, 1) node {text} -- (2,2);
\draw (1, 1) node[circle, draw] {text};
```
1.1.4 树和图的语法
树的表示

```
\begin{tikzpicture}
        \node {root}
              child {node {left}}
              child {node {right}
                    child {node {child}}
                    child {node {child}}
              };
\end{tikzpicture}

```

图的表示


```
\begin{tikzpicture}
        \graph [grow down, branch right] {
               root -> { left, right -> {child, child} }
        };
\end{tikzpicture}
```














































\[LaTeX 绘图\] tikz 绘制平面几何，示例两则

https://zhuanlan.zhihu.com/p/82427838


TikZ的包吧  
[Simple flow chart](https://link.zhihu.com/?target=http%3A//www.texample.net/tikz/examples/simple-flow-chart/)  
更复杂的mindmaps：  
[TikZ examples feature: Mindmaps](https://link.zhihu.com/?target=http%3A//www.texample.net/tikz/examples/feature/mindmaps/)

数据流程图，用Latex生成的：


-   绘图工具很多，不同的图形有不同的自然表达方式。用专门为特定问题设计的合适的绘图工具来画图，通常效果最好，效率也高。所以在可能的情况下，我们尽量用适合问题的工具。
  
-   另一方面，使用你熟悉的工具效率也高。所以在可能的情况下，我们尽量用自己熟悉的工具。
  
-   人的精力是有限的，学习和熟悉工具也需要时间。所以在可能的情况下，我们希望少学新工具或者只学简单的工具。  
    
  

这几条道理很简单，除了绘图工具在很多地方也都是一样的道理。可惜这几个原则是有冲突的，越专门的工具越得多学几样才能应付工作，越通用的工具使用起来相对越不方便，学的工具越少就对工具越不熟悉，往往如此。 所以，你需要对你自己要做的事情，要花的精力有个充分的估计。然后取个好的折衷。

换句话说，你了解你自己要画的图形和不同工具适合画的图形，挑选适合自己的工具。

TikZ 与 MetaPost 都是代码作图工具，适合画能用坐标表示的精确图形。不过二者也有差别。

MetaPost 脱胎于字体设计语言 MetaFont，其语法可以用相对直观的方式精确描述 Bézier 曲线，又自带语法方便的线性方程求解功能、图形的线性变换功能，因而有很强的二维曲线造型功能；同时又有宏定义、循环、分支等程序结构，可以表达较复杂的数学图形；同时可以插入 TeX 代码的文字、公式。所以用 MetaPost 来画有数学描述的、数值或半数值化的、有 TeX 公式的曲线或直线图是最适合的，在一些已有的宏支持下也适合数据结构图。举个例子的话，比如说，L-system 定义的分形曲线，集合论里面的 Venn 图，正十七边形或五角星，射影几何里面 Desargues 定理的配图，计算机科学中的 B+ 树，都挺合适。

TikZ 是由 TeX 宏编写的宏包，抽象掉底层 pdfTeX 这样的引擎或 Dvips、dvipdfmx 这样的输出驱动来完成实际的绘图工作。在功能上借鉴 PSTricks，在语法上也部分借鉴 MetaPost。由于 TeX 宏本身的限制，TikZ 在曲线造型、数值计算、复杂数据结构组织上，虽然也能做，但效率比较低；优势是开发比较深入，预定义的功能多，能直接用的包比较多，作为宏包与 TeX 结合也最紧密。适合画简单的小符号，数据结构图，计算量不太大的数学图形等。适合做的图形与 MetaPost 有不少重叠的，比如集合论的 Venn 图，正十七边形或五角星，简单流程图，数据结构图；也包括自己独有优势的如数学符号标记，图表标注，数学交换图等。现在在 luatex 的帮助下也能完成一些复杂计算，比如复杂函数图，图可视化。

所以，如果你要画的图形与工具擅长的方面一致，又画的比较多肯花时间熟悉，那学这些东西就有用。
https://www.zhihu.com/question/27332117/answer/36291713

会一种https://www.zhihu.com/question/27332117/answer/36291713称手的矢量绘图工具就好了，无论是基于GUI，还是基于script。metapost和tikz以及一切程序类语言的优点在于可以绘制精确的几何图形，但调整效果会没那么直观，需要调试->编译->调试->编译->…

另外，metapost和tikz和latex很好的协作能力，对于latex控还是很有吸引力的。

我现在用tikz，熟练的部分直接编脚本，然后用ktikz边改边看效果。为防止嵌入到latex中拖慢编译速度，于是单独写了个将tikz代码转成pdf的脚本。

[https://raw.githubusercontent.com/pkuwwt/code-collections/master/shell/pgf2pdf](https://link.zhihu.com/?target=https%3A//raw.githubusercontent.com/pkuwwt/code-collections/master/shell/pgf2pdf)













