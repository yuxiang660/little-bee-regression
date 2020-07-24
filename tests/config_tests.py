from . import context
from tester import Config
import unittest

config_file = "config.json"

class ConfigTestSuite(unittest.TestCase):

    def test_config_get(self):
        c = Config(config_file)
        print(c.get_test_names())
        print(c.get_test_root())
        print(c.get_test_result_root())
        print(c.get_log_file_path())
        print(c.get_configs())

def main():
    unittest.main()


if __name__ == '__main__':
    main()
