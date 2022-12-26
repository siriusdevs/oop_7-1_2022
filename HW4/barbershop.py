"""Module simulating the work of a barbershop in the center of St. Petersburg."""
from multiprocessing import Process, Queue, Lock, Event
from random import randint, choice
from time import sleep

NAMES_CLIENTS = ['Пожилой Гиббон', 'Гиперактивный Орангутан', 'Богатое Шимпанзе', 'Бешеная Макака']

class Client:
    """The class that creates the Client."""
    ACTIONS = "HAIRCUT"
    def __init__(self, name: str, action: str = "HAIRCUT"):
        """Initializing attributes for the client.

        Args:
            name (str): Client name.
            action (str, optional): client actions. Defaults to "HAIRCUT".
        """
        self.name = str(choice(NAMES_CLIENTS))
        self.name = name
        self.action = action

class Barber:
    """The class that creates the Barber."""
    TIMEOUT = 20
    WORK_INTERVAL = (1, 3)
    def __init__(self):
        """Initializing attributes for the Barber"""
        self.__client_came = Event()

    def sleep(self):
        """The hairdresser sleeps while there are no clients.

        Returns:
            bool: if the client comes.
        """
        print("Барбер спит")
        return self.__client_came.wait(timeout=Barber.TIMEOUT)

    def call(self):
        """Time to wake up, Barber."""
        self.__client_came.set()

    def greet(self, client: Client):
        """Barber greets clients.

        Args:
            client (Client): client of barbershop from class Client.
        """
        self.__client_came.clear()
        print("Барбер приветствует клиента: {0}".format(client.name))
        if client.action == "HAIRCUT":
            self.haircut(client)
            sleep(randint(*Barber.WORK_INTERVAL))

    def haircut(self, client: Client):
        """Client haircut process.

        Args:
            client (Client): client of barbershop from class Client.
        """
        print('Стрижка клиента {0} началась'.format(client.name))
        sleep(randint(*Barber.WORK_INTERVAL))
        print('Стрижка клиента {0} завершена'.format(client.name))


class Barbershop:
    """A class that combines barber and client under one roof."""
    def __init__(self, queue_size: int):
        """Barbershop Initialization.

        Args:
            queue_size (int): size of queue.
        """
        self.queue_size = queue_size
        self.__queue = Queue(maxsize=queue_size)
        self.__worker = Barber()
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """Opening the barbershop when you start the program."""
        print('Барбершоп "три обезьяны" открывается, доступно {} мест(а) в очереди'.format(self.queue_size))
        self.__process.start()

    def close(self):
        """Closing the barbershop in the absence of customers.

        Raises:
            SystemExit: correct program closure, stolen from stackoverflow.
        """
        print('Барбершоп закрывается')
        raise SystemExit

    def work(self):
        """The method that ensures the operation of the barbershop."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result = self.__worker.sleep()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client):
        """A method for clients to enter a barbershop.

        Args:
            client (Client): client of barbershop from class Client.
        """
        with self.mutex:
            print("Клиент {0} пришёл в барбершоп".format(client.name))
            if self.__queue.full():
                print("Клиент {0} пошлёпал домой - мест нет".format(client.name))
            else:
                self.__queue.put(client)
                self.__worker.call()


SIZE_QUEUE = 5
INTERVAL = (1, 2)

if __name__ == '__main__':
    clients = [Client(human) for human in NAMES_CLIENTS]
    barbershop = Barbershop(SIZE_QUEUE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*INTERVAL))
