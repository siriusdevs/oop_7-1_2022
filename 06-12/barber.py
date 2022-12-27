"""Model philosophers."""

from multiprocessing import Process, Queue, Event, Lock
from random import randint
from time import sleep


class Client:
    """Class of client."""

    def __init__(self, name: str) -> None:
        """Create a client.

        Args:
            name: str - client's name.
        """
        self.name = name


class Barber:
    """Class of barber."""

    TIMEOUT = 10
    WORK_TIME = (2, 4)

    def __init__(self, name: str) -> None:
        """Create a barber.

        Args:
            name: str - the barber's name.
        """
        self.__client_came = Event()
        self.name = name

    def sleep(self):
        """Function which sends barber sleeping.

        Returns:
            bool - if client steel waiting.
        """
        print("Barber {0} goes sleeping".format(self.name))
        return self.__client_came.wait(timeout=Barber.TIMEOUT)

    def call(self):
        """Function which calls barber."""
        self.__client_came.set()

    def work(self, client: Client):
        """Function which starts barber work.

        Args:
            client: Client - client in barbershop.
        """
        self.__client_came.clear()
        print('Barber {0} is cutting {1}'.format(self.name, client.name))
        sleep(randint(*Barber.WORK_TIME))
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
        self.__worker = Barber("Viktor")
        self.__process = Process(target=self.work)
        self.mutex = Lock()

    def open(self):
        """Function which opens barbershop."""
        print("Barbershop is open with queue size of {0}".format(self.q_size))
        self.__process.start()

    def work(self):
        """Function which controls queue."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():
                self.mutex.release()
                work_result = self.__worker.sleep()
                if not work_result:
                    print("Barbershop closes")
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.work(client)

    def enter(self, client: Client):
        """Function which controls enters of clients.

        Args:
            client: Client - a client of the barbershop.
        """
        with self.mutex:
            print("Client {0} has entered a barbershop".format(client.name))
            if self.__queue.full():
                print("Client {0} sees full queue and leaves".format(client.name))
            else:
                self.__queue.put(client)
                self.__worker.call()
