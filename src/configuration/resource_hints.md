---
layout: default
title: Resource Hints
parent: Configuration
nav_order: 1
---

## Resource hints

**Resource hints** in AWPL specifies the expected computational resources for a task. These hints help the runtime system optimize execution, allowing it to allocate sufficient resources while balancing load across the pipeline. Each resource hint defines the type of resource and a suggested minimum and maximum allocation.

```yaml
resource_hints:
  - type: "type"
    min: "min"
    max: "max"
```

#### Arguments

| Name  | Type   | Required | Default  | Description                                                                                                          |
|-------|--------|----------|----------|----------------------------------------------------------------------------------------------------------------------|
| `type`| string | yes      | –        | The type of resource. Allowed values are: `cpu` (in millicores), `memory` (in mb), `gpu` (in mb), `storage` (in mb). |
| `min` | number | no       | 0        | Minimum amount of the resource expected for the task (e.g. `2000`).                                                  |
| `max` | number | no       | infinity | Maximum amount of the resource that the task may use (e.g. `5000`).                                                  |
