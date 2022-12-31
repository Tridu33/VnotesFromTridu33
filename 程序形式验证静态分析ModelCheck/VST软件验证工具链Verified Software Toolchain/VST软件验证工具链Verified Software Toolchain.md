# VST软件验证工具链Verified Software Toolchain

https://github.com/PrincetonUniversity/VST 普林斯顿


https://vst.cs.princeton.edu/



> 我想知道:
​coq有类似的命令行工具吗？用来管理锁定各依赖工具的版本。
还是说现在coq的ventoring，基本都只能靠直接依赖库的源码到工程目录下?(不是指opam是指更上层的依赖管理命令行工具xxx，opam和工具xxx的关系，感觉类似pip install和conda install)
ruby的bundle有Gemfile.lock，
​python的虚拟环境工具如conda有requirement.txt绑定版本依赖实现和部署安装，
js的​npm有package-lock.json锁版本实现，
java有maven的pom.xml管理不兼容的各个版本依赖包，
cpp全靠源码级别复制和极其难用的scons,conan,make,cmake之类的.so，.a和复直接暴力复制头文件等操作管理各个版本不兼容的依赖库...





群主牛逼：
> .opam文件可以
liyishuai(506162544) 2022/1/24 23:58:25
depends: [
  "coq" {>= "8.11.0"}
  "coq-compcert" {= "3.9"}
]
就限定了coq-compcert必须为3.9
liyishuai(506162544) 2022/1/24 23:58:51
然后`opam install .`
liyishuai(506162544) 2022/1/24 23:59:19
命令行的话用opam pin
vendoring很罕见，我只在VST里见到过 VST堪称依赖管理缝合怪：https://github.com/PrincetonUniversity/VST （普林维护代码库的方式不要学习





