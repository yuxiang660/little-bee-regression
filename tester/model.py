from .command import Command
import logging
import os
import time

class Model:
    def __init__(self, model_path, socket_file, log_file):
        assert os.path.exists(model_path)
        self._model_path = model_path
        self._socket_file = os.path.join(model_path, socket_file)
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self._log_file = log_file

        start_log = f"--- Begin to start model at '{self._model_path}', see the log in '{self._log_file}' ---"
        logging.info(start_log)
        with open(self._log_file, 'w') as f:
            f.write(start_log + "\n\n")

    def start(self, timeout_s):
        if os.path.exists(self._socket_file):
            os.remove(self._socket_file)

        start_model_cmd = f'cd {self._model_path} && start.sh'
        self._cmd = Command(start_model_cmd, self._log_file)

        start_time = time.time()
        while not os.path.exists(self._socket_file):
            logging.info(f"--- Starting model at '{self._model_path}', see the log in '{self._log_file}' ---")
            time.sleep(5)
            if (round(time.time() - start_time) > timeout_s):
                logging.error(f"--- Failed to start model at '{self._model_path}', see the log in '{self._log_file}' ---")
                raise Exception("Failed to start model")
        logging.info(f"--- Successfully start model at '{self._model_path}', see the log in '{self._log_file}' ---")

    def stop(self):
        if self._cmd is not None:
            logging.info(f"--- Stop model at '{self._model_path}', see the log in '{self._log_file}' ---")
            self._cmd.kill()
