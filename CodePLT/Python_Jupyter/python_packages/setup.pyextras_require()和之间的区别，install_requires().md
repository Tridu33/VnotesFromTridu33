# 1. setup.pyextras_require()和之间的区别，install_requires()











https://stackoverflow.com/questions/41268863/difference-between-extras-require-and-install-requires-in-setup-py







如果需要依赖项来运行您的项目，请将其放在中install_requires。它们将始终被安装。

如果您的项目具有添加依赖项的可选功能，请将这些依赖项放入中extras_require。除非用户或其他软件包要求该功能，否则将不会安装这些依赖项。














