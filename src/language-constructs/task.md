---
layout: default
title: Task
parent: Getting Started
nav_order: 1
---

## Task

A **task** in AWPL represents a unit of computation or data processing within an application. Tasks are the fundamental building blocks of AWPL and can perform a wide variety of operations, such as:

- reading or writing data from external sources,
- executing computations or transformations (like filtering, aggregating, joining), and
- logging or monitoring.

Each task is uniquely identified by its `id` and can optionally include a `description` for documentation purposes. Tasks can also define task-specific configurations (`task_config`) and dependencies on other tasks (`depends_on`), allowing AWPL to manage execution order automatically.

```yaml
task: 
  id: "identifier"
  description: "description"
  depends_on:
    - "identifier"
  task_config: ...
```

#### Arguments

| Name              | Type   | Required | Default | Description                              |
|-------------------|--------|----------|---------|------------------------------------------|
| `id`              | string | yes      | –       | Unique identifier of the task.           |
| `description`     | string | no       | ""      | Optional description of the task.        |
| `depends_on`      | list   | no       | []      | List of task IDs this one depends on.    |
| `task_config`     | object | yes      | -       | see [here]({% link configuration.md %}). |

