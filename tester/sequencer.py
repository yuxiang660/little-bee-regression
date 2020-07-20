from . import runner

class Sequencer:
    def run(self):
        task1 = runner.Runner('task1')
        task2 = runner.Runner('task2')
        task1.run()
        task2.run()

