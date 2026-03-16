---
layout: default
title: Runtime Systems
parent: Configuration
nav_order: 3
---

## Runtime System

This type of configuration is **runtime system–specific**, meaning the exact parameters depend on the target execution platform (e.g., [Apache Airflow]({% link configuration/runtime/apache_airflow.md %}) or [Apache Flink]({% link configuration/runtime/apache_flink.md %})).

The `runtime` field specifies which execution platform should be used to run the application. A list of available runtime systems can be found in the corresponding section of this documentation.

```yaml
---
name: "name"
runtime: "runtime"
config: ...
nodes: ...
```
