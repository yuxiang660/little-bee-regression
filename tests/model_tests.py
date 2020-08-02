from . import context
from tester import Model
import unittest
import logging
import os


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
model_dir = './mock/model'
socket_file = 'data/socket_port.info'
log_file = './output/model_tests.log'

os.makedirs(os.path.dirname(log_file), exist_ok=True)


class ModelTestSuite(unittest.TestCase):

    def test_model_start_stop(self):
        m = Model(model_dir, socket_file, log_file)
        m.start(10)
        m.stop()

def main():
    unittest.main()


if __name__ == '__main__':
    main()
