# Latex 书写 IEEE 会议论文





[https://blog.csdn.net/u011414200/article/details/51723535](https://blog.csdn.net/u011414200/article/details/51723535)












### 1.写作之前--选择合适的Class

很多人都忽略了这一点，以为选了会议模板就可以之前用了。其实，选择合适的class是文章正确书写的第一步，class定义了文章字体、板式等内容，举例来说，模板中默认的文章纸张大小是letterpaper，这主要是在美国召开会议所用的模板，欧洲等地会议的要求是就是使用a4paper。如果你在EDAS等会议系统里提交的时候，纸张大小不合格也是不能通过的，请大家也注意下这个小细节吧。

一些主要的设置有（粗体我模板默认）：

> 1.字体大小：9pt, **10pt**, 11pt, 12pt 
> 
> 2.稿件模式：draft, draftcls, draftclsnofoot, **ﬁnal**
> 
> 3.投稿类型：conference, **journal**, technote, peerreview, peerreviewca
> 
> 4.特殊模式：comsoc, compsoc, transmag
> 
> 5.纸张大小：**letterpaper**, a4paper, cspaper
> 
> 6.单双页：**oneside**, twoside
> 
> 7.单双列：**onecolumn**, twocolumn
> 
> 8.其他设置项：romanappendices，captionsoff，nofonttune

### 2.开始写作--套用模板

在模板中\\title{  }填写上题目，如果需要手动换行，在需要断的地方加上双斜杠\\\，在后文其他需要换行的地方，你也可以使用\\\。

\\author{}中填写作者单位，注意排版格式，模板里用的\\and使三个作者及其单位位于三个不同的行。我个人则是居中放置的，在作者后边和单位前边加上上角标进行区别，上角标用\\IEEEauthorrefmark{数字}进行区别，通常我都用2和3号角标进行区别。

摘要写在对应的\\begin{abstract}和\\end{abstract}之前，不再赘述。

关键词（索引词Index terms）：在会议模板中并为给出，查看trans的模板可知，一般审稿时的稿件不需要添加关键词，如果需要的话可以用\\begin{IEEEkeywords}和\\end{IEEEkeywords}来添加。

% Note that keywords are not normally used for peerreview papers.

\\begin{IEEEkeywords}

IEEE, IEEEtran, journal, \\LaTeX, paper, template.

\\end{IEEEkeywords}

  
  
作者：小松书  
链接：https://www.jianshu.com/p/2edb884cfb5d  
来源：简书  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。









































