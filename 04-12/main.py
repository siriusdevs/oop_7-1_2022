"""Философы, которые едят по очереди."""
from multiprocessing import Process, Event, Lock
from time import sleep
from random import randint


numbs = 7
events, sticks, phls = [], [], []
for _ in range(numbs):
    events.append(Event())
    sticks.append(Lock())
    phls.append(0)


def phl(num: int, quant: int):
    """
    Функция философа для передачи в процесс.

    Args:
        num(int): номер философа
        quant(int): количество философов
    """
    events[num].set()
    while True:
        events[num].clear()
        if events[num - 1].is_set() and events[(num + 1) % quant].is_set():
            print("Филосов {0} собирается брать палочки для еды".format(num))
            sticks[num - 1].acquire()
            print("Филосов {0} взял левую палочку".format(num))
            sticks[num].acquire()
            print("Филосов {0} взял правую палочку".format(num))
            events[num].set()
            print("Филосов {0} ест".format(num))
            sleep(randint(1, 2))
            print("Филосов {0} поел и размышляет".format(num))
            sticks[num - 1].release()
            sticks[num].release()
            sleep(randint(1, 2))
        else:
            events[num].set()
            events[num - 1].wait()
            events[(num + 1) % quant].wait()


if __name__ == '__main__':
    for i in range(numbs):
        phls[i] = Process(target=phl, args=(i, numbs))
        phls[i].start()
