import subprocess
import time
import logging
import os


class Command:

    TIMEOUT = -1

    def __init__(self, cmd, log_file):
        assert os.path.exists(os.path.dirname(log_file))

        self._cmd = cmd
        self._log_file = log_file
        self._start = time.time()

        with open(self._log_file, 'a') as f:
            start_log = f">>> Start command '{self._cmd}' <<<"
            f.write(start_log + '\n')
            logging.info(start_log)
            self._proc = subprocess.Popen(self._cmd,
                                          shell=True,
                                          universal_newlines=True,
                                          stdout=f,
                                          stderr=f)

    def communicate(self, timeout_s=None):
        with open(self._log_file, 'a') as f:
            try:
                self._proc.communicate(None, timeout_s)
            except subprocess.TimeoutExpired as e:
                err_log = f">>> End command '{self._cmd}' with timeout error: {e.__str__()} <<<"
                f.write(err_log + '\n\n')
                logging.error(err_log)
                return self.TIMEOUT
            else:
                elapsed = time.time() - self._start
                end_log = ">>> End command '{}' in {:.3f} seconds <<<".format(self._cmd, elapsed)
                f.write(end_log + '\n\n')
                logging.info(end_log)
                return elapsed
