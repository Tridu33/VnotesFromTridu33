# 1. haskell文学编程





lhs2tex
[https://github.com/kosmikus/lhs2tex/tree/lhs2tex-1.23](https://github.com/kosmikus/lhs2tex/tree/lhs2tex-1.23)

[http://hackage.haskell.org/package/lhs2tex-1.18.1](http://hackage.haskell.org/package/lhs2tex-1.18.1)













pandoc *.lhs 


```cmd
pandoc -f markdown+lhs -t html+lhs
```



















## 1.1. Literate Haskell support

#### 1.1.1.1. Extension: `literate_haskell`

Treat the document as literate Haskell source.

This extension can be enabled/disabled for the following formats:

input formats

`markdown`, `rst`, `latex`

output formats

`markdown`, `rst`, `latex`, `html`

If you append `+lhs` (or `+literate_haskell`) to one of the formats above, pandoc will treat the document as literate Haskell source. This means that

-   In Markdown input, “bird track” sections will be parsed as Haskell code rather than block quotations. Text between `\begin{code}` and `\end{code}` will also be treated as Haskell code. For ATX-style headings the character ‘=’ will be used instead of ‘#’.
    
-   In Markdown output, code blocks with classes `haskell` and `literate` will be rendered using bird tracks, and block quotations will be indented one space, so they will not be treated as Haskell code. In addition, headings will be rendered setext-style (with underlines) rather than ATX-style (with ‘#’ characters). (This is because ghc treats ‘#’ characters in column 1 as introducing line numbers.)
    
-   In restructured text input, “bird track” sections will be parsed as Haskell code.
    
-   In restructured text output, code blocks with class `haskell`will be rendered using bird tracks.
    
-   In LaTeX input, text in `code` environments will be parsed as Haskell code.
    
-   In LaTeX output, code blocks with class `haskell` will be rendered inside `code` environments.
    
-   In HTML output, code blocks with class `haskell` will be rendered with class `literatehaskell` and bird tracks.
    

Examples:

```
pandoc -f markdown+lhs -t html
```

reads literate Haskell source formatted with Markdown conventions and writes ordinary HTML (without bird tracks).

```
pandoc -f markdown+lhs -t html+lhs
```

writes HTML with the Haskell code in bird tracks, so it can be copied and pasted as literate Haskell source.

Note that GHC expects the bird tracks in the first column, so indented literate code blocks (e.g. inside an itemized environment) will not be picked up by the Haskell compiler.


[https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)



When converting markdown to markdown+lhs following 2 variants should yield the same output:


``` {.literate .haskell}
main = putStr "Hello World!"
```

不行，想在代码里显示包住代码的``````怎么写？

```lhs
main = putStr "Hello World!"
```


should both yield

```
> main = putStr "Hello World!"
```



[https://github.com/jgm/pandoc/issues/4510](https://github.com/jgm/pandoc/issues/4510)




















Contents
1	Haskell and literate programming
2	Bird Style
3	Latex suggestions for literate programming
3.1	Verbatim package
3.2	Listings package
3.3	Minted package
3.4	Hiding code from Latex
3.5	Hiding code from Haskell
4	Transformation of .lhs-files
5	Editors
5.1	Multi-mode support in Emacs
5.2	Vim
6	lhs2TeX
7	Shuffle
8	See also

[https://wiki.haskell.org/Literate_programming](https://wiki.haskell.org/Literate_programming)



































