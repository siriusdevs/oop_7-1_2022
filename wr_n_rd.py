"""Readers and writers."""
from threading import Thread, Condition, Lock
from time import sleep
from random import randint


TEXT = ['Aboba', 'Kokos', 'Cond']
CUR_LETTER = ''


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
        while True:
            with cond:
                cond.wait()
                print('Reader {0} read letter {1}'.format(self.name, CUR_LETTER))


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
        global CUR_LETTER
        while True:
            with lock:
                print('Writer {0} starting writing'.format(self.name))
                text = TEXT[randint(0, len(TEXT) - 1)]
                res = text
                while text:
                    letter, text = text[:1], text[1:]
                    CUR_LETTER = letter
                    print('Writer {0} wrote {1}'.format(self.name, letter))
                    with cond:
                        cond.notify_all()
                    sleep(randint(*Writer.TIMEOUT_WRITING))
            print('Writer {0} has wrote {1}'.format(self.name, res))
            print('Writer {0} goes to sleep'.format(self.name))
            sleep(randint(*Writer.TIME_OF_SLEEP))


if __name__ == "__main__":
    cond = Condition(lock=Lock())
    lock = Lock()
    for nums in range(10):
        Reader(str(nums)).start()
    for num in range(2):
        Writer(str(num)).start()
