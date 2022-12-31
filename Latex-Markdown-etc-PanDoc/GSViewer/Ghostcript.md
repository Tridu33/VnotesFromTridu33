


https://github.com/topics/




https://web.mit.edu/ghostscript/www/Ps2pdf.htm

```
ps2pdf input.[e]ps input.pdf
```




postscript

ps


# 1. Ghostcript


GPL Ghostscript 9.50 (2019-10-15)

Copyright (C) 2019 Artifex Software, Inc. All rights reserved.

Usage: gs [switches] [filel.ps file2.ps ...]

Most frequently used switches:	(you can use # in place 〇f =)

-dNOPAUSE	no pause after page	|	-q	'quiet1, fewer messages

-g<width>x<height>	page size in pixels	|	-r<res>	pixels/inch resolution

-sDEVICE=<devname>	select device	|	-dBATCH	exit after last file

一s〇utputFile=<file> select output file: - for stdout, |command for pipe,

embed %d or %ld for page #

Input formats: PostScript PostScriptLevell PostScriptLevel2 PostScriptLevel3

Default output device: display

Available devices:

bbox bit bitcmyk bitrgb bitrgbtags bjlOe bj200 bjc600 bjc800 bmpl6 bmpl6m bmp256 bmp32b bmpgray bmpmono bmpsepl bmpsep8 cdeskjet cdj550 cdjcolor cdjmono chameleon declj250 deskjet devicen display djet500 djet500c eps2write eps9high eps9mid epson epsonc fpng gprf ibmpro ijs ink_cov inkcov jetp3852 jpeg jpegcmyk jpeggray laserjet lbp8 1j250 1jet2p 1jet3 1jet3d 1jet4 1jet4d 1jetplus m8510 mswinpr2 necp6 nullpage pam pamcmyk32 pamcmyk4 pbm pbmraw pclm pcxl6 pcx24b pcx256 pcxcmyk pcxgray pcxmono pdfimage24 pdfimage32 pdfimage8 pdfwrite pgm pgmraw pgnm pgnmraw pj pjxl pjxl300 pkmraw plan plane plang plank planm planr plib plibc plibg plibk plibm pngl6 pngl6m png256 pngalpha pnggray pngmono pngmonod pnm pnmemyk pnmraw ppm ppmraw ps2write psdemyk psdcmykl6 psdcmykog psdrgb psdrgbl6 pxlcolor pxlmono r4081 spotemyk st800 stcolor t4693d2 t4693d4 t4693d8 tek4696 tiff12nc tiff24nc tiff32nc tiff48nc tiff64nc tiffcrle tiffg3 tiffg32d tiffg4 tiffgray tifflzw tiffpack tiffscaled tiffscaled24 tiffscaled32 tiffscaled4 tiffscaled8 tiffsep tiffsepl txtwrite uniprint xpswrite

Search path:

C:\Program Files\gs\gs9.50\bin ; C:\Program Files\gs\gs9.50\lib ; C:\Program Files\gs\gs9.50\fonts ; %rom%Resource/Init/ ; %rom%lib/ ; c:/gs/gs9.50/Resource/Init ; c:/gs/gs9.50/lib ; c:/gs/gs9.50/Resource/Font ; c:/gs/fonts

Initialization files are compiled into the executable.

For more information, see c:/gs/gs9.50/doc/Use.htm.

Please report bugs to bugs.ghostscript.com.

Close this window with the close button on the title bar or the system menu.













example:  
gswin64 -dSAFER -dBATCH -dNOPAUSE -r300 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=jpeggray -sOutputFile=test%03d.jpg -dFirstPage=102 -dLastPage=103 ori.pdf  
  
-sDEVICE 支持 PNG, JPEG, TIFF, PNM, FAX, BMP, PCX, PSD 当然也有 pdfwrite, pswrite, epswrite

-r300 表示转出來的图像的解析度(resolution)是 300dpi

gswin64.exe 还支持 antialiasing ，可以根据 pdf 的字和图形各別做转
化：

-dTextAlphaBits=n : 用來支持文字的 antialiasing  
-dGraphicsAlphaBits=n : 用來支持图形的 antialiasing  
这两个 n 可以给到 4 就有可以接受的效果了。

如果文件本身不是彩色的，可以用 pnggray 或 jpeggray ，可以快一點。 %03d 用來编号，这样就会变成数字以 001, 002, … 一直下去。





gswin64 -dSAFER -dBATCH -dNOPAUSE -r300 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=jpeggray -sOutputFile=test%03d.jpg -dFirstPage=102 -dLastPage=103 plustimes.ps























