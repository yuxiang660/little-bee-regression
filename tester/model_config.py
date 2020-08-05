from .config import Config
import json
import os

class ModelTest:
    MODEL_DIR_KEY = "model_dir"
    SOCKET_FILE_KEY = "socket_file"
    MODEL_LOG_FILE_KEY = "model_log_file"
    MODEL_TIMEOUT_KEY = "model_timeout"
    TESTS_KEY = "tests"
    TEST_LOG_FILE_KEY = "test_log_file"

    def __init__(self, model_test):
        self._model_test = model_test

    def get_model_dir(self):
        return self._model_test[self.MODEL_DIR_KEY]

    def get_socket_file(self):
        return self._model_test[self.SOCKET_FILE_KEY]

    def get_model_log_file(self):
        return self._model_test[self.MODEL_LOG_FILE_KEY]

    def get_model_timeout(self):
        return self._model_test[self.MODEL_TIMEOUT_KEY]

    def get_test_names(self):
        return self._model_test[self.TESTS_KEY] if self._model_test[self.TESTS_KEY] else None

    def get_test_log_file(self):
        return self._model_test[self.TEST_LOG_FILE_KEY]

class ModelConfig(Config):

    def __init__(self, config_file):
        super().__init__(config_file)

    def get_case_list(self):
        model_tests = []
        for model_test in super().get_case_list():
            model_tests.append(ModelTest(model_test))
        return model_tests
