"""File with function - philosophers dinner."""
from multiprocessing import Process, Lock
import time
import random


sticks = Lock()
number_of_loops = 10
people_num = int(input())


def dinner(num, lock):
    """Function which prints action of philosophers.

    Args:
        num: int - number(name) of philosopher.
        lock: Lock - class Lock for managing philosophers sticks.
    """
    if lock.acquire(timeout=3):
        print('Филосов #{0} - начинает думать'.format(num - 1 if num - 1 > 0 else num))
        print('Филосов #{0} - ест'.format(num))
        time.sleep(random.randint(1, 4))
        print('Филосов #{0} - начинает думать'.format(num))
    else:
        lock.release()
        print('Филосов #{0} - думает'.format(num))
        time.sleep(random.randint(1, 4))
        print('Филосов #{0} - начинает есть'.format(num))


if __name__ == '__main__':
    while number_of_loops != 0:
        procs = []
        if people_num >= 2:
            for philosopher in range(people_num):
                proc = Process(target=dinner, args=(philosopher, sticks))
                procs.append(proc)
                proc.start()
            for proc_stop in procs:
                proc_stop.join()
            number_of_loops -= 1
        else:
            print('Dead')
            break
