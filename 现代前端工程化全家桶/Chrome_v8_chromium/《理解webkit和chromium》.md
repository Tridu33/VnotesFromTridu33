




# 《理解webkit和chromium》

https://blog.csdn.net/realDonaldTrump/article/details/80796780
这是一本博客衍生的书

当前市场上只有 3 个主要的浏览器引擎：
- Mozilla 的 Gecko、
- Google 的 Blink、
- 苹果的 WebKit（Blink 的近亲）。

Blink 从 WebKit 直接复制出一
个版本出来，然后将与 chromium 无关的 Ports 全部移除掉，将代码结构重新整理，就目前而言，Blink 的渲染和
WebKit 是一样，但是，以后两者将各自走不同的路。（WebKit当年也是以这样的方式来从KHTML中复制出来的。）
因此，在未来是Blink作为主力而不再是WebKit
http://www.chromium.org/blink

世界上第一款 JavaScript 引擎是伴随第一个能运行 JavaScript 程序的浏览器出现的，也就是 Netscape Navigator。
SpiderMonkey——第一个 JavaScript 引擎，该引擎过去驱动 Netscape Navigator，如今驱动 Firefox 浏览器。


WebKit位于Chromium目录下的src/third_party/WebKit

chrome://chrome-urls/

tauri使用的渲染库wry在macos下采用Webkit.framework，在windows下采用了webview2


js引擎 ： nodejs-v8 rust的deno
JavaScriptCore——开源，苹果公司为 Safair 浏览器开发的














