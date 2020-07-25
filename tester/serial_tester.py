from .job import Job
from .logger import Logger
from .config import Config
import os
import logging


class SerialTester:
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

    def one_click_run(self):
        for job_name, job in self._jobs.items():
            logging.info(f"### Setup test '{job_name}' ###")
            job.setup(self._configs.get_env_configs())

            logging.info(f"### Compile test '{job_name}' ###")
            job.compile()

            logging.info(f"### Run test '{job_name}' ###")
            job.run(self._configs.get_timeout())
            runtime = job.get_runtime()
            logging.info(
                "### End test '{}' in {:.3f} seconds ###".format(job_name, runtime))

            self._job_run_times[job_name] = runtime

    def log(self):
        os.makedirs(os.path.dirname(
            self._configs.get_log_file_path()), exist_ok=True)
        l = Logger(self._job_result_files, self._job_run_times)
        l.log(self._configs.get_log_file_path())
