


https://github.com/hashicorp/hcl

https://github.com/hashicorp
基础结构即代码 (IaC) 使用 DevOps 方法和版本控制以及描述性模型来定义和部署基础结构，例如网络、虚拟机、负载均衡器和连接拓扑。 正如同一源代码始终生成相同的二进制文件一样，IaC 模型在每次部署时都会生成相同的环境。

IaC 是一种重要的 DevOps 做法，也是 持续交付的组成部分。 使用 IaC，DevOps 团队可以使用一组统一的做法和工具协作，快速可靠地大规模交付应用程序及其支持基础结构。



# IaC 自动化配置与编排神器 - Terraform 深度解析



















https://www.infoq.cn/article/0LqVmJ*RfKmIYuX1qeXN

Terraform 是 Hashicorp 公司开源的一种多云资源编排工具。使用者通过一种特定的配置语言（HCL, Hashicorp Configuration Language）来描述基础设施，由 Terraform 工具统一解析，构建资源之间的关系，生成执行计划，并通过调用各家云厂商的具体实现来完成整个基础设施生命周期的管理。



相对于其它的云上资源管理方式，Terraform 的主要特点有：



基于 IaC（基础设施即代码，Infrastructure as Code）的设计，可以将基础设施以一种领域特定语言描述出来，消除了在基础设施自动化时描述语义上的歧义，同时减轻了人为因素造成的不确影响。

Terraform 在执行编排动作前，会生成一份可读性良好的执行计划，关键基础设施的变更可以得到充分审查，保证了基础设施的可靠性。

基于 DAG（有向无环图，Directed Acyclic Graph）描述资源与资源之间的关系，由于 DAG 良好的拓扑性质，当资源属性与资源关系发生改变时，变更动作将被充分并行地执行。