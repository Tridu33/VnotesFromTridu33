# 1. solver.planning.domains线上规划解决方案


http://solver.planning.domains/

http://planning.domains/




包括：

- api
http://api.planning.domains/ api查询

https://github.com/AI-Planning/classical-domains PDDL文件的简单集合。当前仅包括经典问题

planning.domains API提供了对广泛的PDDL基准域和问题文件的编程访问。所有物理文件都可以 在GitHub的域存储库中找到。您可以通过克隆存储库或使用下面描述的命令行实用程序来自己获得一份副本。

如果您在PDDL文件中发现任何错误（不完整的集，不良的配方等），请克隆存储库，并将您的修订作为请求请求提交。在合理的情况下，我们还将接受带有全新基准测试集的拉取请求（例如，在新的IPC竞赛之后或作为特定套件的发布）。目前，仅接受经典的PDDL基准（任何PDDL级别/表现力），但是将来我们希望将其扩展到其他更丰富的形式主义（POND，FOND，RDDL等）。

文件集合只是api.planning.domains的第一个组件。该服务的主要方面是提供用于查询，查看和浏览现有域的界面。我们存储并不断更新每个领域和问题的属性。例如，计划成本的上限和下限，域中的要求，问题的经典宽度等。在此页面上，您可以找到api.planning.domains接口的描述以及有关的详细信息用来简化与API交互的工具/库。

该API包含三种类型的对象：

问题：有关每个问题的信息，包括其文件，相应的域文件，问题的统计信息等。
域：每个单独域的信息，包括其描述和该域的各种统计信息。
集合：域集，包括每个IPC的集合，单个计划程序集合等。
免责声明：此刻，API应该被认为处于非常Alpha阶段。希望最终有一种方法可以精确地引用评估软件时使用的基准，但暂时我们仍在修复领域，替换问题集并纠正各种统计数据中的错误。在删除此免责声明之前，我们建议您不要将API用于公务（学术界或其他领域）。





- solver


http://solver.planning.domains/


在线PDDL文件求解器范例教程 ，

可以通过发送指向PDDL文件的链接或直接以JSON格式发送原始PDDL内容来调用软件，以检索或验证计划。

Javascript/pytoon远程调用使用范例 代码


- editor

http://editor.planning.domains/  在线PDDL编辑/求解/验证器












- education

http://education.planning.domains/

学习自动教学计划和建模技术的资源

PPT课间源码和视频教程



































