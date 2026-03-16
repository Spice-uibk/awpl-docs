---
layout: default
title: Configuration
nav_order: 2
---

# Configuration

In AWPL, users can define custom configurations for their applications or tasks. Three configurable layers are provided, each serving a distinct purpose:
- [**Resource hints**]({% link configuration/resource_hints.md %}): Provide guidance on the computational resources that the tasks are expected to require. These hints can include CPU/GPU, memory, or storage preferences, helping the runtime system optimize execution. 
- [**Service-Level Objectives (SLOs)**]({% link configuration/slo.md %}): Define performance or quality goals of an application or task, such as execution deadlines, latency targets, or throughput expectations. SLOs allow AWPL to reason about trade-offs and make scheduling or optimization decisions.
- [**Runtime system-specific**]({% link configuration/runtime.md %}): Contains parameters and settings specific to the execution platform (e.g., Apache Flink, Apache Airflow). This layer includes fields like scheduling options, retry policies, and platform-specific tuning parameters.

```yaml
---
name: "name"
runtime: "runtime"
config:                       # application-specific configuration
  resource_hints: ...
  slo: ...
  runtime: ...
nodes:
  - task:
      id: "identifier"
      task_config:            # task-specific configuration
        resource_hints: ...
        slo: ...
        ...
```
