---
layout: default
title: ML Pipeline
parent: Examples
nav_order: 5
---

## ML Pipeline
This example demonstrates an AWPL application that represents a typical machine learning pipeline. The pipeline performs data preprocessing, model training, evaluation, and conditional branching. It demonstrates tasks, loops, parallel execution (map), aggregation, and branching.

### Steps
- **`fetch_data`** – Fetches data and calculates an initial metric.

- **`preprocessing_loop`** – Repeatedly runs `preprocessing` until `$loop_identifier_1.metric >= 0.8`. The loop variable is initialized from `fetch_data` and updated each iteration.

- **`train_model`** – Trains the model on preprocessed data; depends on `preprocessing_loop`.

- **`fetch_test_sets`** – Retrieves multiple test sets for evaluation.

- **`evaluation_map`** – Runs `evaluate` on each test set in parallel; depends on `train_model` and `fetch_test_sets`.

- **`aggregate_results`** – Aggregates evaluation outcomes and calculates the average; depends on `evaluation_map`.

- **`result_branch`** – Conditional execution:
   - If average > 0.86 → `advanced_task`
   - Else → `basic_task`
   Depends on `aggregate_results`.

- **`finalize`** – Performs cleanup and outputs results; depends on `result_branch`.


### Concepts
- Looping until a metric threshold is met
- Parallel evaluation with map
- Conditional branching based on results 
- Proper task dependencies to enforce execution order


```yaml
---
name: "ml_pipeline"
runtime: "airflow"
config:
  resource_hints: []
  slo: []
  runtime:
    schedule: "@daily"
    catchup: false
    default_args:
      owner: "user"
      retries: 3
      retry_delay: "1m"
      start_date: '2025-05-05'
nodes:
  - task:
      id: "fetch_data"
      description: "Fetches some data, calculates some metric and stores in xcom"
      task_config: {}
      depends_on: []
  - loop:
      id: "preprocessing_loop"
      description: "Runs until some metric > 0.8"
      loop_data:
        id: "loop_identifier_1"
        init: "$fetch_data.metric"
        loop: "$preprocessing.metric"
      conditions:
        - lhs: "$loop_identifier_1"
          rhs: "0.8"
          operator: "<"
      body:
        - task:
            id: "preprocessing"
            task_config: {}
            depends_on: []
      depends_on:
        - "fetch_data"
  - task:
      id: "train_model"
      description: "Trains model with preprocessed data"
      task_config: {}
      depends_on:
        - "preprocessing_loop"
  - task:
      id: "fetch_test_sets"
      description: "Fetches multiple test sets"
      task_config: {}
      depends_on: []
  - map:
      id: "evaluation_map"
      description: "Evaluation trained model on test sets"
      items: "$fetch_test_sets.test_sets"
      body:
        - task:
            id: "evaluate"
            task_config: {}
            depends_on: []
      depends_on:
        - "train_model"
        - "fetch_test_sets"
  - task:
      id: "aggregate_results"
      description: "Aggregates results and calculates average"
      task_config: {}
      depends_on:
        - "evaluation_map"
  - branch:
      id: "result_branch"
      description: "Chooses different path depending on average result"
      conditions:
        - lhs: "$aggregate_results.result"
          rhs: "0.86"
          operator: ">"
          negation: false
      branches:
        true:
          - task:
              id: "advanced_task"
              description: "Runs an advanced task"
              task_config: {}
              depends_on: []
        false:
          - task:
              id: "basic_task"
              description: "Runs a basic task"
              task_config: {}
              depends_on: []
      depends_on:
        - "aggregate_results"
  - task:
      id: "finalize"
      description: "Some finalization steps, outputs result, cleans up"
      task_config: {}
      depends_on:
        - "result_branch"
```