import json
import os

class Config:
    NONE_TIMEOUT = -1

    CASE_LIST_KEY = "case_list"
    ENV_KEY = "env"
    ENV_PATH_KEY = "path"
    ENV_CUSTOM_KEY = "custom"
    TEST_ROOT_KEY = "test_root"
    TEST_RESULT_ROOT_KEY = "test_result_root"
    LOG_FILE_KEY = "log_file"
    EMULATOR_KEY = "emulator"
    TIMEOUT_KEY = "timeout"

    def __init__(self, config_file):
        assert os.path.exists(config_file)
        with open(config_file, 'r') as f:
            data = json.load(f)
        self._case_list = data[self.CASE_LIST_KEY]
        self._env_path = data[self.ENV_KEY][self.ENV_PATH_KEY]
        self._env_custom = data[self.ENV_KEY][self.ENV_CUSTOM_KEY]
        self._test_root = data[self.TEST_ROOT_KEY]
        self._test_result_root = data[self.TEST_RESULT_ROOT_KEY]
        self._log_file = data[self.LOG_FILE_KEY]
        self._emulator = data[self.EMULATOR_KEY]
        self._timeout = data[self.TIMEOUT_KEY]

    def get_test_names(self):
        return self._case_list

    def get_test_root(self):
        return self._test_root

    def get_test_result_root(self):
        return self._test_result_root

    def get_log_file_path(self):
        return self._log_file

    def get_timeout(self):
        return self._timeout if self._timeout != self.NONE_TIMEOUT else None

    def get_env_configs(self):
        configs = []
        for path in self._env_path:
            configs.append(f'setenv PATH {path}:$PATH')
        for custom in self._env_custom:
            configs.append(custom)
        configs.append(f'setenv EMULATOR {self._emulator}')
        return configs