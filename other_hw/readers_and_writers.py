"""Solving readers and writers problem."""
from threading import Thread, Condition, Lock
from time import sleep
from faker import Faker
from random import randint

string_for_people = ''


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
        """Main reader's function that start him."""
        global condition
        while True:
            with condition:
                condition.wait()
                print('{0} is reading!'.format(self.name))
                print("Current title: ", string_for_people)


class Writer(Thread):
    """Representation of writer."""

    TIMEOUT_WRITING = (4, 6)
    SLEEPING_TIME = (2, 4)
    TEXTS = ["Cъешь этих мягких французких булок", "Не ешь эти булки, они отравлены"]

    def __init__(self, name: str) -> None:
        """Initialization method.

        Args:
            name (str): writer's name.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Main writer's function that start him."""
        global condition, lock, string_for_people
        while True:
            with lock:
                text_copy = Writer.TEXTS[randint(0, len(Writer.TEXTS) - 1)]
                while text_copy:
                    letter = text_copy[:1]
                    string_for_people += letter
                    text_copy = text_copy[1:]
                    print("Writer {0} wrote {1}.".format(self.name, letter))
                    condition.acquire()
                    condition.notify_all()
                    condition.release()
                    sleep(randint(*Writer.TIMEOUT_WRITING))
                print("Writer {0} has wrote {1}.".format(self.name, string_for_people))
                print('Writer {0} goes to sleep'.format(self.name))
                string_for_people = ''
            sleep(randint(*Writer.SLEEPING_TIME))


NUMBER_OF_READERS = 5
NUMBER_OF_WRITERS = 2

if __name__ == "__main__":
    condition = Condition(lock=Lock())
    lock = Lock()
    readers = [Faker().name() for _ in range(NUMBER_OF_READERS)]
    for ind, reader in enumerate(readers):
        Reader("{0} #{1}".format(reader, ind)).start()
    for number in range(NUMBER_OF_WRITERS):
        Writer("{0} #{1}".format(Faker().name(), number)).start()
