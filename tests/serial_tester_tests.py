from . import context
from tester import SerialTester
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')
test_root_path = './mock'
test_names = ["test1", "test2"]
log_dir = './output'
regression_log = './output/regression.log'
configs = ['echo "set up environment1"', 'echo "set up environment2"']


class SequencerTestSuite(unittest.TestCase):
    def test_sequencer_run(self):
        s = SerialTester(test_root_path, test_names, log_dir)
        s.run(configs)
        s.log(regression_log)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
