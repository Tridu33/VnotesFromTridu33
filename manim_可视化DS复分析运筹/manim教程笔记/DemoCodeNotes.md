[TOC]

manim最新教程 系列视频 https://www.bilibili.com/video/BV19K411V7SV?p=13





# 1. DemoCodeNotes



```python




画Text

```python 
class makeText(Scene):
    def construct(self):
        #######Code#######中文不行
        #Making text
        first_line = TextMobject("Hello")
        second_line = TextMobject("So high!")
        third_line = TextMobject("Deal,delay no more,")
        final_line = TextMobject("Hi!", color=BLUE)
        color_final_line = TextMobject("Deal might late no doubt!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)
        third_line.next_to(second_line, DOWN)
        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line),Write(third_line))
        self.wait(1)
        self.play(FadeOut(second_line),FadeOut(third_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)

```

https://blog.csdn.net/wsx_9999/article/details/102642987
manim-TextMobject 换行
在需要换行的地方插入"\\\"即可

```python 

class example(Scene):
    def construct(self):
        text=TextMobject('This is the first raw. \\\ And this is the second raw.')
        self.play(Write(text),run_time=5)
        self.wait()
        
```

https://github.com/3b1b/manim/pull/680  各种文字教程，彩色，韩文变化字体等等

```python 
from manimlib.imports import *

class Demo(Scene):
    def construct(self):
        text = Text('Hello, world!')
        self.play(Write(text))
        
```

https://blog.csdn.net/wsx_9999/article/details/102672279
画钟表

```python 
class example(Scene):
    def construct(self):
        text_list=[]
        text_group=VGroup()
        for i in range(1,13):
            t=str(i)
            text=TextMobject(t)
            text.move_to(UP*2.5)
            text.rotate(-PI/6*i,about_point=ORIGIN)
            self.play(Write(text),run_time=0.2)
            text_list.append(text)
            text_group=VGroup(text_group,text_list[i-1])
        self.wait()
```



























