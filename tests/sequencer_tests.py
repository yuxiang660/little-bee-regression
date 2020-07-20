from . import context
from tester import sequencer
import unittest

class SequencerTestSuite(unittest.TestCase):
    """Sequencer test cases."""

    def test_hello(self):
        assert True
    
    def test_run(self):
        test = sequencer.Sequencer()
        test.run()

def main():
    unittest.main()

if __name__ == '__main__':
    main()
