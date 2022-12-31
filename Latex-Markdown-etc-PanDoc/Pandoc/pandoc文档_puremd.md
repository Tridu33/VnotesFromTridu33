[TOC]


# Pandoc用户指南


英文网站链接


-   [概要](https://pandoc.org/MANUAL.html#synopsis)
-   [描述](https://pandoc.org/MANUAL.html#description)▸
-   [选件](https://pandoc.org/MANUAL.html#options)▸
-   [退出码](https://pandoc.org/MANUAL.html#exit-codes)
-   [默认文件](https://pandoc.org/MANUAL.html#default-files)
-   [范本](https://pandoc.org/MANUAL.html#templates)▸
-   [扩展名](https://pandoc.org/MANUAL.html#extensions)▸
-   [潘多克的降价促销](https://pandoc.org/MANUAL.html#pandocs-markdown)▸
-   [使用Pandoc制作幻灯片](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc)▸
-   [使用Pandoc创建EPUB](https://pandoc.org/MANUAL.html#creating-epubs-with-pandoc)▸
-   [使用Pandoc创建Jupyter笔记本](https://pandoc.org/MANUAL.html#creating-jupyter-notebooks-with-pandoc)
-   [语法高亮](https://pandoc.org/MANUAL.html#syntax-highlighting)
-   [自定义样式](https://pandoc.org/MANUAL.html#custom-styles)▸
-   [习俗作家](https://pandoc.org/MANUAL.html#custom-writers)
-   [安全注意事项](https://pandoc.org/MANUAL.html#a-note-on-security)
-   [作者](https://pandoc.org/MANUAL.html#authors)

# 概要

`pandoc`\[ *选项* \] \[ *输入文件* \]…

# 描述

Pandoc是用于从一种标记格式转换为另一种标记格式的[Haskell](https://www.haskell.org/)库，也是使用该库的命令行工具。

Pandoc可以在多种标记和文字处理格式之间转换，包括但不限于[Markdown](https://daringfireball.net/projects/markdown/)，[HTML](https://www.w3.org/html/)，[LaTeX](https://www.latex-project.org/)和[Word docx的](https://en.wikipedia.org/wiki/Office_Open_XML)各种样式。有关输入和输出格式的完整列表，请参见[下面](https://pandoc.org/MANUAL.html#general-options)的[`--from`](https://pandoc.org/MANUAL.html#option--from)和[选项](https://pandoc.org/MANUAL.html#general-options)。Pandoc也可以生成[PDF](https://www.adobe.com/pdf/)输出：请参见下面的[创建PDF](https://pandoc.org/MANUAL.html#creating-a-pdf)。[`--to`](https://pandoc.org/MANUAL.html#option--to)[](https://pandoc.org/MANUAL.html#general-options)[](https://www.adobe.com/pdf/)[](https://pandoc.org/MANUAL.html#creating-a-pdf)

Pandoc的Markdown增强版本包括[表格](https://pandoc.org/MANUAL.html#tables)语法，[定义列表](https://pandoc.org/MANUAL.html#definition-lists)，[元数据块](https://pandoc.org/MANUAL.html#metadata-blocks)，[脚注](https://pandoc.org/MANUAL.html#footnotes)，[引文](https://pandoc.org/MANUAL.html#citations)，[数学](https://pandoc.org/MANUAL.html#math)等。参见下文[Pandoc的Markdown下](https://pandoc.org/MANUAL.html#pandocs-markdown)。

Pandoc具有模块化设计：它由一组阅读器和一组编写器组成，这些阅读器以给定的格式解析文本并生成文档的本机表示形式（*抽象语法树*或AST），而作者将这些本机表示形式转换为目标格式。因此，添加输入或输出格式仅需要添加读取器或写入器。用户还可以运行自定义[pandoc筛选器](https://pandoc.org/filters.html)来修改中间AST。

由于pandoc的文档中间表示形式不如其在多种格式之间进行转换，因此，不应期望每种格式之间都能进行完美的转换。Pandoc尝试保留文档的结构元素，但不设置格式细节，例如边距大小。而且某些文档元素（例如复杂表）可能不适合pandoc的简单文档模型。虽然从pandoc的Markdown到所有格式的转换都希望是完美的，但是从比pandoc的Markdown更具表现力的格式的转换可能会带来损失。

## 使用pandoc

如果未指定*输入文件*，则从*stdin*读取*输入*。默认情况下，输出进入*标准输出*。要输出到文件，请使用以下[`-o`](https://pandoc.org/MANUAL.html#option--output)选项：

```
pandoc -o output.html input.txt
```

默认情况下，pandoc会生成一个文档片段。要生成独立文档（例如，包含`<head>`和的有效HTML文件`<body>`），请使用[`-s`](https://pandoc.org/MANUAL.html#option--standalone)或[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)标志：

```
pandoc -s -o output.html input.txt
```

有关如何生成独立文档的更多信息，请参见下面的[模板](https://pandoc.org/MANUAL.html#templates)。

如果给出了多个输入文件，`pandoc`将在解析之前将它们全部连接起来（它们之间有空行）。（用于[`--file-scope`](https://pandoc.org/MANUAL.html#option--file-scope)分别解析文件。）

## 指定格式

可以使用命令行选项显式指定输入和输出的格式。可以使用[`-f/--from`](https://pandoc.org/MANUAL.html#option--from)选项指定输入格式，使用选项指定输出格式[`-t/--to`](https://pandoc.org/MANUAL.html#option--to)。因此，要将`hello.txt`Markdown 转换为LaTeX，您可以输入：

```
pandoc -f markdown -t latex hello.txt
```

要将`hello.html`HTML 转换为Markdown：

```
pandoc -f html -t markdown hello.html
```

支持的输入和输出格式在“ [选项”](https://pandoc.org/MANUAL.html#options)下面列出（请参阅参考[`-f`](https://pandoc.org/MANUAL.html#option--from)以了解输入格式和[`-t`](https://pandoc.org/MANUAL.html#option--to)输出格式）。您还可以使用`pandoc --list-input-formats`和`pandoc --list-output-formats`打印支持的格式列表。

如果未明确指定输入或输出格式，`pandoc`将尝试从文件名的扩展名中猜测出来。因此，例如

```
pandoc -o hello.tex hello.txt
```

`hello.txt`将从Markdown 转换为LaTeX。如果未指定输出文件（以便输出转到*stdout*），或者输出文件的扩展名未知，则输出格式将默认为HTML。如果未指定输入文件（因此输入来自*stdin*），或者输入文件的扩展名未知，则将假定输入格式为Markdown。

## 字符编码

Pandoc对输入和输出均使用UTF-8字符编码。如果您的本地字符编码不是UTF-8，则应通过[`iconv`](https://www.gnu.org/software/libiconv/)以下管道传递输入和输出：

```
iconv -t utf-8 input.txt | pandoc | iconv -f utf-8
```

请注意，在某些输出格式（例如HTML，LaTeX，ConTeXt，RTF，OPML，DocBook和Texinfo）中，有关字符编码的信息包含在文档标题中，只有在使用此[`-s/--standalone`](https://pandoc.org/MANUAL.html#option--standalone)选项时才会包含这些字符。

## 创建PDF

要生成PDF，请指定带有`.pdf`扩展名的输出文件：

```
pandoc test.txt -o test.pdf
```

默认情况下，pandoc将使用LaTeX创建PDF，这需要安装LaTeX引擎（请参见[`--pdf-engine`](https://pandoc.org/MANUAL.html#option--pdf-engine)下文）。另外，pandoc可以使用ConTeXt，roff ms或HTML作为中间格式。要做到这一点，请用一个输出文件`.pdf`扩展名，和以前一样，但添加[`--pdf-engine`](https://pandoc.org/MANUAL.html#option--pdf-engine)的选项或[`-t context`](https://pandoc.org/MANUAL.html#option--to)，[`-t html`](https://pandoc.org/MANUAL.html#option--to)或[`-t ms`](https://pandoc.org/MANUAL.html#option--to)在命令行。可以使用指定用于从中间格式生成PDF的工具[`--pdf-engine`](https://pandoc.org/MANUAL.html#option--pdf-engine)。

您可以使用变量，取决于所使用的中间格式控制PDF风格：看到[了LaTeX的变量](https://pandoc.org/MANUAL.html#variables-for-latex)，[上下文变量](https://pandoc.org/MANUAL.html#variables-for-context)，[变量`wkhtmltopdf`](https://pandoc.org/MANUAL.html#variables-for-wkhtmltopdf)，[用于MS变量](https://pandoc.org/MANUAL.html#variables-for-ms)。当HTML用作中间格式时，可以使用设置样式[`--css`](https://pandoc.org/MANUAL.html#option--css)。

要调试PDF的创建，请看一下中间表示，这可能会很有用：代替[`-o test.pdf`](https://pandoc.org/MANUAL.html#option--output)，例如使用[`-s -o test.tex`](https://pandoc.org/MANUAL.html#option--standalone)输出生成的LaTeX。然后，您可以使用进行测试`pdflatex test.tex`。

当使用乳胶，下面的包必须是可用的（它们都包含在所有最新版本的[TeX Live中](https://www.tug.org/texlive/)）： ，[`amsfonts`](https://ctan.org/pkg/amsfonts)，[`amsmath`](https://ctan.org/pkg/amsmath)，[`lm`](https://ctan.org/pkg/lm)，[`unicode-math`](https://ctan.org/pkg/unicode-math)，[`ifxetex`](https://ctan.org/pkg/ifxetex)，[`ifluatex`](https://ctan.org/pkg/ifluatex)（[`listings`](https://ctan.org/pkg/listings)如果该[`--listings`](https://pandoc.org/MANUAL.html#option--listings)选项时使用）[`fancyvrb`](https://ctan.org/pkg/fancyvrb)，[`longtable`](https://ctan.org/pkg/longtable)，[`booktabs`](https://ctan.org/pkg/booktabs)，[`graphicx`](https://ctan.org/pkg/graphicx)（如果文档包含图片）[`hyperref`](https://ctan.org/pkg/hyperref)，[`xcolor`](https://ctan.org/pkg/xcolor)，[`ulem`](https://ctan.org/pkg/ulem)，[`geometry`](https://ctan.org/pkg/geometry)（与`geometry`变量集）， [`setspace`](https://ctan.org/pkg/setspace)（有`linestretch`），和[`babel`](https://ctan.org/pkg/babel)（带`lang`）。使用`xelatex`或`lualatex`作为PDF引擎需要[`fontspec`](https://ctan.org/pkg/fontspec)。`xelatex`使用[`polyglossia`](https://ctan.org/pkg/polyglossia)（with `lang`），[`xecjk`](https://ctan.org/pkg/xecjk)and和[`bidi`](https://ctan.org/pkg/bidi)（with the `dir`variable set）。如果`mathspec`设置了变量，`xelatex`将使用[`mathspec`](https://ctan.org/pkg/mathspec)代替[`unicode-math`](https://ctan.org/pkg/unicode-math)。的[`upquote`](https://ctan.org/pkg/upquote)和[`microtype`](https://ctan.org/pkg/microtype)如果可用的软件包使用，并且[`csquotes`](https://ctan.org/pkg/csquotes)将用于[排版](https://pandoc.org/MANUAL.html#typography)如果`csquotes`变量或元数据字段被设置为真值。在[`natbib`](https://ctan.org/pkg/natbib)，[`biblatex`](https://ctan.org/pkg/biblatex)，[`bibtex`](https://ctan.org/pkg/bibtex)，和[`biber`](https://ctan.org/pkg/biber)包可以任选地用于[引用渲染](https://pandoc.org/MANUAL.html#citation-rendering)。以下软件包将用于提高输出质量（如果存在），但pandoc不需要使用它们：（[`upquote`](https://ctan.org/pkg/upquote)用于逐字环境中的直引号），[`microtype`](https://ctan.org/pkg/microtype)（用于更好的间距调整），[`parskip`](https://ctan.org/pkg/parskip)（用于更好的段落间空格），[`xurl`](https://ctan.org/pkg/xurl)（更好的URL换行符），[`bookmark`](https://ctan.org/pkg/bookmark)（以获得更好的PDF书签）和[`footnotehyper`](https://ctan.org/pkg/footnotehyper)或[`footnote`](https://ctan.org/pkg/footnote)（或允许在表格中添加脚注）。

## 从网上阅读

代替输入文件，可以给出绝对URI。在这种情况下，pandoc将使用HTTP获取内容：

```
pandoc -f html -t markdown https://www.fsf.org
```

从URL请求文档时，可以提供自定义的User-Agent字符串或其他标头：

```
pandoc -f html -t markdown --request-header User-Agent:"Mozilla/5.0" \
  https://www.fsf.org
```

# 选件

## 常规选项

`-f` *格式*，*格式*，*格式*，*格式*`-r` `--from=``--read=`

指定输入格式。*格式*可以是：

-   `commonmark`（[CommonMark](https://commonmark.org/) Markdown）
-   `commonmark_x`（带有扩展名的[CommonMark](https://commonmark.org/) Markdown）
-   `creole`（[克里奥尔语1.0](http://www.wikicreole.org/wiki/Creole1.0)）
-   `csv`（[CSV](https://tools.ietf.org/html/rfc4180)表）
-   `docbook`（[DocBook](https://docbook.org/)）
-   `docx`（[Word docx](https://en.wikipedia.org/wiki/Office_Open_XML)）
-   `dokuwiki`（[DokuWiki标记](https://www.dokuwiki.org/dokuwiki)）
-   `epub`（[EPUB](http://idpf.org/epub)）
-   `fb2`（[FictionBook2](http://www.fictionbook.org/index.php/Eng:XML_Schema_Fictionbook_2.1)电子书）
-   `gfm`（[GitHub-Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)），或者已弃用且准确性较低`markdown_github`；[`markdown_github`](https://pandoc.org/MANUAL.html#markdown-variants)仅在您需要时不支持的扩展名时使用[`gfm`](https://pandoc.org/MANUAL.html#markdown-variants)。
-   `haddock`（[Haddock标记](https://www.haskell.org/haddock/doc/html/ch03s08.html)）
-   `html`（[HTML](https://www.w3.org/html/)）
-   `ipynb`（[Jupyter笔记本](https://nbformat.readthedocs.io/en/latest/)）
-   `jats`（[JATS](https://jats.nlm.nih.gov/) XML）
-   `jira`（[Jira](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all) / Confluence Wiki标记）
-   `json` （本机AST的JSON版本）
-   `latex`（[乳胶](https://www.latex-project.org/)）
-   `markdown`（[Pandoc的Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)）
-   `markdown_mmd`（[MultiMarkdown](https://fletcherpenney.net/multimarkdown/)）
-   `markdown_phpextra`（[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)）
-   `markdown_strict`（原始的未扩展[Markdown](https://daringfireball.net/projects/markdown/)）
-   `mediawiki`（[MediaWiki标记](https://www.mediawiki.org/wiki/Help:Formatting)）
-   `man`（[roff man](https://man.cx/groff_man(7))）
-   `muse`（[缪斯](https://amusewiki.org/library/manual)）
-   `native` （本机Haskell）
-   `odt`（[ODT](https://en.wikipedia.org/wiki/OpenDocument)）
-   `opml`（[OPML](http://dev.opml.org/spec2.html)）
-   `org`（[Emacs组织模式](https://orgmode.org/)）
-   `rst`（[reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/introduction.html)）
-   `t2t`（[txt2tags](https://txt2tags.org/)）
-   `textile`（[纺织](https://www.promptworks.com/textile)）
-   `tikiwiki`（[TikiWiki标记](https://doc.tiki.org/Wiki-Syntax-Text#The_Markup_Language_Wiki-Syntax)）
-   `twiki`（[TWiki标记](https://twiki.org/cgi-bin/view/TWiki/TextFormattingRules)）
-   `vimwiki`（[Vimwiki](https://vimwiki.github.io/)）

扩展名可以通过在格式名称后附加`+EXTENSION`或单独启用或禁用`-EXTENSION`。有关[扩展](https://pandoc.org/MANUAL.html#extensions)及其名称的列表，请参见下面的扩展。请参阅下面的[`--list-input-formats`](https://pandoc.org/MANUAL.html#option--list-input-formats)和[`--list-extensions`](https://pandoc.org/MANUAL.html#option--list-extensions)。

`-t` *格式*，*格式*，*格式*，*格式*`-w` `--to=``--write=`

指定输出格式。*格式*可以是：

-   `asciidoc`（[AsciiDoc](https://www.methods.co.nz/asciidoc/)）或`asciidoctor`（[AsciiDoctor](https://asciidoctor.org/)）
-   `beamer`（[LaTeX投影仪](https://ctan.org/pkg/beamer)幻灯片放映）
-   `commonmark`（[CommonMark](https://commonmark.org/) Markdown）
-   `commonmark_x`（带有扩展名的[CommonMark](https://commonmark.org/) Markdown）
-   `context`（[ConTeXt](https://www.contextgarden.net/)）
-   `docbook`或`docbook4`（[DocBook](https://docbook.org/) 4）
-   `docbook5` （DocBook 5）
-   `docx`（[Word docx](https://en.wikipedia.org/wiki/Office_Open_XML)）
-   `dokuwiki`（[DokuWiki标记](https://www.dokuwiki.org/dokuwiki)）
-   `epub`或`epub3`（[EPUB](http://idpf.org/epub) v3书）
-   `epub2` （EPUB v2）
-   `fb2`（[FictionBook2](http://www.fictionbook.org/index.php/Eng:XML_Schema_Fictionbook_2.1)电子书）
-   `gfm`（[GitHub-Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)），或者已弃用且准确性较低`markdown_github`；[`markdown_github`](https://pandoc.org/MANUAL.html#markdown-variants)仅在您需要时不支持的扩展名时使用[`gfm`](https://pandoc.org/MANUAL.html#markdown-variants)。
-   `haddock`（[Haddock标记](https://www.haskell.org/haddock/doc/html/ch03s08.html)）
-   `html`或`html5`（[HTML](https://www.w3.org/html/)，即  [HTML5](https://html.spec.whatwg.org/) / XHTML [多语言标记](https://www.w3.org/TR/html-polyglot/)）
-   `html4`（[XHTML](https://www.w3.org/TR/xhtml1/) 1.0过渡版）
-   `icml`（[InDesign ICML](https://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/indesign/sdk/cs6/idml/idml-cookbook.pdf)）
-   `ipynb`（[Jupyter笔记本](https://nbformat.readthedocs.io/en/latest/)）
-   `jats_archiving`（[JATS](https://jats.nlm.nih.gov/) XML，归档和交换标记集）
-   `jats_articleauthoring`（[JATS](https://jats.nlm.nih.gov/) XML，文章创作标签集）
-   `jats_publishing`（[JATS](https://jats.nlm.nih.gov/) XML，期刊出版标签集）
-   `jats`（的别名`jats_archiving`）
-   `jira`（[Jira](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all) / Confluence Wiki标记）
-   `json` （本机AST的JSON版本）
-   `latex`（[乳胶](https://www.latex-project.org/)）
-   `man`（[roff man](https://man.cx/groff_man(7))）
-   `markdown`（[Pandoc的Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)）
-   `markdown_mmd`（[MultiMarkdown](https://fletcherpenney.net/multimarkdown/)）
-   `markdown_phpextra`（[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)）
-   `markdown_strict`（原始的未扩展[Markdown](https://daringfireball.net/projects/markdown/)）
-   `mediawiki`（[MediaWiki标记](https://www.mediawiki.org/wiki/Help:Formatting)）
-   `ms`（[roff ms](https://man.cx/groff_ms(7))）
-   `muse`（[缪斯](https://amusewiki.org/library/manual)），
-   `native` （本机Haskell），
-   `odt`（[OpenOffice文本文件](https://en.wikipedia.org/wiki/OpenDocument)）
-   `opml`（[OPML](http://dev.opml.org/spec2.html)）
-   `opendocument`（[OpenDocument](http://opendocument.xml.org/)）
-   `org`（[Emacs组织模式](https://orgmode.org/)）
-   `pdf`（[PDF](https://www.adobe.com/pdf/)）
-   `plain` （纯文本），
-   `pptx`（[PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint)幻灯片放映）
-   `rst`（[reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/introduction.html)）
-   `rtf`（[富文本格式](https://en.wikipedia.org/wiki/Rich_Text_Format)）
-   `texinfo`（[GNU Texinfo](https://www.gnu.org/software/texinfo/)）
-   `textile`（[纺织](https://www.promptworks.com/textile)）
-   `slideous`（[幻灯片](https://goessner.net/articles/slideous/) HTML和JavaScript幻灯片）
-   `slidy`（[滑动式](https://www.w3.org/Talks/Tools/Slidy2/) HTML和JavaScript幻灯片）
-   `dzslides`（[DZSlides](http://paulrouget.com/dzslides/) HTML5 + JavaScript幻灯片），
-   `revealjs`（[manifest.js](https://revealjs.com/) HTML5 + JavaScript幻灯片放映）
-   `s5`（[S5](https://meyerweb.com/eric/tools/s5/) HTML和JavaScript幻灯片放映）
-   `tei`（[TEI简单](https://github.com/TEIC/TEI-Simple)）
-   `xwiki`（[XWiki标记](https://www.xwiki.org/xwiki/bin/view/Documentation/UserGuide/Features/XWikiSyntax/)）
-   `zimwiki`（[ZimWiki标记](https://zim-wiki.org/manual/Help/Wiki_Syntax.html)）
-   自定义Lua编写器的路径，请参见下面的[自定义编写器](https://pandoc.org/MANUAL.html#custom-writers)

需要注意的是`odt`，`docx`，`epub`，和`pdf`输出将不会被定向到*标准输出*，除非被迫[`-o -`](https://pandoc.org/MANUAL.html#option--output)。

扩展名可以通过在格式名称后附加`+EXTENSION`或单独启用或禁用`-EXTENSION`。有关[扩展](https://pandoc.org/MANUAL.html#extensions)及其名称的列表，请参见下面的扩展。请参阅下面的[`--list-output-formats`](https://pandoc.org/MANUAL.html#option--list-output-formats)和[`--list-extensions`](https://pandoc.org/MANUAL.html#option--list-extensions)。

`-o` *文件*，*文件*`--output=`

将输出写入*FILE*而不是*stdout*。如果*FILE*是`-`，输出将转到*标准输出*，即使一个非文本格式（`docx`，`odt`，`epub2`，`epub3`）被指定。

`--data-dir=`*目录*

指定用户数据目录以搜索pandoc数据文件。如果未指定此选项，则将使用默认的用户数据目录。在\* nix和macOS系统上，这将是`pandoc`XDG数据目录的子目录（默认情况下`$HOME/.local/share`，可通过设置`XDG_DATA_HOME`环境变量来覆盖）。如果该目录不存在，`$HOME/.pandoc`将使用（为了向后兼容）。在Windows中，默认用户数据目录为`C:\Users\USERNAME\AppData\Roaming\pandoc`。通过查看的输出，可以找到系统上的默认用户数据目录`pandoc --version`。一`reference.odt`，`reference.docx`，`epub.css`，`templates`，`slidy`，`slideous`，或`s5`放在这个目录下的目录将覆盖pandoc的正常的默认值。

`-d` *文件*，*文件*`--defaults=`

指定一组默认选项设置。*FILE*是一个YAML文件，其字段与命令行选项设置相对应。可以使用默认文件设置用于文档转换的所有选项，包括输入和输出文件。首先在工作目录中搜索文件，然后在`defaults`用户数据目录的子目录中搜索文件（请参阅参考资料[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)）。该`.yaml`扩展名可以省略。有关文件格式的更多信息，请参见[默认文件](https://pandoc.org/MANUAL.html#default-files)部分。来自默认文件的设置可能会被命令行上的后续选项覆盖或扩展。

`--bash-completion`

生成一个bash完成脚本。要使用pandoc启用bash补全功能，请将其添加到您的中`.bashrc`：

```
eval "$(pandoc --bash-completion)"
```

`--verbose`

提供详细的调试输出。

`--quiet`

禁止显示警告消息。

`--fail-if-warnings`

如果有任何警告，则以错误状态退出。

`--log=`*文件*

将机器可读的JSON格式的日志消息写入*FILE*。不管详细级别设置（[`--verbose`](https://pandoc.org/MANUAL.html#option--verbose)，[`--quiet`](https://pandoc.org/MANUAL.html#option--quiet)），都会写入DEBUG级别以上的所有消息。

`--list-input-formats`

列出支持的输入格式，每行一种。

`--list-output-formats`

列出支持的输出格式，每行一种。

`--list-extensions`\[ *格式* \]`=`

列出*FORMAT*支持的扩展名（每行一个），后跟一个`+`或`-`指示是否在*FORMAT中*默认启用了该扩展名。如果未指定*FORMAT*，则会给出pandoc的Markdown的默认值。

`--list-highlight-languages`

列出语法突出显示支持的语言，每行一种。

`--list-highlight-styles`

列出语法突出显示支持的样式，每行一种。请参阅[`--highlight-style`](https://pandoc.org/MANUAL.html#option--highlight-style)。

`-v`， `--version`

打印版本。

`-h`， `--help`

显示使用情况消息。

## 阅读器选项

`--shift-heading-level-by=`*数*

将标题级别移动一个正整数或负整数。例如，使用[`--shift-heading-level-by=-1`](https://pandoc.org/MANUAL.html#option--shift-heading-level-by)，级别2标题变为级别1标题，级别3标题变为级别2标题。标题的级别不能小于1，因此将变为低于1级别的标题成为常规段落。例外：移位-N时，文档开头的N级标题替换了元数据标题。[`--shift-heading-level-by=-1`](https://pandoc.org/MANUAL.html#option--shift-heading-level-by)在转换使用初始级别1标题作为文档标题和级别2+标题作为节的HTML或Markdown文档时，它是一个不错的选择。[`--shift-heading-level-by=1`](https://pandoc.org/MANUAL.html#option--shift-heading-level-by)由于pandoc使用1级标题来呈现文档标题，因此对于将使用部分1级标题的Markdown文档转换为HTML可能是一个不错的选择。

`--base-header-level=`*数*

*不推荐使用。使用[`--shift-heading-level-by`](https://pandoc.org/MANUAL.html#option--shift-heading-level-by)= X代替，其中X = NUM​​BER-1。*指定标题的基本级别（默认为1）。

`--strip-empty-paragraphs`

*不推荐使用。请改用`+empty_paragraphs`扩展名。*忽略没有内容的段落。如果用户使用空的段落来创建段落间空间，则此选项对于转换文字处理文档很有用。

`--indented-code-classes=`*类*

指定用于缩进代码块的类，例如`perl,numberLines`或`haskell`。多个类可以用空格或逗号分隔。

`--default-image-extension=`*延期*

指定图像路径/ URL没有扩展名时要使用的默认扩展名。这使您可以将相同的源用于需要不同类型图像的格式。当前，此选项仅影响Markdown和LaTeX阅读器。

`--file-scope`

在合并多文件文档之前，分别分析每个文件。这将使具有相同标识符的不同文件中的脚注能够按预期工作。如果设置此选项，则脚注和链接将无法跨文件使用。读取二进制文件（docx，odt，epub）意味着[`--file-scope`](https://pandoc.org/MANUAL.html#option--file-scope)。

`-F` *PROGRAM*，*程序*`--filter=`

指定一个可执行文件，将其用作在解析输入之后和写入输出之前转换pandoc AST的筛选器。可执行文件应从stdin读取JSON并将JSON写入stdout。JSON的格式必须类似于pandoc自己的JSON输入和输出。输出格式的名称将作为第一个参数传递到过滤器。因此，

```
pandoc --filter ./caps.py -t latex
```

相当于

```
pandoc -t json | ./caps.py latex | pandoc -f json -t latex
```

后一种形式对于调试过滤器可能有用。

过滤器可以用任何语言编写。`Text.Pandoc.JSON`导出`toJSONFilter`以方便在Haskell中编写过滤器。那些希望用python编写过滤器的人可以使用可[`pandocfilters`](https://github.com/jgm/pandocfilters)从PyPI安装的模块。在[PHP](https://github.com/vinai/pandocfilters-php)，[perl](https://metacpan.org/pod/Pandoc::Filter)和[JavaScript / node.js](https://github.com/mvhenderson/pandoc-filter-node)中也有pandoc过滤器库。

按照优先顺序，pandoc将在以下位置查找过滤器

1.  指定的完整或相对路径（可执行或不可执行）
    
2.  `$DATADIR/filters`（可执行或不可执行）`$DATADIR`用户数据目录在哪里（请参见[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)上文）。
    
3.  `$PATH` （仅可执行）
    

过滤器和Lua过滤器按照命令行上指定的顺序应用。

`-L` *SCRIPT*，*SCRIPT*`--lua-filter=`

以与JSON过滤器类似的方式转换文档（请参阅[`--filter`](https://pandoc.org/MANUAL.html#option--filter)参考资料），但是使用pandoc的内置Lua过滤系统。预期给定的Lua脚本将返回将按顺序应用的Lua过滤器列表。每个Lua过滤器必须包含由AST元素的名称索引的元素转换函数，在该AST元素上应应用过滤器功能。

所述`pandoc`的Lua模块元素创建提供的辅助函数。它总是被加载到脚本的Lua环境中。

以下是用于宏扩展的Lua脚本示例：

```
function expand_hello_world(inline)
  if inline.c == '{{helloworld}}' then
    return pandoc.Emph{ pandoc.Str "Hello, World" }
  else
    return inline
  end
end

return {{Str = expand_hello_world}}
```

为了获得优先顺序，pandoc将在以下位置查找Lua过滤器

1.  指定的完整或相对路径（可执行或不可执行）
    
2.  `$DATADIR/filters`（可执行或不可执行）`$DATADIR`用户数据目录在哪里（请参见[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)上文）。
    

`-M` *KEY* \[ *VAL* \]，*KEY* \[ *VAL* \]`=``--metadata=``:`

将元数据字段*KEY*的值*VAL*。在命令行上指定的值会覆盖使用[YAML元数据块](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)在文档中指定的值。值将被解析为YAML布尔值或字符串值。如果未指定任何值，则该值将被视为布尔值true。像一样[`--variable`](https://pandoc.org/MANUAL.html#option--variable)，[`--metadata`](https://pandoc.org/MANUAL.html#option--metadata)导致设置模板变量。但是，与有所不同[`--variable`](https://pandoc.org/MANUAL.html#option--variable)，它[`--metadata`](https://pandoc.org/MANUAL.html#option--metadata)会影响基础文档的元数据（可从过滤器访问该元数据，并且可能以某些输出格式进行打印），并且将元数据值插入模板后将对其进行转义。

`--metadata-file=`*文件*

从提供的YAML（或JSON）文件中读取元数据。该选项可以与每种输入格式一起使用，但是YAML文件中的字符串标量将始终被解析为Markdown。通常，将以与[YAML元数据块](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)相同的方式处理输入。可以重复使用此选项以包含多个元数据文件。稍后在命令行中指定的文件中的值将优先于先前文件中指定的值。在文档内部指定的元数据值，或者通过使用[`-M`](https://pandoc.org/MANUAL.html#option--metadata)，覆盖此选项指定的值。

`-p`， `--preserve-tabs`

保留制表符，而不是将其转换为空格。（默认情况下，pandoc在解析其输入之前将制表符转换为空格。）请注意，这只会影响文字代码范围和代码块中的制表符。常规文本中的制表符始终被视为空格。

`--tab-stop=`*数*

指定每个选项卡的空格数（默认为4）。

`--track-changes=accept`| `reject`|`all`

指定如何处理由MS Word“跟踪更改”功能产生的插入，删除和注释。`accept`（默认设置），插入所有插入内容，并忽略所有删除内容。`reject`插入所有删除内容，并忽略插入。双方`accept`并`reject`忽略注释。`all`在插入，缺失和评论放，裹在跨，`insertion`，`deletion`，`comment-start`，和`comment-end`分别班。包括作者和更改时间。`all`对于脚本编写很有用：例如，仅接受某个审阅者的更改，例如，在某个日期之前。如果插入或删除了一个段落，则在受影响的段落中断之前`track-changes=all`产生一个带有类`paragraph-insertion`/ 的跨度`paragraph-deletion`。此选项仅影响docx阅读器。

`--extract-media=`*目录*

提取包含在源文档中或从源文档链接到路径*DIR的*图像和其他媒体，并在必要时进行创建，并调整文档中的图像引用，使其指向提取的文件。如果源格式是二进制容器（docx，epub或odt），则从容器中提取媒体，并使用原始文件名。否则，将从文件系统中读取或下载媒体，并根据内容的SHA1哈希值构造新的文件名。

`--abbreviations=`*文件*

指定自定义缩写文件，每行缩写一个。如果未指定此选项，则pandoc将从`abbreviations`用户数据目录中读取数据文件，或使用系统默认值。要查看系统默认值，请使用`pandoc --print-default-data-file=abbreviations`。该列表的唯一使用Pandoc品牌是在Markdown阅读器中。在此列表中找到的以句点结尾的字符串后将带有一个不间断的空格，因此，句点不会以LaTeX之类的格式产生句子结尾的空间。

## 一般作家选项

`-s`， `--standalone`

产生带有适当的页眉和页脚的输出（例如，独立的HTML，LaTeX，TEI或RTF文件，而不是片段）。此选项是自动设置的`pdf`，`epub`，`epub3`，`fb2`，`docx`，和`odt`输出。对于`native`输出，此选项将导致包含元数据。否则，将抑制元数据。

`--template=`*文件* | *网址*

使用指定的文件作为生成文档的自定义模板。暗示[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)。见[模板](https://pandoc.org/MANUAL.html#templates)，下面为模板语法的描述。如果未指定扩展名，则将添加与writer对应的扩展名，以便[`--template=special`](https://pandoc.org/MANUAL.html#option--template)寻找`special.html`HTML输出。如果找不到该模板，则pandoc将`templates`在用户数据目录的子目录中搜索它（请参阅参考资料[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)）。如果不使用此选项，将使用适合于输出格式的默认模板（请参阅参考资料[`-D/--print-default-template`](https://pandoc.org/MANUAL.html#option--print-default-template)）。

`-V` *KEY* \[ *VAL* \]，*KEY* \[ *VAL* \]`=``--variable=``:`

设置模板变量*KEY*的值*VAL*呈现在单机模式下的文档时。如果未指定*VAL*，则将为键赋予value `true`。

`-D` *FORMAT*，*FORMAT*`--print-default-template=`

打印系统默认模板以输出*FORMAT*。（请参阅参考资料，[`-t`](https://pandoc.org/MANUAL.html#option--to)获取可能的*FORMAT*的列表。）用户数据目录中的模板将被忽略。此选项可以与[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)一起使用，以将输出重定向到文件，但是[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)必须[`--print-default-template`](https://pandoc.org/MANUAL.html#option--print-default-template)在命令行之前。

请注意，某些默认模板使用了局部变量，例如`styles.html`。要打印部分，请使用[`--print-default-data-file`](https://pandoc.org/MANUAL.html#option--print-default-data-file)：，例如[`--print-default-data-file=templates/styles.html`](https://pandoc.org/MANUAL.html#option--print-default-data-file)。

`--print-default-data-file=`*文件*

打印系统默认数据文件。用户数据目录中的文件将被忽略。此选项可以与[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)一起使用，以将输出重定向到文件，但是[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)必须[`--print-default-data-file`](https://pandoc.org/MANUAL.html#option--print-default-data-file)在命令行之前。

`--eol=crlf`| `lf`|`native`

手动指定行尾：`crlf`（Windows），`lf`（macOS / Linux / UNIX）或`native`（适合于运行pandoc的操作系统的行尾）。默认值为`native`。

`--dpi`= *NUMBER*

指定默认的dpi（每英寸点数）值，以从像素转换为英寸/厘米，反之亦然。（从技术上讲，正确的术语是ppi：每英寸像素数。）默认值为96dpi。当图像内部包含有关dpi的信息时，将使用编码值，而不是此选项指定的默认值。

`--wrap=auto`| `none`|`preserve`

确定如何在输出中包装文本（源代码，而不是呈现的版本）。使用`auto`（默认值），pandoc将尝试将行换行为[`--columns`](https://pandoc.org/MANUAL.html#option--columns)（默认值72）指定的列宽。使用`none`，pandoc根本不会换行。使用时`preserve`，pandoc将尝试保留源文档的换行（即，源中存在非语义换行符的地方，输出中也将包含非语义换行符）。自动换行当前在HTML输出中不起作用。在`ipynb`输出中，此选项影响降价单元格内容的包装。

`--columns=`*数*

指定字符的行长。这会影响生成的源代码中的文本换行（请参阅参考资料[`--wrap`](https://pandoc.org/MANUAL.html#option--wrap)）。它还影响列的宽度为纯文本表的计算（见[表](https://pandoc.org/MANUAL.html#tables)下文）。

`--toc`， `--table-of-contents`

包括的内容的自动生成的表（或者，在的情况下`latex`，`context`，`docx`，`odt`，`opendocument`，`rst`，或`ms`，一个指令创建一个）的输出文件内。此选项，除非没有效果[`-s/--standalone`](https://pandoc.org/MANUAL.html#option--standalone)时，它有没有影响`man`，`docbook4`，`docbook5`，或`jats`输出。

请注意，如果通过生成PDF `ms`，则目录将出现在文档的开头，标题之前。如果您希望它位于文档末尾，请使用选项[`--pdf-engine-opt=--no-toc-relocation`](https://pandoc.org/MANUAL.html#option--pdf-engine-opt)。

`--toc-depth=`*数*

指定要包含在目录中的部分级别的数量。默认值为3（这意味着将在目录中列出1、2和3级标题）。

`--strip-comments`

在Markdown或Textile源中剥离HTML注释，而不是将它们作为原始HTML传递给Markdown，Textile或HTML输出。如果`markdown_in_html_blocks`未设置扩展名，则不适用于原始HTML块内的HTML注释。

`--no-highlight`

即使给出了语言属性，也禁用代码块和内联的语法高亮显示。

`--highlight-style=`*风格* | *文件*

指定要在突出显示的源代码中使用的着色样式。选项`pygments`（默认）， ，`kate`，`monochrome`，`breezeDark`，`espresso`，`zenburn`，`haddock`和`tango`。有关pandoc中语法突出显示的更多信息，请参见下面的[语法突出显示](https://pandoc.org/MANUAL.html#syntax-highlighting)。另请参阅[`--list-highlight-styles`](https://pandoc.org/MANUAL.html#option--list-highlight-styles)。

可以提供带有扩展名的JSON文件来代替*STYLE*名称`.theme`。这将被解析为KDE语法突出显示主题，并且（如果有效）用作突出显示样式。

要生成现有样式的JSON版本，请使用[`--print-highlight-style`](https://pandoc.org/MANUAL.html#option--print-highlight-style)。

`--print-highlight-style=`*风格* | *文件*

打印突出显示样式的JSON版本，可以对其进行修改，使用`.theme`扩展名保存并与一起使用[`--highlight-style`](https://pandoc.org/MANUAL.html#option--highlight-style)。此选项可以与[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)一起使用，以将输出重定向到文件，但是[`-o`](https://pandoc.org/MANUAL.html#option--output)/ [`--output`](https://pandoc.org/MANUAL.html#option--output)必须[`--print-highlight-style`](https://pandoc.org/MANUAL.html#option--print-highlight-style)在命令行之前。

`--syntax-definition=`*文件*

指示pandoc加载KDE XML语法定义文件，该文件将用于对经过适当标记的代码块进行语法高亮显示。这可用于添加对新语言的支持或对现有语言使用更改的语法定义。可以重复此选项以添加多个语法定义。

`-H` *文件*，*文件* | *网址*`--include-in-header=`

在标头末尾逐字包含*FILE的*内容。例如，它可以用于在HTML文档中包括特殊的CSS或JavaScript。可以重复使用此选项，以在头文件中包含多个文件。它们将以指定的顺序包括在内。暗示[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)。

`-B` *文件*，*文件* | *网址*`--include-before-body=`

在文档正文的开头（例如，在HTML中的标记之后或LaTeX中的命令之后）逐字添加*FILE的*内容。这可用于在HTML文档中包含导航栏或横幅。可以重复使用此选项以包含多个文件。它们将按指定顺序包括在内。暗示。`<body>``\begin{document}`[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)

`-A` *文件*，*文件* | *网址*`--include-after-body=`

在文档正文末尾（在HTML中的标记之前或在LaTeX中的命令之前）逐字添加*FILE的*内容。可以重复使用此选项以包含多个文件。它们将以指定的顺序包括在内。暗示。`</body>``\end{document}`[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)

`--resource-path=`*搜索路径*

搜索图像和其他资源的路径列表。路径应`:`在Linux，UNIX和macOS系统上以及`;`在Windows 上分开。如果[`--resource-path`](https://pandoc.org/MANUAL.html#option--resource-path)未指定，则默认资源路径为工作目录。请注意，如果[`--resource-path`](https://pandoc.org/MANUAL.html#option--resource-path)已指定，则必须明确列出工作目录，否则将不会搜索该目录。例如：[`--resource-path=.:test`](https://pandoc.org/MANUAL.html#option--resource-path)将按`test`该顺序搜索工作目录和子目录。

[`--resource-path`](https://pandoc.org/MANUAL.html#option--resource-path)如果（a）的输出格式中嵌入的图像（例如，只具有一个效果`docx`，`pdf`或`html`用[`--self-contained`](https://pandoc.org/MANUAL.html#option--self-contained)）或（b）它与一起使用[`--extract-media`](https://pandoc.org/MANUAL.html#option--extract-media)。

`--request-header=`*NAME* *VAL*`:`

发出HTTP请求时（例如，在命令行上指定URL或必须下载文档中使用的资源时），将请求标头*NAME*的值设置为*VAL*。如果您位于代理后面，则还需要将环境变量设置`http_proxy`为`http://...`。

`--no-check-certificate`

禁用证书验证，以允许访问不安全的HTTP资源（例如，当证书不再有效或自签名时）。

## 影响特定作者的选项

`--self-contained`

使用`data:`URI合并链接的脚本，样式表，图像和视频的内容，生成没有外部依赖性的独立HTML文件。暗示[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)。生成的文件应该是“自包含的”，从某种意义上说，它不需要外部文件，也不需要网络访问即可由浏览器正确显示。此选项仅适用于HTML输出格式，包括`html4`，`html5`，`html+lhs`，`html5+lhs`，`s5`，`slidy`，`slideous`，`dzslides`，和`revealjs`。绝对URL上的脚本，图像和样式表将被下载；将相对于工作目录（如果第一个源文件是本地文件）或相对于基本URL（如果第一个源文件是远程文件）来查找相对URL处的文件。具有属性的元素`data-external="1"`将独自一人; 他们链接到的文档将不包含在文档中。限制：无法合并通过JavaScript动态加载的资源；结果，[`--self-contained`](https://pandoc.org/MANUAL.html#option--self-contained)不能使用[`--mathjax`](https://pandoc.org/MANUAL.html#option--mathjax)，并且某些高级功能（例如，缩放或扬声器注释）在离线“自包含” `reveal.js`幻灯片放映中可能无法使用。

`--html-q-tags`

将`<q>`标记用于HTML中的引号。

`--ascii`

在输出中仅使用ASCII字符。当前支持XML和HTML格式（选择此选项时使用实体而不是UTF-8），CommonMark，gfm和Markdown（使用实体），roff ms（使用十六进制转义）以及在一定程度上支持LaTeX （在可能的情况下，将标准命令用于重音字符）。roff man输出默认情况下使用ASCII。

`--reference-links`

在编写Markdown或reStructuredText时，使用引用样式的链接而不是内联的链接。默认情况下，使用内联链接。链接引用的位置受该[`--reference-location`](https://pandoc.org/MANUAL.html#option--reference-location)选项影响。

`--reference-location = block`| `section`|`document`

指定是否将脚注（和参考，如果`reference-links`已设置）放置在当前（顶层）块，当前节或文档的末尾。默认值为`document`。当前仅影响降价编写器。

`--atx-headers`

在Markdown输出中使用ATX样式的标题。默认设置是将setext样式的标题用于1到2级，然后使用ATX标题。（注意：对于`gfm`输出，始终使用ATX标题。）此选项还会影响`ipynb`输出中的降价单元。

`--top-level-division=[default|section|chapter|part]`

将顶级标题视为LaTeX，ConTeXt，DocBook和TEI输出中的给定分区类型。层次结构的顺序是：部分，章节，然后是部分；所有标题均会发生移动，以使顶级标题成为指定的类型。默认行为是通过试探法确定最佳划分类型：除非适用其他条件，否则将`section`选择。当`documentclass`变量设置为`report`，`book`或时`memoir`（除非`article`指定了选项），`chapter`隐含为该选项的设置。如果`beamer`输出格式为，则指定`chapter`或`part`将导致顶级标题变为`\part{..}`，而第二级标题保留为默认类型。

`-N`， `--number-sections`

LaTeX，ConTeXt，HTML，Docx或EPUB输出中的数字部分标题。默认情况下，部分未编号。`unnumbered`即使[`--number-sections`](https://pandoc.org/MANUAL.html#option--number-sections)已指定，带有class的节也不会编号。

`--number-offset=`*NUMBER* \[ *NUMBER* *…* \]`,``,`

HTML输出中节标题的偏移量（在其他输出格式中忽略）。对于顶级标题，第一个数字添加到节号中，对于第二级标题，第二个添加到节号中，依此类推。因此，例如，如果您希望文档中的第一个顶级标题编号为“ 6”，请指定[`--number-offset=5`](https://pandoc.org/MANUAL.html#option--number-offset)。如果您的文档以2级标题开头，您希望将其编号为“ 1.5” [`--number-offset=1,4`](https://pandoc.org/MANUAL.html#option--number-offset)。默认情况下，偏移量为0。暗示[`--number-sections`](https://pandoc.org/MANUAL.html#option--number-sections)。

`--listings`

将[`listings`](https://ctan.org/pkg/listings)软件包用于LaTeX代码块。该软件包不支持源代码的多字节编码。要处理UTF-8，您将需要使用自定义模板。该问题已在此处完整记录：[清单包的编码问题](https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings#Encoding_issue)。

`-i`， `--incremental`

使幻灯片放映中的列表项逐渐显示（一个一个）。默认值为一次显示所有列表。

`--slide-level=`*数*

指定以指定级别的标题创建幻灯片（为`beamer`，`s5`，`slidy`，`slideous`，`dzslides`）。层次结构中高于此级别的标题用于将幻灯片放映分为几部分；低于此级别的标题将在幻灯片中创建子标题。请注意，幻灯片级别标题下未包含的内容将不会显示在幻灯片中。默认设置是根据文档的内容设置幻灯片级别；请参阅“ [构造幻灯片放映”](https://pandoc.org/MANUAL.html#structuring-the-slide-show)。

`--section-divs`

在`<section>`标签（或的`<div>`标签`html4`）中包装节，然后将标识符附加到封闭的`<section>`（或`<div>`）而不是标题本身。请参阅下面的[标题标识符](https://pandoc.org/MANUAL.html#heading-identifiers)。

`--email-obfuscation=none`| `javascript`|`references`

指定用于混淆`mailto:`HTML文档中链接的方法。`none`保持`mailto:`链接不变。`javascript`使用JavaScript对其进行混淆。`references`通过将其字母打印为十进制或十六进制字符引用来对其进行混淆。默认值为`none`。

`--id-prefix=`*串*

指定要添加到HTML和DocBook输出中的所有标识符和内部链接以及Markdown和Haddock输出中的脚注编号的前缀。当生成要包含在其他页面中的片段时，这对于防止重复的标识符很有用。

`-T` *STRING*，*STRING*`--title-prefix=`

将*STRING*指定为出现在HTML标头中的标题开头的前缀（但不要指定为出现在HTML正文开头的标题中的前缀）。暗示[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)。

`-c` *URL*，*URL*`--css=`

链接到CSS样式表。可以重复使用此选项以包含多个文件。它们将按指定顺序包括在内。

生成EPUB需要样式表。如果使用此选项（或`css`或`stylesheet`元数据字段）未提供任何内容，则pandoc将`epub.css`在用户数据目录中查找文件（请参阅参考资料[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)）。如果在此处找不到，将使用合理的默认值。

`--reference-doc=`*文件*

在生成docx或ODT文件时，请使用指定的文件作为样式参考。

Docx

为了获得最佳结果，参考docx应该是使用pandoc生成的docx文件的修改版本。参考docx的内容将被忽略，但新docx中将使用其样式表和文档属性（包括边距，页面大小，页眉和页脚）。如果在命令行上未指定参考docx，则pandoc将`reference.docx`在用户数据目录中查找文件（请参阅参考资料[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)）。如果也没有找到，将使用合理的默认值。

要产生一个习惯`reference.docx`，首先要得到一个默认的副本`reference.docx`：`pandoc -o custom-reference.docx --print-default-data-file reference.docx`。然后`custom-reference.docx`在Word中打开，根据需要修改样式，然后保存文件。为了获得最佳结果，请勿修改此文件，除非修改pandoc使用的样式：

段落样式：

-   正常
-   主体
-   第一段
-   紧凑
-   标题
-   字幕
-   作者
-   日期
-   抽象
-   参考书目
-   标题1
-   标题2
-   标题3
-   标题4
-   标题5
-   标题6
-   标题7
-   标题8
-   标题9
-   阻止文字
-   脚注文字
-   定义词
-   定义
-   标题
-   表格标题
-   图片说明
-   数字
-   字幕图
-   TOC标题

字符样式：

-   默认段落字体
-   正文文字字符
-   逐字记录
-   脚注参考
-   超连结
-   部门编号

桌子风格：

-   表

ODT

为了获得最佳结果，参考ODT应该是使用pandoc生成的ODT的修改版本。参考ODT的内容将被忽略，但其样式表将在新的ODT中使用。如果在命令行上未指定参考ODT，则pandoc将`reference.odt`在用户数据目录中查找文件（请参阅参考资料[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)）。如果也没有找到，将使用合理的默认值。

要产生一个习惯`reference.odt`，首先要得到一个默认的副本`reference.odt`：`pandoc -o custom-reference.odt --print-default-data-file reference.odt`。然后`custom-reference.odt`在LibreOffice中打开，根据需要修改样式，然后保存文件。

微软幻灯片软件

Microsoft PowerPoint 2013附带的模板（带有扩展名`.pptx`或`.potx`扩展名）都可以正常工作，大多数从这些模板派生的模板也可以正常工作。

具体要求是模板应从以下前四个布局开始：

1.  标题幻灯片
2.  标题和内容
3.  节头
4.  两种内容

最新版本的MS PowerPoint随附的所有模板均符合这些条件。（您可以单击菜单`Layout`下的`Home`进行检查。）

您还可以修改默认值`reference.pptx`：首先运行`pandoc -o custom-reference.pptx --print-default-data-file reference.pptx`，然后`custom-reference.pptx`在MS PowerPoint中进行修改（如上所述，pandoc将使用前四个布局幻灯片）。

`--epub-cover-image=`*文件*

使用指定的图像作为EPUB封面。建议图像的宽度和高度小于1000px。请注意，在Markdown源文档中，您还可以`cover-image`在YAML元数据块中指定（请参见下面的[EPUB元数据](https://pandoc.org/MANUAL.html#epub-metadata)）。

`--epub-metadata=`*文件*

在指定的XML文件中查找EPUB的元数据。该文件应包含一系列[Dublin Core元素](https://www.dublincore.org/specifications/dublin-core/dces/)。例如：

```
 <dc:rights>Creative Commons</dc:rights>
 <dc:language>es-AR</dc:language>
```

默认情况下，pandoc将包含以下元数据元素：（`<dc:title>`来自文档标题），`<dc:creator>`（来自文档作者），`<dc:date>`（来自文档日期，应采用[ISO 8601格式](https://www.w3.org/TR/NOTE-datetime)），`<dc:language>`（来自`lang`变量，如果不是）设置，语言环境）和`<dc:identifier id="BookId">`（随机生成的UUID）。这些元素中的任何一个都可以被元数据文件中的元素覆盖。

注意：如果源文档是Markdown，则可以改用文档中的YAML元数据块。请参见下面的[EPUB元数据](https://pandoc.org/MANUAL.html#epub-metadata)。

`--epub-embed-font=`*文件*

将指定的字体嵌入到EPUB中。可以重复此选项以嵌入多种字体。也可以使用通配符：例如，`DejaVuSans-*.ttf`。但是，如果在命令行上使用通配符，请确保对通配符进行转义或将整个文件名放在单引号中，以防止shell解释通配符。要使用嵌入字体，您需要在CSS中添加如下声明[`--css`](https://pandoc.org/MANUAL.html#option--css)：

```
@font-face {
font-family: DejaVuSans;
font-style: normal;
font-weight: normal;
src:url("DejaVuSans-Regular.ttf");
}
@font-face {
font-family: DejaVuSans;
font-style: normal;
font-weight: bold;
src:url("DejaVuSans-Bold.ttf");
}
@font-face {
font-family: DejaVuSans;
font-style: italic;
font-weight: normal;
src:url("DejaVuSans-Oblique.ttf");
}
@font-face {
font-family: DejaVuSans;
font-style: italic;
font-weight: bold;
src:url("DejaVuSans-BoldOblique.ttf");
}
body { font-family: "DejaVuSans"; }
```

`--epub-chapter-level=`*数*

指定将EPUB分成单独的“章节”文件的标题级别。默认设置是在第1级标题下分成几章。此选项仅影响EPUB的内部组成，而不会影响向用户显示章节的方式。如果章节文件太大，某些读者可能会很慢，因此对于标题级别很少的大型文档，一个人可能希望使用章节级别2或3。

`--epub-subdirectory=`*DIRNAME*

在OCF容器中指定用于保存EPUB特定内容的子目录。默认值为`EPUB`。要将EPUB内容放在顶层，请使用空字符串。

`--ipynb-output=all|none|best`

确定如何处理ipynb输出单元。`all`表示保留原始文件中包含的所有数据格式。`none`表示省略数据单元的内容。`best`使pandoc尝试在与输出格式兼容的每个输出单元中选择最丰富的数据块。默认值为`best`。

`--pdf-engine=`*程序*

产生PDF输出时，请使用指定的引擎。有效值为`pdflatex`，`lualatex`，`xelatex`，`latexmk`，`tectonic`，`wkhtmltopdf`，`weasyprint`，`prince`，`context`，和`pdfroff`。如果引擎不在您的PATH中，则可以在此处指定引擎的完整路径。如果未指定此选项，则pandoc将使用以下默认值，具体取决于使用以下命令指定的输出格式[`-t/--to`](https://pandoc.org/MANUAL.html#option--to)：

-   [`-t latex`](https://pandoc.org/MANUAL.html#option--to)或无：`pdflatex`（其他的选项：`xelatex`，`lualatex`，`tectonic`，`latexmk`）
-   [`-t context`](https://pandoc.org/MANUAL.html#option--to)： `context`
-   [`-t html`](https://pandoc.org/MANUAL.html#option--to)：（`wkhtmltopdf`其他选项：[；；](https://print-css.rocks/)有关从HTML / CSS生成PDF的详细介绍`prince`，`weasyprint`请参见[print-css.rocks](https://print-css.rocks/)。）
-   [`-t ms`](https://pandoc.org/MANUAL.html#option--to)： `pdfroff`

`--pdf-engine-opt=`*串*

使用给定的字符串作为的命令行参数`pdf-engine`。例如，要将永久目录`foo`用于`latexmk`的辅助文件，请使用[`--pdf-engine-opt=-outdir=foo`](https://pandoc.org/MANUAL.html#option--pdf-engine-opt)。请注意，不检查重复选项。

## 引文渲染

`--bibliography=`*文件*

将`bibliography`文档的元数据中的字段设置为*FILE*，覆盖元数据中设置的任何值，然后使用来处理引用`pandoc-citeproc`。（等效于[`--metadata bibliography=FILE --filter pandoc-citeproc`](https://pandoc.org/MANUAL.html#option--metadata)。）如果未提供[`--natbib`](https://pandoc.org/MANUAL.html#option--natbib)或[`--biblatex`](https://pandoc.org/MANUAL.html#option--biblatex)也`pandoc-citeproc`未使用，则使其等效于[`--metadata bibliography=FILE`](https://pandoc.org/MANUAL.html#option--metadata)。如果您多次提供此参数，则每个*FILE*都会添加到书目中。

`--csl=`*文件*

将`csl`文档的元数据中的字段设置为*FILE*，以覆盖元数据中设置的任何值。（等效于[`--metadata csl=FILE`](https://pandoc.org/MANUAL.html#option--metadata)。）此选项仅与有关`pandoc-citeproc`。

`--citation-abbreviations=`*文件*

将`citation-abbreviations`文档的元数据中的字段设置为*FILE*，以覆盖元数据中设置的任何值。（等效于[`--metadata citation-abbreviations=FILE`](https://pandoc.org/MANUAL.html#option--metadata)。）此选项仅与有关`pandoc-citeproc`。

`--natbib`

使用[`natbib`](https://ctan.org/pkg/natbib)在LaTeX的输出引用。此选项不适用于`pandoc-citeproc`过滤器或PDF输出。它旨在用于生成可以使用处理的LaTeX文件[`bibtex`](https://ctan.org/pkg/bibtex)。

`--biblatex`

使用[`biblatex`](https://ctan.org/pkg/biblatex)在LaTeX的输出引用。此选项不适用于`pandoc-citeproc`过滤器或PDF输出。它旨在用于生成可以使用[`bibtex`](https://ctan.org/pkg/bibtex)或处理的LaTeX文件[`biber`](https://ctan.org/pkg/biber)。

## HTML中的数学渲染

默认设置是使用Unicode字符尽可能多地渲染TeX数学。公式放在`span`with中`class="math"`，这样，如果需要，它们的样式可以与周围的文本不同。但是，这仅会为基本数学给出可接受的结果，通常您将要使用[`--mathjax`](https://pandoc.org/MANUAL.html#option--mathjax)或下列其他选项。

`--mathjax`\[ *网址* \]`=`

使用[MathJax](https://www.mathjax.org/)在HTML输出中显示嵌入式TeX数学。TeX数学将介于`\(...\)`（对于内联数学）或`\[...\]`（对于显示数学）之间，并包装在`<span>`带有class的标签中`math`。然后，MathJax JavaScript将呈现它。该*URL*应指向`MathJax.js`加载脚本。如果未提供*URL*，将插入到Cloudflare CDN的链接。

`--mathml`

转换的TeX数学来[MATHML](https://www.w3.org/Math/)（在`epub3`，`docbook4`，`docbook5`，`jats`，`html4`和`html5`）。这是`odt`输出中的默认设置。请注意，当前只有Firefox和Safari（以及某些电子书阅读器）本身支持MathML。

`--webtex`\[ *网址* \]`=`

将TeX公式转换为`<img>`标签，这些标签链接到将公式转换为图像的外部脚本。该公式将经过URL编码，并与提供的URL串联在一起。对于SVG图片，您可以使用[`--webtex https://latex.codecogs.com/svg.latex?`](https://pandoc.org/MANUAL.html#option--webtex)。如果未指定URL，将使用生成CodeCogs URL的PNG（`https://latex.codecogs.com/png.latex?`）。注意：该[`--webtex`](https://pandoc.org/MANUAL.html#option--webtex)选项将影响Markdown的输出以及HTML，如果您要定位的Markdown版本没有本机数学支持，则此选项将很有用。

`--katex`\[ *网址* \]`=`

使用[KaTeX](https://github.com/Khan/KaTeX)在HTML输出中显示嵌入式TeX数学。该*URL*是KaTeX库的基本URL。该目录应包含`katex.min.js`和`katex.min.css`文件。如果未提供*URL*，将插入指向KaTeX CDN的链接。

`--gladtex`

`<eq>`在HTML输出的标签中包含TeX数学。然后，[GladTeX](https://humenda.github.io/GladTeX/)可以处理生成的HTML，以生成排版公式的图像以及带有指向这些图像的链接的HTML文件。因此，过程为：

```
pandoc -s --gladtex input.md -o myfile.htex
gladtex -d myfile-images myfile.htex
# produces myfile.html and images in myfile-images
```

## 包装器脚本的选项

`--dump-args`

将有关命令行参数的信息*输出*到*stdout*，然后退出。此选项主要用于包装脚本中。输出的第一行包含使用该[`-o`](https://pandoc.org/MANUAL.html#option--output)选项指定的输出文件的名称，如果未指定输出文件，则为`-`（对于*stdout*）。其余各行包含命令行参数，每行一个，按其出现的顺序排列。这些不包括常规的pandoc选项及其参数，但包括`--`在行尾的分隔符之后出现的所有选项。

`--ignore-args`

忽略命令行参数（用于包装脚本）。常规pandoc选项不会被忽略。因此，例如

```
pandoc --ignore-args -o foo.html -s foo.txt -- -e latin1
```

相当于

```
pandoc -o foo.html -s
```

# 退出码

如果pandoc成功完成，它将返回退出代码0。非零退出代码具有以下含义：

| 码 | 错误 |
| --- | --- |
| 3 | PandocFailOnWarningError |
| 4 | PandocAppError |
| 5 | PandocTemplateError |
| 6 | PandocOptionError |
| 21 | PandocUnknownReaderError |
| 22 | PandocUnknownWriterError |
| 23 | PandocUnsupportedExtensionError |
| 31 | PandocEpubSubdirectoryError |
| 43 | PandocPDFError |
| 47 | PandocPDFProgramNotFoundError |
| 61 | PandocHttpError |
| 62 | PandocShouldNeverHappenError |
| 63 | PandocSomeError |
| 64 | PandocParseError |
| 65岁 | PandocParsecError |
| 66 | PandocMakePDFError |
| 67 | PandocSyntaxMapError |
| 83 | PandocFilterError |
| 91 | 潘多克宏循环 |
| 92 | PandocUTF8DecodingError |
| 93 | PandocIpynbDecodingError |
| 97 | PandocCouldNotFindDataFileError |
| 99 | PandocResourceNotFound |

# 默认文件

该[`--defaults`](https://pandoc.org/MANUAL.html#option--defaults)选项可用于指定选项包。这是一个示例默认文件，演示了所有可能使用的字段：

```
from: markdown+emoji
# reader: may be used instead of from:
to: html5
# writer: may be used instead of to:

# leave blank for output to stdout:
output-file:
# leave blank for input from stdin, use [] for no input:
input-files:
- preface.md
- content.md
# or you may use input-file: with a single value

template: letter
standalone: true
self-contained: false

# note that structured variables may be specified:
variables:
  documentclass: book
  classoption:
    - twosides
    - draft

# metadata values specified here are parsed as literal
# string text, not markdown:
metadata:
  author:
  - Sam Smith
  - Julie Liu
metadata-files:
- boilerplate.yaml
# or you may use metadata-file: with a single value

# Note that these take files, not their contents:
include-before-body: []
include-after-body: []
include-in-header: []
resource-path: ["."]

# filters will be assumed to be Lua filters if they have
# the .lua extension, and json filters otherwise.  But
# the filter type can also be specified explicitly, as shown:
filters:
- pandoc-citeproc
- wordcount.lua
- type: json
  path: foo.lua

file-scope: false

data-dir:

# ERROR, WARNING, or INFO
verbosity: INFO
log-file: log.json

# citeproc, natbib, or biblatex
cite-method: citeproc
# part, chapter, section, or default:
top-level-division: chapter
abbreviations:

pdf-engine: pdflatex
pdf-engine-opts:
- "-shell-escape"
# you may also use pdf-engine-opt: with a single option
# pdf-engine-opt: "-shell-escape"

# auto, preserve, or none
wrap: auto
columns: 78
dpi: 72

extract-media: mediadir

table-of-contents: true
toc-depth: 2
number-sections: false
# a list of offsets at each heading level
number-offset: [0,0,0,0,0,0]
# toc: may also be used instead of table-of-contents:
shift-heading-level-by: 1
section-divs: true
identifier-prefix: foo
title-prefix: ""
strip-empty-paragraphs: true
# lf, crlf, or native
eol: lf
strip-comments: false
indented-code-classes: []
ascii: true
default-image-extension: ".jpg"

# either a style name of a style definition file:
highlight-style: pygments
syntax-definitions:
- c.xml
# or you may use syntax-definition: with a single value
listings: false

reference-doc: myref.docx

# method is plain, webtex, gladtex, mathml, mathjax, katex
# you may specify a url with webtex, mathjax, katex
html-math-method:
  method: mathjax
  url: "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
# none, references, or javascript
email-obfuscation: javascript

tab-stop: 8
preserve-tabs: true

incremental: false
slide-level: 2

epub-subdirectory: EPUB
epub-metadata: meta.xml
epub-fonts:
- foobar.otf
epub-chapter-level: 1
epub-cover-image: cover.jpg

reference-links: true
# block, section, or document
reference-location: block
atx-headers: false

# accept, reject, or all
track-changes: accept

html-q-tags: false
css:
- site.css

# none, all, or best
ipynb-output: best

# A list of two-element lists
request-headers:
- ["User-Agent", "Mozilla/5.0"]

fail-if-warnings: false
dump-args: false
ignore-args: false
trace: false
```

省略的字段将只有其常规默认值。因此，默认文件可以很简单：

```
verbosity: INFO
```

可以将默认文件放在`defaults`用户数据目录的子目录中，并可以在任何目录中使用它们。例如，可以创建一个文件，指定用于写字母的默认值，将其保存为用户数据目录`letter.yaml`的`defaults`子目录，然后使用`pandoc --defaults letter`或从任何目录中调用这些默认值`pandoc -dletter`。

当使用多个默认值时，它们的内容将被合并。

需要注意的是，这里的命令行参数可以重复（[`--metadata-file`](https://pandoc.org/MANUAL.html#option--metadata-file)，[`--css`](https://pandoc.org/MANUAL.html#option--css)，[`--include-in-header`](https://pandoc.org/MANUAL.html#option--include-in-header)，[`--include-before-body`](https://pandoc.org/MANUAL.html#option--include-before-body)，[`--include-after-body`](https://pandoc.org/MANUAL.html#option--include-after-body)，[`--variable`](https://pandoc.org/MANUAL.html#option--variable)，[`--metadata`](https://pandoc.org/MANUAL.html#option--metadata)，[`--syntax-definition`](https://pandoc.org/MANUAL.html#option--syntax-definition)），在命令行上指定的值将与缺省文件中指定的值进行组合，而不是替换它们。

# 范本

使用该[`-s/--standalone`](https://pandoc.org/MANUAL.html#option--standalone)选项时，pandoc使用模板添加独立文档所需的页眉和页脚材料。要查看使用的默认模板，只需键入

```
pandoc -D *FORMAT*
```

其中*FORMAT*是输出格式的名称。可以使用[`--template`](https://pandoc.org/MANUAL.html#option--template)选项指定自定义模板。您还可以通过将文件放在用户数据目录中来覆盖给定输出格式*FORMAT*的系统默认模板`templates/default.*FORMAT*`（请参见[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)上文）。*例外情况：*

-   对于`odt`输出，请自定义`default.opendocument`模板。
-   对于`pdf`输出，自定义`default.latex`模板（或`default.context`模板，如果你使用[`-t context`](https://pandoc.org/MANUAL.html#option--to)，或`default.ms`模板，如果你使用[`-t ms`](https://pandoc.org/MANUAL.html#option--to)，或`default.html`模板，如果你使用[`-t html`](https://pandoc.org/MANUAL.html#option--to)）。
-   `docx`并且`pptx`没有模板（但是，您可以用[`--reference-doc`](https://pandoc.org/MANUAL.html#option--reference-doc)来自定义输出）。

模板包含*变量*，这些*变量*允许在文件的任何位置包含任意信息。可以使用[`-V/--variable`](https://pandoc.org/MANUAL.html#option--variable)选项在命令行中设置它们。如果未设置变量，则pandoc将在文档的元数据中寻找密钥，可以使用[YAML元数据块](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)或使用该[`-M/--metadata`](https://pandoc.org/MANUAL.html#option--metadata)选项进行设置。此外，pandoc还为某些变量提供了默认值。见[变量](https://pandoc.org/MANUAL.html#variables)下面的pandoc的默认模板中使用的变量列表。

如果使用自定义模板，则可能需要在pandoc更改时对其进行修改。我们建议跟踪默认模板中的更改，并相应地修改自定义模板。一种简单的方法是派生[pandoc-templates](https://github.com/jgm/pandoc-templates)储存库，并在每个pandoc发布后合并更改。

## 模板语法

### 注释

序列`$--`和行尾之间的任何内容都将被视为注释，并从输出中省略。

### 定界符

为了在模板中标记变量和控制结构，可以使用`$`… `$`或`${`… `}`作为分隔符。样式也可以混合在同一模板中，但是每种情况下，开始和结束定界符必须匹配。分隔符后面可能跟着一个或多个空格或制表符，这些空格或制表符将被忽略。结束定界符后可以跟一个或多个空格或制表符，这些空格或制表符将被忽略。

要`$`在文档中包含文字，请使用`$$`。

### 内插变量

内插变量的槽是变量名，由匹配的定界符包围。变量名必须以字母开头，可以包含字母，数字`_`，`-`和`.`。关键字`it`，`if`，`else`，`endif`，`for`，`sep`，并且`endfor`可以不使用作为变量名。例子：

```
$foo$
$foo.bar.baz$
$foo_bar.baz-bim$
$ foo $
${foo}
${foo.bar.baz}
${foo_bar.baz-bim}
${ foo }
```

带句点的变量名称用于获取结构化变量值。因此，例如，`employee.salary`将返回`salary`对象字段的值，即`employee`字段的值。

-   如果变量的值为简单值，则将逐字呈现。（请注意，没有进行转义；假定调用程序将为输出格式适当地对字符串进行转义。）
-   如果值是列表，则将这些值连接在一起。
-   如果该值为地图，`true`则将呈现字符串。
-   每隔一个值将被呈现为空字符串。

### 有条件的

有条件的以`if(variable)`（以匹配的定界符括起来）开始，以（以匹配的定界符括起来）结束`endif`。它可以可选地包含一个`else`（用匹配的定界符括起来）。`if`如果该部分`variable`具有非空值，则使用该`else`部分；否则，使用该部分（如果存在）。例子：

```
$if(foo)$bar$endif$

$if(foo)$
  $foo$
$endif$

$if(foo)$
part one
$else$
part two
$endif$

${if(foo)}bar${endif}

${if(foo)}
  ${foo}
${endif}

${if(foo)}
${ foo.bar }
${else}
no foo!
${endif}
```

关键字`elseif`可以用于简化复杂的嵌套条件：

```
$if(foo)$
XXX
$elseif(bar)$
YYY
$else$
ZZZ
$endif$
```

### 对于循环

for循环以`for(variable)`（包围在分隔符中）开始，以（包围在分隔符中）结束`endfor`。

-   如果`variable`为数组，则将反复评估循环内的材料，并将其`variable`依次设置为数组的每个值并进行连接。
-   如果`variable`是地图，则内部材质将设置为地图。
-   如果关联变量的值不是数组或映射，则将对其值执行一次迭代。

例子：

```
$for(foo)$$foo$$sep$, $endfor$

$for(foo)$
  - $foo.last$, $foo.first$
$endfor$

${ for(foo.bar) }
  - ${ foo.bar.last }, ${ foo.bar.first }
${ endfor }

$for(mymap)$
$it.name$: $it.office$
$endfor$
```

您可以选择使用`sep`（用匹配的定界符括起来）在连续值之间指定分隔符。`sep`和之间的材料`endfor`是分隔符。

```
${ for(foo) }${ foo }${ sep }, ${ endfor }
```

代替`variable`在循环内部使用，`it`可以使用特殊的回指关键字。

```
${ for(foo.bar) }
  - ${ it.last }, ${ it.first }
${ endfor }
```

### 部分

可以使用部分的名称来包含部分（存储在不同文件中的子模板）`()`，例如后跟，例如：

```
${ styles() }
```

将在包含主模板的目录中查找部分内容。如果没有扩展名，则假定文件名具有与主模板相同的扩展名。调用部分文件时，也可以使用全名，包括文件扩展名：

```
${ styles.html() }
```

（如果在模板的目录中找不到部分，则还将`templates`在用户数据目录的子目录中查找它。）

可以选择使用分号将分号应用于变量：

```
${ date:fancy() }

${ articles:bibentry() }
```

如果`articles`是一个数组，它将遍历它的值，将partial `bibentry()`应用于每个数组。因此，上面的第二个示例等效于

```
${ for(articles) }
${ it:bibentry() }
${ endfor }
```

请注意，`it`迭代局部词时必须使用anaphoric关键字。在以上示例中，`bibentry`partial应该包含`it.title`（依此类推）而不是`articles.title`。

最终的换行符从部分中省略。

局部可以包括其他局部。

可以在变量名或部分变量之后的方括号中指定数组值之间的分隔符：

```
${months[, ]}$

${articles:bibentry()[; ]$
```

在这种情况下，分隔符是文字的，并且（与`sep`显式`for`循环不同）不能包含插值变量或其他模板指令。

### 套料

为确保内容“嵌套”，即缩进后几行，请使用以下`^`指令：

```
$item.number$  $^$$item.description$ ($item.price$)
```

在此示例中，如果`item.description`有多行，则将全部缩进以与第一行对齐：

```
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
```

要将多行嵌套到同一级别，请使其与`^`模板中的指令对齐。例如：

```
$item.number$  $^$$item.description$ ($item.price$)
               (Available til $item.sellby$.)
```

将产生

```
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
       (Available til March 30, 2020.)
```

如果变量本身在一行上出现，并在其前面加上空格，而后没有同一行中的其他文本或指令，并且该变量的值包含多行，则它将自动嵌套。

### 易碎空间

通常，模板本身中的空格（与插值变量的值相反）是不可破坏的，但是可以通过使用`~`关键字（以另一个结尾`~`）使它们在模板的一部分中可破坏。

```
$~$This long line may break if the document is rendered
with a short line length.$~$
```

### 管子

管道可转换变量或部分变量的值。`/`在变量名称（或部分名称）和管道名称之间使用斜杠（）指定管道。例：

```
$for(name)$
$name/uppercase$
$endfor$

$for(metadata/pairs)$
- $it.key$: $it.value$
$endfor$

$employee:name()/uppercase$
```

管道可以链在一起：

```
$for(employees/pairs)$
$it.key/alpha/uppercase$. $it.name$
$endfor$
```

一些管道采用参数：

```
|----------------------|------------|
$for(employee)$
$it.name.first/uppercase/left 20 "| "$$it.name.salary/right 10 " | " " |"$
$endfor$
|----------------------|------------|
```

当前，以下管道是预定义的：

-   `pairs`：将地图或数组转换为地图数组，每个都有`key`和`value`字段。如果原始值为数组，`key`则将为数组索引，从1开始。
    
-   `uppercase`：将文本转换为大写。
    
-   `lowercase`：将文本转换为小写。
    
-   `length`：返回值的长度：文本值的字符数，映射或数组的元素数。
    
-   `reverse`：反转文本值或数组，并且对其他值没有影响。
    
-   `first`：返回数组的第一个值（如果应用于非空数组）；否则返回原始值。
    
-   `last`：返回数组的最后一个值（如果应用于非空数组）；否则返回原始值。
    
-   `rest`：返回数组中除第一个值以外的所有值（如果应用于非空数组）；否则返回原始值。
    
-   `allbutlast`：返回数组的最后一个值（如果应用于非空数组）；否则返回原始值。
    
-   `chomp`：删除结尾的换行符（和易碎的空格）。
    
-   `nowrap`：禁用易碎空间上的换行。
    
-   `alpha`：将可以作为整数读取的文本值转换为小写字母字符`a..z`（mod 26）。这可用于从数组索引中获取字母枚举。要获取大写字母，请与链接`uppercase`。
    
-   `roman`：将可以作为整数读取的文本值转换为小写的罗马数字。这可用于从数组索引中获取字母枚举。要获取大写罗马字母，请与链接`uppercase`。
    
-   `left n "leftborder" "rightborder"`：以宽度为一个块的形式呈现文本值，该块`n`与左侧对齐，并带有可选的左右边框。对其他值没有影响。可用于对齐表格中的材料。宽度是表示字符数的正整数。边界是双引号内的字符串。文字`"`和`\`字符必须使用反斜杠转义。
    
-   `right n "leftborder" "rightborder"`：以一个宽度块呈现一个文本值，该块的宽度`n`向右对齐，并且不影响其他值。
    
-   `center n "leftborder" "rightborder"`：以宽度为一块的文本值呈现文本`n`，并与中心对齐，并且对其他值没有影响。
    

## 变数

### 元数据变量

`title`，`author`，`date`

允许识别文档的基本方面。通过LaTeX和ConTeXt包含在PDF元数据中。这些可以通过允许多位作者的[pandoc标题块](https://pandoc.org/MANUAL.html#extension-pandoc_title_block)或[YAML元数据块设置](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)：

```
---
author:
- Aristotle
- Peter Abelard
...
```

请注意，如果你只是想设置PDF或HTML元数据，不包括文档本身的标题栏，你可以设置`title-meta`，`author-meta`以及`date-meta`变量。（默认情况下，这些都是自动设置的基础上`title`，`author`和`date`）。

`subtitle`

文档字幕，包含在HTML，EPUB，LaTeX，ConTeXt和docx文档中

`abstract`

文档摘要，包含在LaTeX，ConTeXt，AsciiDoc和docx文档中

`keywords`

HTML，PDF，ODT，pptx，docx和AsciiDoc元数据中包含的关键字列表；重复`author`以上

`subject`

文档主题，包含在ODT，PDF，docx和pptx元数据中

`description`

文档描述，包含在ODT，docx和pptx元数据中。一些应用程序将此显示为`Comments`元数据。

`category`

文档类别，包含在docx和pptx元数据中

此外，未包含在ODT，docx或pptx元数据中的任何根级别字符串元数据都将作为*自定义属性*添加。例如，以下[YAML](https://yaml.org/spec/1.2/spec.html "YAML v1.2规范")元数据块：

```
---
title:  'This is the title'
subtitle: "This is the subtitle"
author:
- Author One
- Author Two
description: |
    This is a long
    description.

    It consists of two paragraphs
...
```

将包括`title`，`author`和`description`作为标准文档属性和`subtitle`转换为DOCX，ODT或PPTX当作为自定义属性。

### 语言变量

`lang`

使用IETF语言标签（遵循[BCP 47](https://tools.ietf.org/html/bcp47)标准）识别文档的主要语言，例如`en`或`en-GB`。该[语言的子标签查找](https://r12a.github.io/app-subtags/)工具可以查找或验证这些标记。这会影响大多数格式，并在使用LaTeX（通过[`babel`](https://ctan.org/pkg/babel)和[`polyglossia`](https://ctan.org/pkg/polyglossia)）或ConTeXt 时控制PDF输出中的断字。

将本机pandoc Div [和Spans](https://pandoc.org/MANUAL.html#divs-and-spans)与`lang`属性一起使用以切换语言：

```
---
lang: en-GB
...

Text in the main document language (British English).

::: {lang=fr-CA}
> Cette citation est écrite en français canadien.
:::

More text in English. ['Zitat auf Deutsch.']{lang=de}
```

`dir`

基本脚本方向`rtl`（从右到左）或`ltr`（从左到右）。

对于双向文档，具有某些属性（值或）的本机pandoc `span`和`div`s 可用于在某些输出格式中覆盖基本方向。如果最终的渲染器（例如，在生成HTML时的浏览器）支持[Unicode双向算法](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)，则不一定总是需[要这样做](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)。`dir``rtl``ltr`[](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics)

将LaTeX用于双向文档时，仅`xelatex`完全支持引擎（使用[`--pdf-engine=xelatex`](https://pandoc.org/MANUAL.html#option--pdf-engine)）。

### HTML数学变量

`classoption`

使用[KaTeX时](https://pandoc.org/MANUAL.html#option--katex)，可以使用[YAML元数据](https://pandoc.org/MANUAL.html#layout)或使用来使显示数学方程向左[平移](https://pandoc.org/MANUAL.html#option--katex)[`-M classoption=fleqn`](https://pandoc.org/MANUAL.html#option--metadata)。

### HTML幻灯片的变量

当[使用pandoc制作幻灯片](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc)时，这些会影响HTML输出。

所有[Reveal.js配置选项](https://revealjs.com/config/)都可以作为变量使用。要关闭在show.js中默认为true的布尔标志，请使用`0`。

`revealjs-url`

manifest.js文档的基本网址（默认为`https://unpkg.com/reveal.js@^4/`）

`s5-url`

S5文档的基本URL（默认为`s5/default`）

`slidy-url`

Slidy文档的基本网址（默认为`https://www.w3.org/Talks/Tools/Slidy2`）

`slideous-url`

滑动文档的基本网址（默认为`slideous`）

`title-slide-attributes`

manifest.js幻灯片的标题幻灯片的其他属性。有关[示例，](https://pandoc.org/MANUAL.html#background-in-reveal.js-and-beamer)请参见[reveal.js和beamer中的背景](https://pandoc.org/MANUAL.html#background-in-reveal.js-and-beamer)。

### Beamer幻灯片的变量

这些变量使用更改PDF幻灯片的外观[`beamer`](https://ctan.org/pkg/beamer)。

`aspectratio`

幻灯片宽高比（`43`对于4：3 \[默认\]，`169`对于16：9，`1610`对于16:10，`149`对于14：9，`141`对于1.41：1，`54`对于5：4，`32`对于3：2）

`beamerarticle`

从Beamer幻灯片制作文章

`beameroption`

添加额外的投影仪选项 `\setbeameroption{}`

`institute`

作者单位：有多个作者时可以列出

`logo`

幻灯片的徽标图像

`navigation`

控制导航符号（默认为`empty`用于没有导航符号;其他有效的值是`frame`，`vertical`和`horizontal`）

`section-titles`

为新部分启用“标题页”（默认为true）

`theme`，`colortheme`，`fonttheme`，`innertheme`，`outertheme`

投影仪主题

`themeoptions`

LaTeX Beamer主题的选项（列表）。

`titlegraphic`

标题幻灯片的图像

### PowerPoint的变量

这些变量控制着幻灯片的视觉效果，而这些视觉效果很难通过模板来控制。

`monofont`

用于代码的字体。

### LaTeX的变量

Pandoc在使用LaTeX引擎[创建PDF](https://pandoc.org/MANUAL.html#creating-a-pdf)时会使用这些变量。

#### 布局

`block-headings`

让`\paragraph`与`\subparagraph`（第四和第五级标题，或五，六水平书类），自立，而不是磨合; 需要进一步的格式以区别于`\subsubsection`（第三或第四级标题）。代替使用此选项，[KOMA-Script](https://ctan.org/pkg/koma-script)可以更广泛地调整标题：

```
---
documentclass: scrartcl
header-includes: |
  \RedeclareSectionCommand[
    beforeskip=-10pt plus -2pt minus -1pt,
    afterskip=1sp plus -1sp minus 1sp,
    font=\normalfont\itshape]{paragraph}
  \RedeclareSectionCommand[
    beforeskip=-10pt plus -2pt minus -1pt,
    afterskip=1sp plus -1sp minus 1sp,
    font=\normalfont\scshape,
    indent=0pt]{subparagraph}
...
```

`classoption`

文档类的选项，例如  `oneside`；对多个选项重复：

```
---
classoption:
- twocolumn
- landscape
...
```

`documentclass`

文档类：通常的标准类之一，[`article`](https://ctan.org/pkg/article)，[`book`](https://ctan.org/pkg/book)，和[`report`](https://ctan.org/pkg/report); 所述[KOMA脚本](https://ctan.org/pkg/koma-script)当量，`scrartcl`，`scrbook`，和`scrreprt`，其中默认为更小的空间; 要么[`memoir`](https://ctan.org/pkg/memoir)

`geometry`

[`geometry`](https://ctan.org/pkg/geometry)包装选项，例如  `margin=1in`; 对多个选项重复：

```
---
geometry:
- top=30mm
- left=20mm
- heightrounded
...
```

`hyperrefoptions`

[`hyperref`](https://ctan.org/pkg/hyperref)包装选项，例如  `linktoc=all`; 对多个选项重复：

```
---
hyperrefoptions:
- linktoc=all
- pdfwindowui
- pdfpagemode=FullScreen
...
```

`indent`

使用文档类设置进行缩进（默认的LaTeX模板否则会删除缩进并在段落之间添加空格）

`linestretch`

使用[`setspace`](https://ctan.org/pkg/setspace)软件包调整行距，例如  `1.25`，`1.5`

`margin-left`，`margin-right`，`margin-top`，`margin-bottom`

设置边距（如果`geometry`未使用）（否则`geometry`覆盖这些边距）

`pagestyle`

control `\pagestyle{}`：默认的文章类支持`plain`（默认），`empty`（无标题或页码）和`headings`（标题中的节标题）

`papersize`

纸张尺寸，例如  `letter`，`a4`

`secnumdepth`

部分的编号深度（带有[`--number-sections`](https://pandoc.org/MANUAL.html#option--number-sections)选项或`numbersections`变量）

#### 字型

`fontenc`

允许通过`fontenc`包（带有`pdflatex`）指定字体编码；默认值为`T1`（请参阅[LaTeX字体编码指南](https://ctan.org/pkg/encguide)）

`fontfamily`

使用的字体包`pdflatex`：[TeX Live](https://www.tug.org/texlive/)包含许多选项，这些选项记录在[LaTeX字体目录中](https://tug.org/FontCatalogue/)。默认值为[Latin Modern](https://ctan.org/pkg/lm)。

`fontfamilyoptions`

包的选项用作`fontfamily`; 为多个选项重复。例如，要在包中将Libertine字体与小写比例的数字（旧式）一起使用[`libertinus`](https://ctan.org/pkg/libertinus)：

```
---
fontfamily: libertinus
fontfamilyoptions:
- osf
- p
...
```

`fontsize`

正文的字体大小。标准类允许10pt，11pt和12pt。要使用其他大小，请设置`documentclass`为[KOMA-Script](https://ctan.org/pkg/koma-script)类之一，例如`scrartcl`或`scrbook`。

`mainfont`，`sansfont`，`monofont`，`mathfont`，`CJKmainfont`

`xelatex`或一起使用的字体家族`lualatex`：使用[`fontspec`](https://ctan.org/pkg/fontspec)软件包获取任何系统字体的名称。`CJKmainfont`使用[`xecjk`](https://ctan.org/pkg/xecjk)包装。

`mainfontoptions`，`sansfontoptions`，`monofontoptions`，`mathfontoptions`，`CJKoptions`

选择与使用`mainfont`，`sansfont`，`monofont`，`mathfont`，`CJKmainfont`中`xelatex`和`lualatex`。允许通过以下方式进行任何选择[`fontspec`](https://ctan.org/pkg/fontspec)：为多个选项重复。例如，要使用具有小写字母的[Palaxino](http://www.gust.org.pl/projects/e-foundry/tex-gyre)的[TeX Gyre](http://www.gust.org.pl/projects/e-foundry/tex-gyre)版本：

```
---
mainfont: TeX Gyre Pagella
mainfontoptions:
- Numbers=Lowercase
- Numbers=Proportional
...
```

`microtypeoptions`

传递给微型包装的选项

#### 链接

`colorlinks`

为链接文本添加颜色；自动启用如果任何`linkcolor`，`filecolor`，`citecolor`，`urlcolor`，或`toccolor`设置

`linkcolor`，`filecolor`，`citecolor`，`urlcolor`，`toccolor`

颜色为内部链接，外部链接，引文链接，链接的URL，并链接在的内容时，分别表：用途选择由允许[`xcolor`](https://ctan.org/pkg/xcolor)，包括`dvipsnames`，`svgnames`和`x11names`列表

`links-as-notes`

使链接被打印为脚注

#### 前事

`lof`， `lot`

包括图列表，表列表

`thanks`

标题后的确认脚注内容

`toc`

包含目录（也可以使用设置[`--toc/--table-of-contents`](https://pandoc.org/MANUAL.html#option--toc)）

`toc-depth`

目录中包含的部分级别

#### BibLaTeX参考书目

当使用BibLaTeX进行[引文渲染](https://pandoc.org/MANUAL.html#citation-rendering)时，这些变量将起作用。

`biblatexoptions`

biblatex的选项列表

`biblio-style`

书目风格（与[`--natbib`](https://pandoc.org/MANUAL.html#option--natbib)和一起使用时）[`--biblatex`](https://pandoc.org/MANUAL.html#option--biblatex)。

`biblio-title`

参考书目标题（与[`--natbib`](https://pandoc.org/MANUAL.html#option--natbib)和一起使用时）[`--biblatex`](https://pandoc.org/MANUAL.html#option--biblatex)。

`bibliography`

参考文献用于解决参考文献

`natbiboptions`

natbib的选项列表

### ConTeXt的变量

Pandoc使用ConTeXt [创建PDF](https://pandoc.org/MANUAL.html#creating-a-pdf)时会使用这些变量。

`fontsize`

正文文本的字体大小（例如  `10pt`，`12pt`）

`headertext`， `footertext`

放置在运行页眉或页脚中的文本（请参见[ConTeXt页眉和页脚](https://wiki.contextgarden.net/Headers_and_Footers)）；对于不同的位置，最多重复四次

`indenting`

控制段落的缩进，例如  `yes,small,next`（请参见[ConTeXt缩进](https://wiki.contextgarden.net/Indentation)）；对多个选项重复

`interlinespace`

调整行距，例如  `4ex`（使用[`setupinterlinespace`](https://wiki.contextgarden.net/Command/setupinterlinespace)）；对多个选项重复

`layout`

页边距和文本排列的选项（请参见[ConTeXt布局](https://wiki.contextgarden.net/Layout)）；对多个选项重复

`linkcolor`， `contrastcolor`

页面外部和内部链接的颜色，例如  `red`，`blue`（请参见[ConTeXt Color](https://wiki.contextgarden.net/Color)）

`linkstyle`

对于链接字体样式，例如  `normal`，`bold`，`slanted`，`boldslanted`，`type`，`cap`，`small`

`lof`， `lot`

包括图列表，表列表

`mainfont`，`sansfont`，`monofont`，`mathfont`

字体系列：使用任何系统字体的名称（请参阅[ConTeXt字体切换](https://wiki.contextgarden.net/Font_Switching)）

`margin-left`，`margin-right`，`margin-top`，`margin-bottom`

设置边距（如果`layout`未使用）（否则将`layout`覆盖这些边距）

`pagenumbering`

页码样式和位置（使用[`setuppagenumbering`](https://wiki.contextgarden.net/Command/setuppagenumbering)）；对多个选项重复

`papersize`

纸张尺寸，例如  `letter`，`A4`，`landscape`（见[上下文纸张设置](https://wiki.contextgarden.net/PaperSetup)）; 对多个选项重复

`pdfa`

增加了前同步码的设置需要生成PDF /的类型的指定，例如  `1a:2005`，`2a`。如果未指定任何类型（即，例如通过YAML元数据块[`--metadata=pdfa`](https://pandoc.org/MANUAL.html#option--metadata)或`pdfa: true`在YAML元数据块`1b:2005`中将其值设置为True  ），则出于向后兼容的原因，它将用作默认值。[`--variable=pdfa`](https://pandoc.org/MANUAL.html#option--variable)不支持不指定值使用。要成功生成PDF / A，必须提供所需的ICC颜色配置文件，并且内容和所有包含的文件（例如图像）必须符合标准。可以使用`pdfaiccprofile`和来指定ICC配置文件和输出意图`pdfaintent`。有关更多详细信息，另请参见[ConTeXt PDFA](https://wiki.contextgarden.net/PDF/A)。

`pdfaiccprofile`

与结合使用时`pdfa`，指定要在PDF中使用的ICC配置文件，例如  `default.cmyk`。如果未指定，`sRGB.icc`则用作默认值。可以重复以包含多个配置文件。请注意，概要文件必须在系统上可用。可以从[ConTeXt ICC配置文件中](https://wiki.contextgarden.net/PDFX#ICC_profiles)获取它们。

`pdfaintent`

当与结合使用时`pdfa`，指定颜色的输出意图，例如，  `ISO coated v2 300\letterpercent\space (ECI)`如果未指定，`sRGB IEC61966-2.1`则用作默认值。

`toc`

包含目录（也可以使用设置[`--toc/--table-of-contents`](https://pandoc.org/MANUAL.html#option--toc)）

`whitespace`

段落之间的间距，例如  `none`，`small`（使用[`setupwhitespace`](https://wiki.contextgarden.net/Command/setupwhitespace)）

`includesource`

将所有源文档作为文件附件包括在PDF文件中

### 的变量 `wkhtmltopdf`

当Pandoc使用这些变量[创建PDF](https://pandoc.org/MANUAL.html#creating-a-pdf)使用[`wkhtmltopdf`](https://wkhtmltopdf.org/)。该[`--css`](https://pandoc.org/MANUAL.html#option--css)选项还会影响输出。

`footer-html`， `header-html`

将信息添加到页眉和页脚

`margin-left`，`margin-right`，`margin-top`，`margin-bottom`

设置页边距

`papersize`

设置PDF纸张尺寸

### 手册页变量

`adjusting`

将文本调整为左边（`l`），右边（`r`），中心（`c`）或两个（`b`）边距

`footer`

手册页中的页脚

`header`

手册页中的标题

`hyphenate`

如果`true`（默认），将使用连字符

`section`

手册页中的节号

### ms的变量

`fontfamily`

字体系列（例如  `T`或`P`）

`indent`

段落缩进（例如  `2m`）

`lineheight`

线高（例如  `12p`）

`pointsize`

点大小（例如  `10p`）

### 变量自动设置

Pandoc会根据[选项](https://pandoc.org/MANUAL.html#options)或文档内容自动设置这些变量。用户也可以修改它们。这些取决于输出格式，并且包括以下内容：

`body`

文件主体

`date-meta`

`date`转换为ISO 8601 YYYY-MM-DD 的变量，包含在所有基于HTML的格式（dzslides，epub，html，html4，html5，re揭示js，s5，slideous，slidy）中。识别出的格式`date`是：`mm/dd/yyyy`，`mm/dd/yy`，`yyyy-mm-dd`（ISO 8601）， `dd MM yyyy`（例如，任一`02 Apr 2018`或`02 April 2018`）， `MM dd, yyyy`（例如，  `Apr. 02, 2018`或`April 02, 2018),`YYYY \[毫米\[DD\]\]\] `(e.g.`20180402，`201804`或`2018`）。

`header-includes`

指定的内容[`-H/--include-in-header`](https://pandoc.org/MANUAL.html#option--include-in-header)（可能有多个值）

`include-before`

指定的内容[`-B/--include-before-body`](https://pandoc.org/MANUAL.html#option--include-before-body)（可能有多个值）

`include-after`

指定的内容[`-A/--include-after-body`](https://pandoc.org/MANUAL.html#option--include-after-body)（可能有多个值）

`meta-json`

所有文档元数据的JSON表示形式。字段值将转换为所选的输出格式。

`numbersections`

如果[`-N/--number-sections`](https://pandoc.org/MANUAL.html#option--number-sections)指定了 非空值

`sourcefile`， `outputfile`

源和目标文件名，如命令行所示。`sourcefile`如果输入来自多个文件，也可以是列表；如果输入来自标准输入，则也可以为空。您可以在模板中使用以下代码片段来区分它们：

```
$if(sourcefile)$
$for(sourcefile)$
$sourcefile$
$endfor$
$else$
(stdin)
$endif$
```

同样，如果输出到终端，`outputfile`也可以`-`。

如果需要绝对路径，请使用例如  `$curdir$/$sourcefile$`。

`curdir`

运行pandoc的工作目录。

`toc`

如果[`--toc/--table-of-contents`](https://pandoc.org/MANUAL.html#option--toc)指定了 非空值

`toc-title`

目录标题（仅适用于EPUB，HTML，opendocument，odt，docx，pptx，beamer，LaTeX）

# 扩展名

某些读者和作家的行为可以通过启用或禁用各种扩展来进行调整。

扩展名可以通过添加`+EXTENSION`格式名称来启用，而扩展名可以通过添加来禁用`-EXTENSION`。例如，[`--from markdown_strict+footnotes`](https://pandoc.org/MANUAL.html#option--from)启用脚注的是严格的Markdown，而[`--from markdown-footnotes-pipe_tables`](https://pandoc.org/MANUAL.html#option--from)没有脚注或管道表的Pandoc的Markdown是。

降价阅读器和编写器到目前为止最多都使用扩展。因此只使用它们扩展覆盖在部分[Pandoc的降价](https://pandoc.org/MANUAL.html#pandocs-markdown)以下（见[降价变种](https://pandoc.org/MANUAL.html#markdown-variants)的`commonmark`和`gfm`。）在下面，这也为其他格式的工作覆盖扩展。

请注意，添加到`ipynb`格式的markdown扩展会影响Jupyter笔记本中的Markdown单元（如命令行选项一样[`--atx-headers`](https://pandoc.org/MANUAL.html#option--atx-headers)）。

## 版式

#### 延期： `smart`

将直引号解释为卷曲引号，`---`破折号，`--`破折号和`...`省略号。在某些缩写（例如“先生”）之后插入不间断空格。

可以为以下格式启用/禁用此扩展名：

输入格式

`markdown`，`commonmark`，`latex`，`mediawiki`，`org`，`rst`，`twiki`

输出格式

`markdown`，`latex`，`context`，`rst`

默认启用

`markdown`，`latex`，`context`（输入和输出）

注意：如果您正在*编写* Markdown，则`smart`扩展名会产生相反的效果：原本是弯引号的内容会直接显示出来。

在LaTeX中，`smart`是指对引号（` `` `以及`''`双引号`` ` ``和`'`单引号）和破折号（`--`对于破折号和`---`破折号）使用标准的TeX连字。如果`smart`被禁用，那么在阅读LaTeX时，pandoc将按字面意义解析这些字符。在编写LaTeX时，`smart`enable告诉pandoc在可能的情况下使用连字；如果`smart`禁用，则pandoc将使用Unicode引号和破折号字符。

## 标题和章节

#### 延期： `auto_identifiers`

没有明确指定标识符的标题将根据标题文本自动分配一个唯一的标识符。

可以为以下格式启用/禁用此扩展名：

输入格式

`markdown`，`latex`，`rst`，`mediawiki`，`textile`

输出格式

`markdown`， `muse`

默认启用

`markdown`， `muse`

用于从标题文本中获取标识符的默认算法是：

-   删除所有格式，链接等。
-   删除所有脚注。
-   删除所有非字母数字字符，下划线，连字符和点号除外。
-   用连字符替换所有空格和换行符。
-   将所有字母字符转换为小写。
-   删除所有内容，直到第一个字母为止（标识符不能以数字或标点符号开头）。
-   如果在此之后什么也没留下，请使用标识符`section`。

因此，例如

| 标题 | 识别码 |
| --- | --- |
| `Heading identifiers in HTML` | `heading-identifiers-in-html` |
| `Maître d'hôtel` | `maître-dhôtel` |
| `*Dogs*?--in *my* house?` | `dogs--in-my-house` |
| `[HTML], [S5], or [RTF]?` | `html-s5-or-rtf` |
| `3. Applications` | `applications` |
| `33` | `section` |

在大多数情况下，这些规则应允许人们根据标题文本确定标识符。例外的是几个标题具有相同的文本。在这种情况下，第一个将获得如上所述的标识符；第二个将获得相同的标识符并`-1`附加；第三与`-2`; 等等。

（但是，如果`gfm_auto_identifiers`启用，则使用其他算法；请参阅下文。）

这些标识符用于在[`--toc|--table-of-contents`](https://pandoc.org/MANUAL.html#option--toc)选项生成的目录中提供链接目标。它们还使提供从文档的一个部分到另一部分的链接变得容易。例如，指向此部分的链接可能如下所示：

```
See the section on
[heading identifiers](#heading-identifiers-in-html-latex-and-context).
```

但是请注意，这种提供指向节的链接的方法仅适用于HTML，LaTeX和ConTeXt格式。

如果[`--section-divs`](https://pandoc.org/MANUAL.html#option--section-divs)指定了选项，则每个节都将被包裹在`section`（或`div`，如果`html4`指定了）中，并且标识符将附加到封闭的`<section>`（或`<div>`）标签上，而不是标题本身。这样就可以使用JavaScript操纵整个部分，或在CSS中对它们进行不同的处理。

#### 延期： `ascii_identifiers`

导致由产生的标识符 `auto_identifiers`为纯ASCII。带有重音拉丁字母的重音被去除，非拉丁字母被省略。

#### 延期： `gfm_auto_identifiers`

更改所使用的算法`auto_identifiers`以符合GitHub的方法。空格将被转换为破折号（`-`），大写字符将转换为小写字符，并且标点符号除`-`和外将`_`被删除。表情符号将替换为其名称。

## 数学输入

扩展名[`tex_math_dollars`](https://pandoc.org/MANUAL.html#extension-tex_math_dollars)，[`tex_math_single_backslash`](https://pandoc.org/MANUAL.html#extension-tex_math_single_backslash)和[`tex_math_double_backslash`](https://pandoc.org/MANUAL.html#extension-tex_math_double_backslash)在有关Pandoc的Markdown的部分中进行了描述。

但是，它们也可以与HTML输入一起使用。例如，这对于读取使用MathJax格式化的网页非常方便。

## 原始HTML / TeX

以下扩展在[Pandoc的Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)的相应部分中进行了详细说明：

-   [`raw_html`](https://pandoc.org/MANUAL.html#extension-raw_html)允许将在pandoc的AST中无法表示的HTML元素解析为原始HTML。默认情况下，禁用HTML输入。
    
-   [`raw_tex`](https://pandoc.org/MANUAL.html#extension-raw_tex)允许将原始LaTeX，TeX和ConTeXt包含在文档中。可以为以下格式（除了`markdown`）启用/禁用此扩展名：
    
    输入格式
    
    `latex`，`org`，`textile`，`html`（环境，`\ref`和`\eqref`只），`ipynb`
    
    输出格式
    
    `textile`， `commonmark`
    
    注意：作为施加到`ipynb`，`raw_html`并`raw_tex`在降价细胞不仅影响原料的TeX，但与MIME数据类型`text/html`中的输出单元。由于`ipynb`读者会在给出多个选项时尝试保留尽可能丰富的输出，因此，如果禁用`raw_html`并`raw_tex`转换为`docx`不允许使用raw `html`或的格式，则会获得最佳结果`tex`。
    
-   [`native_divs`](https://pandoc.org/MANUAL.html#extension-native_divs)导致将HTML `div`元素解析为本地pandoc Div块。如果希望将它们解析为原始HTML，请使用[`-f html-native_divs+raw_html`](https://pandoc.org/MANUAL.html#option--from)。
    
-   [`native_spans`](https://pandoc.org/MANUAL.html#extension-native_spans)导致将HTML `span`元素解析为本地pandoc Span内联。如果希望将它们解析为原始HTML，请使用[`-f html-native_spans+raw_html`](https://pandoc.org/MANUAL.html#option--from)。如果你想删除所有`div`S和`span`转换HTML到降价当s，你可以使用`pandoc -f html-native_divs-native_spans -t markdown`。
    

## 精通Haskell支持

#### 延期： `literate_haskell`

将文档视为识字的Haskell来源。

可以为以下格式启用/禁用此扩展名：

输入格式

`markdown`，`rst`，`latex`

输出格式

`markdown`，`rst`，`latex`，`html`

如果您将`+lhs`（或`+literate_haskell`）附加到上述格式之一，则pandoc会将文档视为识字的Haskell源。这意味着

-   在Markdown输入中，“鸟追踪”部分将被解析为Haskell代码，而不是块引用。之间的文本`\begin{code}`，并`\end{code}`也将被视为Haskell代码。对于ATX样式的标题，将使用字符'='代替'＃'。
    
-   在Markdown输出中，具有类`haskell`和代码块的代码块`literate`将使用鸟形轨迹进行渲染，并且块引号将缩进一个空格，因此不会被视为Haskell代码。此外，标题将显示为setext样式（带有下划线），而不是ATX样式（带有'＃'字符）。（这是因为ghc将第1列中的'＃'字符视为引入行号。）
    
-   在重组的文本输入中，“鸟类追踪”部分将被解析为Haskell代码。
    
-   在重组文本输出中，具有类的代码块`haskell`将使用鸟形轨迹进行渲染。
    
-   在LaTeX输入中，`code`环境中的文本将被解析为Haskell代码。
    
-   在LaTeX输出中，具有类的代码块`haskell`将在`code`环境中呈现。
    
-   在HTML输出中，具有class的代码块`haskell`将使用class `literatehaskell`和bird轨迹呈现。
    

例子：

```
pandoc -f markdown+lhs -t html
```

读取使用Markdown约定格式化的识字Haskell源代码，并编写普通的HTML（无任何跟踪）。

```
pandoc -f markdown+lhs -t html+lhs
```

用Haskell代码在鸟径中编写HTML，因此可以将其复制并粘贴为识字的Haskell源代码。

请注意，GHC希望在第一列中显示鸟类轨迹，因此，Haskell编译器不会拾取缩进的识字代码块（例如，在逐项环境中）。

## 其他扩展

#### 延期： `empty_paragraphs`

允许为空的段落。默认情况下，空的段落被忽略。

可以为以下格式启用/禁用此扩展名：

输入格式

`docx`， `html`

输出格式

`docx`，`odt`，`opendocument`，`html`

#### 延期： `native_numbering`

启用图形和表格的本地编号。枚举从1开始。

可以为以下格式启用/禁用此扩展名：

输出格式

`odt`， `opendocument`

#### 延期： `styles` {＃ext-styles}

从docx转换时，无论pandoc是否理解这些样式的含义，都应将所有docx样式读为div（用于段落样式）和span（用于字符样式）。可以与[docx自定义样式](https://pandoc.org/MANUAL.html#custom-styles)一起使用。默认禁用。

输入格式

`docx`

#### 延期： `amuse`

在`muse`输入格式中，这将启用Text :: Amuse扩展至Emacs Muse标记。

#### 延期： `raw_markdown`

在`ipynb`输入格式中，这会导致Markdown单元作为原始Markdown块包含在内（允许无损往返）而不是被解析。仅在定位`ipynb`或基于降价的输出格式时使用此格式。

#### 延期： `citations`

输入中还接受[Pandoc的Markdown引用语法的](https://pandoc.org/MANUAL.html#citations)某些方面`org`。

#### 延期： `ntb`

在`context`输出格式中，这允许使用[自然表（TABLE）](https://wiki.contextgarden.net/TABLE)而不是默认的[极端表（xtables）](https://wiki.contextgarden.net/xtables)。自然表允许进行更细粒度的全局自定义，但与极限表相比会降低性能。

# 潘多克的降价促销

Pandoc了解John Gruber的[Markdown](https://daringfireball.net/projects/markdown/)语法的扩展版本和稍作修订的版本。本文档说明了语法，并指出了与标准Markdown的区别。除非另有说明，否则可以通过使用`markdown_strict`格式代替来抑制这些差异`markdown`。可以启用或禁用扩展以更精细地指定行为。它们在下面描述。另见[扩展](https://pandoc.org/MANUAL.html#extensions)上面，用于扩展这项工作也对其他格式。

## 哲学

Markdown的设计易于编写，更重要的是，易于阅读：

> Markdown格式的文档应以纯文本形式原样发布，而不会看起来像被标签或格式说明所标记。– [约翰·格鲁伯](https://daringfireball.net/projects/markdown/syntax#philosophy)

该原则指导pandoc决定查找表，脚注和其他扩展名的语法。

但是，在一个方面，潘多克的目标与Markdown的原始目标有所不同。Markdown最初是为考虑HTML生成而设计的，而pandoc是为多种输出格式而设计的。因此，尽管pandoc允许嵌入原始HTML，但不鼓励使用它，并提供了其他非HTMLish的方式来表示重要的文档元素，例如定义列表，表格，数学和脚注。

## 段落

段落是一行或多行文本，后接一个或多个空行。换行符被视为空格，因此您可以根据需要对段落进行重排。如果需要强行换行，请在行尾放置两个或多个空格。

#### 延期： `escaped_line_breaks`

反斜杠后跟换行符也是强行换行。注意：在多行和网格表单元格中，这是创建硬断行的唯一方法，因为单元格中的尾部空格将被忽略。

## 标题

标题有两种：Setext和ATX。

### Setext样式的标题

setext样式的标题是一行带下划线（带有下划线）的文本行，其中带有一排`=`符号（用于第一级标题）或`-`符号（用于第二级标题）：

```
A level-one heading
===================

A level-two heading
-------------------
```

标题文本可以包含内联格式，例如强调（请参见下面的[内联格式](https://pandoc.org/MANUAL.html#inline-formatting)）。

### ATX样式的标题

ATX样式的标题由一到六个`#`符号和一行文本组成，可以选择后面跟任意数量的`#`符号。行首的`#`符号数是标题级别：

```
## A level-two heading

### A level-three heading ###
```

与setext样式的标题一样，标题文本可以包含格式：

```
# A level-one heading with a [link](/url) and *emphasis*
```

#### 延期： `blank_before_header`

标准Markdown语法在标题之前不需要空白行。Pandoc确实需要这样做（当然，在文档开头除外）。要求的原因是，很容易`#`因意外（可能通过换行）而结束在行的开头。考虑例如：

```
I like several of their flavors of ice cream:
#22, for example, and #5.
```

#### 延期： `space_in_atx_header`

许多降价的实现不需要开口部之间的空间`#`的ATX标题和标题文本的S，以便`#5 bolt`和`#hashtag`算作标题。通过此扩展，pandoc确实需要空间。

### 标题标识符

另请参见上面的[`auto_identifiers`扩展名](https://pandoc.org/MANUAL.html#extension-auto_identifiers)。

#### 延期： `header_attributes`

可以在包含标题文本的行的末尾使用以下语法为标题分配属性：

```
{#identifier .class .class key=value key=value}
```

因此，例如，以下标题将全部分配有标识符`foo`：

```
# My heading {#foo}

## My heading ##    {#foo}

My other heading   {#foo}
---------------
```

（此语法与[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)兼容。）

请注意，尽管此语法允许分配类和键/值属性，但编写者通常不会使用所有这些信息。标识符，类和键/值属性用于HTML和基于HTML的格式，例如EPUB和slidy。标识符用于LaTeX，ConTeXt，Textile，Jira标记和AsciiDoc编写器中的标签和链接锚。

`unnumbered`即使[`--number-sections`](https://pandoc.org/MANUAL.html#option--number-sections)已指定，该类别的标题也不会编号。`-`属性上下文中的单个连字符（）等效于`.unnumbered`，并且在非英语文档中更可取。所以，

```
# My heading {-}
```

与...相同

```
# My heading {.unnumbered}
```

如果`unlisted`除之外还存在该类`unnumbered`，则标题将不包含在目录中。（当前仅针对某些格式实现此功能：基于LaTeX和HTML，PowerPoint和RTF的格式。）

#### 延期： `implicit_header_references`

Pandoc的行为就像为每个标题定义了参考链接。因此，要链接到标题

```
# Heading identifiers in HTML
```

你可以简单地写

```
[Heading identifiers in HTML]
```

要么

```
[Heading identifiers in HTML][]
```

要么

```
[the section on heading identifiers][heading identifiers in
HTML]
```

而不是明确给出标识符：

```
[Heading identifiers in HTML](#heading-identifiers-in-html)
```

如果有多个标题相同的标题，则相应的引用将仅链接到第一个，并且如上所述，您将需要使用显式链接来链接到其他标题。

像常规参考链接一样，这些参考不区分大小写。

显式链接引用定义始终优先于隐式标题引用。因此，在以下示例中，链接将指向`bar`，而不是`#foo`：

```
# Foo

[foo]: bar

See [foo]
```

## 块报价

Markdown使用电子邮件约定来引用文本块。块引号是一个或多个段落或其他块元素（例如列表或标题），每行前都有一个`>`字符和一个可选的空格。（`>`不必从左边距开始，但是缩进不应超过三个空格。）

```
> This is a block quote. This
> paragraph has two lines.
>
> 1. This is a list inside a block quote.
> 2. Second item.
```

`>`也允许使用“惰性”形式，该形式仅在每个块的第一行要求字符：

```
> This is a block quote. This
paragraph has two lines.

> 1. This is a list inside a block quote.
2. Second item.
```

可以包含在块引用中的块元素中还有其他块引用。也就是说，可以嵌套块引号：

```
> This is a block quote.
>
> > A block quote within a block quote.
```

如果`>`字符后跟可选空格，则该空格将被视为块引号标记的一部分，而不是内容缩进的一部分。因此，要将缩进的代码块放在块引号中，您需要在空格后加上五个空格`>`：

```
>     code
```

#### 延期： `blank_before_blockquote`

标准Markdown语法在块引号之前不需要空白行。Pandoc确实需要这样做（当然，在文档开头除外）。要求的原因是，很容易`>`因意外（可能通过换行）而结束在行的开头。因此，除非使用该`markdown_strict`格式，否则以下内容不会在pandoc中产生嵌套的块引用：

```
> This is a block quote.
>> Nested.
```

## 逐字（代码）块

### 缩进的代码块

缩进四个空格（或一个制表符）的文本块被视为逐字记录文本：也就是说，特殊字符不会触发特殊格式，并且保留所有空格和换行符。例如，

```
    if (a > 3) {
      moveShip(5 * gravity, DOWN);
    }
```

最初的缩进（四个空格或一个制表符）不被视为逐字记录的一部分，而是在输出中将其删除。

注意：逐字记录文本中的空白行不必以四个空格开头。

### 围栏代码块

#### 延期： `fenced_code_blocks`

除了标准的缩进代码块之外，pandoc还支持*受防护的*代码块。它们以一行三个或更多波浪号（`~`）开始，并以一行波浪号结束，波浪线的长度必须至少与起始行的长度相同。这些行之间的所有内容均视为代码。无需缩进：

```
~~~~~~~
if (a > 3) {
  moveShip(5 * gravity, DOWN);
}
~~~~~~~
```

与常规代码块一样，带栅栏的代码块必须与周围的文本用空白行隔开。

如果代码本身包含一行波浪号或反引号，则只需在开头和结尾处使用一行较长的波浪号或反引号即可：

```
~~~~~~~~~~~~~~~~
~~~~~~~~~~
code including tildes
~~~~~~~~~~
~~~~~~~~~~~~~~~~
```

#### 延期： `backtick_code_blocks`

与相同`fenced_code_blocks`，但使用反引号（`` ` ``）代替波浪号（`~`）。

#### 延期： `fenced_code_attributes`

（可选）您可以使用以下语法将属性附加到受保护的或反引号代码块：

```
~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

这里`mycode`是一个标识符，`haskell`并且`numberLines`是类，`startFrom`是具有值的属性`100`。某些输出格式可以使用此信息进行语法突出显示。当前，使用此信息的唯一输出格式是HTML，LaTeX，Docx，MS和PowerPoint。如果您的输出格式和语言支持突出显示，则上面的代码块将突出显示，并带有编号的行。（要查看支持哪些语言，请键入`pandoc --list-highlight-languages`。）否则，以上代码块将显示如下：

```
<pre id="mycode" class="haskell numberLines" startFrom="100">
  <code>
  ...
  </code>
</pre>
```

的`numberLines`（或`number-lines`）类将导致代码块的行进行编号，从`1`或的值`startFrom`属性。的`lineAnchors`（或`line-anchors`）类会引起线是在HTML输出可点击的锚。

快捷方式也可以用于指定代码块的语言：

```
```haskell
qsort [] = []
```
```

这等效于：

```
``` {.haskell}
qsort [] = []
```
```

如果`fenced_code_attributes`扩展名被禁用，但是输入包含代码块的类属性，则第一个类属性将作为裸词打印在打开的围栏之后。

为防止所有突出显示，请使用[`--no-highlight`](https://pandoc.org/MANUAL.html#option--no-highlight)标志。要设置突出显示样式，请使用[`--highlight-style`](https://pandoc.org/MANUAL.html#option--highlight-style)。有关突出显示的更多信息，请参见下面的[语法突出显示](https://pandoc.org/MANUAL.html#syntax-highlighting)。

## 线块

#### 延期： `line_blocks`

线块是一系列以竖线（`|`）和空格开头的线。分成几行的内容以及任何前导空格都将保留在输出中；否则，这些行将被格式化为Markdown。这对于经文和地址非常有用：

```
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718
```

如有必要，可以将这些行进行硬包装，但续行必须以空格开头。

```
| The Right Honorable Most Venerable and Righteous Samuel L.
  Constable, Jr.
| 200 Main St.
| Berkeley, CA 94718
```

该语法是从[reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/introduction.html)借用的。

## 清单

### 项目符号清单

项目符号列表是项目符号列表项目的列表。项目符号列表项始于子弹（`*`，`+`，或`-`）。这是一个简单的示例：

```
* one
* two
* three
```

这将产生一个“紧凑”列表。如果您想要一个“松散”列表，其中每个项目都被格式化为一个段落，请在项目之间放置空格：

```
* one

* two

* three
```

子弹不必与左边距齐平；它们可以缩进一个，两个或三个空格。项目符号后必须跟空格。

如果后续行与第一行（在项目符号后）齐平，则列表项看起来最好：

```
* here is my first
  list item.
* and my second.
```

但是Markdown还允许使用“惰性”格式：

```
* here is my first
list item.
* and my second.
```

### 阻止列表项中的内容

列表项可能包含多个段落和其他块级内容。但是，后续段落必须在前面有一个空白行，并缩进以与列表标记之后的第一个非空格内容对齐。

```
  * First paragraph.

    Continued.

  * Second paragraph. With a code block, which must be indented
    eight spaces:

        { code }
```

例外：如果列表标记后接缩进代码块，该代码块必须在列表标记后5个空格处开始，则后续段落必须在列表标记的最后一个字符后两列开始：

```
*     code

  continuation paragraph
```

列表项可能包括其他列表。在这种情况下，前面的空白行是可选的。嵌套列表必须缩进以与包含列表项的列表标记之后的第一个非空格字符对齐。

```
* fruits
  + apples
    - macintosh
    - red delicious
  + pears
  + peaches
* vegetables
  + broccoli
  + chard
```

如上所述，Markdown允许您“懒惰”地编写列表项，而不是缩进连续行。但是，如果列表项中有多个段落或其他块，则每个行的第一行都必须缩进。

```
+ A lazy, lazy, list
item.

+ Another one; this looks
bad but is legal.

    Second paragraph of second
list item.
```

### 有序列表

有序列表的工作方式与项目符号列表相同，只是项目以枚举符而不是项目符号开头。

在标准Markdown中，枚举数是十进制数字，后跟一个句点和一个空格。数字本身被忽略，因此此列表之间没有区别：

```
1.  one
2.  two
3.  three
```

还有这个：

```
5.  one
7.  two
1.  three
```

#### 延期： `fancy_lists`

与标准Markdown不同，pandoc除了阿拉伯数字外，pandoc还允许对有序列表项进行大写和小写字母以及罗马数字标记。列表标记可以括在括号内，或后跟单个右括号或句点。它们必须与后面的文本至少隔开一个空格，并且如果列表标记是带句点的大写字母，则必须至少隔开两个空格。[1个](https://pandoc.org/MANUAL.html#fn1)

该`fancy_lists`扩展名还允许' `#`'代替数字用作有序列表标记：

```
#. one
#. two
```

#### 延期： `startnum`

Pandoc还注意所使用的列表标记的类型和起始编号，并且两者都尽可能以输出格式保存。因此，下面的代码产生一个带有数字的列表，其后跟一个单括号，从9开始，以及一个带有小写罗马数字的子列表：

```
 9)  Ninth
10)  Tenth
11)  Eleventh
       i. subone
      ii. subtwo
     iii. subthree
```

每次使用其他类型的列表标记时，Pandoc都会启动一个新列表。因此，以下将创建三个列表：

```
(2) Two
(5) Three
1.  Four
*   Five
```

如果需要默认列表标记，请使用`#.`：

```
#.  one
#.  two
#.  three
```

#### 延期： `task_lists`

Pandoc使用GitHub-Flavored Markdown的语法支持任务列表。

```
- [ ] an unchecked task list item
- [x] checked item
```

### 定义清单

#### 延期： `definition_lists`

Pandoc使用[PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)的语法和一些扩展来支持定义列表。[2](https://pandoc.org/MANUAL.html#fn2)

```
Term 1

:   Definition 1

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.
```

每个术语必须占一行，可以选择在其后跟随一个空白行，并且必须跟随一个或多个定义。定义以冒号或代字号开头，可以缩进一个或两个空格。

一个术语可以有多个定义，每个定义可以由一个或多个块元素（段落，代码块，列表等）组成，每个元素缩进四个空格或一个制表位。定义的主体（包括第一行，冒号或代字号除外）应缩进四个空格。但是，与其他Markdown列表一样，您可以“懒惰”地省略缩进，除非在段落或其他块元素的开头：

```
Term 1

:   Definition
with lazy continuation.

    Second paragraph of the definition.
```

如果在定义之前保留空格（如上例所示），则定义的文本将被视为段落。在某些输出格式中，这将意味着术语/定义对之间的间距更大。要获得更紧凑的定义列表，请在定义之前省略空格：

```
Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b
```

请注意，定义列表中各项之间必须有空格。（可以通过以下方法激活放宽此要求但不允许“懒惰”硬包装的变体`compact_definition_lists`：请参见下面的[非Pandoc扩展](https://pandoc.org/MANUAL.html#non-pandoc-extensions)。）

### 编号示例列表

#### 延期： `example_lists`

特殊列表标记`@`可用于顺序编号的示例。`@`在整个文档中，第一个带有标记的列表项将标记为“ 1”，下一个为“ 2”，依此类推。编号示例不必出现在单个列表中；每个使用的新列表`@`都会占用最后一个停止的位置。因此，例如：

```
(@)  My first example will be numbered (1).
(@)  My second example will be numbered (2).

Explanation of examples.

(@)  My third example will be numbered (3).
```

编号示例可以在文档中的其他地方标记和引用：

```
(@good)  This is a good example.

As (@good) illustrates, ...
```

标签可以是字母数字字符，下划线或连字符的任何字符串。

注意：示例列表中的延续段落必须始终缩进四个空格，而不管列表标记的长度如何。也就是说，示例列表的行为始终就像`four_space_rule`设置了扩展名一样。这是因为示例标签往往很长，并且在标签之后将内容缩进第一个非空格字符会很尴尬。

### 紧凑和宽松的清单

Pandoc的行为方式与`Markdown.pl`某些涉及列表的“边缘案例” 不同。考虑以下来源：

```
+   First
+   Second:
    -   Fee
    -   Fie
    -   Foe

+   Third
```

Pandoc将其转换为“紧凑列表”（`<p>`在“ First”，“ Second”或“ Third”周围没有标签），而Markdown `<p>`在“ Second”和“ Third”（而非“ First”）周围放置标签“第三”周围的空白。Pandoc遵循一个简单的规则：如果文本后跟空白行，则将其视为段落。由于“第二”后面是列表，而不是空白行，因此不会将其视为段落。列表后跟空白行这一事实是无关紧要的。（注意：即使`markdown_strict`指定了格式，Pandoc仍以这种方式工作。此行为与Markdown官方语法描述一致，即使它与的描述也不同`Markdown.pl`。

### 结束清单

如果要在列表后放置缩进的代码块怎么办？

```
-   item one
-   item two

    { my code block }
```

麻烦！在这里，pandoc（与其他Markdown实现一样）将被`{ my code block }`视为第二项的第二段，而不是代码块。

要“切断”第二项之后的列表，可以插入一些非缩进内容，例如HTML注释，该内容不会以任何格式产生可见的输出：

```
-   item one
-   item two

<!-- end of list -->

    { my code block }
```

如果要两个连续的列表而不是一个大列表，可以使用相同的技巧：

```
1.  one
2.  two
3.  three

<!-- -->

1.  uno
2.  dos
3.  tres
```

## 水平尺

含有三个或更多的行线`*`，`-`或`_`字符（任选由空格分隔）产生水平线：

```
*  *  *  *

---------------
```

## 桌子

可以使用四种表格。前三种预设使用固定宽度的字体，例如Courier。第四类可以与按比例隔开的字体一起使用，因为它不需要对齐列。

#### 延期： `table_captions`

可以为所有4种表格提供标题（如下例所示）。标题是一个以字符串`Table:`（或仅仅是`:`）开头的段落，该段落将被剥离。它可能出现在表格之前或之后。

#### 延期： `simple_tables`

简单表如下所示：

```
  Right     Left     Center     Default
-------     ------ ----------   -------
     12     12        12            12
    123     123       123          123
      1     1          1             1

Table:  Demonstration of simple table syntax.
```

标题行和表格行必须分别适合一行。列的对齐方式取决于标题文本相对于其下方的虚线的位置：[3](https://pandoc.org/MANUAL.html#fn3)

-   如果虚线与标题文本齐平，但在左侧超出标题文本，则该列为右对齐。
-   如果虚线与标题文本齐平，但在右侧超出标题文本，则该列将向左对齐。
-   如果虚线超出两侧的标题文本，则该列居中。
-   如果虚线在两边都与标题文本齐平，则使用默认对齐方式（在大多数情况下，将保留该对齐方式）。

该表必须以空白行或虚线后接空白行的结尾。

如果使用虚线结束表格，则可以省略列标题行。例如：

```
-------     ------ ----------   -------
     12     12        12             12
    123     123       123           123
      1     1          1              1
-------     ------ ----------   -------
```

如果省略标题行，则根据表格主体的第一行确定列对齐方式。因此，在上表中，这些列分别是右对齐，左对齐，居中对齐和右对齐。

#### 延期： `multiline_tables`

多行表允许标题行和表行跨越多行文本（但不支持跨表多列或多行的单元格）。这是一个例子：

```
-------------------------------------------------------------
 Centered   Default           Right Left
  Header    Aligned         Aligned Aligned
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
-------------------------------------------------------------

Table: Here's the caption. It, too, may span
multiple lines.
```

它们的工作方式类似于简单表，但有以下区别：

-   它们必须在标题文本之前以破折号开头（除非省略了标题行）。
-   它们必须以破折号结尾，然后是空白行。
-   行必须用空白行分隔。

在多行表中，表解析器注意列的宽度，并且编写者尝试在输出中重现这些相对宽度。因此，如果发现输出中的一列太窄，请尝试在Markdown源中将其加宽。

在多行表和简单表中，标题都可以省略：

```
----------- ------- --------------- -------------------------
   First    row                12.0 Example of a row that
                                    spans multiple lines.

  Second    row                 5.0 Here's another one. Note
                                    the blank line between
                                    rows.
----------- ------- --------------- -------------------------

: Here's a multiline table without a header.
```

多行表可能只有一行，但是该行后应该有一个空行（然后是该表末尾的破折号行），否则该表可以解释为简单表。

#### 延期： `grid_tables`

网格表如下所示：

```
: Sample grid table.

+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+
```

`=`s 行将标题与表主体分隔开，对于无标题表可以省略。网格表的单元格可以包含任意块元素（多个段落，代码块，列表等）。不支持跨多个列或行的单元格。使用Emacs的表格模式（`M-x table-insert`）可以轻松创建表格。

可以像在管道表中一样指定对齐方式，方法是在标头后面的分隔线边界处放置冒号：

```
+---------------+---------------+--------------------+
| Right         | Left          | Centered           |
+==============:+:==============+:==================:+
| Bananas       | $1.34         | built-in wrapper   |
+---------------+---------------+--------------------+
```

对于无标题表，冒号放在第一行：

```
+--------------:+:--------------+:------------------:+
| Right         | Left          | Centered           |
+---------------+---------------+--------------------+
```

##### 表格限制

Pandoc不支持具有行跨度或列跨度的网格表。这意味着Pandoc不支持可变行数的列或可变行数的列。所有网格表的每一行必须具有相同数量的列，并且每一列必须具有相同数量的行。例如，Docutils [示例网格表](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables)将无法使用Pandoc呈现预期的效果。

#### 延期： `pipe_tables`

管道表如下所示：

```
| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|   12  |  12  |    12   |    12  |
|  123  |  123 |   123   |   123  |
|    1  |    1 |     1   |     1  |

  : Demonstration of pipe table syntax.
```

语法与[PHP Markdown Extra表](https://michelf.ca/projects/php-markdown/extra/#table)相同。起始和结束管道字符是可选的，但所有列之间都必须有管道。冒号表示列对齐，如图所示。标头不能省略。要模拟无标题表，请包含带有空白单元格的标题。

由于管道指示列边界，因此不必像上面的示例一样垂直对齐列。因此，这是一个非常合法（尽管很丑）的管道表：

```
fruit| price
-----|-----:
apple|2.05
pear|1.37
orange|3.09
```

管道表的单元格不能包含段落和列表之类的块元素，并且不能跨越多行。如果管道表包含行，其Markdown内容的宽度大于列宽度（请参阅参考资料[`--columns`](https://pandoc.org/MANUAL.html#option--columns)），则该表将占据全文宽度，单元格内容将换行，而相对单元格的宽度则由虚线中的破折号确定。将表格标题与表格主体分隔开的行。（例如，`---|-`将第一列的3/4作为全文宽度的第二行。）另一方面，如果没有任何行比列的宽度宽，则将不包装单元格内容，并且单元格将根据其内容调整大小。

注意：pandoc也可以识别以下形式的管道表，如Emacs的orgtbl-mode可以生成的那样：

```
| One | Two   |
|-----+-------|
| my  | table |
| is  | nice  |
```

区别在于，`+`使用而不是`|`。不支持其他orgtbl功能。特别是，要获得非默认的列对齐方式，您需要如上所述添加冒号。

## 元数据块

#### 延期： `pandoc_title_block`

如果文件以标题栏开头

```
% title
% author(s) (separated by semicolons)
% date
```

它将被解析为书目信息，而不是常规文本。（例如，将在独立的LaTeX或HTML输出的标题中使用它。）该块可能仅包含标题，标题和作者，或全部三个元素。如果要包括作者但不包含标题，或者标题和日期不包含作者，则需要空行：

```
%
% Author
```

```
% My title
%
% June 15, 2006
```

标题可能占据多行，但续行必须以前导空格开头，因此：

```
% My title
  on multiple lines
```

如果文档中有多位作者，则作者可以放在前导空格的单独行中，或以分号分隔，或两者兼而有之。因此，以下所有均等价：

```
% Author One
  Author Two
```

```
% Author One; Author Two
```

```
% Author One;
  Author Two
```

日期必须在一行中。

所有三个元数据字段都可以包含标准的内联格式（斜体，链接，脚注等）。

标题栏将始终被解析，但是只有选择[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)（[`-s`](https://pandoc.org/MANUAL.html#option--standalone)）选项时，标题栏才会影响输出。在HTML输出中，标题将出现两次：一次出现在文档标题中（这是将显示在浏览器窗口顶部的标题），一次出现在文档正文的开头。文档头中的标题可以附加一个可选的前缀（[`--title-prefix`](https://pandoc.org/MANUAL.html#option--title-prefix)或[`-T`](https://pandoc.org/MANUAL.html#option--title-prefix)选项）。正文中的标题显示为带有“ title”类的H1元素，因此可以使用CSS对其进行隐藏或重新格式化。如果指定了标题前缀，[`-T`](https://pandoc.org/MANUAL.html#option--title-prefix)并且在文档中没有标题栏，则标题前缀将自己用作HTML标题。

手册页编写器从标题行提取标题，手册页节号以及其他页眉和页脚信息。假定标题是标题行上的第一个单词，可以选择在括号中以（单个数字）段号结尾。（标题和括号之间不应有空格。）此后的所有内容均视为附加的页脚和标题文本。`|`应该使用单个竖线字符（）将页脚文本与页眉文本分开。从而，

```
% PANDOC(1)
```

将产生一个带有标题`PANDOC`和第1节的手册页。

```
% PANDOC(1) Pandoc User Manuals
```

页脚中还将有“ Pandoc用户手册”。

```
% PANDOC(1) Pandoc User Manuals | Version 4.0
```

标头中还将包含“ Version 4.0”。

#### 延期： `yaml_metadata_block`

甲[YAML](https://yaml.org/spec/1.2/spec.html "YAML v1.2规范")元数据块是有效的YAML对象，由线三个连字符（分隔`---`）在顶部和三个连字符（行`---`）或三个点（`...`）在底部。YAML元数据块可能会出现在文档中的任何位置，但是，如果不是在开始位置，则必须在其前面加一个空行。（请注意，由于在提供多个文件时pandoc会串联输入文件的方式，因此您也可以将元数据保存在单独的YAML文件中，并将其与Markdown文件一起作为参数传递给pandoc：

```
pandoc chap1.md chap2.md chap3.md metadata.yaml -s -o book.html
```

只是要确保YAML文件开始`---`和结束与`---`或`...`）。此外，你可以使用[`--metadata-file`](https://pandoc.org/MANUAL.html#option--metadata-file)选项。但是，使用这种方法时，您不能引用Markdown主输入文档中的内容（如脚注）。

元数据将从YAML对象的字段中获取，并添加到任何现有文档元数据中。元数据可以包含列表和对象（任意嵌套），但是所有字符串标量都将解释为Markdown。名称以下划线结尾的字段将被pandoc忽略。（它们可以被给予由外部处理器的作用。）字段名必须不能解释成YAML数字或布尔值（因此，例如，`yes`，`True`，和`15`不能被用作字段名称）。

一个文档可能包含多个元数据块。如果两个元数据块尝试设置相同的字段，则将采用第二个块的值。

当pandoc与[`-t markdown`](https://pandoc.org/MANUAL.html#option--to)创建Markdown文档一起使用时，仅当使用该[`-s/--standalone`](https://pandoc.org/MANUAL.html#option--standalone)选项时，才会生成YAML元数据块。所有元数据将出现在文档开头的单个块中。

请注意，必须遵循[YAML](https://yaml.org/spec/1.2/spec.html "YAML v1.2规范")转义规则。因此，例如，如果标题包含冒号，则必须用引号引起来。竖线字符（`|`）可用于开始缩进的块，该块将按字面意义进行解释，而无需转义。当字段包含空行或块级格式时，此表格是必需的：

```
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.

  It consists of two paragraphs.
...
```

模板变量将从元数据中自动设置。因此，例如，在编写HTML时，该变量`abstract`将被设置为与该`abstract`字段中的Markdown等效的HTML ：

```
<p>This is the abstract.</p>
<p>It consists of two paragraphs.</p>
```

变量可以包含任意的YAML结构，但是模板必须与此结构匹配。`author`默认模板中的变量需要一个简单的列表或字符串，但是可以更改以支持更复杂的结构。例如，以下组合将给作者增加一个从属关系：

```
---
title: The document title
author:
- name: Author One
  affiliation: University of Somewhere
- name: Author Two
  affiliation: University of Nowhere
...
```

要在上面的示例中使用结构化作者，您将需要一个自定义模板：

```
$for(author)$
$if(author.name)$
$author.name$$if(author.affiliation)$ ($author.affiliation$)$endif$
$else$
$author$
$endif$
$endfor$
```

可以使用`header-includes`；来指定要包含在文档标题中的原始内容。但是，使用[`raw_attribute`扩展名](https://pandoc.org/MANUAL.html#extension-raw_attribute)）将此内容标记为特定输出格式的原始代码很重要，否则它将被解释为markdown。例如：

```
header-includes:
- |
  ```{=latex}
  \let\oldsection\section
  \renewcommand{\section}[1]{\clearpage\oldsection{#1}}
  ```
```

## 反斜杠转义符

#### 延期： `all_symbols_escapable`

除了在代码块或内联代码内部，任何标点符号或空格字符后加反斜杠都将按字面进行处理，即使它通常会指示格式。因此，例如，如果一个人写

```
*\*hello\**
```

一个会得到

```
<em>*hello*</em>
```

代替

```
<strong>hello</strong>
```

该规则比标准Markdown规则更容易记住，后者仅允许以下字符使用反斜杠转义：

```
\`*_{}[]()>#+-.!
```

（但是，如果使用`markdown_strict`格式，将使用标准的Markdown规则。）

反斜杠转义的空间被解析为不间断空间。在TeX输出中，它将显示为`~`。在HTML和XML输出中，它将显示为文字Unicode不间断空格字符（请注意，因此它实际上在生成的HTML源代码中看起来是“不可见的”；您仍然可以使用[`--ascii`](https://pandoc.org/MANUAL.html#option--ascii)命令行选项使它显示为显式实体）。

反斜杠转义的换行符（即，在行尾出现的反斜杠）被解析为硬换行符。它将在TeX输出中显示为`\\`，在HTML中显示为`<br />`。这是Markdown使用行上的两个尾随空格来指示硬断行的“不可见”方式的不错替代。

反斜杠转义在逐字环境中不起作用。

## 内联格式

### 重点

要*强调*一些文本，请用`*`或括起来`_`，如下所示：

```
This text is _emphasized with underscores_, and this
is *emphasized with asterisks*.
```

双人`*`或`_`产生**强烈的重点**：

```
This is **strong emphasis** and __with underscores__.
```

一个`*`或`_`字符包围的空间，或反斜杠转义，将不会触发强调：

```
This is * not emphasized *, and \*neither is this\*.
```

#### 延期： `intraword_underscores`

由于`_`有时在单词和标识符内部使用，因此pandoc不会将`_`字母数字字符包围的内容解释为重点标记。如果您只想强调单词的一部分，请使用`*`：

```
feas*ible*, not feas*able*.
```

### 淘汰赛

#### 延期： `strikeout`

要用水平线删除一段文本，请以开头和结尾`~~`。因此，例如

```
This ~~is deleted text.~~
```

### 上标和下标

#### 扩展名：`superscript`，`subscript`

上标可以用`^`字符将上标文本括起来；下标可以通过用`~`字符包围下标文本来编写。因此，例如

```
H~2~O is a liquid.  2^10^ is 1024.
```

文本之间`^...^`或之间`~...~`不能包含空格或换行符。如果上标或下标文本包含空格，则这些空格必须使用反斜杠进行转义。（这是为了防止通过正常使用`~`和`^`以及与脚注的不良交互来意外地进行上标和下标。）因此，如果要在下标中使用字母P与“猫”，请使用`P~a\ cat~`，而不要使用`P~a cat~`。

### 逐字

要使一小段文字保持原状，请将其放在反引号内：

```
What is the difference between `>>=` and `>>`?
```

如果逐字记录文本包含反引号，请使用双反引号：

```
Here is a literal backtick `` ` ``.
```

（在开始反引号之后和在结束反引号之前的空间将被忽略。）

一般规则是，逐字跨度以一串连续的反引号（可选地后跟一个空格）开始，以一串相同数量的反引号（可选地后跟一个空格）结束。

请注意，反斜杠转义符（和其他Markdown构造）在逐字上下文中不起作用：

```
This is a backslash followed by an asterisk: `\*`.
```

#### 延期： `inline_code_attributes`

可以将属性附加到逐字记录文本，就像[受防护的代码块一样](https://pandoc.org/MANUAL.html#fenced-code-blocks)：

```
`<$>`{.haskell}
```

### 小帽子

要写小写字母，请使用以下`smallcaps`类：

```
[Small caps]{.smallcaps}
```

或者，不带`bracketed_spans`扩展名：

```
<span class="smallcaps">Small caps</span>
```

为了与其他Markdown版本兼容，还支持CSS：

```
<span style="font-variant:small-caps;">Small caps</span>
```

这将支持所有支持小写字母的输出格式。

## 数学

#### 延期： `tex_math_dollars`

两个`$`字符之间的任何字符都将被视为TeX数学。开头`$`必须在其右边立即有一个非空格字符，而结尾`$`必须在其左侧必须有一个非空格字符，并且不得紧跟一个数字。因此，`$20,000 and $30,000`不会解析为数学。如果由于某种原因您需要将文本括在文字中`$`字符中，请使用反斜杠其转义，并且它们不会被视为数学定界符。

对于显示数学，请使用`$$`定界符。（在这种情况下，分隔符可以通过空格与公式分隔。）

TeX数学将以所有输出格式打印。呈现方式取决于输出格式：

胶乳

它会逐字出现，并用`\(...\)`（对于内联数学）或`\[...\]`（对于显示数学）括起来。

Markdown，Emacs Org模式，ConTeXt，ZimWiki

它会逐字出现，并用`$...$`（对于内联数学）或`$$...$$`（对于显示数学）括起来。

XWiki

它会被逐字包围`{{formula}}..{{/formula}}`。

reStructuredText

将使用[解释后的文本角色`:math:`](https://docutils.sourceforge.io/docs/ref/rst/roles.html#math)来呈现它。

AsciiDoc

对于AsciiDoc输出格式（[`-t asciidoc`](https://pandoc.org/MANUAL.html#option--to)），它会被逐字显示为`latexmath:[$...$]`（对于内联数学）或`[latexmath]++++\[...\]+++`（对于显示数学）。对于AsciiDoctor输出格式（[`-t asciidoctor`](https://pandoc.org/MANUAL.html#option--to)），省略LaTex分隔符（`$..$`和`\[..\]`）。

Texinfo

它将在`@math`命令中呈现。

罗夫人，吉拉标记

它将不加逐字呈现`$`。

MediaWiki，DokuWiki

它将在`<math>`标签内呈现。

纺织品

它将在`<span class="math">`标签内呈现。

RTF，OpenDocument

如果可能，将使用Unicode字符对其进行渲染，否则将逐字显示。

ODT

如果可能，将使用MathML进行渲染。

DocBook

如果使用了该[`--mathml`](https://pandoc.org/MANUAL.html#option--mathml)标志，则将使用`inlineequation`or `informalequation`标记中的MathML呈现该标志。否则，将尽可能使用Unicode字符来呈现它。

Docx

它将使用OMML数学标记来呈现。

小说书2

如果使用该[`--webtex`](https://pandoc.org/MANUAL.html#option--webtex)选项，则使用CodeCogs或其他兼容的Web服务将公式呈现为图像，然后将其下载并嵌入到电子书中。否则，它们将逐字显示。

HTML，Slidy，DZSlides，S5，EPUB

用HTML呈现数学的方式将取决于所选的命令行选项。因此，请参见上面的[HTML中的数学渲染](https://pandoc.org/MANUAL.html#math-rendering-in-html)。

## 原始HTML

#### 延期： `raw_html`

降价让您插入原始的HTML（或DocBook的）在文档的任何地方（除了逐字环境中，在那里`<`，`>`和`&`按字面解释）。（从技术上讲，这不是扩展，因为标准的Markdown允许它，但已将其扩展为可以根据需要禁用的扩展。）

原始HTML将以HTML，S5，Slidy，Slideous，DZSlides，EPUB，Markdown，CommonMark，Emacs Org模式和Textile输出不变地传递，并以其他格式隐藏。

有关在Markdown文档中包括原始HTML的更明确的方法，请参阅[`raw_attribute`扩展名](https://pandoc.org/MANUAL.html#extension-raw_attribute)。

在CommonMark格式中，如果`raw_html`启用，则上标，下标，删除线和小写字母将以HTML表示。否则，将使用纯文本后备。请注意，即使`raw_html`禁用表，如果表不能使用管道语法，它们也将使用HTML语法呈现。

#### 延期： `markdown_in_html_blocks`

标准Markdown允许您包括HTML“块”：平衡标记之间的HTML块，这些标记与周围的文本用空白行隔开，并在左边界处开始和结束。在这些块中，所有内容都解释为HTML，而不是Markdown。因此（例如），`*`并不表示强调。

`markdown_strict`使用该格式时，Pandoc的行为方式是这样；但默认情况下，pandoc会将HTML块标签之间的内容解释为Markdown。因此，例如pandoc会变成

```
<table>
<tr>
<td>*one*</td>
<td>[a link](https://google.com)</td>
</tr>
</table>
```

进入

```
<table>
<tr>
<td><em>one</em></td>
<td><a href="https://google.com">a link</a></td>
</tr>
</table>
```

而`Markdown.pl`将其保持原样。

此规则有一个例外：`<script>`和`<style>`标记之间的文本不解释为Markdown。

与标准Markdown的区别应该使Markdown与HTML块元素的混合更加容易。例如，一个人可以用`<div>`标记将Markdown文本块包围起来，而不会阻止其解释为Markdown。

#### 延期： `native_divs`

将本地pandoc `Div`块用于`<div>`标记内的内容。在大多数情况下，它应该提供与相同的输出`markdown_in_html_blocks`，但是可以更轻松地编写pandoc过滤器来操作块组。

#### 延期： `native_spans`

将本地pandoc `Span`块用于`<span>`标记内的内容。在大多数情况下，它应该提供与相同的输出`raw_html`，但是可以更轻松地编写pandoc过滤器来处理内联组。

#### 延期： `raw_tex`

除了原始HTML外，pandoc还允许将原始LaTeX，TeX和ConTeXt包含在文档中。内联TeX命令将保留并保持不变地传递给LaTeX和ConTeXt编写器。因此，例如，您可以使用LaTeX包含BibTeX引文：

```
This result was proved in \cite{jones.1967}.
```

请注意，在LaTeX环境中，例如

```
\begin{tabular}{|l|l|}\hline
Age & Frequency \\ \hline
18--25  & 15 \\
26--35  & 33 \\
36--45  & 22 \\ \hline
\end{tabular}
```

begin和end标签之间的内容将被解释为原始LaTeX，而不是Markdown。

有关在Markdown文档中包括原始TeX的更明确，更灵活的方法，请参阅[`raw_attribute`扩展](https://pandoc.org/MANUAL.html#extension-raw_attribute)。

内联LaTeX在Markdown，LaTeX，Emacs Org模式和ConTeXt以外的输出格式中被忽略。

### 通用原始属性

#### 延期： `raw_attribute`

具有特殊属性的内联跨度和受防护的代码块将被解析为具有指定格式的原始内容。例如，下面的代码生成一个原始的roff `ms`块：

```
```{=ms}
.MYMACRO
blah blah
```
```

并且以下代码会生成原始的`html`内联元素：

```
This is `<a>html</a>`{=html}
```

这对于将原始xml插入`docx`文档（例如分页符）很有用：

```
```{=openxml}
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
```
```

格式名称应与目标格式名称相匹配（[`-t/--to`](https://pandoc.org/MANUAL.html#option--to)有关列表，请参见上方的，或使用`pandoc --list-output-formats`）。使用`openxml`的`docx`输出，`opendocument`用于`odt`输出，`html5`用于`epub3`输出，`html4`用于`epub2`输出，并且`latex`，`beamer`，`ms`，或`html5`用于`pdf`输出（取决于您使用什么[`--pdf-engine`](https://pandoc.org/MANUAL.html#option--pdf-engine)）。

该扩展的前提是启用了相关类型的内联代码或受防护的代码块。因此，例如，`backtick_code_blocks`必须启用将原始属性与反引号代码块一起使用。

raw属性不能与常规属性组合。

## LaTeX宏

#### 延期： `latex_macros`

启用此扩展名后，pandoc将解析LaTeX宏定义，并将结果宏应用于所有LaTeX数学和原始LaTeX。因此，例如，以下内容将适用于所有输出格式，而不仅仅是LaTeX：

```
\newcommand{\tuple}[1]{\langle #1 \rangle}

$\tuple{a, b, c}$
```

请注意，如果LaTeX宏出现在标有[`raw_attribute`扩展名](https://pandoc.org/MANUAL.html#extension-raw_attribute)的原始跨度或块内，则将不会应用它们。

当`latex_macros`被禁用时，生胶乳和数学不会有应用宏。当您定位LaTeX或PDF时，这通常是一种更好的方法。

如果`latex_macros`未启用，则LaTeX中的宏定义将作为原始LaTeX传递。`raw_tex`不管是否`latex_macros`启用，都会通过Markdown源（或其他允许的格式）中的宏定义进行传递。

## 链接

Markdown允许以多种方式指定链接。

### 自动链接

如果将URL或电子邮件地址括在尖括号中，它将成为链接：

```
<https://google.com>
<sam@green.eggs.ham>
```

### 内联链接

内联链接由方括号中的链接文本和括号中的URL组成。（可选的是，URL后面可以带有链接标题，并用引号引起来。）

```
This is an [inline link](/url), and here's [one with
a title](https://fsf.org "click here for a good time!").
```

带括号的部分和带括号的部分之间不能有空格。链接文本可以包含格式（例如强调），但标题不能。

内联链接中的电子邮件地址不会自动检测到，因此必须以开头`mailto`：

```
[Write me!](mailto:sam@green.eggs.ham)
```

### 参考链接

一个*明确的*参照链接有两个部分，链路本身和连杆的定义，其可（之前或链路之后）在文件中的其他地方发生。

链接由方括号中的链接文本和方括号中的标签组成。（除非`spaced_reference_links`启用了扩展名，否则两者之间不能有空格。）链接定义由带括号的标签，后跟冒号，空格，URL和可选的（在空格之后）引号引起的链接标题组成。或括号中。标签不得被解析为引用（假设`citations`已启用扩展名）：引用优先于链接标签。

这里有些例子：

```
[my label 1]: /foo/bar.html  "My title, optional"
[my label 2]: /foo
[my label 3]: https://fsf.org (The free software foundation)
[my label 4]: /bar#special  'A title in single quotes'
```

该URL可以选择用尖括号括起来：

```
[my label 5]: <http://foo.bar.baz>
```

标题可能在下一行：

```
[my label 3]: https://fsf.org
  "The free software foundation"
```

请注意，链接标签不区分大小写。因此，这将起作用：

```
Here is [my link][FOO]

[Foo]: /bar/baz
```

在*隐式*参考链接中，第二对括号为空：

```
See [my website][].

[my website]: http://foo.bar.baz
```

注意：在`Markdown.pl`Markdown和大多数其他实现中，引用链接定义不能出现在嵌套结构（例如列表项或块引号）中。Pandoc解除了这种看似随意的限制。因此，尽管在大多数其他实现中并非如此，但在pandoc中以下内容仍然可以：

```
> My block [quote].
>
> [quote]: /foo
```

#### 延期： `shortcut_reference_links`

在*快捷方式*参考链接中，可以完全省略第二对括号：

```
See [my website].

[my website]: http://foo.bar.baz
```

### 内部连结

要链接到同一文档的另一部分，请使用自动生成的标识符（请参阅[标题标识符](https://pandoc.org/MANUAL.html#heading-identifiers)）。例如：

```
See the [Introduction](#introduction).
```

要么

```
See the [Introduction].

[Introduction]: #introduction
```

HTML格式（包括HTML幻灯片和EPUB），LaTeX和ConTeXt当前支持内部链接。

## 图片

紧随其后的链接`!`将被视为图像。链接文本将用作图像的替代文本：

```
![la lune](lalune.jpg "Voyage to the moon")

![movie reel]

[movie reel]: movie.gif
```

#### 延期： `implicit_figures`

本身在段落中出现的带有非空alt文本的图像将被渲染为带有标题的图形。图片的替代文字将用作标题。

```
![This is the caption](/url/of/image.png)
```

呈现方式取决于输出格式。某些输出格式（例如RTF）尚不支持数字。在这些格式下，您将只获得段落本身的图像，没有标题。

如果只需要常规的嵌入式图像，请确保它不是该段落中唯一的内容。一种方法是在图像后插入一个不间断的空格：

```
![This image won't be a figure](/url/of/image.png)\
```

请注意，在reveal.js幻灯片显示中，具有`stretch`类的段落本身的图像将填充屏幕，而标题和图形标签将被省略。

#### 延期： `link_attributes`

可以在链接和图像上设置属性：

```
An inline ![image](foo.jpg){#id .class width=30 height=20px}
and a reference ![image][ref] with attributes.

[ref]: foo.jpg "optional title" {#id .class key=val key2="val 2"}
```

（这个语法兼容[PHP降价外](https://michelf.ca/projects/php-markdown/extra/)，只有当`#id`和`.class`使用。）

对于HTML和EPUB，除`width`和`height`（但包括`srcset`和`sizes`）之外的所有已知HTML5属性均按原样传递。未知属性作为自定义属性传递，带有`data-`前缀。其他作者忽略其输出格式未特别支持的属性。

图像上的`width`和`height`属性会得到特殊处理。当不使用单位使用时，假定单位为像素。然而，任何下列单元标识符，可以使用：`px`，`cm`，`mm`，`in`，`inch`和`%`。数字和单位之间不得有任何空格。例如：

```
![](file.jpg){ width=50% }
```

-   尺寸可以转换为与输出格式兼容的形式（例如，将HTML转换为LaTeX时，以像素为单位的尺寸将转换为英寸）。像素和物理测量之间的转换受该[`--dpi`](https://pandoc.org/MANUAL.html#option--dpi)选项的影响（默认情况下，假设图像分辨率为96 dpi，除非图像本身包含dpi信息）。
-   该`%`单元通常相对于一些可用空间。例如，上面的示例将呈现为以下内容。
    -   HTML： `<img href="file.jpg" style="width: 50%;" />`
    -   LaTeX ：（`\includegraphics[width=0.5\textwidth,height=\textheight]{file.jpg}`如果您使用的是自定义模板，则需要`graphicx`按照默认模板进行配置。）
    -   内容： `\externalfigure[file.jpg][width=0.5\textwidth]`
-   某些输出格式具有类（[ConTeXt](https://wiki.contextgarden.net/Using_Graphics#Multiple_Image_Settings)）或唯一标识符（LaTeX `\caption`）或两者（HTML）的概念。
-   如果未指定`width`或`height`属性，则后备方法是查看图像分辨率和图像文件中嵌入的dpi元数据。

## 股利和跨度

使用`native_divs`和`native_spans`扩展名（请参见[上文](https://pandoc.org/MANUAL.html#extension-native_divs)），HTML语法可以用作markdown的一部分，以在pandoc AST中创建本机`Div`和`Span`元素（与原始HTML相对）。但是，还有更好的语法可用：

#### 延期： `fenced_divs`

允许对本机`Div`块使用特殊的受防护语法。Div的围栏至少包含三个连续的冒号以及一些属性。可选地，属性后面可以是另一串连续的冒号。属性语法与受保护的代码块中的语法完全相同（请参阅[扩展：）`fenced_code_attributes`](https://pandoc.org/MANUAL.html#extension-fenced_code_attributes)。与带防护的代码块一样，可以使用大括号中的属性或单个不带括号的单词，将其视为类名。Div以另一行结尾，该行包含至少三个连续冒号的字符串。带围栏的Div应与前面和后面的块之间用空行分隔。

例：

```
::::: {#special .sidebar}
Here is a paragraph.

And another.
:::::
```

有栅栏的div可以嵌套。区分开放栅栏的原因在于它们*必须*具有以下属性：

```
::: Warning ::::::
This is a warning.

::: Danger
This is a warning within a warning.
:::
::::::::::::::::::
```

没有属性的栅栏总是封闭栅栏。与带有围栏的代码块不同，封闭围栏中的冒号数量不必与开放围栏中的冒号数量匹配。但是，使用不同长度的围栏将嵌套的div与它们的父母区分开来对视觉清晰度很有帮助。

#### 延期： `bracketed_spans`

用括号括起来的一系列内联序列（如果用来开始链接），`Span`如果紧接其后是属性，则将被视为具有属性的：

```
[This is *some text*]{.class key="val"}
```

## 脚注

#### 延期： `footnotes`

Pandoc的Markdown使用以下语法允许添加脚注：

```
Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.

        { some.code }

    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.

This paragraph won't be part of the note, because it
isn't indented.
```

脚注引用中的标识符不得包含空格，制表符或换行符。这些标识符仅用于将脚注参考与注释本身相关联；在输出中，脚注将按顺序编号。

脚注本身不必放在文档末尾。它们可能出现在除其他块元素（列表，块引号，表等）内部之外的任何位置。每个脚注应与周围的内容（包括其他脚注）用空白行分隔。

#### 延期： `inline_notes`

还可以使用行内脚注（尽管与常规注解不同，它们不能包含多个段落）。语法如下：

```
Here is an inline note.^[Inlines notes are easier to write, since
you don't have to pick an identifier and move down to type the
note.]
```

内联和常规脚注可以自由混合。

## 引文

#### 延期： `citations`

使用外部过滤器，`pandoc-citeproc`pandoc可以自动生成多种样式的引文和参考书目。基本用法是

```
pandoc --filter pandoc-citeproc myinput.txt
```

为了使用此功能，您将需要使用`bibliography`YAML元数据部分中的元数据字段或[`--bibliography`](https://pandoc.org/MANUAL.html#option--bibliography)命令行参数来指定书目文件。如果要使用多个书目文件，则可以提供多个[`--bibliography`](https://pandoc.org/MANUAL.html#option--bibliography)参数或将`bibliography`元数据字段设置为YAML数组。参考书目可以采用以下任何一种格式：

| 格式 | 文件扩展名 |
| --- | --- |
| BibLaTeX | 。围兜 |
| BibTeX | .bibtex |
| 科帕克 | .copac |
| CSL JSON | .json |
| CSL YAML | .yaml |
| 尾注 | .enl |
| EndNote XML | .xml |
| ISI | .wos |
| MEDLINE | .medline |
| 模式 | .mods |
| RIS | .ris |

请注意，该文件`.bib`可同时用于BibTeX和BibLaTeX文件。用于`.bibtex`强制BibTeX。

请注意，`pandoc-citeproc --bib2json`并且`pandoc-citeproc --bib2yaml`可以从任何受支持的格式生成`.json`和`.yaml`文件。

现场标记：在BibTeX和BibLaTeX数据库中，pandoc-citeproc解析LaTeX标记的子集；在CSL YAML数据库中，pandoc Markdown；在CSL JSON数据库中，[类似HTML的标记](https://docs.citationstyles.org/en/1.0/release-notes.html#rich-text-markup-within-fields)：

`<i>...</i>`

斜体字

`<b>...</b>`

胆大

`<span style="font-variant:small-caps;">...</span>` 要么 `<sc>...</sc>`

小首都

`<sub>...</sub>`

下标

`<sup>...</sup>`

上标

`<span class="nocase">...</span>`

防止短语被大写为标题

`pandoc-citeproc -j`并`-y`尽可能地相互转换CSL JSON和CSL YAML格式。

作为使用[`--bibliography`](https://pandoc.org/MANUAL.html#option--bibliography)或YAML元数据字段指定书目文件的替代方法`bibliography`，您可以将引文数据直接包含`references`在文档的YAML元数据字段中。该字段应包含YAML编码的引用数组，例如：

```
---
references:
- type: article-journal
  id: WatsonCrick1953
  author:
  - family: Watson
    given: J. D.
  - family: Crick
    given: F. H. C.
  issued:
    date-parts:
    - - 1953
      - 4
      - 25
  title: 'Molecular structure of nucleic acids: a structure for deoxyribose
    nucleic acid'
  title-short: Molecular structure of nucleic acids
  container-title: Nature
  volume: 171
  issue: 4356
  page: 737-738
  DOI: 10.1038/171737a0
  URL: https://www.nature.com/articles/171737a0
  language: en-GB
...
```

（`pandoc-citeproc --bib2yaml`可以从书目文件中以支持的格式之一生成这些内容。）

可以使用[Zotero样式存储库中](https://www.zotero.org/styles)列出的[Citation Style Language](https://citationstyles.org/)支持的任何样式来格式化引文和参考。这些文件是使用选项或元数据字段指定的。默认情况下，将使用“ [芝加哥样式手册”](https://chicagomanualofstyle.org/)作者日期格式。CSL项目提供有关[查找和编辑样式的](https://citationstyles.org/authors/)更多信息。[](https://www.zotero.org/styles)[`--csl`](https://pandoc.org/MANUAL.html#option--csl)`csl``pandoc-citeproc`[](https://chicagomanualofstyle.org/)[](https://citationstyles.org/authors/)

要使引用超链接到相应的书目条目，请添加`link-citations: true`到YAML元数据。

引文放在方括号内，并用分号分隔。每个引用都必须具有一个键，该键由“ @” +数据库中的引用标识符组成，并且可以选择具有前缀，定位符和后缀。引用密钥必须以字母，数字或开头，`_`并且可以包含字母数字`_`，和内部标点符号（`:.#$%&-+?<>~/`）。这里有些例子：

```
Blah blah [see @doe99, pp. 33-35; also @smith04, chap. 1].

Blah blah [@doe99, pp. 33-35, 38-39 and *passim*].

Blah blah [@smith04; @doe99].
```

`pandoc-citeproc`在[CSL语言环境文件中](https://github.com/citation-style-language/locales)检测定位词。缩写形式或非缩写形式都可以接受。在`en-US`区域设置，定位符项可以被写入任一单数或复数形式，如`book`，`bk.`/ `bks.`; `chapter`，`chap.`/ `chaps.`; `column`，`col.`/ `cols.`; `figure`，`fig.`/ `figs.`; `folio`，`fol.`/ `fols.`; `number`，`no.`/ `nos.`; `line`，`l.`/ `ll.`; `note`，`n.`/ `nn.`; `opus`，`op.`/ `opp.`; `page`，`p.`/ `pp.`; `paragraph`，`para.`/ `paras.`; `part`，`pt.`/ `pts.`; `section`，`sec.`/ `secs.`; `sub verbo`，`s.v.`/ `s.vv.`;`verse`，`v.`/ `vv.`; `volume`，`vol.`/ `vols.`; `¶`/ `¶¶`; `§`/ `§§`。如果未使用定位词，则假定为“页面”。

`pandoc-citeproc`将使用启发式方法将定位器与后缀区分开。在复杂的情况下，可以将定位符括在花括号中（`pandoc-citeproc`仅使用0.15和更高版本）：

```
[@smith{ii, A, D-Z}, with a suffix]
[@smith, {pp. iv, vi-xi, (xv)-(xvii)} with suffix here]
```

`-`之前的减号（）`@`将禁止在引用中提及作者。当文本中已经提到作者时，这可能会很有用：

```
Smith says blah [-@smith04].
```

您还可以编写文本引用，如下所示：

```
@smith04 says blah.

@smith04 [p. 33] says blah.
```

如果样式要求引用的作品列表，则将其放置在id为的div中`refs`（如果存在）：

```
::: {#refs}
:::
```

否则，它将被放置在文档的末尾。通过`suppress-bibliography: true`在YAML元数据中进行设置，可以抑制书目的生成。

如果希望书目具有节标题，则可以`reference-section-title`在元数据中进行设置，也可以将标题放在带有id `refs`（如果正在使用）的div的开头或文档的末尾：

```
last paragraph...

# References
```

在此标题之后将插入参考书目。请注意，`unnumbered`该类将添加到此标题，因此该部分将不会编号。

如果要在书目中包含项目而不在正文中实际引用它们，则可以定义一个虚拟`nocite`元数据字段并将引用放在此处：

```
---
nocite: |
  @item1, @item2
...

@item3
```

在这个例子中，该文件将包含在引用`item3`而已，但参考书目将包含以下条目`item1`，`item2`和`item3`。

可以使用通配符创建包含所有引文的书目，无论它们是否出现在文档中：

```
---
nocite: |
  @*
...
```

对于LaTeX输出，您还可以使用[`natbib`](https://ctan.org/pkg/natbib)或[`biblatex`](https://ctan.org/pkg/biblatex)渲染参考书目。为此，请按照上述说明指定书目文件，并在调用中添加[`--natbib`](https://pandoc.org/MANUAL.html#option--natbib)或[`--biblatex`](https://pandoc.org/MANUAL.html#option--biblatex)参数`pandoc`。请记住，书目文件必须采用各自的格式（BibTeX或BibLaTeX）。

有关更多信息，请参见[pandoc-citeproc手册页](https://github.com/jgm/pandoc-citeproc/blob/master/man/pandoc-citeproc.1.md)。

## 非Pandoc扩展

在pandoc中，默认情况下未启用以下Markdown语法扩展名，但可以通过将`+EXTENSION`扩展名添加到格式名称中来启用`EXTENSION`。因此，例如`markdown+hard_line_breaks`Markdown带有硬换行符。

#### 延期： `attributes`

允许将属性附加到任何内联或块级元素。属性的语法与中使用的语法相同[`header_attributes`](https://pandoc.org/MANUAL.html#extension-header_attributes)。

-   内联元素之后立即出现的属性会影响该元素。如果它们跟随一个空间，则它们属于该空间。（因此，此选项包含`inline_code_attributes`和`link_attributes`。）
-   一行上紧接在块元素之前的属性会影响该元素。
-   连续属性说明符可用于块或内联。它们的属性将被合并。
-   Setext或ATX标题的文本末尾出现的属性（与文本之间用空格分隔）会影响标题元素。（因此，该选项包含在内`header_attributes`。）
-   在带围栏的代码块中的打开围栏之后出现的属性会影响该代码块元素。（因此，该选项包含在内`fenced_code_attributes`。）
-   引用链接定义末尾出现的属性会影响引用该定义的链接。

请注意，pandoc的AST当前不允许将属性附加到任意元素。因此，如果需要，将添加Span或Div容器。

#### 延期： `old_dashes`

选择pandoc <= 1.8.2.1行为来解析智能破折号：`-`在数字前是一个破折号，又`--`是一个破折号。此选项仅在`smart`启用后才有效。自动选择`textile`输入。

#### 延期： `angle_brackets_escapable`

允许`<`并`>`进行反斜杠转义，因为它们可以在GitHub风格的Markdown中出现，但不能在原始Markdown中出现。pandoc的default暗示了这一点`all_symbols_escapable`。

#### 延期： `lists_without_preceding_blankline`

允许列表在段落之后出现，中间没有空格。

#### 延期： `four_space_rule`

选择用于解析列表的pandoc <= 2.0行为，以便列表项继续段落需要四个空格缩进。

#### 延期： `spaced_reference_links`

例如，在参考链接的两个组件之间允许使用空格，

```
[foo] [bar].
```

#### 延期： `hard_line_breaks`

使段落中的所有换行符都解释为硬换行符而不是空格。

#### 延期： `ignore_line_breaks`

导致段落中的换行符被忽略，而不是被视为空格或硬换行符。此选项适用于东亚语言，在东亚语言中，单词之间不使用空格，但为了便于阅读，文本分为几行。

#### 延期： `east_asian_line_breaks`

当两个换行符出现在两个东亚宽字符之间时，导致忽略该换行符，而不是将它们视为空格或换行符。这是比`ignore_line_breaks`包含东亚宽字符和其他字符的文本更好的选择。

#### 延期： `emoji`

解析文本表情符号，例如`:smile:`Unicode表情符号。

#### 延期： `tex_math_single_backslash`

什么原因之间`\(`和`\)`被解释为内嵌TeX的数学和之间的任何`\[`和`\]`被解释为显示TeX的数学。注意：此扩展程序的一个缺点是它不能转义`(`和`[`。

#### 延期： `tex_math_double_backslash`

什么原因之间`\\(`和`\\)`被解释为内嵌TeX的数学和之间的任何`\\[`和`\\]`被解释为显示TeX的数学。

#### 延期： `markdown_attribute`

默认情况下，pandoc将块级标签中的材料解释为Markdown。此扩展更改了行为，以便仅当标记具有属性时，才在块级标记中解析Markdown `markdown=1`。

#### 延期： `mmd_title_block`

在文档顶部启用[MultiMarkdown](https://fletcherpenney.net/multimarkdown/)样式标题[栏](https://fletcherpenney.net/multimarkdown/)，例如：

```
Title:   My title
Author:  John Doe
Date:    September 1, 2008
Comment: This is a sample mmd title block, with
         a field spanning multiple lines.
```

有关详细信息，请参见MultiMarkdown文档。如果启用`pandoc_title_block`或`yaml_metadata_block`，它将优先于`mmd_title_block`。

#### 延期： `abbreviations`

解析PHP Markdown额外的缩写键，例如

```
*[HTML]: Hypertext Markup Language
```

请注意，pandoc文档模型不支持缩写，因此，如果启用了此扩展名，则仅跳过缩写键（而不是将其解析为段落）。

#### 延期： `autolink_bare_uris`

使所有绝对URI成为链接，即使没有尖尖括号也是如此`<...>`。

#### 延期： `mmd_link_attributes`

解析链接和图像引用上的multimarkdown样式键值属性。此扩展不应与[`link_attributes`](https://pandoc.org/MANUAL.html#extension-link_attributes)扩展混淆。

```
This is a reference ![image][ref] with multimarkdown attributes.

[ref]: https://path.to/image "Image title" width=20px height=30px
       id=myId class="myClass1 myClass2"
```

#### 延期： `mmd_header_identifiers`

解析multimarkdown样式标题标识符（在标题之后，但在`#`ATX标题中的任何结尾s 之前的方括号中）。

#### 延期： `compact_definition_lists`

激活pandoc 1.12.x和更早版本的定义列表语法。此语法在几个方面与上面“ [定义列表”](https://pandoc.org/MANUAL.html#definition-lists)下描述的语法不同：

-   定义列表的连续项目之间不需要空白行。
-   要获得“紧凑”或“紧凑”列表，请在连续的项目之间省略空格；术语及其定义之间的空间不会影响任何内容。
-   不允许延迟换行：整个定义必须缩进四个空格。[4](https://pandoc.org/MANUAL.html#fn4)

#### 延期： `gutenberg`

使用[Gutenberg项目](https://www.gutenberg.org/)惯例进行`plain`输出：全大写形式用于强调，下划线包围以用于常规强调，在标题周围添加额外的空格。

## Markdown变体

除了pandoc的扩展Markdown之外，还支持以下Markdown变体：

`markdown_phpextra` （PHP Markdown Extra）

`footnotes`，`pipe_tables`，`raw_html`，`markdown_attribute`，`fenced_code_blocks`，`definition_lists`，`intraword_underscores`，`header_attributes`，`link_attributes`，`abbreviations`，`shortcut_reference_links`，`spaced_reference_links`。

`markdown_github` （已弃用GitHub-Flavored Markdown）

`pipe_tables`，`raw_html`，`fenced_code_blocks`，`auto_identifiers`，`gfm_auto_identifiers`，`backtick_code_blocks`，`autolink_bare_uris`，`space_in_atx_header`，`intraword_underscores`，`strikeout`，`task_lists`，`emoji`，`shortcut_reference_links`，`angle_brackets_escapable`，`lists_without_preceding_blankline`。

`markdown_mmd` （MultiMarkdown）

`pipe_tables`，`raw_html`，`markdown_attribute`，`mmd_link_attributes`，`tex_math_double_backslash`，`intraword_underscores`，`mmd_title_block`，`footnotes`，`definition_lists`，`all_symbols_escapable`，`implicit_header_references`，`auto_identifiers`，`mmd_header_identifiers`，`shortcut_reference_links`，`implicit_figures`，`superscript`，`subscript`，`backtick_code_blocks`，`spaced_reference_links`，`raw_attribute`。

`markdown_strict` （Markdown.pl）

`raw_html`，`shortcut_reference_links`，`spaced_reference_links`。

我们还支持`commonmark`和`gfm`（（作为GitHub扩展的Markdown，这是作为的一组扩展实现的`commonmark`）。

但是请注意，`commonmark`并且`gfm`对扩展的支持有限。只有那些下面列出（和`smart`，`raw_tex`和`hard_line_breaks`）会工作。但是，可以单独禁用所有扩展。同样，`raw_tex`仅影响`gfm`输出，不影响输入。

`gfm` （GitHub-Flavored Markdown）

`pipe_tables`，`raw_html`，`native_divs`，`fenced_code_blocks`，`auto_identifiers`，`gfm_auto_identifiers`，`backtick_code_blocks`，`autolink_bare_uris`，`space_in_atx_header`，`intraword_underscores`，`strikeout`，`task_lists`，`emoji`，`shortcut_reference_links`，`angle_brackets_escapable`，`lists_without_preceding_blankline`。

# 使用Pandoc制作幻灯片

您可以使用pandoc生成HTML + JavaScript幻灯片演示文稿，可以通过Web浏览器进行查看。使用[S5](https://meyerweb.com/eric/tools/s5/)，[DZSlides](http://paulrouget.com/dzslides/)，[Slidy](https://www.w3.org/Talks/Tools/Slidy2/)，[Slideous](https://goessner.net/articles/slideous/)或[Reveal.js](https://revealjs.com/)可以通过五种方法来执行此[操作](https://revealjs.com/)。您也可以使用LaTeX制作PDF幻灯片[`beamer`](https://ctan.org/pkg/beamer)，或以Microsoft [PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint)格式幻灯片。

这是Markdown的简单幻灯片显示源`habits.txt`：

```
% Habits
% John Doe
% March 22, 2005

# In the morning

## Getting up

- Turn off alarm
- Get out of bed

## Breakfast

- Eat eggs
- Drink coffee

# In the evening

## Dinner

- Eat spaghetti
- Drink wine

------------------

![picture of spaghetti](images/spaghetti.jpg)

## Going to sleep

- Get in bed
- Count sheep
```

要生成HTML / JavaScript幻灯片，只需键入

```
pandoc -t FORMAT -s habits.txt -o habits.html
```

其中`FORMAT`或者是`s5`，`slidy`，`slideous`，`dzslides`，或`revealjs`。

对于Slidy，Slideous，reveal.js和S5，由pandoc生成并带有[`-s/--standalone`](https://pandoc.org/MANUAL.html#option--standalone)选项的文件会嵌入指向JavaScript和CSS文件的链接，这些链接假定在相对路径`s5/default`（对于S5），`slideous`（对于Slideous），`reveal.js`（的网址`w3.org`（可显示代码），或访问Slidy网站（用于Slidy）。（这些路径可以通过设置来改变`slidy-url`，`slideous-url`，`revealjs-url`，或`s5-url`变量;参见[用于HTML幻灯片变量](https://pandoc.org/MANUAL.html#variables-for-html-slides)。，上文）对于DZSlides中，（相对短）JavaScript和CSS包括默认的文件中。

对于所有HTML幻灯片格式，此[`--self-contained`](https://pandoc.org/MANUAL.html#option--self-contained)选项可用于生成一个文件，其中包含显示幻灯片所需的所有数据，包括链接的脚本，样式表，图像和视频。

要使用投影仪生成PDF幻灯片，请键入

```
pandoc -t beamer habits.txt -o habits.pdf
```

请注意，reveal.js幻灯片也可以通过从浏览器打印到文件中而转换为PDF。

要制作PowerPoint幻灯片，请键入

```
pandoc habits.txt -o habits.pptx
```

## 安排幻灯片放映

默认情况下，*幻灯片级别*是层次结构中的最高标题级别，紧随其后的是文档中某处的内容，而不是另一个标题。在上面的示例中，级别1标题之后始终是级别2标题，其后是内容，因此幻灯片级别为2。可以使用[`--slide-level`](https://pandoc.org/MANUAL.html#option--slide-level)选项覆盖此默认值。

该文档根据以下规则分为幻灯片：

-   水平尺总是开始新的幻灯片。
    
-   幻灯片级别的标题始终会开始创建新幻灯片。
    
-   标题*下面的*层次结构中的幻灯片级别创建标题*中*的幻灯片。
    
-   层次结构中幻灯片级别*上方*的标题会创建“标题幻灯片”，其中仅包含章节标题，并有助于将幻灯片分为几部分。这些标题下的非幻灯片内容将包含在标题幻灯片中（用于HTML幻灯片显示）或后续具有相同标题的幻灯片中（用于投影机）。
    
-   标题页是从文档的标题栏自动构建的（如果存在）。（对于投影仪，可以通过注释掉默认模板中的某些行来禁用此功能。）
    

这些规则旨在支持许多不同样式的幻灯片放映。如果您不在乎将幻灯片按节和小节进行结构化，则可以对每张幻灯片使用1级标题。（在这种情况下，级别1将是幻灯片级别。）但是，您也可以像上面的示例一样将幻灯片放映结构分成几部分。

注：在reveal.js幻灯片中，如果幻灯片级别为2，则将生成二维布局，其中级别1的标题水平构建，级别2的标题垂直构建。不建议您将更多级别的嵌套嵌套与reveal.js一起使用。

## 增量清单

默认情况下，这些作者生成的列表显示“一次全部”。如果您希望列表递增显示（一次显示一项），请使用该[`-i`](https://pandoc.org/MANUAL.html#option--incremental)选项。如果要使特定列表偏离默认列表，请将其放在`div`class `incremental`或类中`nonincremental`。因此，例如，使用`fenced div`语法，无论文档默认如何，以下内容都是递增的：

```
::: incremental

- Eat spaghetti
- Drink wine

:::
```

要么

```
::: nonincremental

- Eat spaghetti
- Drink wine

:::
```

虽然建议使用`incremental`and `nonincremental`divs是根据情况设置增量列表的推荐方法，但也支持较旧的方法：将列表放在blockquote内将偏离文档默认值（也就是说，它将逐步显示而没有该[`-i`](https://pandoc.org/MANUAL.html#option--incremental)选项，并且所有同时使用该[`-i`](https://pandoc.org/MANUAL.html#option--incremental)选项）：

```
> - Eat spaghetti
> - Drink wine
```

两种方法都允许将增量和非增量列表混合在单个文档中。

注意：[`-i/--incremental`](https://pandoc.org/MANUAL.html#option--incremental)此处介绍的选项或任何方法当前均不适用于PowerPoint输出。

## 插入暂停

您可以在幻灯片中添加“暂停”，方法是添加一个包含三个点的段落，并用空格隔开：

```
# Slide with a pause

content before the pause

. . .

content after the pause
```

注意：PowerPoint输出尚未实现此功能。

## 造型幻灯片

您可以通过将自定义CSS文件放在`$DATADIR/s5/default`（对于S5），`$DATADIR/slidy`（对于Slidy）或`$DATADIR/slideous`（对于Slideous）`$DATADIR`（用户数据目录[`--data-dir`](https://pandoc.org/MANUAL.html#option--data-dir)位于）中来更改HTML幻灯片的样式。原始文件可以在pandoc的系统数据目录中找到（通常为`$CABALDIR/pandoc-VERSION/s5/default`）。Pandoc将在此处查找用户数据目录中找不到的任何文件。

对于dzslides，CSS包含在HTML文件本身中，可以在此处进行修改。

可以通过变量设置所有[reveal.js配置选项](https://revealjs.com/config/)。例如，可以通过设置`theme`变量来使用主题：

```
-V theme=moon
```

或者，您可以使用[`--css`](https://pandoc.org/MANUAL.html#option--css)选项指定自定义样式表。

为了风格的幻灯片投影仪，你可以指定一个`theme`，`colortheme`，`fonttheme`，`innertheme`，和`outertheme`使用[`-V`](https://pandoc.org/MANUAL.html#option--variable)选项：

```
pandoc -t beamer habits.txt -V theme:Warsaw -o habits.pdf
```

请注意，标题属性将变成HTML幻灯片格式的幻灯片属性（在`<div>`或上`<section>`），使您可以设置单个幻灯片的样式。在Beamer中，唯一会影响幻灯片的标题属性是`allowframebreaks`class，该类设置`allowframebreaks`选项，如果内容超出框架，则会创建多个幻灯片。特别推荐用于书目：

```
# References {.allowframebreaks}
```

## 演讲者备注

show.js和PowerPoint（pptx）输出中支持演讲者注释。您可以这样在Markdown文档中添加注释：

```
::: notes

This is my note.

- It can contain Markdown
- like this list

:::
```

要在reveal.js中显示注释窗口，请`s`在查看演示文稿时按。PowerPoint中的演讲者注释将照常在讲义和演示者视图中提供。

其他幻灯片格式尚不支持注释，但是注释不会出现在幻灯片本身上。

## 列

要将材料并排放置，可以使用具有class的本机div容器`columns`，其中包含两个或多个具有class `column`和`width`属性的div容器：

```
:::::::::::::: {.columns}
::: {.column width="40%"}
contents...
:::
::: {.column width="60%"}
contents...
:::
::::::::::::::
```

### Beamer中的其他列属性

div容器具有类，`columns`并且`column`可以选择具有`align`属性。该类`columns`可以选择具有`totalwidth`属性或`onlytextwidth`类。

```
:::::::::::::: {.columns align=center totalwidth=8em}
::: {.column width="40%"}
contents...
:::
::: {.column width="60%" align=bottom}
contents...
:::
::::::::::::::
```

的`align`有关属性`columns`和`column`可与值一起使用`top`，`top-baseline`，`center`和`bottom`对垂直对齐的列。默认为`top`in `columns`。

该`totalwidth`属性将列的宽度限制为给定值。

```
:::::::::::::: {.columns align=top .onlytextwidth}
::: {.column width="40%" align=center}
contents...
:::
::: {.column width="60%"}
contents...
:::
::::::::::::::
```

该类`onlytextwidth`将设置`totalwidth`为`\textwidth`。

有关更多详细信息，请参见《[Beamer用户指南》的](http://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf) 12.7节。

## 投影仪中的框架属性

有时有必要将LaTeX `[fragile]`选项添加到投影仪的框架中（例如，在使用`minted`环境时）。可以通过将`fragile`类添加到介绍幻灯片的标题中来强制执行此操作：

```
# Fragile slide {.fragile}
```

所有在的第8.1节中描述的其它框的属性[比默用户指南](http://mirrors.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf)，也可以使用：`allowdisplaybreaks`，`allowframebreaks`，`b`，`c`，`t`，`environment`，`label`，`plain`，`shrink`，`standout`，`noframenumbering`。

## Reveal.js和Beamer中的背景

可以将背景图像添加到独立的Reveal.js幻灯片和Beamer幻灯片中。

对于每张幻灯片上的同一图像，请`background-image`在YAML元数据块中或将其用作命令行变量来使用配置选项。（在Beamer中没有其他选项，本节的其余部分与Reveal.js幻灯片有关。）

对于Reveal.js，您可以改用Reveal.js-native选项`parallaxBackgroundImage`。您还可以以相同的方式进行设置`parallaxBackgroundHorizontal`，`parallaxBackgroundVertical`并且还必须进行设置`parallaxBackgroundSize`以使您的值生效。

要为特定的reveal.js幻灯片设置图像，请添加`{data-background-image="/path/to/image"}`到幻灯片上的第一个幻灯片级别标题（甚至可能为空）。

在explain.js的概述模式下，parallaxBackgroundImage仅显示在第一张幻灯片上。

其他reveal.js背景设置还对个别幻灯片，包括工作`data-background-size`，`data-background-repeat`，`data-background-color`，`data-transition`，和`data-transition-speed`。

要将背景图像添加到自动生成的标题幻灯片中，请使用`title-slide-attributes`YAML元数据块中的变量。它必须包含属性名称和值的映射。

有关更多详细信息，请参见[Reveal.js文档](https://revealjs.com/backgrounds/)。

例如在reveal.js中：

```
---
title: My Slideshow
parallaxBackgroundImage: /path/to/my/background_image.png
title-slide-attributes:
    data-background-image: /path/to/title_image.png
    data-background-size: contain
---

## Slide One

Slide 1 has background_image.png as its background.

## {data-background-image="/path/to/special_image.jpg"}

Slide 2 has a special image for its background, even though the heading has no content.
```

# 使用Pandoc创建EPUB

## EPUB元数据

可以使用该[`--epub-metadata`](https://pandoc.org/MANUAL.html#option--epub-metadata)选项指定EPUB元数据，但是如果源文档是Markdown，则最好使用[YAML元数据块](https://pandoc.org/MANUAL.html#extension-yaml_metadata_block)。这是一个例子：

```
---
title:
- type: main
  text: My Book
- type: subtitle
  text: An investigation of metadata
creator:
- role: author
  text: John Smith
- role: editor
  text: Sarah Jones
identifier:
- scheme: DOI
  text: doi:10.234234.234/33
publisher:  My Press
rights: © 2007 John Smith, CC BY-NC
ibooks:
  version: 1.3.4
...
```

可以识别以下字段：

`identifier`

字符串值或具有字段`text`和的对象`scheme`。有效值的`scheme`是`ISBN-10`，`GTIN-13`，`UPC`，`ISMN-10`，`DOI`，`LCCN`，`GTIN-14`，`ISBN-13`，`Legal deposit number`，`URN`，`OCLC`，`ISMN-13`，`ISBN-A`，`JP`，`OLCC`。

`title`

字符串值，或者是包含字段`file-as`和的对象`type`，或者是此类对象的列表。为有效值`type`ARE `main`，`subtitle`，`short`，`collection`，`edition`，`extended`。

`creator`

一个字符串值，或与域的对象`role`，`file-as`和`text`，或者这样的对象的列表。有效值`role`是[MARC关联者](https://loc.gov/marc/relators/relaterm.html)，但pandoc会尝试将人类可读的版本（例如“作者”和“编辑者”）转换为适当的marc关联者。

`contributor`

与相同的格式`creator`。

`date`

`YYYY-MM-DD`格式的字符串值。（只有年份是必要的。）Pandoc将尝试转换其他常见的日期格式。

`lang`（或遗留：`language`）

[BCP 47](https://tools.ietf.org/html/bcp47)格式的字符串值。如果未指定任何内容，则Pandoc将默认为本地语言。

`subject`

字符串值或此类值的列表。

`description`

字符串值。

`type`

字符串值。

`format`

字符串值。

`relation`

字符串值。

`coverage`

字符串值。

`rights`

字符串值。

`cover-image`

字符串值（封面图像的路径）。

`css`（或遗留：`stylesheet`）

字符串值（CSS样式表的路径）。

`page-progression-direction`

无论是`ltr`或`rtl`。指定[元素](http://idpf.org/epub/301/spec/epub-publications.html#sec-spine-elem)的`page-progression-direction`属性。 [`spine`](http://idpf.org/epub/301/spec/epub-publications.html#sec-spine-elem)

`ibooks`

iBooks特定的元数据，具有以下字段：

-   `version`：（字符串）
-   `specified-fonts`：`true`| `false`（默认`false`）
-   `ipad-orientation-lock`：`portrait-only`|`landscape-only`
-   `iphone-orientation-lock`：`portrait-only`|`landscape-only`
-   `binding`：`true`| `false`（默认`true`）
-   `scroll-axis`：`vertical`| `horizontal`|`default`

## 该`epub:type`属性

对于`epub3`输出，您可以使用[`epub:type`属性](http://www.idpf.org/epub/31/spec/epub-contentdocs.html#sec-epub-type-attribute)标记与EPUB章节相对应的标题。例如，要将属性设置为value `prologue`，请使用以下markdown：

```
# My chapter {epub:type=prologue}
```

这将导致：

```
<body epub:type="frontmatter">
  <section epub:type="prologue">
    <h1>My chapter</h1>
```

`<body epub:type="bodymatter">`除非使用以下值之一，否则Pandoc将输出，在这种情况下，将输出`frontmatter`或`backmatter`。

| `epub:type` 第一节 | `epub:type` 身体 |
| --- | --- |
| 序幕 | 前题 |
| 抽象 | 前题 |
| 致谢 | 前题 |
| 版权页 | 前题 |
| 奉献 | 前题 |
| 学分 | 前题 |
| 关键字 | 前题 |
| 烙印 | 前题 |
| 贡献者 | 前题 |
| 其他学分 | 前题 |
| 勘误 | 前题 |
| 修订记录 | 前题 |
| 标题页 | 前题 |
| 半标题页 | 前题 |
| 系列页面 | 前题 |
| 前言 | 前题 |
| 前言 | 前题 |
| 系列页面 | 前题 |
| 附录 | 回事 |
| 胶体 | 回事 |
| 参考书目 | 回事 |
| 指数 | 回事 |

## 链接媒体

默认情况下，pandoc将下载从任何引用的媒体`<img>`，`<audio>`，`<video>`或`<source>`存在于所生成的EPUB元件，并且将其包含在容器EPUB，得到一种完全自包含的EPUB。如果要链接到外部媒体资源，请在源中使用原始HTML，并`data-external="1"`使用`src`属性将其添加到标签中。例如：

```
<audio controls="1">
  <source src="https://example.com/music/toccata.mp3"
          data-external="1" type="audio/mpeg">
  </source>
</audio>
```

# 使用Pandoc创建Jupyter笔记本

创建[Jupyter笔记本时](https://nbformat.readthedocs.io/en/latest/)，pandoc将尝试推断笔记本的结构。具有该类的代码块`code`将被视为代码单元，中间内容将被作为Markdown单元。将自动为Markdown单元中的图像创建附件。元数据将从`jupyter`元数据字段中获取。例如：

```
---
title: My notebook
jupyter:
  nbformat: 4
  nbformat_minor: 5
  kernelspec:
     display_name: Python 2
     language: python
     name: python2
  language_info:
     codemirror_mode:
       name: ipython
       version: 2
     file_extension: ".py"
     mimetype: "text/x-python"
     name: "python"
     nbconvert_exporter: "python"
     pygments_lexer: "ipython2"
     version: "2.7.15"
---

# Lorem ipsum

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.

``` code
print("hello")
```

## Pyout

``` code
from IPython.display import HTML
HTML("""
<script>
console.log("hello");
</script>
<b>HTML</b>
""")
```

## Image

This image ![image](myimage.png) will be
included as a cell attachment.
```

如果要添加单元格属性，对单元格进行不同的分组或将输出添加到代码单元格，则需要包括div来指示结构。您可以为此使用[围栏div](https://pandoc.org/MANUAL.html#extension-fenced_divs)或[本机div](https://pandoc.org/MANUAL.html#extension-native_divs)。这是一个例子：

```
:::::: {.cell .markdown}
# Lorem

**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.
::::::

:::::: {.cell .code execution_count=1}
``` {.python}
print("hello")
```

::: {.output .stream .stdout}
```
hello
```
:::
::::::

:::::: {.cell .code execution_count=2}
``` {.python}
from IPython.display import HTML
HTML("""
<script>
console.log("hello");
</script>
<b>HTML</b>
""")
```

::: {.output .execute_result execution_count=2}
```{=html}
<script>
console.log("hello");
</script>
<b>HTML</b>
hello
```
:::
::::::
```

如果在输出单元格中包含原始HTML或TeX，请使用\[raw attribute\] \[Extension：`fenced_attribute`\]，如上面示例的最后一个单元格所示。尽管pandoc可以处理“裸”原始HTML和TeX，但结果通常是散布着原始元素和普通文本元素，并且在输出单元格中，pandoc期望有一个单独的，连接的原始块。为避免使用原始HTML或TeX，除非使用原始属性进行显式标记，否则建议`-raw_html-raw_tex+raw_attribute`在Markdown和ipynb笔记本之间进行翻译时指定扩展名。

请注意，影响Markdown读取和写入的选项和扩展也会影响ipynb笔记本中的Markdown单元。例如，[`--wrap=preserve`](https://pandoc.org/MANUAL.html#option--wrap)将在Markdown单元格中保留换行符；[`--atx-headers`](https://pandoc.org/MANUAL.html#option--atx-headers)将导致使用ATX样式的标题；并[`--preserve-tabs`](https://pandoc.org/MANUAL.html#option--preserve-tabs)可以防止将制表符转为空格。

# 语法高亮

Pandoc会自动在带有语言名称标记的[受防护代码块](https://pandoc.org/MANUAL.html#fenced-code-blocks)中突出显示语法。Haskell库的[天窗](https://github.com/jgm/skylighting)用于突出显示。当前，仅HTML，EPUB，Docx，Ms和LaTeX / PDF输出支持突出显示。要查看pandoc可以识别的语言名称列表，请输入`pandoc --list-highlight-languages`。

可以使用[`--highlight-style`](https://pandoc.org/MANUAL.html#option--highlight-style)选项选择配色方案。默认配色方案是`pygments`，它模仿Python库pygments使用的默认配色方案（尽管pygments实际上并未用于突出显示）。要查看突出显示样式的列表，请键入`pandoc --list-highlight-styles`。

如果您对预定义样式不满意，可以使用[`--print-highlight-style`](https://pandoc.org/MANUAL.html#option--print-highlight-style)生成JSON `.theme`文件，该文件可以修改并用作的参数[`--highlight-style`](https://pandoc.org/MANUAL.html#option--highlight-style)。要获取`pygments`样式的JSON版本，例如：

```
pandoc --print-highlight-style pygments > my.theme
```

然后`my.theme`像这样编辑和使用它：

```
pandoc --highlight-style my.theme
```

如果您对内置突出显示不满意，或者想要突出显示不支持的语言，则可以使用该[`--syntax-definition`](https://pandoc.org/MANUAL.html#option--syntax-definition)选项加​​载[KDE样式的XML语法定义文件](https://docs.kde.org/stable5/en/applications/katepart/highlight.html)。在编写自己的脚本之前，请查看KDE的[语法定义存储库](https://github.com/KDE/syntax-highlighting/tree/master/data/syntax)。

要禁用突出显示，请使用该[`--no-highlight`](https://pandoc.org/MANUAL.html#option--no-highlight)选项。

# 自定义样式

自定义样式可以以docx和ICML格式使用。

## 输出量

默认情况下，pandoc的docx和ICML输出为块（如段落和块引号）应用预定义的样式集，并对内联使用很大程度上默认的格式（斜体，粗体）。这将适用于大多数目的，尤其是与`reference.docx`文件一起使用。但是，如果您需要将自己的样式应用于图块，或者与一组预先存在的样式匹配，则pandoc允许您分别使用`div`s和`span`s 为图块和文本定义自定义样式。

如果您使用属性定义`div`或`span`，则`custom-style`pandoc会将指定的样式应用于所包含的元素（功能取决于样式的元素（如标题，代码块，块引号或链接）除外）。因此，例如，使用`bracketed_spans`语法，

```
[Get out]{custom-style="Emphatically"}, he said.
```

会生成一个带有字符样式设置为“ Get out”的docx文件`Emphatically`。同样，使用`fenced_divs`语法，

```
Dickinson starts the poem simply:

::: {custom-style="Poetry"}
| A Bird came down the Walk---
| He did not know I saw---
:::
```

将使用`Poetry`段落样式来对包含的两行进行样式设置。

对于docx输出，如果您的reference.docx中还没有样式，则样式将在输出文件中定义为从普通文本继承。如果已经定义，则pandoc不会更改定义。

此功能允许与[pandoc过滤器](https://pandoc.org/filters.html)一起进行最大程度的自定义。如果希望缩进引号后的所有段落，则可以编写过滤器以应用必要的样式。如果希望将所有斜体转换为`Emphasis`字符样式（可能会更改其颜色），则可以编写一个过滤器，该过滤器会将所有斜体内联转换为`Emphasis`自定义样式内的内联`span`。

对于docx输出，您无需启用任何扩展名即可使用自定义样式。

## 输入值

默认情况下，docx阅读器仅通过直接转换或解释输入文档样式的派生来读取可以转换为pandoc元素的样式。

通过在docx阅读器（）中启用[`styles`扩展名](https://pandoc.org/MANUAL.html#ext-styles)[`-f docx+styles`](https://pandoc.org/MANUAL.html#option--from)，您可以使用`custom-style`该类来生成保留输入文档样式的输出。段落样式解释为div，而字符样式解释为span。

例如，使用`custom-style-reference.docx`测试目录中的文件，我们具有以下不同的输出：

没有`+styles`扩展名：

```
$ pandoc test/docx/custom-style-reference.docx -f docx -t markdown
This is some text.

This is text with an *emphasized* text style. And this is text with a
**strengthened** text style.

> Here is a styled paragraph that inherits from Block Text.
```

并带有扩展名：

```
$ pandoc test/docx/custom-style-reference.docx -f docx+styles -t markdown

::: {custom-style="First Paragraph"}
This is some text.
:::

::: {custom-style="Body Text"}
This is text with an [emphasized]{custom-style="Emphatic"} text style.
And this is text with a [strengthened]{custom-style="Strengthened"}
text style.
:::

::: {custom-style="My Block Style"}
> Here is a styled paragraph that inherits from Block Text.
:::
```

使用这些自定义样式，您可以在创建docx输出时将输入文档用作参考文档（请参见下文），并在输入和输出文件中保持相同的样式。

# 习俗作家

Pandoc可以扩展为使用[Lua](https://www.lua.org/)编写的自定义作家。（Pandoc包含Lua解释器，因此不需要单独安装Lua。）

要使用自定义编写器，只需指定Lua脚本的路径来代替输出格式。例如：

```
pandoc -t data/sample.lua
```

创建自定义编写器要求为pandoc文档中的每个可能的元素编写一个Lua函数。要获取可以根据需要进行修改的记录示例，请执行

```
pandoc --print-default-data-file sample.lua
```

请注意，自定义编写器没有默认模板。如果要[`--standalone`](https://pandoc.org/MANUAL.html#option--standalone)与自定义编写器一起使用，则需要使用手动指定模板，[`--template`](https://pandoc.org/MANUAL.html#option--template)或者将新的默认模板的名称添加`default.NAME_OF_CUSTOM_WRITER.lua`到`templates`用户数据目录的子目录中（请参见[Templates](https://pandoc.org/MANUAL.html#templates)）。

# 安全注意事项

如果您使用pandoc在Web应用程序中转换用户贡献的内容，请记住以下几点：

1.  尽管pandoc本身不会创建或修改除您明确要求创建的文件以外的任何文件（用于生成PDF的临时文件除外），但过滤器或自定义编写器原则上可以在文件系统上执行任何操作。在使用过滤器和自定义编写器之前，请非常仔细地对其进行审核。
    
2.  如果您的应用程序将pandoc用作Haskell库（而不是脱壳到可执行文件），则可以通过在`PandocPure`monad中运行pandoc操作，在将pandoc与文件系统完全隔离的模式下使用它。有关更多详细信息，请参阅文档“ [使用pandoc API](https://pandoc.org/using-the-pandoc-api.html) ”。
    
3.  Pandoc的解析器可以在某些极端情况下展现出病理性能。明智的做法是将任何pandoc操作置于超时之下，以避免利用这些问题的DOS攻击。如果使用的是pandoc可执行文件，则可以添加命令行选项`+RTS -M512M -RTS`（例如）以将堆大小限制为512MB。
    
4.  不能保证pandoc生成的HTML是安全的。如果`raw_html`为Markdown输入启用了，则用户可以注入任意HTML。即使`raw_html`被禁用，用户也可以在标题，跨度和代码块的属性中包含危险内容。为了安全起见，您应该通过HTML清理程序运行所有生成的HTML。
    

# 作者

版权所有2006–2020 John MacFarlane（jgm@berkeley.edu）。根据[GPL](https://www.gnu.org/copyleft/gpl.html "GNU通用公共许可证")版本2或更高版本[发布](https://www.gnu.org/copyleft/gpl.html "GNU通用公共许可证")。该软件不提供任何形式的保证。（有关完整的版权和保修声明，请参阅COPYRIGHT。）有关贡献者的完整列表，请参见pandoc源代码中的AUTHORS.md文件。

***

1.  该规则的重点是确保以人的姓名缩写开头的普通段落，例如
    
    ```
    B. Russell was an English philosopher.
    ```
    
    不要被视为列表项。
    
    这条规则不会阻止
    
    ```
    (C) 2007 Joe Smith
    ```
    
    不会被解释为列表项。在这种情况下，可以使用反斜杠转义符：
    
    ```
    (C\) 2007 Joe Smith
    ```
    
    [↩︎](https://pandoc.org/MANUAL.html#fnref1)
2.  [大卫•惠勒](https://justatheory.com/2009/02/modest-markdown-proposal/)的建议给我带来了影响。[↩︎](https://pandoc.org/MANUAL.html#fnref2)
    
3.  该方案归于Michel Fortin提出，他在[Markdown讨论列表中](http://six.pairlist.net/pipermail/markdown-discuss/2005-March/001097.html)提出了该方案。[↩︎](https://pandoc.org/MANUAL.html#fnref3)
    
4.  要了解为什么懒惰与放松项目之间的空白行的要求不兼容，请考虑以下示例：
    
    ```
    bar
    :    definition
    foo
    :    definition
    ```
    
    这是一个具有两个“ bar”定义（其中第一个是延迟包装）的单个列表项，还是两个列表项？要消除歧义，我们必须禁止延迟包装或在列表项之间使用空白行。














































