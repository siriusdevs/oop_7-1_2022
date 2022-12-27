"""Main for philosopher."""
from multiprocessing import Lock
from philosophers import Philosopher

PHILOSOPHERS = 6
if __name__ == '__main__':
    chopsticks = [Lock() for _ in range(PHILOSOPHERS)]
    for num, name in enumerate(range(PHILOSOPHERS)):
        left = chopsticks[num - 1]
        right = chopsticks[num]
        Philosopher("Philosopher {0}".format(name), chopstick_left=left, chopstick_right=right).start()
