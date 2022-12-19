"""Readers and writers."""
from threading import Thread, Condition, Event
from time import sleep
from random import randint


TEXT = ['Aboba', 'Kokos', 'Kakat']


class Reader(Thread):
    """Class of reader."""

    def __init__(self, name):
        """Initialization of reader.

        Args:
            name (str): name of reader.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Run method of reader."""
        global event
        while event.wait():
            print('Reader {0} read letter'.format(self.name))


class Writer(Thread):
    """Class of writer."""

    TIMEOUT_WRITING = (3, 6)
    TIME_OF_SLEEP = (2, 4)

    def __init__(self, name):
        """Inialization of writer.

        Args:
            name (str): name of writer.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Run method of writer."""
        global cond
        global event
        with cond:
            cond.wait()
            index = randint(0, len(TEXT) - 1)
            text = TEXT[index]
            print('Writer {0} starting writing'.format(self.name))
            res = text
            while text:
                word = text[:1]
                text = text[1:]
                event.set()
                print('Writer {0} wrote {1}'.format(self.name, word))
                event.clear()
                sleep(randint(*Writer.TIMEOUT_WRITING))
            print('Writer {0} has wrote {1}'.format(self.name, res))
            print('Writer {0} goes to sleep'.format(self.name))
            sleep(randint(*Writer.TIME_OF_SLEEP))


if __name__ == "__main__":
    cond = Condition()
    event = Event()
    for nums in range(10):
        Reader(str(nums)).start()
    while True:
        for num in range(2):
            Writer(str(num)).start()
        with cond:
            cond.notify_all()
