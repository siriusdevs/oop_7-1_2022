from threading import Thread, Lock
from time import sleep
from random import randint


num_philosophers = 5


class Philosopher(Thread):

    EAT_TIME = (3, 4)
    TIMEOUT = 0.5
    TIME_TO_THINK = (3, 4)

    def __init__(self, name, right_fork, left_fork):
        super().__init__()
        self.name = name
        self.right_fork = right_fork
        self.left_fork = left_fork

    def run(self):
        while True:
            if self.right_fork.acquire(timeout=Philosopher.TIMEOUT):
                print(f'philosopher {self.name} takes right fork')
                if self.left_fork.acquire(timeout=Philosopher.TIMEOUT):
                    print(f'philosopher {self.name} takes left fork')
                    print(f'philosopher {self.name} is eating')
                    sleep(randint(*Philosopher.EAT_TIME))
                    self.left_fork.release()
                    self.right_fork.release()
                    print(f'philosopher {self.name} puts forks on the table')
                    print(f'philosopher {self.name} is thinking')
                    sleep(randint(*Philosopher.TIME_TO_THINK))
                    print(f'philosopher {self.name} wants to eat')
                else:
                    self.right_fork.release()


forks_lock = [Lock() for _ in range(num_philosophers)]
PHILOSOPHERS = []
for num in range(num_philosophers):
    right_fork = min(num, (num + 1) % num_philosophers)
    left_fork = max(num, (num + 1) % num_philosophers)
    PHILOSOPHERS.append(Philosopher(num, forks_lock[right_fork], forks_lock[left_fork]))


for philosopher in PHILOSOPHERS:
    philosopher.start()
