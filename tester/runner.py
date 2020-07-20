from . import command


class Runner:
    def __init__(self, name):
        self._name = name

    def run(self):
        print('Runner starts test:', self._name)
        cmd = command.Command('ls')
        cmd.run()
