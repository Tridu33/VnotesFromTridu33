# JupyterNotebook2PDF





https://www.jianshu.com/p/c970fdce69e8

```
\documentclass[11pt]{ctexart}   %将download as tex得到的文件做修改，将article更改以支持中文
```




```
%导言区
\documentclass{ctexart}

%导入宏包
\usepackage{amsmath}
\usepackage{amssymb}

%正文区
\begin{document}
    %多行公式--带编号
    \begin{gather}
        a + b +c = b + a \\
        1+2 = 2 + 1
    \end{gather}
    %多行公式--不带编号1
    \begin{gather*}
        a + b = b + a \\
        1+2 = 2 + 1
    \end{gather*}
    
    %多行公式--带编号2 \notag 阻止编号
    \begin{gather}
    a + b = b + a \notag \\
    1+2 = 2 + 1 \notag
    \end{gather}
    
    % 按&号对齐,--带编号
    \begin{align}
        a+b &= b+a \\
        1+2= & 2+1
    \end{align}
    
    % 按&号对齐,--不带编号
    \begin{align*}
    a+b &= b+a \\
    1+2 &=2+1
    \end{align*}
    
    %一个公式的多行排版--带编号
    \begin{equation}
        \begin{split}
        \cos 2x &= \cos^2 x - \sin^2x \\
        &=2\cos^2x-1
        \end{split} 
    \end{equation}
    
    %一个公式的多行排版--不带编号
    \begin{equation*}
    \begin{split}
    \cos 2x &= \cos^2 x - \sin^2x \\
    &=2\cos^2x-1
    \end{split} 
    \end{equation*}
    
    %case环境, text{}在数学模式中处理中文-带编号
    \begin{equation}
        D(x)=\begin{cases}
        1, & \text{如果} x \in \mathbb{Q};\\
        0, & \text{如果} x \in \mathbb{R}\setminus\mathbb{Q}
        \end{cases}
    \end{equation}
    
    %case环境, text{}在数学模式中处理中文-不带编号
    \begin{equation*}
    D(x)=\begin{cases}
    1, & \text{如果} x \in \mathbb{Q};\\
    0, & \text{如果} x \in \mathbb{R}\setminus\mathbb{Q}
    \end{cases}
    \end{equation*}

\end{document}

```








