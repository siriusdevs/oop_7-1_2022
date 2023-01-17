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
        """A method for determining the spelling of something.
        """
        global book, notifier, records
        book.acquire()
        print(f"Писатель {self.name} начал переписывать")
        records = ""
        for _ in range(5):
            with notifier:
                records += choice(ascii_lowercase)
                notifier.notify_all()
            sleep(Writer.WRITE_TIME)
        book.release()


    def run(self):
        """The method responsible for the writer's sleep and start.
        """
        while True:
            print(f"Писатель {self.name} отдыхает")
            sleep(randint(*Writer.SLEEP_TIME))
            print(f"Писатель {self.name} готов к работе")
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
        """The method responsible for the readers's start.
        """
        global notifier, records
        while True:
            with notifier:
                notifier.wait()
                print(f"Читатель {self.name} читает {records}")


if __name__ == "__main__":
    NUM_WRITERS = 2
    book = Lock()
    notifier = Condition(Lock())
    records = ""
    WRITERS = [Writer(str(num)) for num in range(NUM_WRITERS)]
    READERS = [Reader(str(num))for num in range(NUM_WRITERS)]
    for i in enumerate(WRITERS):
        WRITERS[i[0]].start()
        READERS[i[0]].start()
        sleep(1)
