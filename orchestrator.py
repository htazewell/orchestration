import logging
import time
from task import Task


class Orchestrator:
    def __init__(self):
        self.tasks = []

    def add_task(self, cron_expression, script_type):
        task = Task(cron_expression, script_type)
        self.tasks.append(task)
        return task

    def execute_tasks(self):
        while True:
            for task in self.tasks:
                # Check if the task should be skipped
                if any(skip_condition for skip_condition in task.skips):
                    logging.info(f"Skipping task execution due to skip conditions: {task.cron_expression}")
                    continue

                if task.should_execute():
                    for script in task.scripts:
                        if isinstance(script, tuple) and len(script) == 2:
                            script_path, parameters_list = script
                            task.repeat(script_path, parameters_list)
                        else:
                            task.execute_script(script)

            time.sleep(task.interval)  # Sleep for 1 second