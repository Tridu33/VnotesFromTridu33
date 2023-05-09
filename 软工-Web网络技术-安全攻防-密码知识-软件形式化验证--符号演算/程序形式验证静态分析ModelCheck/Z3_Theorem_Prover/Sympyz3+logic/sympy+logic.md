





https://docs.sympy.org/latest/index.html 文档汇总

https://docs.sympy.org/latest/modules/logic.html

# 1. sympy+logic



```python
from sympy import symbols
from sympy.logic.boolalg import to_cnf
from sympy.logic import simplify_logic
```


Boolean Logic – SOP Form, POS Form

https://www.electronicshub.org/boolean-logic-sop-form-pos-form/

There are two types of canonical forms:

- Sum-of-min terms or Canonical SOP
- Product-of- max terms or Canonical POS

Canonical Form (Standard SOP and POS Form)

1. SOP Form, 

乘积和（SOP）形式是一种简化逻辑门的布尔表达式的方法（或形式）。在这种布尔函数表示形式的SOP形式中，变量由AND（乘积）运算以形成乘积项，所有这些乘积项进行“或”运算（求和或加法）以得到最终函数。

乘积和形式可以通过使用布尔加法运算将两个或多个乘积项相加（或求和）来形成。在这里，乘积项是通过使用AND运算定义的，总和项是通过使用OR运算定义的。

乘积和形式也称为**析取范式**，因为乘积项进行“或”运算，而析取运算是逻辑“或”。产品总和表格也称为标准SOP。

SOP表单表示最适合在FPGA（现场可编程门阵列）中使用。



2. POS Form

求和形式的乘积是一种简化逻辑门的布尔表达式的方法（或形式）。在此POS形式中，所有变量都进行“或”运算，即作为总和形式写入总和项。

将所有这些总和项进行“与”运算（相乘），得到和积形式。此表格与SOP表格完全相反。因此，这也可以称为“ SOP表格的对偶”。

在这里，总和项是使用“或”运算定义的，乘积项是使用“与”运算定义的。当两个或多个和项乘以布尔或运算时，结果输出表达式将为和积形式或POS形式。

“和”积形式也称为“**合取范式**”，因为总和项被“与”在一起，并且合取运算是逻辑“与”。“总和”表格也称为“标准POS”。










