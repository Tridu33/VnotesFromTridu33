Go 语言基础：包括语言基础、变量、数据类型、控制语句、函数、指针、数组、切片、映射、结构体等等。

Go 语言并发：Go 语言天生支持并发，学习并发编程需要掌握 goroutine 和 channel 的使用，以及常用的并发模型和并发编程的技巧。

Go 语言标准库：Go 语言的标准库非常丰富，学习如何使用标准库可以让你更快速地编写高效的程序。

Go 语言开发工具和环境：学习如何安装和配置 Go 语言的开发环境，以及如何使用 Go 的命令行工具进行编译、运行和调试程序。

Go 语言网络编程：Go 语言天生支持网络编程，学习如何使用 Go 编写网络程序，包括 HTTP、TCP、UDP 等协议的编程。

Go 语言测试和调试：Go 语言内置了测试框架，学习如何编写测试用例以及如何使用调试工具进行调试，可以帮助你更好地开发和维护 Go 语言程序。

----


- 当GO111MODULE的值为off时，go modules experiment feature关闭，go compiler显然会始终使用GOPATH mode，即无论要构建的源码目录是否在GOPATH路径下，go compiler都会在传统的GOPATH和vendor目录(仅支持在gopath目录下的package)下搜索目标程序依赖的go package；

