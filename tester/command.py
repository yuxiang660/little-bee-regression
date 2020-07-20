class Command:
    def __init__(self, cmd):
        self._cmd = cmd

    def run(self):
        print("Run Command:", self._cmd)
