from .job import Job
from .logger import Logger
import os


class Tester:
    def __init__(self, configs):
        os.makedirs(configs.get_test_result_root(), exist_ok=True)
        self._configs = configs

        self._jobs = {}
        self._job_result_files = {}
        self._job_run_times = {}
        for test_name in configs.get_test_names():
            test_dir = configs.get_test_root() + f'/{test_name}'
            test_result_file = configs.get_test_result_root() + f'/{test_name}.log'
            self._jobs[test_name] = Job(test_name, test_dir, test_result_file)
            self._job_result_files[test_name] = test_result_file

    def setup(self):
        for _, job in self._jobs.items():
            job.setup(self._configs.get_env_configs())

    def compile(self):
        for _, job in self._jobs.items():
            job.compile()

    def run(self):
        for job_name, job in self._jobs.items():
            job.run(self._configs.get_timeout())
            self._job_run_times[job_name] = job.get_runtime()

    def log(self):
        os.makedirs(os.path.dirname(self._configs.get_log_file_path()), exist_ok=True)
        l = Logger(self._job_result_files, self._job_run_times)
        l.log(self._configs.get_log_file_path())
