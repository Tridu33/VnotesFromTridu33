# 1. localStorage









localStorage.XXX=YYY






**重点来了，localStore在webview怎么用不了！！**   
原因是webView默认没有启动localStore功能的服务，需要我们自己手动去开启服务：








WebSettings settings = webview.getSettings();
settings.setDomStorageEnabled(true);







