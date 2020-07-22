from . import context
from tester import Sequencer
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')
test_root_path = './mock'
test_names = ["test1", "test2"]
log_dir = './output'

class SequencerTestSuite(unittest.TestCase):
    """Sequencer test cases."""

    def test_constructor(self):
        Sequencer(test_root_path, test_names, log_dir)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
