import json
import os
import re

class Logger:
    TEST_RESULT_KEY = 'test_log_file'
    TEST_RUNTIME_KEY = 'run_time'
    TEST_PASS_KEY = 'pass'

    def __init__(self, test_results, test_run_times):
        self._test_results = test_results
        self._test_run_times = test_run_times

    def __parse(self, test_log_file):
        assert os.path.exists(test_log_file)
        with open(test_log_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if re.match('error', line, re.IGNORECASE):
                    return False
            for line in lines:
                if re.match('TEST_PASSED', line):
                    return True
        return False

    def log(self, output_file):
        output = {}
        for test_name, test_log_file in self._test_results.items():
            log = {}
            log[self.TEST_RESULT_KEY] = os.path.abspath(test_log_file)
            log[self.TEST_RUNTIME_KEY] = round(self._test_run_times[test_name], 2)
            log[self.TEST_PASS_KEY] = self.__parse(test_log_file)
            output[test_name] = log

        assert os.path.exists(os.path.dirname(output_file))
        with open(output_file, 'w') as f:
            json.dump(output, f, indent=4)

