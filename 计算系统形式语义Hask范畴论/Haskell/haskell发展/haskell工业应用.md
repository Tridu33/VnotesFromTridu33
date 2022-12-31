# 1. haskell工业应用











程序语言理论学术界的工作在工业界有哪些应用？ - rainoftime的回答 - 知乎
https://www.zhihu.com/question/44446105/answer/97408935



举几个例子：
编译器：Chez Scheme, Glasgow Haskell Compiler(GHC)!
程序分析：Coverity, Grammar Tech(主要产品CodeSonar), Astree
程序生成：Flash Fill(集成在Office 2013)
程序测试: SAGE
程序验证: SLAM
语言设计：Rust的affine type, regine type，Type Script, Python的gradual typing..
定理证明: Coq, Isabelle, ACL2, Z3...
...

程序语言相关的研究很广，都有其理论和实践部分：

偏向System/Arch/Security的：并行、系统安全等，相关会议：ASPLOS、OSDI/SOSP, NDSS/S&P/CCS/USecurity..)
传统Compiler向的：CGO，CC等
有侧重于Software Engineering的：ICSE、FSE、ASE等（PS: Software engineering各种提神醒脑的应用多了去了...
话题比较小的：ISSTA, SAS, PEPM..
有重点关注Verification/Formal method的：CAV, TACAS, VMCAI, FMCAD，更理论的LICS, ICALP..
综合性的: POPL, PLDI, ICFP, ECOOP, OOPSLA..


把分析/验证/生成/安全..“等应用全去掉，限制为狭义的，纯粹的“程序语言理论”，比如语义/类型/xx演算什么的，我可以表示无可奉告。像Game semantic，Homotopy type，都是需要相当的基础的（范畴论，代数拓扑等），不要自己看不懂就想批判一番（现在还做这些理论的已经很少了，少一些xx，多一些尊重。。。














