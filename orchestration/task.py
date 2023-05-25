import logging
import subprocess
import signal
import pytz
import os
from croniter import croniter
from datetime import datetime, timedelta


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Task:
    def __init__(self, cron_expression, script_type, interval=1):
        self.script_type = script_type
        self.cron_expression = cron_expression
        self.interval = interval
        self.scripts = []
        self.skips = []
        self.parameters = {}

    def add_script(self, script_path, script_parameters=None):
        self.scripts.append(script_path)
        if script_parameters:
            self.parameters.update(script_parameters)

    def add_skip(self, skip_condition):
        self.skips.append(skip_condition)

    def execute_script(self, script_path):
        script_args = [self.parameters.get(param_name, arg) for param_name, arg in self.parameters.items()]
        logging.info(f"Executing {self.script_type} script: {script_path} with arguments: {script_args}")

        try:
            if self.script_type == 'bash':
                process = subprocess.Popen(['bash', script_path] + script_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif self.script_type == 'python':
                process = subprocess.Popen(['python', script_path] + script_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                logging.error(f"Unsupported script type: {self.script_type}")
                return

            stdout, stderr = process.communicate(timeout=60)

            if process.returncode != 0:
                logging.error(f"Error executing script: {script_path}")
                logging.error(stderr)
            else:
                logging.info(f"Script output: {stdout}")
        except subprocess.TimeoutExpired:
            logging.warning(f"Script execution timed out: {script_path}")
            # Kill the hanging script process
            self.kill_script_process(process)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing script: {script_path}")
            logging.error(e.output.decode())

    def kill_script_process(self, process):
        try:
            os.kill(process.pid, signal.SIGTERM)
            logging.warning(f"Hanging script process killed: {process.pid}")
        except OSError:
            logging.error(f"Failed to kill hanging script process: {process.pid}")

    def repeat(self, script_path, parameters_list):
        for parameters in parameters_list:
            self.parameters.update(parameters)
            self.execute_script(script_path)  # Default script type is 'bash'

    def should_execute(self):
        now = datetime.now(pytz.utc)
        cron = croniter(self.cron_expression)
        next_execution = cron.get_next(datetime).replace(tzinfo=pytz.utc)
        return next_execution - now < timedelta(seconds=self.interval*1.01)


