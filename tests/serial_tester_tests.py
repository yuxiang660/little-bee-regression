from . import context
from tester import SerialTester
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')

test_names = ["test1", "test2"]
test_root = './mock'
test_result_root = './output'
log_file = './output/regression.log'
configs = ['echo "set up environment1"', 'echo "set up environment2"']


class SequencerTestSuite(unittest.TestCase):
    def test_sequencer_run(self):
        s = SerialTester(test_names, test_root, test_result_root)
        s.run(configs)
        s.log(log_file)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
