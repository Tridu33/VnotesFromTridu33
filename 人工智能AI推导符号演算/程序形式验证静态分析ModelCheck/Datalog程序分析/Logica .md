

https://www.w3cschool.cn/logica/

# 1. Logica 




Logica 是一种用于数据操作的开源声明式逻辑编程语言。Logica 是Yedalog（Yedalog）的继承者， Yedalog 是 Google 之前创建的一种语言


Logica如何工作？
Logica 将逻辑程序编译为 SQL 表达式，因此可以在 BigQuery（最新的 SQL 引擎）上执行。

在数据库理论家中，众所周知 Datalog 和 SQL 是等效的。实际上，从 Datalog 到 SQL 的转换通常很简单。但是，有一些细微差别，例如如何处理析取和否定。在 Logica 中，我们尝试做出各种选择，以尽可能简化对结果 SQL 结构的理解，从而使用户能够编写高效执行的程序。

为什么叫Logica？
Logica 代表具有聚合的逻辑（ Logic with ggregation）。

先决条件
要在 BigQuery 上运行 Logica 程序，您将需要一个 Google Cloud Project。拥有项目后，您可以在 CoLab 中运行 Logica 程序，并提供您的项目 ID。

要在本地运行 Logica，您需要 Python3。

要从您需要的命令行启动 Logica 谓词执行，这 bq 是一个 BigQuery 命令行工具。为此，您需要安装 Google Cloud SDK。

```
# Install.
python3 -m pip install logica
# Run:
# To see usage message.
python3 -m logica
# To print SQL for HelloWorld program.
python3 -m logica - print Greet <<<'Greet(greeting: "Hello world!")'
```



