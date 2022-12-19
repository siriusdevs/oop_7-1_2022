from multiprocessing import Process, Lock
import time
import random


class Philosopher(Process):

    def __init__(self, phi, locks):
        super().__init__()
        self.phi = phi
        self.locks = locks

    def run(self):
        time.sleep(random.randint(1, 3))
        print(f"Philosopher {self.phi} is hungry and want to eat")
        self.start_eat()

    def start_eat(self):
        left = self.locks[self.phi - 1]
        right = self.locks[self.phi % 5]

        while True:
            result = left.acquire()
            if right.acquire():
                left.release()
            else:
                result = right.acquire()
                print(f"Philosopher {self.phi} is eating")
                time.sleep(random.randint(1, 3))
                right.release()
                left.release()
                print(f"Philosopher {self.phi} is finished")


locks = [Lock() for _ in range(5)]
phils = [Philosopher(1, locks)]

procs = [
    Process(target=Philosopher.run()),
    Process(target=Philosopher, args=(2, locks)),
    Process(target=Philosopher, args=(3, locks)),
    Process(target=Philosopher, args=(4, locks)),
    Process(target=Philosopher, args=(5, locks)),
]

if __name__ == '__main__':
    for proc in procs:
        proc.start()
