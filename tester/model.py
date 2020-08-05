from .command import Command
import logging
import os
import time
import re

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
            f.write(start_log + "\n")

    def start(self, timeout_s):
        # unset ssh folder permission before start model
        # os.system('chmod 600 ~/.ssh')
        if os.path.exists(self._socket_file):
            os.remove(self._socket_file)
        start_model_cmd = f'cd {self._model_path} && make'
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
            self._cmd.kill()
            stop_log = f"--- Stop model at '{self._model_path}', see the log in '{self._log_file}' ---"
            logging.info(stop_log)
            with open(self._log_file, 'a') as f:
                f.write(stop_log + "\n\n")
        # recover ssh folder permission after stop model
        # os.system('chmod 700 ~/.ssh')

    def get_host(self):
        assert os.path.exists(self._socket_file)
        with open(self._socket_file, 'r') as f:
            line = f.readline()
        match_obj = re.match(r"TCP HOST:(.*) PORT:(\d*)", line, re.M)
        return match_obj.group(1)

    def get_port(self):
        assert os.path.exists(self._socket_file)
        with open(self._socket_file, 'r') as f:
            line = f.readline()
        match_obj = re.match(r"TCP HOST:(.*) PORT:(\d*)", line, re.M)
        return match_obj.group(2)