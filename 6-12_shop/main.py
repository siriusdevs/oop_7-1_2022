"""Парикмахер стрижёт приходящих клиентов и спит в промежутках."""
from multiprocessing import Queue, Process, Event
from random import randint
from time import sleep
from sys import exit


class Hairdresser:
    """Парикмахер."""

    def __init__(self) -> None:
        """Инициализация барбера."""
        self.status = 0

    def go_sleep(self):
        """Барбер идёт спать, потому что нет клиентов."""
        print("Barber goes sleeping")
        if not wakeup.wait(timeout=20):
            print("Barbershop closes")
            exit()

    def take_client(self):
        """Барбер идет смотреть, есть ли клиенты. Если да, то начинает работать."""
        if que.empty():
            self.status = 0
            self.go_sleep()
        else:
            wakeup.clear()
            self.status = 1
            client = que.get()
            print("Client {0} is being trimmed".format(client.name))
            sleep(randint(2, 5))
            print("Client {0} is trimmed".format(client.name))


class Client:
    """Клиент, который приходит стричься."""

    def __init__(self, name) -> None:
        """
        Инициализация клиента.

        Args:
            name(int): номер клиента
        """
        self.name = name

    def came(self, dresser):
        """
        Клиент приходит в парикмахерсую.

        Args:
            dresser(obj): парикмахер
        """
        print("Client {0} came".format(self.name))
        if que.full():
            print("Client {0} sees ful queue and goes away".format(self.name))
        elif dresser.status == 0:
            que.put(Client(self.name))
            print("Client {0} wakes up the barber".format(self.name))
            wakeup.set()
        else:
            que.put(Client(self.name))
            print("Client {0} sits into the queue".format(self.name))


def barbershop():
    """Функция запуска парикмахераской."""
    while True:
        hairdresser.take_client()


def clients_are_coming(n):
    """
    Функция прихода новых клиентов.

    Args:
        n(int): рассчётное количество клиентов
    """
    num = -1
    while num < n:
        num += 1
        Client(num).came(hairdresser)
        sleep(randint(4, 7))


que = Queue(maxsize=4)
wakeup = Event()
hairdresser = Hairdresser()

Process(target=barbershop).start()
clients_are_coming(5)
