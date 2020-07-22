from . import context
from tester import command
import os
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')
log_file = 'output/command_tests.log'


class CommandTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # os.remove(log_file) if os.path.exists(log_file) else None
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_ls_cmd(self):
        cmd = command.Command('ls', log_file)
        runtime = cmd.run()
        print("'ls' command runs {:.3f} seconds".format(runtime))
        assert runtime != 0

    def test_timeout_cmd(self):
        cmd = command.Command('sleep 2', log_file)
        runtime = cmd.run(1)
        print("'sleep 2' command with timeout error")
        assert runtime == command.Command.TIMEOUT

    def test_cmd_run_twice(self):
        cmd = command.Command('cd mock && make clean', log_file)
        runtime = cmd.run()
        print("First time 'cd mock && make clean' command runs {:.3f} seconds".format(
            runtime))
        assert runtime != 0
        cmd = command.Command('cd mock && make clean', log_file)
        runtime = cmd.run()
        print("Second time 'cd mock && make clean' command runs {:.3f} seconds".format(
            runtime))
        assert runtime != 0


class CommandMockTestSuite(unittest.TestCase):
    param_list = ['cd mock && make clean',
                  'cd mock && make regcompile', 'cd mock && make regrun']

    @classmethod
    def setUpClass(cls):
        # os.remove(log_file) if os.path.exists(log_file) else None
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def test_mock_cmds(self):
        for p in self.param_list:
            with self.subTest(msg=f"Run command '{p}'"):
                cmd = command.Command(p, log_file)
                runtime = cmd.run()
                print("'{}' command runs {:.3f} seconds".format(p, runtime))
                assert runtime != 0


def main():
    unittest.main()


if __name__ == '__main__':
    main()
