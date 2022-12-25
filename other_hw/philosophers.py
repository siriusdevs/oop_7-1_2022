"""Home work about philosopher's problem."""
from multiprocessing import Process, Lock
from random import randint
from faker import Faker

from time import sleep
PHILOSOPHERS = 6


class Philosopher(Process):
    """Representation of philosopher."""

    EATING_TIME = (1, 3)
    THINKING_TIME = (4, 6)
    TIMEOUT = 0.01
    LEFT_RIGHT = [0, 1]
    RIGHT_LEFT = [1, 0]

    def __init__(self, name: str, chopstick_left: Lock, chopstick_right: Lock):
        """Initialization method.

        Args:
            name (str): philosopher's name.
            chopstick_left (Lock): his left chopstick.
            chopstick_right (Lock): his right chopstick.
        """
        super().__init__(name=name)
        self.name = name
        self.chopstick_left = chopstick_left
        self.chopstick_right = chopstick_right

    def out(self):
        """Function which show us what philosopher doing."""
        print("{0} start eaiting.".format(self.name))
        sleep(randint(*Philosopher.EATING_TIME))
        print("{0} end eating and start thinking.".format(self.name))

    def run(self) -> None:
        """Main philosopher's function that start him."""
        while True:
            chopsticks = self.chopstick_right, self.chopstick_left
            for first_choice, second_choice in (Philosopher.LEFT_RIGHT, Philosopher.RIGHT_LEFT):
                if chopsticks[first_choice].acquire(timeout=Philosopher.TIMEOUT):
                    if chopsticks[second_choice].acquire(timeout=Philosopher.TIMEOUT):
                        self.out()
                        self.chopstick_right.release()
                        self.chopstick_left.release()
                        sleep(randint(*Philosopher.THINKING_TIME))
                        print("{0} end thinking and want's eating.".format(self.name))
                    else:
                        chopsticks[first_choice].release()


if __name__ == '__main__':
    chopsticks = [Lock() for _ in range(PHILOSOPHERS)]

    for number_of_stick in range(PHILOSOPHERS):
        philosopher_name = "Pholosopher {0} #{1}".format(Faker().name(), number_of_stick)
        chopstick_left = chopsticks[number_of_stick - 1]
        chopstick_right = chopsticks[number_of_stick]
        Philosopher(philosopher_name, chopstick_left, chopstick_right).start()
