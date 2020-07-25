from . import context
from tester import Job
import unittest
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
job_name = 'JobUnitTests'
mock_dir = './mock'
log_file = './output/job_tests.log'

os.makedirs(os.path.dirname(log_file), exist_ok=True)


class JobTestSuite(unittest.TestCase):
    j = Job(job_name, mock_dir, log_file)

    def test_job_setup(self):
        configs = ['echo "set up environment1"', 'echo "set up environment2"']
        self.j.setup(configs)

    def test_job_compile(self):
        self.j.compile()

    def test_job_run(self):
        self.j.run()

    def test_job_runtime(self):
        print("Total runtime of job '{}' is {:.3f} seconds".format(job_name, self.j.get_runtime()))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
