"""The dinnig philosophers classes"""

from multiprocessing import Process, Lock
from time import sleep
from random import randint

WAIT = 10
THINKING = (5, 10)
EATING = (5, 10)
NUM_PHILOSOPH = 5


class Philosopher(Process):
    """The class of creating Philosophers"""

    def __init__(self, name: str, chop_left: Lock, chop_right: Lock) -> None:
        """Method  initialize class Philosopher.

        Args:
            name: name of philosoph
            chop_left: the left chopstick
            chop_right: the right chopstick
        """
        super().__init__()
        self.name = name
        self.chop_left = chop_left
        self.chop_right = chop_right

    def run(self):
        """Dinner start."""
        while True:
            if self.chop_left.acquire(timeout=WAIT):
                print('Филосов {0} взял левую палочку'.format(self.name))
                if self.chop_right.acquire(timeout=WAIT):
                    print('Филосов {0} взял правую палочку'.format(self.name))
                    print('Филосов {0} начал есть'.format(self.name))
                    sleep(randint(*EATING))
                    print('Филосов {0} закончил трапезу'.format(self.name))
                    self.chop_right.release()
                    self.chop_left.release()
                    print('Филосов {0} думает'.format(self.name))
                    sleep(randint(*THINKING))
                    print('Филосов {0} хочет поесть'.format(self.name))
                else:
                    self.chop_left.release()


if __name__ == '__main__':
    CHOPSTICK = [Lock() for _ in range(NUM_PHILOSOPH)]
    PHILOSOPH = [Philosopher(str(num), CHOPSTICK[num - 1], CHOPSTICK[num]) for num in range(NUM_PHILOSOPH)]
    for phi in PHILOSOPH:
        phi.start()
