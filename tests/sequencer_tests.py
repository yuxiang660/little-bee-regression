from . import context
from tester import sequencer
import unittest

test_names = ["test1", "test2"]

class SequencerTestSuite(unittest.TestCase):
    """Sequencer test cases."""

    def test_constructor(self):
        sequencer.Sequencer(test_names)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
