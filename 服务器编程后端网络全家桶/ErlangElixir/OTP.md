
不推荐各位工程师在生产环境中使用 Elixir

说白了还是生态问题，当强到足以从头开始，又有时间，就不存在问题


# OTP











OTP 的全称是 Open Telecom Platform，即开放电信平台


Elixir 中的 OTP 其实就是一个包，它包含一系列的行为，包括 GenServer、Application、Supervisor，这里我们从通用服务器 GenServer 出发对 Elixir 面向并发的开发模式和 OTP 本身进行介绍。https://draveness.me/elixir-or-not/








使用场景，也就是服务端集群的一些特点：

- 使用 GraphQL 对外暴露接口；
多种语言 Ruby、Elixir 和 Go 进行开发；
- 通过 Kubernetes 对容器进行编排；
- 服务间调用；
早期使用 RabbitMQ 和 Protobuf；
后期使用 gRPC 和 Protobuf；
- 服务发现和路由；
早期使用 RabbitMQ 和etcd；
后面使用 Linkerd/Istio；































