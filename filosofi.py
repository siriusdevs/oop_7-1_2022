"""Dining philosophers."""
from multiprocessing import Process, Lock
from time import sleep
from random import randint


class Philosopher(Process):
    """Class of phisopher. Like all philosophers, he can only eat and think."""

    EATING_INTERVAL = (2, 3)
    THINKING_INTERVAL = (4, 6)
    TIMEOUT_ACQUIRE = 0.0001

    def __init__(self, name, l_lock, r_lock):
        """Initialization of philosopher.

        Args:
            name (str): name of phisopher
            l_lock (Lock): left chopstick
            r_lock (Lock): right chopstick
        """
        super().__init__(name=name)
        self.l_lock = l_lock
        self.r_lock = r_lock

    def eating(self):
        """Method that reflects the actions of a philosopher."""
        print('Philosopher {0} is eating'.format(self.name))
        sleep(randint(*Philosopher.EATING_INTERVAL))
        self.r_lock.release()
        self.l_lock.release()
        print('Philosopher {0} is thinking'.format(self.name))
        sleep(randint(*Philosopher.THINKING_INTERVAL))

    def run(self):
        """Main method of philosopher."""
        while True:
            if self.l_lock.acquire(timeout=Philosopher.TIMEOUT_ACQUIRE):
                if self.r_lock.acquire(timeout=Philosopher.TIMEOUT_ACQUIRE):
                    self.eating()
                else:
                    self.l_lock.release()


class Dinner:
    """Class of dinner for philosophers."""

    def __init__(self, chopsticks):
        """Start dinner.

        Args:
            chopsticks (list): list of chopsticks.
        """
        self.chopsticks = chopsticks
        for num in range(5):
            Philosopher(str(num), self.chopsticks[num - 1], self.chopsticks[num]).start()


if __name__ == '__main__':
    chopsticks = []
    for _ in range(5):
        lock = Lock()
        chopsticks.append(lock)
    Dinner(chopsticks)
