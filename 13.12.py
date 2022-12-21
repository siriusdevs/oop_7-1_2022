"""Representation of a reader and writer."""
from threading import Thread, Lock, Condition
from time import sleep
from random import randint, choice


class Writer(Thread):
    """Representation of a writer."""

    REST_TIME = (1, 2)
    WRITE_TIME = 1

    def __init__(self, name: str, line: str) -> None:
        """Initialize a writer.

        Args:
            name : str - name of the writer
            line : str - line that the writer will write
        """
        super().__init__()
        self.name = name
        self.line = line

    def run(self) -> None:
        """Start writing a book."""
        global book, lock, notifier
        while True:
            print('Writer {0} wants to write {1}'.format(self.name, self.line))
            lock.acquire()
            book = ''
            print('Writer {0} clears the book and starts his work'.format(self.name))
            for letter in self.line:
                with notifier:
                    book += letter
                    print('Writer {0} writes down {1}'.format(self.name, book))
                    notifier.notify_all()
                sleep(Writer.WRITE_TIME)
            print('Writer {0} has finished his line: {1}'.format(self.name, self.line))
            rest = randint(*Writer.REST_TIME)
            print('Writer {0} will rest now for {1} s.'.format(self.name, rest))
            lock.release()
            sleep(rest)


class Reader(Thread):
    """Representation of a reader."""

    def __init__(self, name: str) -> None:
        """Initialize a reader.

        Args:
            name : str - name of the reader
        """
        super().__init__()
        self.name = name

    def run(self):
        """Start reading a book."""
        global book, notifier
        while True:
            with notifier:
                notifier.wait()
                print('Reader {0} reads {1}'.format(self.name, book))


NUMBER_OF_READERS = 6
NUMBER_OF_WRITERS = 50
LINES = ['TU CASA MI CASA', 'THE BETTER THE WORSE', 'EXTRAORDINARY LINES']

if __name__ == '__main__':
    notifier = Condition(lock=Lock())
    lock = Lock()
    for r_name in range(NUMBER_OF_READERS):
        Reader(str(r_name)).start()
    for w_name in range(NUMBER_OF_WRITERS):
        random_line = choice(LINES)
        Writer(w_name, random_line).start()
