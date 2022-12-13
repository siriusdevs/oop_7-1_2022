"""Imitation of a working barbershop."""
from multiprocessing import Process, Queue, Lock, Event
from random import randint
from time import sleep
from faker import Faker


class Client:
    """Representation of a client."""

    def __init__(self, name: str) -> None:
        """Initialize a client.

        Args:
            name : str - name of a client
        """
        self.name = name


class Barber:
    """Representation of a barber."""

    TIMEOUT = 10
    WORK_TIME = (2, 5)

    def __init__(self) -> None:
        """Initialize a barber."""
        self._client_came = Event()

    def wait_client(self) -> bool:
        """Wait for clients."""
        print('Barber is waiting for a client.')
        return self._client_came.wait(timeout=Barber.TIMEOUT)

    def call(self) -> None:
        """Call the barber."""
        self._client_came.set()

    def cut(self, client: Client) -> None:
        """Barber cuts client`s hair.

        Args:
            client : Client - client whos hair are being cut
        """
        print('Barber welcomes {0}'.format(client.name))
        self._client_came.clear()
        sleep(randint(*Barber.WORK_TIME))
        print('Client {0} is done'.format(client.name))


class Barbershop:
    """Representation of a barbershop."""

    def __init__(self, q_size: int) -> None:
        """Initialize a barbershop.

        Args:
            q_size : int - size of the queue
        """
        self._queue = Queue(maxsize=q_size)
        self._worker = Barber()
        self._process = Process(target=self.work)
        self.mutex = Lock()

    def open(self) -> None:
        """Open barbershop."""
        print('Barbershop is opened.')
        self._process.start()

    def close(self) -> None:
        """Close barbershop."""
        print('Barbershop is closed.')

    def work(self) -> None:
        """Representation of a working barbershop."""
        while True:
            self.mutex.acquire()
            if self._queue.empty():
                self.mutex.release()
                work_result = self._worker.wait_client()
                if not work_result:
                    self.close()
                    break
            else:
                self.mutex.release()
                client = self._queue.get()
                self._worker.cut(client)

    def enter(self, client: Client) -> None:
        """Client entering a barbershop.

        Args:
            client : Client - a client who entered a barbershop
        """
        with self.mutex:
            print('Client {0} has entered the barbershop'.format(client.name))
            if self._queue.full():
                print('Client {0} sees full queue and leaves'.format(client.name))
            else:
                print('Client {0} wants to do a haircut'.format(client.name))
                self._queue.put(client)
                self._worker.call()


QUEUE_SIZE = 2
ENTER_INTERVAL = (1, 3)
NUMBER_OF_CLIENTS = 10
if __name__ == '__main__':
    faker = Faker()
    names = [faker.name() for _ in range(NUMBER_OF_CLIENTS)]
    clients = [Client(name) for name in names]
    barbershop = Barbershop(QUEUE_SIZE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*ENTER_INTERVAL))
