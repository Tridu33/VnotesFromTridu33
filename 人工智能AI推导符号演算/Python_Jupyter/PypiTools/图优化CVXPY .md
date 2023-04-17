# 1. 图优化CVXPY 









https://www.cvxpy.org/index.html

CVXPY是用于凸优化问题的Python嵌入式建模语言。它使您可以按照数学的自然方式来表达问题，而不是以求解器所要求的限制性标准形式来表达自己的问题。





使用CVXOPT和GLPK支持安装
CVXPY支持CVXOPT求解器。此外，通过CVXOPT，CVXPY支持GLPK求解器。在大多数平台上， CVXOPT捆绑了GLPK。在此类平台上，通过以下方式安装CVXOPT：

```
pip install cvxopt
```
应该足以获得对CVXOPT和GLPK的支持。






# 2. GLPK（GNU线性编程套件）




GLPK（G NU L inear P编程K it）软件包旨在解决大规模线性编程（LP），混合整数编程（MIP）和其他相关问题。它是一组用ANSI C编写并以可调用库的形式组织的例程。

GLPK支持GNU MathProg建模语言，它是AMPL语言的子集。

GLPK软件包包括以下主要组件：

原始和对偶单纯形法
原对偶内点法
切分法
GNU MathProg的翻译器
应用程序接口（API）
独立的LP / MIP求解器


https://www.gnu.org/software/glpk/



























