[TOC]






【Haskell】Stack用法详细介绍（长期持续更新中！）

https://blog.csdn.net/myRealization/article/details/118967134




# stack Nix



Haskell项目中，经常用到包管理工具，有些用cabal，stack， nix。这里对这三个工具做个简要的说明。

首先要明确的是cabal库，是一个haskell包集合的库，提供了不同的包以及不同的版本。cabal-install和stack均是前端基于cabal库使用的工具。

cabal-install是最早用的工具，用于haskell包的管理。提供了规范文件，来构建包，同时也提供了工具来进行包的下载安装cabal-install。

stack是一个可以替代cabal的工具，提供了更加便利的包管理，对于包的依赖，不同的版本，均提供了很好的支持。同时stack也支持不同的ghc发行版本管理。可以将不同的ghc发行版本来进行本地安装，通过配置文件，来进行选择。

stack通过提供沙盒机制，来进行隔离，从而使得不同版本应用之间不会冲突。

nix其实像stack，都是提供项目代码的包依赖，将这些依赖的包编译并且运行。但是stack要求依赖的包都是Haskell包，而nix是一个更加通用的包管理工具，可以是任何的包。它提供了一个库管理的通用方法，每一个库不同的版本，均有一个唯一的标识，这样可以做了多个包多个版本的管理。nixos就是原生包含了nix管理能力的linux的一个发型版本。



## stack

https://docs.haskellstack.org/en/stable/install_and_upgrade/#china-based-users 
stack配置国内镜像


/home/tridu33/.stack/config.yaml


```
# This file contains default non-project-specific settings for 'stack', used
# in all projects.  For more information about stack's configuration, see
# http://docs.haskellstack.org/en/stable/yaml_configuration/

# The following parameters are used by "stack new" to automatically fill fields
# in the cabal config. We recommend uncommenting them and filling them out if
# you intend to use 'stack new'.
# See https://docs.haskellstack.org/en/stable/yaml_configuration/#templates
templates:
  params:
    author-name: tridu33
    author-email: tridu33@qq.com
#    copyright:
#    github-username:



###ADD THIS IF YOU LIVE IN CHINA 
setup-info-locations: 
- "http://mirrors.tuna.tsinghua.edu.cn/stackage/stack-setup.yaml"
urls:
  latest-snapshot: http://mirrors.tuna.tsinghua.edu.cn/stackage/snapshots.json

package-indices:
  - download-prefix: http://mirrors.tuna.tsinghua.edu.cn/hackage/
    hackage-security:
        keyids:
        - 0a5c7ea47cd1b15f01f5f51a33adda7e655bc0f0b0615baa8e271f4c3351e21d
        - 1ea9ba32c526d1cc91ab5e5bd364ec5e9e8cb67179a471872f6e26f0ae773d42
        - 280b10153a522681163658cb49f632cde3f38d768b736ddbc901d99a1a772833
        - 2a96b1889dc221c17296fcc2bb34b908ca9734376f0f361660200935916ef201
        - 2c6c3627bd6c982990239487f1abd02e08a02e6cf16edb105a8012d444d870c3
        - 51f0161b906011b52c6613376b1ae937670da69322113a246a09f807c62f6921
        - 772e9f4c7db33d251d5c6e357199c819e569d130857dc225549b40845ff0890d
        - aa315286e6ad281ad61182235533c41e806e5a787e0b6d1e7eef3f09d137d2e9
        - fe331502606802feac15e514d9b9ea83fee8b6ffef71335479a2e68d84adc6b0
        key-threshold: 3
        ignore-expiry: no

```





















