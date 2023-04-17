# VScode tasks.json和launch.json的设置 
[VScode tasks.json和launch.json的设置https://zhuanlan.zhihu.com/p/92175757](https://zhuanlan.zhihu.com/p/92175757)
Visual Studio Code 配置C/C++运行的Task（任务）文件-01 - 品颜完月的文章 - 知乎
https://zhuanlan.zhihu.com/p/374826543


VSCode环境中的Task构建 - 爱吃的小白的文章 - 知乎
https://zhuanlan.zhihu.com/p/399605960

我的评论；
 比如haskell最简单的stack执行ghci单文件的话，可以这样指定curghci任务stack ghci运行当前打开的文件：
 
 ```json

{
"type": "shell",
"label": "curghci",
"command": "cd ${fileDirname} && stack runghc ${fileDirname}/${fileBasename}",
"args": [],
"problemMatcher": [],
"presentation": {
"echo": true,
"reveal": "always",
"focus": true,
"showReuseMessage": true,
"clear": true
},
"group": {
"kind": "build",
"isDefault": true
}
}
 ```
 

ctrl+shift+p输入`Preferences: Open Keyboard Shortcuts (JSON)` 打开`keybindings.json`可以为特定的`task`指定快捷键：



```json

{
"key": "ctrl+shift+r",
"command": "workbench.action.tasks.runTask",
"args": "run"
}
```



## 预定义变量[#](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/editor/variables-reference%23_predefined-variables)

支持下面的预定义变量:

-   **${workspaceFolder}** \- 当前工作目录(根目录)
-   **${workspaceFolderBasename}** \- 当前文件的父目录
-   **${file}** \- 当前打开的文件名(完整路径)
-   **${relativeFile}** \- 当前根目录到当前打开文件的相对路径(包括文件名)
-   **${relativeFileDirname}** \- 当前根目录到当前打开文件的相对路径(不包括文件名)
-   **${fileBasename}** \- 当前打开的文件名(包括扩展名)
-   **${fileBasenameNoExtension}** \- 当前打开的文件名(不包括扩展名)
-   **${fileDirname}** \- 当前打开文件的目录
-   **${fileExtname}** \- 当前打开文件的扩展名
-   **${cwd}** \- 启动时task工作的目录
-   **${lineNumber}** \- 当前激活文件所选行
-   **${selectedText}** \- 当前激活文件中所选择的文本
-   **${execPath}** \- vscode执行文件所在的目录
-   **${defaultBuildTask}** \- 默认编译任务(build task)的名字

## 预定义变量示例:

假设你满足以下的条件

1.  一个文件 `/home/your-username/your-project/folder/file.ext` 在你的编辑器中打开;
2.  一个目录 `/home/your-username/your-project` 作为你的根目录.

下面的预定义变量则代表:

-   **${workspaceFolder}** - `/home/your-username/your-project`
-   **${workspaceFolderBasename}** - `your-project`
-   **${file}** - `/home/your-username/your-project/folder/file.ext`
-   **${relativeFile}** - `folder/file.ext`
-   **${relativeFileDirname}** - `folder`
-   **${fileBasename}** - `file.ext`
-   **${fileBasenameNoExtension}** - `file`
-   **${fileDirname}** - `/home/your-username/your-project/folder`
-   **${fileExtname}** - `.ext`
-   **${lineNumber}** \- 光标所在行
-   **${selectedText}** \- 编辑器中所选择的文本
-   **${execPath}** \- Code.exe的位置































