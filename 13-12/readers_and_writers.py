"""Model for readers and writers."""
from threading import Thread, Lock, Condition
from time import sleep
from random import randint


class Book(Condition):
    """Class for book."""

    def __init__(self, lock: Lock, text: str = ""):
        """Creates a book.

        Args:
            lock: Lock - write lock.
            text: str - book text.
        """
        super().__init__(lock=lock)
        self.text = text


class Writer(Thread):
    """Class of writer."""

    TIMEOUT_WRITING = (1, 2)
    TIME_OF_SLEEP = (3, 4)

    def __init__(self, name: str, text: str, queue: Lock, book: Book):
        """Creates a writer.

        Args:
            name: str - name of the writer.
            text: str - text of the writer.
            queue: Lock - queue for writing text to the book.
            book: Book - book to write.
        """
        super().__init__(name=name)
        self.name = name
        self.book = book
        self.queue = queue
        self.text = text

    def run(self) -> None:
        """Run method of writer."""
        while True:
            with self.queue:
                print('Writer {0} starting writing'.format(self.name))
                for symbol in self.text:
                    self.book.acquire()
                    self.book.notify_all()
                    self.book.text += symbol
                    # print('Writer {0} write new symbol'.format(self.name))
                    self.book.release()
                    sleep(randint(*Writer.TIME_OF_SLEEP))
                print('Writer {0} end write {1}'.format(self.name, self.text))
                self.book.text = ""
            print('Writer {0} goes to sleep'.format(self.name))
            sleep(randint(*Writer.TIME_OF_SLEEP))


class Reader(Thread):
    """Class of reader."""

    def __init__(self, name: str, book: Book):
        """Creates a reader.

        Args:
            name: str - name of the reader.
            book: Book - book to read.
        """
        super().__init__(name=name)
        self.name = name
        self.book = book

    def run(self) -> None:
        """Run method of reader."""
        while True:
            with self.book:
                self.book.wait()
                print('Reader {0} read letter {1}'.format(self.name, self.book.text))
