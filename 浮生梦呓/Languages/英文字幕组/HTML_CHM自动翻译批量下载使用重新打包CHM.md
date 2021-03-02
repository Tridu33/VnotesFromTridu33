一个chm文件，Trados不能直接翻译chm文件，需要先转成html，网上还有说需要将html转成ttx再用Trados2007的Tageditor来翻译。我觉得Trados2014应该也是可以翻译html的，但是，我自己尝试了一下，直接翻译，导出html之后，发现有些超链和格式出现错误，我在网上也没有找到相关介绍，所以来这里求教各位i大婶，怎么使用Trados翻译html文件，同时保证各种标记、超链和格式正确呢？



PlantSimulation翻译工具只是把CHM解压文件夹，再调用已有的仓库翻译 
https://github.com/ShichaoMa/translate_html
，然后翻译成功！！！！！
、
https://zhuanlan.zhihu.com/p/25818996


https://www.v2ex.com/t/434137
有没有什么工具可以将 html 文件的内容的英文翻译成中文？

C:\Users\shinelon>pip install translate-html
Collecting translate-html
  Using cached https://files.pythonhosted.org/packages/2e/94/e90ec27d4897135728c210ee0195f6f91186624469a9176938607e5ec7fe/translate-html-1.2.4.tar.gz
Collecting toolkity>=1.4.7 (from translate-html)
  Using cached https://files.pythonhosted.org/packages/2d/d9/b15d1218080eb322fe0c3da458540d5871847873b0540c1e02c5808373d3/toolkity-1.8.0.tar.gz
    ERROR: Complete output from command python setup.py egg_info:
    ERROR: Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\shinelon\AppData\Local\Temp\pip-install-fbv0i1zm\toolkity\setup.py", line 34, in <module>
        VERSION = get_version("toolkit")
      File "C:\Users\shinelon\AppData\Local\Temp\pip-install-fbv0i1zm\toolkity\setup.py", line 14, in get_version
        init_py = open(os.path.join(package, '__init__.py')).read()
    UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 415: illegal multibyte sequence
    ----------------------------------------
ERROR: Command "python setup.py egg_info" failed with error code 1 in C:\Users\shinelon\AppData\Local\Temp\pip-install-fbv0i1zm\toolkity\

























































































