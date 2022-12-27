"""The Reader and Writer classes"""
from threading import Thread, Lock, Event
from time import sleep
from random import randint, choice

TIMEOUT_THE_LETTERS = (1, 1)
CHILL = (4, 5)
book = ''
LINES = ['ARINA IS SLEEPING']
BOOK_LOCK = Lock()
add_letters = Event()


class Writer(Thread):
    """Tthe Writer class"""

    def __init__(self, name: str, line: str, book_lck: Lock):
        """Method  initialize  Writer's class.

        Args:
            name: writer's name.
            line: writer's line to write in the book.
            book_lck (Lock): the lock to change book .
        """
        super().__init__()
        self.name = name
        self.line = line
        self.book_lkc = book_lck

    def run(self):
        """Writers write in  book and sleep."""
        global book, add_letters
        while True:
            print('Писатель по имени  {0} хочет написать {1}'.format(self.name, self.line))
            with self.book_lkc:
                for letter in self.line:
                    book += letter
                    print('Писатель по имени {0} пишет букву {1}'.format(self.name, letter))
                    add_letters.set()
                    add_letters.clear()
                    sleep(randint(*TIMEOUT_THE_LETTERS))
            print('Писатель по имени  {0} уходит спать '.format(self.name))
            sleep(randint(*CHILL))


class Reader(Thread):
    """The Reader class"""

    def __init__(self, name: str):
        """Method which initialize cllas Reader.

        Args:
            name: name of a reader.
        """
        super().__init__()
        self.name = name

    def run(self):
        """Readers are reading a book in real time."""
        global add_letters, book

        while True:
            add_letters.wait()
            print('Читатель по имени  {0} читает {1}'.format(self.name, book))


if __name__ == '__main__':
    WRITERS = [Writer(numbers, choice(LINES), BOOK_LOCK) for numbers in range(3)]
    READERS = [Reader(numbers) for numbers in range(4)]

    for reader in READERS:
        reader.start()

    for writer in WRITERS:
        writer.start()
