




Serverless Workflow项目由CNCF（Cloud Native Computing Foundation，云原生计算基金会）托管。它的引擎是用 c# 实现的，思想非常不错，社区有人在用c# 做云原生项目。有关谁参与以及Serverless Workflow扮演角色的详细信息，请阅读Serverless Workflow的建议书：

https://github.com/cncf/toc/blob/master/proposals/serverlessworkflow.md

网站/代码：

http://serverlessworkflow.io/

https://github.com/serverlessworkflow

文档：

https://github.com/serverlessworkflow/specification

https://github.com/serverlessworkflow/specification/wiki




# Serverless Workflow
工作流通常适用于有状态的（stateful），异步 (async)，长时间执行（long running）等特性的业务场景。其中比较典型的场景包括：

视频，音频，图片处理工作流

订单、审批流程

数据处理流水线

自动化运维

机器学习流水线、基因测序工作流

常见的开源工作流服务软件如 Apache Airflow，Activiti，Flowable，Netflix Conductor 等提供了使用代码，DSL 或是 BPMN 这类标准的工作流描述方式，允许开发者自己搭建工作流服务。不同云服务厂商也提供了各自的工作流服务如 AWS Step Functions, AWS Simple Workflow Service，Azure Durable Functions。那么有没有一个云原生的工作流服务呢？




https://serverlessworkflow.io/
https://github.com/serverlessworkflow/specification







CNCF Serverless Workflow 定义了一个供应商中立、开源且完全由社区驱动的生态系统，用于定义和运行面向 Serverless 技术领域的基于 DSL 的工作流。

该项目由以下部分组成：

定义基于 DSL 的工作流的规范
针对不同编程语言的开发者 SDK
支持规范的工作流运行时
开发人员工具支持编写基于 DSL 的工作流




















