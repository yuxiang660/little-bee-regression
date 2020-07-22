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
compile_configs = ['echo "set up compile environment1"', 'echo "set up compile environment2"']
run_configs = ['echo "set up run environment1"', 'echo "set up run environment2"']

class SequencerTestSuite(unittest.TestCase):
    def test_sequencer_run(self):
        seq = Sequencer(test_root_path, test_names, log_dir)
        seq.run(compile_configs, run_configs)
        seq.log(regression_log)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
