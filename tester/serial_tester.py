from .job import Job
import os
import logging


class SerialTester:
    def __init__(self, test_root_path, test_names, log_dir):
        os.makedirs(log_dir, exist_ok=True)
        self._jobs = {}
        self._job_log_files = {}
        for test_name in test_names:
            test_dir = test_root_path + f'/{test_name}'
            log_file = log_dir + f'/{test_name}.log'
            self._jobs[test_name] = Job(test_name, test_dir, log_file)
            self._job_log_files[test_name] = log_file

    def run(self, compile_configs, run_configs):
        for job_name, job in self._jobs.items():
            logging.info(f"### Start compile test '{job_name}' ###")
            job.compile(compile_configs)
            logging.info(f"### Start running test '{job_name}' ###")
            job.run(run_configs)
            logging.info("### End test '{}' in {:.3f} seconds ###".format(
                job_name, job.get_runtime()))

    def log(self, log_file):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, 'w') as f:
            f.write("Regression Test Results:\n")
