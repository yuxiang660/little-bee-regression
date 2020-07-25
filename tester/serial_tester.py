from .tester import Tester
from .job import Job
import os
import logging


class SerialTester(Tester):
    def __init__(self, configs):
        super().__init__(configs)

    def one_click_run(self):
        for job_name, job in self._jobs.items():
            logging.info(f"### Setup test '{job_name}' ###")
            job.setup(self._configs.get_env_configs())

            logging.info(f"### Compile test '{job_name}' ###")
            job.compile()

            logging.info(f"### Run test '{job_name}' ###")
            job.run(self._configs.get_timeout())
            runtime = job.get_runtime()
            logging.info("### End test '{}' in {:.3f} seconds ###".format(job_name, runtime))

            self._job_run_times[job_name] = runtime
