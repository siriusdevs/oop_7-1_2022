"""Парикмахер стрижёт приходящих клиентов и спит в промежутках."""
from multiprocessing import Queue, Process, Event
from random import randint
from time import sleep
from sys import exit


class Hairdresser:
    """Парикмахер."""

    def go_sleep(self):
        """Барбер идёт спать, потому что нет клиентов."""
        print("Barber goes sleeping")
        if not wakeup.wait(timeout=TIMEOUT):
            print("Barbershop closes")
            exit()

    def take_client(self):
        """Барбер идет смотреть, есть ли клиенты. Если да, то начинает работать."""
        if que.empty():
            self.go_sleep()
        else:
            wakeup.clear()
            client = que.get()
            print("Client {0} is being trimmed".format(client.name))
            sleep(randint(*CUTTING_TIME))
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

    def came(self):
        """Клиент приходит в парикмахерсую."""
        print("Client {0} came".format(self.name))
        if que.full():
            print("Client {0} sees ful queue and goes away".format(self.name))
        else:
            que.put(Client(self.name))
            print("Client {0} sits into the queue".format(self.name))
            wakeup.set()


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
    for i in range(n):
        Client(i).came()
        sleep(randint(*CLIENT_COMING_TIME))


TIMEOUT = 20
CUTTING_TIME = (1, 3)
CLIENT_COMING_TIME = (4, 7)
CLIENTS_QUANTITY = 6
que = Queue(maxsize=1)
wakeup = Event()
hairdresser = Hairdresser()

Process(target=barbershop).start()
clients_are_coming(CLIENTS_QUANTITY)
