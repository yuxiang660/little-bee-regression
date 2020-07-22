from . import context
from tester import Sequencer
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')
test_root_path = './mock'
test_names = ["test1", "test2"]
log_dir = './output'
regression_log = './output/regression.log'


class SequencerTestSuite(unittest.TestCase):
    def test_sequencer_run(self):
        seq = Sequencer(test_root_path, test_names, log_dir)
        seq.run()
        seq.log(regression_log)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
