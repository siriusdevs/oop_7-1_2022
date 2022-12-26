"""Homework about philosopher's problem."""
from multiprocessing import Process, Lock

from time import sleep
PHILOSOPHERS = 6


class Philosopher(Process):
    """Representation of philosopher."""

    EATING_TIME = (1, 3)
    THINKING_TIME = (4, 6)
    TIMEOUT = 0.2

    def __init__(self, name: str, left: Lock, right: Lock):
        """Initialization method.

        Args:
            name (str): philosopher's reader_name.
            left (Lock): philosopher's left stick.
            right (Lock): philosopher's right stick.
        """
        super().__init__(name=name)
        self.name = name
        self.left = left
        self.right = right

    def eat(self):
        """Function where philosopher start eating."""
        print('{0} start eating.'.format(self.name))
        # sleep(randint(*Philosopher.EATING_TIME))
        sleep(0.1)
        print('{0} end eating and start thinking'.format(self.name))

    def run(self) -> None:
        """Function which checks acquire of sticks."""
        while True:
            if self.right.acquire(timeout=Philosopher.TIMEOUT):
                print('{0} got right stick'.format(self.name))
                if self.left.acquire(timeout=Philosopher.TIMEOUT):
                    print('{0} got left stick'.format(self.name))
                    self.eat()
                    self.right.release()
                    self.left.release()
                    # sleep(randint(*Philosopher.THINKING_TIME))
                    sleep(self.TIMEOUT)
                    print('{0} end thinking and hungry'.format(self.name))
                    print('{0} put down left stick'.format(self.name))
                    print('{0} put down right stick'.format(self.name))
                else:
                    self.right.release()
                    print('{0} put down right stick'.format(self.name))


if __name__ == '__main__':
    sticks = [Lock() for _ in range(PHILOSOPHERS)]

    for number_of_stick in range(PHILOSOPHERS):
        philosopher_name = 'Philosopher #{0}'.format(number_of_stick)
        stick_left = sticks[number_of_stick - 1]
        stick_right = sticks[number_of_stick]
        Philosopher(philosopher_name, stick_left, stick_right).start()
