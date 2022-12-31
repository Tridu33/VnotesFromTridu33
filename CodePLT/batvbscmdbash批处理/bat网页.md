

# bat网页

批处理批量打开网页
https://www.cnblogs.com/ae6623/p/4416488.html


https://ehall.jlu.edu.cn/jlu_portal/login

```


<li>
    <a href="/jlu_portal/guide?id=5D0187EE-18E5-48A4-AAC6-4B280D07440C">
        <dl>
            <dt><img src="https://ehall.jlu.edu.cn/file/4d818bf1-1e87-4595-a9a2-96b881468cec"width="94px" height="94px" alt=""></dt>
            <dd>本科生健康状况申报</dd>
        </dl>
    </a>
</li>


```


跳转

```
jump_open('https://ehall.jlu.edu.cn/infoplus/form/JLDX_BK_XNYQSB/start')

```





js点击事件触发

  https://zhidao.baidu.com/question/433848756.html
用JS来点击按钮需要分复2步，第一步是选中按钮的元素，第二步是使用元素自带的click函数。

例如接下来我将要演示的例子中，仅用

document.getElementById("btn").click()

一行就可以制控制按钮点击。

其中document.getElementById("btn")是根究id获取按钮的元素，click()是使按钮被点击一次。


```
var a=getElementsClass("ca")；
alert(a[i]) 
```
https://zhidao.baidu.com/question/361073485656215612.html
**class**

```
获取class='aaa'的DIV元素来：$('.aaa')

获取父级元素id为aaa的div元素：$("#aaa>div.aaaaaa")

获取父级元素id为bbb自身类为aaaaaa的元素：$("#bbb>.aaaaaa")

jQuery 元素选择器：

jQuery 使用 CSS 选择器来选取 HTML 元素。

$("p") ：选取 <p> 元素。

$("p.intro") ：选取所有 class="intro" 的 <p> 元素。

$("p#demo") ：选取所有 id="demo" 的 <p> 元素
```

下载

https://www.cnblogs.com/hamsterPP/p/6763458.html

 window.open("下载文件的后端接口");

由于ajax函数的返回类型只有xml、text、json、html等类型，没有“流”类型，所以通过ajax去请求该接口是无法下载文件的，所以我们创建一个新的form元素来请求接口。







```
tmp=document.getElementsByClassName("bt_2");
tmp.item("0").onclick();
```

属性方法，实现自定义的onclick()

```
var ob=eval(tmp);
　　var property="";
　　for(var p in ob){
　　 property+=p+"\n";
　　}

alert(property);
```
属性。





跳转

```
<div align="center">
<input type="checkbox" style="FONT-FAMILY：微软雅黑；FONT-SIZE:small " offvalue="false" title class="xdBehavior_Boolean infoplus_control infoplus_checkcontrol validate[funcCall[checkRenderFormFields1]
infoplus_writable infoplus_fieldChange" id="V1_CTRL82" name="fieldCNS">
V<label for="V1_CTRL82" class="infoplus_checkLabel">
<font size="3">本人承诺以上填写内容均真实可靠</font>
</1abe1>
</div>
```




选中

```
cb=document.getElementById('V1_CTRL82');
cb.checked=true;
```


提交
```
<li class="command_button" style="">
    <a class="command_button_content" name="infoplus_action_2025_1" id="infoplus_action_2025_1">
        <nobr>确认填报</nobr>
    </a>
    <span class="alpha40 scroll_tip left" style="display: none;">点此区域按钮提交</span>
</li>
```

不同申请时间会不一样
```
<a class="command_button_content" name="infoplus_action_1611_1" id="infoplus_action_1611_1"><nobr>确认填报</nobr></a>
```
提交
```
tj=document.getElementById('infoplus_action_2025_1');
tj.click();
```

跳转https://ehall.jlu.edu.cn/infoplus/form/9392089/render 确定“好”
```
<div class="dialog display" id="dialog_container_45557" style="display: block; max-width: 620px; margin-left: -310px; margin-top: -71px;">

<div class="dialog_body"><div class="dialog_title clearFix" style="display: none;"><span class="dialog_title_span" style="width: 0px;"></span><a class="dialog_close button" href="#" title="关闭"><i class="i-icon-close2"></i></a><a class="dialog_openNew button" href="#"><i class="i-icon-external-link"></i></a><a class="dialog_minimise button" href="#" title="最小化"><i class="i-icon-minus"></i></a></div><div class="dialog_content" style="max-height: 469px;"><div id="form_do_action_dialog" style="">
    <div id="form_do_action_message_description" style="display:none;"></div>
    <div id="form_do_action_show_remark" class="clearfix"><span class="form_do_action_info ui-icon ui-icon-info"></span><span>如有其它相关说明，请点击</span><a href="#" class="show_comment">备注</a><span>，或直接</span><a class="make_remark" href="#">批注</a><span class="form_do_action_remark_made"></span><span>在填表内容处</span></div>
    <div id="form_do_action_remark_div" style="display: none;">
        <div id="form_do_action_remark_tip" style="margin-bottom:2px">请填写备注信息</div>
        <textarea id="form_do_action_remark" rows="5"></textarea>
    </div>
    <div id="form_do_action_next_steps" style="display: none;">
        <div id="form_do_action_show_next_steps" class="clearfix">
            <span class="form_do_action_info ui-icon ui-icon-info"></span>
            <span class="form_do_action_next_steps">完成本操作后，流程将转到以下步骤</span>
        </div>
        <ul id="form_do_action_user_list"></ul>
    </div>
    <div style="height:10px"><a id="linkPrint" href="#" target="_blank"></a></div>
</div>
</div>
</div>

<div class="dialog_footer">
        <button class="dialog_button default fr" style="">好</button>
        <button class="dialog_button fr">取消</button>
</div>

</div>

```



```

hao=document.getElementsByClassName('dialog_button default fr');
hao.item("0").click();

```


```

guanbi=document.getElementsByClassName('dialog_button default fr');
guanbi.item("0").click();

```

汇总

```
console.log("WelCome,Tridu33");
window.location.href = 'https://ehall.jlu.edu.cn/jlu_portal/guide?id=5D0187EE-18E5-48A4-AAC6-4B280D07440C';
woyaobanli = document.getElementsByClassName("bt_2");
woyaobanli.item("0").onclick();

```

跳转新的console

```
cb = document.getElementById('V1_CTRL82');
cb.checked = true;
tj = document.getElementById('infoplus_action_2025_1');不同申请时间会不一样infoplus_action_1611_1"
tj.click();
hao = document.getElementsByClassName('dialog_button default fr');
hao.item("0").click();
guanbi = document.getElementsByClassName('dialog_button default fr');
guanbi.item("0").click();
```















