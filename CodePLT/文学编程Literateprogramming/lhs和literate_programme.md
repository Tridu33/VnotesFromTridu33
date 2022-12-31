# lhs和literate_programme


wiki.haskell.org/Literate_programming








## Haskell and literate programming

Haskell is one of the few languages that provides native features to support literate programming. In haskell, a literate program is one with the suffix `.lhs` rather than `.hs`.

In a literate Haskell program, there are two ways to distinguish between code and non-code portions. You can either prepend all code with a `> `, (bird style) or surround lines of code with `\begin{code}` and `\end{code}` pairs (latex style). For those who know, use and love latex, the latter is the suggested way to go.

Note that [Happy](https://wiki.haskell.org/Happy "Happy") supports literate programming as well, via bird style (the `> `marker) in `.ly` files. Sadly, [Alex](https://wiki.haskell.org/Alex "Alex") no longer does. You might consider using [noweb](http://www.eecs.harvard.edu/~nr/noweb/) with it.

## Bird Style

According to the [Haskell Report](http://www.haskell.org/onlinereport/literate.html), this style of comment was developed by Richard Bird (hence the name) and Philip Wadler. All lines starting with `>` are interpreted as code, everything else is considered a comment. One additional requirement is that you always leave a blank line before and after the code block:

In Bird-style you have to leave a blank before the code.

> fact **::** Integer **->** Integer
> fact 0 **=** 1
> fact n **=** n * fact (n-1)

And you have to leave a blank line after the code as well.

The idea behind this restriction is capturing the mistake of not inserting the `>` mark at the beginning of the line. In general this is not only good practice, but also a formatting that makes the code more readable.

However, there are cases in which you might like to get around this restriction. Perhaps you're writing Haskell code within a markup language that's not Latex, and you may have to surround your code with something equivalent to `\begin{code}` and `\end{code}`. In this case, GHC provides a flag that can be used to lift the blank lines requirement:

$ ghc -optL -q

  

## Latex suggestions for literate programming

(See also [#lhs2TeX](https://wiki.haskell.org/Literate_programming#lhs2TeX) below) In the majority of these suggestions, you can simply write:

\begin{code}
tsort \[\]     **=** \[\]
tsort (x:xs) **=** tsort \[y | y**<-**xs, y>x\] ++ \[x\] ++ tsort \[y | y**<-**xs, y<=x\]
\end{code}

and the code will be formatted as you requested.

The advantage: Source code and documentation are consistent! The code environment is understood by Haskell compilers, so you can run your documentation files directly.

### Verbatim package

One can always simply use verbatim mode which will format the code "as-is".

Use verbatim:

\\usepackage{verbatim}
\\newenvironment{code}{\\footnotesize\\verbatim}{\\endverbatim\\normalsize}

### Listings package

Another alternative is to use the latex-package listings, which allows you to do much more customization of the output:

\\usepackage{listings}
\\lstnewenvironment{code}{\\lstset{language=Haskell,basicstyle=\\small}}{}

You can configure the appearance of the listings quite a bit! Some people find these settings to be the most satisfying:

\\usepackage{listings}
\\lstloadlanguages{Haskell}
\\lstnewenvironment{code}
    {\\lstset{}%
      \\csname lst@SetFirstLabel\\endcsname}
    {\\csname lst@SaveFirstLabel\\endcsname}
    \\lstset{
      basicstyle=\\small\\ttfamily,
      flexiblecolumns=false,
      basewidth={0.5em,0.45em},
      literate={+}{{$+$}}1 {/}{{$/$}}1 {*}{{$*$}}1 {=}{{$=$}}1
               {>}{{$>$}}1 {<}{{$<$}}1 {\\\}{{$\\lambda$}}1
               {\\\\\\}{{\\char`\\\\\char`\\\}}1
               {->}{{$\\rightarrow$}}2 {>=}{{$\\geq$}}2 {<-}{{$\\leftarrow$}}2
               {<=}{{$\\leq$}}2 {=>}{{$\\Rightarrow$}}2 
               {\ .}{{$\\circ$}}2 {\ .\ }{{$\\circ$}}2
               {>>}{{>>}}2 {>>=}{{>>=}}2
               {|}{{$\\mid$}}1               
    }

You might want to consult the documentation of the "listings" package, to find out whether there's more you can tune to your likings. (Like adding line numbers, etc.) Note that the suggested "literate" option above will replace the given symbols anywhere in the text, including inside strings, which is probably not what one wants.

For arrow notation add the line (requires MnSymbol package, or stmaryrd if you use Yleft instead):

               {<<<}{{$\\lll$}}2 {>>>}{{$\\ggg$}}2 {-<}{{$\\leftY$}}1

### Minted package

It is also possible to use the LaTeX package minted, which uses pygments for rich syntax highlighting:

\\usepackage{minted}
\\newminted\[code\]{haskell}{}
\\newminted\[spec\]{haskell}{}

In order for LaTeX to be able to call pygments, you need to install pygments and call LaTeX with the `-shell-escape` flag.

### Hiding code from Latex

If you want to hide some code, you can e.g. define:

\\long\\def\\ignore#1{}

Auxiliary functions can be hidden as follows:

\\ignore{
\\begin{code}
help = putStr "Help me, what is this LiterateProgramming thing??"
\\end{code}
}

Thanks to Wolfram Kahl, Oliver Braun and the people of the German TeX-newsgroup.

Ciao, Steffen Mazanek

[http://www.steffen-mazanek.de](http://www.steffen-mazanek.de/)

### Hiding code from Haskell

If you want to hide a `\begin{code}...\end{code}` block from the *compiler*, say, if you want to show an example in the text that is not actually part of the source code, you can just add a comment right after the "\\begin{code}" statement. This will cause the Haskell parser to treat this block as text, not code:

And the definition of the following function
would totally screw up my program, so I'm not
definining it:

\\begin{code}% this is not really code
main :: IO ()
main = print "just an example"
\\end{code}

See?

While this works well for vanilla LaTeX, if you're using lhs2TeX, then you'll get the "% this is not really code" printed in your output. Instead of doing the above, either use `\begin{spec} ... \end{spec}`, or if you're writing Bird-style code, flip your ">" characters around:

Neither of the following definitions are really code:

\\begin{spec}
main :: IO ()
main = print "another example"
\\end{spec}

< main :: IO ()
< main = print "...and another"

## Transformation of .lhs-files

Sub-pages here have scripts to convert from the demarcation via `> `(called "bird style" after Dr. Richard Bird) to `\begin{code}` and `\end{code}` pairs

-   [Literate programming/Bird conversion via awk](https://wiki.haskell.org/Literate_programming/Bird_conversion_via_awk "Literate programming/Bird conversion via awk")
-   [Literate programming/Bird conversion via sed](https://wiki.haskell.org/Literate_programming/Bird_conversion_via_sed "Literate programming/Bird conversion via sed")

  

## Editors

### Multi-mode support in Emacs

Another useful tool for literate programmers is the [mmm-mode](http://mmm-mode.sourceforge.net/) for Emacs. mmm-mode switches the current major mode of the buffer between two alternatives, depending on the context the cursor is in. If you're in, say, a `\begin{code}...\end{code}` block, you'll be editing in haskell-mode, but once you leave that block, you'll be editing in latex-mode.

I have managed to cook up a configuration for both literate styles, but surely some Emacs guru can enhance these. To configure mmm-mode for Haskell, add these lines to your .emacs file:

(add-hook 'haskell-mode-hook 'my-mmm-mode)

(mmm-add-classes
 '((literate-haskell-bird
    :submode text-mode
    :front "^\[^>\]"
    :include-front true
    :back "^>\\\|$"
    )
   (literate-haskell-latex
    :submode literate-haskell-mode
    :front "^\\\\\\begin{code}"
    :front-offset (end-of-line 1)
    :back "^\\\\\\end{code}"
    :include-back nil
    :back-offset (beginning-of-line -1)
    )))

(defun my-mmm-mode ()
  ;; go into mmm minor mode when class is given
  (make-local-variable 'mmm-global-mode)
  (setq mmm-global-mode 'true))

(setq mmm-submode-decoration-level 0)

You can activate mmm-mode by running "M-x mmm-ify-by-class" in the buffer. Emacs will prompt you for the class to use, to which should answer literate-haskell-bird or literate-haskell-latex, respectively.

If you want Emacs to activate mmm-mode automatically for certain literate Haskell files, add these lines to it at the end:

% \-\-\-\-\- Configure Emacs -----
%
% Local Variables: ***
% mode: latex ***
% mmm-classes: literate-haskell-latex ***
% End: ***

This is, what the my-mmm-mode hook does, by the way.

### Vim

See [Literate programming/Vim](https://wiki.haskell.org/Literate_programming/Vim "Literate programming/Vim").

## lhs2TeX

Highly recommended is **[lhs2TeX](https://hackage.haskell.org/package/lhs2tex)**, courtesy of Andres Löh. It is designed for typesetting papers *about* Haskell, but **lhs2TeX** is easily configured and can make for a powerful preprocessor and documentation generator.

Input to lhs2TeX is a slightly modified `.lhs` file. One would typically use the standard latex recommendations above, using a `\begin{code}` and `\end{code}` pair to demarcate code. Additionally, lhs2TeX provides specialized macros to control the preprocessing.

Note that lhs2TeX and in-line commenting do not seem to mix well.

Since it can typeset Haskell formulas in mathematical notation with LaTeX's math mode, you can also use it to create *testable* papers. That is, readers can play with the formulas presented in the paper if they obtain the literate Haskell source code for the paper.

## Shuffle

[Shuffle](http://www.cs.uu.nl/wiki/Ehc/Shuffle) is a tool which extends the capabilities of `lhs2TeX`. It was used in documenting the [Essential Haskell Compiler project](http://www.cs.uu.nl/wiki/Ehc/WebHome). It is available as part of this project, but it is usable also independently.

## See also

-   [Daniel Mall's website for Literate Programming.](http://www.literateprogramming.com/)
-   [Wikipedia](http://en.wikipedia.org/wiki/Literate_programming)
-   [Textual Haskell source](https://wiki.haskell.org/Textual_Haskell_source "Textual Haskell source") \- a `.ths` processor, where text is king.








