---
layout: default
title: Loop
parent: Examples
nav_order: 3
---

## Loop

This example illustrates how to use a loop in AWPL to repeatedly execute a set of tasks until a given condition is no longer met.

<img src="../figures/loop.png" alt="loop" style="display: block; margin: 0 auto;" width="50%"/>

- The application starts with task `t_1`.
- The loop node (`loop_1`) is defined with a `loop_data` section:
  - `loop_identifier_1` is the loop variable. 
  - `init: "t_1"` initializes the loop variable with the output of task `t_1`.
  - `loop: "t_2"` updates the loop variable during each iteration with the result of task `t_3`.
- The condition checks whether the value of `loop_identifier_1` equals `10`. If the condition is satisfied, the body of the loop executes again.
- The body of the loop consists of two tasks: `t_2` and `t_3`
- Once the loop condition evaluates to false, execution continues with task `t_4`, which depends on the loop node `loop_1`.

```yaml
---
name: "loop"
runtime: "airflow"
config:
  resource_hints: []
  slo: []
  runtime:
    schedule: "@daily"
nodes:
  - task:
      id: "t_1"
      description: "The first task of the application."
      task_config: {}           # using Airflow EmptyOperator 
      depends_on: []
  - loop:
      id: "loop_1"
      description: "This is a sequential loop."
      loop_data:
        id: "loop_identifier_1"
        init: "$t_1"
        loop: "$t_3"
      conditions:
        - lhs: "$loop_identifier_1"
          rhs: "10"
          operator: "=="
      body:
        - task:
            id: "t_2"
            task_config: {}
            depends_on: []
        - task:
            id: "t_3"
            task_config: {}
            depends_on: 
              - "t_2"
      depends_on:
        - "t_1"
  - task:
      id: "t_4"
      task_config: {}
      depends_on: 
        - "loop_1"
```
