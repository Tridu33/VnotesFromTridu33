
Sub 宏12()
'
' 宏12 宏
'

'
    Range("C279").Select
    ActiveCell.FormulaR1C1 = _
        "=IF(R[-1]C[-1]+R[-2]C-R[-3]C>0,0,R[-3]C-R[-1]C[-1]-R[-2]C)"
    Range("C280").Select
    Range("C286").Select
    Range("C280").Select
    ActiveCell.FormulaR1C1 = "=ROUNDUP(R[-1]C/110,1)*110"
    Range("B281").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[1]"
    Range("C278:C280").Select
    Range("D278").Select
    ActiveCell.FormulaR1C1 = ""
    Range("C279").Select
    Selection.AutoFill Destination:=Range("C279:D279"), Type:=xlFillDefault
    Range("C279:D279").Select
    Range("C280").Select
    Selection.AutoFill Destination:=Range("C280:D280"), Type:=xlFillDefault
    Range("C280:D280").Select
    Range("D278").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C+RC[-1]+R[2]C-R[-2]C"
    Range("D278:D280").Select
    Selection.AutoFill Destination:=Range("D278:H280"), Type:=xlFillDefault
    Range("D278:H280").Select
    ActiveWindow.SmallScroll Down:=0
    Range("F280").Select
    With Selection.Font
        .Color = -16776961
        .TintAndShade = 0
    End With
    Range("B281").Select
    Selection.AutoFill Destination:=Range("B281:H281"), Type:=xlFillDefault
    Range("B281:H281").Select
    Range("H281").Select
    Selection.ClearContents
    Range("F282").Select
End Sub
Sub 宏13()
'
' 宏13 宏
'

'
    ActiveCell.FormulaR1C1 = _
        "=IF(R[-1]C[-1]+R[-2]C-R[-3]C<0,R[-1]C[-1]+R[-2]C-R[-3]C,0)"
    Range("B286").Select
    ActiveCell.FormulaR1C1 = "=RC[-1]+R[2]C+R[-1]C-R[-2]C"
    Range("B288").Select
    ActiveCell.FormulaR1C1 = "=IF(R[-1]C>0,CEILING(R[-1]C/30,1)*30,0)"
    Range("A289").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[1]"
    Range("B286:B288").Select
    Range("C286").Select
    ActiveWindow.SmallScroll Down:=0
    ActiveCell.FormulaR1C1 = ""
    Range("C287").Select
    ActiveCell.FormulaR1C1 = _
        "=IF(R[-3]C-R[-2]C-R[-1]C[-1]>0,R[-3]C-R[-2]C-R[-1]C[-1],0)"
    Range("C288").Select
    ActiveWindow.SmallScroll Down:=-9
    ActiveCell.FormulaR1C1 = "=IF(R[-1]C[-1]>0,CEILING(R[-1]C[-1]/30,1)*30,0)"
    Range("C289").Select
    ActiveWindow.SmallScroll Down:=9
    ActiveCell.FormulaR1C1 = ""
    Range("C288").Select
    ActiveCell.FormulaR1C1 = "=IF(R[-1]C>0,CEILING(R[-1]C/30,1)*30,0)"
    Range("C289").Select
    ActiveCell.FormulaR1C1 = ""
    Range("C286").Select
    ActiveCell.FormulaR1C1 = "=RC[-1]+R[-1]C+R[2]C-R[-2]C"
    Range("C286:C288").Select
    Selection.AutoFill Destination:=Range("C286:H288"), Type:=xlFillDefault
    Range("C286:H288").Select
    ActiveWindow.SmallScroll Down:=-3
    Range("A289").Select
    Selection.AutoFill Destination:=Range("A289:H289"), Type:=xlFillDefault
    Range("A289:H289").Select
    Range("H289").Select
    Selection.ClearContents
    Range("A289:G289").Select
    Range("J288").Select
    Selection.ClearContents
End Sub
Sub 宏21()
'
' 宏21 宏
'

'
    Range("B295").Select
    ActiveCell.FormulaR1C1 = _
        "=IF(R[-1]C[-1]+R[-2]C-R[-3]C<0,R[-1]C[-1]+R[-2]C-R[-3]C,0)"
    Range("B296").Select
    ActiveCell.FormulaR1C1 = "=IF(R[-1]C>0,CEILING(R[-1]C/30,1)*30,0)"
    Range("B294").Select
    ActiveCell.FormulaR1C1 = "=RC[-1]+R[2]C+R[-1]C-R[-2]C"
    Range("A297").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[1]"
    Range("B297").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[1]"
    Range("C294").Select
    ActiveCell.FormulaR1C1 = "=RC[-1]+R[-1]C+R[2]C-R[-2]C"
    Range("C295").Select
    ActiveCell.FormulaR1C1 = _
        "=IF(R[-3]C-R[-2]C-R[-1]C[-1]>0,R[-3]C-R[-2]C-R[-1]C[-1],0)"
    Range("C296").Select
    ActiveCell.FormulaR1C1 = "=IF(R[-1]C>0,CEILING(R[-1]C/100,1)*100,0)"
    Range("C297").Select
    ActiveCell.FormulaR1C1 = "=R[-1]C[1]"
    Range("C294:C296").Select
    Selection.AutoFill Destination:=Range("C294:H296"), Type:=xlFillDefault
    Range("C294:H296").Select
    ActiveWindow.DisplayFormulas = False
    Selection.Font.Italic = False
    ActiveWindow.SmallScroll Down:=-6

End Sub























