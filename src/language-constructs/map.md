---
layout: default
title: Map
parent: Getting Started
nav_order: 4
---

## Map

A **map** in AWPL executes a body concurrently for each element in a list. Unlike a regular loop, which repeats sequentially, a map construct distributes iterations over independent elements, enabling parallel execution.

The `items` field defines the collection to iterate over and can be:
- A literal list (e.g., `[1, 2, 3, 4, 5]`).
- The output of another task, provided that the output is a list.

Each element from items is processed independently by the maps’s body. 

```yaml
map:
  id: "identifier"
  items: "items"
  body:
    - ...
  depends_on:
    - "identifier"
```

#### Arguments

| Name          | Type   | Required | Default | Description                                                                                     |
|---------------|--------|----------|---------|-------------------------------------------------------------------------------------------------|
| `id`          | string | yes      | –       | Unique identifier of the parallel loop node.                                                    |
| `items`       | string | yes      | –       | A literal list of elements (e.g., `[1, 2, 3]`) or the output of another task (must be a list).  |
| `body`        | list   | yes      | –       | List of nodes (tasks, branches, loops, parallel nodes) executed for each element in `items`.    |
| `depends_on`  | list   | no       | []      | List of task or branch IDs that must complete before this parallel loop executes.               |


