---
layout: default
title: Loop
parent: Getting Started
nav_order: 3
---

## Loop

A **loop** in AWPL represents a repeated execution of a set of nodes. The loop definition consists of metadata (identifier, description, dependencies - similar as in [task]({% link language-constructs/task.md %})), 
a loop condition (evaluated in the same way as for a [branch]({% link language-constructs/branching.md %})), and a body that specifies the nodes executed on each iteration.

The `loop_data` field allows defining and tracking data within a loop. Similar to [branch]({% link language-constructs/branching.md %}), where task outputs can be referenced, `loop_data` provides a mechanism to carry values across loop iterations. It requires:
- `init`: the initial value, typically produced by a task outside the loop.
- `loop`: the updated value, produced by a task executed inside the loop.

{: .note }
The `loop_data` identifier can then be referenced in the loop’s condition to determine whether the loop should continue based on the updated values. See [examples]({% link examples.md %}) for more details.

```yaml
loop:
  id: "identifier"
  description: "description"
  loop_data:
    id: "loop_identifier"
    init: "task_outside_loop"
    loop: "task_inside_loop"
  conditions:
    - lhs: "lhs"
      rhs: "rhs"
      operator: "operator"
      negation: true | false
      combinedWith: "and/or"
  body:
    - ...
  depends_on:
    - "identifier"
```

#### Arguments

| Name             | Type   | Required | Default | Description                                                                                      |
|------------------|--------|----------|---------|--------------------------------------------------------------------------------------------------|
| `id`             | string | yes      | –       | Unique identifier of the loop node.                                                              |
| `description`    | string | no       | ""      | Optional description explaining the purpose of the loop.                                         |
| `conditions`     | list   | yes      | –       | Defines when the loop continues or terminates. Conditions follow the same rules as for a branch. |
| `loop_data`      | object | no       | –       | Defines data flow variables associated with the loop.                                            |
| `loop_data.id`   | string | yes      | –       | Identifier for the loop variable.                                                                |
| `loop_data.init` | string | yes      | –       | Reference to a task or value used to initialize the loop variable.                               |
| `loop_data.loop` | string | yes      | –       | Reference to a task inside the loop body that updates the loop variable.                         |
| `body`           | list   | yes      | –       | List of nodes (tasks, branches, loops, parallel nodes) executed in each loop iteration.          |
| `depends_on`     | list   | no       | []      | List of task or branch IDs that must complete before this loop executes.                         |


