[TOC]






# python打包用户指南
packaging.python.org/glossary/#term-import-package





Binary Distribution

一种特定类型的[内置发行版](https://packaging.python.org/glossary/#term-built-distribution)，包含已编译的扩展。

Built Distribution

一个[分配](https://packaging.python.org/glossary/#term-distribution-package)到包含要安装文件和元数据只需要移动到正确的位置在目标系统上，格式。[Wheel](https://packaging.python.org/glossary/#term-wheel)是这种格式，而distutil的[Source Distribution](https://packaging.python.org/glossary/#term-source-distribution-or-sdist)不是，因为它需要一个构建步骤才能安装。此格式并不意味着必须预编译Python文件（[Wheel](https://packaging.python.org/glossary/#term-wheel)有意不包含已编译的Python文件）。

配送套餐

版本化的存档文件，包含Python [包](https://packaging.python.org/glossary/#term-import-package)，[模块](https://packaging.python.org/glossary/#term-module)和其他用于发布[Release的](https://packaging.python.org/glossary/#term-release)资源文件。最终用户将从互联网下载并安装该存档文件。

分发软件包通常用“ package”或“ distribution”一词来表示，但是当需要更加清楚地避免与[Import Package](https://packaging.python.org/glossary/#term-import-package)（也通常称为“ package”）混淆时，本指南可以使用扩展术语。 ）或其他类型的发行版（例如Linux发行版或Python语言发行版），通常使用单个术语“发行版”来指代。

Egg

一个[内置分布](https://packaging.python.org/glossary/#term-built-distribution)通过引入格式[setuptools的](https://packaging.python.org/key_projects/#setuptools)，这是由更换[轮胎](https://packaging.python.org/glossary/#term-wheel)。有关详细信息，请参见[Python Eggs](https://setuptools.readthedocs.io/en/latest/formats.html)和 [Python Eggs ](http://peak.telecommunity.com/DevCenter/PythonEggs)[的内部结构。](https://setuptools.readthedocs.io/en/latest/formats.html)[](http://peak.telecommunity.com/DevCenter/PythonEggs)

扩展模块

用Python实现的底层语言编写的[模块](https://packaging.python.org/glossary/#term-module)：用于Python的C / C ++，用于Jython的Java。通常包含在单个可动态加载的预编译文件中，例如，Unix上用于Python扩展的共享库（.so）文件，Windows上用于Python扩展的DLL（给定的.pyd扩展）或Jython扩展的Java类文件。

Known Good Set (KGS)已知良好组合（KGS）

相互兼容的指定版本的一组发行版。通常，将运行一个测试套件，该套件通过所有测试，然后再将一组特定的软件包声明为已知的良好套件。该术语通常由包含多个独立发行版的框架和工具包使用。

## Import Package

一个Python模块，可以包含其他模块或递归地包含其他软件包。

导入包通常用单个词“包”来指代，但是当需要更清楚地避免与[分发包](https://packaging.python.org/glossary/#term-distribution-package)（通常也称为“包”）混淆时，本指南将使用扩展术语。

模组

Python中代码可重用性的基本单位，存在以下两种类型之一：[Pure Module](https://packaging.python.org/glossary/#term-pure-module)或[Extension Module](https://packaging.python.org/glossary/#term-extension-module)。

包装指数

具有Web界面的发行版存储库，可自动执行 [软件包](https://packaging.python.org/glossary/#term-distribution-package)发现和使用。

每个项目索引

私有或其他非规范[包索引，](https://packaging.python.org/glossary/#term-package-index)由特定[项目](https://packaging.python.org/glossary/#term-project)表示为解决该项目依赖项的首选索引或必需索引。

项目

库，框架，脚本，插件，应用程序或数据或其他资源的集合，或它们的某种组合，旨在打包到[发行版中](https://packaging.python.org/glossary/#term-distribution-package)。

由于大多数项目都 使用以下任一方法创建[发行版](https://packaging.python.org/glossary/#term-distribution-package)[**PEP 518**](https://www.python.org/dev/peps/pep-0518) `build-system`，[ distutils](https://packaging.python.org/key_projects/#distutils)或 [setuptools](https://packaging.python.org/key_projects/#setuptools)是当前定义项目的另一种实用方法，它是在项目源目录的根目录中包含[ pyproject.toml](https://packaging.python.org/glossary/#term-pyproject-toml)，[ setup.py](https://packaging.python.org/glossary/#term-setup-py)或[ setup.cfg](https://packaging.python.org/glossary/#term-setup-cfg)文件的工具。

Python项目必须具有唯一的名称，该名称已在[PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi)上注册 。每个项目将包含一个或多个[发行版](https://packaging.python.org/glossary/#term-release)，每个发行版可包含一个或多个[发行版](https://packaging.python.org/glossary/#term-distribution-package)。

请注意，有一个严格的约定将项目命名为导入要运行该项目的软件包的名称。但是，这不必成立。可以从项目“ foo”安装发行版，并提供仅可作为“ bar”导入的软件包。

纯模块Pure Module

甲[模块](https://packaging.python.org/glossary/#term-module)写入Python和包含在单个的.py文件（以及可能的相关联的pyc文件和/或.pyo文件）。

Python打包机构（PyPA）

PyPA是一个工作组，负责维护Python打包中的许多相关项目。他们在[https://www.pypa.io上](https://www.pypa.io/)维护一个站点， 在[GitHub](https://github.com/pypa)和[Bitbucket](https://bitbucket.org/pypa)上[托管](https://github.com/pypa)项目，并在[distutils-sig邮件列表](https://mail.python.org/mailman3/lists/distutils-sig.python.org/) 和[Python Discourse论坛](https://discuss.python.org/c/packaging)上讨论问题 。

Python封装索引（PyPI）

[PyPI](https://pypi.org/)是Python社区的默认[Package Index](https://packaging.python.org/glossary/#term-package-index)。它对所有Python开发人员开放以使用和分发其发行版。

pypi.org

[pypi.org](https://pypi.org/)是[Python软件包索引（PyPI）](https://packaging.python.org/glossary/#term-python-package-index-pypi)的域名 。它在2017 年取代了旧索引索引域名pypi.python.org。由[Warehouse](https://packaging.python.org/key_projects/#warehouse)提供支持 。

pyproject.toml

与工具无关的[项目](https://packaging.python.org/glossary/#term-project)规范文件。定义于[**PEP 518**](https://www.python.org/dev/peps/pep-0518)。

释放

[项目](https://packaging.python.org/glossary/#term-project)在特定时间点的快照，由版本标识符表示。

发布可能需要发布多个 [发行版](https://packaging.python.org/glossary/#term-distribution-package)。例如，如果发布了项目的1.0版，则可能以源分发格式和Windows安装程序分发格式提供。

需求

要安装的[软件包](https://packaging.python.org/glossary/#term-distribution-package)的规范。 [PIP](https://packaging.python.org/key_projects/#pip)，所述[PYPA](https://packaging.python.org/glossary/#term-python-packaging-authority-pypa)建议安装程序，允许所有可以被认为是一个“规定”的各种形式规格。有关更多信息，请参见 [pip安装](https://pip.pypa.io/en/latest/reference/pip_install/#pip-install "（在pip v20.3中）")参考。

需求说明

[pip](https://packaging.python.org/key_projects/#pip)用于从[Package Index](https://packaging.python.org/glossary/#term-package-index)安装软件包的格式。有关格式的EBNF图，请参阅[setuptools](https://packaging.python.org/key_projects/#setuptools)文档中的 [pkg_resources.Requirement](https://setuptools.readthedocs.io/en/latest/pkg_resources.html#requirement-objects) 条目。例如，“ foo> = 1.3”是需求说明符，其中“ foo”是项目名称，而“> = 1.3”部分是[版本](https://packaging.python.org/glossary/#term-version-specifier)说明符[](https://packaging.python.org/key_projects/#setuptools)[](https://packaging.python.org/glossary/#term-version-specifier)

需求文件

包含可以使用[pip](https://packaging.python.org/key_projects/#pip)安装的[需求](https://packaging.python.org/glossary/#term-requirement)列表的文件。有关更多信息，请参阅[需求文件](https://pip.pypa.io/en/latest/user_guide/#requirements-files "（在pip v20.3中）") 上的[pip](https://packaging.python.org/key_projects/#pip)文档。[](https://packaging.python.org/key_projects/#pip)[](https://packaging.python.org/key_projects/#pip)[](https://pip.pypa.io/en/latest/user_guide/#requirements-files "（在pip v20.3中）")

**setup.py**

**setup.cfg**

[distutils](https://packaging.python.org/key_projects/#distutils)和[setuptools](https://packaging.python.org/key_projects/#setuptools)的项目规范文件。另请参见[pyproject.toml](https://packaging.python.org/glossary/#term-pyproject-toml)。

源档案

包含用于将原始源代码存档[推出](https://packaging.python.org/glossary/#term-release)创建之前，[源分布](https://packaging.python.org/glossary/#term-source-distribution-or-sdist)或[内置分布](https://packaging.python.org/glossary/#term-built-distribution)。

来源分布（或“ sdist”）

一种[分发](https://packaging.python.org/glossary/#term-distribution-package)格式（通常使用生成），提供诸如[pip之](https://packaging.python.org/key_projects/#pip)类的工具安装或生成[内置分发](https://packaging.python.org/glossary/#term-built-distribution)所需的元数据和基本源文件。`python setup.py sdist`[](https://packaging.python.org/key_projects/#pip)[](https://packaging.python.org/glossary/#term-built-distribution)

系统包装System Package

以操作系统固有格式提供的软件包，例如rpm或dpkg文件。

版本说明符

[需求说明符](https://packaging.python.org/glossary/#term-requirement-specifier)的版本组件。例如，“ foo> = 1.3”的“> = 1.3”部分。 [**PEP 440**](https://www.python.org/dev/peps/pep-0440)包含一个[](https://www.python.org/dev/peps/pep-0440#version-specifiers)Python包装当前支持的说明符的[**完整说明**](https://www.python.org/dev/peps/pep-0440#version-specifiers)。在[ setuptools](https://packaging.python.org/key_projects/#setuptools) v8.0和[ pip](https://packaging.python.org/key_projects/#pip) v6.0中实现了对PEP440的支持。

虚拟环境Virtual Environment

一个隔离的Python环境，允许安装软件包以供特定应用程序使用，而不是在系统范围内安装。有关更多信息，请参见“ [创建虚拟环境](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments) ”部分。

轮Wheel

一个[内置分配](https://packaging.python.org/glossary/#term-built-distribution)形式介绍了[**PEP 427**](https://www.python.org/dev/peps/pep-0427)，旨在替代[ Egg](https://packaging.python.org/glossary/#term-egg)格式。Wheel目前受[ pip](https://packaging.python.org/key_projects/#pip)支持。

Working Set工作集

可供导入的[发行](https://packaging.python.org/glossary/#term-distribution-package)版集合。这些是sys.path 变量上的分布。在工作集中最多[只能](https://packaging.python.org/glossary/#term-distribution-package)有一个项目的[分发](https://packaging.python.org/glossary/#term-distribution-package)。












