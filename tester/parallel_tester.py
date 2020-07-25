from .tester import Tester
from .job import Job
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging


class ParallelTester(Tester):
    def __init__(self, configs):
        super().__init__(configs)
        self._total_time = 0

    def __compile(self, job_name):
        super().compile(job_name)
        return job_name

    def one_click_run(self):
        start = time.time()

        for job_name in self._jobs:
            self.setup(job_name)

        with ThreadPoolExecutor(max_workers=5) as t:
            tasks = []
            for job_name in self._jobs:
                tasks.append(t.submit(self.__compile, job_name))
            for future in as_completed(tasks):
                job_name = future.result()
                self.run(job_name)

        self._total_time = time.time() - start
        logging.info("*** Regression parallel test total time: {:.3f} seconds ***".format(self._total_time))
