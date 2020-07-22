from . import context
from tester import runner
import unittest
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')


runner_name = 'RunnerUnitTests'
mock_dir = './mock'
log_file = './output/runner_tests.log'


class RunnerTestSuite(unittest.TestCase):
    r = runner.Runner(runner_name, mock_dir, log_file)

    @classmethod
    def setUpClass(cls):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_runner_clean(self):
        self.r.clean()

    def test_runner_compile(self):
        configs = ['echo "set up compile environment1"',
                   'echo "set up compile environment2"']
        runtime = self.r.compile(configs)
        print("Runner 'compile' runs {:.3f} seconds".format(runtime))
        assert runtime != 0

    def test_runner_run(self):
        configs = ['echo "set up run environment1"',
                   'echo "set up run environment2"']
        runtime = self.r.run(configs)
        print("Runner 'run' runs {:.3f} seconds".format(runtime))
        assert runtime != 0


def main():
    unittest.main()


if __name__ == '__main__':
    main()
