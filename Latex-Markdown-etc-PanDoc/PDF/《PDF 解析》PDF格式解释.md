

# PDF格式解释



【PDF里，到底都是些啥？-哔哩哔哩】 https://www.bilibili.com/video/BV1Vi4y1C71M/

开源工具链





MuPDF->SumatraPDF

MuPDFTool命令行工具

pdf重命名为txt，用命令行即可生成文本格式描述的pdf，不会出现二进制乱码 https://mupdf.com/docs/manual-mutool-convert.html

```cmd
./mutool.exe clean -a -d example.pdf plain.pdf
```

PDF动作，坐标，文字，渲染。只剩下排版信息，缺乏段落，画图等特点，仅仅描述如何排版

word导出“辅助功能文档标记”选项，添加额外的信息

-----------



LaTeX的磅pt'和PDF的磅pt不同:
14pt'*72/72.27 = 14.3462pt


## PDF Explained （译作《PDF 解析》）
PDF Explained (https://zxyle.github.io/PDF-Explained/) PDF Explained的非官方中文翻译版,  https://resources.oreilly.com/examples/0636920021483/


Adobe PDF Reference 1.7 (https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_1-7.pdf)



## pdftk
https://www.pdflabs.com/tools/pdftk-server/
是一个基于iText库的多平台命令行工具（在第116页的“iText for Java和C＃”中有描述）。 它具有合并，拆分和标记文档以及设置和读取元数据的功能。



下面示例：

合并PDF：

```
pdftk 1.pdf 2.pdf 3.pdf cat output 123.pdf
```
或者 (使用通配符):

```
pdftk *.pdf cat output combined.pdf
```
把多个PDF的不同页面组合成一个新的PDF文档(将one.pdf的前7页，two.pdf的前5页，one.pdf的第8页按先后顺序合并成combined.pdf)

```
pdftk A=one.pdf B=two.pdf cat A1-7 B1-5 A8 output combined.pdf
```

旋转PDF的第一页为顺时针90度（向东）（其余页方向不变，2-end表示第2页到最后一页）

```
pdftk in.pdf cat 1E 2-end output out.pdf
```
旋转PDF的第一页为逆时针（向西）90度，只提取第一页

```
pdftk in.pdf cat 1W output out.pdf
```
选择所有PDF页面180度：

```
pdftk in.pdf cat 1-endS output out.pdf
```
使用128强度加密PDF（安全模式，只读）

```
pdftk in.pdf output mydoc.128.pdf owner_pw foopass
```
同上，同时给PDF加上访问密码（会弹出一个密码输入框）

```
pdftk in.pdf output mydoc.128.pdf owner_pw foo user_pw baz
```
同上，但是运行打印：

```
pdftk in.pdf output mydoc.128.pdf owner_pw foo user_pw baz allow printing
```

解密PDF文档(foopass替换成pdf的owner_pw密码)：注意：前提是你得知道pdf的密码所以此功能只是解除所有者的密码，使阅读者不需要输密码

```
pdftk secured.pdf input_pw foopass output unsecured.pdf
```
合并两个PDF文档，其中一个是加密的，但最终文档不加密：

```
pdftk A=secured.pdf mydoc.pdf input_pw A=foopass cat output combined.pdf
```

解压PDF流，以便文本编辑：（不清楚是干什么用的）

```
pdftk mydoc.pdf output mydoc.clear.pdf uncompress
```
压缩PDF：
```
pdftk mydoc.pdf output mydoc.clear.pdf compress
```

修复PDF文档

```
pdftk broken.pdf output fixed.pdf
```
分解成单页（文件名以pg_开头）

```
pdftk mydoc.pdf burst
```
报告PDF信息，输出到文本

```
pdftk mydoc.pdf dump_data output report.txt
```

























































