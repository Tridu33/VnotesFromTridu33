# ghcjs
cabal install haste-compiler

https://www.haste-lang.org/

GHCJS 有实际的 use case 么？ - 王世友的回答 - 知乎
https://www.zhihu.com/question/47690121/answer/109026976
https://haskell-miso.org/ GHCjs前端框架



Haste 是Haskell函数式编程语言的一种实现，面向 Web 应用程序。Haste 基于事实上的标准 GHC 编译器，这意味着它支持完整的 Haskell 语言，包括 GHC 扩展并生成高度优化的代码，但带有一组扩展的标准库。Haste 支持开箱即用的现代 Web 技术，例如 WebSockets、LocalStorage、Canvas 等。此外，Haste 预装了用于抢占式多任务处理、处理二进制数据和其他细节的工具。

一个 Haste 程序可以编译成单个 JavaScript 文件，就像传统的浏览器端程序一样，或者编译成一个 JavaScript 文件和一个服务器端二进制文件，两者之间进行强类型通信。本质上，Haste 允许您将客户端-服务器 Web 应用程序编写为一个单一的、类型安全的程序，而不是两个单独的程序，它们只是像传统那样通过一些 Web API 相互通信。

您无需扔掉所有旧代码即可开始使用 Haste。除了标准的 Haskell FFI 之外，Haste 还提供了自己的灵活机制来轻松实现 Haskell-JavaScript 集成，使用花哨的类型魔术来允许 Haskell 和 JavaScript 代码以最少的努力使用任何类型的数据。




High level interface for webkit-javascriptcore
jsaddle, 使用GHCJS或者GHC的JavaScript介面
源代码网址: https://github.com/ghcjs/jsaddle

有許多不同的JSaddle runner可以選擇

在warp伺服器上運行 ，並使用連接到它的網路瀏覽器運行 JSaddle。
jsaddle-webkit2gtk - 在WebKitGTK窗口中運行 JSaddle。
JSaddle WKWebView - 在iOS或者 macOS的WKWebView中運行 JSaddle。
JSaddle clib - C 介面，用於使用JNI在Android上運行 JSaddle。
