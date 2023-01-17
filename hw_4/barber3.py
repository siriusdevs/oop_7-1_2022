"""Barbershop."""

from multiprocessing import Process, Event, Queue, Lock
from time import sleep
from random import randint


class NotValidName(Exception):
    """This exception returns if name isn't correct."""

    def __str__(self):
        """This magic method returns string of error."""
        return 'Invalid name'


class Client:
    """Barbershop client class. He only has a name and nothing else."""

    def __init__(self, name: str):
        """Client initialization. His name is checked for correctness.

        Args:
            name (str): name of client.

        Raises:
            NotValidName: if name isn't correct.
        """
        self.name = name
        if not self.is_valid():
            raise NotValidName

    def is_valid(self):
        """This method checks the name for correctness."""
        return isinstance(self.name, str)


class Barber():
    """Barber class. He knows how to work and sleep."""

    TIMEOUT = 10
    WORK_INTERVAL = (1, 3)

    def __init__(self, name: str):
        """Barber init. CHecks the name for correctness and creates an event.

        Args:
            name (str): name of barber.

        Raises:
            NotValidName: if name isn't correct.
        """
        self.name = name
        self.client_came = Event()
        self.sleeping = 0
        if not self.is_valid():
            raise NotValidName

    def is_valid(self):
        """This method checks the name for correctness."""
        return isinstance(self.name, str)

    def work(self):
        """Method of status barber.

        Returns:
            bool: status of barber.
        """
        print('Barber {0} is sleeping'.format(self.name))
        return self.client_came.wait(timeout=Barber.TIMEOUT)

    def call(self):
        """This method changes the state of the event."""
        self.client_came.set()

    def cutting(self, client: Client):
        """This method is responsible for barber work with client.

        Args:
            client (Client): barber client.
        """
        print('Barber {0} is cutting {1}'.format(self.name, client.name))
        sleep(randint(*Barber.WORK_INTERVAL))
        print('{0} is done by Barber {1}'.format(client.name, self.name))
        self.client_came.clear()


class Barbershop:
    """Barbershop class. It works with barber process."""

    def __init__(self, q_size: int):
        """Barbershop initialization.

        Args:
            q_size (int): queue size
        """
        self.q_size = q_size
        self.queue = Queue(maxsize=q_size)
        self.worker = Barber('Aboba')
        self.process = Process(target=self.work)
        self.mutex = Lock()

    def close(self):
        """This method displays barbershop closing."""
        print('Barbershop closed. Good luck.')

    def open(self):
        """This method displays barbershop opening and barber launches."""
        print('Barbershop opens')
        self.process.start()

    def barber_left(self, barber: Barber):
        """This method is responsible for barber output.

        Args:
            barber (Barber): barber who output.
        """
        print('{0} is left of barbershop'.format(barber.name))

    def work(self):
        """This method is responsible for the work of the barbershop."""
        while True:
            self.mutex.acquire()
            if self.queue.empty():
                self.mutex.release()
                if not self.worker.work():
                    self.barber_left(self.worker)
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self.queue.get()
                self.worker.cutting(client)

    def enter(self, client: Client):
        """This method is responsible for entering the client into the barbershop.

        Args:
            client (Client): client who came.
        """
        with self.mutex:
            if self.queue.full():
                print('{0} sees a full queue and goes somewhere'.format(client.name))

            else:
                self.queue.put(client)
                self.worker.call()


COUNT_OF_CLIENTS = 10
SIZE_OF_QUEUE = 4


if __name__ == "__main__":
    bp = Barbershop(SIZE_OF_QUEUE)
    bp.open()
    for num in range(COUNT_OF_CLIENTS):
        sleep(1)
        bp.enter(Client(str(num)))
