[TOC]




------------------------------------

Grant Sanderson
3b1b
# 1. manim教程笔记ReadMe-官方


https://blog.csdn.net/YinShiJiaW/article/details/94409981




https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/



[Build Status](https://travis-ci.org/3b1b/manim)
[Documentation](https://www.eulertour.com/learn/manim/)
[MIT License](http://choosealicense.com/licenses/mit/)
[Manim Subreddit](https://www.reddit.com/r/manim/)
[Manim Discord](https://discord.gg/mMRrZQW)

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, as seen in the videos at [3Blue1Brown](https://www.3blue1brown.com/).


物理大佬教学
https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/

官方教程
https://www.eulertour.com/learn/manim/getting_started/index.html

github仓库
https://github.com/3b1b/manim#using-manim

外文教程很多，github源码就是最好的教程，已经有很多包在github一搜就有，本地目录：!manim_help
所有旧版文件通通把$big_ol_pile_of_manim_imports$更换成为

```python

# -*- coding: utf-8 -*-
'''
>File Name      :MyPractise.py

'''

from manimlib.imports import *
```



鹏程万里Tony写的：

[https://github.com/Tony031218/manim-projects](https://github.com/Tony031218/manim-projects)

cigar666写的内容：

https://www.bilibili.com/video/av42621196/
常见问题记录1
https://blog.csdn.net/bababi/article/details/84640840
第一阶段性总结

https://blog.csdn.net/YinShiJiaW/article/details/94409981

第二阶段性总结
https://blog.csdn.net/YinShiJiaW/article/details/95393683
https://www.bilibili.com/video/av52591210

工程结构理解
https://blog.csdn.net/YinShiJiaW/article/details/93586984

Bilibli的教程



https://www.bilibili.com/read/cv2539928?from=articleDetail  （1）

https://www.bilibili.com/read/cv2579540   教程latex，文字贴图（2）

https://www.bilibili.com/read/cv2650778/ 牛逼（3）



C:\Users\admin\Documents\Tridu33\!Py\!3b1b-video\manim\docs_Zh\build\html





```python

python -m manim example_scenes.py SquareToCircle -pl
python -m manim example_scenes.py OpeningManimExample -pl


```

texlive-fonts-extra 字体包
texlive-science 数学物理计算机科学的包

中文





# 2. TextMobject-TexObject




TextMobject和之间的主要区别TexMobject是，文本数学对象假定所有内容都是纯文本，除非您指定带有美元符号的方程式；而Tex数学对象假定所有内容都是方程式，除非您使用指定了某些内容是纯文本\\text{}。

资料来源：https : //talkingphysics.wordpress.com/

请注意，如果您使用原始字符串，例如，不需要双反斜杠。 r"\text{bla}"

https://github.com/3b1b/manim/issues/505
试试掰开用命令行latex运行，别继续进行这种没有用的小技巧，大智慧是解析源代码，不是抄袭小技巧复制别人的代码。



pdflatex @.tex




https://github.com/3b1b/manim/issues/768  
  

  
https://github.com/3b1b/manim/issues/671  
  

  
https://github.com/3b1b/manim/issues/707 原来如此textMobject








xelatex -.tex






编辑svg draw.io






新版只要用中文textMoject  Texobject就会报错。英文没问题，中文解决方案是不是只有Text字体？













# 3. 官方help






```python
python -m manim example_scenes.py SquareToCircle -pl
```

命令中，python解析器，manim.py以脚本方式执行的python文件，example_scenes.py用户文件名，SquareToCircle 是用户文件里的类名，表示执行该命令，还有很多参数api，下面介绍：

[^_^]:
    注释 (`>>`).
    
程序执行流程：主程序入口manim.py进入manimlib.main()

[//]: #(python文件有一个内置属性，__name__，如果它是一个被执行的脚本文件，那么它的值就会变成"__main__"，否则就是自身文件名，我们知道程序的入口只能有一个，python也不例外，解释器会寻找到__name__的值为"__main__"的文件并将它当作唯一脚本来执行)


根目录文件命令以及对应功能，正在调试进行中的文件名称为$demo.py$


帮助

-w报错，os错误


``` python
python -m  manim --help
usage: manim.py [-h] [-p] [-w] [-s] [-l] [-m] [--high_quality] [-g] [-i] [-f]
                [-t] [-q] [-a] [-o FILE_NAME] [-n START_AT_ANIMATION_NUMBER从动画编号开始]
                [-r 分辨率RESOLUTION] [-c COLOR] [--sound] [--leave_progress_bars]
                [--media_dir MEDIA_DIR]
                [--video_dir VIDEO_DIR | --video_output_dir VIDEO_OUTPUT_DIR]
                [--tex_dir TEX_DIR] [--livestream] [--to-twitch]
                [--with-key TWITCH_KEY]
                [file] [scene_names [scene_names ...]]

positional arguments:
  file                  path to file holding the python code for the scene包含场景的python代码的文件的路径
  scene_names           Name of the Scene class you want to see您要查看的Scene类的名称

optional arguments:
  -h, --help            show this help message and exit
  -p, --preview         Automatically open the saved file once its done完成后自动打开预览保存的文件

  -w, --write_to_movie  Render the scene as a movie file将场景渲染为电影文件
  -s, --save_last_frame 保存最后一帧Save the last frame
  -l, --low_quality     Render at a low quality (for faster rendering)快低质量渲染
  -m, --medium_quality  Render at a medium quality 中质量
  --high_quality        Render at a high quality 高质量
  -g, --save_pngs       Save each frame as a png 每帧保存png
  -i, --save_as_gif     Save the video as gif 视频保存为gif
  -f, --show_file_in_finder    Show the output file in finder 在finder中显示输出文件
  -t, --transparent     Render to a movie file with an alpha channel使用Alpha通道渲染到电影文件
  -q, --quiet
  -a, --write_all       Write all the scenes from a file写一个文件中所有场景
  -o FILE_NAME, --file_name FILE_NAME
                        Specify the name of the output file, ifit should be different from the scene class name指定输出文件的名称（如果它与场景类名称不同）
  -n START_AT_ANIMATION_NUMBER, --start_at_animation_number START_AT_ANIMATION_NUMBER
Start rendering not from the first animation, but from another, specified by its index. If you passin two comma separated values, e.g. "3,6", it will end the rendering at the second value不从第一个动画开始渲染，而是从其索引指定的另一个动画开始渲染。如果您传入两个逗号分隔的值，例如“ 3,6”，它将在第二个值处结束渲染
  -r RESOLUTION, --resolution RESOLUTION
                        Resolution, passed as "height,width"分辨率，“高度，宽度”传递
  -c COLOR, --color COLOR
                        Background color背景色
  --sound               Play a success/failure sound成功失败显示声音
  --leave_progress_bars
                        Leave progress bars displayed in terminal保持进度条显示在终端中
  --media_dir MEDIA_DIR
                        directory to write media写入多媒体路径
  --video_dir VIDEO_DIR
                        directory to write file tree for video写入视频文件树的目录
  --video_output_dir VIDEO_OUTPUT_DIR
                        directory to write video 编写视频的目录
  --tex_dir TEX_DIR     directory to write tex 写入text路径
  --livestream          Run in streaming mode流模式
  --to-twitch           Stream to twitch
  --with-key TWITCH_KEY
                        Stream key for twitch

位置参数：
  
保存场景的python代码的文件的文件路径
  
scene_names要查看的Scene类的名称


可选参数：
  
-h， -  help显示此帮助消息并退出
  
-p， -  preview一旦完成，自动打开保存的文件
  
-w， -  write_to_movie将场景渲染为影片文件
  
-s， -  save_last_frame保存最后一帧
  
-l， -  low_quality以低质量渲染（以便更快地渲染）
  
-m， -  medium_quality以中等质量渲染
  
--high_quality以高品质渲染
  
-g， -  save_pngs将每个帧保存为png
  
-i， -  save_as_gif将视频另存为gif
  
-f， -  show_file_in_finder
                        
在finder中显示输出文件
  
-t， -  transarent向具有Alpha通道的电影文件渲染
  
-q， -  quiet
  
-a， -  write_all写入文件中的所有场景
  
-o FILE_NAME， -  file_name FILE_NAME指定输出文件的名称，ifit应该是不同于场景类名
  
-n START_AT_ANIMATION_NUMBER， -  START_at_animation_number START_AT_ANIMATION_NUMBER
不是从第一个动画开始渲染，而是从另一个，由其索引指定。如果你通过两个
逗号分隔值，例如“3,6”，它将结束渲染第二个值

-r RESOLUTION， - 分辨率解决方案,分辨率，作为“高度，宽度”传递
  
-c COLOR， -  color COLOR背景颜色
  
--sound播放成功/失败声音
  
--leave_progress_bars在终端中显示进度条
  
--media_dir MEDIA_DIR目录写媒体
  
--video_dir VIDEO_DIR用于编写视频文件树的目录
  
--video_output_dir VIDEO_OUTPUT_DIR目录写视频

--tex_dir TEX_DIR目录写tex
--livestream以流模式运行 - 抽搐流到抽搐
--with-key TWITCH_KEY用于抽搐的流键


```
第一个和第二个命令行参数是必须给出的（哪个文件里哪个模块），而且必须要按顺序（可以区分的参数不用按照顺序，不可以区分的要按照顺序），之后都是可选参数。再往下面就是对获取到的命令行参数的提取，最后是对这些参数的使用，我们最终把这个包含参数的args对象返回出去给外部使用。



config.py命令行参数解析

```python 




def parse_cli():
    try:
        parser = argparse.ArgumentParser()
                module_location = parser.add_mutually_exclusive_group()
        module_location.add_argument(
            "file",
            nargs="?",
            help="path to file holding the python code for the scene源py代码路径",
        )
        parser.add_argument(
            "scene_names",
            nargs="*",
            help="Name of the Scene class you want to see场景类想看到的",
        )
        parser.add_argument(
            "-p", "--preview",
            action="store_true",
            help="Automatically open the saved file once its done一旦完成自动打开保存的文件",
        ),
        parser.add_argument(
            "-w", "--write_to_movie",
            action="store_true",
            help="Render the scene as a movie file写视频文件",
        ),
        parser.add_argument(
            "-s", "--save_last_frame",
            action="store_true",
            help="Save the last frame保存最后一帧",
        ),
        parser.add_argument(
            "-l", "--low_quality",
            action="store_true",
            help="Render at a low quality (for faster rendering)低质量渲染",
        ),
        parser.add_argument(
            "-m", "--medium_quality",
            action="store_true",
            help="Render at a medium quality中等质量渲染",
        ),
        parser.add_argument(
            "--high_quality",
            action="store_true",
            help="Render at a high quality高品质渲染高质量渲染",
        ),
        parser.add_argument(
            "-g", "--save_pngs",
            action="store_true",
            help="Save each frame as a png每帧保存图片Png",
        ),
        parser.add_argument(
            "-i", "--save_as_gif",
            action="store_true",
            help="Save the video as gif视频保存gif",
        ),
        parser.add_argument(
            "-f", "--show_file_in_finder",
            action="store_true",
            help="在finder中显示输出文件Show the output file in finder",
        ),
        parser.add_argument(
            "-t", "--transparent",
            action="store_true",
            help="Render to a movie file with an alpha channel使用Alpha通道渲染到电影文件",
        ),
        parser.add_argument(
            "-q", "--quiet",
            action="store_true",
            help="",
        ),
        parser.add_argument(
            "-a", "--write_all",
            action="store_true",
            help="Write all the scenes from a file写文件中所有视频",
        ),
        parser.add_argument(
            "-o", "--file_name",
            help="Specify the name of the output file, if"
                 "it should be different from the scene class name输出文件命名",
        )
        parser.add_argument(
            "-n", "--start_at_animation_number",
            help="Start rendering not from the first animation, but"
                 "from another, specified by its index.  If you pass"
                 "in two comma separated values, e.g. \"3,6\", it will end"
                 "the rendering at the second value从第三帧到第六帧",
        )
        parser.add_argument(
            "-r", "--resolution",
            help="Resolution, passed as \"height,width\"分辨率",
        )
        parser.add_argument(
            "-c", "--color",
            help="Background color背景色,eg:#ffffff",
        )
        parser.add_argument(
            "--sound",
            action="store_true",
            help="Play a success/failure sound",
        )
        parser.add_argument(
            "--leave_progress_bars",
            action="store_true",
            help="Leave progress bars displayed in terminal保持进度条显示在终端中",
        )
        parser.add_argument(
            "--media_dir",
            help="directory to write media多媒体目录",
        )
        video_group = parser.add_mutually_exclusive_group()
        video_group.add_argument(
            "--video_dir",
            help="directory to write file tree for video",
        )
        video_group.add_argument(
            "--video_output_dir",
            help="directory to write video写视频目录",
        )
        parser.add_argument(
            "--tex_dir",
            help="directory to write tex写latex文件目录",
        )

        # For live streaming
        module_location.add_argument(
            "--livestream",
            action="store_true",
            help="Run in streaming mode",
        )
        parser.add_argument(
            "--to-twitch",
            action="store_true",
            help="Stream to twitch",
        )
        parser.add_argument(
            "--with-key",
            dest="twitch_key",
            help="Stream key for twitch",
        )
        args = parser.parse_args()

        if args.file is None and not args.livestream:
            parser.print_help()
            sys.exit(2)
        if args.to_twitch and not args.livestream:
            print("You must run in streaming mode in order to stream to twitch")
            sys.exit(2)
        if args.to_twitch and args.twitch_key is None:
            print("Specify the twitch stream key with --with-key用--with-key指定切换视频流制作键")
            sys.exit(2)
        return args
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)



```
渲染命令选项

```python 
# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
# python -m 打开manim.py入口文件里面的AquareToCircle类
# Use the flat -l for a faster rendering at a lower低质量快速渲染看
# quality.
# Use -s to skip to the end and just save the final frame调到保存最后一帧
# Use the -p to have the animation (or image, if -s was used) pop up once done.完成后，使用-p自动弹出动画（或图像，如果使用-s的话）。
# Use -n <number> to skip ahead to the n'th animation of a scene.跳到第n帧动画场景
# Use -r <number> to specify a resolution (for example, -r 1080 for a 1920x1080分辨率 video)

```




## 3.1. Installation

Manim runs on python 3.7. You can install it from PyPI via pip

```sh
pip3 install manimlib
```

System requirements are [cairo](https://www.cairographics.org), [ffmpeg](https://www.ffmpeg.org), [sox](http://sox.sourceforge.net), [latex](https://www.latex-project.org) (optional, if you want to use LaTeX).

You can now use it via the `manim` command. For example:

```sh
manim my_project.py MyScene
```

For more options, take a look at the “Using manim“ sections further below.

### 3.1.1. Directly

If you want to hack on manimlib itself, clone this repository and in that directory execute:

```sh
# Install python requirements
python3 -m pip install -r requirements.txt

# Try it out
python3 ./manim.py example_scenes.py SquareToCircle -pl
```

### 3.1.2. Directly (Windows)

1. [Install FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows).

2. Install Cairo. Download the wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo. For most users, ``pycairo‑1.18.0‑cp37‑cp37m‑win32.whl`` will do fine.

   ```sh
   pip3 install C:\path\to\wheel\pycairo‑1.18.0‑cp37‑cp37m‑win32.whl
   ```

3. Install a LaTeX distribution. [MiKTeX](https://miktex.org/download) is recommended.

4. [Install SoX](https://sourceforge.net/projects/sox/files/sox/).

5. Install the remaining Python packages. Make sure that ``pycairo==1.17.1`` is changed to ``pycairo==1.18.0`` in requirements.txt.

   ```sh
   git clone https://github.com/3b1b/manim.git
   cd manim
   pip3 install -r requirements.txt
   python3 manim.py example_scenes.py SquareToCircle -pl
   ```

## 3.2. Anaconda Install

- Install sox and latex as above. 
- Create a conda environment using `conda env create -f environment.yml`
- **WINDOWS ONLY** Install `pyreadline` via `pip install pyreadline`. 

### 3.2.1. Using `virtualenv` and `virtualenvwrapper`

After installing `virtualenv` and `virtualenvwrapper`

```sh
git clone https://github.com/3b1b/manim.git
mkvirtualenv -a manim -r requirements.txt manim
python3 -m manim example_scenes.py SquareToCircle -pl
```

### 3.2.2. Using Docker

Since it's a bit tricky to get all the dependencies set up just right, there is a Dockerfile and Compose file provided in this repo as well as [a premade image on Docker Hub](https://hub.docker.com/r/eulertour/manim/tags/). The Dockerfile contains instructions on how to build a manim image, while the Compose file contains instructions on how to run the image.

The prebuilt container image has manim repository included.
`INPUT_PATH` is where the container looks for scene files. You must set the `INPUT_PATH`
environment variable to the absolute path containing your scene file and the
`OUTPUT_PATH` environment variable to the directory where you want media to be written.

1. [Install Docker](https://docs.docker.com)
2. [Install Docker Compose](https://docs.docker.com/compose/install/)
3. Render an animation

```sh
INPUT_PATH=/path/to/dir/containing/source/code \
OUTPUT_PATH=/path/to/output/ \
docker-compose run manim example_scenes.py SquareToCircle -l
```

The command needs to be run as root if your username is not in the docker group.

You can replace `example.scenes.py` with any relative path from your `INPUT_PATH`.

<img src=./manim_docker_diagram.png/>

After running the output will say files ready at `/tmp/output/`, which refers to path inside the container. Your OUTPUT_PATH is bind mounted to this `/tmp/output` so any changes made by the container to `/tmp/output` will be mirrored on your OUTPUT_PATH. `/media/` will be created in `OUTPUT_PATH`.

`-p` won't work as manim would look for video player in the container system, which it does not have.

The first time you execute the above command, Docker will pull the image from Docker Hub and cache it. Any subsequent runs until the image is evicted will use the cached image.
Note that the image doesn't have any development tools installed and can't preview animations. Its purpose is building and testing only.

## 3.3. Using manim

Try running the following:

```sh
python3 -m manim example_scenes.py SquareToCircle -pl
```

The `-p` flag in the command above is for previewing, meaning the video file will automatically open when it is done rendering. The `-l` flag is for a faster rendering at a lower quality.

Some other useful flags include:

- `-s` to skip to the end and just show the final frame.
- `-n <number>` to skip ahead to the `n`'th animation of a scene.
- `-f` to show the file in finder (for OSX).

Set `MEDIA_DIR` environment variable to specify where the image and animation files will be written.

Look through the `old_projects` folder to see the code for previous 3b1b videos.  Note, however, that developments are often made to the library without considering backwards compatibility with those old projects.  To run an old project with a guarantee that it will work, you will have to go back to the commit which completed that project.

While developing a scene, the `-sp` flags are helpful to just see what things look like at the end without having to generate the full animation.  It can also be helpful to use the `-n` flag to skip over some number of animations.

### 3.3.1. Documentation

Documentation is in progress at [eulertour.com/learn/manim](https://www.eulertour.com/learn/manim/).

### 3.3.2. Walkthrough

Todd Zimmerman put together a [tutorial](https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/) on getting started with manim, which has been updated to run on python 3.7.

### 3.3.3. Live Streaming

To live stream your animations, simply run manim with the `--livestream` option.

```sh
> python -m manim --livestream
Writing to media/videos/scene/scene/1080p30/LiveStreamTemp.mp4

Manim is now running in streaming mode. Stream animations by passing
them to manim.play(), e.g.
>>> c = Circle()
>>> manim.play(ShowCreation(c))

>>>
```

It is also possible to stream directly to Twitch. To do that simply pass
--livestream and --to-twitch to manim and specify the stream key with
--with-key. Then when you follow the above example the stream will directly
start on your Twitch channel (with no audio support).

## 3.4. Contributing

Is always welcome. In particular, there is a dire need for tests and documentation.

## 3.5. License

All files in the directories active_projects and old_projects, which by and large generate the visuals for 3b1b videos, are copyright 3Blue1Brown.

The general purpose animation code found in the remainder of the repository, on the other hand, is under the MIT license.











# 4. Manim[Constants](https://www.eulertour.com/learn/manim/constants.html#manim-constants "固定到该标题")

该`constants.py`下`manimlib/`包含了设置和运行manim过程中使用的变量。此处未记录某些变量，因为它们仅由manim内部使用。

## 4.1. [Index](https://www.eulertour.com/learn/manim/constants.html#directories "固定到该标题")

> MEDIA_DIR
> 
> 如果未通过标志指定创建目录`VIDEO_DIR`和`TEX_DIR`创建目录。
> 
> VIDEO_DIR
> 
> 用于存储Manim渲染的场景。场景渲染完成后，它将存储在下`VIDEO_DIR/module_name/scene_name/quality/scene_name.mp4`。`MEDIA_DIR`默认情况下创建。
> 
> TEX_DIR
> 
> Latex编写的文件存储在这里。它还充当缓存，这样就不必在每次需要Latex时都重写文件。

如果这些目录不存在，则创建它们。

## 4.2. [latex](https://www.eulertour.com/learn/manim/constants.html#tex "固定到该标题")

> TEX\_USE\_CTEX
> 
> 布尔值。如果需要使用中文排版，请将其更改为True。
> 
> TEX\_TEXT\_TO_REPLACE
> 
> manim在生成tex文件时使用的占位符文本
> 
> TEMPLATE\_TEX\_FILE
> 
> 默认情况下`manimlib/tex_template.tex`使用。如果`TEX_USE_CTEX`设置为True，则`manimlib/ctex_template.tex`使用。

## 4.3. [数字常量](https://www.eulertour.com/learn/manim/constants.html#numerical-constants "固定到该标题")

> PI
> 
> 别名 `numpy.pi`
> 
> AU
> 
> PI * 2
> 
> DEGREES
> 
> TAU / 360

## 4.4. [相机配置](https://www.eulertour.com/learn/manim/constants.html#camera-configuration "固定到该标题")

渲染设置预设

> PRODUCTION\_QUALITY\_CAMERA_CONFIG
> 
> 2560x1440 @ 60fps＃渲染场景时的默认设置
> 
> HIGH\_QUALITY\_CAMERA_CONFIG
> 
> 1920x1080 @ 60帧/秒 ＃在传递`-h`or `--high_quality`标志时使用。
> 
> MEDIUM\_QUALITY\_CAMERA_CONFIG
> 
> 1280x720 @ 30fps。＃在 传递`-m`or `--medium_quality`标志时使用。
> 
> LOW\_QUALITY\_CAMERA_CONFIG
> 
> 854x480 @ 15fps。＃在传递`-l`or `--low_quality`标志时使用。

## 4.5. [坐标](https://www.eulertour.com/learn/manim/constants.html#coordinates "固定到该标题")

用于2d / 3d动画和放置：

```python
ORIGIN
UP
DOWN
RIGHT
LEFT
IN # 3d camera only, away from camera
OUT # 3d camera only, close to camera

UL = UP + LEFT # diagonal abbreviations. You can use either one
UR = UP + RIGHT
DL = DOWN + LEFT
DR = DOWN + RIGHT

TOP
BOTTOM
LEFT_SIDE
RIGHT_SIDE
```

## 4.6. [颜色](https://www.eulertour.com/learn/manim/constants.html#colors "固定到该标题")

> COLOR_MAP
> 
> 预定义的颜色图
> 
> 调色板
> 
> 从COLOR_MAP派生的彩色十六进制字符串列表


















# 5. 3D
manim-3D场景

https://blog.csdn.net/wsx_9999/article/details/102643242

---------------------------放这里是因为我的Vnote备忘修改添加方便做笔记

————————————————
版权声明：本文为CSDN博主「wsx_9999」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wsx_9999/article/details/102643242


设置角度



```python
class CameraPosition4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=20*DEGREES,gamma=30*DEGREES,distance=6)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()


```



其中phi表示摄像头从z轴顶部向下旋转的角度，theta表示摄像头绕z轴逆时针旋转的角度（假设坐标轴是静止不动的）,整体上来说，phi和theta可以将摄像机移动到球坐标系的某一个特定点上。gamma表示摄像头绕自身的视线轴顺时针旋转的角度（由于运动的相对性，此时图像表现为逆时针旋转）。

ShowCreat和设置摄像头角度时的默认角度
在这里要特别注意的是，在默认创建3D坐标时，Y轴方向向上，X轴方向向右，Z轴方向与纸面垂直向外（指向摄像机方向）。当定义摄像位置时，Y轴的0位置是向右，X轴的0位置是向下。例如：当我们延时移动摄像头的操作时，将所有参数设为0：




```python

class MoveCamera1(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=0*DEGREES,theta=0*DEGREES,gamma=0*DEGREES,run_time=3)
        self.wait()

```



该坐标系依旧发生90°的转动。

接下来，我们尝试将摄像头设置成默认的方向。这样坐标就不会发生移动。


  

```python

class MoveCamera1(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=0*DEGREES,theta=0*DEGREES,gamma=90*DEGREES,run_time=1)
        self.wait()


  

```
另外，我也不知道为什么一定要加上def get_axis()代码才能运行。

```python

class MoveCamera1(ThreeDScene):
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=80*DEGREES,theta=20*DEGREES,gamma=20*DEGREES,run_time=1)
        self.wait()

```


```python

class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Stop move camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Return the position of the camera
        self.wait()

```
3D场景中划线




```python
class ParametricCurve1(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()


```


```python

# Add this in the object: .set_shade_in_3d(True)

class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

```




## 5.1. 3D场景中画面

### 5.1.1. 球面


```python 
    #----- Surfaces
class SurfacesAnimation(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait(5)
        



```

球的参数方程

$$ x=sin(α)∗cos(β) x=\sin(\alpha)*\cos(\beta)x=sin(α)∗cos(β)$$

$$ y=cos(α)∗sin(beta) y=\cos(\alpha)*\sin(beta)y=cos(α)∗sin(beta)$$

$$ z=sin(α) z=\sin(\alpha)z=sin(α)$$

resolution(15,32) 设置表面被分隔成15*32小块。其中水平切成15份，竖直切成32份

圆柱面


```python

        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces     




```

fade(0.5) 设置透明度为0.5
圆柱的参数方程：
$x=cos(α) x=\cos(\alpha)x=cos(α)$
$y=sin(α) y=\sin(\alpha)y=sin(α)$


$z=(1−u) z=(1-u)z=(1−u)$
在manim的lambda中，u，v的取值范围默认为0~1


### 5.1.2. 3\. 抛物面

```python

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

     
```

抛物面的参数方程：

$x=cos(α)∗u x=\cos(\alpha)*ux=cos(α)∗u$
$y=sin(α)∗u y=\sin(\alpha)*uy=sin(α)∗u$
$z=u2 z=u^2z=u^2$

### 5.1.3. 4\. 马鞍面




```python

        
        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)


```

马鞍面的参数方程：
$x=u x=ux=u$
$y=v y=vy=v$
$z=u2−z2 z=u^2-z^2z=u^2-z^2$



### 5.1.4. 5\. 圆锥面

```python
        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

```
圆锥面的参数方程：
$x=u∗cos(α) x=u*\cos(\alpha)x=u∗cos(α)$
$y=u∗sin(α) y=u*\sin(\alpha)y=u∗sin(α)$
$z=u z=uz=u$

### 5.1.5. 6\. 双曲面




```python
		hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

```

双曲面的参数方程：
$x=cosh(α)∗cos(β) x=\cosh(\alpha)*\cos(\beta)x=cosh(α)∗cos(β)$
$y=cosh(α)∗sin(β) y=\cosh(\alpha)*\sin(\beta)y=cosh(α)∗sin(β)$
$z=sinh(α) z=\sinh(\alpha)z=sinh(α)$

7. 椭圆面

```python
		ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

```

椭圆面的参数方程：
$x=cos(α)∗cos(β) x=\cos(\alpha)*\cos(\beta)x=cos(α)∗cos(β)$
$y=cos(α)∗sin(β) y=\cos(\alpha)*\sin(\beta)y=cos(α)∗sin(β)$
$z=sin(α) z=\sin(\alpha)z=sin(α)$

面的转化

```python
class SurfacesAnimation(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    def construct(self):
        axes = ThreeDAxes()
        
        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait(1)
        

```

ReplacementTransform(a,b) 函数，将a图像替换成b图像。
注意它与Transform(a,b)和TransformFromCopy(a,b)的区别。


————————————————
版权声明：本文为CSDN博主「wsx_9999」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wsx_9999/article/details/102643242






# 6. manim-arrange_submobjects的应用及LaggedStart的应用




————————————————
版权声明：本文为CSDN博主「wsx_9999」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wsx_9999/article/details/102673351


这是example_scenes.py中的代码

```python
class example(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()
        self.play(
            FadeOutAndShift(title,UP),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()
```

重点关注VGroup的arrange_submobjects的应用：

```
  VGroup(title, basel).arrange_submobjects(DOWN)
```

以及LaggedStart的应用：

```
LaggedStart(FadeOutAndShiftDown, basel),
```

让我困惑的是，LaggedStart只能对FadeOutAndShiftDown起作用：

```
self.play(LaggedStart(FadeOutAndShift(title,UP))
```

对于FadeOutAndShift()会报错。
因此为了将LaggedStart()应用于FadeOutAndShift(title,UP)，我们可以仿造FadeOutAndShiftDown()，建立FadeOutAndShiftUp()。
打开manimlib\animation\creation.py
```

class FadeOutAndShift(FadeOut):
    CONFIG = {
        "direction": DOWN,
    }

    def __init__(self, mobject, direction=None, **kwargs):
        FadeOut.__init__(self, mobject, **kwargs)
        if direction is None:
            direction = self.direction
        self.target_mobject.shift(direction)


class FadeOutAndShiftDown(FadeOutAndShift):
    CONFIG = {
        "direction": DOWN,
    }
class FadeOutAndShiftUp(FadeOutAndShift):
    CONFIG = {
        "direction": UP,
    }
class FadeOutAndShiftLeft(FadeOutAndShift):
    CONFIG = {
        "direction": LEFT,
    }
class FadeOutAndShiftRight(FadeOutAndShift):
    CONFIG = {
        "direction": RIGHT,
    }

```
然后利用它们：
```

class example(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()
        self.play(
            LaggedStart(FadeOutAndShiftUp,title),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()




```


闪退效果做出来了。




































































































































































































































