- 当GO111MODULE的值为on时（export GO111MODULE=on），go modules experiment feature始终开启，与off相反，go compiler会始终使用module-aware mode，即无论要构建的源码目录是否在GOPATH路径下，go compiler都不会在传统的GOPATH和vendor目录下搜索目标程序依赖的go package，而是在go mod命令的缓存目录($GOPATH/pkg/mod）下搜索对应版本的依赖package；

- auto 自动模式下，项目在\$GOPATH\/src里会使用\$GOPATH\/src的依赖包，在$GOPATH/src外，就使用go.mod 里 require的包。

    - 如果要构建的源码目录不在以GOPATH/src为根的目录体系下，且包含go.mod文件(两个条件缺一不可)，那么使用module-aware mode；

    - 否则使用传统的GOPATH mode。


```
>go env
```

 GOPATH=C:\Users\tridu33\go 工作目录下
 
bin存放编译后生成的exe文件

pkg存放编译后的包文件

src项目源码


 GOROOT=C:\Program Files\Go安装目录 
GOTOOLDIR=C:\Program Files\Go\pkg\tool\windows_amd64工具的目录

执行go mod init创建go.mod文件； 也可以 `go mod init tridu33.com/learning/go_demos`

执行go mod tidy将自动将代码中的import和go.mod中的依赖进行同步；

```
  go mod init:初始化modules go.mod
  go mod tidy:检查，删除错误或者不使用的modules，下载没download的package,更新依赖文件
  go mod download:下载modules到本地cache
  go mod edit:手动修改依赖文件,编辑go.mod文件，选项有-json、-require和-exclude，可以使用帮助go help mod edit
  go mod graph:以文本模式打印模块需求图,打印依赖图
  go mod vendor: # 执行此命令,会将刚才下载至 GOPATH 下的依赖复制至该项目根目录下的 vendor(自动新建) 文件夹下生成vendor目录
  go mod verify:验证依赖是否正确, 校验依赖
  go mod why：查找依赖
  ​
  go test    执行一下，自动导包
  ​
  go list -m  主模块的打印路径
  go list -m -f={{.Dir}}  print主模块的根目录
  go list -m all  查看当前的依赖和版本信息

```

程序名	程序用途
dlv.exe	go 语言调试工具
gocode.exe	go语言代码检查，自动补全
godef.exe 	go语言代码定义和引用的跳转
golint.exe 	go语言代码规范检查
go-outline.exe 	用于在Go源文件中提取JSON形式声明的简单工具
gopkgs.exe 	快速列出可用包的工具
gorename.exe 	在Go源代码中执行标识符的精确类型安全重命名
goreturns.exe 	类似fmt和import的工具，使用零值填充Go返回语句以匹配func返回类型
go-symbols.exe 	从go源码树中提取JSON形式的包符号的工具
gotour.exe 	go语言指南网页版
guru.exe 	go语言源代码有关工具，如代码高亮等


Go包管理详解 - 刘sir的文章 - 知乎
https://zhuanlan.zhihu.com/p/92992277
文件名与包名没有直接关系，不一定要将文件名与包名定成同一个。
 文件夹名与包名没有直接关系，并非需要一致。
 同一个文件夹下的文件只能有一个包名，否则编译报错。
 
go1.18中go run无法直接识别和下载依赖，必在go mod init后执行go mod tidy才能识别和下载依赖，同时把依赖包信息写到go.mod和go.sun中
# Go


```
go build -o hello2.exe
go install
```


gobuild

```
-o 　　　　　　　　　　　　指定输出的文件名，可以带上路径，例如 go build -o a``/b/c
-i　　　　 　　　　　　　　安装相应的包，编译 + go ``install
-a 　　　　　　　　　　　　更新全部已经是最新的包的，但是对标准包不适用
-n 　　　　　　把需要执行的编译命令打印出来，但是不执行，这样就可以很容易的知道底层是如何运行的
-p n 　　　　　　　　　　　指定可以并行可运行的编译数目，默认是 CPU 数目
-race 　　　　　　　　　　 开启编译的时候自动检测数据竞争的情况，目前只支持 64 位的机器
-``v 　　　　　　　　　　　　 打印出来我们正在编译的包名
-work 　　　　   　　　　  打印出来编译时候的临时文件夹名称，并且如果已经存在的话就不要删除
-x 　　　　　　　　　　　　 打印出来执行的命令，其实就是和 -n 的结果类似，只是这个会执行
-ccflags ``'arg list' 　　 传递参数给 5c, 6c, 8c 调用
-compiler name 　　　　   指定相应的编译器，gccgo 还是 gc
-gccgoflags ``'arg list'   传递参数给 gccgo 编译连接调用
-gcflags ``'arg list' 　　  传递参数给 5g, 6g, 8g 调用
-installsuffix suffix    为了和默认的安装包区别开来，采用这个前缀来重新安装那些依赖的包，-race 的时候默认已经是 -installsuffix race，大家可以通过 -n 命令来验证
-ldflags ``'flag list' 　  传递参数给 5l, 6l, 8l 调用
-tags ``'tag list' 　　　　 设置在编译的时候可以适配的那些 tag，详细的 tag 限制参考里面的 Build Constraints

```


https://www.runoob.com/go/go-tutorial.html

Go 语言被设计成一门应用于搭载 Web 服务器，存储集群或类似用途的巨型中央服务器的系统编程语言。

对于高性能分布式系统领域而言，Go 语言无疑比大多数其它语言有着更高的开发效率。它提供了海量并行的支持，这对于游戏服务端的开发而言是再好不过了。


go get会做两件事：
1. 从远程下载需要用到的包
2. 执行go install

go install 会生成可执行文件直接放到bin目录下，当然这是有前提的
你编译的是可执行文件，如果是一个普通的包，会被编译生成到pkg目录下该文件是.a结尾

go run 

go build


go fmt


go test(xxx_Test.go)

go doc fmt等
godoc fmt PrintLn

 
在go快速发展的过程中，有一些依赖包地址变更了。
以前的做法

修改源码，用新路径替换import的地址
git clone 或 go get 新包后，copy到$GOPATH/src里旧的路径下
无论什么方法，都不便于维护，特别是多人协同开发时。
使用go.mod就简单了，在go.mod文件里用 replace 替换包，例如

```
replace golang.org/x/text => github.com/golang/text latest
```


---


# package
镜像
```
go env -w GOPROXY=https://goproxy.cn,https://mirrors.aliyun.com/goproxy,direct
go env -w GO111MODULE=auto 
```
开启Go mod机制


包

```
go get -u github.com/gin-gonic/gin
go get -u github.com/go-delve/delve/cmd/dlv
go get -u golang.org/x/lint/golint
go get -u golang.org/x/tools/go/buildutil
go get -u golang.org/x/tools/go/buildutil
go get -u github.com/ramya-rao-a/go-outline
go get -u golang.org/x/tools/cmd/gopls
go get github.com/mailgun/godebug


```
























