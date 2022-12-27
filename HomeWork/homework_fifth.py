"""Solving readers and writers problem."""
from threading import Thread, Condition, Lock
from time import sleep
from faker import Faker
from random import randint

BOOK = ''
COUNT_READERS = 5
COUNT_WRITERS = 2


class Writer(Thread):
    """Representation of writer."""

    TIMEOUT_WRITE = (4, 6)
    SLEEP_TIME = (2, 4)
    TEXTS = ["Мне литр пива!", "Пожалуйста, ваше пиво!"]

    def __init__(self, name: str) -> None:
        """Initialization method.

        Args:
            name(str): writer's name.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Main writer's function start."""
        global condition, lock, BOOK
        while True:
            with lock:
                copy_text = Writer.TEXTS[randint(0, len(Writer.TEXTS) - 1)]
                while copy_text:
                    letter = copy_text[:1]
                    BOOK += letter
                    copy_text = copy_text[1:]
                    print("Писатель {0} \033[92mнаписал\033[0m {1}.".format(self.name, letter))
                    condition.acquire()
                    condition.notify_all()
                    condition.release()
                    sleep(randint(*Writer.TIMEOUT_WRITE))
                print("Писатель {0} \033[90mнаписал\033[0m {1}.".format(self.name, BOOK))
                print('Писатель {0} \033[95mушёл спать.\033[0m'.format(self.name))
                BOOK = ''
            sleep(randint(*Writer.SLEEP_TIME))


class Reader(Thread):
    """Representation of reader."""

    def __init__(self, name: str) -> None:
        """Initialization method.

        Args:
            name (str): reader's name.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Main reader's function start."""
        global condition
        while True:
            with condition:
                condition.wait()
                print('{0} \033[94mпрочёл!!\033[0m'.format(self.name))
                print("\033[93mЧитатель проитал:\033[0m ", BOOK)


if __name__ == "__main__":
    condition = Condition(lock=Lock())
    lock = Lock()
    readers = [Faker().name() for _ in range(COUNT_READERS)]
    for ind, reader in enumerate(readers):
        Reader("{0} #{1}".format(reader, ind)).start()
    for number in range(COUNT_WRITERS):
        Writer("{0} #{1}".format(Faker().name(), number)).start()