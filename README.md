# Orchestration

The Orchestration library provides functionality to schedule and execute tasks based on cron expressions. It allows you to add skip conditions and dynamically generate script parameters. This library is designed to simplify the process of automating script execution.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Creating an Orchestrator](#creating-an-orchestrator)
  - [Adding Tasks](#adding-tasks)
  - [Adding Scripts](#adding-scripts)
  - [Adding Repeats](#adding-repeats)
  - [Adding Skip Conditions](#adding-skip-conditions)
  - [Executing Tasks](#executing-tasks)

## Installation<a name="installation"></a>

To use the Orchestration library, you need to have Python installed. You can then install the library using pip:

```
pip install orchestration
```

## Usage<a name="usage"></a>

### Creating an Orchestrator<a name="creating-an-orchestrator"></a>

To get started with the Orchestrator library, you need to create an instance of the `Orchestrator` class:

```python
from orchestration import Orchestrator

orchestrator = Orchestrator()
```

### Adding Tasks<a name="adding-tasks"></a>

You can add tasks to the orchestrator using the `add_task` method. The `add_task` method takes two arguments: `cron_expression` and `script_type`. The `cron_expression` specifies the schedule for the task using cron syntax, and the `script_type` specifies the type of script to execute (e.g., 'bash' or 'python').

```python
task = orchestrator.add_task('0 * * * *', 'bash')
```


You can also specify an optional interval argument to set the interval in seconds between task executions (default is 1 second).

### Adding Scripts<a name="adding-scripts"></a>

You can add scripts to a task using the `add_script` method. The `add_script` method takes the `script_path` argument, which specifies the path to the script file, and an optional `script_parameters` argument, which is a dictionary of parameters to pass to the script.

```python
task.add_script('/path/to/script.sh', {'param1': 'value1', 'param2': 'value2'})
```

### Adding Repeats<a name="adding-repeats"></a>

You can run the same script multiple times with different parameters using the `add_repeat` method. The `add_repeat` method takes the `script_path` argument, which specifies the path to the script file, and a `script_parameters` argument, which is a list of dictionaries of parameters to pass to the script.

```python
task.add_repeat('/path/to/script.sh', [{'param1': 'value1', 'param2': 'value2'}, {'param1': 'value3', 'param2': 'value4'}])
```

### Adding Skip Conditions<a name="adding-skip-conditions"></a>

Skip conditions allow you to specify conditions under which a task should be skipped during execution. You can add skip conditions to a task using the `add_skip` method.

```python
task.add_skip(some_skip_condition)
```



### Executing Tasks<a name="executing-tasks"></a>

Once you have added tasks to the orchestrator, you can start executing them by calling the `execute_tasks` method. This method will continuously check if any tasks need to be executed based on their cron expressions and execute the corresponding scripts.

```python
orchestrator.execute_tasks()
```


The script(s) will be executed using the specified `script_type` (e.g., 'bash' or 'python').
