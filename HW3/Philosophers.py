"""The module allows you to imagine a situation with philosophers at a round table \
    (philosophers can reflect and consume food)."""
from threading import Thread, Lock
from time import sleep
from random import randint, choice

NAMES_PHILOSOPHERS = ['Геродот', 'Евклид', 'Архимед', 'Альберт Андреевич', 'Вячеслав Александрович']
EAT_TIME = (2, 3)
THINK_TIME = (3, 4)
TIMEOUT = 1


class ThinkingAndEating(Thread):
    """A class for thinking and eating philosophers."""

    def __init__(self, name: str, right_chopstick, left_chopstick):
        """Initializing attributes.

        Args:
            name (str): philosopher's name.
            right_chopstick (lock): attribute with locking function.
            left_chopstick (lock): attribute with locking function.
        """
        super().__init__()
        self.name = str(choice(NAMES_PHILOSOPHERS))
        self.right_chopstick = right_chopstick
        self.left_chopstick = left_chopstick

    def run(self):
        """Method for starting philosophers."""
        while True:
            print("{0} размышляет".format(self.name))
            sleep(randint(*THINK_TIME))
            print("{0} натолкнулся на мысль поесть".format(self.name))
            self.eat()

    def eat(self):
        """Method for philosophers to eat."""
        left_chopstick = self.left_chopstick
        right_chopstick = self.right_chopstick
        if left_chopstick.acquire(TIMEOUT):
            print("{0} взял левую палочку".format(self.name))
            if right_chopstick.acquire(TIMEOUT):
                print("{0} взял правую палочку".format(self.name))
                print("{0} приступил к поглощению".format(self.name))
                sleep(randint(*EAT_TIME))
                left_chopstick.release()
                right_chopstick.release()
                print("{0} поел и готов к размышлениям".format(self.name))
            else:
                print("{0} положил на место левую палочку".format(self.name))
                left_chopstick.release()


if __name__ == "__main__":
    NUM_PHILOSOPHERS = len(NAMES_PHILOSOPHERS)
    CHOPSTICKS = [Lock() for _ in range(NUM_PHILOSOPHERS)]
    PHILOSOPHERS = [
        ThinkingAndEating(str(num), CHOPSTICKS[num], CHOPSTICKS[(num + 1) % NUM_PHILOSOPHERS])
        for num in range(NUM_PHILOSOPHERS)
    ]
    for philosopher in PHILOSOPHERS:
        philosopher.start()
        sleep(1)
