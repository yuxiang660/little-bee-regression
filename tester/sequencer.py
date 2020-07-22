from .job import Job
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')


class Sequencer:
    LOG_DIR = './output'
    TEST_BASE_DIR = './mock'

    def __init__(self, test_names):
        os.makedirs(self.LOG_DIR, exist_ok=True)
        log_files = []
        test_dirs = []
        for test_name in test_names:
            log_file = self.LOG_DIR + f'/{test_name}.log'
            log_files.append(log_file)
            test_dir = self.TEST_BASE_DIR + f'/{test_name}'
            test_dirs.append(test_dir)
            logging.info(
                f">>> Create log file: '{log_file}' for the test '{test_dir}' <<<")

    def run(self):
        pass
