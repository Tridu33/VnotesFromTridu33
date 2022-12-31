# 1. F12Debug





https://www.zhihu.com/question/35667558/answer/530643532  前端页面，用 JavaScript 在调试 Bug 时有哪些奇技淫巧？


[Chrome——F12 谷歌开发者工具详解https://www.cnblogs.com/xiaowenshu/p/10450848.html](https://www.cnblogs.com/xiaowenshu/p/10450848.html)

```
Ctrl + Shift +J	直接进入console面板
Console()
Ctrl + L 清除控制台消息
Tab	自动完成通用常缀
向右键 接受建议
Ctrl + U 清除console的提示（便于查看源代码）
向上键/向下键 选中上一行/下一行
Enter 执行代码或命令
Debugger(调试面板)
F8/Ctrl + \ 暂停/继续
F10/Ctrl + ’	单步执行
F11/Ctrl + ;	单步进入
Shift + F11/Ctrl + Shift + ;	单步退出
Ctrl + ./Ctrl +,	上一帧/下一帧
Ctrl + Shift + E	被选中代码在控制台中打印出console信息
Ctrl + Shift + A	添加到debugger的watch里面，可以关注选中内容的变化
Ctrl + B	打断点/取消断点
Text Editor(文本编辑器)
Ctrl + Shift+P 跳转到某个成员
Ctrl + Space 自动完成
Ctrl + G 跳转到某行
Alt + - 跳转到之前的编辑位置
Alt + + 跳转到下一个编辑的位置
Ctrl + / 快捷键注释
Alt + ↑ 调整CSS度量单位,每次增加一个单元
Alt + ↓ 调整CSS度量单位,每次减少一个单元
Alt + PageUp 调整CSS度量单位,每次增加10个单元
Alt + PageDown 调整CSS度量单位,每次减少10个单元
Ctrl + D 选择选中内容的下一个匹配内容
Ctrl + U 软撤销
Ctrl + M 进入匹配的括号
Alt + W 关闭编辑便签
Alt + O 切换相同名字的或者不同后缀的文件
All Panels(所有面板)
Ctrl + [/Ctrl + ]	切换面板（向左/向右）
Ctrl + Shift + [/Ctrl + Shift + ] 返回之前/之后的面板转态
Ctrl + Tilde[~]	显示Console
Esc 小菜单弹出隐藏
Ctrl + Shift + M 进去仿真设备模式（移动平板屏幕）
Ctrl + Shift + D 切换调试 面板在底部还是侧边栏展示
Ctrl + F 搜索内容
Ctrl + Shift + F 在所有代码中搜索（跨域）
Ctrl + Shift + C 选择页面节点并且查看代码
Ctrl + P 快速切换源码文件
Style Pane(风格面板)
Tab/Shift + Tab 下一个/上一个属性
↑ 增加CSS度量单位->1单元
↓ 减少CSS度量单位->1单元
PageUp/Shift + ↑ 增加CSS度量单位->10单元
PageDown/Shift + ↓ 减少CSS度量单位->10单元
Shift + PageUp 增加CSS度量单位->100单元
Shift + PageDown 减少CSS度量单位->100单元
Alt + ↑ 增加CSS度量单位->0.1单元
Alt + ↓ 减少CSS度量单位->0.1单元
Timeline Panel(时间轴面板)
Ctrl + E 开始
Ctrl + S 保存时间轴时间
Ctrl + O 加载时间轴数据
```


# 2. [Chrome使用技巧（几个月的心得）](https://www.cnblogs.com/MuYunyun/p/5678405.html)

**阅读目录(Content)**

-   [如何最简易地用上谷歌搜索？](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label0)
-   [chrome实用插件：](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label1)
-   [Chrome调试工具介绍：](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label2)
-   [快速切换文件](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label3)
-   [在源代码中搜索](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label4)
-   [在源代码中快速跳转到指定的行](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label5)
-   [使用多个插入符进行选择](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label6)
-   [设备模式](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label7)
-   [格式化凌乱的js源码](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label8)
-   [颜色选择器](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label9)
-   [改变颜色格式](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label10)
-   [强制改变元素状态（方便查看不同状态下元素的样式）](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label11)
-   [利用chrome来查看和编辑本地文件](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label12)
-   [选择下一个匹配项](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label13)
-   [可视化的DOM阴影](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label14)
-   [奇淫技](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label15)
-   [Chrome Dev开发者选项](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label16)
-   [总结](https://www.cnblogs.com/MuYunyun/p/5678405.html#_label17)







































































