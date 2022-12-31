# Bugs

# Open

```python

>> python -m manim graphing.py UpdatersExample -pl
Media will be written to ./media\. You can change this behavior with the --media_dir flag.

   UpdatersExample is not in the script


Unfortunately, the package iftex could not be installed.
Please check the log file:
C:\Users\admin\AppData\Local\MiKTeX\2.9\miktex\log\latex.log



Traceback (most recent call last):
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\extract_scene.py", line 155, in main
    scene = SceneClass(**scene_kwargs)
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\scene\scene.py", line 53, in __init__
    self.construct()
  File "graphing.py", line 19, in construct
    graph_lab = self.get_graph_label(func_graph, label = "x^{2}")
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\scene\graph_scene.py", line 204, in get_graph_label
    label = TexMobject(label)
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\mobject\svg\tex_mobject.py", line 144, in __init__
    self, self.arg_separator.join(tex_strings), **kwargs
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\mobject\svg\tex_mobject.py", line 44, in __init__
    self.template_tex_file_body
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\utils\tex_file_writing.py", line 19, in tex_to_svg_file
    dvi_file = tex_to_dvi(tex_file)
  File "C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\manimlib\utils\tex_file_writing.py", line 67, in tex_to_dvi
    "See log output above or the log file: %s" % log_file)
Exception: Latex error converting to dvi. See log output above or the log file: ./media\Tex\8af8aa35cd1d7d44.log



```






# closed
## GIF

https://github.com/3b1b/manim/pull/529


https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/


```python
ffmpeg  -i SquareToCircle.mp4 -f gif SquareToCircle.gif
```

更好看的https://github.com/3b1b/manim/issues/699


---------------------------


manim是如何显示汉字的呀？我怎么配置都不成功


https://www.bilibili.com/video/av42621196


## 中文解决后续

[鹤翔万里](https://space.bilibili.com/171431343)[](https://www.bilibili.com/blackboard/help.html#%E4%BC%9A%E5%91%98%E7%AD%89%E7%BA%A7%E7%9B%B8%E5%85%B3)在manimlib/constants.py文件中第42行TEX\_USE\_CTEX改成True



打开中间过程中生成的.tex文件后，发现里面中文已乱码，所以在后续的dvisvgm命令调用中未能将此乱码的内容转为svg，进而影响到后面。

解决方法
找到manim-master项目中的 tex_file_writing.py文件，将里面 with open(result, “w”) as outfile:
修改为 with open(result, “w”, encoding=‘utf-8’) as outfile:
————————————————

**上述中文都没用了，manim新版中看源$constants.py$**
```python 

Warning:
You haven't set font.
If you are not using English, this may cause text rendering problem.
You set font like:
text = Text('your text', font='your font')
or:
class MyText(Text):
    CONFIG = {
        'font': 'My Font'
    }


```

! LaTeX Error: File `ctexart.sty' not found.Type X to quit or <RETURN> to proceed,or enter new name. (Default extension: sty)Enter file name:! Emergency stop.<read > \linespread




已经解决，gtihub-manim-issues看到一个text设置font的例子













