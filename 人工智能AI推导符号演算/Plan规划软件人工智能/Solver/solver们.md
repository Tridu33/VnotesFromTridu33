# 1. solver汇总


- Planner Tools
  - [VAL - The Plan Validator](https://nms.kcl.ac.uk/planning/software/val.html)
  - [ROSPlan - Planning in ROS](https://github.com/KCL-Planning/ROSPlan/)
  - [PlanSys2 - Planning in ROS2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)
  - [Eviscerator - The Planner tester](https://www.github.com/nergmada/eviscerator)
  - [Universal Planning Validator (Under Development)](https://github.com/aig-upf/universal-planning-validator)




https://planning.wiki/extras 介绍 规划工具

 [VAL-计划验证器](https://nms.kcl.ac.uk/planning/software/val.html)

[VAL](https://nms.kcl.ac.uk/planning/software/val.html)（也称为验证器）是一种工具，用于根据原始域和问题文件验证计划者生成的解决方案。VAL使您可以在执行操作时遵守计划所需的所有前提条件，同时检查计划是否真正实现了目标。

 [Eviscerator-规划器测试器](https://www.github.com/nergmada/eviscerator)

[Eviscerator](https://www.github.com/nergmada/eviscerator)是为此PDDL参考指南开发的工具，它使我们能够自动测试和识别计划人员支持的PDDL要求。它是一个开放源代码工具，随附用于Linux的持续部署的预构建二进制文件。这意味着您可以下载它并测试计划程序，而不必担心编译。

 [ROSPlan-ROS中的计划](https://github.com/KCL-Planning/ROSPlan/)

[ROSPlan](https://github.com/KCL-Planning/ROSPlan/)是机器人操作系统（ROS）的模块，允许将AI Planning集成到使用ROS的机器人中。ROSPlan允许对机器人环境进行建模，以计划和执行任务。

[Plansys2-在ROS2中进行规划](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)

[Plansys2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)是机器人作业系统，新版本的一个项目**ROS2**，整合规划和机器人。它的目标是成为一个框架，在其中可以轻松集成不同的计划人员以使机器人执行任务。使用[行为树](https://github.com/BehaviorTree/BehaviorTree.CPP)来实现[动作](https://github.com/BehaviorTree/BehaviorTree.CPP)，并且在仓库中有很多[例子](https://github.com/IntelligentRoboticsLabs/ros2_planning_system_examples/)。

 [通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)

[通用计划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)是一种用于验证计划领域和问题的工具。当前，它只能支持经典的计划问题和领域，但是该工具旨在进行扩展以包括时间域和多主体域。如果您需要一个支持比传统计划更多的PDDL高级功能的验证器，请尝试使用VAL（计划验证器）代替。







