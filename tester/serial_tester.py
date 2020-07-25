from .tester import Tester
from .job import Job
import os


class SerialTester(Tester):
    def __init__(self, configs):
        super().__init__(configs)

    def one_click_run(self):
        for job_name in self._jobs:
            super().setup(job_name)
            super().compile(job_name)
            super().run(job_name)
