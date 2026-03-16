---
layout: home
title: Getting Started
nav_order: 1
---

{: .warning }
> This is an initial version of **AWPL**. The syntax and features may change in the future.

{: .important }
AWPL relies on runtime-specific features to support advanced functionality, such as task-dependent branching, loop conditioning and data mappings. Users are encouraged to consult the [documentation of the target execution platform]({% link configuration/runtime.md %}) to understand how to use these features correctly.

{: .tip }
Download the [JSON Schema](schema.json) to validate your AWPL workflows.

# AWPL

AWPL (Abstract Workflow Pipeline Language) is a **declarative abstraction** for defining both batch and stream applications in a human-readable format using [YAML](https://yaml.org/). 
An AWPL application consists of nodes, which can represent [tasks]({% link language-constructs/task.md %}), [loops]({% link language-constructs/loop.md %}), 
[branches]({% link language-constructs/branching.md %}), or [maps]({% link language-constructs/map.md %}). Each node declares its dependencies, 
as well as runtime-specific [configurations]({% link configuration.md %}). Control flow (e.g., branching, loops, and parallel execution) and data flow among nodes 
are fully specified in the yaml definition. AWPL pipelines remain therefore runtime-system-agnostic, allowing the same specification to be translated into different runtime systems 
such as [Apache Airflow](https://airflow.apache.org/) or [Apache Flink](https://flink.apache.org/), without embedding execution semantics directly in the YAML.

An **application** in AWPL defines a workflow or data pipeline, including its basic control and data flow, execution behavior, and configuration. Each application includes:

- `name`: a unique name of the application,
- `description`: an optional explanation for documentation purposes,
- `runtime`: underlying runtime system to use for execution (see [here]({% link configuration/runtime.md %})),
- `config`: pipeline-specific configuration (see [here]({% link configuration.md %})), and
- `nodes`: the steps that make up the application, which include tasks, branches, loops, or parallel execution.

```yaml
---
name: "name"
description: "description"
runtime: "runtime"
config: ...
nodes:
  - ...
```

#### Arguments

| Name           | Type    | Required | Default | Description                                                                                                                                                                                                                                                                       |
|----------------|---------|----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`         | string  | yes      | –       | Unique name of the application.                                                                                                                                                                                                                                                   |
| `description`  | string  | no       | ""      | Optional description providing context about the application.                                                                                                                                                                                                                     |
| `runtime`      | string  | yes      | –       | Execution environment for the application (see [here]({% link configuration/runtime.md %})).                                                                                                                                                                                      |
| `config`       | object  | yes      | -       | Application-specific configuration; see [here]({% link configuration.md %}).                                                                                                                                                                                                      |
| `nodes`        | list    | no       | []      | List of nodes that make up the application structure. Each node can be a [task]({% link language-constructs/task.md %}), [loop]({% link language-constructs/loop.md %}), [branche]({% link language-constructs/branching.md %}), or [map]({% link language-constructs/map.md %}). |
