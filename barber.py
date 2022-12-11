"""Home work about barber's problem."""
from multiprocessing import Process, Queue, Event, Semaphore, Barrier
from random import randint
from faker import Faker
from time import sleep


class WrongName(Exception):
    """This is representation of wrong name."""

    def __init__(self, name: str) -> None:
        """Initalization method.

        Args:
            name (str): smbd's wrong name.
        """
        super().__init__(name)
        self.name = name

    def __str__(self):
        """Exception in special format."""
        return "Imposible to create with name {0}".format(self.name)


class Client:
    """This is representation of berbershop's client."""

    def __init__(self, name: str) -> None:
        """Initalization method.

        Args:
            name (str): client's name.

        Raises:
            WrongName: if name isn't string .
        """
        self.name = name
        if not self.is_valid():
            raise WrongName(self.name)

    def is_valid(self) -> bool:
        """Check client.

        Returns:
            bool: True if he has normal name  else False.
        """
        return isinstance(self.name, str) and not self.name.isdigit()


class Barber:
    """This is representation of berbershop's worker."""

    TIMEOUT = 10
    WORK_INTERVAL = (9, 10)

    def __init__(self, name: str) -> None:
        """Initalization method.

        Args:
            name (str): barber's name.
        """
        self.name = name
        self.status = "came_to_work"
        self.__client_came = Event()

    def rest(self) -> bool:
        """Representation of barber's rest.

        Returns:
            bool: True if worker wake up else False.
        """
        if self.status != "is_sleeping":
            print("Barber {0} sleep.".format(self.name))
            self.status = "is_sleeping"
        return self.__client_came.wait(timeout=Barber.TIMEOUT)

    def call(self) -> None:
        """Representation of barber's call."""
        self.status = "called"
        self.__client_came.set()

    def do_haircut(self, client: Client) -> None:
        """Representation of client's trim. Sleep random time from WORK_INTERVAL.

        Args:
            client (Client): client who want's to trim.
        """
        print("{0} is cutting {1} hairs".format(self.name, client.name))
        self.status = "is_working"
        sleep(randint(*Barber.WORK_INTERVAL))

    def greet(self, client: Client) -> None:
        """Representation of client's greeting.

        Args:
            client (Client): client who we greet.
        """
        self.__client_came.clear()
        self.do_haircut(client)
        print("Client {0} is done by {1}".format(client.name, self.name))

    def bug(self) -> None:
        """Fix barber's bug."""
        self.__client_came.clear()


class Barbershop:
    """This is representation of berbershop."""

    NUMBER_OF_WORKERS = 100

    def __init__(self, q_size: int) -> None:
        """Initalization method.

        Args:
            q_size (int): siqe of queue.
        """
        fake = Faker()
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__workers = [Barber(fake.name()) for _ in range(Barbershop.NUMBER_OF_WORKERS)]
        self.__processes = [Process(target=self.work, args=(worker,)) for worker in self.__workers]
        self.mutex = Semaphore(Barbershop.NUMBER_OF_WORKERS)
        self.departed = Barrier(Barbershop.NUMBER_OF_WORKERS + 1)
        Process(target=self.close).start()

    def open(self) -> None:
        """Representation of barbershop's open."""
        print("Barber shop is open with the number of seats {0}".format(self.q_size))
        for proc in self.__processes:
            proc.start()

    def exit(self, name: str) -> None:
        """Representation of exiting barber's from the barbershop.

        Args:
            name (str): barber's name.
        """
        print("Barber {0} left from barbershop.".format(name))

    def close(self) -> None:
        """Representation of barbershop's close."""
        self.departed.wait()
        print("Barbershop close")

    def work(self, worker: Barber) -> None:
        """Representation of barbershop's working.

        Args:
            worker (Barber): barber who will trim.
        """
        while True:
            self.mutex.acquire()
            print(worker.name)
            if self.__queue.empty():
                self.mutex.release()
                if worker.rest():
                    worker.bug()
                    continue
                self.exit(worker.name)
                self.departed.wait()
                break
            else:
                self.mutex.release()
                client = self.__queue.get()
                worker.greet(client)

    def enter(self, client: Client):
        """Representation of client's enter.

        Args:
            client (Client): client who enter.
        """
        with self.mutex:
            print("Client {0} has entered a barbershop".format(client.name))
            if self.__queue.full():
                print("Client {0} sees full queue and leaves".format(client.name))
            else:
                print("Client {0} wants to cut his hair ".format(client.name))
                self.__queue.put(client)
                for worker in self.__workers:
                    worker.call()


SIZE_QUEUE = 4
ENTER_TIME_INTERVAL = (2, 3)
NUMBER_OF_CLIENTS = 8

if __name__ == '__main__':
    fake = Faker()
    clients = [Client(fake.name()) for _ in range(NUMBER_OF_CLIENTS)]
    barbershop = Barbershop(SIZE_QUEUE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
