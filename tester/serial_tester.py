from .tester import Tester
from .job import Job
import time
import logging

class SerialTester(Tester):
    def __init__(self, configs):
        super().__init__(configs)
        self._total_time = 0

    def one_click_run(self):
        start = time.time()
        for job_name in self._jobs:
            self.setup(job_name)
            self.compile(job_name)
            self.run(job_name)
        self._total_time = time.time() - start
        logging.info("*** Regression serial test total time: {:.3f} seconds ***".format(self._total_time))
