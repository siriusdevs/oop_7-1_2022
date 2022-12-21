"""Write how the writers and readers interact with the book."""

from threading import Thread, Event, Lock
from random import choice, randint
from time import sleep


class Writer(Thread):
    """Representation of a writer.

    Attributes:
    name(str): name of the writer
    """

    LETTERS = 'e', 'l', 'r', 'e', 'y', 'p', 'l', 'a', 'n', 'e', 't', 'a'

    def __init__(self, name: str):
        """Initialize the writer.

        Args:
            name(str): name of the writer
        """
        super().__init__()
        self.name = name
        self.letters = [choice(Writer.LETTERS) for _ in range(randint(1, 3))]
        self.letters_to_write = ''

    def run(self):
        """Run the writer thread."""
        global mutex
        with mutex:
            for letter in self.letters:
                self.letters_to_write += letter
                print("Writer {0} wrote '{1}'".format(self.name, self.letters_to_write))
                event.set()
                event.clear()
                sleep(randint(*INTERVAL))
        print('Writer {0} goes to sleep'.format(self.name))
        sleep(randint(*SLEEP_INTERVAL))


class Reader(Thread):
    """Representation of a reader.

    Attributes:
    name(str): name of the reader
    event(Event): the event when the writer writes sth in the book
    """

    def __init__(self, name: str, event: Event):
        """Initialize the reader.

        Args:
            name(str): name of the reader
            event(Event): the event when the writer writes sth in the book
        """
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        """Run the reader thread."""
        global writer
        while True:
            self.event.wait()
            print("Reader {0} read '{1}'".format(self.name, writer.letters_to_write))
            sleep(randint(*INTERVAL))


INTERVAL = (2, 3)
SLEEP_INTERVAL = (10, 15)   # el tiempo que necesita un escritor para descansar

if __name__ == '__main__':
    event = Event()
    mutex = Lock()
    for num in range(2):
        Reader(str(num), event).start()

    while True:
        for wnum in range(5):
            writer = Writer(str(wnum))
            writer.start()
            sleep(randint(*INTERVAL))
