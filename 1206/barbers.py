"""File with classes for barbershop."""
from multiprocessing import Process, Queue, Event, Lock
from random import randint
from time import sleep


class Client:
    """Class of client."""

    ACTIONS = "CUT"

    def __init__(self, name: str, action: str = 'CUT') -> None:
        """Function initialises clients.

        Args:
            name: str - reader_name of client.
            action: str - barber flag.
        """
        self.name = name
        self.action = action

    def is_valid(self):
        """Function which checks client parameters.

        Returns:
            bool - if parameters type is str.
        """
        return all([isinstance(parameter, str) for parameter in self.__dict__.values()])\
            and self.action in Client.ACTIONS


class Barber:
    """Class which imitates barber moves."""

    TIMEOUT = 10
    WORK_INTERVAL = (2, 4)

    def __init__(self) -> None:
        """Function which checks barber."""
        self.__client_came = Event()

    def work(self):
        """Function which sends barber sleeping.

        Returns:
            bool - if client steel waiting.
        """
        print("Barber goes sleeping")
        return self.__client_came.wait(timeout=Barber.TIMEOUT)

    def call(self):
        """Function which calls barber."""
        self.__client_came.set()

    def cut(self, client: Client):
        """Function which imitates work of barber.

        Args:
            client: Client - client in barbershop.
        """
        print('Barber is cutting {0}'.format(client.name))

    def greet(self, client: Client):
        """Function which starts barber work.

        Args:
            client: Client - client in barbershop.
        """
        self.__client_came.clear()
        if client.action == "CUT":
            self.cut(client)
            sleep(randint(1, 3))
        print("Client {0} is gone".format(client.name))


class Barbershop:
    """Class of barbershop."""

    def __init__(self, q_size: int) -> None:
        """Function which initialises barbershop parameters.

        Args:
            q_size: int - size of queue.
        """
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Barber()
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """Function which opens barbershop."""
        print("Barbershop is open with queue size of {0}".format(self.q_size))
        self.__process.start()

    def close(self):
        """Function which closes barbershop."""
        print("Barbershop closes")

    def work(self):
        """Function which controls queue."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result = self.__worker.work()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client):
        """Function which controls enters of clients.

        Args:
            client: Client - object of class Client.
        """
        with self.mutex:
            print("Client {0} has entered a barbershop".format(client.name))
            if self.__queue.full():
                print("Client {0} sees full queue and leaves".format(client.name))
            else:
                self.__queue.put(client)
                self.__worker.call()


SIZE_QUEUE = 2
ENTER_TIME_INTERVAL = (3, 3)

PEOPLE = [
    'Viktor',
    'Michelin',
    'Kino',
    'Watermelon',
    'Alice'
]


if __name__ == '__main__':
    clients = [Client(human) for human in PEOPLE]
    library = Barbershop(SIZE_QUEUE)
    library.open()
    for client in clients:
        library.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
