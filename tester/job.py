from .command import Command
import logging
import os
from datetime import datetime


class Job:
    REG_SETUP_FILE = 'reg.setup.tmp'
    ORIGIN_SETUP_FILE = 'setup.sh'

    def __init__(self, name, dir, log_file):
        assert os.path.exists(dir)
        assert os.path.exists(os.path.dirname(log_file))

        self._name = name
        self._dir = dir
        self._log_file = log_file
        self._compile_time = 0
        self._run_time = 0

        logging.info(
            f"--- Test '{self._name}' in '{self._dir}' folder, see the log in '{self._log_file}' ---")
        with open(self._log_file, 'w') as f:
            f.write(
                f"--- Test '{self._name}' in '{self._dir}' folder at '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' ---\n\n")

    def setup(self, configs):
        self.__clean()

        dest_file = f'{self._dir}/{self.REG_SETUP_FILE}'
        src_file = f'{self._dir}/{self.ORIGIN_SETUP_FILE}'

        with open(src_file, 'r') as src:
            lines = src.readlines()

        with open(dest_file, 'w') as dest:
            for line in lines:
                line = line.strip()
                if line.strip() != None:
                    dest.write(line + '\n')
            for config in configs:
                dest.write(config + '\n')

    def compile(self):
        compile_cmd = f'cd {self._dir} && make regcompile'
        cmd = Command(compile_cmd, self._log_file)
        self._compile_time = cmd.run()

    def run(self, timeout=None):
        run_cmd = f'cd {self._dir} && make regrun'
        cmd = Command(run_cmd, self._log_file)
        self._run_time = cmd.run(timeout)

    def get_runtime(self):
        if self._run_time != Command.TIMEOUT:
            return self._compile_time + self._run_time
        return Command.TIMEOUT

    def __clean(self):
        clean_cmd = f'cd {self._dir} && make clean'
        cmd = Command(clean_cmd, self._log_file)
        cmd.run()
