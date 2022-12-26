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

    WAIT = 7
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
        left_free = self.left.acquire(timeout=Philosopher.WAIT)
        if left_free:
            print('Philosopher {0} took left fork'.format(self.name))
        right_free = self.right.acquire(timeout=Philosopher.WAIT)
        if right_free:
            print('Philosopher {0} took right fork'.format(self.name))
        if left_free and right_free:
            print('Philosopher {0} starts eating'.format(self.name))
            sleep(randint(*Philosopher.EATING))
            print('Philosopher {0} finishes eating'.format(self.name))
            self.left.release()
            self.right.release()

    def run(self):
        """Run the philosopher`s process."""
        while True:
            print('Philosopher {0} is thinking'.format(self.name))
            sleep(randint(*Philosopher.THINKING))
            print('Philosopher {0} wants to eat'.format(self.name))
            self.eating()


if __name__ == '__main__':
    FORKS = [Lock() for _ in range(6)]
    PHILOSOPHERS = [Philosopher(str(num), FORKS[num % 6], FORKS[(num + 1) % 6]) for num in range(6)]
    for ph in PHILOSOPHERS:
        ph.start()
