# emcc



https://www.cnblogs.com/h2zZhou/p/9909768.html



Emscripten 的安装可以根据[官方文档](http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html)。由于依赖较多，安装起来比较麻烦，我发现更方便的方法是[安装 SDK](http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html#updating-the-emscripten-sdk)。

你可以按照下面的[步骤](https://github.com/kripken/emscripten/issues/5443#issuecomment-320981440)操作。

> ```bash
> 
> $ git clone https://github.com/juj/emsdk.git
> $ cd emsdk
> $ ./emsdk install --build=Release sdk-incoming-64bit binaryen-master-64bit
> $ ./emsdk activate --build=Release sdk-incoming-64bit binaryen-master-64bit
> $ source ./emsdk_env.sh
> 
> ```

注意，最后一行非常重要。每次重新登陆或者新建 Shell 窗口，都要执行一次这行命令`source ./emsdk_env.sh`。



























