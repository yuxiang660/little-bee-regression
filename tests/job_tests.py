from . import context
from tester import Job
import unittest
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')
job_name = 'JobUnitTests'
mock_dir = './mock'
log_file = './output/job_tests.log'


class JobTestSuite(unittest.TestCase):
    j = Job(job_name, mock_dir, log_file)

    @classmethod
    def setUpClass(cls):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_job_clean(self):
        self.j.clean()

    def test_job_compile(self):
        configs = ['echo "set up compile environment1"',
                   'echo "set up compile environment2"']
        self.j.compile(configs)

    def test_job_run(self):
        configs = ['echo "set up run environment1"',
                   'echo "set up run environment2"']
        self.j.run(configs)

    def test_job_runtime(self):
        print("Total runtime of job '{}' is {:.3f} seconds".format(job_name, self.j.get_runtime()))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
