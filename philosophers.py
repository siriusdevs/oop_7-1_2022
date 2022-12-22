"""Problem of dinning philosophers."""
from multiprocessing import Process, Lock
from time import sleep
from random import randint


class Philosopher(Process):
    """Representation of a thinking and eating philosopher."""

    THINK_TIME = (2, 3)
    RUNNING = True
    WAIT_FORK = 5
    EAT_TIME = (1, 2)

    def __init__(self, name: str, left_fork: Lock, right_fork: Lock) -> None:
        """Inicialization of a philosopher.

        Args:
            name : str - name of a philosopher
            left_fork : Lock - fork from the left
            right_fork : Lock - fork from the right
        """
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def eat(self):
        """Philosopher eating."""
        fork_l, fork_r = self.left_fork, self.right_fork
        unlocked_l = fork_l.acquire(timeout=Philosopher.WAIT_FORK)
        if unlocked_l:
            print('Philosopher {0} took left fork'.format(self.name))
        unlocked_r = fork_r.acquire(timeout=Philosopher.WAIT_FORK)
        if unlocked_r:
            print('Philosopher {0} took right fork'.format(self.name))
        if unlocked_l and unlocked_r:
            print('Philosopher {0} starts eating'.format(self.name))
            sleep(randint(*Philosopher.EAT_TIME))
            print('Philosopher {0} is full now and ready to think'.format(self.name))
            fork_l.release()
            fork_r.release()
        else:
            print('Philosopher {0} didn`t get his forks and has to think again'.format(self.name))

    def run(self) -> None:
        """Start the philosopher."""
        while self.RUNNING:
            print('Philosopher {0} is thinking'.format(self.name))
            sleep(randint(*Philosopher.THINK_TIME))
            print('Philosopher {0} is starving from his deep thoughts'.format(self.name))
            self.eat()


if __name__ == '__main__':
    NUM_PHILOSOPHERS = 5
    FORKS = [Lock() for _ in range(NUM_PHILOSOPHERS)]
    PHILOSOPHERS = [Philosopher(str(num), FORKS[num % 5], FORKS[(num + 1) % 5]) for num in range(NUM_PHILOSOPHERS)]
    for philosopher in PHILOSOPHERS:
        philosopher.start()
