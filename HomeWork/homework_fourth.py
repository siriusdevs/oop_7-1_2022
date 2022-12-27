"""The classes for barbershop."""
from multiprocessing import Process, Queue, Event, Lock
from random import randint
from time import sleep
from faker import Faker


SIZE_QUEUE = 2
TIME_INTERVAL = (2, 4)
PEOPLE = [Faker().name() for name in range(10)]


class Client:
    """Class of client."""

    def __init__(self, name: str) -> None:
        """The function initializes the clients.

        Args:
            name: str - client_reader_name.
        """
        self.name = name

    def is_valid(self):
        """Function  checks client parameters.

        Returns:
            bool - if parameters type is str or bool.
        """
        return all([isinstance(self.name, str) and isinstance(self.action, type(Client.ACTIONS))])


class Barber:
    """Class barber."""

    TIMEOUT = 10
    WORK_INTERVAL = (4, 6)

    def __init__(self) -> None:
        """Function checks barber."""
        self.client_came = Event()

    def work(self):
        """Function sends barber sleeping.

        Returns:
            bool - if client steel waiting.
        """
        print("\033[36mПарикмахер уходит спать.\033[0m")
        return self.client_came.wait(timeout=Barber.TIMEOUT)

    def call(self):
        """Function calls barber."""
        self.client_came.set()

    def cut(self, client_name: str):
        """Function  imitates work of barber.

        Args:
            client_name: Client - client in barbershop.
        """
        print('\033[35mПарикмахер стрежёт\033[0m {0}.'.format(client_name))

    def greet(self, client: Client):
        """Function  starts barber work.

        Args:
            client: Client - client in barbershop.
        """
        self.client_came.clear()
        self.cut(client.name)
        sleep(randint(*self.WORK_INTERVAL))
        print("Клиент {0} \033[37mуходит.\033[0m".format(client.name))


class Barbershop:
    """Class of barbershop."""

    def __init__(self, queue_size: int) -> None:
        """Function  initialises barbershop parameters.

        Args:
            queue_size: int - size of queue.
        """
        self.queue_size = queue_size
        self.queue_client = Queue(maxsize=queue_size)
        self.barber = Barber()
        self.process_work = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """Function  opens barbershop."""
        print("\033[92mПарикмахерская открывается\033[0m, размер очереди - {0}.".format(self.queue_size))
        self.process_work.start()

    def close(self):
        """Function  closes barbershop."""
        print("\033[91mПарикмахерская закрывается.\033[0m")

    def work(self):
        """Function  controls queue."""
        while True:
            self.mutex.acquire()
            if self.queue_client.empty():
                self.mutex.release()
                work_result = self.barber.work()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.queue_client.get()
                self.barber.greet(client)

    def enter(self, client: Client):
        """Function controls enters of clients.

        Args:
            client: Client - object of class Client.
        """
        with self.mutex:
            print("Клиент {0} \033[32mзаходит в парикмахерскую.\033[0m".format(client.name))
            if self.queue_client.full():
                print("Клиент {0} \033[101mувидел полную очередь и ушёл.\033[0m".format(client.name))
            else:
                self.queue_client.put(client)
                self.barber.call()


if __name__ == '__main__':
    clients = [Client(human) for human in PEOPLE]
    queue = Barbershop(SIZE_QUEUE)
    queue.open()
    for client in clients:
        queue.enter(client)
        sleep(randint(*TIME_INTERVAL))
