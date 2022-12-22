from multiprocessing import Process, Lock, Event
from time import sleep
import random
forks = 5
philosophers = 5

forks_lock = [Lock() for n in range(forks)]


def philosophers_dinner(right_fork, left_fork, philosopher):
    while True:

        first_fork = min(right_fork, left_fork)
        second_fork = max(right_fork, left_fork)
        forks_lock[first_fork].acquire()

        print(f'Философ {philosopher} takes right fork')

        forks_lock[second_fork].acquire()
        print(f'Философ {philosopher} takes second fork')

        print(f'Философ {philosopher} is eating')
        sleep(random.randint(4, 6))
        forks_lock[second_fork].release()
        print(f'Философ {philosopher} returns right fork')
        forks_lock[first_fork].release()
        print(f'Философ {philosopher} returns left fork')


action = Event()

for philosopher in range(philosophers):
    right_fork = philosopher
    left_fork = (philosopher + 1) % philosophers
    pr = Process(target=philosophers_dinner, args=(right_fork, left_fork, philosopher))
    pr.start()
