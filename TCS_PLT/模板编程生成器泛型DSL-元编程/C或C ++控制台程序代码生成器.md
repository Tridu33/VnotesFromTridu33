# C或C ++控制台程序代码生成器






codeproject.com/Articles/669611/C-or-Cplusplus-Console-Program-Code-Generator









该程序生成C或C ++程序，这些程序可以解析命令行参数并显示已解析的值。该程序的目的是保存类型并允许快速创建可以针对某些预期目的进行修改的程序。

该程序旨在节省编写C或C ++控制台程序时的键入。当程序生成运行代码时，预期用户将希望修改生成的代码。

将使用与在命令行上传递的程序名称的基本名称相同的名称创建一个文件夹，并在该文件夹中创建生成的代码。





该程序是使用Python 2.7版编写的，但它也应该在Python 2.6上运行。该程序由以下文件组成：
>make_c_cpp_prog.py	解析输入参数并调用其他python文件以创建生成的文件的主程序文件。
c_cpp_program_creator.py	主代码生成器，该生成器创建C或C ++代码主文件来解析参数并显示它们。
carginfo.py	存储生成的程序参数的类型，名称和默认值信息。
program_properties.py	存储是否生成C或C ++程序以及其他程序属性。
cpp_keyword_checker.py	标识名称是否为C ++关键字。即使正在生成C代码，也禁止使用最新的C ++ 11关键字。
makefile_creator.py	创建一个Linux Makefile。
get_arg_info_creator.py	创建文件get_arg_info.c和get_arg_info.h，用于解析C或C ++参数。
platform_os_creator.py	创建头文件platform_os.h，该文件用于定义平台和操作特定的符号。
vs_build_creator.py	创建Visual Studio构建文件。
example_program.bat	这不是程序的一部分。该Windows TM批处理文件运行该程序以生成示例程序。用户必须在批处理文件名之后提供文件名。
我最近在Windows上使用Visual Studio进行编译。Linux曾经可以使用，虽然我希望没有问题，但对于Linux来说，文件platform_os.h和Makefile可能需要进行一些调整。如果有任何问题，我将更新代码。











