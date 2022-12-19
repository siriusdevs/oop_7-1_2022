"""Solving readers and writers problem."""
from threading import Thread, Condition, Event
from time import sleep
from faker import Faker
from random import randint

global string_for_people
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
        global event
        while event.wait():
            print('{0} is reading!'.format(self.name))
            print("Current title: ", string_for_people)


class Writer(Thread):
    """Representation of writer."""

    TIMEOUT_WRITING = (2, 4)

    def __init__(self, name: str, text: str) -> None:
        """Initialization method.

        Args:
            name (str): writer's name.
            text (str): writer's text.
        """
        super().__init__(name=name)
        self.name = name
        self.text = text

    def run(self):
        """Main writer's function that start him."""
        global condition
        global event
        global string_for_people
        string_copy = string_for_people
        with condition:
            condition.wait()
            while self.text:
                letter = self.text[:1]
                string_for_people += letter
                self.text = self.text[1:]
                event.set()
                print("Writer {0} wrote {1}.".format(self.name, letter))
                event.clear()
                sleep(randint(*Writer.TIMEOUT_WRITING))
            print("Writer {0} has wrote {1}.".format(self.name, string_for_people))
            print('Writer {0} goes to sleep'.format(self.name))
            string_for_people = string_copy


NUMBER_OF_READERS = 5
NUMBER_OF_WRITERS = 2
TEXTS = ["Cъешь этих мягких французких булок", "Не ешь эти булки, они отравлены"]
if __name__ == "__main__":
    condition = Condition()
    event = Event()
    readers = [Faker().name() for _ in range(NUMBER_OF_READERS)]
    for ind, reader in enumerate(readers):
        Reader("{0} #{1}".format(reader, ind)).start()
    while True:
        for number in range(NUMBER_OF_WRITERS):
            Writer("{0} #{1}".format(Faker().name(), number), TEXTS[randint(0, len(TEXTS) - 1)]).start()
        with condition:
            condition.notify_all()
