# 1. TomCat


[https://blog.csdn.net/menglinjie/article/details/79479282](https://blog.csdn.net/menglinjie/article/details/79479282)



用文本编辑工具打开用于启动Tomcat的批处理文件startup.bat，仔细阅读。在这个文件中，首先判断CATALINA_HOME环境变量是否为空，如果为空，就将当前目录设为CATALINA_HOME的值。接着判断当前目录下是否存在bin\catalina.bat，如果文件不存在，将当前目录的父目录设为CATALINA_HOME的值。根据笔者机器上Tomcat安装目录的层次结构，最后CATALINA_HOME的值被设为Tomcat的安装目录。如果环境变量CATALINA_HOME已经存在，则通过这个环境变量调用bin目录下的“catalina.bat start”命令。通过这段分析，我们了解到两个信息，一是Tomcat启动时，需要查找CATALINA_HOME这个环境变量，如果在Tomcat的bin目录下调用startup.bat，Tomcat会自动并正确设置CATALINA_HOME；二是执行startup.bat命令，实际上执行的是“catalina.bat start”命令。



     

<table border="0" cellpadding="0" cellspacing="0" width="1600" style="border-collapse:
 collapse;width:600pt;mso-yfti-tbllook:1536"><colgroup><col width="256" style="mso-width-source:userset;width:96pt"> <col width="1344" style="mso-width-source:userset;width:504pt"></colgroup><tbody><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">bin</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">所有的可执行命令，启动和关闭服务器的命令就在此文件夹之中</span></p></td></tr><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">conf</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">服务器的配置文件夹，里面保存了各个配置信息</span></p></td></tr><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">lib</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:
  &quot;Times New Roman&quot;;mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;
  color:black;mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;
  mso-style-textfill-type:solid;mso-style-textfill-fill-themecolor:text1;
  mso-style-textfill-fill-color:black;mso-style-textfill-fill-alpha:100.0%">Tomcat</span><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">服务器所需要的各个库文件</span></p></td></tr><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">logs</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">保存服务器的系统日志</span></p></td></tr><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">webapps</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:
  &quot;Times New Roman&quot;;mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;
  color:black;mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;
  mso-style-textfill-type:solid;mso-style-textfill-fill-themecolor:text1;
  mso-style-textfill-fill-color:black;mso-style-textfill-fill-alpha:100.0%">web</span><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">应用程序存放的目录，</span><span style="font-size:16.0pt;font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:
  &quot;Times New Roman&quot;;mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;
  color:black;mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;
  mso-style-textfill-type:solid;mso-style-textfill-fill-themecolor:text1;
  mso-style-textfill-fill-color:black;mso-style-textfill-fill-alpha:100.0%">web</span><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">项目保存到此目录中即可发布</span></p></td></tr><tr height="107" style="mso-height-source:userset;height:40.29pt"><td height="107" class="oa1" width="256" style="height:40.29pt;width:96pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:center;direction:ltr;unicode-bidi:embed;mso-line-break-override:
  none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;
  font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">work</span></p></td><td class="oa2" width="1344" style="width:504pt"><p style="language:zh-CN;margin-top:0pt;margin-bottom:0pt;margin-left:0in;
  text-align:justify;text-justify:inter-ideograph;direction:ltr;unicode-bidi:
  embed;mso-line-break-override:none;word-break:normal;punctuation-wrap:hanging"><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">临时文件夹，生成所有的临时文件（</span><span style="font-size:16.0pt;font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:
  &quot;Times New Roman&quot;;mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;
  color:black;mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;
  mso-style-textfill-type:solid;mso-style-textfill-fill-themecolor:text1;
  mso-style-textfill-fill-color:black;mso-style-textfill-fill-alpha:100.0%">*.java</span><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">、</span><span style="font-size:
  16.0pt;font-family:&quot;Times New Roman&quot;;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:en-US;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">*.class</span><span style="font-size:16.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-fareast-font-family:宋体;mso-bidi-font-family:&quot;Times New Roman&quot;;color:black;
  mso-color-index:1;mso-font-kerning:1.0pt;language:zh-CN;mso-style-textfill-type:
  solid;mso-style-textfill-fill-themecolor:text1;mso-style-textfill-fill-color:
  black;mso-style-textfill-fill-alpha:100.0%">）</span></p></td></tr></tbody></table>
  


-   bin: 启动关闭tomcat的命令路径

该目录下存放的是二进制可执行文件，如果是安装版，那么这个目录下会有两个exe文件：tomcat6.exe、tomcat6w.exe，前者是在控制台下启动Tomcat，后者是弹出UGI窗口启动Tomcat；如果是解压版，那么会有startup.bat和shutdown.bat文件，startup.bat用来启动Tomcat，但需要先配置JAVA_HOME环境变量才能启动，shutdawn.bat用来停止Tomcat；

-   conf: 配置

这是一个非常非常重要的目录，这个目录下有四个最为重要的文件：

**server.xml**：配置整个服务器信息。例如修改端口号，添加虚拟主机等；下面会详细介绍这个文件；

**tomcatusers.xml**：存储tomcat用户的文件，这里保存的是tomcat的用户名及密码，以及用户的角色信息。可以按着该文件中的注释信息添加tomcat用户，然后就可以Tomcat主页中进入Tomcat Manager页面了；


**web.xml**：部署描述符文件，这个文件中注册了很多MIME类型，即文档类型。这些MIME类型是客户端与服务器之间说明文档类型的，如用户请求一个html网页，那么服务器还会告诉客户端浏览器响应的文档是text/html类型的，这就是一个MIME类型。客户端浏览器通过这个MIME类型就知道如何处理它了。当然是在浏览器中显示这个html文件了。但如果服务器响应的是一个exe文件，那么浏览器就不可能显示它，而是应该弹出下载窗口才对。MIME就是用来说明文档的内容是什么类型的！

**context.xml**：对所有应用的统一配置，通常我们不会去配置它。

-   lib: jar文件

Tomcat的类库，里面是一大堆jar文件。如果需要添加Tomcat依赖的jar文件，可以把它放到这个目录中，当然也可以把应用依赖的jar文件放到这个目录中，这个目录中的jar所有项目都可以共享之，但这样你的应用放到其他Tomcat下时就不能再共享这个目录下的Jar包了，所以建议只把Tomcat需要的Jar包放到这个目录下；最重要的是JSP.jar,Servlet.jar



-   logs: 空路径，存放日志文件





     这个目录中都是日志文件，记录了Tomcat启动和关闭的信息，如果启动Tomcat时有错误，那么异常也会记录在日志文件中。


-   temp: 临时文件

     存放Tomcat的临时文件，这个目录下的东西可以在停止Tomcat后删除！


-   webapps：不熟web应用（web应用复制到该路径，自动部署）





      存放web项目的目录，其中每个文件夹都是一个项目；如果这个目录下已经存在了目录，那么都是tomcat自带的。项目。其中ROOT是一个特殊的项目，在地址栏中没有给出项目目录时，对应的就是ROOT项目。http://localhost:8080/examples     ，进入示例项目。其中examples就是项目名，即文件夹的名字。（html,java程序）

-   work: class文件,存放将JSP转换成Servlet文件

运行时生成的文件，最终运行的文件都在这里。通过webapps中的项目生成的！可以把这个目录下的内容删除，再次运行时会生再次生成work目录。当客户端用户访问一个JSP文件时，Tomcat会通过JSP生成Java文件，然后再编译Java文件生成class文件，生成的java和class文件都会存放到这个目录下。









启动tomcat:双击bin目录下startup.bat   
浏览器地址栏输入[http://localhost:8080](http://localhost:8080/)   
进入tomcat页面表示安装成功。

————————————————
版权声明：本文为CSDN博主「温柔狠角色」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_25827845/article/details/53982209








打开conf/server.xml文件，68行，port:8080就是端口号




**注意：端口号修改完需要重启。如果需要运行多个服务，需要复制Service元素，在不同的端口**


#### 1.1.1.1. 配置用户名和密码

打开conf/tomcat-users.xml   
tomcat默认没有配置任何用户   
在其中添加如下内容：

（1）name指主机名，可任意命名；   
（2）appBase指虚拟主机的目录，可以为绝对路径，也可为CATALINA\_HOME（环境变量路经）的相对路经，默认为CATALINA\_HOME/webapps；   
（3）unpackWARs如果此项设置为true,表示把WEB应用的WAR文件先展开为开放目录结构后再运行.如果设为false将直接运行为WAR文件；   
（4）autoDeploy如果此项设为true,表示Tomcat服务处于运行状态时,能够监测appBase下的文件,如果有新有web应用加入进来,会自运发布这个WEB应用；   
（5）path指映像目录，映像到docBase的物理地址，“/test”指定URL入口，“ ”指默认入口为虚拟根目录，即webapps/ROOT；   
（6）docBase指实际项目的物理地址，存在任一磁盘中，可为绝对路径，也可为appBase的相对路径。   
（7）reloadable如果这个属性设为true, Tomcat服务器在运行状态下会监视在WEB-INF/classes和Web-INF/lib目录CLASS文件的改运.如果监视到有class文件被更新,服务器自重新加载Web应用。

最后还要在Connector元素下配置好port属性，即端口号，默认为8080，事先可在命令行中查看端口是否被占用，输入netstat-aon|findstr “8080”命令，如果没有显示则为空闲状态
















































































