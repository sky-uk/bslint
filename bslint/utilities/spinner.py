import sys
import time
from multiprocessing import Process


class SpinnerProcess(Process):
    def __init__(self, process_lock):
        Process.__init__(self)
        self.process_lock = process_lock

    def run(self):
        spinner = self.spinning_cursor()
        self.show_spinner(spinner)

    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    def show_spinner(self, spinner):
        while self.process_lock.acquire(False):
            self.process_lock.release()
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\r')
