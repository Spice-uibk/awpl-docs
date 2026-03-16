---
layout: default
title: Apache Airflow
parent: Runtime Systems
nav_order: 1
---

# Apache Airflow

{: .important }
To enable task-specific branching, loop iterations or map in AWPL, users **must** implement their tasks to push outputs via **Airflow XComs**. AWPL relies on this to evaluate conditions and determine the execution path in branches, loops and maps.

##### `runtime`: "airflow"

### Application specific configuration

An application `config` in AWPL defines settings that apply to the application as a whole. These settings control scheduling, retries, and metadata tags, enabling fine-grained control over application behavior.

```yaml
config:
  schedule: "schedule"
  catchup: false | true
  tags:
    - "tags"
  default_args:
    owner: "owner"
    retries: retries
    retry_delay: "retry_delay"
    start_date: 'yyyy-mm-ddThh:mm:ssZ'
    end_date: 'yyyy-mm-ddThh:mm:ssZ'
    is_paused_upon_creation: false | true
```

#### Arguments

| Name                        | Type   | Required | Default     | Description                                                                                        |
|-----------------------------|--------|----------|-------------|----------------------------------------------------------------------------------------------------|
| `schedule`                  | string | yes      | –           | Cron-style schedule or interval specifying when the pipeline should run. Allowed values: `@daily`. |
| `catchup`                   | bool   | no       | false       | Whether the pipeline should catch up on missed runs.                                               |
| `tags`                      | list   | no       | []          | Metadata tags to organize or categorize applications.                                              |
| `default_args`              | object | no       | {}          | Default arguments of an application.                                                               |
| `default_args.owner`        | string | no       | ""          | Identifier of the pipeline owner.                                                                  |
| `default_args.retries`      | int    | no       | 0           | Number of times to retry failed tasks by default.                                                  |
| `default_args.retry_delay`  | string | no       | 0m          | Delay between retries (e.g., `"5m"` for 5 minutes).                                                |
| `default_args.start_date`   | string | no       | immediately | Earliest time from which the pipeline can start executing (ISO 8601 format).                       |
| `default_args.end_date`     | string | no       | no end time | Latest time until which the pipeline is allowed to run (ISO 8601 format).                          |
| `is_paused_upon_creation`   | bool   | no       | false       | Specifies if the dag is paused when created for the first time.                                    |


### Task specific configuration

A `task_config` in AWPL allows customizing the behavior and execution environment of a task. It can include general options and runtime-specific configurations such as running the task in a Kubernetes pod.

{: .note }
If the `task_config` is empty (`{}`), AWPL will automatically use the Airflow **EmptyOperator** as a default. This operator acts as a no-op, allowing the task to participate in dependencies, branching, or workflow structure without executing any actual computation.

```yaml
task_config:
  kubernetes_pod_operator:
    name: "name"
    do_xcom_push: true | false
    namespace: "namespace"
    image: "image"
    cmds:
      - "cmd"
    arguments:
      - "argument"
    volumes:
      - name: "name"
        claim_name: "claim_name"
    volume_mounts:
      - name: "name"
        mount_path: "mount_path"
    env_vars:
      - name: "name"
        value: "value"
    image_pull_policy: "Always"
    config_file: "~/.kube/config"
    hostnetwork: true | false
    skip_on_exit_code: 000
```

#### Arguments

| Name                      | Type   | Required | Default        | Description                                                                                                                                    |
|---------------------------|--------|----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `kubernetes_pod_operator` | object | no       | –              | Configuration for running the task in a Kubernetes pod.                                                                                        |
| `do_xcom_push`            | bool   | no       | true           | Whether the task pushes XComs (inter-task messages) in Airflow.                                                                                |
| `name`                    | string | yes      | –              | Name of the Kubernetes pod.                                                                                                                    |
| `namespace`               | string | no       | default        | Kubernetes namespace for the pod.                                                                                                              |
| `image`                   | string | yes      | –              | Docker image to use for the pod.                                                                                                               |
| `cmds`                    | list   | no       | []             | List of commands to execute in the pod.                                                                                                        |
| `arguments`               | list   | no       | []             | Arguments passed to the container entrypoint.                                                                                                  |
| `volumes`                 | list   | no       | []             | Volumes to mount into the pod. Each volume requires a `name` and `claim_name`.                                                                 |
| `volume_mounts`           | list   | no       | []             | Volume mounts inside the pod. Each mount requires a `name` and `mount_path`.                                                                   |
| `env_vars`                | list   | no       | []             | Environment variables for the pod. Each entry has a `name` and `value`.                                                                        |
| `image_pull_policy`       | string | no       | Always         | Image pull policy for the container (e.g., `Always`, `IfNotPresent`).                                                                          |
| `config_file`             | string | no       | ~/.kube/config | Path to the Kubernetes config file.                                                                                                            |
| `hostnetwork`             | bool   | no       | false          | Whether the pod uses the host network.                                                                                                         |
| `skip_on_exit_code`       | number | no       | None           | If the task exits with this exit code, leave the task in skipped state. If set to `None`, any non-zero exit code will be treated as a failure. |

