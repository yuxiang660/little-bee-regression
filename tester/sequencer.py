from .job import Job
import os
import logging


class Sequencer:
    def __init__(self, test_root_path, test_names, log_dir):
        os.makedirs(log_dir, exist_ok=True)
        self._jobs = {}
        for test_name in test_names:
            test_dir = test_root_path + f'/{test_name}'
            log_file = log_dir + f'/{test_name}.log'
            self._jobs[test_name] = Job(test_name, test_dir, log_file)

    def run(self):
        for job_name, job in self._jobs.items():
            logging.info(f"### Start test '{job_name}' ###")
            job.clean()
            job.compile([])
            job.run([])
            run_time = job.get_runtime()
            logging.info("### End test '{}' in {:.3f} seconds ###".format(
                job_name, run_time))
