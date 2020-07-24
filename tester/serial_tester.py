from .job import Job
from .logger import Logger
import os
import logging


class SerialTester:
    def __init__(self, test_names, test_root, test_result_root):
        os.makedirs(test_result_root, exist_ok=True)
        self._jobs = {}
        self._job_result_files = {}
        self._job_run_times = {}
        for test_name in test_names:
            test_dir = test_root + f'/{test_name}'
            test_result_file = test_result_root + f'/{test_name}.log'
            self._jobs[test_name] = Job(test_name, test_dir, test_result_file)
            self._job_result_files[test_name] = test_result_file

    def run(self, configs):
        for job_name, job in self._jobs.items():
            logging.info(f"### Start compile test '{job_name}' ###")
            job.compile(configs)
            logging.info(f"### Start running test '{job_name}' ###")
            job.run(configs)
            runtime = job.get_runtime()
            self._job_run_times[job_name] = runtime
            logging.info("### End test '{}' in {:.3f} seconds ###".format(
                job_name, runtime))

    def log(self, output_file):
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        l = Logger(self._job_result_files, self._job_run_times)
        l.log(output_file)
