"""Dining philosophers."""
from multiprocessing import Process, Lock
from time import sleep
from random import randint
import os


class Philosopher(Process):
    """Class of phisopher. Like all philosophers, he can only eat and think."""

    EATING_INTERVAL = (2, 3)
    THINKING_INTERVAL = (4, 6)
    TIMEOUT_ACQUIRE = 0.00001
    LEFT_RIGHT = [0, 1]
    RIGHT_LEFT = [1, 0]

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
        print('Philosopher {0} has finished thinking and wants to eat'.format(self.name))

    def check_pid(self, pid):
        """Check if process is alive.

        Args:
            pid (int): process id.

        Returns:
            _bool_: true if process is alive else false.
        """
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        return True

    def cognitive(self, check, chopsticks):
        """Method with main logic.

        Args:
            check (bool): checks if the process is alive.
            chopsticks (list): list of chopsticks.
        """
        for choice1, choice2 in (Philosopher.LEFT_RIGHT, Philosopher.RIGHT_LEFT):
            if chopsticks[choice1].acquire(timeout=Philosopher.TIMEOUT_ACQUIRE) and check:
                if chopsticks[choice2].acquire(timeout=Philosopher.TIMEOUT_ACQUIRE) and check:
                    self.eating()
                else:
                    chopsticks[choice1].release()

    def run(self):
        """Main method of philosopher."""
        while True:
            check = self.check_pid(os.getpid())
            chopsticks = self.r_lock, self.l_lock
            self.cognitive(check, chopsticks)


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
