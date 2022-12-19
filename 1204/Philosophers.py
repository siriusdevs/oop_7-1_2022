import datetime
from multiprocessing import Process, Lock, Event
from random import randint

from time import sleep
PHILOSOPHERS = 6


class Philosopher(Process):
    EATING_TIME = (1, 3)
    FAMINE_TIME = (1, 3)
    THINKING_TIME = (3,3)

    def __init__(self, name: str, right: Lock, left: Lock):
        super().__init__(name=name)
        self.name = name
        self.chopstick_left = right
        self.chopstick_right = left

    def out(self):
        print("{} start eating".format(self.name))
        sleep(randint(*Philosopher.EATING_TIME))
        print("{} stop eating and start thinking".format(self.name))
        self.chopstick_right.release()
        self.chopstick_left.release()
        # self.hunger.set()
        sleep(randint(*Philosopher.THINKING_TIME))
        print("{} stop thinking and want to eating".format(self.name))

    def run(self) -> None:
        while True:
            if self.chopstick_left.acquire(timeout=0.001):
                if self.chopstick_right.acquire(timeout=0.001):
                    self.out()
                else:
                    try:
                        self.chopstick_left.release()
                    except ValueError:
                        pass
            else:
                if self.chopstick_right.acquire(timeout=0.001):
                    if self.chopstick_left.acquire(timeout=0.001):
                        self.out()
                    else:
                        self.chopstick_right.release()


if __name__ == '__main__':
    sticks = [Lock() for _ in range(PHILOSOPHERS)]

    for i in range(PHILOSOPHERS):
        if i == 0:
            Philosopher("Philosopher {}".format(i), right=sticks[-1], left=sticks[0]).start()
        else:
            Philosopher("Philosopher {}".format(i), right=sticks[i - 1], left=sticks[i]).start()
