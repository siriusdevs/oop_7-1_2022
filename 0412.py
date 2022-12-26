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

    WAIT = 0.1
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

    def run(self):
        """Run the philosopher`s process."""
        while True:
            if self.left.acquire(timeout=Philosopher.WAIT):
                # если философ возьмет правую вилку, он зайдет в if и будет есть, если нет, он отпустит левую
                print('Philosopher {0} takes left fork'.format(self.name))
                if self.right.acquire(timeout=Philosopher.WAIT):
                    print('Philosopher {0} takes right fork'.format(self.name))
                    print('Philosopher {0} starts eating'.format(self.name))
                    sleep(randint(*Philosopher.EATING))
                    print('Philosopher {0} finishes eating'.format(self.name))
                    self.right.release()
                    self.left.release()
                    print('Philosopher {0} is thinking'.format(self.name))
                    sleep(randint(*Philosopher.THINKING))
                    print('Philosopher {0} wants to eat'.format(self.name))
                else:
                    self.left.release()


if __name__ == '__main__':
    FORKS = [Lock() for _ in range(6)]
    PHILOSOPHERS = [Philosopher(str(num), FORKS[num - 1], FORKS[num]) for num in range(6)]
    for ph in PHILOSOPHERS:
        ph.start()
