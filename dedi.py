from multiprocessing import Lock, Process
from random import randint
from time import sleep


class Philosopher(Process):

    THINK_TIME = (2, 3)
    WAIT_FORK = 5
    EAT_TIME = (1, 2)

    def __init__(self, name: str, left_stick: Lock, right_stick: Lock):
        super().__init__()
        self.name = name
        self.left_stick = left_stick
        self.right_stick = right_stick

    def eat(self):
        left_stick, right_stick = self.left_stick, self.right_stick
        unlock_l = left_stick.acquire(timeout=Philosopher.WAIT_FORK)
        unlock_r = right_stick.acquire(timeout=Philosopher.WAIT_FORK)
        if unlock_l:
            print(f"Philosopher {self.name} picked left stick")
        if unlock_r:
            print(f"Philosopher {self.name} picked right stick")
        if unlock_l and unlock_r:
            print(f"Philosopher {self.name} started eating")
            sleep(randint(*self.EAT_TIME))
            left_stick.release()
            right_stick.release()
            print(f"Phiosopher {self.name} finished eating")

    def run(self):
        while True:
            print(f"Philosopher {self.name} is thinking")
            sleep(randint(*Philosopher.THINK_TIME))
            print(f"Philosopher {self.name} want to eat")
            self.eat()


if __name__ == "__main__":
    NUM_PHILOSOPHERS = 50
    STICKS = [Lock() for _ in range(NUM_PHILOSOPHERS)]
    PHILOSOPHERS = [
        Philosopher(str(n), STICKS[n], STICKS[(n + 1) % NUM_PHILOSOPHERS])
        for n in range(NUM_PHILOSOPHERS)
    ]
    for philosopher in PHILOSOPHERS:
        philosopher.start()
        sleep(1)
