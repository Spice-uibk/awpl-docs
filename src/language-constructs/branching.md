---
layout: default
title: Branching
parent: Getting Started
nav_order: 2
---

## Branch

A **branch** in AWPL represents a conditional step that determines which set of downstream tasks should be executed. Branches allow for dynamic routing of application execution depending on task outputs or other criteria.

A condition in AWPL follows these rules:

- The left- and right-hand sides (`lhs` and `rhs`) of a condition can reference:
  - A literal value (e.g., `10`).
  - The output of a previous task by using its task identifier, prefixed with the special character `$` (e.g., `$task_1`). If the task produces a JSON object, dot notation (`.`) can be used to access a specific field or nested object (e.g., `$task_1.output.field`).
- The `operator` must be one of: `>`, `<`, `>=`, `<=`, `==`, or `equals`.
- `combinedWith` is used to combine multiple conditions using logical operators (`and` / `or`).
- The `branches` field specifies which nodes (tasks, branches, loops, etc.) are executed depending on whether the condition evaluates to true or false. 

All other fields are similar to those of a [task]({% link language-constructs/task.md %}) and follow the same conventions for identifiers, descriptions, and dependencies.

```yaml
branch:
  id: "identifier"
  description: "description"
  conditions:
    - lhs: "lhs"
      rhs: "rhs"
      operator: "operator"
      negation: true | false
      combinedWith: "and/or"
  branches:
    true:
      - ...
    false:
      - ...
  depends_on:
    - "identifier"
```

#### Arguments

| Name             | Type   | Required | Default | Description                                                                                                                          | 
|------------------|--------|----------|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | string | yes      | –       | Unique identifier of the branch node.                                                                                                |
| `description`    | string | no       | ""      | Optional description explaining the purpose of this branch.                                                                          |
| `conditions`     | list   | yes      | –       | List of individual conditions. Each condition compares a left-hand side (`lhs`) with a right-hand side (`rhs`) using an `operator`.  |
| `lhs`            | string | yes      | –       | Left-hand side of a condition.                                                                                                       |
| `rhs`            | string | yes      | –       | Right-hand side of a condition.                                                                                                      |
| `operator`       | string | yes      | –       | Comparison operator to evaluate the condition, such as `>`, `<`, `==`.                                                               |
| `negation`       | bool   | no       | false   | If true, negates the condition result.                                                                                               |
| `combinedWith`   | string | no       | "and"   | Logical operator used to combine multiple conditions. Can be `and` or `or`.                                                          |
| `branches`       | object | yes      | –       | Defines the downstream nodes to execute depending on the condition outcome. Contains `true` and `false` lists of nodes.              |
| `branches.true`  | list   | yes      | []      | Downstream nodes to execute if the condition evaluates to `true`.                                                                    |
| `branches.false` | list   | no       | []      | Downstream nodes to execute if the condition evaluates to `false`.                                                                   |
| `depends_on`     | list   | no       | []      | List of task or branch IDs that must complete before this branch executes.                                                           |

