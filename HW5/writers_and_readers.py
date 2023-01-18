"""Module for solving the problem about writers and readers."""
from random import choice, randint
from string import ascii_lowercase
from threading import Condition, Lock, Thread
from time import sleep


class Writer(Thread):
    """A class that creates a writer."""

    SLEEP_TIME = (1, 3)
    WRITE_TIME = 1

    def __init__(self, name):
        """Initializing attributes for the writer.

        Args:
            name (str): the name of writer.
        """
        super().__init__()
        self.name = name

    def write(self):
        """A method for determining the spelling of something."""
        global book, notifier, records
        book.acquire()
        print("Писатель {0} начал переписывать".format(self.name))
        records = ""
        for _ in range(5):
            with notifier:
                records += choice(ascii_lowercase)
                notifier.notify_all()
            sleep(Writer.WRITE_TIME)
        book.release()

    def run(self):
        """The method responsible for the writer's sleep and start."""
        while True:
            print("Писатель {0} отдыхает".format(self.name))
            sleep(randint(*Writer.SLEEP_TIME))
            print("Писатель {0} готов к работе".format(self.name))
            self.write()


class Reader(Thread):
    """A class that creates a reader."""

    def __init__(self, name):
        """Initializing attributes for the reader.

        Args:
            name (str): the name of reader.
        """
        super().__init__()
        self.name = name

    def run(self):
        """The method responsible for the readers's start."""
        global notifier, records
        while True:
            with notifier:
                notifier.wait()
                print("Читатель {0} читает {1}".format(self.name, records))


if __name__ == "__main__":
    NUM_WRITERS = 2
    NUM_READERS = 6
    book = Lock()
    notifier = Condition(Lock())
    records = ""
    WRITERS = [Writer(str(num)) for num in range(NUM_WRITERS)]
    READERS = [Reader(str(num))for num in range(NUM_READERS)]
    for r in READERS:
        r.start()
    for wr in WRITERS:
        wr.start()
    sleep(1)
