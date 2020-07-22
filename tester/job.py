from . import command
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
        self._runtime = 0

        logging.info(
            f">>> Start test '{self._name}' in '{self._dir}' folder, see the log in '{self._log_file}' <<<")
        with open(self._log_file, 'w') as f:
            f.write(
                f"--- Start test '{self._name}' in '{self._dir}' folder at '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}' ---\n\n")

    def clean(self):
        clean_cmd = f'cd {self._dir} && make clean'
        cmd = command.Command(clean_cmd, self._log_file)
        self._runtime += cmd.run()

    def compile(self, configs):
        self.__setup(configs)
        compile_cmd = f'cd {self._dir} && make regcompile'
        cmd = command.Command(compile_cmd, self._log_file)
        self._runtime += cmd.run()

    def run(self, configs, timeout=None):
        self.__setup(configs)
        run_cmd = f'cd {self._dir} && make regrun'
        cmd = command.Command(run_cmd, self._log_file)
        self._runtime += cmd.run(timeout)

    @property
    def runtime(self):
        return self._runtime

    def __setup(self, configs):
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
