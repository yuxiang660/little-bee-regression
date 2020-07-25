from . import context
from tester import SerialTester, Config
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')

config_file = "config.json"

class SequencerTestSuite(unittest.TestCase):
    def test_sequencer_run(self):
        s = SerialTester(Config(config_file))
        s.one_click_run()
        s.log()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
