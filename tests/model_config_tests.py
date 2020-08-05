from . import context
from tester import ModelConfig
import unittest

config_file = "config_emu.json"

class ModelConfigTestSuite(unittest.TestCase):

    def test_config_get(self):
        c = ModelConfig(config_file)
        print(c.get_case_list())
        print(c.get_test_root())
        print(c.get_test_result_root())
        print(c.get_log_file_path())
        print(c.get_env_configs())
        print('--- Model Tests ---')
        model_tests = c.get_case_list()
        for model_test in model_tests:
            print(model_test.get_model_dir())
            print(model_test.get_model_log_file())
            print(model_test.get_model_timeout())
            print(model_test.get_socket_file())
            print(model_test.get_test_log_file())
            print(model_test.get_test_names())

def main():
    unittest.main()


if __name__ == '__main__':
    main()
