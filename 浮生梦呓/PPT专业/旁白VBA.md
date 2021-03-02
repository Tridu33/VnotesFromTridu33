
# 旁白VBA

Module新建

```
Dim s As Object
Public Sub MyRead()
    Dim ss As String
    Dim tmpShape As Shape, tmpSlide As Slide
    For Each tmpShape In ActivePresentation.SlideShowWindow.View.Slide.Shapes
        If tmpShape.HasTextFrame Then
            With tmpShape.TextFrame
                If .HasText Then ss = ss + .TextRange.Text '可以加这句话+ "English txt,,,...Dot"
            End With
        End If
        'ss=ss+tmpShape.TextFrame.TextRange.Text
    Next tmpShape
    Set s = CreateObject("sapi.spvoice")
    s.Rate = 1
    s.Speak ss, 1
End Sub


```

插入按钮：

```
Private Sub CommandButton1_Click()
Call MyRead
End Sub

```

朗读当前页面的文本框




[官方CreateObject教程https://support.office.com/zh-cn/article/GetObject-%E5%87%BD%E6%95%B0-b24e00a4-5f83-44c9-8cbf-cdc65faa2cf5](https://support.office.com/zh-cn/article/GetObject-%E5%87%BD%E6%95%B0-b24e00a4-5f83-44c9-8cbf-cdc65faa2cf5)



自动朗读文本 VBA: [https://wenku.baidu.com/view/3a9d62100242a8956aece49f.html](https://wenku.baidu.com/view/3a9d62100242a8956aece49f.html)











































































