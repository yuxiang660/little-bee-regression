from . import context
from tester import Command
import os
import logging
import unittest

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
log_file = 'output/command_tests.log'


class CommandTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # os.remove(log_file) if os.path.exists(log_file) else None
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_ls_cmd(self):
        cmd = Command('ls', log_file)
        runtime = cmd.run()
        print("'ls' command runs {:.3f} seconds".format(runtime))
        assert runtime != 0

    def test_timeout_cmd(self):
        cmd = Command('sleep 2', log_file)
        runtime = cmd.run(1)
        print("'sleep 2' command with timeout error")
        assert runtime == Command.TIMEOUT

    def test_cmd_run_twice(self):
        cmd_str = 'cd mock && ls'
        cmd = Command(cmd_str, log_file)
        runtime = cmd.run()
        print("First time '{}' command runs {:.3f} seconds".format(cmd_str, runtime))
        assert runtime != 0
        cmd = Command(cmd_str, log_file)
        runtime = cmd.run()
        print("Second time '{}' command runs {:.3f} seconds".format(cmd_str, runtime))
        assert runtime != 0


class CommandMockTestSuite(unittest.TestCase):
    param_list = ['cd mock && make regcompile', 'cd mock && make regrun', 'cd mock && make clean']

    @classmethod
    def setUpClass(cls):
        # os.remove(log_file) if os.path.exists(log_file) else None
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_mock_cmds(self):
        for p in self.param_list:
            with self.subTest(msg=f"Run command '{p}'"):
                cmd = Command(p, log_file)
                runtime = cmd.run()
                print("'{}' command runs {:.3f} seconds".format(p, runtime))
                assert runtime != 0


def main():
    unittest.main()


if __name__ == '__main__':
    main()
