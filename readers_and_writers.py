"""Solving readers and writers problem."""
from threading import Thread, Lock
from time import sleep
from faker import Faker

global string_for_people
string_for_people = 'a'
lock = Lock()


class Reader(Thread):
    """Representation of reader."""

    REST_BETWEEN_READING = 1

    def __init__(self, name: str) -> None:
        """Initialization method.

        Args:
            name (str): reader's name.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Main reader's function that start him."""
        global string_for_people
        while string_for_people:
            print('{0} is reading!'.format(self.name))
            print("Current title: ", string_for_people)
            sleep(Reader.REST_BETWEEN_READING)


class Writer(Thread):
    """Representation of writer."""

    NUMBER_OF_WRITTING_LETTERS = 10

    def __init__(self, name: str) -> None:
        """Initialization method.

        Args:
            name (str): writer's name.
        """
        super().__init__(name=name)
        self.name = name

    def run(self):
        """Main writer's function that start him."""
        lock.acquire()
        global string_for_people
        string_copy = string_for_people
        print('Writer {0} start writing!'.format(self.name))
        for _ in range(Writer.NUMBER_OF_WRITTING_LETTERS):
            print('Writer {0} is writing!-------'.format(self.name))
            string_for_people += "a"
            sleep(1)
        string_for_people = string_copy
        lock.release()


NUMBER_OF_READERS = 5
NUMBER_OF_WRITERS = 2
if __name__ == "__main__":
    readers = [Faker().name() for _ in range(NUMBER_OF_READERS)]
    writers = [Writer("{0} #{1}".format(Faker().name(), number)) for number in range(NUMBER_OF_WRITERS)]
    for ind, reader in enumerate(readers):
        Reader("{0} #{1}".format(reader, ind)).start()
    while writers:
        writer = writers.pop(0)
        writers.append(Writer(writer.name))
        writer.start()
        sleep(Writer.NUMBER_OF_WRITTING_LETTERS)
