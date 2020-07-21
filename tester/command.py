import subprocess
import time
import logging


class Command:

    TIMEOUT = -1

    def __init__(self, cmd, log_file):
        self._cmd = cmd
        self._log_file = log_file

    def run(self, timeout_s=None):
        with open(self._log_file, 'a') as f:
            start_log = f">>> Start command '{self._cmd}' <<<"
            f.write(start_log + '\n')
            logging.info(start_log)

        with open(self._log_file, 'a') as f:
            start = time.time()
            try:
                subprocess.run(self._cmd,
                               shell=True,
                               check=False,
                               universal_newlines=True,
                               timeout=timeout_s,
                               stdout=f,
                               stderr=f)
            except subprocess.TimeoutExpired as e:
                err_log = f">>> End command '{self._cmd}' with timeout error: {e.__str__()} <<<"
                f.write(err_log + '\n\n')
                logging.error(err_log)
                return self.TIMEOUT
            else:
                elapsed = time.time() - start
                end_log = ">>> End command '{}' in {:.3f} seconds <<<".format(
                    self._cmd, elapsed)
                f.write(end_log + '\n\n')
                logging.info(end_log)
        return elapsed
