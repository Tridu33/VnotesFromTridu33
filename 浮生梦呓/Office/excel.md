# excel


这样好些：


```

Sub Macro2()
'
' Macro2 Macro
'

'
    Dim a As Integer
    a = Application.WorksheetFunction.CountA(Range("c2:c60000"))
    Range("E1").Select
    ActiveCell.Formula2R1C1 = _
        "=SUMPRODUCT(1/COUNTIF(R[1]C[-2]:R[60000]C[-2],R[1]C[-2]:R[" + CStr(a) + "]C[-2]))"
    MsgBox ("Done.")
End Sub
```






只要C列数据不超过60000个元素就能用,存到E1


不想可以直接Msgbox (结果)
















