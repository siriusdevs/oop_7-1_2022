"""Write how the barber works using processes."""

from multiprocessing import Event, Lock, Process, Queue
from random import randint
from time import sleep


class Client:
    """Representation of a client.

    Attributes:
    name(str): name of the client
    """

    def __init__(self, name: str):
        """Initialize the client.

        Args:
            name(str): name of the client
        """
        self.name = name

    def is_valid(self):
        """Check condition of client's existence.

        Returns:
            bool: if name is a string
        """
        return isinstance(self.name, str)

    def __str__(self) -> str:
        """Represent the object as a string.

        Returns:
            str: that client 'name' gets a haircut
        """
        return '{0} GETS a haircut'.format(self.name)


class Barber:
    """Representation of a barber."""

    timeout = 20
    work_interval = (2, 4)

    def __init__(self) -> None:
        """Initialize the barber."""
        self.__client_came = Event()

    def sleep(self):
        """Make the barber sleep until the client comes.

        Returns:
            bool: if the client comes or the timeout works
        """
        print('Barber sleeps')
        return self.__client_came.wait(timeout=Barber.timeout)

    def call(self):
        """Call the barber if the client comes."""
        self.__client_came.set()   # устанавливает в True, что клиент пришел

    def cut_hair(self, client: Client):
        """Spend time on cutting hair to the client.

        Args:
            client(Client): the name of the client that gets a haircut
        """
        sleep(randint(*Barber.work_interval))
        print('Barber cuts hair to {0}'.format(client.name))

    def greet(self, client: Client):
        """Greet the client from the queue.

        Args:
            client(Client): the name of the client
        """
        print('Barber greets {0}'.format(client.name))
        self.__client_came.clear()
        self.cut_hair(client)
        print('Client {0} is done'.format(client.name))


class Barbershop:
    """Representation of a barbershop."""

    def __init__(self, q_size: int) -> None:
        """Initialize the barbershop.
        
        Args:
            q_size(int): size of the queue in the barbershop
        """
        self.q_size = q_size
        self.__queue = Queue(maxsize=q_size)
        self.__worker = Barber()
        self.__process = Process(target=self.work)
        # делаем их скрытыми, чтобы снаружи никто не обращался
        self.mutex = Lock()

    def open(self):
        """Inform us when the barbershop opens."""
        print('Barbershop opens with queue size of {0}'.format(self.q_size))
        self.__process.start()

    def close(self):
        """Inform us when the barbershop closes."""
        print('Barbershop closes')

    def work(self):
        """Work when the client comes."""
        while True:
            self.mutex.acquire()
            if self.__queue.empty():   # если очередь пустая
                self.mutex.release()
                work_result = self.__worker.sleep()
                if not work_result:  # если вернул False, те сработал timeout
                    self.close()  # парикмахерская закрывается
                    break
            else:
                self.mutex.release()
                client = self.__queue.get()
                self.__worker.greet(client)  # работает с клиентом

    def enter(self, client: Client):
        """Put the client into the queue.

        Args:
            client(Client): the name of the client that enters the barbershop
        """
        with self.mutex:
            print('Client {0} has entered the barbershop'.format(client.name))
            if self.__queue.full():
                print('Client {0} sees full queue, leaves'.format(client.name))
            else:
                self.__queue.put(client)
                self.__worker.call()


SIZE_QUEUE = 1
ENTER_TIME_INTERVAL = (1, 5)

CLIENTS = [
    'Vladislav',
    'Victor',
    'Kirill',
    'Albert',
    'Yaroslav',
]

if __name__ == '__main__':
    clients = [Client(str(cl)) for cl in CLIENTS]
    barbershop = Barbershop(SIZE_QUEUE)
    barbershop.open()
    for client in clients:
        barbershop.enter(client)
        sleep(randint(*ENTER_TIME_INTERVAL))
