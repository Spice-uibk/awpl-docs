---
layout: default
title: Map
parent: Examples
nav_order: 4
---

## Map

This example shows how to use a map node in AWPL to apply a set of tasks in parallel to each element of a list.

<img src="../figures/map.png" alt="map" style="display: block; margin: 0 auto;" width="50%"/>

- The application begins with task `t_1`, which produces a list output (e.g., `[1,2,3,4]`).
- The map node (`map_1`) takes this list as input via the `items: "t_1"` field. Each element in the list is processed independently in parallel.
- The body of the map defines the tasks executed for each list element:
  - `t_2` runs first for each item.
  - `t_3` depends on `t_2`, so it runs afterward, still within the context of each list element.
- Once all elements have been processed by the map node, execution continues with `t_4`, which depends on `map_1`.

```yaml
---
name: "map"
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
  - map:
      id: "map_1"
      items: "$t_1"             # list
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
        - "map_1"
```
