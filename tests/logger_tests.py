from . import context
from tester import Logger
import unittest

test_results = {"test1": "./output/test1.log", "test2": "./output/test2.log"}
test_run_times = {"test1": 1.222, "test2": -1}
output_file = "./output/logger_tests.log"


class LoggerTestSuite(unittest.TestCase):

    def test_logger_log(self):
        l = Logger(test_results, test_run_times)
        l.log(output_file)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
