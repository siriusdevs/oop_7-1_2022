"""The vizualization of eating and thinking philosophers."""

from multiprocessing import Process, Lock
from time import sleep
from random import randint


class Philosopher(Process):
    """Representation of a philosopher.

    Attributes:
        name(str): name of the philosopher
        left(Lock): the fork that lies on the left
        right(Lock): the fork that lies on the right
    """

    WAIT = 1
    THINKING = (4, 6)
    EATING = (4, 6)

    def __init__(self, name: str, left: Lock, right: Lock):
        """Initialize the philosopher.

        Args:
            name(str): name of the philosopher
            left(Lock): the fork that lies on the left
            right(Lock): the fork that lies on the right
        """
        super().__init__()
        self.name = name
        self.left = left
        self.right = right

    def eating(self):
        """Make the philosopher eat if the forks are free."""
        if self.left.acquire():
            # если философ возьмет правую вилку, он зайдет в if и будет есть, если нет, он отпустит левую вилку.
            if self.right.acquire():
                print('Philosopher {0} starts eating'.format(self.name))
                sleep(randint(*Philosopher.EATING))
                print('Philosopher {0} finishes eating'.format(self.name))
                self.right.release()
            self.left.release()

    def run(self):
        """Run the philosopher`s process."""
        while True:
            print('Philosopher {0} is thinking'.format(self.name))
            sleep(randint(*Philosopher.THINKING))
            print('Philosopher {0} wants to eat'.format(self.name))
            self.eating()


if __name__ == '__main__':
    FORKS = [Lock() for _ in range(6)]
    PHILOSOPHERS = [Philosopher(str(num), FORKS[num-1], FORKS[num]) for num in range(6)]
    for ph in PHILOSOPHERS:
        ph.start()
