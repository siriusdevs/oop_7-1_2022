"""This file for Barbershop and Client classes."""
from multiprocessing import Event, Queue, Process, Lock
from random import randint
from time import sleep


class Client(object):
    """Class client create client."""

    def __init__(self, name: str) -> None:
        """
        Creates a client.
        Args:
            name: str - client name.
        """
        self.name = name

    def is_valid(self) -> bool:
        """
        Checks if the client name is correct.
        Returns:
            bool: if name is a string or not.
        """
        return isinstance(self.name, str)

    def __str__(self) -> str:
        """
        Return the object as a string.
        Returns:
            str: a message that client 'name' gets a haircut.
        """
        return 'Client {0} gets a haircut'.format(self.name)


class Barber(object):
    """Class barber create barber."""

    timeout = 15
    work_interval = (1, 4)

    def __init__(self) -> None:
        """Creates a barber."""
        self.__client_came = Event()

    def have_rest(self) -> bool:
        """
        The hairdresser rests while there are no clients.
        Returns:
            bool: if the client comes.
        """
        print('Barber have rest on chair')
        return self.__client_came.wait(timeout=Barber.timeout)

    def call(self) -> None:
        """Wakes up the barber when the client arrives."""
        self.__client_came.set()

    def worked(self, client: Client) -> None:
        """
        Barber's working method.
        Args:
            client: Client - served client.
        """
        sleep(randint(*Barber.work_interval))
        print('Barber work on a client {0}'.format(client.name))

    def greet(self, client: Client):
        """
        Barber welcomes the client in the queue.
        Args:
            client: Client - the client of barbershop
        """
        print('Barber greets client {0}'.format(client.name))
        self.__client_came.clear()
        self.worked(client)
        print('Client {0} is done'.format(client.name))


class Barbershop(object):
    """The class creates a barbershop."""

    def __init__(self, q_size: int) -> None:
        """
        Creates barbershop.
        Args:
            q_size: int - the queue max size.
        """
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Barber()
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self) -> None:
        """Barbershop opens."""
        print('Barbershop opens with queue size of {0}'.format(self.q_size))
        self.__process.start()

    def close(self) -> None:
        """Barbershop closes."""
        print('Barbershop closes')

    def work(self) -> None:
        """Work when the client comes."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result = self.__worker.have_rest()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client) -> None:
        """
        Adds a client to the queue.
        Args:
            client: Client - client was entered to barbershop.
        """
        with self.mutex:
            print('Client {0} has entered to the barbershop'.format(client.name))
            if self.__queue.full():
                print('Client {0} sees full queue, leaves'.format(client.name))
            else:
                self.__queue.put(client)
                self.__worker.call()


CLIENTS = ['Nestrov', 'Nazaroff', 'Prohodko', 'Orehov', 'Filatov', 'Bezborodov']

SIZE_QUEUE = 3
ENTER_TIME_INTERVAL = (1, 10)

if __name__ == "__main__":
    clients = [Client(str(cl)) for cl in CLIENTS]
    barbershop = Barbershop(SIZE_QUEUE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
