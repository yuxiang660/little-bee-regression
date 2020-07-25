from . import context
from tester import ParallelTester, Config
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

config_file = "config.json"


class ParallelTesterTestSuite(unittest.TestCase):
    def test_parallel_tester_run(self):
        p = ParallelTester(Config(config_file))
        p.one_click_run()
        p.log()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
