"""Философы, которые едят по очереди."""
from multiprocessing import Process, Lock
from time import sleep
from random import randint


def phl(num: int, fst: Lock, snd: Lock):
    """
    Функция философа для передачи в процесс.

    Args:
        num(int): номер философа
        fst(Lock): палочка, которую философ берёт первой
        snd(Lock): палочка, которую философ берёт второй
    """
    while True:
        print("Философ {0} собирается брать палочки для еды".format(num))
        if fst.acquire(timeout=randint(*TIMEOUT)):
            print("Философ {0} взял левую палочку".format(num))
            if snd.acquire(timeout=randint(*TIMEOUT)):
                print("Философ {0} взял правую палочку".format(num))
                print("Филосов {0} ест".format(num))
                sleep(randint(*EATING_TIME))
                print("Философ {0} поел и размышляет".format(num))
                fst.release()
                snd.release()
                sleep(randint(*THINKING_TIME))
            else:
                fst.release()


if __name__ == '__main__':
    NUMBS = 7
    TIMEOUT = (1, 2)
    EATING_TIME = (3, 4)
    THINKING_TIME = (3, 4)
    sticks, phls = [], []
    for _ in range(NUMBS):
        sticks.append(Lock())
        phls.append(0)
    for i in range(NUMBS):
        phls[i] = Process(target=phl, args=(i, sticks[i - 1], sticks[i]))
        phls[i].start()
