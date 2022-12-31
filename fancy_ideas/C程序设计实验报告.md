# 通讯录管理系统的设计与实现任务书
 **课程设计报告格式：**

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid black .5pt;
 mso-border-themecolor:text1;mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt"><tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes"><td width="141" valign="top" style="width:106.5pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">学院：</span><span lang="EN-US" style="font-size:12.0pt"><o:p></o:p></span></p></td><td width="141" valign="top" style="width:106.5pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-left:none;mso-border-left-alt:solid black .5pt;
  mso-border-left-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">专业：</span><span lang="EN-US" style="font-size:12.0pt"><o:p></o:p></span></p></td><td width="141" valign="top" style="width:106.55pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-left:none;mso-border-left-alt:solid black .5pt;
  mso-border-left-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">学号：</span><span lang="EN-US" style="font-size:12.0pt"><o:p></o:p></span></p></td><td width="141" valign="top" style="width:106.55pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-left:none;mso-border-left-alt:solid black .5pt;
  mso-border-left-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">姓名：</span><span lang="EN-US" style="font-size:12.0pt"><o:p></o:p></span></p></td></tr><tr style="mso-yfti-irow:1"><td width="566" colspan="4" valign="top" style="width:426.1pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-top:none;mso-border-top-alt:solid black .5pt;
  mso-border-top-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">系统设计</span><span lang="EN-US" style="font-size:12.0pt"> ( </span><span style="font-size:12.0pt;font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">模块划分、每个模块功能、对应的函数、输入、输出</span><span lang="EN-US" style="font-size:12.0pt"> )<o:p></o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p></td></tr><tr style="mso-yfti-irow:2"><td width="566" colspan="4" valign="top" style="width:426.1pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-top:none;mso-border-top-alt:solid black .5pt;
  mso-border-top-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">关键代码</span><span lang="EN-US" style="font-size:12.0pt"> ( </span><span style="font-size:12.0pt;font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">要求有必要的注释</span><span lang="EN-US" style="font-size:12.0pt"> )<o:p></o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p></td></tr><tr style="mso-yfti-irow:3"><td width="566" colspan="4" valign="top" style="width:426.1pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-top:none;mso-border-top-alt:solid black .5pt;
  mso-border-top-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">测试结果</span><span lang="EN-US" style="font-size:12.0pt"> ( </span><span style="font-size:12.0pt;font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">除浏览功能外，每个功能至少</span><span lang="EN-US" style="font-size:12.0pt">2</span><span style="font-size:12.0pt;
  font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
  &quot;Times New Roman&quot;">组测试用例</span><span lang="EN-US" style="font-size:12.0pt"> )<o:p></o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p></td></tr><tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes"><td width="566" colspan="4" valign="top" style="width:426.1pt;border:solid black 1.0pt;
  mso-border-themecolor:text1;border-top:none;mso-border-top-alt:solid black .5pt;
  mso-border-top-themecolor:text1;mso-border-alt:solid black .5pt;mso-border-themecolor:
  text1;padding:0cm 5.4pt 0cm 5.4pt"><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span style="font-size:12.0pt;font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">系统特色：（如果没有可不写）</span><span lang="EN-US" style="font-size:12.0pt"><o:p></o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p><p class="MsoNormal" style="margin-top:6.0pt;mso-para-margin-top:.5gd"><span lang="EN-US" style="font-size:12.0pt"><o:p>&nbsp;</o:p></span></p></td></tr></tbody></table>




































