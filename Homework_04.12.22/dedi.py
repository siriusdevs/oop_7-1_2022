"""This file for philosopher class."""
from multiprocessing import Process, Lock
from time import sleep


class Philosophers(Process):
    """This class create Philosopher."""

    TIMEOUT_R_STICK = 2
    TIMEOUT_EAT = 1
    TIMEOUT_THINK = 2

    def __init__(self, name: str, l_chopstick: Lock(), r_chopstick: Lock()):
        """
        This function create process philosopher.
        Args:
            name: str - philosopher and process name.
            l_chopstick: Lock - left chopstick philosopher.
            r_chopstick: Lock - right chopstick philosopher.
        """
        super().__init__(name=name)
        self.name = name
        self.r_chopstick = r_chopstick
        self.l_chopstick = l_chopstick

    def run(self):
        """This function describes the process of a philosopher's lunch."""
        while True:
            if self.r_chopstick.acquire(timeout=self.TIMEOUT_R_STICK):  # Блокирует если можно
                print("Дед {0} взял правую палочку".format(self.name))
                if self.l_chopstick.acquire(timeout=self.TIMEOUT_R_STICK):
                    print("Дед {0} взял левую палочку".format(self.name))  # Блокирует если можно
                    print("Дед {0} начинает есть".format(self.name))
                    sleep(self.TIMEOUT_EAT)
                    print("Дед {0} закончил есть".format(self.name))
                    self.r_chopstick.release()  # Освобождение блокировки
                    self.l_chopstick.release()
                    print("Дед {0} Положил обе палочки".format(self.name))
                    self.think()
                    sleep(self.TIMEOUT_THINK)
                else:
                    self.r_chopstick.release()  # Освобождение блокировки
                    print("Дед {0} положил правую палочку".format(self.name))

    def think(self):
        """This function describes the process of thinking of a philosopher."""
        print("Дед {0} думает . . .".format(self.name))
        sleep(self.TIMEOUT_THINK)


PHILOSOPHERS = ['Nestrov', 'Nazaroff', 'Prohodko', 'Orehov', 'Filatov', 'Bezborodov']


if __name__ == "__main__":
    sticks = [Lock() for _ in range(len(PHILOSOPHERS))]
    for num_stick in range(len(PHILOSOPHERS)):
        Philosophers(PHILOSOPHERS[num_stick], sticks[num_stick - 1], sticks[num_stick]).start()
    sleep(1)
