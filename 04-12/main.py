"""Философы, которые едят по очереди."""
from multiprocessing import Process, Lock
from time import sleep
from random import randint


numbs = 7
sticks, phls = [], []
for _ in range(numbs):
    sticks.append(Lock())
    phls.append(0)


def phl(num: int, fst: Lock, snd: Lock, palochki):
    """
    Функция философа для передачи в процесс.

    Args:
        num(int): номер философа
        fst(Lock): палочка, которую философ берёт первой
        snd(Lock): палочка, которую философ берёт второй
    """
    while True:
        print("Философ {0} собирается брать палочки для еды".format(num))
        fst.acquire()
        print("Философ {0} взял {1} палочку".format(num, palochki[0]))
        snd.acquire()
        print("Философ {0} взял {1} палочку".format(num, palochki[1]))
        print("Филосов {0} ест".format(num))
        sleep(randint(0, 3))
        print("Философ {0} поел и размышляет".format(num))
        fst.release()
        snd.release()
        sleep(randint(0, 3))


if __name__ == '__main__':
    for i in range(0, numbs, 2):
        phls[i] = Process(target=phl, args=(i, sticks[i - 1], sticks[i], ("левую", "правую")))
        phls[i].start()
    for i in range(1, numbs, 2):
        phls[i] = Process(target=phl, args=(i, sticks[i], sticks[i - 1], ("правую", "левую")))
        phls[i].start()
