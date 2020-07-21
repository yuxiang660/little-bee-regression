from . import context
from tester import command
import os
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')


class CommandTestSuite(unittest.TestCase):
    """Command test cases."""

    log_file = 'output/command_tests.log'

    @classmethod
    def setUpClass(cls):
        # os.remove(cls.log_file) if os.path.exists(cls.log_file) else None
        os.makedirs(os.path.dirname(cls.log_file), exist_ok=True)

    def test_ls_cmd(self):
        cmd = command.Command('ls', self.log_file)
        runtime = cmd.run()
        print("'ls' command runs {:.3f} seconds".format(runtime))
        assert runtime != 0

    def test_timeout_cmd(self):
        cmd = command.Command('sleep 2', self.log_file)
        runtime = cmd.run(1)
        print("'sleep 2' command with timeout error")
        assert runtime == command.Command.TIMEOUT


def main():
    unittest.main()


if __name__ == '__main__':
    main()
