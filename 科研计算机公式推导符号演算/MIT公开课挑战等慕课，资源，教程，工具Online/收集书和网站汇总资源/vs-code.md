# vs-code




https://zhuanlan.zhihu.com/p/22880087







**相关文档**

  

-   官方文档（英文版）：[Documentation for Visual Studio Code](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs)
-   中文文档（未完成）：[GitHub - jeasonstudio/CN-VScode-Docs: VScode说明文档翻译](https://link.zhihu.com/?target=https%3A//github.com/jeasonstudio/CN-VScode-Docs)

> 这里提一句，，上面的中文文档是我早期建的一个仓库，希望大家一起来为 VSCode 的中文社区的发展做出贡献，欢迎 fork & star

  

**下载**

  

[Download Visual Studio Code](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/Download)

  

**简介**

  

VSCode是微软推出的一款轻量编辑器，采取了和VS相同的UI界面，搭配合适的插件可以优化前端开发的体验。

布局：左侧是用于展示所要编辑的所有文件和文件夹的文件管理器，依次是`**资源管理器**`，`**搜索`，\`GIT\`，`调试`，`插件`**，右侧是打开文件的编辑区域，最多可同时打开三个编辑区域到侧边。

底栏：依次是**\`Git Branch\`，\`error&warning\`，`编码格式`**等。

**常用插件（待补充）**

  

-   HTML Snippets：增强了zen-coding，增加了H5的自动补全，安装后每次打开自动启用(可能与其他插件冲突)。
-   Angular 1.x Snippets：增加了AngularJs 1在.html和.js中的代码补全，安装后每次打开自动启用。
-   Git Easy：增加了vscode中自带的git操作，安装后按F1调出控制台，输入git easy \[options\]完成git操作，代替git bash。
-   HTML CSS Support: 增加.html中css的代码补全，可以手动增加配置文件来增加外部css中的class补全。详情见插件说明。
-   VScode-icons： 美化VSCode的界面，在文件名前面显示小图标，安装后每次打开自动启用。
-   Git Blame：可以查看当前光标所在位置的Git Log，最近一次提交的人和时间，显示在左下角，安装后每次打开自动启用。
-   HTML CSS Class Completion：扫描项目中的所有css中的class名，在html中自动补全，安装后每次打开自动启用。**注意：如果css过多容易卡死。**
-   Debugger for Chrome：方便js调试的插件，前端项目在Chrome中运行起来之后，可以直接在VSCode中打断点、查看输出、查看控制台，需要配置launch.json,详情见插件说明。
-   background：VSCode美化插件，修改界面背景，详情见插件说明。

  

**常用快捷键（待补充）**

  

**编辑器与窗口管理**

  

同时打开多个窗口（查看多个项目）

  

-   打开一个新窗口： Ctrl+Shift+N
-   关闭窗口： Ctrl+Shift+W

  

同时打开多个编辑器（查看多个文件）

-   新建文件 Ctrl+N
-   历史打开文件之间切换 Ctrl+Tab，Alt+Left，Alt+Right
-   切出一个新的编辑器（最多3个）Ctrl+\\，也可以按住Ctrl鼠标点击Explorer里的文件名
-   左中右3个编辑器的快捷键Ctrl+1 Ctrl+2 Ctrl+3
-   **3个编辑器之间循环切换 Ctrl+`**
-   **编辑器换位置，Ctrl+k然后按Left或Right**

  

**代码编辑**

  

**格式调整**

-   代码行缩进Ctrl+\[， Ctrl+\]
-   **折叠打开代码块 Ctrl+Shift+\[， Ctrl+Shift+\]**
-   Ctrl+C Ctrl+V如果不选中，默认复制或剪切一整行
-   代码格式化：Shift+Alt+F，或Ctrl+Shift+P后输入format code
-   修剪空格Ctrl+Shift+X
-   上下移动一行： Alt+Up 或 Alt+Down
-   **向上向下复制一行： Shift+Alt+Up或Shift+Alt+Down**
-   在当前行下边插入一行Ctrl+Enter
-   在当前行上方插入一行Ctrl+Shift+Enter

  

**光标相关**

-   移动到行首：Home
-   移动到行尾：End
-   移动到文件结尾：Ctrl+End
-   移动到文件开头：Ctrl+Home
-   移动到后半个括号 Ctrl+Shift+\]
-   选中当前行Ctrl+i（双击）
-   选择从光标到行尾Shift+End
-   选择从行首到光标处Shift+Home
-   **删除光标右侧的所有字Ctrl+Delete**
-   Shrink/expand selection： Shift+Alt+Left和Shift+Alt+Right
-   Multi-Cursor：可以连续选择多处，然后一起修改，Alt+Click添加cursor或者Ctrl+Alt+Down 或 Ctrl+Alt+Up
-   同时选中所有匹配的Ctrl+Shift+L
-   Ctrl+D下一个匹配的也被选中(被我自定义成删除当前行了，见下边Ctrl+Shift+K)
-   **回退上一个光标操作Ctrl+U**

  

**重构代码**

-   跳转到定义处：F12
-   定义处缩略图：只看一眼而不跳转过去Alt+F12
-   **列出所有的引用：Shift+F12**
-   同时修改本文件中所有匹配的：Ctrl+F12
-   重命名：比如要修改一个方法名，可以选中后按F2，输入新的名字，回车，会发现所有的文件都修改过了。
-   跳转到下一个Error或Warning：当有多个错误时可以按F8逐个跳转
-   查看diff 在explorer里选择文件右键 Set file to compare，然后需要对比的文件上右键选择Compare with 'file\_name\_you_chose'.

  

**查找替换**

  

-   查找 Ctrl+F
-   查找替换 Ctrl+H
-   整个文件夹中查找 Ctrl+Shift+F

  

**显示相关**

  

-   全屏：F11
-   zoomIn/zoomOut：Ctrl + =/Ctrl + -
-   侧边栏显/隐：Ctrl+B
-   **预览markdown Ctrl+Shift+V**

  

**其他**

  

-   自动保存：File -> AutoSave ，或者Ctrl+Shift+P，输入 auto


















