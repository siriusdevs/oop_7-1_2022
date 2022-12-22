from threading import Thread, Lock, Condition
from time import sleep
from random import randint, choice


class Writer(Thread):
    """Writer class."""
    TIME_OUT = (1, 2)
    WRITE_TIME = 1

    def __init__(self, name: str, text: str) -> None:
        """Initialize writer.

        Args:
            name: str - name of writer.
            text: str - strings which he writes.
        """
        super().__init__()
        self.name = name
        self.text = text

    def run(self) -> None:
        """Function where writer writes and notify readers"""
        global book, lock, notifier
        while True:
            lock.acquire()
            book = ''
            print('Writer {0} starts writing'.format(self.name))
            for letter in self.text:
                with notifier:
                    book += letter
                    print('Writer {0} writes down {1}'.format(self.name, book))
                    notifier.notify_all()
                sleep(Writer.WRITE_TIME)
            lock.release()
            sleep(randint(*Writer.TIME_OUT))


class Reader(Thread):
    """Reader class."""

    def __init__(self, name: str) -> None:
        """Initialize reader.

        Args:
            name : str - name of the reader.
        """
        super().__init__()
        self.name = name

    def run(self):
        """Start reading."""
        global book, notifier
        while True:
            with notifier:
                notifier.wait()
                print('Reader {0} is reading {1}'.format(self.name, book))


READERS = 6
WRITERS = 2
LINES = ['check1', 'check2', 'check3']

if __name__ == '__main__':
    notifier = Condition(lock=Lock())
    lock = Lock()
    for reader in range(READERS):
        Reader(str(reader)).start()
    for writer in range(WRITERS):
        if writer < len(LINES):
            Writer(writer, LINES[writer]).start()
        else:
            Writer(writer, choice(LINES)).start()
