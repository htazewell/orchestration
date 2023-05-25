# Orchestrator

This Python script provides functionality to schedule and execute scripts based on cron expressions. It allows executing both bash and Python scripts and provides options to add script parameters and skip conditions.

## Dependencies
- `croniter`: A Python library to parse cron expressions and calculate the next execution time.

## Usage
1. Import the required modules:
```python
import logging
import subprocess
import signal
import pytz
import time
import os
from croniter import croniter
from datetime import datetime, timedelta
```

2. Configure logging settings:
```python
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

3. Create a `Task` object to define a script execution task:
```python
task = Task(cron_expression, script_type, interval=1)
```
- `cron_expression` (str): A cron expression specifying the schedule of the task.
- `script_type` (str): The type of script to execute, either 'bash' or 'python'.
- `interval` (int): The interval in seconds between task executions (default is 1 second).

4. Add scripts to the task using the `add_script` method:
```python
task.add_script(script_path, script_parameters=None)
```
- `script_path` (str): The path to the script file.
- `script_parameters` (dict): Optional dictionary of script parameters.

5. Add skip conditions to the task using the `add_skip` method:
```python
task.add_skip(skip_condition)
```
- `skip_condition` (bool): A condition that determines whether the task should be skipped.

6. Execute a script using the `execute_script` method:
```python
task.execute_script(script_path)
```
- `script_path` (str): The path to the script file.

7. Repeat script execution with different parameters using the `repeat` method:
```python
task.repeat(script_path, parameters_list)
```
- `script_path` (str): The path to the script file.
- `parameters_list` (list): A list of dictionaries containing different sets of script parameters.

8. Check if the task should be executed using the `should_execute` method:
```python
if task.should_execute():
    # Execute the task
```

9. Create an `Orchestrator` object to manage multiple tasks:
```python
orchestrator = Orchestrator()
```

10. Add tasks to the orchestrator using the `add_task` method:
```python
task = orchestrator.add_task(cron_expression, script_type)
```
- `cron_expression` (str): A cron expression specifying the schedule of the task.
- `script_type` (str): The type of script to execute, either 'bash' or 'python'.

11. Execute all tasks using the `execute_tasks` method:
```python
orchestrator.execute_tasks()
```

Note: The script will run indefinitely, executing tasks based on their schedules and intervals.

## Example

Here's an example usage of the script:

```python
# Create a Task
task = Task("*/5 * * * *", "bash", interval=5)

# Add scripts to the task
task.add_script("script.sh")
task.add_script("another_script.sh", {"param1": "value1", "param2": "value2"})

# Add skip conditions
task.add_skip(False)  # Do not skip this task

# Create a Orchestrator
orchestrator = Orchestrator()

# Add the task to the orchestrator
orchestrator.add_task("0 0 * * *", "python")

# Execute all tasks