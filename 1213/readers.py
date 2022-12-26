"""Solving readers and writers problem."""
from threading import Thread, Condition, Lock
from time import sleep
from random import randint

read_string = ''


class Reader(Thread):
    """Readers class."""

    def __init__(self, reader_name: str) -> None:
        """Initialize method.

        Args:
            reader_name : str - reader name.
        """
        super().__init__(name=reader_name)
        self.reader_name = reader_name

    def run(self):
        """Main readers function that start him."""
        global condition
        while True:
            with condition:
                condition.wait()
                print('{0} читает!'.format(self.reader_name))
                print("Текущая книга: ", read_string)


class Writer(Thread):
    """Writers class."""

    WRITING_TIME = (3, 5)
    TIME_SLEEP = (1, 3)
    LINES = ["Я пишу, пишу, пишу...", "Меня зовут Кирилл, я..."]

    def __init__(self, writer_name: str) -> None:
        """Initialize method.

        Args:
            writer_name : str - writer name.
        """
        super().__init__(name=writer_name)
        self.writer_name = writer_name

    def run(self):
        """Main writer's function that start him."""
        global read_string
        while True:
            with lock:
                text_copy = Writer.LINES[randint(0, len(Writer.LINES) - 1)]
                while text_copy:
                    letter = text_copy[:1]
                    read_string += letter
                    text_copy = text_copy[1:]
                    print("Писатель {0} написал {1}.".format(self.writer_name, letter))
                    condition.acquire()
                    condition.notify_all()
                    condition.release()
                    sleep(randint(*Writer.WRITING_TIME))
                print("Писатель {0} закончил писать {1}.".format(self.writer_name, read_string))
                print('Писатель {0} идёт спать.'.format(self.writer_name))
                read_string = ''
            sleep(randint(*Writer.TIME_SLEEP))


READERS_NUMBER = 5
WRITERS_NUMBER = 2

if __name__ == "__main__":
    condition = Condition(lock=Lock())
    lock = Lock()
    for reader in range(READERS_NUMBER):
        Reader("{0}".format(reader)).start()
    for writer in range(WRITERS_NUMBER):
        Writer("{0}".format(writer)).start()
